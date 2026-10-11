#!/usr/bin/env python3
"""Static validation; does not evaluate expressions or compile Blogger templates."""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

B = "{http://www.google.com/2005/gml/b}"
ROOT = Path(__file__).resolve().parents[1]


def validate(path):
    root = ET.parse(path).getroot()
    errors = []
    ids = set()
    for node in root.iter():
        identifier = node.get("id")
        if identifier and node.tag != f"{B}includable":
            if identifier in ids:
                errors.append(f"Duplicate ID: {identifier}")
            ids.add(identifier)
    skins = root.findall(f".//{B}skin")
    if len(skins) != 1 or not skins[0].text:
        errors.append("The theme must contain one b:skin with CSS.")
    for section in root.iter(f"{B}section"):
        if not re.fullmatch(r"[A-Za-z0-9]+", section.get("id", "")):
            errors.append("Section requires an alphanumeric ID.")
        if any(child.tag != f"{B}widget" for child in section):
            errors.append(f"Section {section.get('id')} contains a non-widget element.")
    for widget in root.iter(f"{B}widget"):
        blocks = [block.get("id") for block in widget.findall(f"{B}includable")]
        if "main" not in blocks:
            errors.append(f"Widget {widget.get('id')} has no main block.")
        if len(blocks) != len(set(blocks)):
            errors.append(f"Widget {widget.get('id')} has duplicate blocks.")
        for include in widget.iter(f"{B}include"):
            if include.get("name") not in blocks:
                errors.append(f"Missing local include: {include.get('name')}")
    blogs = [w for w in root.iter(f"{B}widget") if w.get("type") == "Blog"]
    if len(blogs) != 1:
        errors.append("The theme must contain exactly one Blog widget.")
    if errors:
        raise ValueError("\n".join(errors))
    print(f"OK: {path.name} — XML and local structure valid. Blogger import remains unverified.")


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            validate(Path(sys.argv[1]))
        else:
            for path in sorted((ROOT / "theme").glob("*.xml")):
                validate(path)
    except (ET.ParseError, ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
