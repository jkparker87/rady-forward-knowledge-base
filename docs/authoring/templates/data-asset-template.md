---
title: Data asset template
description: Reusable data asset template for new knowledge-base content.
tags:
- Type/Authoring
- Type/Template
kb:
  id: template.data-asset-template
  type: template
  status: approved
  render_connections: false
  review:
    last_reviewed: '2026-09-08'
---

# Data asset template

```yaml
---
title: <Asset>
description: <What the object is for>
tags:
  - Data Asset/<Table|View|Function>
kb:
  id: asset.<stable-slug>
  type: data_asset
  status: draft
  object_name: <database.schema.object>
  asset_type: <table|view|function>
  owners:
    technical: Analytics Engineering
    business_definition: <Domain steward>
  source_systems: []
  relationships:
    domains: []
    concepts: []
    metrics: []
    guides: []
  review:
    last_reviewed: <YYYY-MM-DD>
---
```

## Purpose

## Grain

State exactly what one row represents.

## Keys

| Field | Meaning |
| --- | --- |
| ... | ... |

## Important fields

| Field | Meaning |
| --- | --- |
| ... | ... |

## Refresh

## Common joins

## Known limitations

## Example query

```sql
SELECT ...
FROM ...
```
