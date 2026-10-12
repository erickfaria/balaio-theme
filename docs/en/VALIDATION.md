# Validation — v0.2.0-rc.6

[English](VALIDATION.md) · [Português](../VALIDATION.md)

## Status

rc.6 recovers the widget definitions and home continuation script from rc.3, confirmed by the owner and observed with ten posts live on October 11, 2026. It retains the sidebar-free layout, compact footer, open variable fonts, mobile navigation and 22px reading text. The owner confirmed rc.6 import and sidebar removal on October 12, 2026. It is the recommended main-branch version.

Actions runs for PRs, main, tags and manual dispatch. Historical records below retain the original verification conditions.

## Automated checks

26 local tests pass: XML/widget structure, locales, metadata/rendered HTML audit, Designer, contrast, mobile navigation/search, both CDATA serializations and continuation startup from a two-post home. A zero request budget makes no request; the default follows native pagination with the remaining count and an eight-second timeout. Without Node the four JavaScript checks are skipped locally; CI includes Node. Markdown links, English generation, XML, whitespace and preview generation pass.

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
