---
title: Publishing a New Document
status: draft
owner: Rady Forward maintainers
audience:
  - content-contributor
review_cycle: annual
tags:
  - contributing
  - documentation
---

# Publishing a New Document

Use this workflow to add a Markdown document to Rady Forward and publish it through MkDocs.

## 1. Choose the document location

Create the file under `docs/` in the section that best matches its subject. Use a short, descriptive, lowercase filename with hyphens, such as:

```text
docs/how-we-work/publishing-a-new-document.md
```

Do not place source documents in `site/`. MkDocs generates that directory during the build.

## 2. Start with the page template

Copy `docs/templates/page-template.md` and update its front matter and content. At minimum, identify the page title, status, owner, audience, review cycle, and tags.

```yaml
---
title: Example Document
status: draft
owner: Team or Role
audience:
  - data-consumer
review_cycle: annual
tags:
  - example
---
```

Keep the first level-one heading consistent with the `title`. Follow the [Documentation Standard](../standards/documentation.md), link to authoritative sources instead of duplicating them, and state important assumptions or limitations.

## 3. Add the document to navigation

Add the page to the appropriate section under `nav:` in `mkdocs.yml`. Paths are relative to `docs/`.

```yaml
nav:
  - How We Work:
      - how-we-work/index.md
      - Publishing a New Document: how-we-work/publishing-a-new-document.md
```

Place the entry where readers would expect to find it. Use spaces for YAML indentation; incorrect indentation can break the site build.

## 4. Preview and validate

From the repository root, create and activate a Python virtual environment if needed, then install the project dependencies:

=== "Windows PowerShell"

    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    ```

=== "macOS or Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

Start the preview server:

```bash
mkdocs serve
```

Open the local URL printed in the terminal and check the page's navigation, headings, links, formatting, and appearance in both light and dark themes.

Before submitting the change, run the same strict build used by GitHub Actions:

```bash
mkdocs build --strict
```

Resolve every warning or error. A strict build fails on issues such as invalid navigation entries or broken internal links.

## 5. Submit the document for review

Commit the Markdown file and `mkdocs.yml` change on a branch, push the branch, and open a pull request. In the pull request:

- summarize the document's purpose and intended audience;
- identify the content owner or subject-matter expert;
- note any authoritative sources used; and
- request review from the appropriate owner.

Merge only after the required review and automated checks pass.

## 6. Confirm publication

Merging to `main` starts the **Deploy Knowledge Base** GitHub Actions workflow. The workflow builds the site with strict validation and deploys it to GitHub Pages.

After the workflow succeeds, open the [published knowledge base](https://jkparker87.github.io/rady-forward-knowledge-base/) and confirm that the new document appears in navigation and that its links work. If deployment fails, open the workflow run in the repository's **Actions** tab and address the reported build error.

