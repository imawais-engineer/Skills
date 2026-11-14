---
name: ai-app-builder
description: Build complete AI-first applications with product workflow, prompts, model/provider boundaries, data storage, evals, cost controls, safety checks, UI, testing, and deployment readiness. Use when the app is primarily AI-based, includes chat, assistants, agents, RAG, generation, classification, extraction, copilots, workflow automation, or AI-assisted decisions.
---

# AI App Builder

## Principle

Use AI intentionally only when it is central to the product. If AI is secondary, ask for approval before adding AI features. Keep the normal application complete: dashboard-first UI, real workflows, persistence, tests, auth after functionality, layered security, docs, and deployment.

## AI Application Blueprint

1. Define the core AI job: generation, extraction, classification, retrieval, recommendation, workflow automation, chat, agentic execution, or decision support.
2. Define the user workflow around the AI job, including inputs, review, editing, saving, exporting, and history.
3. Define required data: user content, prompts, model outputs, feedback, files, embeddings, tool results, cost/usage, and audit logs.
4. Define model/provider requirements without hard-coding current model assumptions. Verify provider docs before implementation.
5. Define safety boundaries: what the AI may do, what requires user approval, and what it must refuse or escalate.
6. Define validation: schema checks, output checks, user confirmation, evals, and fallback behavior.

## Build Order

1. Build the main app workflow and dashboard shell.
2. Build the AI happy path with controlled test data.
3. Store prompts, inputs, outputs, status, usage, and feedback when persistence is required.
4. Add prompt and output validation before saving important results.
5. Add retries, timeouts, streaming, cancellation, and error states where relevant.
6. Add auth, authorization, rate limits, usage quotas, and audit logs before stable release.
7. Add evaluation cases for quality, reliability, safety, and regression.
8. Document setup, environment variables, model/provider configuration, and operational limits.

## Required AI Components

Include these when relevant:

- Prompt templates or prompt builders
- Structured input and output schemas
- Model/provider adapter boundary
- Tool/function contracts
- RAG ingestion, retrieval, and citation path
- Conversation or job history
- Human review and approval flow
- Feedback capture
- Usage and cost tracking
- Safety and abuse controls
- Evaluation fixtures and expected behavior

## Ask Before Implementing

Ask before using external AI APIs, paid models, persistent user data, scraping, file ingestion, agentic actions, email/message sending, payments, or anything that changes external systems.

## Completion Check

AI app work is not done until:

- The core AI workflow works end to end.
- Outputs are validated before critical use.
- Failures are visible and recoverable.
- Required data is stored correctly.
- Cost, rate, and safety boundaries are defined.
- Verification and validation both pass.
