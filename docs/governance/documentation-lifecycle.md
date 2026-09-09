---
title: Documentation Lifecycle
description: The lifecycle states and review expectations for knowledge-base content.
tags:
- Governance/Lifecycle
kb:
  id: governance.documentation-lifecycle
  type: governance
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---

# Documentation lifecycle

Use a small number of explicit states.

| Status | Meaning |
| --- | --- |
| `draft` | Content is being developed and should not be treated as authoritative. |
| `review` | Content is substantially complete and awaiting business / technical validation. |
| `approved` | Content is the current documented interpretation. |
| `deprecated` | Content is retained for traceability but should not be used for new work. |

Every substantive page should also have a review cadence and last-reviewed date in metadata.

The build hook validates status values and unresolved metadata relationships. With `strict: true`, build warnings fail CI, turning broken documentation relationships into visible maintenance work.
