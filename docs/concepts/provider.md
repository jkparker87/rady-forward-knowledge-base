---
title: Provider
description: A person or organizational entity associated with care delivery, scheduling,
  ordering, billing, or another operational role.
tags:
- Concept/Provider
kb:
  id: concept.provider
  type: concept
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  source_systems:
  - Epic
  aliases:
  - clinician
  - practitioner
  relationships:
    domains:
    - domain.scheduling-access
    - domain.outpatient-care
    - domain.surgical-services
    assets:
    - asset.dim-provider
    - asset.curated-appointment
    - asset.curated-encounter
    guides:
    - guide.joins
    - guide.historical-changes
---

# Provider

## Plain-language definition

A person or organizational entity associated with care delivery, scheduling, ordering, billing, or another operational role.

## What the operational system is doing

The same person may appear in several provider roles and organizational contexts. Specialty, department, and active status can also change over time.

## Analytical interpretation

Choose the provider role that matches the question. Scheduling provider is not automatically the same as rendering, attending, ordering, or billing provider.

## Typical grain

A provider dimension is typically one row per provider identity; provider-role associations may be one-to-many.

--8<-- "includes/snippets/grain-warning.md"

## Common pitfalls

- Using the first available provider field without defining the role.
- Ignoring specialty or department changes over time.
- Counting provider-role rows as distinct providers.
