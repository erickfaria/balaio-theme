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

    def test_continuation_waits_for_load_and_yields_before_fetch(self):
        # Execute the real script; isolate lifecycle events without mocking a browser engine.
        harness = r"""
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = JSON.parse(require('node:fs').readFileSync(0, 'utf8'));
for (const [state, idle] of [['loading', true], ['complete', true], ['loading', false]]) {
  const calls = [], events = [], tasks = [];
  const older = {getAttribute: () => '/search?start=2'};
  const card = {querySelector: () => ({getAttribute: () => '/first.html?m=1'})};
  const blog = {querySelector: () => older, querySelectorAll: () => [card]};
  const list = {dataset: {homePosts: '10', pageLimit: '4'}, closest: () => blog,
    setAttribute() {}, removeAttribute() {}};
  const fetch = (url, options) => { calls.push({url, options}); return new Promise(() => {}); };
  const window = {fetch, AbortController,
    addEventListener: (type, run, options) => events.push({type, run, options})};
  if (idle) window.requestIdleCallback = (run, options) => tasks.push({run, options});
  vm.runInNewContext(source, {window, fetch, AbortController, URL,
    document: {readyState: state, getElementById: () => list},
    location: {origin: 'https://example.com', href: 'https://example.com/'},
    setTimeout: (run, delay) => { tasks.push({run, delay}); return tasks.length; }, clearTimeout() {}});
  assert.equal(calls.length, 0, 'initial parsing must not start continuation');
  if (state === 'loading') {
    assert.equal(tasks.length, 0);
    assert.equal(events[0].type, 'load');
    assert.equal(events[0].options.once, true);
    events[0].run();
  } else assert.equal(events.length, 0, 'late script must not wait for an event already fired');
  assert.equal(calls.length, 0, 'load handler must yield before starting requests');
  assert.equal(tasks.length, 1);
  if (idle) assert.equal(tasks[0].options.timeout, 1000);
  else assert.equal(tasks[0].delay, 0);
  tasks[0].run();
  assert.equal(calls.length, 1);
  assert.equal(calls[0].options.priority, 'low');
  assert.equal(calls[0].options.credentials, 'omit');
  assert.equal(new URL(calls[0].url).searchParams.get('m'), '0');
  assert.equal(new URL(calls[0].url).searchParams.get('max-results'), '9');
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
