---
name: data-persistence-design
description: Published skill from SDLC Skills Hub (SRS Architect themed). Extracted and structured for agent use.
source: https://sdlc.base44.app/skill/data-persistence-design
priority: foundation-first
---

V1.0.0
Data Persistence Design

Database and storage design preferences for AI-built applications. Use when selecting a database, designing schemas, replacing mock data, creating migrations, seed data, indexes, relationships, ownership rules, Supabase tables/RLS, MongoDB collections, PostgreSQL schemas, or persistence plans before stable release.

Data Persistence Design

Skill SK-07 · Phase 3 — Data & Persistence · Applies to: web apps, Android apps, APIs, AI apps Design the data layer intentionally — schema, ownership, access rules, migrations, indexes — before writing persistence code.

1. Purpose

An unplanned data model is the deepest source of AI rebuild loops: a missing owner field means rewriting access rules; a missing status field means rewriting every screen. This skill derives the data model from the SRS, chooses the store by explicit rules, and replaces mock data with real, protected persistence before any stable release.

2. When to use — and when not to

Use it when selecting a database, designing schemas or collections, replacing mock data, adding migrations, seed data, indexes, access rules, or offline storage on Android.

Do not use it to change a client-mandated database; record that as a constraint.

3. Inputs required
Input	Source	Required
SRS §7 data model and §3 roles	SK-01	Yes
Entities table and lifecycle	SK-03	Yes
Data store decision or constraint	SK-02	Yes
Sensitive-data and retention rules	SK-02 / SRS §6	Yes
4. Procedure
Step	SDLC phase	Action
1	Analysis	Identify entities from the core workflow and FRs.
2	Design	Choose the database: explicit requirement first; otherwise Supabase → MongoDB → PostgreSQL → another only when justified.
3	Design	Draft the schema: fields, types, defaults, constraints, relationships, ownership, lifecycle states.
4	Design	Define access rules per operation (create/read/update/delete) per role — Supabase RLS, Base44 RLS, or equivalent.
5	Design	Define validation boundaries: what is validated in UI, API/server, and database.
6	Implementation	Write migrations or setup scripts; add seed data that exercises real states (empty, many, edge values).
7	Implementation	Implement reads/writes behind clear service/API boundaries.
8	Implementation	Add indexes for lookup, filter, sort, ownership and joins.
9	Testing	Test create, read, update, delete, validation, cross-user access denial, and failure behaviour.
10	Release	Confirm mock data is removed or isolated before stable release.

Android note: if offline is required, define the local store (Room/SQLite), the sync direction, and the conflict rule (e.g. last-write-wins or server-wins) as explicit requirements.

Ask before choosing when the requirement implies compliance, unusual scale, offline-first, multi-tenant isolation, strict reporting, or a client-mandated provider.

5. Deliverables
## Schema
| Entity | Field | Type | Required | Default | Constraint | Notes |
| --- | --- | --- | --- | --- | --- | --- |
## Access rules
| Entity | Create | Read | Update | Delete |
| --- | --- | --- | --- | --- |
## Indexes
| Entity | Fields | Serves query / FR |
| --- | --- | --- |

Plus migrations/setup scripts, seed data, and a "mock data removed" note.

6. Acceptance criteria
Given user A and user B, when A requests B's private record, then access is denied (tested).
Every entity has an owner field or a documented reason it has none.
Every query used by a list/filter/sort screen has a supporting index.
No required data is stored only locally, fake or temporary at stable release.
7. Verification checklist
 Store chosen by the precedence rule and recorded.
 Schema table complete with types, constraints, ownership, lifecycle.
 Access rules defined per role and per operation.
 Validation boundaries documented.
 Migrations/setup scripts and seed data exist.
 Indexes mapped to queries.
 CRUD, validation, failure and cross-user denial tested.
 Mock data removed or isolated.
8. Failure modes and anti-loop guards
Failure mode	Guard
Schema rewritten mid-build	Schema derived from SRS §7 and approved before persistence code.
Data leak between users	Access rules per operation plus a cross-user test.
App "works" only on mock data	Release check: no mock-only required data.
Slow lists as data grows	Index table tied to screen queries.
Validation only in the UI	Three-layer validation boundaries.
9. Prompt template
ROLE: Senior data engineer.
INPUT: SRS §7 entities, roles (§3), Foundations data store: <paste>.
DO:
1. Output a schema table (entity, field, type, required, default, constraint).
2. Output an access-rule table per entity × operation × role (RLS or equivalent).
3. Output indexes, each mapped to the query/FR it serves.
4. Write migrations/setup and seed data covering empty, typical and edge states.
5. Implement persistence behind a service/API layer; validate on server and database, not only UI.
6. Test CRUD, validation errors, and that user A cannot read or edit user B's private data. Report results per FR ID.
RULE: Do not change fields or rules not required by the cited FRs; list any schema question as "I need X".

10. Traceability to the SRS

Each entity maps to SRS §7; each access rule maps to a role in §3 and a security NFR; each index cites the FR whose screen uses it. Data tests (TC IDs) go into §14.

11. Definition of done

Real persistence replaces all mock-only required data, access rules are enforced and tested (including cross-user denial), migrations and seed data run cleanly, and verification and validation both pass.

Related skills

Previous: SK-06 Functional Prototype First. Next: SK-13 Stable Release Hardening, SK-12 Security First Review.

Ready to hand this to your AI?

Copy the skill, drop it into your project, and require the AI to read it before the first prompt.

COPY SKILL
DOWNLOAD .MD