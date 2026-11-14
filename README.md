# Skills for hackathon builds

Compiled skill library for building hackathon applications with AI.

**Muhammad Awais**  
Forward Deployed AI Engineer

This branch joins the professional skills from `main` with the eight hackathon skills. Hackathon instructions decide the project. The SDLC skills do the developmental stages inside that decision. The public product library on `main` does not include the competition skills.

Licensed under the [MIT License](LICENSE).

Read [TREE.md](TREE.md) for the compiled order. [GLOBAL_SKILL_ROUTER.md](GLOBAL_SKILL_ROUTER.md) routes a request to the stage you are in. Start at [skills/intake/hackathon-project-system/SKILL.md](skills/intake/hackathon-project-system/SKILL.md). Do not write application code until `sdlc-best-practices` has an approved specification from the brief.

## Order of use

1. `hackathon-project-system` — the brief is the source of truth.
2. `hackathon-brief-analyzer` — extract requirements, rubric, resources, and rules before designing.
3. `sdlc-best-practices` — give those facts requirement IDs. This is the code gate.
4. `hackathon-judging-strategy` — pick a demo that can score.
5. `hackathon-compliance-review` — stop if eligibility, tools, or deliverables are unsafe. Read it again before code, before the demo, and before submission.
6. `project-foundations-and-architecture` — lock platform, access, and privacy inside the rules.
7. `hackathon-resource-planner` — map required and allowed tools.
8. `app-global-preferences` — defaults only where the brief is silent.
9. `complete-app-blueprint` — pages, data, and APIs for the minimum winning demo.
10. `hackathon-build-roadmap` — timebox the work. A finished demo beats a larger unfinished app.
11. `dashboard-first-ui` — the screens the judges must see.
12. `functional-prototype-first` — first code. Mock data is allowed.
13. `data-persistence-design` — real data and required integrations after the core path works.
14. `ai-app-builder` — only when the brief or the product is AI.
15. `prompt-engineering-system` — prompts for that job.
16. `agent-workflow-design` — only when a fixed workflow is not enough.
17. `encapsulation-backend-config` — the public demo hides keys and provider internals.
18. `security-first-review` — after the demo path works.
19. `stable-release-hardening` — tests and auth only as deep as the demo needs.
20. `hackathon-demo-pitch` — problem, working path, required tools, rubric evidence.
21. `deploy-and-document` — the URL and the setup judges will open.
22. `hackathon-submission-packager` — the package the competition actually asked for.

## Layout

```text
skills/
├── intake/
├── decision/
├── plan/
├── build/
├── harden/
└── submit/
```

Each skill folder contains `SKILL.md`. Hackathon skills and the AI skills also contain `agents/openai.yaml`.

## Use it

```bash
git clone https://github.com/imawais-engineer/Skills.git
cd Skills
git checkout hackathon-skills
```

Give the agent the skill for the stage you are in, or symlink the folders into `~/.codex/skills/` as shown in [GLOBAL_SKILL_ROUTER.md](GLOBAL_SKILL_ROUTER.md).

Check the compilation:

```bash
python3 scripts/validate_skills.py
```

## Security

Do not commit credentials, tokens, or `.env` files. See [SECURITY.md](SECURITY.md). A public demo still follows `encapsulation-backend-config`.

## License

[MIT](LICENSE). Copyright (c) 2026 Muhammad Awais.

**GitHub:** [imawais-engineer/Skills](https://github.com/imawais-engineer/Skills)
