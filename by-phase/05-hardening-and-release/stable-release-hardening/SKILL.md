---
name: stable-release-hardening
description: Stable release workflow for testing, authentication, authorization, layered security, and verification/validation. Use after a functional prototype works, or when preparing an AI-built app for release, adding auth, securing routes/APIs/data, writing tests, running quality gates, or deciding whether an app is done.
---

# Stable Release Hardening

## Release Principle

Security is the second priority after a functional application. Add hardening in layers and test after each layer so the app remains working.

## V&V Done Gate

- Verification: confirm all requirements are implemented.
- Validation: confirm every implementation works as intended.
- Done: both verification and validation pass.

## Hardening Sequence

1. Confirm the functional prototype works end to end.
2. Replace required mock-only data with real persistence.
3. Define user roles and permissions from the app requirements.
4. Add authentication after functionality unless auth is part of the core feature.
5. Add authorization and protected routes.
6. Add input validation and structured error handling.
7. Add database access rules and ownership checks.
8. Add secure environment variable handling.
9. Add rate limiting, file restrictions, audit logs, and dependency checks where relevant.
10. Test after each layer before continuing.

## Auth And Roles

- Do not assume extra roles without app evidence.
- Ask when admin, owner, super-admin, tenant, or staff permissions are unclear.
- Implement role-specific dashboards, protected routes, and audit logs only when roles require them.

## Testing Requirements

Use both manual browser testing and automated testing where practical. Stable release should cover:

- Core user flows
- Database operations
- Authentication and authorization
- Important edge cases
- Validation and error states
- UI responsiveness and visible breakage
- Security-sensitive routes, inputs, and data access

## Security Baseline

Before stable release, evaluate:

- Input validation
- Auth/session security
- Role-based permissions
- Protected API routes and pages
- Secure environment variables and secret handling
- Database access rules
- Rate limits where relevant
- File upload restrictions where relevant
- Audit logs for important actions
- Dependency and configuration checks

## Completion Report

When finishing, report what was verified, what was validated, what tests ran, and any remaining limitations or external requirements.
