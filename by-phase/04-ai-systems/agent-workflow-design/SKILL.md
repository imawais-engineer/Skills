---
name: agent-workflow-design
description: Design reliable AI agent workflows with goals, state, tools, permissions, memory, handoffs, human approval, retries, timeouts, logging, evaluation, and security boundaries. Use when building agents, multi-step AI automation, tool-using assistants, background AI workers, autonomous workflows, or human-in-the-loop agent systems.
---

# Agent Workflow Design

## Principle

Use an agent only when a deterministic workflow is not enough. Design the agent as a controlled state machine with explicit tools, permissions, stop conditions, and human approval points.

## Agent Design Workflow

1. Define the objective and success criteria.
2. Decide whether an agent is justified or whether a normal service/job is safer.
3. Define the workflow states, transitions, and stop conditions.
4. Define tools and the exact actions each tool may perform.
5. Define required user approvals before external side effects.
6. Define memory and persistence: what is stored, for how long, and why.
7. Define retries, timeouts, cancellation, fallback, and escalation.
8. Define logs, audit trail, cost tracking, and observability.
9. Define evals for successful, failed, unsafe, and ambiguous runs.

## Tool And Permission Rules

- Give each tool the smallest useful permission.
- Make external side effects explicit: sending messages, changing records, charging money, deploying, deleting, publishing, or contacting users.
- Require approval for high-impact or irreversible actions.
- Make tool calls idempotent when practical.
- Validate tool inputs and outputs.
- Store enough run state to resume or explain the workflow.

## Human-In-The-Loop

Add review gates for:

- Destructive operations
- Financial actions
- Security-sensitive changes
- Customer-facing messages
- Legal/compliance outputs
- Bulk updates
- Low-confidence decisions

## Implementation Order

1. Build the non-agent app workflow first when possible.
2. Add the simplest agent loop that completes the core task.
3. Add tool boundaries and approvals.
4. Add persistence, run history, and visibility.
5. Add auth, rate limits, audit logs, and abuse controls before stable release.
6. Add evals and replayable test cases.

## Done Check

Agent workflow work is done when the agent has a bounded goal, controlled tools, visible state, tested failure behavior, approval gates, auditability, and verification plus validation.
