---
title: Events vs. Snapshots
description: How event data differs from point-in-time or interval representations.
tags:
- Topic/Temporal Modeling
kb:
  id: guide.snapshots-events
  type: guide
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---

# Events vs. snapshots

Some questions ask **what happened**. Others ask **what was true at a point in time**.

## Event model

Examples: admission, discharge, cancellation, transfer, referral creation.

Event data is well suited to counts and durations between explicit events.

## Snapshot model

Examples: midnight census, active appointment backlog, provider roster on a date.

Snapshot data represents state at an observation point and is often easier for occupancy or inventory-style questions.

## Why this matters

You can derive snapshots from event intervals, but only if start/end events and overlap rules are reliable. Likewise, a snapshot table is usually poor for reconstructing exact event timing.

Choose the temporal model that matches the question rather than forcing one table to do both jobs.
