---
title: Scheduling & Access
description: Appointments, referrals, schedule capacity, wait time, arrival outcomes,
  cancellations, and access to care.
tags:
- Domain/Scheduling & Access
kb:
  id: domain.scheduling-access
  type: domain
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  owners:
    business: Access / Scheduling Operations
    technical: Analytics Engineering
  source_systems:
  - Epic
  relationships:
    concepts:
    - concept.appointment
    - concept.referral
    - concept.provider
    - concept.department-location
    metrics:
    - metric.no-show-rate
    - metric.appointment-lead-time
    assets:
    - asset.curated-appointment
    - asset.dim-provider
    guides:
    - guide.dates
    - guide.rates-denominators
    - guide.q2d-clinic-access
---

# Scheduling & Access

Appointments, referrals, schedule capacity, wait time, arrival outcomes, cancellations, and access to care.

## Common business questions

- How long are patients waiting to obtain an appointment?
- Where is appointment demand exceeding available capacity?
- How often do scheduled appointments end in completion, cancellation, or no-show?
- How do referral and scheduling workflows affect access?

## Major events and states

| Event / state | Why it matters |
| --- | --- |
| **Appointment creation** | The scheduling record is created; useful for measuring scheduling activity but not necessarily patient wait time. |
| **Scheduled service** | The intended date and time of service. |
| **Arrival / check-in** | The patient reaches the care setting or completes the relevant arrival workflow. |
| **Cancellation / no-show** | The scheduled service does not occur as planned; definitions depend on status and timing. |
| **Referral initiation** | A request for specialty or other care begins and may precede appointment creation. |

## Interpretation risks

- Treating appointment creation date as the same thing as requested or scheduled date.
- Counting rescheduled records as separate demand without understanding the workflow.
- Comparing no-show rates when departments use different eligible populations.
- Mixing referral lead time with appointment lead time.

## How to use this domain

Start with the business question, then use the automatically linked concepts and metrics below to clarify definitions before selecting a curated data asset.

--8<-- "includes/snippets/source-of-truth-note.md"
