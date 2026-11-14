# Changelog

## 2.0.0 — 2026-11-14

Public release of the professional skill library for software development with AI, by Forward Deployed AI Engineer Muhammad Awais. Licensed under MIT.

The library is `skills/`, with unnumbered phase folders and a priority order read from each skill.

### Added

- `TREE.md` records the 14-skill professional order and why each skill sits where it does.
- `scripts/validate_skills.py` checks frontmatter, folder names, duplicate names, that order, referenced paths, and relative links.
- `CHANGELOG.md`.

### Changed

- Fourteen product skills now live under `skills/foundational`, `skills/design-and-prototype`, `skills/data-and-persistence`, `skills/ai-systems`, `skills/hardening-and-release`, and `skills/deployment-and-documentation`. The moves were `git mv`.
- Eleven of those skills use the compiled SDLC Skills Hub text. Their YAML `description` is the generic hub line. The specific trigger sentence remains in the body. The three AI skills were already identical to the package and were only moved.
- Priority inside `foundational` is `sdlc-best-practices`, then `project-foundations-and-architecture`, then `app-global-preferences`, then `complete-app-blueprint`. Preferences cannot precede foundations: SK-04 requires the Foundations Record and the SRS.
- Priority inside `hardening-and-release` is `encapsulation-backend-config`, then `security-first-review`, then `stable-release-hardening`. The release skill requires the security findings, and the review applies the encapsulation skill.
- `GLOBAL_SKILL_ROUTER.md` and `README.md` follow this tree, this order, and the install path `skills/<phase>/<skill>`.

### Removed from this branch

Eight hackathon skills. They were not deleted from git. They remain on `cursor/hackathon-skills-beaf`:

- `hackathon-project-system`
- `hackathon-brief-analyzer`
- `hackathon-judging-strategy`
- `hackathon-resource-planner`
- `hackathon-build-roadmap`
- `hackathon-compliance-review`
- `hackathon-demo-pitch`
- `hackathon-submission-packager`

`by-use-case/` was removed earlier. It was a symlink index, not a second set of skills. Nothing was moved to `skills/unsorted/`.

### Unchanged skill text

- `ai-app-builder`, `prompt-engineering-system`, and `agent-workflow-design`, including `agents/openai.yaml`.
- Existing `agents/openai.yaml` files on skills whose compiled folder shipped `SKILL.md` only.
- `.github/workflows/security-scan.yml` and `SECURITY.md`.
