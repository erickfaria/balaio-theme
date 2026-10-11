"""Guard against mobile URLs breaking search and hiding navigation widgets."""
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parents[1]
B = "{http://www.google.com/2005/gml/b}"
H = "{http://www.w3.org/1999/xhtml}"


class NavigationTests(unittest.TestCase):
    def test_search_route_ignores_mobile_query(self):
        for path in (ROOT / "theme").glob("*.xml"):
            form = ET.parse(path).getroot().find(f".//{H}form[@class='search']")
            for query in ("", "?m=1", "?m=0"):
                self.assertEqual(urlparse(urljoin("https://example.com/" + query, form.get("action"))).path, "/search")

    def test_pages_and_custom_widgets_available_on_mobile(self):
        for path in (ROOT / "theme").glob("*.xml"):
            root = ET.parse(path).getroot()
            navigation = root.find(f".//{B}section[@id='navigation']")
            self.assertEqual(navigation.find(f"{B}widget[@id='PageList1']").get("type"), "PageList")
            for widget in root.iter(f"{B}widget"):
                self.assertEqual(widget.get("mobile"), "yes", widget.get("id"))


if __name__ == "__main__":
    unittest.main()
