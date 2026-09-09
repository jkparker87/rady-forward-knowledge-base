---
title: Patient
description: The person receiving or seeking care, represented through one or more
  identifiers and demographic attributes.
tags:
- Concept/Patient
kb:
  id: concept.patient
  type: concept
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  source_systems:
  - Epic
  aliases:
  - person
  - patient identity
  relationships:
    domains:
    - domain.inpatient-care
    - domain.emergency-care
    - domain.surgical-services
    assets:
    - asset.curated-appointment
    - asset.curated-encounter
    guides:
    - guide.joins
    - guide.historical-changes
---

# Patient

## Plain-language definition

The person receiving or seeking care, represented through one or more identifiers and demographic attributes.

## What the operational system is doing

Patient identity is managed through registration and identity-management workflows. Attributes can change and duplicate identities may be merged.

## Analytical interpretation

Use a stable enterprise patient identifier when counting unique patients. Be explicit about whether demographic attributes should reflect current values or values at the time of an encounter.

## Typical grain

A patient dimension is generally one row per enterprise patient identity; encounter and appointment assets contain repeated patient identifiers.

--8<-- "includes/snippets/grain-warning.md"

## Common pitfalls

- Counting rows instead of distinct patients.
- Using mutable demographic attributes without deciding whether point-in-time history matters.
- Combining identifiers from different systems without an identity-resolution rule.
