"""Check both script serializations: XML text and Blogger's preserved CDATA."""
from html.parser import HTMLParser
import json
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


@unittest.skipUnless(NODE, "Install Node.js to check JavaScript syntax and scheduling (required in CI).")
class HomeScriptTests(unittest.TestCase):
    def scripts(self):
        for path in sorted((ROOT / "theme").glob("*.xml")):
            xml = path.read_text(encoding="utf-8")
            block = re.search(r"(<script id='home-continuation'\s.*?</script>)", xml, re.S).group(1)
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
                    ".//{http://www.w3.org/1999/xhtml}script[@id='home-continuation']"
                ).text
                result = self.syntax(script)
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_two_post_home_starts_native_continuation(self):
        harness = r"""
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = JSON.parse(require('node:fs').readFileSync(0, 'utf8'));
for (const budget of ['4', '0']) {
  const calls = [], timers = [];
  const older = {getAttribute: () => '/search?start=2'};
  const cards = ['first', 'second'].map(slug => ({querySelector: () => ({getAttribute: () => '/' + slug + '.html?m=1'})}));
  const blog = {querySelector: () => older, querySelectorAll: () => cards};
  const list = {dataset: {homePosts: '10', pageLimit: budget}, closest: () => blog,
    setAttribute() {}, removeAttribute() {}};
  const fetch = (url, options) => { calls.push({url, options}); return new Promise(() => {}); };
  vm.runInNewContext(source, {window: {fetch, AbortController}, fetch, AbortController, URL,
    document: {getElementById: () => list},
    location: {origin: 'https://example.com', href: 'https://example.com/'},
    setTimeout: (run, delay) => {timers.push({run, delay}); return timers.length;}, clearTimeout() {}});
  assert.equal(calls.length, budget === '0' ? 0 : 1);
  if (budget === '0') continue;
  assert.equal(calls[0].options.credentials, 'omit');
  assert.equal(calls[0].options.redirect, 'error');
  assert.equal(new URL(calls[0].url).searchParams.get('m'), '0');
  assert.equal(new URL(calls[0].url).searchParams.get('max-results'), '8');
  assert.equal(timers[0].delay, 8000);
}
"""
        for name, _, source in self.scripts():
            with self.subTest(locale=name):
                result = subprocess.run([NODE, '-e', harness], input=json.dumps(source), text=True, capture_output=True)
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
