---
title: Inpatient Care
description: Admissions, transfers, discharges, patient class, daily census, length
  of stay, and inpatient utilization.
tags:
- Domain/Inpatient Care
kb:
  id: domain.inpatient-care
  type: domain
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  owners:
    business: Hospital Operations
    technical: Analytics Engineering
  source_systems:
  - Epic
  relationships:
    concepts:
    - concept.encounter
    - concept.patient
    - concept.patient-class
    - concept.department-location
    - concept.census-day
    metrics:
    - metric.census
    - metric.length-of-stay
    assets:
    - asset.curated-encounter
    - asset.daily-census
    guides:
    - guide.snapshots-events
    - guide.dates
    - guide.q2d-inpatient-utilization
---

# Inpatient Care

Admissions, transfers, discharges, patient class, daily census, length of stay, and inpatient utilization.

## Common business questions

- How many patients are occupying inpatient beds?
- How long are patients staying?
- How does utilization vary by unit, service, or patient population?
- Where are transfers or discharge patterns affecting capacity?

## Major events and states

| Event / state | Why it matters |
| --- | --- |
| **Admission** | The start of an inpatient stay or inpatient-classified episode, depending on the metric definition. |
| **Transfer** | Movement between units, departments, or levels of care during an encounter. |
| **Census snapshot** | A point-in-time or daily representation of occupied beds / patients. |
| **Discharge** | The end of the inpatient stay for analytical purposes. |

## Interpretation risks

- Using encounter counts when the question requires patient-days.
- Mixing midnight census, average daily census, and occupied-bed snapshots.
- Calculating length of stay with inconsistent start or end timestamps.
- Ignoring transfers when assigning utilization to a department.

## How to use this domain

Start with the business question, then use the automatically linked concepts and metrics below to clarify definitions before selecting a curated data asset.

--8<-- "includes/snippets/source-of-truth-note.md"
