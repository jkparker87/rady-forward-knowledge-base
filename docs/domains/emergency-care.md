---
title: Emergency Care
description: ED arrivals, throughput, disposition, boarding, conversion to admission,
  and emergency-care flow.
tags:
- Domain/Emergency Care
kb:
  id: domain.emergency-care
  type: domain
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  owners:
    business: Emergency Services
    technical: Analytics Engineering
  source_systems:
  - Epic
  relationships:
    concepts:
    - concept.encounter
    - concept.patient
    - concept.department-location
    - concept.patient-class
    metrics:
    - metric.ed-boarding-time
    assets:
    - asset.curated-encounter
    guides:
    - guide.dates
    - guide.q2d-emergency-flow
    - guide.grain
---

# Emergency Care

ED arrivals, throughput, disposition, boarding, conversion to admission, and emergency-care flow.

## Common business questions

- How many patients are arriving to the ED and when?
- How long do patients spend moving through the ED?
- How often do ED visits result in hospital admission?
- Where is boarding contributing to throughput delay?

## Major events and states

| Event / state | Why it matters |
| --- | --- |
| **Arrival** | Patient arrival or registration into the emergency-care workflow. |
| **Clinical start** | First meaningful clinical assessment or treatment event, depending on the measure. |
| **Disposition decision** | Decision to discharge, admit, transfer, or otherwise disposition the patient. |
| **Departure / unit arrival** | The patient physically leaves the ED or reaches the inpatient destination. |

## Interpretation risks

- Using disposition decision time and physical departure time interchangeably.
- Mixing ED encounters with subsequent inpatient encounters without a defined linkage rule.
- Calculating boarding time from different organizational definitions.
- Comparing volumes without accounting for visit grain and encounter status.

## How to use this domain

Start with the business question, then use the automatically linked concepts and metrics below to clarify definitions before selecting a curated data asset.

--8<-- "includes/snippets/source-of-truth-note.md"
