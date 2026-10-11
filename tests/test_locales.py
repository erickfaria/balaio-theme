"""Ensure language variants preserve the same styling and widget identities."""
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
B = "{http://www.google.com/2005/gml/b}"


class LocaleTests(unittest.TestCase):
    def setUp(self):
        self.pt = ET.parse(ROOT / "theme/balaio.xml").getroot()
        self.en = ET.parse(ROOT / "theme/balaio.en.xml").getroot()

    def test_same_css_without_translated_comments(self):
        def css(tree):
            return re.sub(r"/\*.*?\*/", "", tree.find(f".//{B}skin").text, flags=re.S)
        self.assertEqual(css(self.pt), css(self.en))

    def test_same_widget_ids_and_types(self):
        def widgets(tree):
            return [(w.get("id"), w.get("type")) for w in tree.iter(f"{B}widget")]
        self.assertEqual(widgets(self.pt), widgets(self.en))


if __name__ == "__main__":
    unittest.main()
