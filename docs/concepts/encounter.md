---
title: Encounter
description: A structured representation of a patient's interaction with the healthcare
  organization for a defined episode, setting, or billing/clinical workflow.
tags:
- Concept/Encounter
kb:
  id: concept.encounter
  type: concept
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  source_systems:
  - Epic
  aliases:
  - visit
  - clinical encounter
  relationships:
    domains:
    - domain.inpatient-care
    - domain.emergency-care
    - domain.outpatient-care
    - domain.surgical-services
    metrics:
    - metric.census
    - metric.length-of-stay
    - metric.ed-boarding-time
    assets:
    - asset.curated-encounter
    - asset.daily-census
    guides:
    - guide.grain
    - guide.joins
    - guide.dates
---

# Encounter

## Plain-language definition

A structured representation of a patient's interaction with the healthcare organization for a defined episode, setting, or billing/clinical workflow.

## What the operational system is doing

Operational systems can create multiple encounter-like records around one real-world episode. Encounter type and patient class determine how records should be interpreted.

## Analytical interpretation

Use encounter data when the question concerns delivered care, utilization, admission/discharge activity, or clinical episode characteristics. Confirm setting and encounter type before counting.

## Typical grain

Usually one row per encounter in a curated encounter table, with child events or movements stored at finer grains.

--8<-- "includes/snippets/grain-warning.md"

## Common pitfalls

- Treating all encounter types as comparable.
- Counting transfers or child records as new visits.
- Assuming appointment and encounter IDs represent the same business event.
