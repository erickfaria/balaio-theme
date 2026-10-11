import importlib.util
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('audit_seo', ROOT / 'scripts/audit_seo.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

HTML = '''<html lang="pt-BR"><head><title>A &amp; B</title>
<link rel="canonical" href="https://example.com/post">
<meta name="description" content="An example."></head><body>
<h1>A <em>useful</em> post</h1><img alt=""><article itemscope itemtype="https://schema.org/BlogPosting"></article></body></html>'''


class RenderedSEOTests(unittest.TestCase):
    def test_good_document_and_decorative_image(self):
        report = module.audit(HTML)
        self.assertEqual(report['errors'], [])
        self.assertEqual(report['warnings'], [])
        self.assertEqual(report['h1'], ['A useful post'])
        self.assertEqual(report['title'], ['A & B'])

    def test_duplicate_canonical_is_an_error(self):
        self.assertTrue(module.audit(HTML.replace('</head>', '<link rel="canonical" href="https://example.com/other"></head>'))['errors'])

    def test_empty_description_is_warning(self):
        report = module.audit(HTML.replace('content="An example."', 'content=" "'))
        self.assertEqual(report['errors'], [])
        self.assertTrue(any('description' in warning for warning in report['warnings']))

    def test_robot_scope_is_preserved_and_not_reported_as_global_block(self):
        report = module.audit(HTML, ['googlebot: noindex', 'bingbot: nosnippet'])
        self.assertEqual(len(report['warnings']), 2)
        self.assertIn('googlebot: noindex', report['warnings'][0])
        self.assertEqual(module.audit(HTML, ['index, follow'])['warnings'], [])

    def test_invalid_json_and_missing_alt(self):
        report = module.audit(HTML.replace('<img alt="">', '<img><script type="application/ld+json">{"bad":}</script>'))
        self.assertTrue(any('JSON-LD' in error for error in report['errors']))
        self.assertTrue(any('alt' in warning for warning in report['warnings']))


class TemplateSEOTests(unittest.TestCase):
    def test_native_metadata_and_visible_article_schema(self):
        b = '{http://www.google.com/2005/gml/b}'
        expr = '{http://www.google.com/2005/gml/expr}'
        for path in (ROOT / 'theme').glob('*.xml'):
            root = ET.parse(path).getroot()
            # Strip XHTML only; retain Blogger expression/data namespaces.
            for node in root.iter():
                node.tag = node.tag.removeprefix('{http://www.w3.org/1999/xhtml}')
            head = root.find('head')
            self.assertEqual(len(head.findall('title')), 1)
            self.assertEqual(len([node for node in head.findall(b + 'include') if node.get('name') == 'all-head-content']), 1)
            self.assertFalse([node for node in head.findall('link') if node.get('rel') == 'canonical'])
            self.assertFalse([node for node in head.findall('meta') if node.get('name') in ('description', 'robots', 'googlebot')])
            article = root.find('.//' + b + "includable[@id='article']/article")
            self.assertIn('BlogPosting', article.get(expr + 'itemtype'))
            self.assertIn('WebPage', article.get(expr + 'itemtype'))
            body = article.find("div[@class='post-body']")
            self.assertIn('articleBody', body.get(expr + 'itemprop'))
            self.assertIsNotNone(body.find('{http://www.google.com/2005/gml/data}post.body'))


if __name__ == '__main__':
    unittest.main()
