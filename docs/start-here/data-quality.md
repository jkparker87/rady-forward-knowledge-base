---
title: Understand Data Quality
description: How to evaluate whether data is fit for the question being asked.
tags:
- Type/Reference
- Topic/Data Quality
kb:
  id: reference.data-quality
  type: reference
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  relationships:
    guides:
    - guide.data-quality-assessment
---


# Understand data quality

Data quality is not a single score. Data can be technically clean and still be inappropriate for a specific question.

| Dimension | Practical question |
| --- | --- |
| **Validity** | Does the value conform to the rules and possible values of the field? |
| **Accuracy** | Does the value reflect the real-world state or event it is intended to represent? |
| **Completeness** | Is the expected information present for the population and time period? |
| **Consistency** | Are definitions and representations stable across sources, departments, and time? |
| **Timeliness** | Is the data current enough for the intended decision? |
| **Reliability** | Does the process produce sufficiently stable and reproducible information over time? |
| **Uniqueness** | Are duplicated records or entities introducing over-counting? |

Quality must be evaluated against intended use. A manually entered cancellation reason may be adequate for operational follow-up but too inconsistently populated for a precise organization-wide benchmark.

[Use the data quality assessment guide](../guides/data-quality-assessment.md) when evaluating a new dataset or metric.
