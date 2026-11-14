# Global Skill Router

Choose the skill to read before planning, building, or releasing. [TREE.md](TREE.md) is the priority index. The library is [skills/](skills).

This tree is the professional library. Hackathon skills are not in it. They are on branch `cursor/hackathon-skills-beaf`.

Priority was read from each skill, one by one. Folder names are phases. They do not encode the order.

## Priority

| Priority | Skill | Phase | Why this slot |
| --- | --- | --- | --- |
| 1 | `sdlc-best-practices` | foundational | SK-01. Creates the requirement IDs every other skill cites. No code until the SRS is approved. |
| 2 | `project-foundations-and-architecture` | foundational | SK-02. Needs discovery notes from SK-01. Confirmed record is written back into the SRS. No files before that confirmation. |
| 3 | `app-global-preferences` | foundational | SK-04. Requires the Foundations Record and the SRS. Fills silence only. Precedence is user, then SRS and foundations, then these defaults. |
| 4 | `complete-app-blueprint` | foundational | SK-03. Requires the confirmed Foundations Record and the SRS. Maps pages, entities, and capabilities before coding. |
| 5 | `dashboard-first-ui` | design-and-prototype | SK-05. Requires the blueprint page table. Designs the product screen before implementation. |
| 6 | `functional-prototype-first` | design-and-prototype | SK-06. First code. Requires the approved SRS and the blueprint. Mock data is allowed. Auth and hardening stay out of this pass. |
| 7 | `data-persistence-design` | data-and-persistence | SK-07. Schema, ownership, and access rules before persistence code. Replaces the prototype's mock data before release. |
| 8 | `ai-app-builder` | ai-systems | Use only when AI is the product. Defines the AI job after the normal workflow exists. |
| 9 | `prompt-engineering-system` | ai-systems | Prompts are components of the job defined by `ai-app-builder`. |
| 10 | `agent-workflow-design` | ai-systems | Use only when a deterministic workflow is not enough. |
| 11 | `encapsulation-backend-config` | hardening-and-release | SK-11. Constrains public UI and APIs as they are built. The security review applies this skill. |
| 12 | `security-first-review` | hardening-and-release | SK-12. After the prototype works, before release. Produces the findings the release gate requires. |
| 13 | `stable-release-hardening` | hardening-and-release | SK-13. Requires a passing prototype and the security findings. Auth and the V&V gate live here. |
| 14 | `deploy-and-document` | deployment-and-documentation | SK-14. Requires the V&V report. Last, unless the user asks for a labelled preview. |

Canonical gate file: `skills/foundational/sdlc-best-practices/SKILL.md`.

## How the order was decided

- `sdlc-best-practices` is first because every other skill traces to the requirement IDs it creates, and it blocks code until the SRS is approved.
- `project-foundations-and-architecture` is second, not third. It needs the discovery notes, and its confirmed record is an input to the rest of the SRS. The sketch listed preferences here. `app-global-preferences` cannot run yet: its required inputs are the Foundations Record and the SRS.
- `app-global-preferences` is third. It is a tie-breaker with explicit precedence: user decision, then SRS and foundations, then defaults.
- `complete-app-blueprint` is fourth. It refuses to map the product until both the record and the SRS exist.
- `dashboard-first-ui` precedes `functional-prototype-first` because the prototype implements the page table and the screen rules.
- `data-persistence-design` follows the prototype. The prototype may use mock data and a draft entity shape. This skill is the one that designs the store and removes that mock data before release.
- The three AI skills stay behind the data skill and stay optional. `ai-app-builder` defines the job. `prompt-engineering-system` writes the prompts for that job. `agent-workflow-design` is last, and only when a fixed workflow is not enough.
- Inside hardening, the old list put stable release first. The skills disagree. `stable-release-hardening` requires the security findings. `security-first-review` applies `encapsulation-backend-config`. Read encapsulation, then the review, then the release gate.
- `deploy-and-document` is last. It refuses a build that has not passed the release gate, unless the user asks for a labelled preview.

## Fast routing

| Request | Start with | Then |
| --- | --- | --- |
| New product or "build an app" | `sdlc-best-practices` | `project-foundations-and-architecture`, then `app-global-preferences`, then `complete-app-blueprint` |
| Platform, stack, access, or privacy is unset | `project-foundations-and-architecture` | Finish the SRS in `sdlc-best-practices` |
| A default is missing and the SRS is silent | `app-global-preferences` | Do not override a recorded decision |
| Pages, roles, data, and APIs are still vague | `complete-app-blueprint` | `dashboard-first-ui` |
| UI, layout, dashboard, tables, forms | `dashboard-first-ui` | `functional-prototype-first` |
| First implementation | `functional-prototype-first` | `data-persistence-design` when mock data must become real |
| Schema, migrations, RLS, ownership | `data-persistence-design` | `security-first-review` when access rules are the risk |
| The product is an AI app | `ai-app-builder` | `prompt-engineering-system`, then `agent-workflow-design` only if needed |
| Prompts or structured model output | `prompt-engineering-system` | `ai-app-builder` when the prompt is part of a product |
| An agent, tools, or human approval | `agent-workflow-design` | `security-first-review` |
| Public UI or API might show config or secrets | `encapsulation-backend-config` | `security-first-review` |
| Review security before release | `security-first-review` | `stable-release-hardening` |
| Prototype works and should become a release | `stable-release-hardening` | `deploy-and-document` |
| Deploy, DNS, SSL, README, release notes | `deploy-and-document` | Only after `stable-release-hardening`, or label the deploy as a preview |

## Product sequence

1. `sdlc-best-practices`
2. `project-foundations-and-architecture`
3. `app-global-preferences`
4. `complete-app-blueprint`
5. `dashboard-first-ui`
6. `functional-prototype-first`
7. `data-persistence-design`
8. `encapsulation-backend-config`
9. `security-first-review`
10. `stable-release-hardening`
11. `deploy-and-document`

## AI product sequence

1. `sdlc-best-practices`
2. `project-foundations-and-architecture`
3. `app-global-preferences`
4. `complete-app-blueprint`
5. `dashboard-first-ui`
6. `functional-prototype-first`
7. `data-persistence-design`
8. `ai-app-builder`
9. `prompt-engineering-system`
10. `agent-workflow-design` only if an agent is justified
11. `encapsulation-backend-config`
12. `security-first-review`
13. `stable-release-hardening`
14. `deploy-and-document`

## Install

Skills stay in this repo. Give an agent the `SKILL.md` path, or symlink one folder into a flat skills directory outside the repo:

```bash
mkdir -p "${HOME}/.codex/skills"
ln -sfn "$(pwd)/skills/foundational/sdlc-best-practices" "${HOME}/.codex/skills/sdlc-best-practices"
```

The copy inside the repo is `skills/foundational/sdlc-best-practices/SKILL.md`.

## Maintenance

1. Put the skill under `skills/` in the phase its inputs belong to.
2. Add it to the priority table in [TREE.md](TREE.md) and in this file, in the order its inputs require.
3. Keep `name` in the frontmatter equal to the folder name.
4. Run `scripts/validate_skills.py`.
