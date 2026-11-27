"""Check both script serializations: XML text and Blogger's preserved CDATA."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NODE = shutil.which("node")


class HomeRenderingTests(unittest.TestCase):
    def test_template_gates_continuation_on_native_pagination(self):
        b = "{http://www.google.com/2005/gml/b}"
        h = "{http://www.w3.org/1999/xhtml}"
        expr = "{http://www.google.com/2005/gml/expr}"
        for path in sorted((ROOT / "theme").glob("*.xml")):
            with self.subTest(locale=path.name):
                root = ET.parse(path).getroot()
                widget = root.find(f".//{b}widget[@id='Blog1']")
                main = widget.find(f"{b}includable[@id='main']")
                target = main.find(f".//{b}with[@var='homePostTarget']")
                limit = target.find(f"{b}with[@var='homePageLimit']")
                postlist = limit.find(f"{h}div[@id='postlist']")
                self.assertEqual(postlist.get(expr + "data-home-posts"), "data:homePostTarget")
                self.assertEqual(postlist.get(expr + "data-page-limit"), "data:homePageLimit")
                self.assertIsNotNone(limit.find(f"{b}include[@name='pagination']"))
                guard = limit.find(f"{b}if")
                self.assertIsNotNone(guard.find(f"{b}include[@name='homeContinuation']"))
                self.assertEqual(guard.get("cond").split(" and "), [
                    "data:blog.url == data:blog.homepageUrl",
                    "data:olderPageUrl",
                    "not data:posts.empty",
                    "data:posts.size < data:homePostTarget",
                    "data:homePageLimit > 0",
                ])

    def test_preview_loads_script_only_for_short_eligible_home(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        try:
            import build_preview
        finally:
            sys.path.pop(0)
        with TemporaryDirectory() as directory, patch.object(build_preview, "OUT", Path(directory)):
            build_preview.build()
            for name, has_script in [
                ("index", False), ("short-disabled", False), ("resources-empty", False),
                ("older-1", False), ("short-home", True), ("short-budget", True),
            ]:
                with self.subTest(preview=name):
                    html = (Path(directory) / f"{name}.html").read_text(encoding="utf-8")
                    self.assertEqual("id='home-continuation'" in html, has_script)


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
for (const {budget, count, readyState, useIdle} of [
  {budget: '4', count: 2, readyState: 'loading', useIdle: true},
  {budget: '4', count: 2, readyState: 'complete', useIdle: false},
  {budget: '0', count: 2, readyState: 'loading', useIdle: true},
  {budget: '4', count: 10, readyState: 'loading', useIdle: true},
]) {
  const calls = [], timers = [], tasks = [], events = [];
  const older = {getAttribute: () => '/search?start=2'};
  const cards = Array.from({length: count}, (_, index) => ({
    querySelector: () => ({getAttribute: () => '/post-' + index + '.html?m=1'})
  }));
  const blog = {querySelector: () => older, querySelectorAll: () => cards};
  const list = {dataset: {homePosts: '10', pageLimit: budget}, closest: () => blog,
    setAttribute() {}, removeAttribute() {}};
  const fetch = (url, options) => { calls.push({url, options}); return new Promise(() => {}); };
  const window = {fetch, AbortController};
  if (useIdle) window.requestIdleCallback = (run, options) => tasks.push({run, timeout: options.timeout});
  const document = {readyState, getElementById: () => list,
    addEventListener: (name, run, options) => events.push({name, run, once: options.once})};
  vm.runInNewContext(source, {window, fetch, AbortController, URL, document,
    location: {origin: 'https://example.com', href: 'https://example.com/'},
    setTimeout: (run, delay) => {timers.push({run, delay}); return timers.length;}, clearTimeout() {}});
  assert.equal(calls.length, 0);
  if (budget === '0' || count === 10) {
    assert.equal(events.length + tasks.length + timers.length, 0);
    continue;
  }
  if (readyState === 'loading') {
    assert.equal(events.length, 1);
    assert.equal(events[0].name, 'DOMContentLoaded');
    assert.equal(events[0].once, true);
    assert.equal(tasks.length, 0);
    events[0].run();
  }
  assert.equal(calls.length, 0);
  if (useIdle) {
    assert.equal(tasks.length, 1);
    assert.equal(tasks[0].timeout, 1000);
    tasks.shift().run();
  } else {
    assert.equal(timers.length, 1);
    assert.equal(timers[0].delay, 0);
    timers.shift().run();
  }
  assert.equal(calls.length, 1);
  assert.equal(calls[0].options.credentials, 'omit');
  assert.equal(calls[0].options.redirect, 'error');
  assert.equal(calls[0].options.priority, 'low');
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
