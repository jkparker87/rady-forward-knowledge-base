---
title: Census
description: How many patients are occupying or assigned to inpatient capacity at
  a defined point or over a defined period?
tags:
- Metric/Census
kb:
  id: metric.census
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
    - domain.inpatient-care
    concepts:
    - concept.census-day
    - concept.encounter
    - concept.patient-class
    - concept.department-location
    assets:
    - asset.daily-census
    guides:
    - guide.snapshots-events
    - guide.grain
---

# Census

<p class="kb-question">How many patients are occupying or assigned to inpatient capacity at a defined point or over a defined period?</p>

## Definition

**Formula:** `Count of eligible patients at the census observation; average daily census is the average of daily census values over the period.`

| Component | Definition |
| --- | --- |
| **Eligible population** | Patients meeting the approved inpatient / observation and location rules at the observation time. |
| **Numerator** | Eligible occupied patient positions or patient records. |
| **Denominator** | Not applicable for census itself; capacity-utilization measures introduce a denominator. |
| **Time basis** | Must specify the observation convention: midnight, another fixed time, average across intervals, or patient-day derivation. |

## Recommended dimensions

- unit / department
- service
- patient class
- date

## Interpretation risks

- Using encounter admissions as a substitute for occupied census.
- Comparing census measures built from different snapshot conventions.
- Double-counting transfers at the observation boundary.

--8<-- "includes/snippets/reconciliation-note.md"
