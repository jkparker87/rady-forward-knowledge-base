---
title: How Our Data Works
description: A conceptual view of how operational activity becomes curated analytical
  data.
tags:
- Type/Reference
- Topic/Data Architecture
kb:
  id: reference.how-data-works
  type: reference
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  relationships:
    guides:
    - guide.grain
    - guide.snapshots-events
    - guide.historical-changes
---


# How our data works

Operational systems are optimized to support care and business workflows. Analytical systems reorganize those records so they can be used consistently for reporting, measurement, and analysis.

```mermaid
flowchart LR
    A[Operational workflow] --> B[Source system records]
    B --> C[Reporting / warehouse layer]
    C --> D[Curated analytical layer]
    D --> E[Metrics and analysis]
    E --> F[Decision or action]
```

## Why a curated layer exists

A curated layer should absorb recurring technical complexity:

- joining related source records
- applying stable inclusion and exclusion logic
- standardizing identifiers and dimensions
- resolving common timestamp choices
- representing useful analytical grains
- exposing derived fields that would otherwise be recreated inconsistently

A curated table is not automatically the answer to every question. It is a **recommended starting point with an explicit grain and purpose**.

## Why source records and analytical concepts differ

Operational systems often contain several records for what a person informally thinks of as one thing. An appointment can be created, rescheduled, canceled, recreated, linked to an encounter, and associated with multiple timestamps. An analytical representation must decide which events and states matter for the intended use.

That is why this site documents both the **concept** and the **asset**.
