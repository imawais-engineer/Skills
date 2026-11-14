# Skills

Open-source skill library for **software development with AI**.

**Muhammad Awais**  
Forward Deployed AI Engineer

Version 2.0.0 is the public release. It is licensed under the [MIT License](LICENSE).

Skills live under `skills/`. Folder names are phases. Priority is not in the folder names. It was read from each skill and is recorded in [TREE.md](TREE.md). [GLOBAL_SKILL_ROUTER.md](GLOBAL_SKILL_ROUTER.md) is the routing guide. Read the skill before writing code.

Hackathon skills are not in this tree. They are on branch `cursor/hackathon-skills-beaf`.

## Order of use

1. `sdlc-best-practices` — discovery and an approved SRS. Nothing else is allowed to invent requirement IDs.
2. `project-foundations-and-architecture` — platform, stack, access, and privacy. Confirmed before the SRS is closed and before any file.
3. `app-global-preferences` — defaults only where the user, the SRS, and the Foundations Record are silent.
4. `complete-app-blueprint` — pages, flows, roles, data, and APIs.
5. `dashboard-first-ui` — the product screen, every state.
6. `functional-prototype-first` — the core workflow, with mock data allowed.
7. `data-persistence-design` — schema and access rules, then replace the mock data.
8. `ai-app-builder` — only when AI is the product.
9. `prompt-engineering-system` — prompts for that AI job.
10. `agent-workflow-design` — only when a fixed workflow is not enough.
11. `encapsulation-backend-config` — public surfaces hide backend detail.
12. `security-first-review` — findings, after the prototype works.
13. `stable-release-hardening` — auth, tests, and the release gate. It consumes the findings.
14. `deploy-and-document` — deploy and write the docs after the gate.

The reasons for this order, including where it differs from a simple top-to-bottom sketch, are in [TREE.md](TREE.md).

## Layout

```text
Skills/
├── LICENSE
├── GLOBAL_SKILL_ROUTER.md
├── README.md
├── TREE.md
├── CHANGELOG.md
└── skills/
    ├── foundational/
    ├── design-and-prototype/
    ├── data-and-persistence/
    ├── ai-systems/
    ├── hardening-and-release/
    └── deployment-and-documentation/
```

Each skill folder contains `SKILL.md`. AI skills also contain `agents/openai.yaml`. A few earlier skills still carry that file.

A skill that does not belong in the priority list goes under `skills/unsorted/`. There are none today.

## Use a skill

```bash
git clone https://github.com/imawais-engineer/Skills.git
cd Skills
```

The gate skill is [skills/foundational/sdlc-best-practices/SKILL.md](skills/foundational/sdlc-best-practices/SKILL.md).

To install one skill where Codex discovers flat folders:

```bash
mkdir -p "${HOME}/.codex/skills"
ln -sfn "$(pwd)/skills/foundational/sdlc-best-practices" "${HOME}/.codex/skills/sdlc-best-practices"
```

Install the whole professional library the same way. The folder name must stay equal to the `name` in that skill's frontmatter.

```bash
mkdir -p "${HOME}/.codex/skills"
find skills -mindepth 2 -maxdepth 2 -type d | while read -r dir; do
  ln -sfn "$(realpath "$dir")" "${HOME}/.codex/skills/$(basename "$dir")"
done
```

In Cursor, point the agent at the same `SKILL.md`. Do not keep a second edited copy in this repo.

## Check the tree

```bash
python3 scripts/validate_skills.py
```

The script checks frontmatter, unique names, the priority order in [TREE.md](TREE.md) and [GLOBAL_SKILL_ROUTER.md](GLOBAL_SKILL_ROUTER.md), the paths those files name, and relative links.

## Security

Do not commit credentials, tokens, or `.env` files. See [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE). Copyright (c) 2026 Muhammad Awais.

You may use, copy, modify, and distribute these skills, including in commercial work. Keep the copyright notice and license text with the copies you distribute.

**GitHub:** [imawais-engineer/Skills](https://github.com/imawais-engineer/Skills)
