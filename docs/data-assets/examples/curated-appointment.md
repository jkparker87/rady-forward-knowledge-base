---
title: Curated Appointment
description: Recommended starting point for appointment-level scheduling and access
  analysis.
tags:
- Data Asset/Table
- Status/Example
kb:
  id: asset.curated-appointment
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
    concepts:
    - concept.appointment
    - concept.patient
    - concept.provider
    - concept.department-location
    metrics:
    - metric.no-show-rate
    - metric.appointment-lead-time
    guides:
    - guide.grain
    - guide.dates
    - guide.joins
  object_name: analytics.curated_appointment
  asset_type: table
---

# Curated Appointment

<span class="kb-object-name">analytics.curated_appointment</span>

!!! warning "Example asset"
    The object name and implementation details on this page are intentionally illustrative. Replace them with the real production object before treating this page as authoritative.

## Purpose

Recommended starting point for appointment-level scheduling and access analysis.

## Grain

**One row per analytical appointment.**

--8<-- "includes/snippets/grain-warning.md"

## Keys

| Field | Meaning |
| --- | --- |
| `appointment_id` | Primary appointment identifier. |
| `patient_id` | Enterprise patient identifier. |
| `department_id` | Scheduling department identifier. |
| `provider_id` | Primary scheduling-provider identifier when applicable. |

## Important fields

| Field | Meaning |
| --- | --- |
| `scheduled_datetime` | Date/time the appointment is scheduled to occur. |
| `created_datetime` | Date/time the scheduling record was created. |
| `appointment_status` | Standardized analytical appointment outcome/status. |
| `is_no_show` | Derived indicator implementing the approved no-show status logic. |
| `visit_type` | Standardized visit-type representation. |

## Refresh

Example: daily or intraday according to the production pipeline.

## Known limitations

- Historical rescheduling behavior must be understood if the source preserves multiple versions.
- Referral-based wait time requires an explicit referral linkage and start-date definition.
- Provider field represents a specific appointment role and should not be treated as every possible provider attribution.

--8<-- "includes/snippets/phi-note.md"
