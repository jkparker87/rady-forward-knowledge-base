---
title: Referral
description: A request or authorization pathway intended to connect a patient with
  a service, specialty, or provider.
tags:
- Concept/Referral
kb:
  id: concept.referral
  type: concept
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  source_systems:
  - Epic
  aliases:
  - referral order
  relationships:
    domains:
    - domain.scheduling-access
    concepts:
    - concept.appointment
    metrics:
    - metric.appointment-lead-time
    guides:
    - guide.dates
    - guide.joins
---

# Referral

## Plain-language definition

A request or authorization pathway intended to connect a patient with a service, specialty, or provider.

## What the operational system is doing

A referral can have its own lifecycle, statuses, authorizations, scheduling links, and closure rules. It may produce zero, one, or several appointments depending on workflow.

## Analytical interpretation

Use referral data when measuring referral demand, conversion, referral-to-appointment time, or leakage. Define what counts as referral initiation and completion.

## Typical grain

Often one row per referral in a curated representation; referral events or status history may be one-to-many.

--8<-- "includes/snippets/grain-warning.md"

## Common pitfalls

- Assuming every referral results in exactly one appointment.
- Mixing referral created date with appointment scheduled date.
- Ignoring referrals closed without scheduled service.
