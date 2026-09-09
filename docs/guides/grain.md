---
title: Understand Grain
description: Grain is the definition of what one row represents.
tags:
- Topic/Grain
kb:
  id: guide.grain
  type: guide
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---

# Understand grain

**Grain is the first analytical decision.** Before counting rows, joining tables, or calculating a rate, state what one row represents in plain language.

Examples:

- one row per appointment
- one row per encounter
- one row per patient
- one row per patient-day
- one row per department-month

## Why grain matters

Suppose an encounter has three diagnosis rows. Joining an encounter-level table to diagnosis without controlling the one-to-many relationship turns one encounter into three rows. A later `COUNT(*)` is technically valid SQL and analytically wrong.

## A practical rule

Before every join, write:

> Left side: one row per ____.  
> Right side: one row per ____.  
> After the join: one row per ____.

If the third blank is unclear, the join is not ready.

--8<-- "includes/snippets/grain-warning.md"
