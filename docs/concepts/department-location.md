---
title: Department & Location
description: Organizational structures that describe where care or operational work
  occurs. A department and a physical location are related but not necessarily identical
  concepts.
tags:
- Concept/Department & Location
kb:
  id: concept.department-location
  type: concept
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
  source_systems:
  - Epic
  aliases:
  - department
  - clinic
  - unit
  - location
  relationships:
    domains:
    - domain.scheduling-access
    - domain.inpatient-care
    - domain.emergency-care
    - domain.outpatient-care
    - domain.surgical-services
    assets:
    - asset.curated-appointment
    - asset.curated-encounter
    - asset.daily-census
    guides:
    - guide.joins
    - guide.historical-changes
---

# Department & Location

## Plain-language definition

Organizational structures that describe where care or operational work occurs. A department and a physical location are related but not necessarily identical concepts.

## What the operational system is doing

Departments often reflect EHR configuration, scheduling, billing, or reporting structures; locations can reflect physical space. Organizations may layer service lines or custom groupings on top.

## Analytical interpretation

Use the organizational hierarchy that matches the decision. Physical location, operational department, specialty, cost center, and service line should not be substituted for one another without an explicit mapping.

## Typical grain

Dimensions are often one row per configured department or location, with hierarchy mappings represented separately.

--8<-- "includes/snippets/grain-warning.md"

## Common pitfalls

- Treating department and physical location as synonyms.
- Ignoring organizational reconfiguration over time.
- Using free-text department labels instead of stable identifiers.
