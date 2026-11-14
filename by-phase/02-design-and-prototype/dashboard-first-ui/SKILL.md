---
name: dashboard-first-ui
description: Published skill from SDLC Skills Hub (SRS Architect themed). Extracted and structured for agent use.
source: https://sdlc.base44.app/skill/dashboard-first-ui
priority: foundation-first
---

V1.0.0
Dashboard First UI

Dashboard-first UI design standards for AI-built applications. Use when designing or implementing app UI, layouts, pages, dashboards, sidebars, navigation, tables, forms, responsive behavior, dark themes, gradient aesthetics, or visual validation for apps built for Awais.

Dashboard First UI

Skill SK-05 · Phase 2 — Design & Prototype (UI design) · Applies to: web apps, Android apps, AI apps Build the useful application screen first, completely, in every state — so the UI is right on the first pass instead of the tenth.

1. Purpose

UI is where AI edit loops are most visible: "move this", "it overlaps", "the button does nothing", "make it look better". Each of those is a missing UI requirement. This skill turns UI into a specification: a dashboard-first structure, a fixed visual baseline, every element implemented, every state designed, and an objective validation pass.

2. When to use — and when not to

Use it when designing or implementing app UI, layouts, pages, navigation, tables, forms, dashboards, or Android screens.

Do not use it for marketing landing pages when the product explicitly requires one — follow the selected Interface Library direction there.

3. Inputs required
Input	Source	Required
Pages table with FR IDs and states	SK-03	Yes
Roles and what each sees	SRS §3	Yes
Interface direction or "none selected"	SK-02 / Interface Library	Yes
Platform targets and breakpoints	SK-02	Yes
4. Procedure
Step	SDLC phase	Action	Output
1	Design	Fix the visual baseline: theme, colour tokens, type scale, spacing scale, radius, component set.	Design tokens
2	Design	Define the app shell: navigation with current location (web: sidebar + top bar; Android: bottom nav or drawer + top app bar).	Shell
3	Design	For each page in the blueprint, lay out: primary action, primary table/list/detail, summary panels where meaningful, filters/search/sort/pagination when data can grow.	Page layouts
4	Design	Design every state per page: loading, empty, error, success, disabled, validation (Android: offline, permission denied).	State designs
5	Implementation	Implement every visible object completely: layout, nav, tables, forms, buttons, empty and data states.	Working UI
6	Verification	Run the validation pass (section 7) at desktop (1440 px), tablet (768 px) and mobile (375 px / small Android device).	Validation record
Visual baseline (default when no direction is selected)
Modern dark background with controlled gradients, used for atmosphere and hierarchy — never as a substitute for information design.
One theme across pages, panels, tables, forms, modals and navigation.
Contrast ≥ WCAG AA (4.5:1 body text, 3:1 large text and UI controls).
No chaotic, experimental or overly decorative layouts.
Layout standards
Conventional structures: sidebar, top nav, content area, tables, cards/panels, filters, settings, detail views.
Fixed UI elements are dimensionally stable: hover states, badges, counters and labels do not shift layout.
No element overlaps, covers, clips, hides or disappears at the three widths above.
Text fits inside buttons, cards, table cells, sidebars and mobile containers.
Touch targets ≥ 44 × 44 px (web) / 48 × 48 dp (Android).
5. Deliverables
Design tokens (colours, type, spacing) written once and reused.
App shell plus every page in the blueprint, each with all its states.
UI validation record: page × width × state grid, each cell Pass/Fail with a note.
6. Acceptance criteria (Given / When / Then)
Given any page, when it loads with no data, then a designed empty state with the primary action is shown.
Given any interactive control, when it is activated, then it performs a real state change or clearly states the missing dependency.
Given widths 375, 768 and 1440 px, when each page is rendered, then no text clips and no element overlaps another.
Given the navigation, when on any page, then the current location is highlighted.
7. Verification checklist
 Every page in the blueprint exists.
 Every page has loading / empty / error / success / disabled / validation states.
 Every interactive element works or names its missing dependency.
 Desktop, tablet and mobile checked; no overlap or clipping.
 Contrast meets WCAG AA; touch targets meet minimum size.
 Theme and spacing consistent across all pages.
 No fake dashboards, metrics or charts without real data behind them.
8. Failure modes and anti-loop guards
Failure mode	Guard
"Make it look better" loops	Replace adjectives with tokens and an Interface Library direction; edits must name a token, a page and a state.
Overlap/clipping found one screen at a time	Run the full page × width grid in one pass, then fix in one batch.
Dead buttons	Every control is wired or explicitly blocked by a named dependency.
Landing page built before the product	Dashboard-first rule.
Layout shift on hover/badges	Dimensionally stable fixed elements.

Edit rule: a UI change request must state page, element, state, expected result. If it cannot, it is a design question — answer it in the tokens or blueprint first.

9. Prompt template
ROLE: Senior product UI engineer. Build dashboard-first UI.
INPUT: Pages table (with FR IDs and required states): <paste>. Interface direction: <name + prompt, or "none: dark theme, controlled gradients">. Platforms: <web / Android>.
DO:
1. Define tokens (colours, type scale, spacing) once and reuse them.
2. Build the app shell with current-location navigation.
3. Build each page with its primary action and all states: loading, empty, error, success, disabled, validation (+ offline/permission for Android).
4. Wire every control to real behaviour, or display "Needs <dependency>".
5. Self-check at 375 / 768 / 1440 px: no overlap, no clipping, WCAG AA contrast. Report the result as a page × width table.
NEVER: placeholders for core features, fake metrics, decorative layouts, pages without an FR ID.

10. Traceability to the SRS

Each page cites FR IDs; each state is a test case (e.g. TC-12: FR-4 empty state on Orders). UI-wide rules become NFRs: NFR-UI-1 contrast AA, NFR-UI-2 no overlap at 375/768/1440 px.

11. Definition of done

Every blueprint page exists with all states, the validation record is 100 % Pass, and every UI TC in the traceability matrix is Verified and Validated.

Related skills

Previous: SK-03 Complete App Blueprint. In parallel: SK-06 Functional Prototype First. Defaults: SK-04 App Global Preferences.

Ready to hand this to your AI?

Copy the skill, drop it into your project, and require the AI to read it before the first prompt.

COPY SKILL
DOWNLOAD .MD