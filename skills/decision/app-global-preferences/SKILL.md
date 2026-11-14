---
name: app-global-preferences
description: Published skill from SDLC Skills Hub (SRS Architect themed). Extracted and structured for agent use.
source: https://sdlc.base44.app/skill/app-global-preferences
priority: foundation-first
---

V1.0.0
App Global Preferences

Personal global development preferences for AI-assisted application builds. Use when planning, building, reviewing, hardening, documenting, or deploying an app for Awais; when the user asks to apply default preferences; or when deciding default SDLC order, stack, UI, data, testing, security, documentation, or deployment behavior.

App Global Preferences

Skill SK-04 · Cross-phase — Engineering standards · Applies to: web apps, Android apps, APIs, AI apps The owner's default engineering preferences. Apply them whenever the SRS and the user are silent; never over an explicit decision.

1. Purpose

When a requirement is silent, an AI fills the silence with its own taste, and each new session fills it differently — another source of rework. This skill is the single, written set of defaults: stack, build order, UI baseline, completeness rules and the done definition. It makes AI output consistent across sessions and tools.

2. When to use — and when not to

Use it when planning, building, reviewing, hardening, documenting or deploying any app, as the tie-breaker for anything the SRS and Foundations Record do not decide.

Do not use it to override a stated user, client or project requirement. Precedence: explicit user decision > SRS / Foundations Record > these defaults.

3. Inputs required
Input	Source	Required
Foundations Record	SK-02	Yes
SRS (FR/NFR)	SK-01	Yes
Platform target (web / Android / both)	SK-02	Yes
4. Procedure — default build order
Step	SDLC phase	Action
1	Requirements	Clarify the core requirement and its acceptance criteria (SK-01).
2	Implementation	Build the main functional workflow first (SK-06).
3	Implementation	Use mock data only to prove the workflow early; mark it as mock.
4	Testing	Test the core workflow manually and automatically where practical.
5	Design	Reorder pages, navigation and layout after the core flow works.
6	Implementation	Replace mock-only behaviour with real persistence before stable release (SK-07).
7	Hardening	Add authentication and authorization after complete functionality, unless auth is the core requirement (SK-13).
8	Implementation	Add supporting sections one by one, testing and validating each.
9	Hardening	Add security in layers, testing after each layer (SK-12).
10	Release	Prepare documentation and deployment only once the app is stable and functional (SK-14).
Default stack (when nothing is specified)
Target	Default
Web, full-stack	Next.js + TypeScript + Tailwind, full-stack architecture
Persistence	Supabase → MongoDB → PostgreSQL (in that order of preference)
Hosting, full-stack	VPS (dedicated port + subdomain per app)
Hosting, fully static	GitHub + Vercel auto-deploy
Android	Record as Assumed and confirm: Kotlin + Jetpack Compose (native) or React Native / Flutter (cross-platform), chosen in SK-02
Low-code builders (Base44, Lovable)	Use the platform's own entities, auth and hosting; apply these rules to structure and quality
UI defaults
Dashboard-first, not landing-page-first, unless the product requires a landing page.
Modern dark aesthetic with a consistent gradient treatment — unless an Interface Library direction was selected.
Conventional layouts: sidebar, top navigation, tables, panels, settings, dashboards, management views (Android: Material 3 navigation patterns).
Consistent theme, spacing, component style, navigation and density across pages.
No overlap, clipping, hidden controls, unreadable text, or inconsistent responsive behaviour.
Completeness rules
Never add placeholders for core functionality.
Never imply a working feature visually if the behaviour is not implemented.
If a feature needs a dependency, credential, service, API, schema decision or approval, say exactly: "I need X to add Y functionally."
Derive roles and access control from the requirements; no admin/super-admin complexity without justification.
AI features are lower priority unless the product is an AI app; ask before adding secondary AI features.
5. Deliverables
A short "Defaults applied" note in the build plan listing each default used and why (e.g. "Persistence: Supabase — default, SRS silent").
Every default that constrains behaviour is added to the SRS as an Assumed NFR for confirmation.
6. Acceptance criteria
No default contradicts an explicit decision.
Every default applied is listed and visible to the user.
The build order was followed, or the deviation is written down with its reason.
7. Verification checklist
 Precedence respected (user > SRS > defaults).
 "Defaults applied" note exists.
 Core workflow built before auth, polish and secondary sections.
 No placeholder for core behaviour; no fake buttons.
 Missing inputs stated as "I need X to add Y functionally".
 UI consistent and free of overlap/clipping at desktop and mobile widths.
8. Failure modes and anti-loop guards
Failure mode	Guard
Each AI session re-decides the stack or style	One written default set; cite it in every build prompt.
Defaults override the client's requirement	Precedence rule.
Fake UI that looks done	Completeness rules.
Polishing before the core works	Default build order step 2 before step 5.
Role explosion (admin, super-admin, staff)	Roles only from requirements.
9. Prompt template
STANDARDS (apply only where my SRS and decisions are silent; never override them):
- Build order: core workflow → test → layout → real persistence → auth → supporting sections → layered security → docs/deploy.
- Stack defaults: Next.js + TypeScript + Tailwind; Supabase > MongoDB > PostgreSQL; VPS for full-stack, GitHub + Vercel for static.
- UI: dashboard-first, dark theme with consistent gradients, conventional layout, no overlap/clipping.
- No placeholders or fake controls for core behaviour. If something is missing say "I need X to add Y functionally" and stop.
- List every default you applied under "Defaults applied".
TASK: <task, citing FR IDs>

10. Traceability to the SRS

Defaults that affect behaviour or operations become Assumed NFRs in SRS §6 and §10 (e.g. NFR-8: Data persists in Supabase — Assumed, pending confirmation). Once confirmed, they are ordinary requirements with test IDs.

11. Definition of done
Verification: all stated requirements are implemented.
Validation: every implementation works as intended.
Done: verification and validation both pass, and every applied default is recorded.
Related skills

SK-03 Complete App Blueprint · SK-05 Dashboard First UI · SK-06 Functional Prototype First · SK-07 Data Persistence Design · SK-13 Stable Release Hardening · SK-11 Encapsulation — Backend Configuration · SK-14 Deploy and Document.

Ready to hand this to your AI?

Copy the skill, drop it into your project, and require the AI to read it before the first prompt.

COPY SKILL
DOWNLOAD .MD