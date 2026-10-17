"""Protect the native contact contract and prevent the hidden-sidebar regression."""
from html.parser import HTMLParser
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
B = "{http://www.google.com/2005/gml/b}"
H = "{http://www.w3.org/1999/xhtml}"
E = "{http://www.google.com/2005/gml/expr}"


class PageMarkers(HTMLParser):
    def __init__(self):
        super().__init__()
        self.markers = 0
        self.template_tags = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "balaio-contact-page" in attrs.get("class", "").split():
            self.markers += 1
        if tag.startswith("b:") or tag in ("form", "script", "html", "body"):
            self.template_tags.append(tag)


class ContactTests(unittest.TestCase):
    def test_native_widget_is_complete_and_outside_the_hidden_sidebar(self):
        for path in (ROOT / "theme").glob("*.xml"):
            with self.subTest(locale=path.name):
                root = ET.parse(path).getroot()
                parent = {child: node for node in root.iter() for child in node}
                widgets = root.findall(f".//{B}widget[@type='ContactForm']")
                self.assertEqual(len(widgets), 1)
                widget = widgets[0]
                section = parent[widget]
                self.assertEqual(section.get("id"), "contactpage")
                self.assertEqual(parent[section].tag, H + "main")
                self.assertEqual(widget.get("cond"), 'data:blog.pageType == "static_page"')
                fields = {node.get(E + "id"): node for node in widget.iter() if node.get(E + "id")}
                suffixes = ("name", "email", "email-message", "submit", "error-message", "success-message")
                for suffix in suffixes:
                    self.assertIn('data:widget.instanceId + "_contact-form-' + suffix + '"', fields)
                labels = {node.get(E + "for") for node in widget.iter(H + "label")}
                for suffix in ("name", "email", "email-message"):
                    expr = 'data:widget.instanceId + "_contact-form-' + suffix + '"'
                    self.assertIn(expr, labels)
                    self.assertEqual(fields[expr].get("required") is not None, suffix != "name")
                submit = fields['data:widget.instanceId + "_contact-form-submit"']
                self.assertEqual(submit.get("type"), "button")
                self.assertEqual(fields['data:widget.instanceId + "_contact-form-error-message"'].get("role"), "alert")
                self.assertEqual(fields['data:widget.instanceId + "_contact-form-success-message"'].get("aria-live"), "polite")

    def test_page_samples_are_portable_content_without_widget_xml(self):
        for path in (ROOT / "examples/pages").glob("contact.*.html"):
            with self.subTest(locale=path.name):
                sample = path.read_text()
                parser = PageMarkers()
                parser.feed(sample)
                self.assertEqual(parser.markers, 1)
                self.assertEqual(parser.template_tags, [])
                self.assertNotIn("/p/", sample)
                self.assertNotIn("balaiocientifico.com", sample)

    def test_contact_adds_no_script_transport_or_fixed_url(self):
        for path in (ROOT / "theme").glob("*.xml"):
            root = ET.parse(path).getroot()
            widget = root.find(f".//{B}widget[@id='ContactForm1']")
            self.assertEqual(list(widget.iter(H + "script")), [])
            self.assertEqual(len(list(root.iter(H + "script"))), 2)
            self.assertNotIn("canonicalUrl", widget.get("cond"))
            css = root.find(f".//{B}skin").text
            self.assertIn("body:has(.post-body .balaio-contact-page) #contactpage", css)
            self.assertIn("#sidebar,", css)


if __name__ == "__main__":
    unittest.main()
