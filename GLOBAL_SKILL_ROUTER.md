# Global Skill Router

Use this file to choose the skill to read before planning, building, reviewing, or submitting. [TREE.md](TREE.md) is the priority index. The only skill library is [by-phase/](by-phase).

On a new product, start at priority 1. The standard sequences later in this file are the build order after that gate, and they match [TREE.md](TREE.md).

## Priority Order

| Priority | Skill | Phase | When to use |
| --- | --- | --- | --- |
| 1 | `sdlc-best-practices` | 01-foundation | Gate skill. Forces full discovery discussion + complete SRS before any code. |
| 2 | `app-global-preferences` | 01-foundation | Apply personal/global development preferences (stack, order, security, docs). |
| 3 | `project-foundations-and-architecture` | 01-foundation | Lock platform, stack, access model, privacy baseline. |
| 4 | `complete-app-blueprint` | 01-foundation | Expand idea into full software blueprint (pages, flows, roles, data, APIs). |
| 5 | `dashboard-first-ui` | 02-design-and-prototype | Dashboard-first UI standards, layouts, navigation, themes. |
| 6 | `functional-prototype-first` | 02-design-and-prototype | Build core functional app before auth, hardening, or secondary features. |
| 7 | `data-persistence-design` | 03-data-and-persistence | Schema, storage, migrations, RLS, ownership rules. |
| 8 | `ai-app-builder` | 04-ai-systems | AI-native application architecture. |
| 9 | `prompt-engineering-system` | 04-ai-systems | Structured prompt engineering. |
| 10 | `agent-workflow-design` | 04-ai-systems | Agent workflows (use only if agentic behavior needed). |
| 11 | `stable-release-hardening` | 05-hardening-and-release | Testing, auth, authorization, quality gates after prototype works. |
| 12 | `security-first-review` | 05-hardening-and-release | Security review before stable release. |
| 13 | `encapsulation-backend-config` | 05-hardening-and-release | Hide secrets, env vars, backend details from UI/API. |
| 14 | `deploy-and-document` | 06-deployment-and-documentation | VPS/Vercel deploy, DNS, SSL, README, release notes. |
| 15 | `hackathon-project-system` | 07-hackathon-intake-and-strategy | Structure the hackathon project. |
| 16 | `hackathon-brief-analyzer` | 07-hackathon-intake-and-strategy | Analyze brief, rules, constraints. |
| 17 | `hackathon-judging-strategy` | 07-hackathon-intake-and-strategy | Align with judging criteria. |
| 18 | `hackathon-resource-planner` | 07-hackathon-intake-and-strategy | Plan time, team, tools. |
| 19 | `hackathon-build-roadmap` | 08-hackathon-build-and-submit | Implementation roadmap for competition. |
| 20 | `hackathon-compliance-review` | 08-hackathon-build-and-submit | Verify rules compliance. |
| 21 | `hackathon-demo-pitch` | 08-hackathon-build-and-submit | Demo flow, pitch narrative, judging evidence. |
| 22 | `hackathon-submission-packager` | 08-hackathon-build-and-submit | Final submission package checklist. |

Canonical file for priority 1: `by-phase/01-foundation/sdlc-best-practices/SKILL.md`.

## Fast Routing

| User request | Start with | Then add |
| --- | --- | --- |
| New product, vague idea, or "build an app" | `sdlc-best-practices` | `app-global-preferences`, `project-foundations-and-architecture`, `complete-app-blueprint` |
| "Plan a full product" | `complete-app-blueprint` | `data-persistence-design`, `stable-release-hardening`, `deploy-and-document` |
| "Make the UI/dashboard" | `dashboard-first-ui` | `functional-prototype-first` |
| "Implement the prototype" | `functional-prototype-first` | `dashboard-first-ui`, `data-persistence-design` |
| "Design database/storage" | `data-persistence-design` | `stable-release-hardening` when auth, RLS, or security is needed |
| "Build an AI app" | `ai-app-builder` | `prompt-engineering-system`, `agent-workflow-design`, `security-first-review` |
| "Design prompts" | `prompt-engineering-system` | `ai-app-builder` when prompts are part of a product |
| "Design an agent workflow" | `agent-workflow-design` | `prompt-engineering-system`, `security-first-review` |
| "Prepare for stable release" | `stable-release-hardening` | `security-first-review`, `deploy-and-document` |
| "Review security" | `security-first-review` | `encapsulation-backend-config`, `stable-release-hardening` |
| "Hide backend config from UI/API" | `encapsulation-backend-config` | `security-first-review` |
| "Deploy/document" | `deploy-and-document` | `stable-release-hardening` |
| "Build for a hackathon" | `hackathon-project-system` | The rest of the hackathon sequence |
| "Parse hackathon brief" | `hackathon-brief-analyzer` | `hackathon-judging-strategy`, `hackathon-resource-planner` |
| "Optimize for judging" | `hackathon-judging-strategy` | `hackathon-demo-pitch` |
| "Create hackathon roadmap" | `hackathon-build-roadmap` | `hackathon-compliance-review` |
| "Check hackathon rules" | `hackathon-compliance-review` | `hackathon-submission-packager` |
| "Prepare pitch/demo" | `hackathon-demo-pitch` | `hackathon-submission-packager` |
| "Prepare submission" | `hackathon-submission-packager` | `hackathon-compliance-review` |

AI skills are used only when AI is the product or the task explicitly needs them. Hackathon skills are used when a brief, rubric, rule set, or submission package is in play. A hackathon app also uses the relevant app and AI skills.

## Standard App Sequence

1. `app-global-preferences`
2. `complete-app-blueprint`
3. `dashboard-first-ui`
4. `functional-prototype-first`
5. `data-persistence-design`
6. `stable-release-hardening`
7. `security-first-review`
8. `encapsulation-backend-config`
9. `deploy-and-document`

Run `sdlc-best-practices` and `project-foundations-and-architecture` before this sequence on a new product. They are priorities 1 and 3 in the table above.

## Standard AI App Sequence

1. `app-global-preferences`
2. `complete-app-blueprint`
3. `ai-app-builder`
4. `prompt-engineering-system`
5. `agent-workflow-design` only if agentic behavior is required
6. `data-persistence-design`
7. `stable-release-hardening`
8. `security-first-review`
9. `encapsulation-backend-config`
10. `deploy-and-document`

## Standard Hackathon Sequence

1. `hackathon-project-system`
2. `hackathon-brief-analyzer`
3. `hackathon-judging-strategy`
4. `hackathon-resource-planner`
5. `hackathon-build-roadmap`
6. `hackathon-compliance-review`
7. `hackathon-demo-pitch`
8. `hackathon-submission-packager`

If the hackathon project is an app, also use the relevant application skills. If it is AI-first, also use the AI skills.

## Install

Skills stay in this repo. Point an agent at a skill by giving it the `SKILL.md` path, or symlink the skill folder into a flat skills directory:

```bash
mkdir -p "${HOME}/.codex/skills"
ln -sfn "$(pwd)/by-phase/01-foundation/sdlc-best-practices" "${HOME}/.codex/skills/sdlc-best-practices"
```

That install path lives outside the repo. The copy inside the repo is `by-phase/01-foundation/sdlc-best-practices/SKILL.md`.

## Maintenance

When adding, renaming, or moving a skill:

1. Put the canonical folder under `by-phase/` in lifecycle order.
2. Add the skill to the priority table in [TREE.md](TREE.md) and in this file, in the same order.
3. Keep `name` in the skill frontmatter equal to the folder name.
4. Run `scripts/validate_skills.py`.
