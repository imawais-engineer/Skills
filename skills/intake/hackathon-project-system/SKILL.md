---
name: hackathon-project-system
description: Orchestrate hackathon and competition project creation from a supplied brief. Use when the user provides or references overview, requirements, what to submit, judging criteria, resources, tools, technologies, rules, prizes, tracks, or wants a project idea, roadmap, build plan, demo, pitch, compliance check, or submission package for a hackathon.
---

# Hackathon Project System

## Principle

Treat the hackathon brief as the source of truth. Build decisions must trace back to the overview, requirements, judging criteria, resources, submission rules, and competition constraints.

## Skill Tree

Use this order:

1. `hackathon-brief-analyzer` to normalize the supplied brief.
2. `hackathon-judging-strategy` to align the idea with the rubric.
3. `hackathon-resource-planner` to choose allowed tools and architecture.
4. `hackathon-build-roadmap` to create the timeboxed implementation plan.
5. `hackathon-compliance-review` to check rules and requirements.
6. `hackathon-demo-pitch` to shape the judging story.
7. `hackathon-submission-packager` to prepare the final deliverables.

Use `app-global-preferences` and the application-building skills when the hackathon project is an app. Use AI-specific skills only when the project is primarily AI or the brief requires AI.

## Required Inputs

Extract these sections when present:

- Overview
- Requirements
- What to Submit
- Judging Criteria
- Resources, tools, and technologies
- Rules
- Deadline, team size, tracks, prizes, and eligibility when present

If a section is missing, proceed with a clearly marked assumption only when the missing data does not affect eligibility, legality, required deliverables, or tool restrictions. Otherwise ask for the missing section.

## Output Workflow

1. Summarize the competition goal and constraints.
2. Identify mandatory requirements and disallowed choices.
3. Identify judging leverage points.
4. Propose one primary project direction and optional alternatives.
5. Define the minimum winning demo.
6. Define architecture and tool choices from allowed resources.
7. Create a build roadmap that proves core functionality first.
8. Define compliance checks and submission assets.
9. Define verification and validation gates before submission.

## Project Priority

Prioritize in this order:

1. Compliance with rules and submission requirements.
2. Strong fit to judging criteria.
3. Working end-to-end demo.
4. Clear story, measurable impact, and visible differentiation.
5. Stable enough implementation to survive judge interaction.
6. Polish only after the core demo works.

## Completion Check

Do not call a hackathon plan complete until every required brief section has either been incorporated, marked as missing, or explicitly ruled irrelevant.
