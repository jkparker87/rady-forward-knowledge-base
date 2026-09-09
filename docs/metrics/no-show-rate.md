---
title: No-show Rate
description: Of the appointments that were expected to occur, what proportion were
  not attended and classified as no-shows?
tags:
- Metric/No-show Rate
kb:
  id: metric.no-show-rate
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
    - domain.scheduling-access
    - domain.outpatient-care
    concepts:
    - concept.appointment
    - concept.department-location
    - concept.provider
    assets:
    - asset.curated-appointment
    guides:
    - guide.rates-denominators
    - guide.dates
---

# No-show Rate

<p class="kb-question">Of the appointments that were expected to occur, what proportion were not attended and classified as no-shows?</p>

## Definition

**Formula:** `No-show appointments ÷ eligible scheduled appointments`

| Component | Definition |
| --- | --- |
| **Eligible population** | Appointments eligible for attendance-status evaluation during the reporting period. |
| **Numerator** | Eligible appointments whose final outcome is classified as no-show under the approved appointment-status logic. |
| **Denominator** | Eligible scheduled appointments, excluding statuses or service types that the organization has determined should not contribute to the rate. |
| **Time basis** | Usually scheduled appointment date, not appointment creation date. |

## Recommended dimensions

- department / clinic
- specialty
- provider role when appropriate
- visit type
- new vs. return status

## Interpretation risks

- Using all appointment records in the denominator, including canceled or administratively invalid records.
- Comparing teams that use materially different scheduling workflows without checking eligibility rules.
- Using appointment creation month instead of scheduled-service month.

--8<-- "includes/snippets/reconciliation-note.md"
