"""Garantias estruturais do validador, sem simular o compilador do Blogger."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts/validate_theme.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ThemeValidationTests(unittest.TestCase):
    def setUp(self):
        self.source = (ROOT / "theme/balaio.xml").read_text(encoding="utf-8")

    def assert_rejected(self, source, message):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.xml"
            path.write_text(source, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, message):
                VALIDATOR.validate(path)

    def test_valid_theme_with_widget_scoped_main_ids(self):
        VALIDATOR.validate(ROOT / "theme/balaio.xml")

    def test_duplicate_section_id(self):
        self.assert_rejected(self.source.replace("id='sidebar'", "id='main'"), "Duplicate ID")

    def test_missing_include(self):
        self.assert_rejected(self.source.replace("name='card'", "name='absent'"), "Missing local include")

    def test_html_inside_section(self):
        root = ET.fromstring(self.source)
        footer = root.find(".//{http://www.google.com/2005/gml/b}section[@id='footer']")
        ET.SubElement(footer, '{http://www.w3.org/1999/xhtml}p').text = 'invalid'
        self.assert_rejected(ET.tostring(root, encoding='unicode'), 'non-widget')


if __name__ == "__main__":
    unittest.main()
