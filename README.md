# Data Knowledge Base

This repository is a starter implementation of a human-centered data knowledge base built with **Material for MkDocs**.

The site is intentionally not an exhaustive technical catalog. Its job is to connect:

**business domain → business concept → metric → curated data asset → analytical guidance**

Alation can ultimately own exhaustive object discovery, technical lineage, certification, and catalog search. This site should remain the narrative and interpretation layer: what the data means, when to use it, what can go wrong, and how the pieces connect.

## What is included

- Content-domain documentation
- Business concept / glossary pages
- Metric definitions
- Curated SQL asset documentation patterns
- Question-to-data pathways
- Data-quality and analytical guidance
- Governance and ownership guidance
- Reusable Markdown snippets
- Directory-level `.meta.yml` inheritance
- Hierarchical Material tags
- A custom MkDocs hook that:
  - validates stable knowledge-base IDs
  - validates relationship targets
  - automatically renders related-content links
  - automatically generates reverse-reference backlinks

## Run locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
mkdocs serve
```

Then open the local address printed by MkDocs.

## Before publishing

1. Replace the placeholder `site_url` in `mkdocs.yml`.
2. Replace the example SQL object names with real curated assets.
3. Align owner names, source-system names, and classification language to local policy.
4. Add or remove domains to match the organization's actual operating model.
5. Keep stable `kb.id` values once pages are published; filenames and titles can change without breaking metadata relationships.

## Authoring model

Every substantive page receives a stable ID such as:

```yaml
kb:
  id: concept.appointment
  type: concept
  status: approved
  relationships:
    domains:
      - domain.scheduling-access
    metrics:
      - metric.no-show-rate
    assets:
      - asset.curated-appointment
```

The hook resolves those IDs to pages and creates both forward and reverse links. This makes the documentation graph modular even when the navigation structure changes.
