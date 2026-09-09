---
title: GitHub / Repository Architecture
status: draft
tags:
  - github
  - technical
---

# GitHub / Repository Architecture

The repository should be the source of truth for version-controlled implementation and documentation source.

A useful high-level structure is:

```text
rady-forward-knowledge-base/
├── .github/
│   └── workflows/
├── docs/
│   ├── start-here/
│   ├── how-we-work/
│   ├── standards/
│   ├── product-design/
│   ├── systems/
│   ├── ai-automation/
│   ├── governance/
│   ├── learning/
│   ├── technical/
│   └── templates/
├── scripts/
├── mkdocs.yml
├── requirements.txt
└── README.md
```

For a larger analytics monorepo, the documentation site can still live under `docs/`, but the navigation should remain organized around user questions rather than mirror the repository's code folders.
