---
name: stable-release-hardening
description: Published skill from SDLC Skills Hub (SRS Architect themed). Extracted and structured for agent use.
source: https://sdlc.base44.app/skill/stable-release-hardening
priority: foundation-first
---

V1.0.0
Stable Release Hardening

Stable release workflow for testing, authentication, authorization, layered security, and verification/validation. Use after a functional prototype works, or when preparing an AI-built app for release, adding auth, securing routes/APIs/data, writing tests, running quality gates, or deciding whether an app is done.

Stable Release Hardening

Skill SK-13 · Phase 5 — Hardening & Release (V&V) · Applies to: web apps, Android apps, APIs, AI apps Turn a working prototype into a stable release: real persistence, auth, layered security, and a verification-and-validation gate.

1. Purpose

The jump from "it works on my screen" to "it is safe to release" is where AI-built apps break most often: auth added late breaks flows, mock data lingers, nothing is tested. This skill sequences hardening into small layers, each followed by tests, and ends with an explicit V&V gate so "done" means something measurable.

2. When to use — and when not to

Use it when moving from functional prototype to stable release: testing, authentication, authorization, layered security, verification and validation.

Do not use it before the core workflow passes its acceptance criteria (SK-06).

3. Inputs required
Input	Source	Required
Passing prototype report	SK-06	Yes
Roles and permissions	SRS §3	Yes
Data model and access rules	SK-07	Yes
Security findings	SK-12	Yes
4. Procedure — hardening sequence
Layer	SDLC phase	Action	Test after
1	Verification	Confirm the prototype works end to end.	Core workflow tests
2	Implementation	Replace required mock-only data with real persistence.	CRUD tests
3	Design	Define roles and permissions from requirements; ask when admin/owner/staff/tenant permissions are unclear.	—
4	Implementation	Add authentication (after functionality, unless auth is core).	Sign-in/out, session expiry
5	Implementation	Add authorization and protected routes/screens.	Role matrix tests
6	Implementation	Add input validation and structured error handling.	Invalid-input tests
7	Implementation	Add database access rules and ownership checks.	Cross-user denial
8	Implementation	Secure environment variables and secrets handling.	Bundle/APK secret scan
9	Implementation	Add rate limiting, file restrictions, audit logs, dependency checks where relevant.	Limit tests
10	Validation	Full regression: manual browser/device test plus automated tests.	V&V gate

Auth and roles: do not assume extra roles without evidence; implement role-specific dashboards, protected routes and audit logs only when roles require them.

Testing scope for stable release

Core user flows · database operations · authentication and authorization · important edge cases · validation and error states · UI responsiveness and visible breakage · security-sensitive routes, inputs and data access. Android: test on at least the minimum supported version and one current version, plus rotation, background/foreground and offline.

5. Deliverables
Hardened build.
Test report: test ID, FR/NFR ID, type (manual/automated), result.
Completion report: what was verified, what was validated, which tests ran, remaining limitations and external requirements.
6. Acceptance criteria
Every Must FR has at least one passing test.
Every role in SRS §3 has a passing permission test (allowed and denied).
No mock-only required data remains.
Each hardening layer was followed by passing tests before the next began.
7. Verification checklist — security baseline
 Input validation.
 Auth/session security.
 Role-based permissions.
 Protected API routes and pages/screens.
 Secure environment variables and secret handling.
 Database access rules.
 Rate limits where relevant.
 File upload restrictions where relevant.
 Audit logs for important actions.
 Dependency and configuration checks.
8. Failure modes and anti-loop guards
Failure mode	Guard
Auth breaks existing flows	Auth is its own layer, followed by the full core workflow test.
Many layers at once, unclear what broke	One layer at a time, test after each.
"Done" without evidence	V&V gate and completion report.
Role explosion	Roles only from requirements.
Mock data in production	Layer 2 + release check.
9. Prompt template
ROLE: Release engineer hardening <app> for stable release.
INPUT: prototype report, roles: <...>, security findings: <SEC IDs>.
DO ONE LAYER PER TURN, in order: real persistence → roles/permissions → authentication → authorization → validation/errors → DB access rules → secrets → rate limits/files/audit/dependencies → full regression.
AFTER EACH LAYER: run the core workflow tests and the layer's tests; report ID | FR/NFR | Result | Evidence. Stop if anything fails.
FINISH WITH: completion report (verified, validated, tests run, remaining limitations, external requirements).
NEVER: add roles not in the SRS; skip tests; leave mock-only data.

10. Traceability to the SRS

Every test cites an FR/NFR ID and updates SRS §14 status to Verified (implemented as specified) and Validated (works as intended in the running app).

11. Definition of done (V&V gate)
Verification: every requirement is implemented.
Validation: every implementation works as intended.
Done: both pass, the security baseline is fully ticked, and the completion report is delivered.
Related skills

Previous: SK-06, SK-07, SK-12. Next: SK-14 Deploy and Document.

RELATED LEARNING

Vibe Coding & AI-Assisted Development

28 MIN READ

Ready to hand this to your AI?

Copy the skill, drop it into your project, and require the AI to read it before the first prompt.

COPY SKILL
DOWNLOAD .MD