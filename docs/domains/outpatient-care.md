---
title: Outpatient Care
description: Ambulatory visits, completed encounters, clinic activity, provider attribution,
  and outpatient utilization.
tags:
- Domain/Outpatient Care
kb:
  id: domain.outpatient-care
  type: domain
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  owners:
    business: Ambulatory Operations
    technical: Analytics Engineering
  source_systems:
  - Epic
  relationships:
    concepts:
    - concept.appointment
    - concept.encounter
    - concept.provider
    - concept.department-location
    metrics:
    - metric.no-show-rate
    - metric.appointment-lead-time
    assets:
    - asset.curated-appointment
    - asset.curated-encounter
    - asset.dim-provider
    guides:
    - guide.grain
    - guide.dates
    - guide.joins
---

# Outpatient Care

Ambulatory visits, completed encounters, clinic activity, provider attribution, and outpatient utilization.

## Common business questions

- How much outpatient care is being delivered?
- Which providers, clinics, or specialties are seeing which patient populations?
- How do scheduled visits translate into completed encounters?
- Where do access and utilization patterns differ?

## Major events and states

| Event / state | Why it matters |
| --- | --- |
| **Scheduled appointment** | The intended ambulatory service. |
| **Arrival** | Patient arrival/check-in for the scheduled or walk-in service. |
| **Completed encounter** | The clinical encounter is completed according to the source workflow. |
| **Provider attribution** | The provider relationship used for reporting, which may differ by question. |

## Interpretation risks

- Assuming every appointment produces exactly one encounter.
- Using scheduling provider when the question requires rendering or billing provider.
- Mixing location, department, specialty, and service-line concepts.
- Using encounter dates when the operational question is about scheduled capacity.

## How to use this domain

Start with the business question, then use the automatically linked concepts and metrics below to clarify definitions before selecting a curated data asset.

--8<-- "includes/snippets/source-of-truth-note.md"
