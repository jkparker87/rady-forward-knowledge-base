---
title: Patient Class
description: A classification describing the care setting or administrative status
  of an encounter, such as inpatient, observation, emergency, or outpatient.
tags:
- Concept/Patient Class
kb:
  id: concept.patient-class
  type: concept
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  source_systems:
  - Epic
  aliases:
  - visit class
  - encounter class
  relationships:
    domains:
    - domain.inpatient-care
    - domain.emergency-care
    concepts:
    - concept.encounter
    metrics:
    - metric.census
    - metric.length-of-stay
    assets:
    - asset.curated-encounter
    - asset.daily-census
    guides:
    - guide.snapshots-events
    - guide.historical-changes
---

# Patient Class

## Plain-language definition

A classification describing the care setting or administrative status of an encounter, such as inpatient, observation, emergency, or outpatient.

## What the operational system is doing

Patient class can change during an episode and may reflect administrative workflow as well as clinical setting.

## Analytical interpretation

Use patient class to define setting-specific populations, but confirm whether the metric requires initial class, final class, class at a point in time, or any class during the encounter.

## Typical grain

Patient class may be a current encounter attribute or a history of class transitions.

--8<-- "includes/snippets/grain-warning.md"

## Common pitfalls

- Using final patient class to reconstruct an earlier point in time.
- Assuming observation and inpatient populations are interchangeable.
- Ignoring class transitions within an encounter.
