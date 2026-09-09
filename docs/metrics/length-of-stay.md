---
title: Length of Stay
description: How long does an eligible patient episode remain in the defined care
  setting?
tags:
- Metric/Length of Stay
kb:
  id: metric.length-of-stay
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
    - concept.encounter
    - concept.patient-class
    assets:
    - asset.curated-encounter
    guides:
    - guide.dates
    - guide.grain
---

# Length of Stay

<p class="kb-question">How long does an eligible patient episode remain in the defined care setting?</p>

## Definition

**Formula:** `Defined end timestamp − defined start timestamp`

| Component | Definition |
| --- | --- |
| **Eligible population** | Eligible encounters or episodes in the care setting being measured. |
| **Numerator** | Not applicable; this is a duration measure. |
| **Denominator** | Not applicable. State whether the summary is mean, median, geometric mean, percentile, or another statistic. |
| **Time basis** | Start and end events must be explicitly defined, such as admission-to-discharge or arrival-to-departure. |

## Recommended dimensions

- unit / service
- patient class
- discharge disposition
- clinical population

## Interpretation risks

- Mixing encounter duration with time on a specific unit.
- Ignoring patients still admitted when calculating completed-stay LOS.
- Comparing medians and means as though they were the same statistic.

--8<-- "includes/snippets/reconciliation-note.md"
