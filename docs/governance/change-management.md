---
title: Change Management
description: How definition and implementation changes should be documented and propagated.
tags:
- Governance/Change
kb:
  id: governance.change-management
  type: governance
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---

# Change management

A change is material when it could change a number, interpretation, population, historical trend, or downstream expectation.

Examples:

- inclusion / exclusion logic changes
- a status mapping changes
- a source field is replaced
- a curated table changes grain
- a date definition changes
- a department hierarchy is remapped

## Minimum change record

Document:

1. what changed
2. why it changed
3. effective date
4. whether history was restated
5. affected concepts, metrics, and assets
6. validation performed
7. who approved the business-definition change

Stable `kb.id` values allow renamed or moved pages to keep the same conceptual identity.
