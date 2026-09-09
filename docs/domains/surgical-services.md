---
title: Surgical Services
description: Cases, procedures, operating-room activity, surgical scheduling, and
  perioperative utilization.
tags:
- Domain/Surgical Services
kb:
  id: domain.surgical-services
  type: domain
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  owners:
    business: Perioperative Services
    technical: Analytics Engineering
  source_systems:
  - Epic
  relationships:
    concepts:
    - concept.encounter
    - concept.provider
    - concept.department-location
    - concept.patient
    assets:
    - asset.curated-encounter
    - asset.dim-provider
    guides:
    - guide.grain
    - guide.dates
    - guide.joins
---

# Surgical Services

Cases, procedures, operating-room activity, surgical scheduling, and perioperative utilization.

## Common business questions

- How many surgical cases are scheduled and completed?
- How is operating-room capacity being used?
- How should procedures, cases, encounters, and appointments be linked?
- How does surgical activity vary by service, location, or provider?

## Major events and states

| Event / state | Why it matters |
| --- | --- |
| **Case request** | A request to perform a surgical procedure or case. |
| **Case scheduling** | Placement of the case into a scheduled date, room, or block. |
| **Procedure start / stop** | Operational timestamps used for utilization and throughput. |
| **Encounter linkage** | Association of surgical activity with the patient's clinical encounter. |

## Interpretation risks

- Counting procedures when the metric is defined at case grain.
- Treating case request date, scheduled date, and procedure date as interchangeable.
- Joining case-level and procedure-level data without controlling duplication.
- Using provider role without defining surgeon, proceduralist, anesthesiologist, or other attribution.

## How to use this domain

Start with the business question, then use the automatically linked concepts and metrics below to clarify definitions before selecting a curated data asset.

--8<-- "includes/snippets/source-of-truth-note.md"
