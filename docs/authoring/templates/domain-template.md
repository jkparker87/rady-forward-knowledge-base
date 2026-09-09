---
title: Domain template
description: Reusable domain template for new knowledge-base content.
tags:
- Type/Authoring
- Type/Template
kb:
  id: template.domain-template
  type: template
  status: approved
  render_connections: false
  review:
    last_reviewed: '2026-09-08'
---

# Domain template

Copy this file to `docs/domains/<slug>.md` and replace every placeholder.

```yaml
---
title: <Domain name>
description: <One-sentence scope>
tags:
  - Domain/<Domain name>
kb:
  id: domain.<stable-slug>
  type: domain
  status: draft
  owners:
    business: <Business owner role>
    technical: Analytics Engineering
  source_systems:
    - <System>
  relationships:
    concepts: []
    metrics: []
    assets: []
    guides: []
  review:
    last_reviewed: <YYYY-MM-DD>
---
```

## Common business questions

- ...

## Major events and states

| Event / state | Why it matters |
| --- | --- |
| ... | ... |

## Interpretation risks

- ...

## How to use this domain

Explain where a consumer should start and what should be clarified before choosing data.
