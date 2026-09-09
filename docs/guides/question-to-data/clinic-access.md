---
title: 'Question-to-Data: Clinic Access'
description: How long are patients waiting to obtain outpatient care, and where is
  access constrained?
tags:
- Question Pathway/Clinic Access
kb:
  id: guide.q2d-clinic-access
  type: guide
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  relationships:
    domains:
    - domain.scheduling-access
    - domain.outpatient-care
    concepts:
    - concept.appointment
    - concept.referral
    - concept.provider
    - concept.department-location
    metrics:
    - metric.appointment-lead-time
    - metric.no-show-rate
    assets:
    - asset.curated-appointment
    - asset.fn-business-days
    guides:
    - guide.dates
    - guide.rates-denominators
---

# Question-to-Data: Clinic Access

<p class="kb-question">How long are patients waiting to obtain outpatient care, and where is access constrained?</p>

## Reasoning pathway

### 1. Define the start event

Decide whether wait begins at referral creation, appointment request, appointment creation, or another operational milestone.

### 2. Define the end event

Usually the scheduled appointment date for prospective access, or completed service date for realized access.

### 3. Choose the population

Specify specialty, visit type, new/return status, departments, and exclusions.

### 4. Choose the summary

Median and percentiles often reveal more than a mean for skewed wait-time distributions.

### 5. Interpret capacity separately

Long waits can reflect demand, template capacity, provider availability, workflow delays, or combinations of these.


## Before writing SQL

State the population, grain, start event, end event, and intended aggregation in plain language. Then select the curated entry point that preserves those choices.

--8<-- "includes/snippets/reconciliation-note.md"
