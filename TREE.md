# Hackathon compilation

This branch is the hackathon build library. It contains every professional skill from `main` and all eight hackathon skills. `main` stays the professional product library and does not include the competition skills.

The brief is the source of truth. Hackathon skills decide what to build and what the judges must see. The SDLC skills do the developmental work inside that frame. No application code until the brief has been turned into an approved specification.

`hackathon-compliance-review` is read before the project is chosen, and again before the first code, before the demo is recorded, and before the package is submitted. It has one folder. The repeats are gates, not extra copies.

AI skills are in the build stage and are used only when the brief requires AI or the product is an AI product.

## Priority

| Priority | Skill | Phase | Why this slot |
| --- | --- | --- | --- |
| 1 | `hackathon-project-system` | intake | Orchestrator. The brief is the source of truth, and this skill names the rest of the hackathon order. |
| 2 | `hackathon-brief-analyzer` | intake | Do not design first. Extract requirements, deliverables, rubric, resources, and rules. |
| 3 | `sdlc-best-practices` | intake | Turn those facts into an SRS with requirement IDs. No code until that specification is approved. |
| 4 | `hackathon-judging-strategy` | decision | Choose the idea that can become a complete demo and score on the rubric. |
| 5 | `hackathon-compliance-review` | decision | Hard stops before a stack or a feature is locked: eligibility, banned tools, licenses, required deliverables. |
| 6 | `project-foundations-and-architecture` | decision | Lock platform, access, and privacy inside the rules. Confirm before any file. |
| 7 | `hackathon-resource-planner` | decision | Map required and allowed tools. Use the default stack only where the brief is silent. |
| 8 | `app-global-preferences` | decision | Fill leftover silence. Never override the brief, the rules, the SRS, or the foundations record. |
| 9 | `complete-app-blueprint` | plan | Map the pages, data, and APIs of the minimum winning demo. |
| 10 | `hackathon-build-roadmap` | plan | Timebox that blueprint. A working demo beats an unfinished larger system. |
| 11 | `dashboard-first-ui` | build | Specify the screens the demo must show before they are coded. |
| 12 | `functional-prototype-first` | build | First code. Prove the core workflow. Mock data is allowed. Auth waits unless it is the demo. |
| 13 | `data-persistence-design` | build | Replace mock data and add the integrations the brief or the demo requires. |
| 14 | `ai-app-builder` | build | Only when AI is required or is the product. |
| 15 | `prompt-engineering-system` | build | Prompts for that AI job. Skip when there is no AI job. |
| 16 | `agent-workflow-design` | build | Only when a fixed workflow is not enough. |
| 17 | `encapsulation-backend-config` | harden | The public demo must not show keys, env names, or provider internals. |
| 18 | `security-first-review` | harden | After the demo path works, before judges use it. |
| 19 | `stable-release-hardening` | harden | Tests and auth only to the depth the demo and the brief require. Uses the security findings. |
| 20 | `hackathon-demo-pitch` | submit | Show the problem, the working path, the required tools, and the rubric evidence. |
| 21 | `deploy-and-document` | submit | Live URL, repo, and setup the submission will point at. |
| 22 | `hackathon-submission-packager` | submit | Package only what the competition asks for, after the links work. |

## Hackathon sequence

1. `hackathon-project-system`
2. `hackathon-brief-analyzer`
3. `sdlc-best-practices`
4. `hackathon-judging-strategy`
5. `hackathon-compliance-review`
6. `project-foundations-and-architecture`
7. `hackathon-resource-planner`
8. `app-global-preferences`
9. `complete-app-blueprint`
10. `hackathon-build-roadmap`
11. `hackathon-compliance-review` again, before the first code
12. `dashboard-first-ui`
13. `functional-prototype-first`
14. `data-persistence-design`
15. `ai-app-builder`, `prompt-engineering-system`, and `agent-workflow-design` only when the brief or the product needs them
16. `encapsulation-backend-config`
17. `security-first-review`
18. `stable-release-hardening`
19. `hackathon-compliance-review` again, before the demo is recorded
20. `hackathon-demo-pitch`
21. `deploy-and-document`
22. `hackathon-compliance-review` again, before packaging
23. `hackathon-submission-packager`

## Directory

```
Skills/
├── LICENSE
├── GLOBAL_SKILL_ROUTER.md
├── README.md
├── TREE.md
└── skills/
    ├── intake/
    │   ├── hackathon-project-system/
    │   ├── hackathon-brief-analyzer/
    │   └── sdlc-best-practices/
    ├── decision/
    │   ├── hackathon-judging-strategy/
    │   ├── hackathon-compliance-review/
    │   ├── project-foundations-and-architecture/
    │   ├── hackathon-resource-planner/
    │   └── app-global-preferences/
    ├── plan/
    │   ├── complete-app-blueprint/
    │   └── hackathon-build-roadmap/
    ├── build/
    │   ├── dashboard-first-ui/
    │   ├── functional-prototype-first/
    │   ├── data-persistence-design/
    │   ├── ai-app-builder/
    │   ├── prompt-engineering-system/
    │   └── agent-workflow-design/
    ├── harden/
    │   ├── encapsulation-backend-config/
    │   ├── security-first-review/
    │   └── stable-release-hardening/
    └── submit/
        ├── hackathon-demo-pitch/
        ├── deploy-and-document/
        └── hackathon-submission-packager/
```

Routing detail is in [GLOBAL_SKILL_ROUTER.md](GLOBAL_SKILL_ROUTER.md).
