---
name: functional-prototype-first
description: Published skill from SDLC Skills Hub (SRS Architect themed). Extracted and structured for agent use.
source: https://sdlc.base44.app/skill/functional-prototype-first
priority: foundation-first
---

V1.0.0
Functional Prototype First

Implementation workflow for building the core functional application before authentication, authorization, production hardening, or secondary sections. Use when coding an app, feature, dashboard, workflow, prototype, MVP, or full-stack product where Awais wants functionality proven before stable-release layers.

Functional Prototype First

Skill SK-06 · Phase 2 — Design & Prototype (Implementation) · Applies to: web apps, Android apps, APIs, AI apps Make the core workflow work end to end with real behaviour before adding production layers.

1. Purpose

Projects stall when auth, settings, polish and secondary pages are built before the one workflow that proves the app's value. Then the core flow is finally attempted on top of a fragile base and every fix breaks something else. This skill builds the smallest complete workflow first, with real UI and real state changes, validates it, and only then expands scope one section at a time.

2. When to use — and when not to

Use it for the first implementation of any app or major feature, after the SRS and blueprint are approved.

Do not use it when authentication or security is the core requirement — then include them in the prototype scope.

3. Inputs required
Input	Source	Required
Approved SRS with Must-priority FRs	SK-01	Yes
Core workflow and pages table	SK-03	Yes
Seed/mock data shape	SK-07 (draft)	Yes
4. Procedure
Step	SDLC phase	Action
1	Planning	Identify the smallest complete workflow that proves the app's value; list its FR IDs.
2	Implementation	Implement it with real UI and real behaviour.
3	Implementation	Use mock or seed data only as a temporary aid; label it mock in code and notes.
4	Implementation	No placeholders for core behaviour.
5	Testing	Run the workflow manually in the app (web browser / Android device or emulator).
6	Testing	Add focused automated tests where practical (one per Must acceptance criterion).
7	Verification	Fix functional and visual defects before expanding scope.
8	Design	Reorder navigation, sections and page structure after the core flow works.
9	Implementation	Add each remaining section one by one.
10	Validation	Validate each section before starting the next.
Placeholder policy
No TODO-only core features.
No fake buttons, dashboards, forms or tables for required behaviour.
Missing input → "I need X to add Y functionally."
Mock data is allowed only to test the prototype and is replaced before stable release.
5. Deliverables
Working core workflow (deployed preview or runnable build / APK).
Prototype report: FR IDs implemented, test results, known missing production layers, mock data still in use.
6. Acceptance criteria
Given the core workflow's FR acceptance criteria, when each is executed in the running app, then all pass.
Every required interaction performs a real state change (visible after reload when persistence exists).
Missing production layers (auth, hardening, real persistence) are listed, not hidden.
7. Verification checklist
 Core workflow FR IDs listed before coding.
 Workflow runs end to end in the app.
 Main screens render correctly on target platforms.
 Interactions perform real state changes.
 Mock data labelled and listed.
 Automated tests for Must criteria where practical.
 Known missing production layers documented.
 Sections added one by one, each validated.
8. Failure modes and anti-loop guards
Failure mode	Guard
Building auth/settings before the core works	Step 1 scope = core workflow only.
"Fix one, break two" spiral	Change one section at a time; re-run the core workflow tests after each change.
Fake UI mistaken for progress	Placeholder policy.
Mock data shipped to production	Mock is labelled and listed in the report; SK-07 removes it.
AI rewrites the whole app for a small fix	Edit requests name the FR ID and the file/section; ask for a minimal diff.

Loop breaker: if the same defect survives two fix attempts, stop. Write the failing behaviour as a Given/When/Then, confirm it is the intended behaviour, then request one fix against that criterion.

9. Prompt template
ROLE: Senior engineer building a functional prototype.
SCOPE: Only the core workflow: <numbered steps>. FR IDs: <FR-1, FR-2, ...>. Acceptance criteria: <paste Given/When/Then>.
RULES:
- Real UI, real state changes. Mock/seed data only where labelled "mock".
- No placeholders, fake buttons, or TODO core features. If something is missing, say "I need X to add Y functionally" and stop.
- Do not add auth, settings, analytics, or secondary pages yet.
- After building, run each acceptance criterion and report Pass/Fail per FR ID, plus: mock data in use, missing production layers.
- For fixes: change only what the cited FR requires; show what changed.

10. Traceability to the SRS

Prototype scope = the Must FRs of the core workflow. Each one gets a row in SRS §14 with status Implemented (prototype); it becomes Verified/Validated when its tests pass on real persistence.

11. Definition of done

The prototype is ready for hardening when the core workflow passes all its acceptance criteria end to end, main screens render, interactions change real state, missing production layers are documented, and verification and validation both pass.

Related skills

Previous: SK-03, SK-05. Next: SK-07 Data Persistence Design → SK-13 Stable Release Hardening.

Ready to hand this to your AI?

Copy the skill, drop it into your project, and require the AI to read it before the first prompt.

COPY SKILL
DOWNLOAD .MD