---
title: Contributing
description: A practical workflow for adding and reviewing knowledge-base content.
tags:
- Type/Authoring
kb:
  id: reference.contributing
  type: reference
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---


# Contributing

## Before adding a page

Search first. If the concept already exists, update or reference it rather than creating a second definition.

## Content review

A substantive page should be reviewed from both perspectives:

=== "Business review"

    - Is the plain-language definition correct?
    - Does the workflow description reflect reality?
    - Are inclusions and exclusions understandable?
    - Are the cautions meaningful to data consumers?

=== "Technical review"

    - Is the stated grain correct?
    - Are keys and join paths accurate?
    - Are source systems and refresh expectations correct?
    - Do relationship IDs resolve?
    - Are caveats consistent with the implementation?

## Build validation

Run:

```bash
mkdocs build
```

The repository uses `strict: true`. Warnings such as duplicate IDs, unresolved relationship targets, or invalid lifecycle values should fail the build rather than silently ship broken documentation.

## Writing style

Prefer:

> One row per appointment.

over:

> This table contains appointment records.

Prefer:

> Use scheduled appointment date when grouping no-shows by service period.

over:

> Use `APPT_DTTM`.

Lead with meaning; follow with implementation.
