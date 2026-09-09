---
title: Metadata Reference
description: Reference for front-matter fields used to classify, connect, review,
  and maintain knowledge-base pages.
tags:
- Type/Authoring
- Topic/Metadata
kb:
  id: reference.metadata
  type: reference
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---


# Metadata reference

Metadata is split between standard Material / MkDocs properties and the custom `kb` object.

## Core front matter

```yaml
---
title: Appointment
description: A scheduled intent for a patient to receive a service.
tags:
  - Concept/Appointment

kb:
  id: concept.appointment
  type: concept
  status: approved
  aliases:
    - scheduled visit
  owners:
    business: Access Operations
    technical: Analytics Engineering
  source_systems:
    - Epic
  relationships:
    domains:
      - domain.scheduling-access
    metrics:
      - metric.no-show-rate
  review:
    last_reviewed: 2026-09-08
---
```

## `kb` fields

| Field | Purpose |
| --- | --- |
| `id` | Stable identifier used for cross-page relationships. |
| `type` | Content type: domain, concept, metric, data_asset, guide, governance, reference, collection, or template. |
| `status` | Documentation lifecycle: draft, review, approved, deprecated. |
| `classification` | Inherited site/folder classification; align values to local policy. |
| `audience` | Intended reader groups. |
| `aliases` | Alternate business terms and search language. |
| `owners` | Durable roles / teams responsible for meaning and implementation. |
| `source_systems` | Major systems represented by the page. |
| `relationships` | Stable IDs for connected pages. |
| `review.last_reviewed` | Most recent substantive review date. |
| `review.cadence` | Expected review frequency; inherited annually by default. |
| `render_connections` | Set `false` for utility pages that should not display the generated relationship panel. |

## Directory inheritance

Material's `meta` plugin recursively merges `.meta.yml` files with page metadata. This repository uses that capability for shared classification, audience, and type tags.

## Relationship keys

The hook recognizes these display labels by default:

- `domains`
- `concepts`
- `metrics`
- `assets`
- `guides`
- `governance`

Additional keys are still rendered; they simply use a generated label.

A reference JSON schema is included at `schema/kb-metadata.schema.json`.
