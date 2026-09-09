---
title: Census Day
description: A daily representation of patient occupancy or presence used to measure
  inpatient utilization over time.
tags:
- Concept/Census Day
kb:
  id: concept.census-day
  type: concept
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  source_systems:
  - Epic
  aliases:
  - patient day
  - daily census record
  relationships:
    domains:
    - domain.inpatient-care
    metrics:
    - metric.census
    assets:
    - asset.daily-census
    guides:
    - guide.snapshots-events
    - guide.grain
---

# Census Day

## Plain-language definition

A daily representation of patient occupancy or presence used to measure inpatient utilization over time.

## What the operational system is doing

Census may be captured at a specific daily time, averaged across observations, or derived from admission/discharge intervals. These approaches answer related but different questions.

## Analytical interpretation

Define whether the analysis uses midnight census, average daily census, patient-days, or another occupancy convention. Do not use the word 'census' without naming the convention.

## Typical grain

Often one row per date and department/unit, or one row per patient-date before aggregation.

--8<-- "includes/snippets/grain-warning.md"

## Common pitfalls

- Comparing midnight census with average daily census.
- Counting encounter rows instead of patient-days.
- Assigning a patient to more than one unit at the same snapshot without a defined rule.
