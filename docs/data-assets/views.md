---
title: Views
description: When views are appropriate as curated or supporting analytical interfaces.
tags:
- Data Asset/View
kb:
  id: reference.views
  type: reference
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---


# Views

Views are useful when consumers need a stable interface over logic that should remain centralized.

Use a documented view when it:

- standardizes a frequently reused filter or join
- exposes a business-friendly shape over technical tables
- preserves a stable contract while underlying implementation changes
- intentionally represents a reusable analytical population

Avoid creating views that merely hide `SELECT *` from another object or stack layers of indirection without adding meaning.
