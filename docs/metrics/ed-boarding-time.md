---
title: ED Boarding Time
description: How long does an admitted ED patient remain in the ED after the defined
  disposition/admission decision before leaving for the inpatient destination?
tags:
- Metric/ED Boarding Time
kb:
  id: metric.ed-boarding-time
  type: metric
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  owners:
    business_definition: Domain steward
    technical_implementation: Analytics Engineering
  relationships:
    domains:
    - domain.emergency-care
    concepts:
    - concept.encounter
    - concept.department-location
    assets:
    - asset.curated-encounter
    guides:
    - guide.dates
    - guide.q2d-emergency-flow
---

# ED Boarding Time

<p class="kb-question">How long does an admitted ED patient remain in the ED after the defined disposition/admission decision before leaving for the inpatient destination?</p>

## Definition

**Formula:** `Defined ED departure or inpatient-arrival timestamp − defined admission/disposition-decision timestamp`

| Component | Definition |
| --- | --- |
| **Eligible population** | ED visits that meet the approved admitted-patient definition. |
| **Numerator** | Not applicable; this is a duration measure. |
| **Denominator** | Not applicable. Summaries should specify the statistic used. |
| **Time basis** | The start and stop timestamps are definition-critical and must be consistent. |

## Recommended dimensions

- ED location
- destination unit
- service
- arrival period

## Interpretation risks

- Starting the clock at an inconsistent decision timestamp.
- Stopping the clock at order placement rather than physical movement.
- Including visits that never transitioned to an inpatient destination.

--8<-- "includes/snippets/reconciliation-note.md"
