"""Native contact widget integration contract; no messages are sent by tests."""
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
B = "{http://www.google.com/2005/gml/b}"
H = "{http://www.w3.org/1999/xhtml}"
E = "{http://www.google.com/2005/gml/expr}"


class ContactTests(unittest.TestCase):
    def widgets(self):
        for path in (ROOT / "theme").glob("*.xml"):
            root = ET.parse(path).getroot()
            yield path.name, root.find(f".//{B}widget[@id='ContactForm1']")

    def test_native_field_ids_and_private_transport(self):
        # These suffixes are consumed by Blogger's native _ContactFormView.
        for name, widget in self.widgets():
            with self.subTest(locale=name):
                self.assertEqual(widget.get("type"), "ContactForm")
                self.assertEqual(widget.get("mobile"), "yes")
                fields = {node.get(E + "id"): node for node in widget.iter() if node.get(E + "id")}
                def field(suffix):
                    return fields['data:widget.instanceId + "_contact-form-' + suffix + '"']
                self.assertIsNone(field("name").get("required"))
                self.assertEqual(field("email").get("type"), "email")
                for suffix in ("email", "email-message"):
                    self.assertEqual(field(suffix).get("required"), "required")
                self.assertEqual(field("submit").get("type"), "button")
                self.assertEqual(field("error-message").get("role"), "alert")
                self.assertEqual(field("success-message").get("role"), "status")
                labels = {node.get(E + "for") for node in widget.iter(H + "label")}
                for suffix in ("name", "email", "email-message"):
                    self.assertIn(field(suffix).get(E + "id"), labels)
                form = widget.find(f".//{H}form")
                self.assertEqual(form.get("method"), "post")
                self.assertEqual(form.get("action"), "#")
                self.assertFalse(list(widget.iter(H + "script")))

    def test_scope_and_default_pages(self):
        for name, widget in self.widgets():
            with self.subTest(locale=name):
                condition = widget.get("cond", "")
                self.assertIn('data:blog.pageType == "static_page" and', condition)
                self.assertIn('"p/contato.html"', condition)
                self.assertIn('"p/contact.html"', condition)
                self.assertIn('data:blog.canonicalUrl == data:blog.canonicalHomepageUrl +', condition)
                self.assertNotIn("balaiocientifico.com", condition)
        for locale in ("pt-BR", "en"):
            text = (ROOT / f"examples/pages/contact.{locale}.html").read_text()
            self.assertNotIn("<form", text)
            self.assertNotIn("Lorem ipsum", text)


if __name__ == "__main__":
    unittest.main()
