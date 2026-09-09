---
title: Join Data Safely
description: How to reason about one-to-one, one-to-many, and many-to-many joins without
  introducing hidden duplication.
tags:
- Topic/Joins
kb:
  id: guide.joins
  type: guide
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---

# Join data safely

A join should preserve the grain you intend to analyze.

## Relationship types

| Relationship | Example | Main risk |
| --- | --- | --- |
| One-to-one | Encounter → unique encounter attributes | Usually low if keys are truly unique |
| Many-to-one | Many encounters → one provider dimension row | Dimension duplication if the dimension is not actually unique |
| One-to-many | Encounter → diagnoses | Row multiplication |
| Many-to-many | Providers ↔ specialties | Combinatorial duplication |

## Safer patterns

- aggregate the many-side before joining when the analysis only needs a summary
- use existence logic when you only need to know whether a related record exists
- validate key uniqueness before treating a table as a dimension
- compare row counts and distinct business keys before and after joins
- avoid `DISTINCT` as a generic fix for an unexplained join problem

`DISTINCT` can hide duplication without fixing the underlying analytical mistake.
