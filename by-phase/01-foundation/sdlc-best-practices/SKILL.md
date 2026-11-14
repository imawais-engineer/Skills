---
name: sdlc-best-practices
description: Published skill from SDLC Skills Hub (SRS Architect themed). Extracted and structured for agent use.
source: https://sdlc.base44.app/skill/sdlc-best-practices
priority: foundation-first
---

V1.0.0
SDLC Best Practices

The gate skill. Forces a full discovery discussion and a complete SRS before any code is written, so the build starts from a specification instead of a guess.

SDLC Best Practices

Skill SK-01 · Phase 0 — Gate (Requirements) · Applies to: web apps, Android apps, APIs, AI apps The gate skill. No code is written until a complete, approved SRS exists.

1. Purpose

The most expensive failure in AI-assisted development is building before the requirement is understood. A prompt such as "build me a booking app" is not a specification. When an AI builder codes from it, every gap is filled with a guess; each guess becomes a bug; each bug fix triggers another guess. That is the infinite edit loop.

This skill breaks the loop at its root. It forces a structured discovery, produces a Software Requirements Specification (SRS) in which every requirement has an ID and a testable acceptance criterion, and blocks implementation until a human approves it. Every other skill in this hub traces back to the requirement IDs created here.

2. When to use — and when not to

Use it when:

Starting any new project (web, Android, API, AI app, internal tool).
A change alters scope, data, roles, user flows, integrations, or platforms.
An AI builder has needed more than two correction rounds on the same feature — that is a missing requirement, not a coding problem.

Do not use it for: a typo, a copy change, or a single-property style fix that is reversible in one edit.

3. Inputs required
Input	Source	Required
Idea or brief in the user's own words	User	Yes
Target users and who must be blocked	User	Yes
Platform targets (web, Android, iOS, API)	User / SK-02	Yes
Existing systems, data, or code	User / repository	If any
Constraints: deadline, budget, compliance, team skills	User	If any
Interface direction (Interface Library prompt or "none")	User	Optional
4. Procedure
Step	SDLC phase	Action	Output
1	Discovery	Restate the problem in one sentence and ask the user to confirm it.	Problem statement
2	Discovery	Ask the discovery questions below, at most three per round, and wait. Never answer them yourself.	Discovery notes
3	Analysis	Run the completeness check (section 7). Every failed item becomes the next question.	Gap list
4	Specification	Write the SRS using the template in section 5. Number every requirement.	SRS v0.x
5	Validation	Run the ambiguity check: replace every vague word with a measurable rule.	SRS v1.0 candidate
6	Approval	Present the SRS and stop. Record the approval and date.	Approved SRS v1.0
7	Planning	Convert the SRS into a roadmap and tasks; every task names the FR IDs it satisfies.	Roadmap, task list
8	Build	Implement one task at a time, in roadmap order.	Increment
9	Verify & validate	After each task, run its acceptance criteria and record the result against the FR ID.	Traceability matrix row
10	Change control	Any new or changed behaviour updates the SRS first (new version), then the code.	SRS changelog
Discovery questions
Area	Ask
Problem	What breaks today? How is it handled now? What does success look like in one sentence?
Users	Who uses this? What can each role do that others cannot? Who must be blocked?
Core flow	Walk me through the single most important thing a user does, step by step.
Data	What is created, by whom, and what happens to it later? What must never be lost?
Rules	What is not allowed? Limits, approvals, pricing, eligibility, timing.
Edge cases	What happens on a duplicate, failure, cancellation, offline, or empty state?
Platforms	Web, Android, both? Offline? Installable? Minimum Android version or browsers?
Out of scope	What are we deliberately not building in version one?
Ambiguity rule

These words are banned in requirements unless followed by a measurable definition: fast, simple, modern, clean, user-friendly, secure, scalable, intuitive, etc., some, many, manage, handle, support, appropriate, as needed.

✗ "The page loads fast." → ✓ "NFR-1: The dashboard renders first content in ≤ 2.0 s on a 4G connection (p75)."
✗ "Users can manage their profile." → ✓ "FR-7: A signed-in user can edit name (1–60 chars) and avatar (PNG/JPG ≤ 2 MB); email is read-only."
5. Deliverables
Discovery notes — answers in the user's words.
SRS — exactly this structure (IEEE 29148 aligned):
# Software Requirements Specification — <Project> · v<version> · <date>

## 1. Purpose and problem
## 2. Scope
### 2.1 In scope (v1)
### 2.2 Out of scope (v1)
## 3. Stakeholders and user roles
| Role | Can do | Cannot do | Approx. count |
| --- | --- | --- | --- |
## 4. Platforms and constraints
## 5. Functional requirements
| ID | Requirement (shall) | Priority (Must/Should/Could) | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- |
| FR-1 | | Must | Given … When … Then … |
## 6. Non-functional requirements
| ID | Category | Requirement | Measure |
| --- | --- | --- | --- |
| NFR-1 | Performance | | |
## 7. Data model
| Entity | Fields (type, required) | Owner | Lifecycle states | Access rule |
| --- | --- | --- | --- | --- |
## 8. User flows (numbered steps, including error and empty paths)
## 9. Edge cases
## 10. Assumptions (each confirmed or pending)
## 11. Open questions (blocking / non-blocking)
## 12. Roadmap
| Phase | Outcome | FR IDs | Depends on |
| --- | --- | --- | --- |
## 13. Task list
- [ ] T-1 — <task> — satisfies FR-1 — done when <observable outcome>
## 14. Traceability matrix
| FR ID | Task(s) | Test ID(s) | Status |
| --- | --- | --- | --- |
## 15. Changelog

Roadmap and task list — inside the SRS (sections 12–13).
Traceability matrix — inside the SRS (section 14), updated after every task.
6. Acceptance criteria
Every functional requirement has a unique ID, a priority, and at least one Given/When/Then criterion.
Every NFR has a measurable target.
Every role states both what it can and cannot do.
The out-of-scope list has at least one entry.
No banned ambiguous word appears without a measurable definition.
The human has explicitly approved the SRS version that the build uses.
7. Verification checklist (completeness check)
 Problem statement confirmed by the user.
 All roles listed, with "cannot do" filled in.
 Core flow written as numbered steps, including failure and empty paths.
 Every entity named with fields, owner, lifecycle, and access rule.
 Every FR has ID + priority + Given/When/Then.
 Every NFR has a number (time, size, count, percentage, version).
 Platforms stated (web / Android / both), with offline and minimum-version needs.
 Out of scope is explicit — silence is not scope.
 Every assumption is confirmed or listed as pending.
 Blocking open questions = 0.
 Roadmap and task list exist and every task cites an FR ID.
 Human approval recorded with SRS version and date.
8. Failure modes and anti-loop guards
Failure mode	Symptom	Guard
Infinite edit loop	The same screen is regenerated 3+ times.	Stop editing. Find the FR behind it; if none exists or it lacks Given/When/Then, write it, get approval, then make one edit that cites it.
Building to impress	A generic dashboard nobody asked for.	Only build what an FR ID requires.
Silent assumptions	"Prices in USD" decided nowhere.	Every guess goes to section 10 and must be confirmed.
Scope by omission	Everything is implicitly expected.	Out-of-scope list is mandatory.
Requirements as vibes	"Manage profile" with no fields or rules.	Ambiguity rule (section 4).
Verifying by looking	"It renders, so it's done."	Done = acceptance criteria passed and recorded.
Spec drift	Behaviour changes mid-build; documents lie.	Change control: SRS first, code second.
"Just build it"	User skips discovery.	Reply with the smallest set of questions (≤ 3) that would make the build correct, and ask for one round of answers. Proceed only with an explicit waiver logged as assumptions.
9. Prompt template

Paste into any AI builder (Base44, Lovable, Cursor, Bolt, v0, Claude, ChatGPT) before any build request:

ROLE: You are a senior requirements engineer. You do not write code in this session.
GOAL: Produce an approved SRS for: <one-sentence idea>.
RULES:
1. Ask at most 3 questions per round, grouped by area, each with concrete options. Wait for answers.
2. Never invent answers. Anything you assume goes under "Assumptions" marked PENDING.
3. Every functional requirement gets an ID (FR-n), a priority (Must/Should/Could), and Given/When/Then acceptance criteria.
4. Every non-functional requirement (NFR-n) has a measurable target.
5. Banned without a measurable definition: fast, simple, modern, clean, user-friendly, secure, scalable, manage, handle, support, etc.
6. Include: scope, out of scope, roles (can / cannot), platforms, data model, user flows incl. error and empty paths, edge cases, open questions, roadmap, task list, traceability matrix.
7. When the SRS is complete, print it and STOP. Do not generate code until I reply "APPROVED v1.0".
CONTEXT I ALREADY HAVE: <paste notes, constraints, platform, interface direction>

10. Traceability to the SRS

This skill creates the IDs every other skill uses:

FR-n → functional requirement · NFR-n → non-functional · T-n → task · TC-n → test case.
Rule: every commit, build prompt, or AI edit request cites at least one FR or NFR ID. A change without an ID is a change request — update the SRS first.
11. Definition of done

The gate is passed when the completeness checklist is 100 % ticked, blocking open questions are zero, and the user has approved a specific SRS version. Building may start only then; the project is done only when every Must-priority FR in the traceability matrix shows Verified (implemented) and Validated (works as intended).

Related skills

Next: SK-02 Project Foundations & Architecture → SK-03 Complete App Blueprint → SK-06 Functional Prototype First. Use the SRS Architect in this hub to run this skill interactively.

RELATED LEARNING

Vibe Coding & AI-Assisted Development

28 MIN READ

Ready to hand this to your AI?

Copy the skill, drop it into your project, and require the AI to read it before the first prompt.

COPY SKILL
DOWNLOAD .MD