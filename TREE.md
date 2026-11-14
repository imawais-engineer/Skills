# Skills Root — Compiled Tree with Priority & Order of Use

**Source:** https://github.com/imawais-engineer/Skills (canonical) + https://sdlc.base44.app/ (SDLC Skills Hub / SRS Architect themed)

**Compiled:** 2026-11-14

This is the single Skills root. All skills are organized under `by-phase/` with foundational and highest-priority skills at the top.

The structure follows the project's natural lifecycle. Foundational skills (especially SRS / discovery) come first so AI reads before it writes.

---

## Priority Order of Use (Foundation → Delivery)

### Tier 0 — Always Start Here (Gate / Preferences)
| Priority | Skill | Phase | When to Use |
|----------|-------|-------|-------------|
| 1 | `sdlc-best-practices` | 01-foundation | Gate skill. Forces full discovery discussion + complete SRS before any code. |
| 2 | `app-global-preferences` | 01-foundation | Apply personal/global development preferences (stack, order, security, docs). |
| 3 | `project-foundations-and-architecture` | 01-foundation | Lock platform, stack, access model, privacy baseline. |
| 4 | `complete-app-blueprint` | 01-foundation | Expand idea into full software blueprint (pages, flows, roles, data, APIs). |

### Tier 1 — Design & Prototype
| Priority | Skill | Phase | When to Use |
|----------|-------|-------|-------------|
| 5 | `dashboard-first-ui` | 02-design-and-prototype | Dashboard-first UI standards, layouts, navigation, themes. |
| 6 | `functional-prototype-first` | 02-design-and-prototype | Build core functional app before auth, hardening, or secondary features. |

### Tier 2 — Data & Persistence
| Priority | Skill | Phase | When to Use |
|----------|-------|-------|-------------|
| 7 | `data-persistence-design` | 03-data-and-persistence | Schema, storage, migrations, RLS, ownership rules. |

### Tier 3 — AI Systems (only when AI is core)
| Priority | Skill | Phase | When to Use |
|----------|-------|-------|-------------|
| 8 | `ai-app-builder` | 04-ai-systems | AI-native application architecture. |
| 9 | `prompt-engineering-system` | 04-ai-systems | Structured prompt engineering. |
| 10 | `agent-workflow-design` | 04-ai-systems | Agent workflows (use only if agentic behavior needed). |

### Tier 4 — Hardening & Release
| Priority | Skill | Phase | When to Use |
|----------|-------|-------|-------------|
| 11 | `stable-release-hardening` | 05-hardening-and-release | Testing, auth, authorization, quality gates after prototype works. |
| 12 | `security-first-review` | 05-hardening-and-release | Security review before stable release. |
| 13 | `encapsulation-backend-config` | 05-hardening-and-release | Hide secrets, env vars, backend details from UI/API. |

### Tier 5 — Deployment & Documentation
| Priority | Skill | Phase | When to Use |
|----------|-------|-------|-------------|
| 14 | `deploy-and-document` | 06-deployment-and-documentation | VPS/Vercel deploy, DNS, SSL, README, release notes. |

### Tier 6 — Hackathon Intake & Strategy
| Priority | Skill | Phase | When to Use |
|----------|-------|-------|-------------|
| 15 | `hackathon-project-system` | 07-hackathon-intake-and-strategy | Structure the hackathon project. |
| 16 | `hackathon-brief-analyzer` | 07-hackathon-intake-and-strategy | Analyze brief, rules, constraints. |
| 17 | `hackathon-judging-strategy` | 07-hackathon-intake-and-strategy | Align with judging criteria. |
| 18 | `hackathon-resource-planner` | 07-hackathon-intake-and-strategy | Plan time, team, tools. |

### Tier 7 — Hackathon Build & Submit
| Priority | Skill | Phase | When to Use |
|----------|-------|-------|-------------|
| 19 | `hackathon-build-roadmap` | 08-hackathon-build-and-submit | Implementation roadmap for competition. |
| 20 | `hackathon-compliance-review` | 08-hackathon-build-and-submit | Verify rules compliance. |
| 21 | `hackathon-demo-pitch` | 08-hackathon-build-and-submit | Demo flow, pitch narrative, judging evidence. |
| 22 | `hackathon-submission-packager` | 08-hackathon-build-and-submit | Final submission package checklist. |

---

## Standard Sequences (from GLOBAL_SKILL_ROUTER)

### Standard App Sequence
1. `app-global-preferences`
2. `complete-app-blueprint`
3. `dashboard-first-ui`
4. `functional-prototype-first`
5. `data-persistence-design`
6. `stable-release-hardening`
7. `security-first-review`
8. `encapsulation-backend-config`
9. `deploy-and-document`

### Standard AI App Sequence
1. `app-global-preferences`
2. `complete-app-blueprint`
3. `ai-app-builder`
4. `prompt-engineering-system`
5. `agent-workflow-design` (if needed)
6. `data-persistence-design`
7. `stable-release-hardening`
8. `security-first-review`
9. `encapsulation-backend-config`
10. `deploy-and-document`

### Standard Hackathon Sequence
1. `hackathon-project-system`
2. `hackathon-brief-analyzer`
3. `hackathon-judging-strategy`
4. `hackathon-resource-planner`
5. `hackathon-build-roadmap`
6. `hackathon-compliance-review`
7. `hackathon-demo-pitch`
8. `hackathon-submission-packager`

(Plus relevant app/AI skills if the project is an app.)

---

## Directory Tree

```
Skills/
├── GLOBAL_SKILL_ROUTER.md          ← Master routing guide
├── README.md
├── TREE.md                         ← This file (priority + order)
└── by-phase/                       ← Canonical skills (foundational at top)
    ├── 01-foundation/              ← HIGHEST PRIORITY
    │   ├── sdlc-best-practices/
    │   ├── app-global-preferences/
    │   ├── project-foundations-and-architecture/
    │   └── complete-app-blueprint/
    ├── 02-design-and-prototype/
    │   ├── dashboard-first-ui/
    │   └── functional-prototype-first/
    ├── 03-data-and-persistence/
    │   └── data-persistence-design/
    ├── 04-ai-systems/
    │   ├── ai-app-builder/
    │   ├── prompt-engineering-system/
    │   └── agent-workflow-design/
    ├── 05-hardening-and-release/
    │   ├── stable-release-hardening/
    │   ├── security-first-review/
    │   └── encapsulation-backend-config/
    ├── 06-deployment-and-documentation/
    │   └── deploy-and-document/
    ├── 07-hackathon-intake-and-strategy/
    │   ├── hackathon-project-system/
    │   ├── hackathon-brief-analyzer/
    │   ├── hackathon-judging-strategy/
    │   └── hackathon-resource-planner/
    └── 08-hackathon-build-and-submit/
        ├── hackathon-build-roadmap/
        ├── hackathon-compliance-review/
        ├── hackathon-demo-pitch/
        └── hackathon-submission-packager/
```

Each skill folder contains:
- `SKILL.md` — operational instructions
- `agents/openai.yaml` (when present) — agent metadata

---

## Notes from Sources

- **GitHub repo** is the first and complete source (includes hackathon skills).
- **SDLC app** (sdlc.base44.app) emphasizes the SRS / Discuss → Specify → Build gate and lists the same foundational + core skills with SDLC Best Practices as the starting point.
- Skills are designed so AI must read the relevant skill(s) before writing code.

Use `GLOBAL_SKILL_ROUTER.md` for detailed routing tables.
