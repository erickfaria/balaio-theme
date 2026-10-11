#!/usr/bin/env python3
"""Static validation; does not evaluate expressions or compile Blogger templates."""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

B = "{http://www.google.com/2005/gml/b}"
ROOT = Path(__file__).resolve().parents[1]


def designer_settings(css):
    """Read Blogger color/font declarations and reject unresolved references."""
    settings = {}
    comments = "\n".join(re.findall(r"/\*.*?\*/", css, flags=re.S))
    for declaration in re.findall(r"<Variable\b[^>]*?/>", comments):
        attrs = ET.fromstring(declaration).attrib
        name = attrs.get("name", "")
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", name):
            raise ValueError("Designer variable requires an alphanumeric name.")
        if name in settings:
            raise ValueError(f"Duplicate Designer variable: {name}")
        if attrs.get("type") not in ("color", "font"):
            raise ValueError(f"Unsupported Designer variable type: {name}")
        if not attrs.get("description") or not attrs.get("default"):
            raise ValueError(f"Incomplete Designer variable: {name}")
        settings[name] = attrs
    references = set(re.findall(r"\$([A-Za-z][A-Za-z0-9]*)", css))
    missing = references - settings.keys()
    if missing:
        raise ValueError("Undeclared Designer variables: " + ", ".join(sorted(missing)))
    return settings


def preview_css(css):
    """Resolve saved Designer values for fixtures, without compiling Blogger."""
    settings = designer_settings(css)
    return re.sub(r"\$([A-Za-z][A-Za-z0-9]*)",
                  lambda match: settings[match[1]].get("value") or settings[match[1]]["default"], css)


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
    if len(skins) == 1 and skins[0].text:
        try:
            designer_settings(skins[0].text)
        except (ET.ParseError, ValueError) as error:
            errors.append(str(error))
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
    print(f"OK: {path.name} — XML and local structure valid.")


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
