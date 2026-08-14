---
name: dashboard-first-ui
description: Dashboard-first UI design standards for AI-built applications. Use when designing or implementing app UI, layouts, pages, dashboards, sidebars, navigation, tables, forms, responsive behavior, dark themes, gradient aesthetics, or visual validation for apps built for Awais.
---

# Dashboard First UI

## Core Direction

Build the useful application screen first. Prefer dashboard-first product UI over landing-page-first marketing UI unless a landing page is explicitly required.

## Visual Style

- Use a modern dark background aesthetic with controlled gradients.
- Keep the theme consistent across all pages, panels, tables, forms, modals, and navigation.
- Use enough color contrast for readability and scanning.
- Avoid chaotic, experimental, controversial, or overly decorative layouts.
- Use gradients as atmosphere and hierarchy, not as a substitute for information design.

## Layout Standards

- Prefer conventional app structures: sidebar, top nav, content area, tables, cards/panels, filters, settings, and detail views.
- Implement all visible objects completely: layout, sidebar, nav bars, tables, forms, buttons, empty states, and data states.
- Keep fixed UI elements dimensionally stable so hover states, badges, counters, and labels do not shift layout.
- Ensure no elements overlap, cover each other, clip text, hide controls, or disappear at common desktop and mobile widths.
- Ensure text fits inside buttons, cards, table cells, sidebars, and mobile containers.

## Dashboard Completeness

Include the dashboard elements the app naturally needs:

- Navigation with current location
- Core action entry points
- Summary metrics or status panels when meaningful
- Primary table/list/detail view
- Search, filters, sort, and pagination when data can grow
- Empty, loading, error, success, and disabled states
- Settings/profile/admin entry points only when the app requires them

## Validation

Before considering UI done:

1. Verify every required page and section exists.
2. Validate that each interactive element works or intentionally asks for the missing dependency.
3. Check desktop and mobile layouts.
4. Check that no text or element overlaps, clips, or hides another element.
5. Check visual consistency across pages.
