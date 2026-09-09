---
title: 'Question-to-Data: Inpatient Utilization'
description: How heavily are inpatient units being used, and how is that changing
  over time?
tags:
- Question Pathway/Inpatient Utilization
kb:
  id: guide.q2d-inpatient-utilization
  type: guide
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  relationships:
    domains:
    - domain.inpatient-care
    concepts:
    - concept.census-day
    - concept.encounter
    - concept.patient-class
    - concept.department-location
    metrics:
    - metric.census
    - metric.length-of-stay
    assets:
    - asset.daily-census
    - asset.curated-encounter
    guides:
    - guide.snapshots-events
    - guide.grain
---

# Question-to-Data: Inpatient Utilization

<p class="kb-question">How heavily are inpatient units being used, and how is that changing over time?</p>

## Reasoning pathway

### 1. Choose the occupancy concept

Decide between midnight census, average daily census, patient-days, or another approved convention.

### 2. Choose the organizational level

Unit, department, service, hospital, or another hierarchy.

### 3. Define the eligible population

Clarify inpatient vs observation and how class changes are handled.

### 4. Add capacity only if comparable

Staffed, licensed, available, and physical capacity are different denominators.

### 5. Separate flow from occupancy

Admissions, discharges, transfers, and length of stay explain occupancy but are not the same measure.


## Before writing SQL

State the population, grain, start event, end event, and intended aggregation in plain language. Then select the curated entry point that preserves those choices.

--8<-- "includes/snippets/reconciliation-note.md"
