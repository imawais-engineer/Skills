# Skills — professional tree

This is the public professional library, version 2.0.0, released under the MIT License. Competition skills are not here. They are on branch `cursor/hackathon-skills-beaf`.

Folder names describe the phase. They are not numbered. Priority was set by reading each skill's required inputs, one by one. The sketch order was the shape, not the sequence.

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

## Sequences

### Product

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

### AI product

Run the product sequence, and when AI is the core job insert, after the data skill:

1. `ai-app-builder`
2. `prompt-engineering-system`
3. `agent-workflow-design` only if an agent is justified

Then continue with encapsulation, security review, release hardening, and deploy.

## Directory

```
Skills/
├── LICENSE
├── GLOBAL_SKILL_ROUTER.md
├── README.md
├── TREE.md
└── skills/
    ├── foundational/
    │   ├── sdlc-best-practices/
    │   ├── project-foundations-and-architecture/
    │   ├── app-global-preferences/
    │   └── complete-app-blueprint/
    ├── design-and-prototype/
    │   ├── dashboard-first-ui/
    │   └── functional-prototype-first/
    ├── data-and-persistence/
    │   └── data-persistence-design/
    ├── ai-systems/
    │   ├── ai-app-builder/
    │   ├── prompt-engineering-system/
    │   └── agent-workflow-design/
    ├── hardening-and-release/
    │   ├── encapsulation-backend-config/
    │   ├── security-first-review/
    │   └── stable-release-hardening/
    └── deployment-and-documentation/
        └── deploy-and-document/
```

Each skill folder contains `SKILL.md`. `agents/openai.yaml` is present on the AI skills and on the skills that already carried it.

A skill that is not in this priority list belongs in an unsorted folder under skills. There are none.

Routing detail is in [GLOBAL_SKILL_ROUTER.md](GLOBAL_SKILL_ROUTER.md).
