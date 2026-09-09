---
title: Appointment
description: A scheduled intent for a patient to receive a service at a particular
  date, time, location, and/or with a particular provider.
tags:
- Concept/Appointment
kb:
  id: concept.appointment
  type: concept
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  source_systems:
  - Epic
  aliases:
  - scheduled visit
  - appointment record
  relationships:
    domains:
    - domain.scheduling-access
    - domain.outpatient-care
    metrics:
    - metric.no-show-rate
    - metric.appointment-lead-time
    assets:
    - asset.curated-appointment
    guides:
    - guide.dates
    - guide.grain
---

# Appointment

## Plain-language definition

A scheduled intent for a patient to receive a service at a particular date, time, location, and/or with a particular provider.

## What the operational system is doing

An appointment is a scheduling object whose status and attributes can change over time. Rescheduling, cancellation, arrival, and completion workflows may alter or replace the record depending on configuration.

## Analytical interpretation

Use appointment data when the question concerns scheduling behavior, access, capacity, appointment outcomes, or scheduled demand. Do not assume an appointment is the same thing as a completed clinical encounter.

## Typical grain

Typically one row per appointment in a curated appointment table, but history tables may contain several rows per appointment as attributes change.

--8<-- "includes/snippets/grain-warning.md"

## Common pitfalls

- Counting rescheduled history as separate appointments.
- Using appointment creation date as a proxy for patient wait time.
- Assuming every completed appointment maps one-to-one to an encounter.
