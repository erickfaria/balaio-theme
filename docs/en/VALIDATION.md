# Validation — v0.2.0-rc.16

[English](VALIDATION.md) · [Português](../VALIDATION.md)

## rc.16 — Optional native Analytics — 2026-10-27

Both XMLs include a single global `google-analytics` call, conditional on `data:blog.analyticsAccountNumber`. The ID belongs to each blog's Settings; no identifier was added to the repository. CSS, custom scripts and widget bodies remain identical to rc.15, apart from the CSS version comment. [Setup](ANALYTICS.md).

Local verification does not execute the platform include. The service was not enabled, blog settings were not changed and no events were sent to a real property. The owner must verify import and collection after configuring the ID; the local preview does not load Analytics.

## rc.15 — Uniform header and curation — October 24, 2026

Topics and menu links share font, size, weight, line height, target height and vertical spacing. There is no separate pill, border, highlighted background, triangle or counter. Widgets, scripts and the existing automatic mode are preserved. [Layout setup](LAYOUT.md) covers five to seven topics, a few main links and up to three highlights, without imposed names or silent cutoffs.

36 local tests pass, alongside XML, locales, links, packaging and preview. CSS adds 634 bytes (95 isolated gzip bytes) against rc.14; scripts remain identical. Connected documentation-preview links were checked. No review browser was available; rc.15 visual verification remains pending.

The owner reported installing rc.14, and a public HTTP check confirmed its version marker and Topics control. This does not confirm rc.15 installation or all profile fields.

## rc.14 — Web library and navigation — October 24, 2026

Main includes optional curated links, native header topics, a conditional author photo and web models for libraries, handbooks and chapters. **36 local tests passed**, including install-package completeness. Locales, XML, documentation links and preview pass; Actions repeats checks before merge and on main/tags.

Both scripts remain identical to rc.13. CSS: 14,724 → 17,566 bytes; isolated gzip: 3,704 → 4,184 bytes. No new fonts, services or print features. The install ZIP includes the Markdown models referenced by the guides. These are file measurements, not published speed results.

Fresh Blogger import, profile-photo field availability and visual device review remain pending. rc.14 is a prerelease; local checks do not establish platform validation.

## Earlier status — rc.13

rc.13 includes the native form in its own section outside the hidden sidebar. A class in static-page content enables presentation through CSS, regardless of title/URL. It adds no URL detection, new JavaScript or automatic page creation. Fresh import and delivery still need confirmation on Blogger.

rc.6 recovers the widget definitions and home continuation script from rc.3, confirmed by the owner and observed with ten posts live on October 11, 2026. It retains the sidebar-free layout, compact footer, open variable fonts, mobile navigation and 22px reading text. The owner confirmed rc.6 import and sidebar removal on October 12, 2026. It is the validated baseline for rc.7.

Actions runs for PRs, main, tags and manual dispatch. Historical records below retain the original verification conditions.

## Content opt-in contact — rc.13, October 17, 2026

The owner’s exported copy contained ContactForm1 in the hidden sidebar with an old URL condition. rc.13 declares the complete gadget in contactpage, outside sidebar, limited to static pages. The HTML sample adds balaio-contact-page; no template-line editing or fixed address is needed. Existing widgets and both scripts are preserved. Previews disable sending and do not load Google transport. 31 local tests pass, alongside documentation links, generated locales, XML and whitespace checks. The six previous widgets and home-continuation/page-navigation scripts were compared against the previous main without differences.

Both language previews were checked at 320, 360, 768 and 1440px: one H1, 16px fields, controls above 44px, alignment with the reading column, a 24px text-to-form gap and no horizontal overflow. Three different URLs (two with numeric suffixes) displayed the form; About, Privacy and the page without the class kept it hidden. The script-free notice appeared in an isolated frame. Invalid email was recognized; fictitious values with a blank name passed HTML validity. Error/success feedback is illustrative only, without sending a message.

No Blogger content, settings or messages were submitted. Local checks do not run platform compilation/migration or confirm email delivery. Fresh import and inbox receipt remain pending.

## Manual contact and integration removal — rc.12, October 17, 2026

The owner reported that Blogger generated a page with a numeric suffix. rc.11’s condition accepted only two fixed paths and therefore did not cover that address. At the owner’s request the integration was removed instead of adding more detection rules.

Both XML files were compared with the rc.10 commit: after normalizing version metadata only, they are identical. Existing widgets, CSS, markup and scripts are preserved. Locale/preview builders also restore rc.10; the obsolete native-contract test and generated form fixtures were removed.

28 local tests pass, including bilingual docs, XML, locales and scripts. The Contact preview contains only reference text without send controls. Guides explain using actual generated URLs, including suffixes, separately configuring a form and removing the rc.11 gadget in Layout if Blogger retains it. XML does not modify published page text. [Reference and migration](CONTACT.md).

No Blogger content/settings were changed and no messages were sent. rc.12 restores previously imported rc.10 code; this is not a fresh Blogger compiler/import check.

## Native contact — rc.11, October 17, 2026

30 local tests pass, including regressions for the six IDs consumed by the native runtime, associated labels, optional name, required email/message, accessible feedback and page scope. The integration contract was checked by reading Blogger’s public widget resource; the library is not copied into the repository.

Public rc.10 pages confirmed the `canonicalUrl` and `canonicalHomepageUrl` fields. Mobile `homepageUrl` includes `?m=1` while both canonical URLs stay clean. The new widget compares canonical URLs, preserving mobile contact-page matching without a fixed domain.

Previews use each XML’s actual form, with Send disabled and no Google transport. At 320, 360, 768 and 1440px in both languages, fields stayed contained with one H1, three associated labels, 16px Inter fields and buttons above 44px. Client/scroll widths matched (305, 345, 753 and 1425px). Introduction-to-form spacing measured 24px with one visible back link. Local screenshots were inspected.

HTML validity rejected malformed email and empty required fields, and accepted fictitious values with an empty name. Error/success examples were checked as **illustrative states**, without claiming delivery. No message or user data was sent. Check layout, inbox delivery, mobile mode, native feedback language and form absence on other pages after importing. [Setup](CONTACT.md).

## Search opening to the left — rc.10, October 17, 2026

The preview uses the actual theme form and CSS. At 320, 360, 768 and 1440px, the open field sits to the left of the magnifier at the same vertical coordinate, with a 6px gap. There is one magnifier element. Opening/closing leaves header height unchanged without horizontal overflow; the home retains two highlights and eight older entries.

On phones the title is hidden while search uses the row, then restored on close without changing header dimensions. Enter opened and Space closed the native control. Tab reached the field; the arrow submitted `ciência dados` through GET, by desktop click and keyboard in a script-disabled frame. Local screenshots were inspected. The 160ms CSS transition is disabled by reduced-motion preference.

28 local tests pass. All widget bodies and both scripts were compared with rc.9 without differences. These preview checks do not establish fresh rc.10 Blogger import.

## Collapsible search and menu updates — rc.9, October 17, 2026

The public blog was observed running rc.8 with populated widgets. Native navigation contained only Home. The public feed now listed only Privacy and About; Members returned HTTP 404 after being returned to draft. A fresh page load displayed the correct three links. rc.8’s session list could retain the previous menu for one minute.

rc.9 removes that list: one low-priority summary-feed request with a six-second timeout and HTTP revalidation per page load. Runtime regressions execute the actual script in both languages and cover publication, title changes, returns to draft, empty feeds, network failure and no sessionStorage access. Manual links and widget definitions remain intact.

28 local tests pass. The preview uses the actual XML details/summary control and search form, and reproduces Blogger’s native margins. Search opened by pointer and Enter, submitted accented terms through GET and worked without JavaScript in a sandboxed frame. At 320, 360, 768 and 1440px, checks covered a 44px magnifier beside the title, a contained open field, two highlights and eight older entries, and no horizontal overflow. The gap between introduction description and Latest posts is 16px on phones and 20px on desktop, without the extra 30px native widget margin. Local screenshots were inspected.

These checks do not compile Blogger XML or confirm fresh rc.9 import. All widget bodies and the continuation script were compared with main rc.8 with no differences.

## Automated checks

28 local tests pass: XML/widget structure, locales, metadata/rendered HTML audit, Designer, contrast, mobile navigation/search, both CDATA serializations and continuation startup from a two-post home. A zero request budget makes no request; the default follows native pagination with the remaining count and an eight-second timeout. Without Node the six JavaScript checks are skipped locally; CI includes Node. Markdown links, English generation, XML, whitespace and preview generation pass.

## Automatic pages and alignment — rc.8, October 17, 2026

Public inspection found rc.7 with four sitemap pages but only Home in PageList1’s native data. All four URLs returned HTTP 200 with a heading and WebPage layout. The navbar section measured 30px while its link measured 44px and crossed the header border.

The public summary feed returned four pages and 6,659 bytes in the observed response, versus 17,308 bytes for the full feed; sizes vary with content. Navigation uses the summary endpoint, one request on an uncached load, a six-second timeout and a one-minute session cache of titles/URLs. No API key or fixed blog domain is required.

28 local tests pass, including both CDATA serializations in both languages and runtime cases for valid/expired cache, unavailable storage, manual mode, invalid/unavailable feeds, duplicates, external/unsafe URLs and the current page.

The preview reproduces native `.navbar{height:30px}` CSS. At 320/360/768/1440px, a local replay of public titles/paths showed five links (Home plus four pages), aligned with the brand and contained inside the header, without a green background or horizontal overflow. The section expanded to 94px at the two smaller widths and 44px at larger widths. All ten posts still loaded. A visual screenshot review confirmed desktop alignment.

Feed failures, invalid JSON and empty lists preserved Home; manual mode retained only configured links; an existing About link retained its custom name without duplication; malicious content became literal text rather than images/events. The Privacy page received `aria-current='page'`. These are local code/DOM checks plus a public feed read, not an rc.8 Blogger import.

## Local visual refinement — rc.7

26 checks pass. At 320, 360, 768 and 1440px the preview retains two highlights and eight distinct entries, correct pagination and no horizontal overflow. The button has an accessible name, keyboard focus, a 44×44px target and an original CSS magnifier with no icon request. Searching “ciência dados” correctly submitted the `q` parameter.

In the 360px sample with six menu links, the posts heading moved from 583 to 488px; at 1440px from 521 to 405px. These are preview measurements using the same fonts and content, not a newly published version. No console errors/warnings. Confirmed Portuguese import below concerns rc.6.

## Public verification — rc.6, October 12, 2026

The owner confirmed successful restoration and the requested sidebar removal. An anonymous request confirmed `balaio-version=0.2.0-rc.6`, rendered Header1/Blog1 elements and no `no-items` sections. The browser on the public URL displayed **two highlights and eight older entries**, ten distinct permalinks, a sidebar with `display:none` and no console errors/warnings. Pagination advanced to a November 2024 section beyond the displayed entries.

This verifies the Portuguese installation and home continuation on the observed blog. Designer, English import, all widget configurations and speed metrics remain subject to their own pending verification; they are not inferred from this confirmation.

## Local recovery verification — rc.6

- Every widget body was recovered from rc.3. The script is again inside Blog1’s `homeContinuation` include; post content and dates are unchanged.
- The preview starts with only two posts. At 320, 360, 768 and 1440px the browser displayed two highlights and eight distinct entries below. Pagination advanced to `older-5.html`, beyond the displayed pages.
- One search per frame, no visible sidebar, no horizontal document overflow: matching client/scroll widths of 305, 345, 753 and 1425px. No console errors or warnings.
- These are local script/CSS checks. They do not run Blogger’s compiler or widget restoration. The rc.6 recommendation also relies on the public verification above; its rc.6 version number is retained.

## Earlier responsive preview evidence — v0.2.0-rc.1

- Nine-post home: three opening cards and six distinct list entries at 320, 360, 768, 801, 1050 and 1440px, without page-wide horizontal overflow.
- Article, privacy and long-content fixtures at 320, 360, 768 and 1440px: 22px reading text and 38.5px line height, with contained wide content.
- Mobile topic fixture: all 24 links remain visible, with at least 44px link height and a single outer sidebar divider. The earlier compact-spacing comparison at 360px reduced the header from 290px to 258px and the topic list from 885px to 642px.
- Privacy navigation: one H1, WebPage microdata and the current-page link highlighted.
- Inherited Profile/Attribution fixture: hidden at 320, 768 and 1440px; article sidebar hidden and no footer output.

These are CSS/DOM fixture checks, not a Blogger compiler or full visual screenshot review. Captures were unavailable during the earlier review; remote-font loading was not confirmed for local fixtures.

## Published blog audit

An earlier browser inspection on October 11, before the v0.2.0-rc.1 upload, found the earlier stylesheet, an empty top menu, two home posts and further posts through pagination. Mobile search incorrectly appended `search` after `?m=1`; the candidate uses `/search`. Inter and Newsreader stylesheet requests and matching computed families were observed. A public article measured at 360px still used the earlier 18px body text.

The audit concerns the earlier installed theme, not a deployment of this candidate. No blog content or settings were changed.

## Earlier home continuation evidence — v0.2.0-rc.2

Before preparing rc.2, the public Portuguese blog was observed running v0.2.0-rc.1 on 11 October 2026. Native responses contained only two posts per initial page despite a `max-results=20` link. A local mirror of the actual public HTML responses, with the new script, displayed two highlights and eight additional unique posts; the pagination link moved to the first undisplayed section. This is a browser DOM/runtime check, not an import of the new XML into Blogger.

Reproducible `build_preview.py` scenarios verified: ten unique posts from a two-post start; duplicate filtering; initial and partial network failures with the last working pagination link preserved; cycles stopping; cross-origin next links not fetched; archive end hiding navigation; fetched scripts/events staying inert; no-script and disabled modes; a one-page request budget; target reached without cutting the last page. The code does not insert fetched HTML into the active document.

The `responsive-home.html` fixture was checked inside 320, 360, 768 and 1440px frames: two highlights and eight entries, with no horizontal document overflow. Measured client widths exclude the 15px vertical scrollbar (305, 345, 753 and 1425px). Tool viewport overrides did not work; the frames applied real dimensions. Screenshots were unavailable, so this is CSS/DOM verification without a fresh image review. The earlier checks above apply to v0.2.0-rc.1; also check a real phone after import. Native metadata and pagination remain intact; extra JavaScript entries are not guaranteed to be indexed on home.

## Published HTML correction — v0.2.0-rc.3

A fresh inspection on 11 October 2026 confirmed rc.2 published, two initial posts, an empty list and a native `max-results=50` link. The console reported `SyntaxError: Unexpected token '<'`: Blogger published the CDATA delimiters literally inside the script. The requested next page returned HTTP 200 without redirecting. Older dates did not prevent access to further posts.

A local replay retained the complete public HTML including its delimiters, changing only the domain to serve requests through the local copy. The original form reproduced two posts and the same error. Adding only `//` before both delimiters displayed ten distinct permalinks: two highlights and eight list entries, starting with “Como usar R no Jamovi?”. Pagination advanced beyond the last displayed entry and that corrected replay logged no errors/warnings. Next pages were requested from the actual blog; the test server did not silently follow redirects.

`build_preview.py` now preserves the raw script block instead of extracting XML parser text. The current preview, with `//<![CDATA[` in its HTML, also displayed 2 + 8 posts in 320, 360, 768 and 1440px frames, with matching client/scroll widths (305, 345, 753 and 1425px). This verifies DOM, execution and width; it is neither an rc.3 Blogger import nor a fresh screenshot review. The earlier rc.2 observations did not establish compatibility with Blogger serialization.

## Performance candidate — v0.2.0-rc.4

- Official font CSS measured 13,667 → 3,772 decoded bytes; both requests referenced the same ten font-file URLs. The ranges cover existing intermediate interface weights.
- The inspected rc.3 article had a 10,086-byte hidden sidebar (192 opening tags). Candidate XML gates this section for item/static_page; the compiled reduction needs a fresh import.
- Local replay of published rc.3 HTML with candidate script: two highlights plus eight distinct entries, no `m` on appended links, correct next-page continuation, no console errors/warnings.
- Rebuilt fixtures preserve success, duplicates, cycles, initial/partial failure, external URL rejection, archive end, inert content, no-script/disabled modes, one-page budget and complete final pages. New cases preserve other query parameters/fragments, ignore cards/pagers outside `Blog1`, and preserve navigation if `Blog1` is missing.
- Home frames at 320, 360, 768 and 1440px each displayed ten distinct entries; client and scroll widths matched at 305, 345, 753 and 1425px. Article/privacy/stress checks retain 22px text and 38.5px line height without page overflow.
- Audits of the live rc.3 home and one article found one title/canonical/H1, Portuguese language, and no structural errors. Both lacked a search description; configure it in Blogger Settings/post editor. No content/settings were changed.

These are local runtime/DOM and byte checks; no Lighthouse, Core Web Vitals, throttled network or production speed comparison was performed. [Performance evidence and controls](PERFORMANCE.md).

## Pending platform checks

Portuguese rc.6 import and home continuation are confirmed. In a test blog, save colors/fonts in Designer; verify Pages/Menu placement, both languages, search, labels, empty lists, thumbnails, pagination and comments. Check keyboard navigation, 200% zoom and printing. Record the chosen language and observed results before promoting this candidate to stable. Core Web Vitals, indexing and search/AI ranking are not established by these checks.

[Platform checklist](ROADMAP.md) · [SEO audit](SEO.md) · [Upgrade and release assets](RELEASE.md)

## Sidebar-free development layout

24 local tests passed. Home preview checked at 320, 360, 768 and 1440px: 10 unique cards, one search, no sidebar and a report-abuse footer. No horizontal overflow in these frames. Fresh Blogger import remains pending.

## Actual restore failure — 12 October 2026

The owner restored both PR #14 candidates, but public sections remain empty with `no-items`.
Header1/Blog1 elements are absent even though JavaScript registers the gadgets. The public feed
still lists 144 posts. Root cause remains open; the XML saved/exported by Blogger is needed.
Neither candidate has been merged. The rendered HTML audit now rejects registered core widgets
whose elements are missing. XML checks and handmade previews do not compile or migrate Blogger
widgets; successful CI is not proof of successful live rendering.

The owner-provided exported XML preserves all custom includables and drops the visible attributes. ID preservation and explicit visibility did not fix rendering. The rc.5 attempt moved JavaScript out of Blog1. The owner later reported visible content but only two posts; the anonymous public request still returned empty rc.5 sections, so the published outcome remains unresolved. rc.6 restored rc.3 widget behavior and subsequently received import confirmation, recorded above.
