---
title: Authoring the Knowledge Base
description: How to add modular content without duplicating definitions or breaking
  relationships.
tags:
- Type/Authoring
kb:
  id: reference.authoring
  type: reference
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---


# Authoring the knowledge base

The content model is intentionally modular.

**Do not copy the same definition into several sections.** Give the concept one stable page and reference its `kb.id` from every related page. The build hook creates forward links and backlinks automatically.

Use snippets only for text that should appear **identically** in several places, such as a standard grain warning or reconciliation note.

## Authoring sequence

1. Decide the page type.
2. Copy the appropriate template.
3. Assign a stable `kb.id`.
4. Add relationships using other stable IDs.
5. Add hierarchical tags.
6. Write the plain-language explanation.
7. Run `mkdocs build`.
8. Resolve metadata or link warnings before merge.
