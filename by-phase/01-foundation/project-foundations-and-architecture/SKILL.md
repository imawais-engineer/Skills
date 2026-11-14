---
name: project-foundations-and-architecture
description: Published skill from SDLC Skills Hub (SRS Architect themed). Extracted and structured for agent use.
source: https://sdlc.base44.app/skill/project-foundations-and-architecture
priority: foundation-first
---

V1.0.0
Project Foundations & Architecture Decisions

Lock the platform, stack, access model and privacy baseline before any code is written — asking only the questions that change the build.

Project Foundations & Architecture Decisions

Skill SK-02 · Phase 1 — Foundation (Architecture decisions) · Applies to: web apps, Android apps, APIs, AI apps Lock the decisions that are expensive to change — platform, stack, access model, data and privacy — before any file is generated.

1. Purpose

Most rebuild loops come from a foundational decision being made silently by the AI instead of explicitly by the user: web when the user needed Android, no login when data was per-person, a database the team cannot operate. This skill does not prescribe a stack. It makes missing decisions visible, offers a small set of grounded options, and produces a confirmed Foundations Record that the SRS (SK-01), the blueprint (SK-03) and the build must follow.

2. When to use — and when not to

Use it when:

Starting a new app, a major feature set, or a rebuild.
The request names no platform, stack, access model, or data store.
A new request conflicts with decisions already recorded.

Do not use it mid-build to re-litigate settled decisions. If a genuine conflict appears, apply Conflict handling (step 6) to the affected area only.

3. Inputs required
Input	Source	Required
Idea or brief, discovery notes	User / SK-01	Yes
Existing code, systems, accounts	Repository / user	If any
Team skills and who operates the app after handoff	User	Yes
Constraints: deadline, budget, compliance, client policy	User	If any
Interface direction (Interface Library)	User	Optional
4. Procedure
Step	SDLC phase	Action	Output
1	Discovery	Extract before you ask. Mine the brief, files, and prior chat for every intake area below. Remove answered items from the question list.	Intake table
2	Analysis	Apply the question selection test to each remaining gap.	Material gaps
3	Discovery	Ask in rounds of ≤ 3 questions, grouped by decision area, each with concrete options.	Answers
4	Design	For "you decide" answers, apply the recommendation rules.	Recommended decisions
5	Design	Classify each item Decided / Recommended / Assumed and blocking / non-blocking.	Decision log
6	Design	Surface conflicts in one sentence with two viable resolutions. Never choose silently.	Resolved conflicts
7	Approval	Present the Foundations Record (section 5) and ask for one confirmation.	Confirmed record
8	Handoff	Pass the record unchanged to SK-01 (SRS sections 4, 6, 7) and SK-03.	Handoff
Intake — what to extract
Area	Look for
Goal	the problem, the outcome, why now
Users	who, internal or public, rough scale
Core workflow	the one path that must work end to end
Scope edges	what is explicitly out of scope
Platforms	web, responsive PWA, native Android/iOS, cross-platform (React Native / Flutter), desktop, API, CLI
Stack	languages, frameworks, backend, database, storage
Access	public or accounts, roles, per-user data
Data	what is stored, what is sensitive
Integrations	payments, email, auth provider, AI models, maps, analytics
Constraints	deadline, budget, team skills, existing systems
Decision areas
A. Problem, users, scope — blocking. Ask: "What single workflow must work end to end in v1?" and "Who uses it, and roughly how many?"
B. Platform and delivery — blocking. Never assume web because it is the default. For Android, also record minimum SDK / Android version, distribution (Play Store, APK, internal), offline needs, and device permissions (camera, location, notifications).
C. Technology architecture — settle only where the user has a preference, existing system, or hard constraint; otherwise recommend and mark Assumed. Rules: smallest stack that meets the requirements; what the team can operate after handoff; managed services unless control is required; no paid accounts or keys the user has not agreed to; keep a user-stated stack (note a real risk once, then proceed).
D. Accounts, privacy, permissions — blocking. Public or accounts? Who may sign up? Per-user private data? Roles? Sensitive data (personal, health, payments, documents)? Can one user see another's records? Deletion/export requests? Ask directly about public content with private submissions — the most commonly missed case.
E. Security and operations baseline — record as requirements: auth method, CRUD permission per record type, where secrets live and who owns them, validation and abuse protection on public forms, backups/export, applicable regulation.
F. Constraints — timeline, budget, reuse, team skills, approvals, lock-in, offline, localization, accessibility.
G. Interface direction — never invent one, never substitute adjectives ("modern", "clean", "premium") — they are a top source of endless UI edits. Point the user to the Interface Library (Interfaces tab of this hub); record the chosen direction and carry its prompt verbatim, or record "none selected" and keep neutral defaults.
Question selection test

A question is material only if a different answer would change at least one of: (1) the data model, (2) screens or navigation, (3) access rules, (4) deploy target, (5) integrations. Do not ask about naming, colours, copy, or file layout. If an answer can be inferred from a stated constraint, ask it as a confirmation, not open-ended.

Recommendation rules

When the user says "you decide": give one recommendation with a one-line reason, at most two alternatives with one-line trade-offs, mark it Recommended, and ask for a single confirmation. Prefer fewer moving parts, lower operating cost, and what the user can support.

Conflict handling
Situation	Resolve by asking
Mobile app requested, stack only supports server-rendered web	native Android, cross-platform, or PWA
Public app with per-user private records	login required, or local-only storage
No login, but data must persist per person	anonymous device storage or accounts
Tight deadline with custom auth and infrastructure	managed service vs reduced scope
User stack cannot meet a stated requirement	which requirement gives way, or which choice changes
5. Deliverables

Foundations Record — present exactly this block (≤ 30 lines), filled in:

Project Foundations — v<version> · <date>

Product:        <name and one-line purpose>
Users:          <who, roughly how many>
Core workflow:  <the path that must work end to end>
Out of scope:   <explicit exclusions>
Platforms:      <day-one targets; Android min version; offline/installable>
Interface:      <Interface Library direction, or none selected>
Architecture:   <layer -> decision (Decided | Recommended | Assumed)>
Access model:   <public, accounts, roles>
Data & privacy: <what is stored, what is sensitive, who sees it>
Security:       <auth method, access rules, secrets owner>
Operations:     <hosting, backups, integrations>
Constraints:    <deadline, budget, existing systems>
Open questions: <none, or the blocking items left>

Status: Ready to build | Blocked on <items>

6. Acceptance criteria
Every blocking item is Decided, Recommended-and-confirmed, or explicitly waived by the user.
Every Assumed item is labelled as such — none is presented as the user's decision.
The record maps into SRS sections 3, 4, 6 and 7 without contradiction.
The user confirmed the record in writing.
7. Verification checklist
 Intake extracted before any question was asked.
 Each question passed the selection test; ≤ 3 per round.
 Platform decided (never defaulted); Android specifics recorded if relevant.
 Access model and per-user privacy decided, including "public content, private submissions".
 Data store and secrets owner decided.
 Required integrations listed with who supplies credentials.
 Interface direction recorded or "none selected".
 Conflicts stated with two resolutions and resolved by the user.
 Foundations Record ≤ 30 lines and confirmed.
8. Failure modes and anti-loop guards
Failure mode	Guard
A twelve-question wall that delays a build the user can already describe	Extract first; ≤ 3 material questions per round.
Silently defaulting to web, React, a relational DB, or login-required	Platform, data store and access model are blocking.
Asking about design, copy or naming in foundation work	Question selection test.
Inventing users, scale or compliance needs	Use the user's words; label anything else Assumed.
Recommending infrastructure the user cannot operate	"Operable after handoff" rule.
Overriding the user's stack silently	Note the risk once, then proceed with their choice.
Rebuild loop after a platform switch (web → Android) late in the build	Platform is decided and confirmed here, before scaffolding.

Build gate: do not scaffold, install packages, or write feature code while a blocking item is unresolved. If the user insists, name what is missing in one line, proceed only with an explicit waiver, and mark waived items Assumed.

9. Prompt template
ROLE: You are a software architect running a foundations interview. No code in this session.
INPUT: <brief / discovery notes / existing system notes>
DO:
1. Extract goal, users, core workflow, scope edges, platforms, stack, access, data, integrations, constraints from the input. Do not ask about anything already answered.
2. Ask only material questions (they change data model, screens, access rules, deploy target, or integrations). Max 3 per round, each with concrete options.
3. For "you decide": one recommendation + one-line reason, max two alternatives with trade-offs.
4. Label every decision Decided / Recommended / Assumed. State conflicts with two resolutions; never pick silently.
5. Output the Project Foundations record (≤ 30 lines) with Status: Ready to build | Blocked on <items>, then STOP and wait for "CONFIRMED".
NEVER: default to web or login-required, invent compliance or scale, use adjectives instead of decisions.

10. Traceability to the SRS
Foundations field	SRS section
Product, Core workflow, Out of scope	§1, §2, §8
Users, Access model	§3 (roles: can / cannot)
Platforms, Constraints	§4
Security, Data & privacy	§6 (NFR-security), §7 (access rule column)
Open questions, Assumed items	§10, §11

Each Decided item that constrains behaviour becomes an NFR (e.g. NFR-3: The app runs on Android 8.0+ (API 26)).

11. Definition of done

The Foundations Record is confirmed by the user, shows Status: Ready to build, and has been copied into the SRS. Later skills must not contradict it without raising a conflict.

Related skills

Previous: SK-01 SDLC Best Practices. Next: SK-03 Complete App Blueprint, then SK-05 Dashboard First UI or SK-06 Functional Prototype First, then SK-07 Data Persistence Design.

Ready to hand this to your AI?

Copy the skill, drop it into your project, and require the AI to read it before the first prompt.

COPY SKILL
DOWNLOAD .MD