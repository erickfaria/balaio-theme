#!/usr/bin/env python3
"""Inspect rendered HTML, never an uncompiled Blogger XML template.

Warnings are observations, not an SEO score or proof of indexability.
Uses only Python's standard library. Network access is opt-in via --url.
"""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import parse_qsl, urlencode, urlsplit
from urllib.request import Request, urlopen


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_head = False
        self.element_ids = set()
        self.capture = None
        self.titles = []
        self.headings = []
        self.canonicals = []
        self.descriptions = []
        self.robots = []
        self.lang = ''
        self.images_missing_alt = 0
        self.schemas = []
        self.json_ld = []

    def handle_starttag(self, tag, attrs):
        attrs = {key: value or '' for key, value in attrs}
        if attrs.get('id'):
            self.element_ids.add(attrs['id'])
        if tag == 'html':
            self.lang = attrs.get('lang', '')
        if tag == 'head':
            self.in_head = True
        if (tag == 'title' and self.in_head) or tag == 'h1':
            self.capture = (tag, [])
        if tag == 'script' and attrs.get('type', '').lower() == 'application/ld+json':
            self.capture = ('script', [])
        if self.in_head and tag == 'link' and 'canonical' in attrs.get('rel', '').lower().split():
            self.canonicals.append(attrs.get('href', ''))
        if self.in_head and tag == 'meta':
            name = attrs.get('name', '').lower()
            if name == 'description':
                self.descriptions.append(attrs.get('content', ''))
            if name in ('robots', 'googlebot', 'bingbot', 'duckduckbot', 'oai-searchbot'):
                self.robots.append({'agent': name, 'content': attrs.get('content', '')})
        if tag == 'img' and 'alt' not in attrs:
            self.images_missing_alt += 1
        if 'itemscope' in attrs and attrs.get('itemtype'):
            self.schemas.append(attrs['itemtype'])

    def handle_data(self, data):
        if self.capture:
            self.capture[1].append(data)

    def handle_endtag(self, tag):
        if self.capture and self.capture[0] == tag:
            value = ''.join(self.capture[1]).strip()
            {'title': self.titles, 'h1': self.headings, 'script': self.json_ld}[tag].append(value)
            self.capture = None
        if tag == 'head':
            self.in_head = False


def audit(html, x_robots=()):
    page = Page()
    page.feed(html)
    errors, warnings = [], []
    # Blogger can register a gadget whose server-rendered element is missing.
    # Detect this real failure independently of source XML and handmade previews.
    registered_core = set(re.findall(
        r"_RegisterWidget\(['\"]_(?:Header|Blog)View['\"],\s*new\s+_WidgetInfo\(['\"]([^'\"]+)", html))
    missing_core = sorted(registered_core - page.element_ids)
    if missing_core:
        errors.append('Registered core Blogger widgets missing from rendered HTML: ' + ', '.join(missing_core))
    if len(page.titles) != 1 or not page.titles[0]:
        errors.append('Expected one nonempty document title.')
    if len(page.canonicals) != 1:
        errors.append('Expected one canonical URL.')
    elif urlsplit(page.canonicals[0]).scheme not in ('https', 'http') or not urlsplit(page.canonicals[0]).netloc:
        errors.append('Canonical URL must be absolute HTTP(S).')
    if len(page.descriptions) > 1:
        errors.append('Duplicate meta descriptions.')
    if not page.descriptions or not page.descriptions[0].strip():
        warnings.append('Missing or empty meta description; configure Blogger search descriptions.')
    if len(page.headings) != 1 or not page.headings[0]:
        warnings.append('Expected one meaningful H1; review the introduction and post headings.')
    if not page.lang.strip():
        warnings.append('Missing document language.')
    if page.images_missing_alt:
        warnings.append(f'{page.images_missing_alt} images lack an alt attribute; decorative alt="" is valid.')
    for raw in page.json_ld:
        try:
            json.loads(raw)
        except ValueError:
            errors.append('Invalid JSON-LD syntax.')
    controls = page.robots + [{'agent': 'HTTP X-Robots-Tag', 'content': value} for value in x_robots]
    for control in controls:
        if re.search(r'\b(noindex|none|nosnippet)\b|max-snippet\s*:\s*0\b', control['content'], re.I):
            warnings.append(f"Review search restriction ({control['agent']}): {control['content']}")
    return {'title': page.titles, 'canonical': page.canonicals, 'description': page.descriptions,
            'h1': page.headings, 'language': page.lang, 'microdata_types': page.schemas,
            'json_ld_blocks': len(page.json_ld), 'missing_core_widgets': missing_core, 'robots': controls, 'errors': errors, 'warnings': warnings}


def audit_url(url):
    request = Request(url, headers={'User-Agent': 'BalaioSEOAudit/1.0'})
    with urlopen(request, timeout=30) as response:
        if 'text/html' not in response.headers.get('Content-Type', '').lower():
            raise ValueError('Expected rendered HTML, not a sitemap or robots.txt.')
        raw = response.read(5_000_001)
        if len(raw) > 5_000_000:
            raise ValueError('HTML exceeds the 5 MB audit limit.')
        report = audit(raw.decode(response.headers.get_content_charset() or 'utf-8'),
                       response.headers.get_all('X-Robots-Tag', []))
        report.update(source=response.url, status=response.status)
        return report


def with_mobile_mode(url, mode):
    parts = urlsplit(url)
    params = [(key, value) for key, value in parse_qsl(parts.query, keep_blank_values=True) if key != 'm']
    params.append(('m', mode))
    return parts._replace(query=urlencode(params), fragment='').geturl()


def compare_mobile(desktop, mobile):
    errors = []
    if not desktop['errors'] and not mobile['errors']:
        desktop_canonical = desktop['canonical'][0]
        if desktop_canonical != mobile['canonical'][0]:
            errors.append('Desktop and mobile canonical URLs differ.')
        if any(key == 'm' for key, _ in parse_qsl(urlsplit(desktop_canonical).query, keep_blank_values=True)):
            errors.append('The desktop canonical URL includes a Blogger mobile mode parameter.')
        if desktop['title'] != mobile['title']:
            errors.append('Desktop and mobile document titles differ.')
        if desktop['description'] != mobile['description']:
            errors.append('Desktop and mobile meta descriptions differ.')
    return {'desktop': desktop, 'mobile': mobile, 'comparison_errors': errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--file', type=Path)
    source.add_argument('--url')
    parser.add_argument('--compare-mobile', action='store_true',
                        help='With --url, compare the Blogger m=0 and m=1 versions.')
    args = parser.parse_args()
    if args.compare_mobile and not args.url:
        parser.error('--compare-mobile requires --url.')
    if args.url and urlsplit(args.url).scheme not in ('http', 'https'):
        parser.error('--url must use HTTP(S).')
    try:
        if args.compare_mobile:
            desktop = audit_url(with_mobile_mode(args.url, '0'))
            mobile = audit_url(with_mobile_mode(args.url, '1'))
            report = compare_mobile(desktop, mobile)
            errors = desktop['errors'] or mobile['errors'] or report['comparison_errors']
        else:
            if args.file:
                report = audit(args.file.read_text(encoding='utf-8'))
                report['source'] = str(args.file)
            else:
                report = audit_url(args.url)
            errors = report['errors']
    except (OSError, ValueError) as error:
        parser.exit(1, f'ERROR: {error}\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
