---
title: Content Model
tags:
  - governance
  - documentation
---

# Content Model

A page belongs in Rady Forward when it provides **reusable human knowledge** that is valuable beyond one file, one analyst, or one implementation.

## Good candidates

- enterprise or team standards
- development and validation workflows
- request and intake processes
- data product design guidance
- user personas and user-story methods
- system overviews and high-level data flows
- governance structures and decision rights
- AI usage guidance
- data and AI literacy content
- service models and support expectations
- reusable runbooks

## Usually better elsewhere

| Content | Better home |
|---|---|
| Table and column catalog | Alation |
| Raw pipeline implementation | GitHub / Databricks |
| SQL source code | GitHub |
| Notebook source | GitHub / Databricks |
| Dashboard-specific configuration | BI platform |
| Secrets / connection credentials | Approved secrets management |
| Temporary project notes | Project issue / project workspace |
| One-off analytical output | Project artifact location |

## Page maturity

Use a simple status model in front matter:

```yaml
status: draft | active | deprecated
owner: team-or-role
audience:
  - data-practitioner
review_cycle: annual
```

The site can later automate checks for stale pages, missing owners, broken links, and required metadata.
