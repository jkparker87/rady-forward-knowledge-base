---
title: Find the Right Data
description: A practical method for selecting the right concepts, metrics, and curated
  assets.
tags:
- Type/Reference
- Topic/Data Discovery
kb:
  id: reference.find-right-data
  type: reference
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  relationships:
    guides:
    - guide.grain
    - guide.dates
    - guide.rates-denominators
---


# Find the right data

A good search starts with the question rather than a table name.

## Ask these questions first

| Question | Why it matters |
| --- | --- |
| What event or state am I trying to measure? | Distinguishes appointments, encounters, referrals, snapshots, and other grains. |
| What population should be included? | Prevents accidental mixing of clinical settings, statuses, or service types. |
| Which date defines the analysis period? | Creation, scheduled, arrival, admission, discharge, and completion dates answer different questions. |
| Do I need a count, rate, duration, or snapshot? | Determines the analytical structure and denominator. |
| What level should one row represent? | Determines safe joins and aggregations. |
| Is there already a curated entry point? | Avoids recreating business logic. |

## Recommended search path

**Domain → concept → metric → curated asset**

For example, a question about access may begin in **Scheduling & Access**, then move to **Appointment**, then to **Appointment Lead Time**, and finally to a curated appointment asset.

If you cannot state the population, date basis, and grain in plain language, the question is not ready to become SQL.
