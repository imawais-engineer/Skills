# Global Skill Router

Use this file as the master index for choosing the right skill before planning, building, reviewing, or submitting a project.

## Directory Model

- Canonical authored skills live in `/home/awais/Skills/by-phase/<phase>/<skill>/SKILL.md`.
- Use-case browsing links live in `/home/awais/Skills/by-use-case/<use-case>/<skill>`.
- Codex-discoverable installed skills live in `/home/awais/.codex/skills/<skill>/SKILL.md`.

Keep `/home/awais/.codex/skills` flat so Codex can discover skills automatically. Use `/home/awais/Skills/by-phase` as the source organization tree.

## Routing Order

1. Use `app-global-preferences` for default development principles and user preferences.
2. Use `complete-app-blueprint` before building any app from a vague or broad request.
3. Use phase-specific skills while moving through implementation.
4. Use AI-specific skills only when AI is the core product or explicitly required.
5. Use hackathon skills when a competition brief, rules, judging criteria, or submission package is involved.
6. Use security and release skills after the core app works, or earlier when security is the task.

## Fast Routing

| User Request | Start With | Then Add |
| --- | --- | --- |
| "Build an app" | `app-global-preferences` | `complete-app-blueprint`, `dashboard-first-ui`, `functional-prototype-first` |
| "Plan a full product" | `complete-app-blueprint` | `data-persistence-design`, `stable-release-hardening`, `deploy-and-document` |
| "Make the UI/dashboard" | `dashboard-first-ui` | `functional-prototype-first` |
| "Implement the prototype" | `functional-prototype-first` | `dashboard-first-ui`, `data-persistence-design` |
| "Design database/storage" | `data-persistence-design` | `stable-release-hardening` when auth/RLS/security is needed |
| "Build an AI app" | `ai-app-builder` | `prompt-engineering-system`, `agent-workflow-design`, `security-first-review` |
| "Design prompts" | `prompt-engineering-system` | `ai-app-builder` when prompts are part of a product |
| "Design an agent workflow" | `agent-workflow-design` | `prompt-engineering-system`, `security-first-review` |
| "Prepare for stable release" | `stable-release-hardening` | `security-first-review`, `deploy-and-document` |
| "Review security" | `security-first-review` | `encapsulation-backend-config`, `stable-release-hardening` |
| "Hide backend config from UI/API" | `encapsulation-backend-config` | `security-first-review` |
| "Deploy/document" | `deploy-and-document` | `stable-release-hardening` |
| "Build for a hackathon" | `hackathon-project-system` | All relevant hackathon child skills |
| "Parse hackathon brief" | `hackathon-brief-analyzer` | `hackathon-judging-strategy`, `hackathon-resource-planner` |
| "Optimize for judging" | `hackathon-judging-strategy` | `hackathon-demo-pitch` |
| "Create hackathon roadmap" | `hackathon-build-roadmap` | `hackathon-compliance-review` |
| "Check hackathon rules" | `hackathon-compliance-review` | `hackathon-submission-packager` |
| "Prepare pitch/demo" | `hackathon-demo-pitch` | `hackathon-submission-packager` |
| "Prepare submission" | `hackathon-submission-packager` | `hackathon-compliance-review` |

## Skills By Phase

### 01 Foundation

| Skill | When To Use | Canonical Path | Installed Path |
| --- | --- | --- | --- |
| `app-global-preferences` | Use for Awais's default SDLC, stack, UI, database, security, documentation, deployment, and V&V preferences. | `/home/awais/Skills/by-phase/01-foundation/app-global-preferences/SKILL.md` | `/home/awais/.codex/skills/app-global-preferences/SKILL.md` |
| `complete-app-blueprint` | Use before building any app, SaaS, dashboard, portal, CRUD system, marketplace, admin system, or broad feature. | `/home/awais/Skills/by-phase/01-foundation/complete-app-blueprint/SKILL.md` | `/home/awais/.codex/skills/complete-app-blueprint/SKILL.md` |

### 02 Design And Prototype

| Skill | When To Use | Canonical Path | Installed Path |
| --- | --- | --- | --- |
| `dashboard-first-ui` | Use for dashboard-first UI, dark gradient app aesthetics, sidebar/nav/table layouts, page completeness, and visual validation. | `/home/awais/Skills/by-phase/02-design-and-prototype/dashboard-first-ui/SKILL.md` | `/home/awais/.codex/skills/dashboard-first-ui/SKILL.md` |
| `functional-prototype-first` | Use when implementing the core workflow before auth, hardening, production layers, or secondary sections. | `/home/awais/Skills/by-phase/02-design-and-prototype/functional-prototype-first/SKILL.md` | `/home/awais/.codex/skills/functional-prototype-first/SKILL.md` |

### 03 Data And Persistence

| Skill | When To Use | Canonical Path | Installed Path |
| --- | --- | --- | --- |
| `data-persistence-design` | Use for database selection, schemas, migrations, seed data, indexes, relationships, Supabase, MongoDB, PostgreSQL, and replacing mock data. | `/home/awais/Skills/by-phase/03-data-and-persistence/data-persistence-design/SKILL.md` | `/home/awais/.codex/skills/data-persistence-design/SKILL.md` |

### 04 AI Systems

| Skill | When To Use | Canonical Path | Installed Path |
| --- | --- | --- | --- |
| `ai-app-builder` | Use for AI-first apps: chat, copilots, RAG, agents, generation, extraction, classification, AI workflows, cost controls, evals, and AI safety. | `/home/awais/Skills/by-phase/04-ai-systems/ai-app-builder/SKILL.md` | `/home/awais/.codex/skills/ai-app-builder/SKILL.md` |
| `prompt-engineering-system` | Use for prompt design, system instructions, structured outputs, prompt libraries, evals, versioning, validation, and prompt-injection boundaries. | `/home/awais/Skills/by-phase/04-ai-systems/prompt-engineering-system/SKILL.md` | `/home/awais/.codex/skills/prompt-engineering-system/SKILL.md` |
| `agent-workflow-design` | Use for AI agents, tool-using assistants, autonomous workflows, state machines, memory, approvals, retries, audit trails, and human-in-the-loop systems. | `/home/awais/Skills/by-phase/04-ai-systems/agent-workflow-design/SKILL.md` | `/home/awais/.codex/skills/agent-workflow-design/SKILL.md` |

### 05 Hardening And Release

| Skill | When To Use | Canonical Path | Installed Path |
| --- | --- | --- | --- |
| `stable-release-hardening` | Use after the core app works to add testing, auth, authorization, validation, security layers, and the V&V done gate. | `/home/awais/Skills/by-phase/05-hardening-and-release/stable-release-hardening/SKILL.md` | `/home/awais/.codex/skills/stable-release-hardening/SKILL.md` |
| `security-first-review` | Use to review auth, APIs, database access, secrets, dependencies, AI features, deployment config, rules, and release security gaps. | `/home/awais/Skills/by-phase/05-hardening-and-release/security-first-review/SKILL.md` | `/home/awais/.codex/skills/security-first-review/SKILL.md` |
| `encapsulation-backend-config` | Use to prevent backend configuration, secrets, env names, provider metadata, runtime modes, and internal integration details from appearing in public UI or public API responses. | `/home/awais/Skills/by-phase/05-hardening-and-release/encapsulation-backend-config/SKILL.md` | `/home/awais/.codex/skills/encapsulation-backend-config/SKILL.md` |

### 06 Deployment And Documentation

| Skill | When To Use | Canonical Path | Installed Path |
| --- | --- | --- | --- |
| `deploy-and-document` | Use for VPS deployment, static Vercel flow, GitHub push workflow, subdomains, shared-IP DNS conflicts, ports, reverse proxy hostname routing, SSL, env files, setup docs, and release notes. | `/home/awais/Skills/by-phase/06-deployment-and-documentation/deploy-and-document/SKILL.md` | `/home/awais/.codex/skills/deploy-and-document/SKILL.md` |

### 07 Hackathon Intake And Strategy

| Skill | When To Use | Canonical Path | Installed Path |
| --- | --- | --- | --- |
| `hackathon-project-system` | Use as the root orchestrator for hackathon or competition project planning from overview, requirements, submission items, judging criteria, resources, and rules. | `/home/awais/Skills/by-phase/07-hackathon-intake-and-strategy/hackathon-project-system/SKILL.md` | `/home/awais/.codex/skills/hackathon-project-system/SKILL.md` |
| `hackathon-brief-analyzer` | Use to parse the brief into structured requirements, deliverables, resources, judging rubric, rules, blockers, and missing information. | `/home/awais/Skills/by-phase/07-hackathon-intake-and-strategy/hackathon-brief-analyzer/SKILL.md` | `/home/awais/.codex/skills/hackathon-brief-analyzer/SKILL.md` |
| `hackathon-judging-strategy` | Use to select or refine a project idea around judging criteria, score drivers, demo evidence, differentiation, and feasible scope. | `/home/awais/Skills/by-phase/07-hackathon-intake-and-strategy/hackathon-judging-strategy/SKILL.md` | `/home/awais/.codex/skills/hackathon-judging-strategy/SKILL.md` |
| `hackathon-resource-planner` | Use to map required tools, sponsor APIs, datasets, SDKs, credits, allowed platforms, credentials, and fallback plans into architecture. | `/home/awais/Skills/by-phase/07-hackathon-intake-and-strategy/hackathon-resource-planner/SKILL.md` | `/home/awais/.codex/skills/hackathon-resource-planner/SKILL.md` |

### 08 Hackathon Build And Submit

| Skill | When To Use | Canonical Path | Installed Path |
| --- | --- | --- | --- |
| `hackathon-build-roadmap` | Use to create a timeboxed build roadmap from requirements, judging strategy, resources, rules, demo-critical path, and submission tasks. | `/home/awais/Skills/by-phase/08-hackathon-build-and-submit/hackathon-build-roadmap/SKILL.md` | `/home/awais/.codex/skills/hackathon-build-roadmap/SKILL.md` |
| `hackathon-compliance-review` | Use before project selection, implementation, demo recording, and final submission to check rules, eligibility, deliverables, licenses, and constraints. | `/home/awais/Skills/by-phase/08-hackathon-build-and-submit/hackathon-compliance-review/SKILL.md` | `/home/awais/.codex/skills/hackathon-compliance-review/SKILL.md` |
| `hackathon-demo-pitch` | Use to prepare judging-focused demo flow, pitch story, video outline, screenshots, rubric proof points, and impact narrative. | `/home/awais/Skills/by-phase/08-hackathon-build-and-submit/hackathon-demo-pitch/SKILL.md` | `/home/awais/.codex/skills/hackathon-demo-pitch/SKILL.md` |
| `hackathon-submission-packager` | Use to prepare README, project description, repo, live URL, demo video, screenshots, setup instructions, attributions, and final submission checklist. | `/home/awais/Skills/by-phase/08-hackathon-build-and-submit/hackathon-submission-packager/SKILL.md` | `/home/awais/.codex/skills/hackathon-submission-packager/SKILL.md` |

## Skills By Use Case

| Use Case | Directory | Skills |
| --- | --- | --- |
| Application development | `/home/awais/Skills/by-use-case/application-development` | `app-global-preferences`, `complete-app-blueprint`, `dashboard-first-ui`, `functional-prototype-first`, `data-persistence-design`, `stable-release-hardening`, `security-first-review`, `encapsulation-backend-config`, `deploy-and-document` |
| AI development | `/home/awais/Skills/by-use-case/ai-development` | `ai-app-builder`, `prompt-engineering-system`, `agent-workflow-design`, `security-first-review` |
| Security and release | `/home/awais/Skills/by-use-case/security-and-release` | `stable-release-hardening`, `security-first-review`, `encapsulation-backend-config`, `deploy-and-document` |
| Hackathons and competitions | `/home/awais/Skills/by-use-case/hackathons-and-competitions` | `hackathon-project-system`, `hackathon-brief-analyzer`, `hackathon-judging-strategy`, `hackathon-resource-planner`, `hackathon-build-roadmap`, `hackathon-compliance-review`, `hackathon-demo-pitch`, `hackathon-submission-packager` |
| Planning and strategy | `/home/awais/Skills/by-use-case/planning-and-strategy` | `app-global-preferences`, `complete-app-blueprint`, `hackathon-project-system`, `hackathon-brief-analyzer`, `hackathon-judging-strategy`, `hackathon-resource-planner` |
| Implementation roadmaps | `/home/awais/Skills/by-use-case/implementation-roadmaps` | `functional-prototype-first`, `dashboard-first-ui`, `data-persistence-design`, `hackathon-build-roadmap` |
| Submission and pitch | `/home/awais/Skills/by-use-case/submission-and-pitch` | `hackathon-demo-pitch`, `hackathon-submission-packager`, `deploy-and-document` |

## Standard App Sequence

Use this sequence for most application builds:

1. `app-global-preferences`
2. `complete-app-blueprint`
3. `dashboard-first-ui`
4. `functional-prototype-first`
5. `data-persistence-design`
6. `stable-release-hardening`
7. `security-first-review`
8. `encapsulation-backend-config`
9. `deploy-and-document`

## Standard AI App Sequence

Use this sequence when AI is core to the product:

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

Use this sequence when the input is a hackathon or competition brief:

1. `hackathon-project-system`
2. `hackathon-brief-analyzer`
3. `hackathon-judging-strategy`
4. `hackathon-resource-planner`
5. `hackathon-build-roadmap`
6. `hackathon-compliance-review`
7. `hackathon-demo-pitch`
8. `hackathon-submission-packager`

If the hackathon project is an app, also use the relevant application skills. If it is AI-first, also use the AI skills.

## Maintenance Rule

When adding, renaming, moving, or deleting a skill:

1. Update the canonical `by-phase` path.
2. Update any relevant `by-use-case` links.
3. Update the installed `/home/awais/.codex/skills` copy if Codex should discover it.
4. Update this router file.
5. Run `quick_validate.py` on the canonical skill and installed copy.
