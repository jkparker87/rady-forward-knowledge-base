---
title: Metric template
description: Reusable metric template for new knowledge-base content.
tags:
- Type/Authoring
- Type/Template
kb:
  id: template.metric-template
  type: template
  status: approved
  render_connections: false
  review:
    last_reviewed: '2026-09-08'
---

# Metric template

```yaml
---
title: <Metric>
description: <Question the metric answers>
tags:
  - Metric/<Metric>
kb:
  id: metric.<stable-slug>
  type: metric
  status: draft
  owners:
    business_definition: <Role>
    technical_implementation: Analytics Engineering
  relationships:
    domains: []
    concepts: []
    assets: []
    guides: []
  review:
    last_reviewed: <YYYY-MM-DD>
---
```

## Question

## Definition

**Formula:** `<formula>`

| Component | Definition |
| --- | --- |
| Eligible population | ... |
| Numerator | ... |
| Denominator | ... |
| Time basis | ... |

## Recommended dimensions

## Interpretation risks
