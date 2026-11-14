# Skills

Canonical skill library for AI-assisted software work: discovery, architecture, design, persistence, AI systems, hardening, deployment, and hackathons.

The library has one arrangement. Skills live under `by-phase/`, in the order a project is built. [TREE.md](TREE.md) is the priority index. [GLOBAL_SKILL_ROUTER.md](GLOBAL_SKILL_ROUTER.md) is the routing guide. Read the skill before writing code.

## Order of use

Start at the top. Later phases do not replace the gate.

1. `sdlc-best-practices` — discovery and an approved SRS before any code.
2. `app-global-preferences` — stack, build order, UI, security, and docs defaults.
3. `project-foundations-and-architecture` — platform, access, and privacy decisions.
4. `complete-app-blueprint` — pages, flows, roles, data, and APIs.
5. `dashboard-first-ui` — dashboard-first UI.
6. `functional-prototype-first` — core workflow before auth or secondary features.
7. `data-persistence-design` — schema, storage, migrations, and ownership.
8. `ai-app-builder` — only when AI is core.
9. `prompt-engineering-system` — prompts as versioned components.
10. `agent-workflow-design` — only when the product needs agents.
11. `stable-release-hardening` — tests, auth, and the release gate.
12. `security-first-review` — security review before release.
13. `encapsulation-backend-config` — keep secrets and backend detail off the public surface.
14. `deploy-and-document` — deploy and write the docs.
15. `hackathon-project-system` through `hackathon-submission-packager` — competition intake, then build and submit.

Full when-to-use notes and the three standard sequences (app, AI app, hackathon) are in [TREE.md](TREE.md).

## Layout

```text
Skills/
├── GLOBAL_SKILL_ROUTER.md
├── README.md
├── TREE.md
├── CHANGELOG.md
└── by-phase/
    ├── 01-foundation/
    ├── 02-design-and-prototype/
    ├── 03-data-and-persistence/
    ├── 04-ai-systems/
    ├── 05-hardening-and-release/
    ├── 06-deployment-and-documentation/
    ├── 07-hackathon-intake-and-strategy/
    └── 08-hackathon-build-and-submit/
```

Each skill folder contains `SKILL.md`. AI and hackathon skills also contain `agents/openai.yaml`. A few earlier skills still carry that file as well.

A skill that is not part of this priority tree belongs under `by-phase/99-unsorted/`. There are none today.

## Use a skill

Clone the repo and open the skill for the phase you are in:

```bash
git clone https://github.com/imawais-engineer/Skills.git
cd Skills
```

The gate skill is [by-phase/01-foundation/sdlc-best-practices/SKILL.md](by-phase/01-foundation/sdlc-best-practices/SKILL.md).

To install one skill where Codex discovers flat skill folders, symlink it out of the repo:

```bash
mkdir -p "${HOME}/.codex/skills"
ln -sfn "$(pwd)/by-phase/01-foundation/sdlc-best-practices" "${HOME}/.codex/skills/sdlc-best-practices"
```

Install the whole library the same way. The folder name must stay equal to the `name` in that skill's frontmatter.

```bash
mkdir -p "${HOME}/.codex/skills"
find by-phase -mindepth 2 -maxdepth 2 -type d | while read -r dir; do
  ln -sfn "$(realpath "$dir")" "${HOME}/.codex/skills/$(basename "$dir")"
done
```

In Cursor, point the agent at the same `SKILL.md`, or copy the skill folder into the project skills directory you already use. Do not keep a second edited copy in this repo.

## Check the tree

```bash
python3 scripts/validate_skills.py
```

The script checks frontmatter, unique names, the priority order in [TREE.md](TREE.md) and [GLOBAL_SKILL_ROUTER.md](GLOBAL_SKILL_ROUTER.md), paths those files name, and relative links. It uses the Python standard library only.

## Security

Do not commit credentials, tokens, or `.env` files. See [SECURITY.md](SECURITY.md).

## License

Add the project's chosen license here before distributing the repository publicly.

**GitHub:** [imawais-engineer/Skills](https://github.com/imawais-engineer/Skills)
