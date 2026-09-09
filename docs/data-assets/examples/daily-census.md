---
title: Daily Census
description: Recommended daily snapshot / patient-day representation for inpatient
  occupancy analysis.
tags:
- Data Asset/Table
- Status/Example
kb:
  id: asset.daily-census
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
    - domain.inpatient-care
    concepts:
    - concept.census-day
    - concept.patient-class
    - concept.department-location
    metrics:
    - metric.census
    guides:
    - guide.snapshots-events
    - guide.grain
  object_name: analytics.daily_census
  asset_type: table
---

# Daily Census

<span class="kb-object-name">analytics.daily_census</span>

!!! warning "Example asset"
    The object name and implementation details on this page are intentionally illustrative. Replace them with the real production object before treating this page as authoritative.

## Purpose

Recommended daily snapshot / patient-day representation for inpatient occupancy analysis.

## Grain

**One row per date and organizational unit, or per patient-date if implemented at patient-day grain; replace this statement with the actual production grain.**

--8<-- "includes/snippets/grain-warning.md"

## Keys

| Field | Meaning |
| --- | --- |
| `census_date` | Date represented by the census observation. |
| `department_id` | Unit / department identifier. |

## Important fields

| Field | Meaning |
| --- | --- |
| `census_count` | Eligible census count under the approved snapshot convention. |
| `patient_class_group` | Optional standardized class grouping. |
| `capacity` | Optional staffed/available capacity when maintained in the same model. |

## Refresh

Example: daily after the prior census period closes.

## Known limitations

- The exact census observation convention must be documented before publication.
- Capacity may come from a different operational source and may have different effective dates.
- Do not derive admissions or discharges from a snapshot table unless the model explicitly supports that use.

--8<-- "includes/snippets/phi-note.md"
