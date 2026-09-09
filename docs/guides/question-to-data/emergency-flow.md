---
title: 'Question-to-Data: Emergency Flow'
description: Where are patients spending time in the emergency-care journey, and where
  do delays occur?
tags:
- Question Pathway/Emergency Flow
kb:
  id: guide.q2d-emergency-flow
  type: guide
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  relationships:
    domains:
    - domain.emergency-care
    concepts:
    - concept.encounter
    - concept.department-location
    - concept.patient-class
    metrics:
    - metric.ed-boarding-time
    assets:
    - asset.curated-encounter
    guides:
    - guide.dates
    - guide.grain
---

# Question-to-Data: Emergency Flow

<p class="kb-question">Where are patients spending time in the emergency-care journey, and where do delays occur?</p>

## Reasoning pathway

### 1. Draw the timeline

Name arrival, clinical start, disposition decision, departure, and inpatient arrival events.

### 2. Choose one duration at a time

Arrival-to-provider, ED length of stay, and boarding time are separate measures.

### 3. Define admitted visits

State exactly which disposition or downstream encounter logic determines admission.

### 4. Check missing timestamps

Missing events can systematically exclude the hardest cases if not evaluated.

### 5. Stratify thoughtfully

Arrival period, acuity, destination, and volume context can materially change interpretation.


## Before writing SQL

State the population, grain, start event, end event, and intended aggregation in plain language. Then select the curated entry point that preserves those choices.

--8<-- "includes/snippets/reconciliation-note.md"
