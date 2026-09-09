---
title: Content Model
description: The modular relationship model connecting domains, concepts, metrics,
  assets, guides, and governance.
tags:
- Type/Authoring
- Topic/Metadata
kb:
  id: reference.content-model
  type: reference
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---


# Content model

The site treats documentation as a small knowledge graph.

```mermaid
flowchart TD
    D[Domain] --> C[Concept]
    D --> M[Metric]
    C --> M
    C --> A[Data asset]
    M --> A
    C --> G[Guide]
    M --> G
    A --> G
    V[Governance] --> D
    V --> C
    V --> M
    V --> A
```

## Stable IDs

A filename is a navigation concern. A `kb.id` is the conceptual identity.

Examples:

- `domain.scheduling-access`
- `concept.appointment`
- `metric.no-show-rate`
- `asset.curated-appointment`
- `guide.grain`

Once published, prefer keeping the ID stable even if the title or file path changes.

## Forward relationships

Pages list IDs under `kb.relationships`:

```yaml
kb:
  relationships:
    domains:
      - domain.scheduling-access
    concepts:
      - concept.appointment
    metrics:
      - metric.no-show-rate
```

## Reverse relationships

Do **not** manually maintain “referenced by” lists. The build hook calculates them from forward relationships. This is the main mechanism that prevents cross-reference drift.
