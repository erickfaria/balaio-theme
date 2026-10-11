#!/usr/bin/env python3
"""Check local Markdown links; external URLs and heading anchors are not fetched."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def validate():
    documents = list(ROOT.glob("*.md"))
    for directory in [ROOT / "docs", ROOT / ".github"]:
        documents.extend(directory.rglob("*.md"))
    errors = []
    for document in documents:
        for target in re.findall(r"\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            path = document.parent / unquote(url.path)
            if not path.exists():
                errors.append(f"{document.relative_to(ROOT)}: missing link {target}")
    if errors:
        raise ValueError("\n".join(errors))
    print(f"OK: local links checked in {len(documents)} Markdown files.")


if __name__ == "__main__":
    try:
        validate()
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
