---
name: project-foundations-and-architecture
description: Lock the platform, stack, access model and privacy baseline before any code is written — asking only the questions that change the build.
---

# Project Foundations & Architecture Decisions

## Purpose

Capture the decisions that cannot be changed cheaply later — what the product is for, who uses it, where it runs, what it is built with, and who may see the data — before a single file is generated. Most rebuild loops come from one of these being decided silently by the assistant instead of explicitly by the user.

This skill does not prescribe a stack. It makes missing decisions visible, offers a small set of grounded options, and produces a confirmed summary that downstream skills and the build itself must follow.

## When to apply

- At the start of a new app, a major feature set, or a rebuild.
- When the request names no platform, no stack, no access model, or no data store.
- When a new request conflicts with decisions already recorded.

Do not apply mid-build to re-litigate settled decisions. If a genuine conflict appears, use Conflict Handling and stop at the affected area only.

## Operating rules

1. Extract before you ask. Mine the request, any attached brief, existing project files, and prior conversation for: goal, users, core workflow, platforms, stack, access model, data, integrations, deadlines.
2. Ask only material questions (see Question Selection Test). Silence on an immaterial point is not a gap.
3. Ask in rounds of at most three questions, grouped by decision area, each with concrete options.
4. Never invent a decision and present it as the user's. Anything you chose yourself is labelled Assumed or Recommended.
5. Use the user's own words for goals and scope. Do not expand the product while clarifying it.
6. Surface conflicts explicitly instead of quietly picking one side.
7. Confirm the summary before building. Unconfirmed assumptions are the root cause of rework.
8. Plain language. Name trade-offs, costs, and operational burden; avoid unexplained jargon.

## Intake — what to extract

| Area | Look for |
| --- | --- |
| Goal | the problem, the outcome, why now |
| Users | who uses it, internal or public, rough scale |
| Core workflow | the one path that must work end to end |
| Scope edges | what is explicitly out of scope |
| Platforms | web, mobile, desktop, API, CLI |
| Stack | languages, frameworks, backend, database, storage |
| Access | public or accounts, roles, per-user data |
| Data | what is stored, what is sensitive |
| Integrations | third-party services, payments, email, AI |
| Constraints | deadline, budget, team skills, existing systems |

Anything already answered here is removed from the question list.

## Decision areas

### A. Problem, users and scope

- Decided when: the core workflow is named and the audience is clear.
- Missing when: the request is a feature list with no workflow, or the audience is ambiguous (consumer vs internal team).
- Ask: 'What is the single workflow that has to work end to end in the first version?' and 'Who uses it, and roughly how many?'
- Blocking: yes. Screens, data model and access rules all derive from this.

### B. Platform and delivery targets

- Options: browser web app; responsive web plus installable PWA; native iOS and Android; cross-platform mobile (React Native or Flutter); desktop (Electron or Tauri); API or service only; a stated combination.
- Why material: it changes UI framework, navigation, offline behaviour, auth flows, and where the app is deployed and distributed.
- Ask: 'Where does this need to run on day one, and does it need to work offline or be installable?'
- Blocking: yes. Never assume web because it is the default path.

### C. Technology architecture

Only settle these where the user has a preference, an existing system, or a hard constraint. Otherwise recommend and mark as Assumed.

- Frontend: React, Vue, Svelte, plain HTML/CSS/JS, React Native, Flutter.
- Backend: managed backend-as-a-service; Node with Express or similar; Python with FastAPI or similar; serverless functions; none (static plus third-party APIs).
- Database: managed PostgreSQL or another relational store; document store; embedded or local storage; none.
- File storage: managed object storage; the platform's own file storage; none required.
- Hosting: platform hosting; managed static or serverless hosts; a cloud VM; containers.
- Integrations: payments, email, auth provider, AI models, maps, analytics.

Decision rules:

- Prefer the smallest stack that satisfies the stated requirements.
- Prefer what the user or their team can actually operate after handoff.
- Prefer managed services unless a requirement demands infrastructure control.
- Do not require accounts, keys, or paid services the user has not agreed to.
- If the user states a stack, keep it. Note a genuine risk once, then proceed with their choice.

### D. Accounts, privacy and permissions

- Questions: public or accounts? who may sign up? is there per-user private data? are there roles (admin, staff, customer)? what is sensitive (personal details, health, payments, documents)? may one user see another's records? are deletion or export requests expected?
- Public content with private submissions is the most commonly missed case. Ask it directly rather than inferring it.
- Blocking: yes. It determines the security rules that must exist from the first write, not later.

### E. Security and operations baseline

Record as requirements, not as implementation detail:

- how users authenticate (email and password, social login, single sign-on, no login)
- who may create, read, update, delete each kind of record
- where secrets and API keys live, and who owns them
- input validation and abuse protection for public forms
- backups or export expectations
- any regulatory or client policy that applies

### F. Constraints

Timeline, budget, existing systems that must be reused, team skills, third-party approvals, vendor lock-in, offline needs, localization, accessibility.

## Question selection test

A question is material only if a different answer would change at least one of:

1. the data model
2. the screens or navigation
3. the access rules
4. the deploy target
5. the integrations

Do not ask about naming, colours, copy, file layout, or anything reversible in a single edit. Those belong to later skills.

If the answer is already stated, do not ask. If it can be inferred confidently from a stated constraint, state the inference as a question of confirmation rather than asking it open-ended.

## Recommendation rules

When the user says 'you decide', 'recommend', or gives a vague answer:

1. Give one recommendation with a one-line reason.
2. Offer at most two alternatives, each with a one-line trade-off.
3. Mark the choice Recommended in the summary and ask for a single confirmation.
4. Prefer fewer moving parts, lower operational cost, and the option the user can support.

## Conflict handling

| Situation | Resolve by asking |
| --- | --- |
| Mobile app requested, stack only supports server-rendered web | native, cross-platform, or PWA |
| Public app with per-user private records | access model: login required, or local-only storage |
| No login requested, but data must persist per person | anonymous device storage or accounts |
| Tight deadline with custom auth and infrastructure | managed service versus reduced scope |
| User states a stack that cannot meet a stated requirement | which requirement gives way, or which choice changes |

State the conflict in one sentence, then the two viable resolutions. Do not choose silently.

## Blocking versus non-blocking

Blocking — must be resolved or explicitly waived before build:

- target platform
- access model and privacy of user data
- where data lives (database, local, none)
- required third-party integrations and who supplies credentials
- secrets and API keys the build depends on

Non-blocking — record as assumptions and move on:

- component library and design system
- file and folder naming
- test framework
- analytics provider
- copy and branding

## Confirmation summary

Present exactly this block, filled in, and ask for a single confirmation:

```
Project Foundations

Product:        <name and one-line purpose>
Users:          <who, roughly how many>
Core workflow:  <the path that must work end to end>
Out of scope:   <explicit exclusions>
Platforms:      <day-one targets, offline or installable needs>
Architecture:   <layer -> decision (Decided | Recommended | Assumed)>
Access model:   <public, accounts, roles>
Data & privacy: <what is stored, what is sensitive, who sees it>
Security:       <auth method, access rules, secrets owner>
Operations:     <hosting, backups, integrations>
Constraints:    <deadline, budget, existing systems>
Open questions: <none, or the blocking items left>

Status: Ready to build | Blocked on <items>
```

Keep it under 30 lines. It is a decision record, not a document.

## Build gate

Do not scaffold, install packages, or write feature code while a blocking item is unresolved. If the user asks to start anyway, name what is missing in one line, proceed only with their explicit waiver, and mark the waived items Assumed in the summary.

## Handoff

After confirmation, pass the summary unchanged to the next skill. It is the input for every later phase; later skills must not contradict it without raising a conflict.

Next in sequence: Complete App Blueprint (foundation planning), then Dashboard First UI or Functional Prototype First, then Data Persistence Design.

## Anti-patterns

- A twelve-question wall that delays a build the user can already describe.
- Silently defaulting to web, React, a relational database, or login-required.
- Asking about design, copy, or naming during foundation work.
- Inventing users, scale, or compliance needs the user never mentioned.
- Recommending infrastructure the user cannot operate after handoff.
- Restating the user's stack as your recommendation, or overriding their choice without saying so.

