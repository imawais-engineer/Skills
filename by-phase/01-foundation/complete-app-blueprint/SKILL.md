---
name: complete-app-blueprint
description: Published skill from SDLC Skills Hub (SRS Architect themed). Extracted and structured for agent use.
source: https://sdlc.base44.app/skill/complete-app-blueprint
priority: foundation-first
---

V1.0.0
Complete App Blueprint

Expand an application idea into a complete software blueprint before implementation. Use when a prompt asks to build an app, SaaS, dashboard, portal, admin system, internal tool, marketplace, AI app, CRUD system, or any feature that may need pages, workflows, roles, data, APIs, dashboards, security, tests, documentation, or deployment.

Complete App Blueprint

Skill SK-03 · Phase 1 — Foundation (System design) · Applies to: web apps, Android apps, APIs, AI apps Map the complete application surface before coding, so the AI never builds only the visible feature.

1. Purpose

AI builders implement what they can see in the prompt: one screen, one happy path. Everything around it — the empty state, the settings page, the role that must be blocked, the record that must be archived — is discovered later, one bug at a time, which drives the edit loop. This skill expands an approved idea into a full App Blueprint: users, workflows, pages, data, APIs, UI states, security, tests, documentation and deployment, while still building the core function first.

2. When to use — and when not to

Use it when a prompt asks to build an app, SaaS, dashboard, portal, admin system, internal tool, marketplace, AI app, CRUD system, Android app, or any feature that may need pages, workflows, roles, data, APIs, security, tests or deployment.

Do not use it for a single isolated component inside an already-blueprinted app — update the existing blueprint instead.

3. Inputs required
Input	Source	Required
Confirmed Foundations Record	SK-02	Yes
Approved or draft SRS (FR/NFR IDs)	SK-01	Yes
Interface direction	Interface Library	Optional
4. Procedure
Step	SDLC phase	Action	Output
1	Analysis	Restate the core requirement in one sentence.	Core statement
2	Analysis	Define primary users and roles; ask if unclear.	Role list (SRS §3)
3	Design	Write the core workflow that proves the app's value as numbered steps.	Core flow
4	Design	List required pages/screens (see page map) — include only those that serve an FR.	Page map
5	Design	List entities, relationships, ownership, lifecycle states.	Data map (SRS §7)
6	Design	List backend/API capabilities, integrations, background jobs, files.	Capability list
7	Design	For every page, list UI states: loading, empty, error, success, disabled, validation, responsive (and for Android: offline, permission denied, rotation, back navigation).	State matrix
8	Design	List security, auth and permission needs for stable release.	Security list
9	Test planning	List tests for prototype and stable release; one test per acceptance criterion.	Test plan (TC IDs)
10	Planning	List documentation and deployment needs.	Ops list
11	Planning	Produce the phased roadmap (section 5).	Roadmap
Page and section map (include only what serves an FR)

Dashboard · sidebar / top navigation (Android: bottom navigation / navigation drawer) · core workflow pages · CRUD management pages · detail pages · search, filters, sorting, pagination · analytics or reports · activity/history logs · notifications · settings · profile/account · admin panel when roles require it · help/docs/about when useful · landing/pricing only when the product requires them.

5. Deliverables
App Blueprint with these tables:
## Pages
| Page / screen | Purpose | FR IDs | Roles | States covered |
| --- | --- | --- | --- | --- |
## Entities
| Entity | Key fields | Relationships | Owner | Lifecycle |
| --- | --- | --- | --- | --- |
## Capabilities
| API / job / integration | Trigger | FR IDs | Credentials needed from |
| --- | --- | --- | --- |
## Tests
| TC ID | Verifies | Type (manual / unit / e2e) |
| --- | --- | --- |

Roadmap in this order: (1) functional prototype of the core workflow with mock or seed data; (2) prototype validation; (3) data layer — schema, migration, seed data, indexes, persistence; (4) UI completion, section by section; (5) authentication and authorization, after working functionality unless required earlier; (6) layered security hardening with tests after each layer; (7) documentation and deployment readiness.
6. Acceptance criteria
Every page/screen maps to at least one FR ID; no FR is left without a page or capability.
Every page lists its non-happy states.
Every entity has an owner and lifecycle.
Every external dependency names who supplies the credential.
The roadmap starts with the core workflow.
7. Verification checklist
 Core requirement restated in one sentence and confirmed.
 Roles match SRS §3.
 Pages table complete; no orphan pages (without FR) and no orphan FRs (without page).
 State matrix covers loading / empty / error / success / disabled / validation / responsive (+ Android states where relevant).
 Entities table matches SRS §7.
 Capabilities list with credential owners.
 Test IDs cover every Must-priority acceptance criterion.
 Roadmap follows the 7-phase order.
8. Failure modes and anti-loop guards
Failure mode	Guard
Narrow build: only the visible feature exists	Page and state matrix must be complete before coding.
Page bloat: admin panels and analytics nobody asked for	No page without an FR ID.
Hidden dependency discovered mid-build	Escalation rule: state "I need X to add Y functionally" before continuing.
Repeated edits for empty/error states	States are listed per page up front, so the first build includes them.
Auth bolted on and breaking flows	Auth phase is planned explicitly in the roadmap.
9. Prompt template
ROLE: You are a solution architect. Produce an App Blueprint. No code yet.
INPUT: Foundations Record: <paste>. SRS: <paste FR/NFR tables>.
OUTPUT, in this order:
1. Core requirement in one sentence.
2. Pages table: page | purpose | FR IDs | roles | states (loading, empty, error, success, disabled, validation, responsive; Android: offline, permission denied, back).
3. Entities table: entity | key fields | relationships | owner | lifecycle.
4. Capabilities table: API/job/integration | trigger | FR IDs | credentials from.
5. Tests table: TC ID | verifies (FR/NFR ID) | type.
6. Roadmap: prototype → validation → data layer → UI completion → auth → security → docs/deploy.
RULES: No page without an FR ID. No FR without a page or capability. List every missing input as "I need X to add Y". Stop after the blueprint and wait for approval.

10. Traceability to the SRS

The blueprint is the bridge FR ID → page/capability → TC ID. Copy the TC IDs into SRS §14 (traceability matrix). Any page added later must cite an FR, or the SRS is updated first.

11. Definition of done

The blueprint has zero orphan pages and zero orphan FRs, every Must FR has a test ID, missing dependencies are listed explicitly, and the user approved the roadmap.

Related skills

Previous: SK-02 Project Foundations. Next: SK-05 Dashboard First UI and SK-06 Functional Prototype First. Defaults: SK-04 App Global Preferences.

RELATED LEARNING

Vibe Coding & AI-Assisted Development

28 MIN READ

Ready to hand this to your AI?

Copy the skill, drop it into your project, and require the AI to read it before the first prompt.

COPY SKILL
DOWNLOAD .MD