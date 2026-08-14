---
name: complete-app-blueprint
description: Expand an application idea into a complete software blueprint before implementation. Use when a prompt asks to build an app, SaaS, dashboard, portal, admin system, internal tool, marketplace, AI app, CRUD system, or any feature that may need pages, workflows, roles, data, APIs, dashboards, security, tests, documentation, or deployment.
---

# Complete App Blueprint

## Goal

Prevent narrow AI builds that implement only the visible feature. Map the complete application surface before coding, while still preserving the preference to build the core function first.

## Blueprint Workflow

1. Restate the core requirement in one sentence.
2. Define primary users and roles from the requirement. Ask if roles are unclear.
3. List the core workflow that proves the app's value.
4. List required pages and sections.
5. List data entities, relationships, ownership, and lifecycle states.
6. List backend/API capabilities, integrations, background jobs, and files if relevant.
7. List UI states: loading, empty, error, success, disabled, validation, and responsive behavior.
8. List security, auth, and permission needs for stable release.
9. List tests needed for prototype and stable release.
10. List documentation and deployment needs.

## Page And Section Map

Consider these sections and include only those that serve the app:

- Dashboard
- Sidebar and top navigation
- Core workflow pages
- CRUD management pages
- Detail pages
- Search, filters, sorting, and pagination
- Analytics or reports
- Activity/history logs
- Notifications
- Settings
- Profile/account
- Admin panel when roles require it
- Help/docs/about pages when useful
- Landing/pricing pages only when product context requires them

## Roadmap Output

Produce the build plan in this order:

1. Functional prototype: core workflow with mock or seed data.
2. Prototype validation: prove the workflow works.
3. Data layer: schema, migration, seed data, indexes, and persistence.
4. UI completion: sections implemented one by one.
5. Auth and authorization: added after working functionality unless required earlier.
6. Security hardening: layered, with tests after each layer.
7. Documentation and deployment readiness.

## Escalation Rule

Do not hide missing dependencies. If the app needs a decision or external input to become functional, state exactly what is needed before continuing.
