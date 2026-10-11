"""Check both script serializations: XML text and Blogger's preserved CDATA."""
from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
import subprocess
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NODE = shutil.which("node")


class ScriptHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.script = ""

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            self.active = True

    def handle_data(self, text):
        if self.active:
            self.script += text

    def handle_endtag(self, tag):
        if tag == "script":
            self.active = False


@unittest.skipUnless(NODE, "Install Node.js to check JavaScript syntax (required in CI).")
class HomeScriptTests(unittest.TestCase):
    def scripts(self):
        for path in sorted((ROOT / "theme").glob("*.xml")):
            xml = path.read_text(encoding="utf-8")
            block = re.search(r"<b:includable id='homeContinuation'>\s*(<script\b.*?</script>)", xml, re.S).group(1)
            parser = ScriptHTML()
            parser.feed(block)
            yield path.name, xml, parser.script

    def syntax(self, source):
        return subprocess.run([NODE, "--check"], input=source, text=True, capture_output=True)

    def test_blogger_preserved_cdata_executes(self):
        for name, _, source in self.scripts():
            with self.subTest(locale=name):
                result = self.syntax(source)
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_xml_parser_stripped_cdata_executes(self):
        for name, xml, _ in self.scripts():
            with self.subTest(locale=name):
                script = ET.fromstring(xml).find(
                    ".//{http://www.google.com/2005/gml/b}includable[@id='homeContinuation']/{http://www.w3.org/1999/xhtml}script"
                ).text
                result = self.syntax(script)
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_reproduces_published_rc2_failure(self):
        for name, _, source in self.scripts():
            with self.subTest(locale=name):
                broken = source.replace("//<![CDATA[", "<![CDATA[").replace("//]]>", "]]>")
                result = self.syntax(broken)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Unexpected token '<'", result.stderr)


if __name__ == "__main__":
    unittest.main()
