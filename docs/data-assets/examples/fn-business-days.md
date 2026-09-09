---
title: Business Days Function
description: Reusable calculation of business-day intervals using the organization's
  approved calendar logic.
tags:
- Data Asset/Function
- Status/Example
kb:
  id: asset.fn-business-days
  type: data_asset
  status: draft
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  owners:
    technical: Analytics Engineering
    business_definition: Relevant domain steward
  source_systems:
  - Epic
  - Enterprise analytics warehouse
  relationships:
    domains:
    - domain.scheduling-access
    metrics:
    - metric.appointment-lead-time
    guides:
    - guide.dates
  object_name: analytics.fn_business_days
  asset_type: function
---

# Business Days Function

<span class="kb-object-name">analytics.fn_business_days</span>

!!! warning "Example asset"
    The object name and implementation details on this page are intentionally illustrative. Replace them with the real production object before treating this page as authoritative.

## Purpose

Reusable calculation of business-day intervals using the organization's approved calendar logic.

## Grain

**Scalar calculation from supplied start and end dates.**

--8<-- "includes/snippets/grain-warning.md"

## Keys

| Field | Meaning |
| --- | --- |
| _None_ | This function does not expose relational keys. |

## Important fields

| Field | Meaning |
| --- | --- |
| `start_date` | Beginning date. |
| `end_date` | Ending date. |
| `return_value` | Number of business days according to the approved calendar. |

## Refresh

Not applicable; logic changes only when the function or underlying calendar changes.

## Known limitations

- Holiday calendars and partial business days must be explicitly defined.
- Calendar-day metrics should not use this function.
- Timezone conversion should occur before date truncation when timestamps cross local-day boundaries.

--8<-- "includes/snippets/phi-note.md"
