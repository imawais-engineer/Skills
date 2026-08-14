---
name: security-first-review
description: Review applications for security gaps after functional implementation and before stable release. Use when checking auth, authorization, API routes, database access, validation, secrets, file uploads, dependencies, AI features, deployment configuration, audit logs, rate limits, or whether an app is safe to release.
---

# Security First Review

## Principle

Security is the second priority after a working application. Review and harden in layers, testing after each layer so functionality stays intact.

## Review Order

1. Confirm the core app is functional enough to review.
2. Identify assets, users, roles, trust boundaries, and sensitive data.
3. Review authentication and session handling.
4. Review authorization, role checks, protected routes, and data ownership.
5. Review input validation, output encoding, and structured errors.
6. Review database rules, migrations, indexes, seed data, and access policies.
7. Review API routes, server actions, background jobs, and webhooks.
8. Review secrets, environment variables, dependency risks, and build configuration.
9. Review file uploads, downloads, external integrations, and AI features when present.
10. Review deployment configuration: HTTPS, reverse proxy, ports, DNS, logs, process manager, and backups.
11. Apply `encapsulation-backend-config` when any public UI or public API route mentions backend configuration, runtime mode, credential state, provider metadata, raw task objects, or internal integration details.

## AI-Specific Checks

When the app uses AI, check:

- Prompt injection boundaries
- Separation of instructions and untrusted content
- Output validation before saving or acting
- Tool/action approval gates
- Data privacy and retention
- Usage abuse, rate limits, and cost controls
- Audit logs for AI actions

## Finding Format

For each finding, include:

- Severity
- Affected file, route, component, or configuration
- Risk and exploit scenario
- Concrete fix
- Validation step after the fix

If reviewing code, cite file paths and line numbers when available.

## Stable Release Gate

Do not call an app release-ready until:

- Auth and authorization match the required roles.
- Critical inputs are validated.
- Secrets are not exposed.
- Backend configuration and provider internals are not exposed in public UI or public API responses.
- Database access rules prevent cross-user data access.
- Sensitive routes are protected.
- Relevant rate limits and audit logs exist.
- Security fixes are tested.
- Verification and validation both pass.

## Escalation

Use a deeper security audit workflow when the app handles payments, health/legal data, credentials, multi-tenant data, file processing, public APIs, or high-impact automation.
