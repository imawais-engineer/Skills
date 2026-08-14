---
name: app-global-preferences
description: Personal global development preferences for AI-assisted application builds. Use when planning, building, reviewing, hardening, documenting, or deploying an app for Awais; when the user asks to apply default preferences; or when deciding default SDLC order, stack, UI, data, testing, security, documentation, or deployment behavior.
---

# App Global Preferences

## Operating Principle

Treat every app request as an end-to-end software product unless the user explicitly scopes it smaller. Build the core requirement first, verify it is present, validate it works, then add real persistence, authentication, security, supporting sections, documentation, and deployment readiness in controlled layers.

## Default Stack

- Prefer Next.js, TypeScript, Tailwind, and full-stack architecture when no stack is specified.
- Prefer Supabase for default persistence, then MongoDB, then PostgreSQL, unless project requirements say otherwise.
- Prefer VPS deployment for full-stack apps unless the client specifies another platform.
- Prefer GitHub plus Vercel auto-deploy for completely static apps.

## Default Build Order

1. Clarify the core requirement and success criteria.
2. Build the main functional workflow first.
3. Use mock data only to prove the workflow early.
4. Test the core workflow manually and automatically where practical.
5. Reorder pages, navigation, and layout after the core flow works.
6. Replace mock-only behavior with real persistence before stable release.
7. Add authentication and authorization after complete functionality unless auth is the core requirement.
8. Add supporting sections one by one, testing and validating each.
9. Add security in layers, testing after each layer.
10. Prepare documentation and deployment only after the app is stable and functional.

## UI Defaults

- Make the app dashboard-first, not landing-page-first, unless the product requires a landing page.
- Use a modern dark aesthetic with consistent gradient treatment.
- Use conventional, non-controversial layouts: sidebar, top navigation, tables, panels, settings, dashboards, and management views.
- Keep theme, spacing, component style, navigation, and visual density consistent across pages.
- Prevent overlap, clipping, hidden controls, unreadable text, and inconsistent responsive behavior.

## Completeness Rules

- Never add placeholders for core functionality.
- Do not imply a working feature visually if the behavior is not implemented.
- If a real feature needs a dependency, credential, service, API, schema decision, or user approval, say exactly: "I need X to add Y functionally."
- Define roles and access control from the app requirements; do not add admin/super-admin complexity when it is not justified.
- Treat AI features as lower priority unless the product is primarily an AI app. Ask for approval before adding secondary AI features.

## Done Definition

- Verification: confirm all stated requirements are added.
- Validation: confirm all implementations work as intended.
- Done: verification and validation are both satisfied.

## Related Skills

- Use `complete-app-blueprint` to expand vague app ideas into full scope.
- Use `dashboard-first-ui` for UI design and page completeness.
- Use `functional-prototype-first` for implementation sequencing.
- Use `data-persistence-design` for schemas, migrations, seed data, and indexes.
- Use `stable-release-hardening` for testing, auth, security, and V&V.
- Use `encapsulation-backend-config` to keep backend configuration, secrets, env names, runtime modes, and provider internals out of public UI and public API responses.
- Use `deploy-and-document` for release documentation and deployment planning.
