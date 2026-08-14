---
name: encapsulation-backend-config
description: Hide backend configuration, secrets, provider credentials, environment variable names, API keys, runtime modes, internal URLs, task metadata, presigned upload data, and implementation details from public UI/UX and public API responses. Use when building or reviewing settings pages, health/status pages, integrations, API routes, deployment screens, logs, documentation, or security-sensitive application surfaces.
---

# Encapsulation - Backend Configuration

## Principle

Backend configuration is an implementation detail. Public users should see service readiness and product behavior, not credentials, environment variables, provider internals, runtime switches, or secret-handling claims.

## Required Behavior

- Do not display API keys, secret names, environment variable names, credential status, backend URLs, provider account state, demo/mock mode, raw task IDs, file IDs, presigned URLs, upload headers, or internal route names in public UI.
- Do not expose low-level provider responses from public API routes. Return sanitized status, user-safe errors, and product-level results only.
- Replace public configuration/settings pages with a health or readiness page unless authentication and authorization explicitly require an admin-only configuration area.
- Keep live/mock/fallback decisions server-side. The user-facing app should say ready, processing, unavailable, or failed without revealing why the backend chose a path.
- Use generic operational language such as "Application online", "Scan service ready", "Guidance available", and "Processing failed. Try again."
- Treat "API key configured: yes/no", "demo mode enabled", and "secrets are server-side" as sensitive implementation leakage in public UI.

## Public Health Pattern

Use health pages to show:

- Overall app status
- User-facing service readiness
- Last checked time only if useful
- Generic privacy or safety boundary status
- Links back to functional workflows

Do not show:

- Environment variable names
- Provider configuration values
- Secret presence or absence
- Runtime mode toggles
- Raw integration diagnostics
- Internal request, file, task, upload, or polling objects

## API Response Pattern

Public routes should return:

- `status`: product-level state such as `ready`, `processing`, `success`, `failed`, or `unavailable`
- `message` or `error`: user-safe wording
- normalized app data required by the UI

Public routes should not return:

- raw upstream JSON
- internal headers
- presigned URLs
- file IDs
- task IDs unless the client truly needs an opaque polling handle
- secrets or configuration metadata

## Admin Exception

Only create configuration UI when the app explicitly requires admin operations. Protect it with authentication, authorization, audit logging, and least-privilege access. Even then, mask secrets and prefer capability status over raw values.
