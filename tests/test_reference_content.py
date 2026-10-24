"""Guard native widget identities, optional author data and guide navigation."""
from html.parser import HTMLParser
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
B = "{http://www.google.com/2005/gml/b}"
H = "{http://www.w3.org/1999/xhtml}"
E = "{http://www.google.com/2005/gml/expr}"


class GuideHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.targets, self.headings = [], [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "a" and attrs.get("href", "").startswith("#"):
            self.targets.append(attrs["href"][1:])
        if tag in ("h1", "b:section", "b:widget", "script"):
            self.headings.append(tag)


class ReferenceContentTests(unittest.TestCase):
    def themes(self):
        for path in sorted((ROOT / "theme").glob("*.xml")):
            root = ET.parse(path).getroot()
            yield path.name, root, {child: parent for parent in root.iter() for child in parent}

    def conditions(self, node, parents):
        result = []
        while node in parents:
            node = parents[node]
            if node.tag == B + "if":
                result.append(node.get("cond"))
        return result

    def test_topics_reuse_native_label_widget_outside_legacy_sidebar(self):
        for name, root, _ in self.themes():
            with self.subTest(theme=name):
                topics = root.find(".//" + B + "section[@id='topics']")
                labels = topics.find(B + "widget[@id='Label1']")
                self.assertEqual(labels.get("type"), "Label")
                self.assertIsNotNone(labels.find(".//" + H + "details/" + H + "summary"))
                self.assertIsNone(root.find(".//" + B + "section[@id='sidebar']/" + B + "widget[@id='Label1']"))
                self.assertIsNotNone(root.find(".//" + B + "section[@id='sidebar']"))

    def test_curated_links_are_optional_native_home_content(self):
        for name, root, parents in self.themes():
            with self.subTest(theme=name):
                widget = root.find(".//" + B + "widget[@id='LinkList2']")
                self.assertEqual(widget.get("type"), "LinkList")
                self.assertIn("data:blog.url == data:blog.homepageUrl", self.conditions(widget, parents))
                nav = widget.find(".//" + H + "nav")
                self.assertIn("data:links", self.conditions(nav, parents))
                self.assertIsNone(widget.find(B + "widget-settings"))
                self.assertIsNone(widget.find(".//" + H + "script"))

    def test_author_photo_is_conditional_and_preserves_text_name(self):
        for name, root, parents in self.themes():
            with self.subTest(theme=name):
                metadata = root.find(".//" + B + "widget[@id='Blog1']/" + B + "includable[@id='metadata']")
                photo = metadata.find(".//" + H + "img")
                self.assertIn('data:blog.pageType == "item"', self.conditions(photo, parents))
                self.assertIn("data:post.authorPhoto.url", self.conditions(photo, parents))
                self.assertEqual((photo.get("width"), photo.get("height"), photo.get("alt")), ("32", "32", ""))
                profile = metadata.find(".//" + H + "a[@rel='author']")
                self.assertIn("data:post.authorProfileUrl", self.conditions(profile, parents))
                self.assertEqual(profile.get(E + "href"), "data:post.authorProfileUrl")
                person = metadata.find(".//" + H + "span[@itemprop='author']")
                self.assertEqual(person.get("itemtype"), "https://schema.org/Person")
                self.assertIsNotNone(person.find(".//" + B + "else"))
                self.assertEqual(len(root.findall(".//" + H + "script")), 2)

    def test_guide_examples_have_working_fragment_links_without_extra_h1(self):
        for path in (ROOT / "examples/pages").glob("guide.*.html"):
            with self.subTest(example=path.name):
                parser = GuideHTML()
                parser.feed(path.read_text())
                self.assertEqual(parser.headings, [])
                self.assertEqual(len(parser.ids), len(set(parser.ids)))
                self.assertTrue(parser.targets)
                self.assertLessEqual(set(parser.targets), set(parser.ids))


if __name__ == "__main__":
    unittest.main()
