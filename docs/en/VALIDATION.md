# Local validation — October 11, 2026

[English](VALIDATION.md) · [Português](../VALIDATION.md)

## Recorded checks

- XML and local widget structure pass the Python validator.
- Four validator regression tests pass locally.
- Preview home and article were measured through browser DOM at 360, 768 and 1440 px without horizontal page overflow in the initial base. Home was checked again after cards and typography changed.
- Code and table overflow is contained; entries without images use their available width.
- Home-to-article navigation was exercised in the preview.
- The current fixture has three opening cards and one list entry, with no duplicate posts.

An article overflow issue was fixed by allowing grid items to shrink (`min-width: 0`) and constraining the reading column. Font-family CSS selects Inter; download confirmation was interrupted by browser synchronization/timeouts. Fallback fonts remain configured.

## Limits

The preview uses actual CSS with sample markup; it does not compile Blogger expressions or widgets. Import, live data, comments and pagination remain unverified in Blogger. Screenshot capture was unavailable; recorded checks use DOM structure and dimensions, not screenshot review.

The initial theme PR passed GitHub CI before merge. The SEO implementation at `15ad07e` also passed [GitHub CI](https://github.com/erickfaria/balaio-theme/actions/runs/38142451054). Passing static checks does not imply Blogger compatibility. Use the checklist in [ROADMAP.md](ROADMAP.md).

## Responsive and bilingual review

- Home and article measured through DOM at 320, 360, 480, 600, 768, 900, 1050 and 1440 px: no horizontal document overflow.
- Long unbroken titles, URLs, wide table content and code checked in a stress fixture at 320, 360, 768 and 1440 px, also without page overflow.
- Added wrapping for long titles and minimum-width constraints in the header.
- Both XML variants validate. Two additional tests ensure matching CSS and widget identities; six tests pass overall.
- Local bilingual documentation links are checked automatically. Heading anchors and external URLs are outside that check.
- Remote font faces were not reported as loaded during this review, so dimensions were checked with fallback typography. Final-font visual review remains pending.

## SEO branch validation

Twelve local tests cover XML, locales, metadata ownership and rendered HTML auditing. This branch adds partial article/page microdata and listing headings; live Blogger import and rich-results validation remain pending. The [SEO guide](SEO.md) records a read-only domain baseline, separate from template verification.

## Live baseline — 2026-10-11

Read-only observations at `https://www.balaiocientifico.com/` **before installing this branch's theme**:

- Home and `/2025/04/analise-de-dados-do-cnes-no-jamovi.html` return HTTP 200 and self-referencing HTTPS canonicals.
- The inspected article has the blog name as H1 rather than the article title. The new theme assigns the article title to H1.
- Both inspected pages lack a standard meta description; the home sharing description is empty. Configure Blogger search descriptions and recheck the output.
- `/robots.txt` allows general crawling of public articles and excludes `/search` and `/share-widget`; it advertises `/sitemap.xml`.
- The sitemap responds successfully with a populated XML URL set. Its `X-Robots-Tag: noindex` applies to the sitemap response and does not establish that articles are excluded.

These observations do not establish actual search indexing, AI citations or performance. No published settings or content were changed during this audit.

## Multi-engine and post layout review

Thirteen local tests pass, including a scoped DuckDuckBot restriction case. The new `media.html` fixture uses the editable Portuguese post example plus a figure and empty 16:9 video iframe. DOM measurements at 320, 360, 768 and 1440 px showed no horizontal document overflow; figure and iframe widths stayed within the reading column. This verifies container layout, not playback or a Blogger import.
