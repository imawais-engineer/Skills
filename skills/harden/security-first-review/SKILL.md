---
name: security-first-review
description: Published skill from SDLC Skills Hub (SRS Architect themed). Extracted and structured for agent use.
source: https://sdlc.base44.app/skill/security-first-review
priority: foundation-first
---

V1.0.0
Security First Review

Review applications for security gaps after functional implementation and before stable release. Use when checking auth, authorization, API routes, database access, validation, secrets, file uploads, dependencies, AI features, deployment configuration, audit logs, rate limits, or whether an app is safe to release.

Security First Review

Skill SK-12 · Phase 5 — Hardening & Release (Security review) · Applies to: web apps, Android apps, APIs, AI apps Security is the second priority after a working app. Review in a fixed order, harden in layers, test after each layer.

1. Purpose

AI-generated apps often work and leak at the same time: open database rules, unprotected routes, secrets in the client, AI that obeys injected instructions. Asking an AI to "make it secure" produces vague, sweeping rewrites that break features — another loop. This skill is a structured review: a fixed order, a standard finding format with severity and a concrete fix, and a release gate.

2. When to use — and when not to

Use it after functional implementation and before any stable release; when checking auth, authorization, data access, input validation, secrets, APIs, uploads, AI features or deployment configuration.

Do not use it on a non-functional prototype — make it work first (SK-06). For payments, health/legal data, credentials, multi-tenant data, file processing, public APIs or high-impact automation, escalate to a deeper audit.

3. Inputs required
Input	Source	Required
Working app (prototype passed)	SK-06	Yes
Roles and access rules	SRS §3, §7	Yes
Sensitive data and compliance	SK-02 / SRS §6	Yes
Code, routes, database rules, deployment config	Repository / platform	Yes
4. Procedure — review order
Step	Area	What to check
1	Readiness	Core app is functional enough to review.
2	Threat model	Assets, users, roles, trust boundaries, sensitive data.
3	Authentication	Sign-in, sessions, token storage (Android: no tokens in plain SharedPreferences; use encrypted storage).
4	Authorization	Role checks, protected routes/screens, data ownership on every read and write.
5	Input/output	Validation, output encoding, structured errors.
6	Database	Access rules (RLS), migrations, indexes, seed data, policies.
7	APIs and jobs	API routes, server actions, background jobs, webhooks (signature verification).
8	Secrets and dependencies	Env vars, secret storage, dependency risks, build config (Android: no keys in the APK, ProGuard/R8, exported components).
9	Files and integrations	Upload type/size limits, downloads, third-party integrations, AI features.
10	Deployment	HTTPS, reverse proxy, ports, DNS, logs, process manager, backups.
11	Encapsulation	Apply SK-11 wherever public UI/APIs mention configuration, modes, credentials or provider internals.
AI-specific checks

Prompt-injection boundaries · separation of instructions and untrusted content · output validation before saving or acting · tool/action approval gates · data privacy and retention · usage abuse, rate limits and cost controls · audit logs for AI actions.

Finding format
Field	Content
ID	SEC-n
Severity	Critical / High / Medium / Low
Location	File, route, component or configuration (with line numbers when available)
Risk	Exploit scenario in one or two sentences
Fix	Concrete change
Validation	Test that proves the fix
Requirement	FR/NFR ID affected
5. Deliverables
Threat model summary (assets, roles, trust boundaries).
Findings table in the format above, sorted by severity.
Fix log with validation results, layer by layer.
6. Acceptance criteria
Given user A, when requesting user B's private data through UI or API, then access is denied.
Given an unauthenticated request to a protected route, then it is rejected.
Given the client bundle/APK, then no secrets are present.
Given every Critical and High finding, then it is fixed and its validation test passes.
7. Verification checklist — stable release gate
 Auth and authorization match the required roles.
 Critical inputs validated server-side.
 Secrets not exposed; backend configuration and provider internals not exposed (SK-11).
 Database rules prevent cross-user access.
 Sensitive routes protected.
 Rate limits and audit logs where relevant.
 AI checks passed where AI is used.
 Every fix tested; core workflow still passes.
8. Failure modes and anti-loop guards
Failure mode	Guard
"Make it secure" sweeping rewrites that break features	One finding → one fix → one test; re-run core workflow tests.
Security only in the UI (hidden buttons)	Authorization enforced server-side / in DB rules.
Findings without fixes	Finding format requires Fix and Validation.
Security added before the app works	Readiness step 1.
AI tools obeying injected text	AI-specific checks.
9. Prompt template
ROLE: Application security reviewer. Do not change code until findings are approved.
SCOPE: <app>, roles: <...>, sensitive data: <...>, platforms: <web/Android>.
REVIEW IN ORDER: threat model → authentication → authorization/ownership → input/output → database rules → APIs/jobs/webhooks → secrets/dependencies/build → files/integrations/AI → deployment → encapsulation.
OUTPUT: findings table: ID | Severity | Location (file:line) | Risk | Fix | Validation test | FR/NFR ID.
THEN (after approval): fix one finding at a time, run its validation test and the core workflow tests, report Pass/Fail.
NEVER: rewrite unrelated code; weaken a check to make a test pass.

10. Traceability to the SRS

Security requirements are NFR-SEC IDs; each finding cites the requirement it violates; each fix's validation is a TC ID in SRS §14. New security requirements found in review are added to the SRS first.

11. Definition of done

All Critical and High findings are fixed and validated, the release-gate checklist is fully ticked, the core workflow still passes, and verification and validation both pass.

Related skills

SK-11 Encapsulation · SK-13 Stable Release Hardening · SK-07 Data Persistence Design.

RELATED LEARNING

Vibe Coding & AI-Assisted Development

28 MIN READ

Ready to hand this to your AI?

Copy the skill, drop it into your project, and require the AI to read it before the first prompt.

COPY SKILL
DOWNLOAD .MD