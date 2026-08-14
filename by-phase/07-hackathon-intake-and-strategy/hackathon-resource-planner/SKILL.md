---
name: hackathon-resource-planner
description: Map hackathon resources, required tools, sponsor technologies, APIs, datasets, SDKs, credits, and allowed platforms into an architecture and implementation plan. Use when a competition brief lists tools, technologies, sponsor resources, required integrations, or restrictions on what can be used.
---

# Hackathon Resource Planner

## Principle

Use the resources that improve eligibility, judging score, and delivery speed. Do not force sponsor tools into the project unless they support the requirements, rubric, or submission category.

## Resource Workflow

1. Classify resources as required, allowed, recommended, optional, or disallowed.
2. Map each required resource to a project feature or architecture component.
3. Identify credentials, API keys, datasets, SDKs, docs, accounts, and rate limits needed.
4. Choose the simplest stack that satisfies requirements and supports a reliable demo.
5. Prefer the user's default app stack when the brief does not specify another stack.
6. Flag any resource that requires approval, paid access, external accounts, sensitive data, or current documentation lookup.
7. Define fallback behavior if a sponsor API or external service fails.

## Architecture Output

Produce:

- Chosen stack
- Required integrations
- Optional integrations
- Data sources
- Environment variables
- Setup risks
- Demo fallback plan
- What must be verified before build

## Default App Stack

When the brief does not specify otherwise, align with the user's defaults:

- Next.js
- TypeScript
- Tailwind
- Full-stack architecture
- Supabase first, then MongoDB, then PostgreSQL
- VPS for full-stack deployment when stable

## Ask Rule

Ask before using paid APIs, non-public datasets, credentials, scraping, external actions, or sponsor services whose terms affect eligibility.

## Done Check

Resource planning is done when every required resource has a purpose, setup path, risk, and validation step.
