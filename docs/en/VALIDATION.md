# Validation — v0.2.0-rc.3

[English](VALIDATION.md) · [Português](../VALIDATION.md)

## Status

Release candidate prepared on October 11, 2026. The owner confirmed v0.1.0 import, and Portuguese v0.2.0-rc.2 was observed published with the home failure described below. The corrected v0.2.0-rc.3 XMLs still need a fresh Blogger import. No claim is made that both languages or every native widget have been tested independently on the platform.

## Automated checks

Twenty-three tests cover XML/widget structure, locale equivalence, native SEO metadata and rendered HTML auditing, Designer variable resolution/default contrast, and mobile navigation/search regressions. Three Node.js checks parse the home script with preserved CDATA, XML-stripped CDATA, and reject the form that failed in rc.2. Without Node the three are skipped locally; they are mandatory in CI. Both XMLs parse; English generation is current; local Markdown links and Git whitespace pass. CI repeats the checks and builds the preview and clean install package. External links and heading anchors are not checked automatically.

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

## Pending platform checks

Import the candidate in a test blog; save colors/fonts in Designer; verify Pages/Menu placement, both languages, search, labels, empty lists, thumbnails, pagination and comments. Check keyboard navigation, 200% zoom and printing. Record the chosen language and observed results before promoting this candidate to stable. Core Web Vitals, indexing and search/AI ranking are not established by these checks.

[Platform checklist](ROADMAP.md) · [SEO audit](SEO.md) · [Upgrade and release assets](RELEASE.md)
