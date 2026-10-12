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
        self.assert_rejected(self.source.replace("id='navigation'", "id='main'"), "Duplicate ID")

    def test_migration_keeps_complete_widgets(self):
        root = ET.fromstring(self.source)
        namespace = '{http://www.google.com/2005/gml/b}'
        widgets = {w.get('id'): w for w in root.iter(namespace + 'widget')}
        for identifier in ['Header1', 'PageList1', 'LinkList1', 'HTML1', 'Blog1', 'Label1']:
            self.assertIsNotNone(widgets[identifier].find(namespace + "includable[@id='main']"))
        labels = widgets['Label1']
        self.assertIsNotNone(labels.find('.//' + namespace + 'loop'))
        self.assertIsNone(root.find('.//' + namespace + "if[@cond='false']"))
        self.assertIn('#sidebar,', self.source)
        self.assertIsNone(root.find(".//{http://www.w3.org/1999/xhtml}div[@hidden='hidden']"))

    def test_continuation_script_is_separate_from_widget_rendering(self):
        root = ET.fromstring(self.source)
        namespace = '{http://www.google.com/2005/gml/b}'
        html = '{http://www.w3.org/1999/xhtml}'
        for widget in root.iter(namespace + 'widget'):
            self.assertEqual(list(widget.iter(html + 'script')), [])
        script = root.find(".//" + html + "script[@id='home-continuation']")
        self.assertIsNotNone(script)
        body = root.find(html + 'body')
        parent = next(node for node in body if script in list(node))
        self.assertEqual(parent.tag, namespace + 'if')
        self.assertEqual(parent.get('cond'), 'data:blog.url == data:blog.homepageUrl')

    def test_missing_include(self):
        self.assert_rejected(self.source.replace("name='card'", "name='absent'"), "Missing local include")

    def test_html_inside_section(self):
        root = ET.fromstring(self.source)
        sidebar = root.find(".//{http://www.google.com/2005/gml/b}section[@id='main']")
        ET.SubElement(sidebar, '{http://www.w3.org/1999/xhtml}p').text = 'invalid'
        self.assert_rejected(ET.tostring(root, encoding='unicode'), 'non-widget')


if __name__ == "__main__":
    unittest.main()
