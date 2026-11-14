# Changelog

## Unreleased (v2.0.0 proposed)

Proposed release: **v2.0.0**. The skill library now has one tree, `by-phase/`, ordered by [TREE.md](TREE.md). No tag and no GitHub release are part of this change.

### Added

- `TREE.md` records the priority order 1–22 and the app, AI app, and hackathon sequences.
- `scripts/validate_skills.py` checks frontmatter, folder names, duplicate names, priority order, referenced paths, and relative links.

### Changed

- Eleven skills now use the compiled SDLC Skills Hub text: `sdlc-best-practices`, `app-global-preferences`, `project-foundations-and-architecture`, `complete-app-blueprint`, `dashboard-first-ui`, `functional-prototype-first`, `data-persistence-design`, `stable-release-hardening`, `security-first-review`, `encapsulation-backend-config`, and `deploy-and-document`.
- Those files share the hub section order (purpose, when to use, inputs, procedure, deliverables, acceptance, verification, failure modes, prompt template, SRS traceability, definition of done). Their YAML `description` is the generic hub line, with `source` and `priority`. The specific trigger sentence remains in the body.
- `GLOBAL_SKILL_ROUTER.md` follows that same 1–22 order. Repo-relative paths replace `/home/awais/Skills/...`. `sdlc-best-practices` and `project-foundations-and-architecture` are in the router. The standard sequences are unchanged from [TREE.md](TREE.md).
- `README.md` documents the phase tree, the order of use, and how to read or symlink a skill.

### Removed

- `by-use-case/` . It was a symlink index of the same skills, and it is not part of the TREE arrangement. No skill lived only there, so nothing was moved to `by-phase/99-unsorted/`.

### Unchanged

- `ai-app-builder`, `prompt-engineering-system`, `agent-workflow-design`, and all eight hackathon skills already matched the compiled package, including `agents/openai.yaml`.
- Existing `agents/openai.yaml` files on non-package-shaped skills were kept. The compiled folders for those skills shipped `SKILL.md` only, and TREE says the agent file is included when it is present.
- `.github/workflows/security-scan.yml`, `SECURITY.md`, and `.gitignore`.

### Not a move

Every skill was already stored at its `by-phase/` path. This revamp does not `git mv` any skill. The old path and the new path are the same file.
