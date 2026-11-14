---
name: hackathon-build-roadmap
description: Create timeboxed hackathon build roadmaps that turn requirements, judging strategy, resources, and rules into implementation phases. Use when planning what to build first, creating an MVP, sequencing prototype, UI, data, AI, security, testing, demo, and submission tasks for a competition project.
---

# Hackathon Build Roadmap

## Principle

In a hackathon, a working demo beats an ambitious incomplete system. Build the smallest complete project that satisfies requirements, scores well, and can be submitted cleanly.

## Roadmap Workflow

1. Define the minimum winning demo.
2. Define core user workflow and required screens.
3. Build the functional prototype first with mock or seed data when useful.
4. Validate the core workflow manually.
5. Add required integrations and persistence.
6. Add judging-visible features one by one.
7. Add auth only when required for the demo or before stable release.
8. Add layered security for sensitive data, public demos, and external actions.
9. Add tests for core flows and fragile integrations.
10. Prepare demo, pitch, and submission assets.

## Timebox Structure

Use these phases unless the event timeline requires a different split:

- Phase 1: brief analysis and project decision
- Phase 2: core prototype
- Phase 3: required resources and data
- Phase 4: dashboard and user-facing completeness
- Phase 5: judging differentiators
- Phase 6: test, security, and compliance
- Phase 7: demo, pitch, and submission packaging

## Task Rules

- Tie each task to a requirement, judging criterion, resource, or submission item.
- Do not add placeholder core features.
- Do not overbuild auth, admin, AI, analytics, or deployment unless the brief or demo requires it.
- Keep a visible checklist of verification and validation.
- Prefer completed flows over broad partial coverage.

## Output

Produce:

- Build phases
- Task checklist
- Dependencies and blockers
- Demo-critical path
- Deferred scope
- Testing and validation plan
- Submission preparation tasks

## Done Check

The roadmap is done when the team knows what to build first, what to defer, how to prove it works, and how it maps to the hackathon brief.
