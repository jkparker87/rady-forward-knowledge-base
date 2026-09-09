---
title: Data Quality
status: draft
tags:
  - data-quality
  - validation
---

# Data Quality

Data quality should be evaluated deliberately rather than assumed because a query executed successfully.

## Core dimensions

### Validity
Does the data represent what it is intended to represent?

### Accuracy
Does the value agree with the real-world or authoritative value it is intended to describe?

### Reliability
Does the data or measurement behave consistently across repeated observations, time periods, systems, or analysts?

### Completeness
Are required records and fields present?

### Consistency
Do values and definitions agree across systems, time, and related data products?

### Timeliness
Is the data current enough for the decision being made?

### Uniqueness
Are records represented at the intended grain without unintended duplication?

## Minimum assessment for reusable data products

Document:

- expected grain
- expected volume
- key completeness
- duplicate behavior
- required-field missingness
- valid ranges or categories
- source reconciliation
- known limitations
- refresh expectations

As the program matures, these checks should move from manual review toward repeatable automated tests where practical.
