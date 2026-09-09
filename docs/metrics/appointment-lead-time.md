---
title: Appointment Lead Time
description: How much time elapses between a defined starting point and the scheduled
  date of care?
tags:
- Metric/Appointment Lead Time
kb:
  id: metric.appointment-lead-time
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
    - concept.referral
    assets:
    - asset.curated-appointment
    - asset.fn-business-days
    guides:
    - guide.dates
    - guide.rates-denominators
---

# Appointment Lead Time

<p class="kb-question">How much time elapses between a defined starting point and the scheduled date of care?</p>

## Definition

**Formula:** `Scheduled appointment date/time − defined start date/time`

| Component | Definition |
| --- | --- |
| **Eligible population** | Appointments within the service population being evaluated. |
| **Numerator** | Not applicable; this is a duration measure. |
| **Denominator** | Not applicable. Summaries should specify median, percentile, mean, or another distributional statistic. |
| **Time basis** | The start event must be named: appointment creation, referral creation, requested date, order date, or another approved event. |

## Recommended dimensions

- specialty
- department
- visit type
- new vs. return
- provider where appropriate

## Interpretation risks

- Calling several different wait-time definitions the same metric.
- Reporting only a mean when the distribution is highly skewed.
- Mixing calendar days and business days.

--8<-- "includes/snippets/reconciliation-note.md"
