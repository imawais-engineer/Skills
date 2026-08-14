# Skills

A structured, reusable skill library for AI-assisted software development, product planning, design, AI systems, security, deployment, and hackathon workflows.

The repository is organized around a **phase-based skill architecture** with a complementary **use-case routing layer**. The goal is to make skills easy to discover, reuse, compose, and route to the right task at the right stage of a project.

---

## What This Repository Contains

This repository provides reusable `SKILL.md` definitions and supporting agent configuration for workflows such as:

* Application architecture and planning
* UI/UX and dashboard design
* Functional prototyping
* Data and persistence design
* AI application development
* Agent workflow design
* Prompt engineering
* Security reviews
* Backend configuration and encapsulation
* Release hardening
* Deployment and documentation
* Hackathon strategy
* Hackathon project planning
* Demo and pitch preparation
* Hackathon compliance
* Submission packaging

The repository is designed to support projects from **initial idea → planning → implementation → AI integration → hardening → deployment → presentation/submission**.

---

## Architecture

The repository uses two complementary organizational layers:

```text
                    ┌─────────────────────┐
                    │ GLOBAL SKILL ROUTER │
                    └──────────┬──────────┘
                               │
                 Select the appropriate skill
                               │
             ┌─────────────────┴─────────────────┐
             │                                   │
      Phase-based skills                   Use-case mappings
             │                                   │
      by-phase/                            by-use-case/
             │                                   │
      Canonical skills                  Discover by intent
```

### 1. `by-phase/`

This is the **canonical skill library**.

Skills are organized according to the stage of a project.

```text
by-phase/
├── 01-foundation/
├── 02-design-and-prototype/
├── 03-data-and-persistence/
├── 04-ai-systems/
├── 05-hardening-and-release/
├── 06-deployment-and-documentation/
├── 07-hackathon-intake-and-strategy/
└── 08-hackathon-build-and-submit/
```

The files under these directories contain the actual skill definitions.

### 2. `by-use-case/`

This is the **discovery and routing layer**.

Instead of asking:

> "Which project phase am I in?"

you can ask:

> "What am I trying to accomplish?"

For example:

```text
by-use-case/
├── ai-development/
├── application-development/
├── hackathons-and-competitions/
├── implementation-roadmaps/
├── planning-and-strategy/
├── security-and-release/
└── submission-and-pitch/
```

These entries map use cases to the appropriate canonical skills.

---

## Global Skill Router

`GLOBAL_SKILL_ROUTER.md` is the central routing guide.

It helps determine:

1. What the user is trying to accomplish
2. Which project phase applies
3. Which skill should be activated
4. Whether multiple skills need to be composed
5. Which skill should run first
6. What information should be preserved between phases

The router is intended to prevent unnecessary skill selection and help workflows follow a coherent progression.

---

## Project Lifecycle

The phase structure follows this general lifecycle:

```text
01 Foundation
      ↓
02 Design & Prototype
      ↓
03 Data & Persistence
      ↓
04 AI Systems
      ↓
05 Hardening & Release
      ↓
06 Deployment & Documentation
      ↓
07 Hackathon Intake & Strategy
      ↓
08 Hackathon Build & Submit
```

Not every project requires every phase.

For example, an existing application may begin at:

```text
02 Design & Prototype
```

while a security review may start directly at:

```text
05 Hardening & Release
```

Hackathon-specific work can use phases `07` and `08` independently or alongside the normal application-development lifecycle.

---

## Skill Structure

A typical skill follows this structure:

```text
skill-name/
├── SKILL.md
└── agents/
    └── openai.yaml
```

### `SKILL.md`

Contains the skill's operational instructions, scope, workflow, constraints, and expected behavior.

### `agents/openai.yaml`

Contains agent-specific metadata/configuration used to describe how the skill should be exposed or invoked.

---

## Skill Categories

### Foundation

Establishes project-wide preferences and complete application blueprints.

Examples:

* `app-global-preferences`
* `complete-app-blueprint`

### Design & Prototype

Focuses on product interfaces and early functional implementation.

Examples:

* `dashboard-first-ui`
* `functional-prototype-first`

### Data & Persistence

Covers application data architecture and persistence decisions.

Example:

* `data-persistence-design`

### AI Systems

Focuses on AI-native application architecture.

Examples:

* `ai-app-builder`
* `agent-workflow-design`
* `prompt-engineering-system`

### Hardening & Release

Improves application security, configuration boundaries, and release stability.

Examples:

* `security-first-review`
* `encapsulation-backend-config`
* `stable-release-hardening`

### Deployment & Documentation

Covers deployment readiness and project documentation.

Example:

* `deploy-and-document`

### Hackathon Intake & Strategy

Helps analyze hackathon opportunities and strategically shape projects.

Examples:

* `hackathon-brief-analyzer`
* `hackathon-judging-strategy`
* `hackathon-project-system`
* `hackathon-resource-planner`

### Hackathon Build & Submit

Covers execution and final submission.

Examples:

* `hackathon-build-roadmap`
* `hackathon-compliance-review`
* `hackathon-demo-pitch`
* `hackathon-submission-packager`

---

## Recommended Workflow

For a new application, a typical workflow is:

```text
1. Define project preferences
        ↓
2. Create application blueprint
        ↓
3. Design the primary interface
        ↓
4. Build a functional prototype
        ↓
5. Design persistence/data layer
        ↓
6. Add AI capabilities
        ↓
7. Review security
        ↓
8. Harden configuration and release
        ↓
9. Deploy and document
```

For a hackathon project:

```text
1. Analyze the hackathon
        ↓
2. Understand judging criteria
        ↓
3. Define project strategy
        ↓
4. Build implementation roadmap
        ↓
5. Implement the project
        ↓
6. Verify compliance
        ↓
7. Prepare demo/pitch
        ↓
8. Package submission
```

---

## Using the Repository

Clone the repository:

```bash
git clone https://github.com/imawais-engineer/Skills.git
cd Skills
```

Inspect the available skills:

```bash
find by-phase -name SKILL.md
```

Inspect skills by use case:

```bash
find by-use-case -type l
```

Read the global router:

```bash
cat GLOBAL_SKILL_ROUTER.md
```

Read an individual skill:

```bash
cat by-phase/04-ai-systems/ai-app-builder/SKILL.md
```

---

## Canonical vs. Use-Case Paths

The `by-phase/` directory is the source of truth for skill definitions.

The `by-use-case/` directory provides alternate discovery paths to those skills.

Conceptually:

```text
Canonical Skill
      │
      ├── Phase classification
      │
      └── Multiple use-case mappings
```

This allows a single skill to be discoverable from multiple perspectives without maintaining duplicate implementations.

---

## Design Principles

The skill library follows several principles.

### Reusability

Skills should solve recurring classes of problems rather than one-off project tasks.

### Composability

Skills should work independently while also being capable of forming larger workflows.

### Clear Scope

Each skill should have a defined purpose and avoid duplicating unrelated responsibilities.

### Phase Awareness

The recommended skill depends on the current project stage.

### Use-Case Discovery

Users should be able to find a skill based on what they want to accomplish rather than knowing the internal phase taxonomy.

### Security First

Security, secrets management, backend boundaries, and release validation should be considered before production deployment.

### Verification

Implementation-oriented workflows should include appropriate validation and verification steps.

---

## Repository Structure

```text
Skills/
│
├── GLOBAL_SKILL_ROUTER.md
├── README.md
│
├── by-phase/
│   │
│   ├── 01-foundation/
│   ├── 02-design-and-prototype/
│   ├── 03-data-and-persistence/
│   ├── 04-ai-systems/
│   ├── 05-hardening-and-release/
│   ├── 06-deployment-and-documentation/
│   ├── 07-hackathon-intake-and-strategy/
│   └── 08-hackathon-build-and-submit/
│
└── by-use-case/
    │
    ├── ai-development/
    ├── application-development/
    ├── hackathons-and-competitions/
    ├── implementation-roadmaps/
    ├── planning-and-strategy/
    ├── security-and-release/
    └── submission-and-pitch/
```

---

## Adding a New Skill

When adding a new skill:

1. Determine the skill's primary responsibility.
2. Place the canonical implementation under the appropriate `by-phase/` directory.
3. Add `SKILL.md`.
4. Add `agents/openai.yaml` when agent metadata is required.
5. Add appropriate use-case mappings under `by-use-case/`.
6. Update `GLOBAL_SKILL_ROUTER.md` when the new skill changes routing decisions.
7. Verify that the skill does not duplicate an existing capability.

A skill should have **one canonical implementation** and can be exposed through multiple discovery paths.

---

## Quality Guidelines

A high-quality skill should:

* Have a clearly defined trigger
* State its scope and limitations
* Provide deterministic workflow guidance
* Define important inputs and outputs
* Avoid unnecessary overlap with other skills
* Include verification where appropriate
* Handle failure conditions explicitly
* Protect secrets and sensitive information
* Prefer existing project context over repeated questions
* Remain reusable across multiple projects

---

## Security

Do not commit:

* API keys
* Access tokens
* Passwords
* Private certificates
* `.env` files containing secrets
* Personal credentials
* Private customer information

Before committing changes, review:

```bash
git status
git diff --cached
```

---

## Git Workflow

Typical update workflow:

```bash
git add .
git commit -m "Describe the change"
git push
```

Check repository state:

```bash
git status
```

The expected clean state is:

```text
nothing to commit, working tree clean
```

---

## Intended Use

This repository is intended as a reusable **AI development skill system**, not merely a collection of documentation files.

The architecture is designed to support:

* AI coding agents
* Agentic development workflows
* Application planning
* Software implementation
* AI product development
* Security reviews
* Release workflows
* Hackathon execution
* Technical documentation
* Repeatable engineering processes

---

## License

Add the project's chosen license here before distributing the repository publicly.

---

## Repository

**GitHub:** `imawais-engineer/Skills`

The repository is continuously evolving as new workflows, skills, routing rules, and engineering patterns are added.
