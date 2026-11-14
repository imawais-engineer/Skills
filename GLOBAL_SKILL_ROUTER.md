# Hackathon skill router

Use this file when the work is a hackathon or competition build. [TREE.md](TREE.md) is the compiled order. The library is [skills/](skills).

The professional product library on `main` is a different tree. This branch adds the eight hackathon skills and retimes the SDLC skills to the competition stages.

Read `hackathon-project-system` first. Then follow the stage you are actually in. Do not start at the build skills while the brief is still unstructured.

## Priority

| Priority | Skill | Phase | Why this slot |
| --- | --- | --- | --- |
| 1 | `hackathon-project-system` | intake | Orchestrator. The brief is the source of truth, and this skill names the rest of the hackathon order. |
| 2 | `hackathon-brief-analyzer` | intake | Do not design first. Extract requirements, deliverables, rubric, resources, and rules. |
| 3 | `sdlc-best-practices` | intake | Turn those facts into an SRS with requirement IDs. No code until that specification is approved. |
| 4 | `hackathon-judging-strategy` | decision | Choose the idea that can become a complete demo and score on the rubric. |
| 5 | `hackathon-compliance-review` | decision | Hard stops before a stack or a feature is locked: eligibility, banned tools, licenses, required deliverables. |
| 6 | `project-foundations-and-architecture` | decision | Lock platform, access, and privacy inside the rules. Confirm before any file. |
| 7 | `hackathon-resource-planner` | decision | Map required and allowed tools. Use the default stack only where the brief is silent. |
| 8 | `app-global-preferences` | decision | Fill leftover silence. Never override the brief, the rules, the SRS, or the foundations record. |
| 9 | `complete-app-blueprint` | plan | Map the pages, data, and APIs of the minimum winning demo. |
| 10 | `hackathon-build-roadmap` | plan | Timebox that blueprint. A working demo beats an unfinished larger system. |
| 11 | `dashboard-first-ui` | build | Specify the screens the demo must show before they are coded. |
| 12 | `functional-prototype-first` | build | First code. Prove the core workflow. Mock data is allowed. Auth waits unless it is the demo. |
| 13 | `data-persistence-design` | build | Replace mock data and add the integrations the brief or the demo requires. |
| 14 | `ai-app-builder` | build | Only when AI is required or is the product. |
| 15 | `prompt-engineering-system` | build | Prompts for that AI job. Skip when there is no AI job. |
| 16 | `agent-workflow-design` | build | Only when a fixed workflow is not enough. |
| 17 | `encapsulation-backend-config` | harden | The public demo must not show keys, env names, or provider internals. |
| 18 | `security-first-review` | harden | After the demo path works, before judges use it. |
| 19 | `stable-release-hardening` | harden | Tests and auth only to the depth the demo and the brief require. Uses the security findings. |
| 20 | `hackathon-demo-pitch` | submit | Show the problem, the working path, the required tools, and the rubric evidence. |
| 21 | `deploy-and-document` | submit | Live URL, repo, and setup the submission will point at. |
| 22 | `hackathon-submission-packager` | submit | Package only what the competition asks for, after the links work. |

Canonical start: `skills/intake/hackathon-project-system/SKILL.md`.

## How the two libraries were compiled

- The hackathon project system already says to run the seven child skills in order, then use the application skills when the entry is an app, and the AI skills only when AI is the product or the brief requires it.
- The brief analyzer forbids designing before the facts are extracted. It therefore comes before the SRS, the idea, and the stack.
- The SRS gate still blocks code. The brief is the input, not a substitute for requirement IDs. The build roadmap ties every task to a requirement, a rubric line, a resource, or a submission item, which is only possible after `sdlc-best-practices`.
- Judging strategy chooses the idea. Compliance runs before that idea is allowed to pick a banned tool or miss a required deliverable.
- Foundations lock platform and privacy. The resource planner then maps sponsor and required tools, and may use the default stack only when the brief is silent. Preferences are last in the decision stage because they lose to the brief, the rules, and the foundations record.
- The blueprint maps the minimum winning demo. The roadmap timeboxes it. Screens are specified before the prototype is coded. The prototype is the first code. Persistence replaces mock data after that path works.
- AI skills stay behind persistence and stay conditional. An agent is last, and only when a fixed workflow cannot do the job.
- Encapsulation, the security review, and release hardening stay in that order because the review applies the encapsulation skill and the release skill requires the findings. For a hackathon, hardening covers the demo path and any sensitive or public action. It does not grow an admin product the brief did not ask for.
- The pitch is prepared after the path is stable. Deploy makes the URL and the setup real. The packager is last.
- Compliance is one skill and four gates: before the project is chosen, before the first code, before the demo is recorded, and before packaging.

## Fast routing

| Request | Start with | Then |
| --- | --- | --- |
| Here is a hackathon brief | `hackathon-project-system` | `hackathon-brief-analyzer`, then `sdlc-best-practices` |
| What must we submit and what is banned? | `hackathon-brief-analyzer` | `hackathon-compliance-review` |
| Which idea should we build? | `hackathon-judging-strategy` | `hackathon-compliance-review` before locking it |
| Which tools and sponsor APIs? | `hackathon-resource-planner` | `project-foundations-and-architecture` if platform or access is still open |
| The brief does not name a stack | `app-global-preferences` | Only after the resource plan says the brief is silent |
| Turn the winning demo into screens and data | `complete-app-blueprint` | `hackathon-build-roadmap` |
| What do we code first? | `hackathon-build-roadmap` | `functional-prototype-first` |
| Build the demo UI | `dashboard-first-ui` | `functional-prototype-first` |
| The core flow works and still uses mock data | `data-persistence-design` | `encapsulation-backend-config` before a public URL |
| The hackathon project is an AI app | `ai-app-builder` | `prompt-engineering-system`, then `agent-workflow-design` only if needed |
| Judges will open a public demo | `encapsulation-backend-config` | `security-first-review` |
| Make the demo path safe enough to click | `security-first-review` | `stable-release-hardening` |
| Write the pitch or record the demo | `hackathon-compliance-review` | `hackathon-demo-pitch` |
| Ship the live URL and README | `deploy-and-document` | `hackathon-submission-packager` |
| Final submission | `hackathon-compliance-review` | `hackathon-submission-packager` |

## Install

```bash
mkdir -p "${HOME}/.codex/skills"
ln -sfn "$(pwd)/skills/intake/hackathon-project-system" "${HOME}/.codex/skills/hackathon-project-system"
```

The copy inside the repo is `skills/intake/hackathon-project-system/SKILL.md`.

Install every skill on this branch:

```bash
mkdir -p "${HOME}/.codex/skills"
find skills -mindepth 2 -maxdepth 2 -type d | while read -r dir; do
  ln -sfn "$(realpath "$dir")" "${HOME}/.codex/skills/$(basename "$dir")"
done
```

## Maintenance

1. Keep one folder per skill under `skills/`.
2. Put it in the stage where a hackathon build reads it first.
3. Add it once to the priority table in [TREE.md](TREE.md) and in this file.
4. Keep `name` equal to the folder name.
5. Run `scripts/validate_skills.py`.
