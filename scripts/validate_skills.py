#!/usr/bin/env python3
"""Validate the hackathon compilation under skills/.

Stdlib only. Checks:
- every SKILL.md has YAML frontmatter with name and description
- name matches the skill folder and is unique
- TREE.md and GLOBAL_SKILL_ROUTER.md priority tables match the priority tree
- every concrete path those two files reference exists
- the directory tree in TREE.md exists and lists skills in priority order
- relative Markdown links in the repo resolve
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Hackathon compilation. Order is the first time each skill is read.
PRIORITY: list[tuple[int, str, str]] = [
    (1, "hackathon-project-system", "intake"),
    (2, "hackathon-brief-analyzer", "intake"),
    (3, "sdlc-best-practices", "intake"),
    (4, "hackathon-judging-strategy", "decision"),
    (5, "hackathon-compliance-review", "decision"),
    (6, "project-foundations-and-architecture", "decision"),
    (7, "hackathon-resource-planner", "decision"),
    (8, "app-global-preferences", "decision"),
    (9, "complete-app-blueprint", "plan"),
    (10, "hackathon-build-roadmap", "plan"),
    (11, "dashboard-first-ui", "build"),
    (12, "functional-prototype-first", "build"),
    (13, "data-persistence-design", "build"),
    (14, "ai-app-builder", "build"),
    (15, "prompt-engineering-system", "build"),
    (16, "agent-workflow-design", "build"),
    (17, "encapsulation-backend-config", "harden"),
    (18, "security-first-review", "harden"),
    (19, "stable-release-hardening", "harden"),
    (20, "hackathon-demo-pitch", "submit"),
    (21, "deploy-and-document", "submit"),
    (22, "hackathon-submission-packager", "submit"),
]

PRIORITY_ROW = re.compile(
    r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*`?([a-z0-9-]+)`?\s*\|"
)
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
MD_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)|!\[[^\]]*\]\(([^)]+)\)")
FENCE = re.compile(r"```[^\n]*\n(.*?)```", re.DOTALL)
CONCRETE_PATH = re.compile(
    r"^(?:skills|scripts)(?:/[A-Za-z0-9_.-]+)*/?$|^(?:README|TREE|CHANGELOG|SECURITY|GLOBAL_SKILL_ROUTER)\.md$"
)
UNSORTED_PHASE = "unsorted"


def skill_path(phase: str, name: str) -> Path:
    return ROOT / "skills" / phase / name / "SKILL.md"


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = FRONTMATTER.match(text)
    if match is None:
        return None
    data: dict[str, str] = {}
    current: str | None = None
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if line[:1] in " \t":
            if current is not None:
                data[current] = (data[current] + " " + line.strip()).strip()
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        current = key.strip()
        data[current] = value.strip().strip("\"'")
    return data


def parse_priority_table(text: str) -> list[tuple[int, str, str]]:
    rows: list[tuple[int, str, str]] = []
    for line in text.splitlines():
        match = PRIORITY_ROW.match(line)
        if match is None:
            continue
        rows.append((int(match.group(1)), match.group(2).strip(), match.group(3).strip()))
    return rows


def strip_fences(text: str) -> str:
    return FENCE.sub("", text)


def parse_directory_tree(text: str) -> list[tuple[str, bool]]:
    block = None
    for candidate in FENCE.findall(text):
        if re.search(r"(?m)^Skills/\s*$", candidate):
            block = candidate
            break
    if block is None:
        return []

    nodes: list[tuple[int, str, bool]] = []
    for line in block.splitlines():
        if not line.strip():
            continue
        cleaned = re.sub(r"[│├└─]", " ", line).split("←", 1)[0].rstrip()
        if not cleaned.strip():
            continue
        indent = len(cleaned) - len(cleaned.lstrip(" "))
        token = cleaned.strip()
        is_dir = token.endswith("/")
        nodes.append((indent, token.rstrip("/"), is_dir))

    stack: list[tuple[int, str]] = []
    paths: list[tuple[str, bool]] = []
    for indent, name, is_dir in nodes:
        while stack and stack[-1][0] >= indent:
            stack.pop()
        parts = [item for _, item in stack] + [name]
        if parts and parts[0] == "Skills":
            parts = parts[1:]
        rel = "/".join(parts)
        if rel:
            paths.append((rel, is_dir))
        if is_dir:
            stack.append((indent, name))
    return paths


def concrete_backtick_paths(text: str) -> list[str]:
    found: list[str] = []
    for token in re.findall(r"`([^`\n]+)`", strip_fences(text)):
        token = token.strip()
        if CONCRETE_PATH.fullmatch(token):
            found.append(token)
    return found


def check_frontmatter(errors: list[str]) -> dict[str, Path]:
    names: dict[str, Path] = {}
    skill_files = sorted((ROOT / "skills").glob("*/*/SKILL.md"))
    if not skill_files:
        errors.append("no SKILL.md files under skills/")
        return names
    for path in skill_files:
        folder = path.parent.name
        phase = path.parent.parent.name
        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        rel = path.relative_to(ROOT)
        if meta is None:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        name = meta.get("name", "").strip()
        description = meta.get("description", "").strip()
        if not name:
            errors.append(f"{rel}: frontmatter missing name")
        if not description:
            errors.append(f"{rel}: frontmatter missing description")
        if name and name != folder:
            errors.append(f"{rel}: name {name!r} does not match folder {folder!r}")
        if name:
            if name in names:
                errors.append(f"duplicate skill name {name!r}: {names[name].relative_to(ROOT)} and {rel}")
            else:
                names[name] = path
        if phase != UNSORTED_PHASE:
            expected = next((item for item in PRIORITY if item[1] == folder), None)
            if expected is None:
                errors.append(f"{rel}: skill is not in the priority tree; move it to skills/{UNSORTED_PHASE}/")
            elif expected[2] != phase:
                errors.append(f"{rel}: phase is {phase}, priority tree places it in {expected[2]}")
    return names


def check_priority_documents(errors: list[str]) -> None:
    for filename in ("TREE.md", "GLOBAL_SKILL_ROUTER.md"):
        path = ROOT / filename
        if not path.is_file():
            errors.append(f"missing {filename}")
            continue
        rows = parse_priority_table(path.read_text(encoding="utf-8"))
        if rows != PRIORITY:
            errors.append(f"{filename}: priority table does not match the priority tree")
            errors.append(f"  expected {len(PRIORITY)} rows, found {len(rows)}")
            for got, want in zip(rows, PRIORITY):
                if got != want:
                    errors.append(f"  found {got}, expected {want}")
                    break
            if len(rows) != len(PRIORITY):
                extra = rows[len(PRIORITY):] or PRIORITY[len(rows):]
                errors.append(f"  length mismatch near {extra[:3]}")


def check_referenced_paths(errors: list[str]) -> None:
    for filename in ("TREE.md", "GLOBAL_SKILL_ROUTER.md"):
        path = ROOT / filename
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for rel in concrete_backtick_paths(text):
            if not (ROOT / rel).exists():
                errors.append(f"{filename}: missing path `{rel}`")
        if filename == "TREE.md":
            tree = parse_directory_tree(text)
            if not tree:
                errors.append("TREE.md: directory tree block was not found")
                continue
            skills_by_phase: dict[str, list[str]] = {}
            for rel, is_dir in tree:
                target = ROOT / rel
                if not target.exists():
                    errors.append(f"TREE.md tree: missing {rel}")
                    continue
                if is_dir and not target.is_dir():
                    errors.append(f"TREE.md tree: {rel} is not a directory")
                if not is_dir and not target.is_file():
                    errors.append(f"TREE.md tree: {rel} is not a file")
                parts = Path(rel).parts
                if is_dir and len(parts) == 3 and parts[0] == "skills" and parts[1] != UNSORTED_PHASE:
                    skills_by_phase.setdefault(parts[1], []).append(parts[2])
            expected_by_phase: dict[str, list[str]] = {}
            for _, name, phase in PRIORITY:
                expected_by_phase.setdefault(phase, []).append(name)
            if skills_by_phase != expected_by_phase:
                errors.append("TREE.md directory tree skill order does not match the priority tree")
                for phase, names in expected_by_phase.items():
                    if skills_by_phase.get(phase) != names:
                        errors.append(f"  {phase}: tree={skills_by_phase.get(phase)} expected={names}")


def check_relative_links(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for match in MD_LINK.finditer(text):
            raw = match.group(1) or match.group(2) or ""
            raw = raw.strip()
            if not raw or raw.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = raw.split()[0]
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link {raw!r} escapes the repo")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken relative link {raw!r}")


def check_disk_coverage(errors: list[str], names: dict[str, Path]) -> None:
    expected_names = {name for _, name, _ in PRIORITY}
    missing = expected_names - set(names)
    for name in sorted(missing):
        errors.append(f"priority skill {name} has no SKILL.md")
    for _, name, phase in PRIORITY:
        path = skill_path(phase, name)
        if not path.is_file():
            errors.append(f"missing {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    priorities = [item[0] for item in PRIORITY]
    skill_names = [item[1] for item in PRIORITY]
    if priorities != list(range(1, len(PRIORITY) + 1)):
        errors.append("priority numbers are not contiguous from 1")
    if len(skill_names) != len(set(skill_names)):
        errors.append("priority tree contains a duplicate skill name")

    names = check_frontmatter(errors)
    check_disk_coverage(errors, names)
    check_priority_documents(errors)
    check_referenced_paths(errors)
    check_relative_links(errors)

    if errors:
        print(f"FAILED: {len(errors)} problem(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    phases = []
    for _, _, phase in PRIORITY:
        if phase not in phases:
            phases.append(phase)
    print("OK: skill tree matches the priority order")
    print(f"OK: {len(names)} SKILL.md files, names unique and equal to their folders")
    print(f"OK: TREE.md and GLOBAL_SKILL_ROUTER.md priority tables match 1-{len(PRIORITY)}")
    print("OK: referenced paths exist and relative links resolve")
    print("Order:")
    for number, name, phase in PRIORITY:
        print(f"  {number:2}. {phase}/{name}")
    print(f"Phases: {', '.join(phases)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
