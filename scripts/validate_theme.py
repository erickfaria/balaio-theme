#!/usr/bin/env python3
"""Validação estática; não executa expressões nem compila templates Blogger."""
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
                errors.append(f"ID duplicado: {identifier}")
            ids.add(identifier)
    skins = root.findall(f".//{B}skin")
    if len(skins) != 1 or not skins[0].text:
        errors.append("O tema deve conter um b:skin com CSS.")
    for section in root.iter(f"{B}section"):
        if not re.fullmatch(r"[A-Za-z0-9]+", section.get("id", "")):
            errors.append("Seção sem ID alfanumérico.")
        if any(child.tag != f"{B}widget" for child in section):
            errors.append(f"Seção {section.get('id')} contém elemento que não é widget.")
    for widget in root.iter(f"{B}widget"):
        blocks = [block.get("id") for block in widget.findall(f"{B}includable")]
        if "main" not in blocks:
            errors.append(f"Widget {widget.get('id')} sem bloco main.")
        if len(blocks) != len(set(blocks)):
            errors.append(f"Widget {widget.get('id')} com blocos duplicados.")
        for include in widget.iter(f"{B}include"):
            if include.get("name") not in blocks:
                errors.append(f"Include local inexistente: {include.get('name')}")
    blogs = [w for w in root.iter(f"{B}widget") if w.get("type") == "Blog"]
    if len(blogs) != 1:
        errors.append("O tema deve conter exatamente um widget Blog.")
    if errors:
        raise ValueError("\n".join(errors))
    print(f"OK: {path.name} — XML e estrutura local válidos. Importação no Blogger pendente.")


if __name__ == "__main__":
    try:
        validate(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "theme/balaio.xml")
    except (ET.ParseError, ValueError, OSError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        sys.exit(1)
