"""Build-time metadata graph for the Data Knowledge Base.

The hook:
1. Reads stable `kb.id` values from Markdown front matter.
2. Validates uniqueness and relationship targets.
3. Appends a human-readable "Knowledge connections" section.
4. Generates reverse-reference backlinks automatically.

It intentionally does not try to become a data catalog. The graph is about
documentation concepts, not exhaustive physical lineage.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import html
import logging
import posixpath
import re

import yaml

log = logging.getLogger("mkdocs")

REGISTRY = {}
BACKLINKS = defaultdict(list)

RELATION_LABELS = {
    "domains": "Domains",
    "concepts": "Business concepts",
    "metrics": "Metrics",
    "assets": "Data assets",
    "guides": "Guides",
    "governance": "Governance",
}

VALID_TYPES = {
    "collection",
    "domain",
    "concept",
    "metric",
    "data_asset",
    "guide",
    "governance",
    "reference",
    "template",
}

VALID_STATUS = {"draft", "review", "approved", "deprecated"}


def _front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        return {}
    value = yaml.safe_load(match.group(1))
    return value if isinstance(value, dict) else {}


def _display_title(meta: dict, file) -> str:
    return str(meta.get("title") or Path(file.src_uri).stem.replace("-", " ").title())


def _page_base(url: str) -> str:
    url = "/" + (url or "")
    if url.endswith("/"):
        return url
    return posixpath.dirname(url) + "/"


def _relative_url(current_url: str, target_url: str) -> str:
    current = _page_base(current_url)
    target = "/" + (target_url or "")
    rel = posixpath.relpath(target, current)
    if target.endswith("/") and not rel.endswith("/"):
        rel += "/"
    return "./" if rel == "." else rel


def _escape(text) -> str:
    return html.escape(str(text), quote=False)


def on_files(files, config, **kwargs):
    """Build the page-ID registry before rendering pages."""
    global REGISTRY, BACKLINKS
    REGISTRY = {}
    BACKLINKS = defaultdict(list)

    docs_dir = Path(config.docs_dir)

    for file in files:
        if not getattr(file, "is_documentation_page", lambda: False)():
            continue
        source = docs_dir / file.src_uri
        meta = _front_matter(source)
        kb = meta.get("kb") or {}
        kb_id = kb.get("id")
        if not kb_id:
            continue

        if kb_id in REGISTRY:
            log.warning(
                "Duplicate kb.id '%s' in %s and %s",
                kb_id,
                REGISTRY[kb_id]["file"].src_uri,
                file.src_uri,
            )
            continue

        REGISTRY[kb_id] = {
            "file": file,
            "meta": meta,
            "title": _display_title(meta, file),
        }

    for source_id, item in REGISTRY.items():
        relationships = (item["meta"].get("kb") or {}).get("relationships") or {}
        if not isinstance(relationships, dict):
            log.warning("kb.relationships must be a mapping on %s", item["file"].src_uri)
            continue
        for rel_name, targets in relationships.items():
            if not targets:
                continue
            if not isinstance(targets, list):
                log.warning(
                    "Relationship '%s' must be a list on %s",
                    rel_name,
                    item["file"].src_uri,
                )
                continue
            for target_id in targets:
                if target_id not in REGISTRY:
                    log.warning(
                        "Unknown relationship target '%s' referenced by %s",
                        target_id,
                        item["file"].src_uri,
                    )
                else:
                    BACKLINKS[target_id].append((source_id, rel_name))

    return files


def _validate_page(page):
    kb = page.meta.get("kb") or {}
    if not kb:
        return

    kb_type = kb.get("type")
    kb_id = kb.get("id")
    status = kb.get("status")

    if kb_type and kb_type not in VALID_TYPES:
        log.warning("Unknown kb.type '%s' on %s", kb_type, page.file.src_uri)

    if kb_type != "template":
        for key in ("id", "type", "status"):
            if not kb.get(key):
                log.warning("Missing kb.%s on %s", key, page.file.src_uri)

    if status and status not in VALID_STATUS:
        log.warning("Unknown kb.status '%s' on %s", status, page.file.src_uri)

    if kb_id and kb_id not in REGISTRY:
        # Usually means the ID was inherited from .meta.yml, which should not happen.
        log.warning("kb.id '%s' is not registered for %s", kb_id, page.file.src_uri)


def _link_list(page, ids):
    links = []
    for target_id in ids:
        target = REGISTRY.get(target_id)
        if not target:
            links.append(f"`{_escape(target_id)}`")
            continue
        url = _relative_url(page.url, target["file"].url)
        links.append(f"[{_escape(target['title'])}]({url})")
    return ", ".join(links)


def on_page_markdown(markdown, page, config, files, **kwargs):
    _validate_page(page)

    kb = page.meta.get("kb") or {}
    if not kb or kb.get("render_connections", True) is False:
        return markdown

    kb_id = kb.get("id")
    if not kb_id:
        return markdown

    rows = []

    status = kb.get("status")
    if status:
        rows.append(("Status", f'<span class="kb-status">{_escape(status)}</span>'))

    rows.append(("Knowledge ID", f"`{_escape(kb_id)}`"))

    aliases = kb.get("aliases") or []
    if aliases:
        rows.append(("Also called", ", ".join(_escape(x) for x in aliases)))

    owners = kb.get("owners") or {}
    if isinstance(owners, dict) and owners:
        owner_text = "; ".join(f"**{_escape(k).replace('_', ' ').title()}:** {_escape(v)}"
                               for k, v in owners.items())
        rows.append(("Ownership", owner_text))

    source_systems = kb.get("source_systems") or []
    if source_systems:
        rows.append(("Source systems", ", ".join(_escape(x) for x in source_systems)))

    relationships = kb.get("relationships") or {}
    if isinstance(relationships, dict):
        for rel_name, ids in relationships.items():
            if ids:
                label = RELATION_LABELS.get(rel_name, rel_name.replace("_", " ").title())
                rows.append((label, _link_list(page, ids)))

    backlinks = []
    seen = set()
    for source_id, rel_name in BACKLINKS.get(kb_id, []):
        if source_id in seen:
            continue
        seen.add(source_id)
        source = REGISTRY.get(source_id)
        if not source:
            continue
        url = _relative_url(page.url, source["file"].url)
        backlinks.append(f"[{_escape(source['title'])}]({url})")
    if backlinks:
        rows.append(("Referenced by", ", ".join(backlinks)))

    review = kb.get("review") or {}
    if isinstance(review, dict):
        review_bits = []
        if review.get("last_reviewed"):
            review_bits.append(f"last reviewed {_escape(review['last_reviewed'])}")
        if review.get("cadence"):
            review_bits.append(f"cadence: {_escape(review['cadence'])}")
        if review_bits:
            rows.append(("Review", "; ".join(review_bits)))

    if not rows:
        return markdown

    table = ["| | |", "| --- | --- |"]
    for label, value in rows:
        table.append(f"| **{label}** | {value} |")

    block = "\n".join([
        "",
        '<div class="kb-connections" markdown>',
        "",
        "## Knowledge connections",
        "",
        *table,
        "",
        "</div>",
        "",
    ])
    return markdown.rstrip() + "\n" + block
