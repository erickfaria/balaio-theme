"""Run the actual automatic-navigation script with both Blogger serializations."""
import json
from pathlib import Path
import re
import subprocess
import unittest
import xml.etree.ElementTree as ET
from test_home_script import NODE, ScriptHTML

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(NODE, "Node.js is required for automatic-navigation checks in CI.")
class PageNavigationTests(unittest.TestCase):
    def scripts(self):
        for path in sorted((ROOT / "theme").glob("*.xml")):
            xml = path.read_text(encoding="utf-8")
            block = re.search(r"(<script id='page-navigation'\s.*?</script>)", xml, re.S).group(1)
            parser = ScriptHTML()
            parser.feed(block)
            parsed = ET.fromstring(xml).find(".//{http://www.w3.org/1999/xhtml}script[@id='page-navigation']").text
            yield path.name, parser.script, parsed

    def test_both_script_serializations(self):
        for name, raw, parsed in self.scripts():
            for mode, script in [("raw", raw), ("parsed", parsed)]:
                with self.subTest(locale=name, mode=mode):
                    result = subprocess.run([NODE, "--check"], input=script, text=True, capture_output=True)
                    self.assertEqual(result.returncode, 0, result.stderr)

    def test_runtime_scenarios(self):
        for name, raw, _ in self.scripts():
            with self.subTest(locale=name):
                result = subprocess.run([NODE, str(ROOT / "tests/page_navigation_runtime.cjs")],
                                        input=json.dumps(raw), text=True, capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr)
