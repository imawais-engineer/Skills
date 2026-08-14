---
name: prompt-engineering-system
description: Design prompts as maintainable application components with clear task contracts, input schemas, output schemas, examples, safety boundaries, eval cases, versioning, and validation. Use when creating or improving prompts, system instructions, AI workflows, structured outputs, extraction/generation/classification prompts, or prompt libraries.
---

# Prompt Engineering System

## Principle

Treat prompts as software artifacts, not disposable text. A production prompt needs a purpose, inputs, outputs, constraints, tests, failure handling, versioning, and ownership.

## Prompt Design Workflow

1. Define the task contract: what the prompt must accomplish and what it must not do.
2. Define input fields, source of each field, required/optional status, and validation rules.
3. Define output format, schema, allowed values, and rejection/error shape.
4. Separate stable instructions from user-provided data.
5. Add concise examples only when they improve reliability.
6. Add safety, privacy, and prompt-injection boundaries.
7. Add validation code or schema checks for outputs.
8. Add eval cases covering normal, edge, malicious, incomplete, and ambiguous inputs.
9. Version the prompt when behavior changes.

## Prompt Structure

Prefer this structure:

- Role and objective
- Context needed for the task
- Input contract
- Output contract
- Constraints and forbidden behavior
- Decision rules
- Examples, if useful
- Failure and escalation behavior

## Application Rules

- Keep prompts close to the feature that uses them, or in a prompt library when reused.
- Never mix untrusted user text into instructions without clear delimiters.
- Prefer structured outputs when the app needs to parse or store results.
- Validate AI output before database writes, external actions, or user-visible critical decisions.
- Log prompt version, model/provider, inputs summary, output status, and validation result when useful.

## Evaluation

Create small eval sets before stable release:

- Happy path examples
- Edge cases
- Missing data
- Ambiguous requests
- Prompt injection attempts
- Unsafe or disallowed content
- Regression cases from real failures

## Done Check

Prompt work is done when the prompt has a clear contract, produces parseable outputs where needed, passes eval cases, handles failure states, and is connected to the app workflow without placeholders.
