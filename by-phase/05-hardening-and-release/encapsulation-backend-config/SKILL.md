---
name: encapsulation-backend-config
description: Published skill from SDLC Skills Hub (SRS Architect themed). Extracted and structured for agent use.
source: https://sdlc.base44.app/skill/encapsulation-backend-config
priority: foundation-first
---

V1.0.0
Encapsulation - Backend Configuration

Hide backend configuration, secrets, provider credentials, environment variable names, API keys, runtime modes, internal URLs, task metadata, presigned upload data, and implementation details from public UI/UX and public API responses. Use when building or reviewing settings pages, health/status pages, integrations, API routes, deployment screens, logs, documentation, or security-sensitive application surfaces.

Encapsulation - Backend Configuration

Skill SK-11 · Phase 5 — Hardening & Release (Information hiding) · Applies to: web apps, Android apps, APIs, AI apps Public users see product behaviour and service readiness — never credentials, environment names, provider internals or runtime modes.

1. Purpose

AI builders love to show their wiring: "API key configured ✓", "Demo mode on", raw provider JSON in an error toast, a settings page listing environment variables. Each one leaks implementation detail, invites attacks, and creates UI that must be rewritten before launch. This skill defines what the public UI and public API may expose, and the patterns that replace everything else.

2. When to use — and when not to

Use it when building or reviewing any public page, error message, status/health page, settings page, public API route, or Android app screen that touches backend services, AI providers, uploads, or integrations.

Do not apply it to an authenticated, authorized admin area that the requirements explicitly call for — use the Admin exception instead.

3. Inputs required
Input	Source	Required
List of integrations and providers	SK-02 / SK-03	Yes
Public routes and pages	SK-03	Yes
Roles (is there a real admin?)	SRS §3	Yes
4. Procedure
Step	SDLC phase	Action
1	Design	Inventory every public page, toast, error, status display and public API response.
2	Design	Classify each piece of displayed data: product data (allowed) vs implementation detail (forbidden list below).
3	Implementation	Replace public configuration/settings pages with a health/readiness page.
4	Implementation	Move live/mock/fallback decisions server-side; the client only sees ready / processing / unavailable / failed.
5	Implementation	Normalize public API responses to the API response pattern.
6	Implementation	Map upstream errors to user-safe messages; log the raw error server-side only.
7	Verification	Search the client bundle/APK and public responses for forbidden items (key prefixes, env names, provider URLs, "mock", "demo").
Forbidden in public UI and public API responses

API keys and secret names · environment variable names · credential status ("API key configured: yes/no") · backend or provider URLs · provider account state · demo/mock mode flags · raw task IDs, file IDs, presigned URLs, upload headers · internal route names · raw upstream JSON · internal headers · statements like "secrets are server-side".

Public health pattern

Show: overall app status · user-facing service readiness · last checked time (if useful) · generic privacy/safety status · links back to workflows. Use generic language: "Application online", "Scan service ready", "Guidance available", "Processing failed. Try again."

API response pattern
{ "status": "ready | processing | success | failed | unavailable",
  "message": "User-safe wording",
  "data": { "...normalized app data the UI needs..." } }

Opaque polling handles are allowed only when the client truly needs one.

Admin exception

Create configuration UI only when the app explicitly requires admin operations. Protect it with authentication, authorization, audit logging and least privilege. Even then, mask secrets and show capability status rather than raw values.

5. Deliverables
Exposure inventory (page/route → data shown → allowed/forbidden → fix).
Health/readiness page replacing any public config page.
Normalized public API responses and an error-mapping table (upstream error → user message → server log).
6. Acceptance criteria
Given any public page, when inspected, then no forbidden item is visible.
Given an upstream provider failure, when a user triggers the action, then they see a user-safe message and the raw error is only in server logs.
Given the client bundle or APK, when searched for key patterns and env names, then nothing is found.
7. Verification checklist
 Exposure inventory complete.
 No public config/settings page showing backend details.
 Health page uses generic wording.
 Public APIs return status, message, normalized data only.
 Mock/live switching is server-side.
 Bundle/APK and network responses searched for secrets and env names.
 Admin config (if any) authenticated, authorized, audited, masked.
8. Failure modes and anti-loop guards
Failure mode	Guard
"Key configured ✓" badges in the UI	Forbidden list; health pattern.
Raw provider errors in toasts	Error-mapping table.
Demo mode visible to users	Server-side mode decisions.
Secrets bundled into the client or APK	Bundle search in verification step 7.
Re-building settings UI at launch	Decide public vs admin surfaces here, once.
9. Prompt template
ROLE: Security-minded full-stack engineer.
TASK: Encapsulate backend configuration for <app>.
DO:
1. List every public page and public API route and what data each shows.
2. Remove from public UI and responses: API keys, secret/env names, credential status, provider URLs, mock/demo flags, raw task/file IDs, presigned URLs, raw upstream JSON.
3. Replace any public config page with a health page using wording like "Application online", "Service ready", "Processing failed. Try again."
4. Normalize public responses to { status, message, data }. Log raw errors server-side only.
5. Keep live/mock/fallback decisions on the server.
6. Report a table: page/route | leaked item | fix | verified.

10. Traceability to the SRS

Encapsulation is a security NFR (NFR-SEC-4: No public page or public API response exposes credentials, env names, provider internals or runtime modes), verified by TC IDs for each public route in SRS §14.

11. Definition of done

The exposure inventory shows zero forbidden items on public surfaces, public responses follow the response pattern, any admin config is protected and masked, and verification and validation both pass.

Related skills

SK-12 Security First Review · SK-13 Stable Release Hardening · SK-08 AI App Builder.

Ready to hand this to your AI?

Copy the skill, drop it into your project, and require the AI to read it before the first prompt.

COPY SKILL
DOWNLOAD .MD