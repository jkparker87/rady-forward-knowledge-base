---
title: Curated Encounter
description: Recommended encounter-level entry point for delivered-care and utilization
  analysis across major settings.
tags:
- Data Asset/Table
- Status/Example
kb:
  id: asset.curated-encounter
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
    - domain.emergency-care
    - domain.outpatient-care
    - domain.surgical-services
    concepts:
    - concept.encounter
    - concept.patient
    - concept.patient-class
    - concept.department-location
    metrics:
    - metric.length-of-stay
    - metric.ed-boarding-time
    guides:
    - guide.grain
    - guide.dates
    - guide.joins
  object_name: analytics.curated_encounter
  asset_type: table
---

# Curated Encounter

<span class="kb-object-name">analytics.curated_encounter</span>

!!! warning "Example asset"
    The object name and implementation details on this page are intentionally illustrative. Replace them with the real production object before treating this page as authoritative.

## Purpose

Recommended encounter-level entry point for delivered-care and utilization analysis across major settings.

## Grain

**One row per analytical encounter.**

--8<-- "includes/snippets/grain-warning.md"

## Keys

| Field | Meaning |
| --- | --- |
| `encounter_id` | Primary encounter identifier. |
| `patient_id` | Enterprise patient identifier. |
| `department_id` | Primary reporting department or location key, as defined by the model. |

## Important fields

| Field | Meaning |
| --- | --- |
| `encounter_type` | Standardized encounter classification. |
| `patient_class` | Analytical patient-class representation. |
| `arrival_datetime` | Defined arrival timestamp when applicable. |
| `admit_datetime` | Defined admission timestamp when applicable. |
| `discharge_datetime` | Defined discharge/departure timestamp when applicable. |

## Refresh

Example: daily or intraday according to the production pipeline.

## Known limitations

- Not every source-system encounter type should be combined in one analysis.
- Unit-level inpatient movement may require a finer-grain location-history asset.
- Appointment analyses should begin from appointment grain rather than forcing encounter data to represent scheduled demand.

--8<-- "includes/snippets/phi-note.md"
