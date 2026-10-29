---
name: sdlc-best-practices
description: The gate skill. Forces a full discovery discussion and a complete SRS before any code is written, so the build starts from a specification instead of a guess.
---

# SDLC Best Practices

## Purpose

This skill stops the most expensive failure in AI-assisted software: building before the requirement is understood. A vague prompt is not a specification. When the AI starts coding from one, the app is rebuilt dozens of times and nobody can say whether it is finished.

Read this skill in full before writing any code, creating any file, or generating any screen.

## When to use it

Use it at the start of every new project, and again whenever a change is large enough to alter scope, data, or user flows — a new feature area, a new user role, an integration, a redesign.

Do not use it for a typo fix or a copy change.

## The rule

You must never generate application code until all four artifacts exist and the human has approvingly answered the discovery questions:

1. **Discovery notes** — who the users are, what they do today, what breaks.
2. **SRS** — scope, users and roles, functional requirements, data model, non-functional requirements, out-of-scope list.
3. **Roadmap** — the order work will be done, and why that order.
4. **Task list** — small, verifiable tasks with explicit acceptance criteria.

If any of the four is missing, your only valid output is the next question that completes it. Never fill a gap with an assumption. When you must proceed on an assumption, write it down under "Assumptions" and ask the human to confirm it explicitly.

## The process

### 1. Discuss (no code)
Ask the questions below, a few at a time, and wait for answers. Do not answer them yourself.

| Area | Questions you must ask |
| --- | --- |
| Problem | What breaks today? How is it handled right now? What does success look like in one sentence? |
| Users | Who uses this, and what can each type do that others cannot? Who must be blocked? |
| Core flow | Walk me through the single most important thing a user does, step by step. |
| Data | What is created, by whom, and what happens to it later? What must never be lost? |
| Rules | What is not allowed? Limits, approvals, pricing, eligibility, timing. |
| Edge cases | What happens on a duplicate, a failure, a cancellation, an empty state? |
| Out of scope | What are we deliberately not building in version one? |

### 2. Specify
Produce the SRS using the template below. Every functional requirement gets a numbered ID so it can be referenced later.

### 3. Plan
Turn the SRS into a roadmap of phases, then break each phase into tasks small enough to verify in one sitting. Every task carries an acceptance criterion written as an observable outcome.

### 4. Build
Only now write code, one task at a time, in roadmap order. After each task, state which requirement ID it satisfies and how it was verified.

### 5. Review
At the end of each phase, list what is built, what is verified, what is deferred, and what changed in the SRS. Never silently drift from the spec — update it and say so.

## Required output template

Produce exactly this structure, filled in:

```markdown
# Software Requirements Specification — <Project>

## 1. Problem and goal
## 2. Users and roles
| Role | Can do | Cannot do |
| --- | --- | --- |

## 3. Scope
### In scope
### Out of scope (v1)

## 4. Functional requirements
| ID | Requirement | Acceptance criterion |
| --- | --- | --- |
| FR-1 |  |  |

## 5. Data model
| Entity | Fields | Owner | Rules |
| --- | --- | --- | --- |

## 6. Non-functional requirements
Performance, accessibility, responsiveness, privacy, localization.

## 7. Assumptions to confirm
## 8. Open questions

## 9. Roadmap
| Phase | Outcome | Depends on |
| --- | --- | --- |

## 10. Task list
- [ ] T1 — <task> — satisfies FR-1 — done when <observable outcome>
```

Present the SRS and stop. Wait for explicit approval before phase one.

## Exit criteria

You may start building only when every line below is true:

- [ ] Every user role and what it may and may not do is written down.
- [ ] Every functional requirement has a number and an acceptance criterion.
- [ ] The data model names every entity, its fields, and who owns it.
- [ ] The out-of-scope list is explicit — silence is not scope.
- [ ] Every open question is either answered or logged as an assumption the human confirmed.
- [ ] The roadmap and task list exist, and the human approved them.

## Anti-patterns

- **Building to look impressive.** Generating a dashboard nobody asked for instead of asking what the user does daily.
- **Silent assumptions.** "I assumed prices are in USD" written nowhere, discovered in production.
- **Scope by omission.** Never stating what is out of scope, so everything is implicitly expected.
- **Requirements as vibes.** "Users can manage their profile" — with no fields, no roles, no rules.
- **Verifying by looking.** Calling a feature done because a screen renders, not because an acceptance criterion was checked.
- **Spec drift.** Changing behaviour mid-build without updating the SRS, so the documents lie.

> If the human says "just build it", reply with the smallest set of questions that would make the build correct, and ask for one round of answers.
