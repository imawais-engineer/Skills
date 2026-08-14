---
name: functional-prototype-first
description: Implementation workflow for building the core functional application before authentication, authorization, production hardening, or secondary sections. Use when coding an app, feature, dashboard, workflow, prototype, MVP, or full-stack product where Awais wants functionality proven before stable-release layers.
---

# Functional Prototype First

## Principle

Make the core application work end to end before adding production layers. Authentication, authorization, broad security hardening, and secondary sections should not block the first functional proof unless they are part of the core requirement.

## Implementation Sequence

1. Identify the smallest complete workflow that proves the app's value.
2. Implement that workflow with real UI and real behavior.
3. Use mock data or seed data only as a temporary prototype aid.
4. Avoid placeholders for core behavior.
5. Test the workflow manually in the app.
6. Add focused automated tests where practical.
7. Fix functional and visual defects before expanding scope.
8. Reorder navigation, sections, and page structure after the core flow works.
9. Add each remaining section one by one.
10. Validate each section before moving to the next one.

## Placeholder Policy

- Do not create TODO-only core features.
- Do not add fake buttons, fake dashboards, fake forms, or fake tables for required behavior.
- If an implementation needs missing input, state: "I need X to add Y functionally."
- Temporary mock data is allowed only when clearly used to test the prototype and later replaced before stable release.

## Prototype Completion Check

Prototype is ready for hardening only when:

- The core requirement works end to end.
- Main UI screens render correctly.
- Required interactions perform real state changes.
- Known missing production layers are documented.
- Verification confirms required prototype scope is present.
- Validation confirms implementation behaves as intended.
