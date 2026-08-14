---
name: data-persistence-design
description: Database and storage design preferences for AI-built applications. Use when selecting a database, designing schemas, replacing mock data, creating migrations, seed data, indexes, relationships, ownership rules, Supabase tables/RLS, MongoDB collections, PostgreSQL schemas, or persistence plans before stable release.
---

# Data Persistence Design

## Database Selection

Follow project or client requirements first. When unspecified, prefer:

1. Supabase
2. MongoDB
3. PostgreSQL
4. Another database only when the app requirements justify it

## Prototype Versus Stable Release

- Use mock data or seed data during the prototype when it helps validate functionality faster.
- Mark mock-only behavior clearly in the implementation notes.
- Before first stable release, replace mock-only storage with real persistence.
- Do not call the app stable while required data is still only local, fake, or temporary.

## Required Data Design

Always design the data layer intentionally:

- Entities/tables/collections
- Fields, types, defaults, and constraints
- Relationships and ownership rules
- Migrations or setup scripts
- Seed data for local testing
- Indexes for expected queries
- Validation boundaries between frontend, backend, and database
- Access rules such as Supabase RLS or equivalent when auth exists

## Data Workflow

1. Identify data entities from the core workflow.
2. Choose the database using explicit requirements, then defaults.
3. Draft schema/collection design before writing persistence code.
4. Add seed data that exercises real app states.
5. Implement reads and writes behind clear service/API boundaries.
6. Add indexes for lookup, filtering, sorting, ownership, and joins.
7. Test create, read, update, delete, validation, and failure behavior.
8. Confirm mock data is removed or isolated before stable release.

## Ask Rule

Ask before choosing a database when the requirement implies compliance, unusual scale, offline-first behavior, multi-tenant isolation, strict reporting, or a client-mandated provider.
