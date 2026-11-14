---
name: deploy-and-document
description: Published skill from SDLC Skills Hub (SRS Architect themed). Extracted and structured for agent use.
source: https://sdlc.base44.app/skill/deploy-and-document
priority: foundation-first
---

V1.0.0
Deploy And Document

Deployment and documentation preferences for AI-built apps. Use when preparing stable functional apps for VPS deployment, static Vercel deployment, GitHub push workflow, subdomain/DNS planning, reverse proxy setup, SSL, ports, environment files, release notes, setup docs, testing checklists, or deployment instructions.

Deploy And Document

Skill SK-14 · Phase 6 — Deployment & Documentation · Applies to: web apps (VPS, static), Android apps (Play Store / APK), APIs Deploy only what is stable, tested and validated — to an exact, verified target — and leave documentation that lets anyone run it.

1. Purpose

Deployment is where small unknowns become outages: a port already in use, a subdomain that loads another app, a missing environment variable, an unsigned APK. AI builders tend to "just deploy" and then iterate in production. This skill makes deployment a checklist-driven release with an exact target, safe routing on shared servers, and the documentation set that makes the app operable after handoff.

2. When to use — and when not to

Use it when preparing a stable, functional app for release: VPS deployment, subdomains, DNS, SSL, reverse proxy, static Vercel deployment, Android release builds, and project documentation.

Do not use it to ship a build that has not passed SK-13 — unless the user explicitly asks for an early preview deployment, which is labelled as such.

3. Inputs required
Input	Source	Required
V&V completion report	SK-13	Yes
Hosting decision	SK-02 / SK-04	Yes
Domain / subdomain and DNS access owner	User	Web
Signing key owner, package name, store listing	User	Android
Environment variables list (names only)	Build	Yes
4. Procedure
Default targets
Full-stack apps → VPS unless requirements say otherwise.
Completely static apps → build, push to GitHub, Vercel auto-deploy.
Android → signed release build (AAB for Play Store, APK for direct distribution).
Client/project requirements always override defaults.
VPS release
Step	Action
1	Ask whether the VPS hosts other apps. If unknown, inspect running services, occupied ports, Nginx/Caddy virtual hosts, certificates and DNS records before changing anything.
2	Choose a dedicated unused localhost port for the app.
3	Confirm the exact FQDN (e.g. app.example.com) and create the DNS A (and AAAA if used) record to the VPS IP.
4	Create an explicit reverse-proxy virtual host for that exact hostname; check for conflicting server_name, wildcard, default and catch-all blocks.
5	Verify public DNS from at least two resolvers.
6	Verify HTTP with the intended Host header before requesting SSL.
7	Issue SSL for the exact subdomain (Let's Encrypt/Certbot or equivalent); verify HTTPS with SNI.
8	Configure process management (Docker Compose, PM2, systemd), environment variables, restart/update workflow, logs and health checks.
9	Ensure a safe default/catch-all so unknown hostnames do not load another app.
10	Validate the target subdomain loads the correct app and unrelated domains still route correctly.

Shared VPS rule: DNS only maps every subdomain to the same IP; the reverse proxy must route by hostname. If the user must configure DNS manually, give only the exact record values, then continue once it resolves.

Static Vercel release

Build locally → push to GitHub → deploy via Vercel → confirm future pushes auto-deploy.

Android release

Set versionCode/versionName → build a signed release (keystore owned by the user, never committed) → enable R8/minification → test the release build on a device → upload to the chosen track (internal → closed → production) with privacy policy and data-safety form completed.

Documentation set

Roadmap · architecture notes · database schema notes · API documentation · .env.example (names only, no values) · setup instructions · deployment instructions · testing checklist · changelog / release notes.

5. Deliverables
Deployed app at the confirmed URL (or store track) with health check.
Deployment record: host, port, FQDN, DNS records, SSL method, process manager, env var names, rollback steps.
Documentation set above, committed with the code.
6. Acceptance criteria
Given the target FQDN, when opened over HTTPS, then the correct app loads with a valid certificate.
Given another app's domain on the same VPS, when opened, then it still loads its own app.
Given an unknown hostname, when requested, then it does not load this or another app.
Given a fresh machine and the setup docs, when followed, then the app runs.
7. Verification checklist — release check
 Requirements verified; implementation validated (SK-13).
 Tests ran, or missing tests disclosed.
 Real persistence in place where required.
 Auth/security present for stable release.
 Port, subdomain, DNS target, SSL approach and process manager specified (VPS).
 Hostname routing, SNI certificate and default-host behaviour verified on shared VPS.
 Android: signed release build tested; keystore stored by owner.
 Documentation set complete; .env.example has no values.
 Rollback steps written.
8. Failure modes and anti-loop guards
Failure mode	Guard
New app hijacks another app's domain	Explicit virtual host + default catch-all + cross-domain validation.
Port collision	Inspect occupied ports first; dedicated port.
SSL requested before DNS resolves	DNS check from two resolvers, HTTP Host test first.
Iterating in production	Deploy only after V&V; preview deployments labelled.
Undocumented setup	Documentation set is a deliverable, not optional.
9. Prompt template
ROLE: DevOps engineer releasing <app>.
TARGET: <VPS | Vercel static | Android Play/APK>. FQDN: <app.example.com>. VPS IP: <x.x.x.x>. Other apps on VPS: <list or "unknown — inspect first">.
DO: (VPS) inspect services/ports/vhosts → pick free port → DNS A/AAAA → explicit vhost for exact hostname → verify DNS (2 resolvers) → HTTP Host test → SSL for exact name → SNI check → process manager, env vars, logs, health check → safe default host → validate target and other domains.
DOCS: roadmap, architecture, schema, API, .env.example (names only), setup, deploy, testing checklist, changelog.
REPORT: deployment record + release checklist with Pass/Fail. Ask for exact DNS/credential inputs as "I need X".
NEVER: deploy unvalidated builds as stable; print secret values; change other apps' config.

10. Traceability to the SRS

Hosting and availability constraints are NFRs (NFR-OPS-1: served over HTTPS at app.example.com, NFR-OPS-2: health endpoint returns 200); release checks are TC IDs; the release notes list the FR IDs included in the version.

11. Definition of done

The app runs at the confirmed target with valid HTTPS (or is live on the chosen store track), routing on shared hosts is verified both ways, the documentation set is complete, the release check is fully ticked, and the release notes list the included FR IDs.

Related skills

Previous: SK-13 Stable Release Hardening. Defaults: SK-04 App Global Preferences.

Ready to hand this to your AI?

Copy the skill, drop it into your project, and require the AI to read it before the first prompt.

COPY SKILL
DOWNLOAD .MD