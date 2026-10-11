# Release validation — 2026-10-11

[English](VALIDATION.md) · [Português](../VALIDATION.md)

## Blogger import confirmed

On October 11, 2026, the project owner reported successful import and explicitly approved promotion to stable `v0.1.0`. This is maintainer-reported platform evidence. The language variant and complete widget test results were not recorded, so it is not a claim that both variants or every behavior were independently tested. The XML templates are unchanged from the imported alpha.

## Automated checks

Thirteen regression tests cover malformed widget sections, duplicate IDs, missing includes, locale equivalence, metadata ownership and HTML SEO auditing. Both XML variants parse; locale generation is current; local Markdown links and Git whitespace checks pass. GitHub CI repeats these checks and builds the preview. External documentation links and heading anchors are not checked automatically.

## Responsive preview evidence

- Home and article DOM measured at 320, 360, 480, 600, 768, 900, 1050 and 1440 px without horizontal page overflow.
- Long unbroken titles, URLs, tables and code checked at 320, 360, 768 and 1440 px; scrolling remains contained.
- Editable post example, figure and empty 16:9 iframe checked at 320, 360, 768 and 1440 px. Media stays within the reading column.
- Privacy page checked at 320, 768 and 1440 px: one H1, WebPage microdata, current menu link highlighted and working navigation to Contact.
- The home fixture contains three opening cards plus one distinct list entry.

## Limits and next checks

These are CSS/DOM fixture checks, not a Blogger compiler. Import is confirmed by the owner. Full testing of native data, gadgets, comments, pagination and published structured data remains pending. Screenshot capture was unavailable, and remote font faces were not confirmed loaded; measurements reflect fallback typography. No Core Web Vitals or ranking claims are established.

The owner authorized stable status after import confirmation; the remaining [platform checklist](ROADMAP.md) documents follow-up testing. Use [SEO.md](SEO.md) for published HTML auditing and [RELEASE.md](RELEASE.md) for package contents and installation.

## Development branch: native customization

The color/font controls are new source changes and are not covered by the stable-release import report above. Eighteen local tests now pass, including variable resolution, locale parity and a 4.5:1 default text contrast check. The preview uses resolved saved values; it cannot verify that Blogger displays or saves Designer controls. Import and save a customized theme in a test blog before releasing these changes.

The updated default preview was measured at 320, 360, 768 and 1440px for home, article, privacy, long-content and media fixtures, with no page-wide horizontal overflow. Article and page body text resolves to 20px at all four widths.

A temporary customization fixture with 24px serif reading text and a pastel sand page background also stayed within the viewport at 320, 768 and 1440px for articles and privacy pages. These generated fixtures are excluded from Git.

## Mobile spacing refinement

DOM measurements of the updated home fixture at 320, 360, 480, 768, 800, 801 and 1440px show no page-wide horizontal overflow. All 24 sample topics remain linked; mobile links are at least 44px tall, and only the outer sidebar has a divider. At 360px, the same fixture changed from a 290px to a 258px header and an 885px to a 642px topic list. Article, privacy and long-content fixtures also remain within the viewport at 320, 360, 768 and 1440px, with 20px reading text. These are local fixture measurements; the updated XML still needs live Blogger verification.

## Published blog audit before integration

On October 11, 2026, browser inspection of `www.balaiocientifico.com` found two posts on the home page and two more through the older-posts link, an empty top navigation, the previous CSS, and a search action incorrectly containing `?m=1search`. Inter and Newsreader CSS requests were present; computed families matched and the browser font loader reported completion. Their upstream OFL licenses and local notices were checked. The current source fixes the search route, adds top Pages navigation and enables custom widgets on mobile. Twenty local tests pass. The nine-post home preview demonstrates three cards plus six unique list entries; it does not control Blogger pagination. These new widget changes still need a fresh Blogger import.

## Larger reading typography

A public article inspected at 360px still used the earlier 18px mobile body size. The current source raises the default reading size from 20px to 22px at every width, with a 1.75 line height. Historical measurements above refer to earlier source revisions. Font families and licenses remain unchanged.

Article, privacy and long-content previews were measured at 320, 360, 768 and 1440px: 22px reading text, 38.5px line height and no page-wide horizontal overflow. Section headings use explicit relative sizes to avoid native widget CSS shrinking H2 text below the reading size.
