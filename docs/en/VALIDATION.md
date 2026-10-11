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
