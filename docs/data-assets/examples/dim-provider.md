---
title: Provider Dimension
description: Standardized provider identity and descriptive attributes for consistent
  joins and reporting.
tags:
- Data Asset/Table
- Status/Example
kb:
  id: asset.dim-provider
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
    - domain.outpatient-care
    - domain.surgical-services
    concepts:
    - concept.provider
    guides:
    - guide.joins
    - guide.historical-changes
  object_name: analytics.dim_provider
  asset_type: table
---

# Provider Dimension

<span class="kb-object-name">analytics.dim_provider</span>

!!! warning "Example asset"
    The object name and implementation details on this page are intentionally illustrative. Replace them with the real production object before treating this page as authoritative.

## Purpose

Standardized provider identity and descriptive attributes for consistent joins and reporting.

## Grain

**One row per provider identity in the current-state version; use a history dimension if point-in-time attributes are required.**

--8<-- "includes/snippets/grain-warning.md"

## Keys

| Field | Meaning |
| --- | --- |
| `provider_id` | Stable provider identifier used for analytical joins. |

## Important fields

| Field | Meaning |
| --- | --- |
| `provider_name` | Display name. |
| `primary_specialty` | Standardized specialty when defined. |
| `active_flag` | Current active/inactive status. |
| `provider_type` | Provider classification or credential type. |

## Refresh

Example: daily.

## Known limitations

- A provider dimension does not determine which provider role is correct for a metric.
- Current-state specialty may not represent specialty at the time of a historical encounter.
- Provider records can require identity cleanup or source-specific mapping.

--8<-- "includes/snippets/phi-note.md"
