---
title: Data Quality Assessment
description: A repeatable framework for assessing whether data is fit for an analytical
  purpose.
tags:
- Topic/Data Quality
kb:
  id: guide.data-quality-assessment
  type: guide
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---

# Data quality assessment

Evaluate quality against a specific intended use.

## 1. State the intended use

Write the decision or analysis the data will support. A dataset cannot be declared “high quality” in the abstract.

## 2. Evaluate dimensions

| Dimension | Example test |
| --- | --- |
| Validity | Values fall within allowed statuses / ranges |
| Completeness | Expected records and required fields are present |
| Accuracy | Sampled values reconcile to the operational source or trusted reference |
| Consistency | Equivalent workflows are represented comparably |
| Timeliness | Refresh meets the decision cadence |
| Reliability | Repeated runs and periods behave predictably |
| Uniqueness | Business keys are unique at the declared grain |

## 3. Quantify limitations

Do not stop at “some values are missing.” State which fields, which populations, how often, and whether the missingness could bias interpretation.

## 4. Decide fitness for use

Possible outcomes:

- fit for the intended use
- fit with documented caveats
- fit only for limited populations
- not fit for the intended use

Quality assessment should lead to a decision, not just a list of defects.
