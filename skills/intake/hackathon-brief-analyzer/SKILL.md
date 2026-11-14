---
name: hackathon-brief-analyzer
description: Parse hackathon and competition briefs into structured requirements, constraints, judging criteria, deliverables, resources, rules, risks, and missing information. Use when the user provides overview, requirements, what to submit, judging criteria, tools, technologies, resources, rules, tracks, prizes, deadlines, or eligibility details.
---

# Hackathon Brief Analyzer

## Principle

Do not design first. Extract the competition facts first, then separate mandatory requirements from useful context and assumptions.

## Analysis Workflow

1. Identify the hackathon name, theme, tracks, deadline, team constraints, and target audience.
2. Extract overview into problem space, intended impact, sponsors, and domain.
3. Extract requirements into mandatory, optional, and ambiguous requirements.
4. Extract what to submit into exact deliverables and formats.
5. Extract judging criteria into rubric categories, weights, and evidence needed.
6. Extract resources into required tools, allowed tools, suggested technologies, APIs, datasets, credits, SDKs, and docs.
7. Extract rules into eligibility, restrictions, licensing, IP, data, safety, submission, and demo constraints.
8. List missing information and questions that affect project choice or eligibility.

## Output Format

Produce:

- Brief summary
- Mandatory requirements
- Optional opportunities
- Submission checklist
- Judging rubric map
- Resource/tool map
- Rules and restrictions
- Risks and blockers
- Open questions
- Initial project implications

## Extraction Rules

- Quote or paraphrase exact constraints when they affect eligibility or submission.
- Do not invent technologies, features, APIs, or tracks.
- Mark assumptions clearly.
- Flag contradictions between requirements, resources, and rules.
- Treat deadlines and submission formats as hard constraints.

## Done Check

The brief is analyzed when a builder can see what must be built, what must be submitted, what will be judged, what resources are allowed, and what rules cannot be violated.
