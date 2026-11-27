# Performance and a clean Blogger theme

[English](PERFORMANCE.md) · [Português](../PERFORMANCE.md)

rc.7 retains the rc.6 baseline and restores rc.3 widgets and continuation, retaining the pastel layout, 22px reading text and open Inter/Newsreader fonts. The base includes no external JavaScript library or carousel. Analytics is optional starting with rc.16 and is only called with an ID configured in Blogger. [Setup](ANALYTICS.md). Portuguese import and home continuation were confirmed by the owner and checked on the public blog. [Status and evidence](VALIDATION.md).

## How the theme limits work

- One Google Fonts stylesheet, two preconnections, `display=swap` and local fallbacks. Inter 400–750 and Newsreader 400–700 use variable ranges. [Google Fonts CSS2](https://developers.google.com/fonts/docs/css2).
- Two HTML highlights and a continuation list targeting ten posts. When the homepage needs more posts, continuation waits for the initial HTML and browser idle time when available, fetching at most four sequential pages at low priority. Requests have eight-second timeouts; it does not download the entire archive. [Home settings](HOME.md).
- Inert template parsing; the theme reads only the response’s Blog1 widget and rebuilds entries with text, links and thumbnails. Fetched scripts, event handlers and styles are never inserted into the active document. Native pagination remains on failure.
- Decorative thumbnails have dimensions, lazy loading and asynchronous decoding. When Blogger offers two distinct sizes, the browser chooses between 320w and 640w. The original URL remains the fallback. Entries without thumbnails remain readable.
- Page-specific titles, Blogger canonical and metadata, with visible-content microdata. No special crawler scripts or duplicated metadata.
- The legacy sidebar section is reserved for the Layout editor so widgets have a place during migration. Check the editor and public HTML after importing the XML.

Check a short homepage and native pagination after importing the theme. Measure load on a mobile connection to assess the effects of scheduling and the priority hint.

## Earlier measurements

On October 11, 2026 official font responses measured 13,667 → 3,772 decoded CSS bytes using variable ranges. Both referenced the same ten font-file URLs: less stylesheet CSS, without proof of fewer font downloads. Responses vary with browser and cache.

The inspected rc.3 home HTML measured 37,049 decoded bytes (9,744 gzip). One article measured 44,477 bytes (11,048 gzip), including 10,086 bytes of hidden sidebar. Native Blogger widget CSS/JavaScript measured 36,892/152,070 decoded bytes and remains enabled. These are not Lighthouse scores, Core Web Vitals or proof of better rankings. No production speed comparison was performed with this recovery.

## Keep your installation fast

1. Start with ten posts in Settings and retain the default continuation budget. Set `data-page-limit='0'` to disable extra requests. Higher targets increase traffic.
2. Check inherited optional gadgets in the Layout editor after installing the theme.
3. Resize/compress images before upload; include dimensions and descriptive alt text. Keep initial article images eager; use lazy loading for later images. [Browser image loading](https://web.dev/articles/browser-level-image-lazy-loading).
4. Avoid fixed widths and excessive post styles/scripts. Use the [post sample](POSTS.md) and a native jump break after long introductions.
5. For device fonts, remove the three Google Fonts links from the XML head. Preserve OFL notices when self-hosting fonts. [Licenses](PROVENANCE.md).
6. Fill blog and post search descriptions. The theme uses native metadata rather than inventing summaries. [SEO](SEO.md).

## Verify on the public blog

After import, check two highlights plus the list below, correct pagination, an article, a static page, search, mobile layout, no horizontal overflow and no console errors. Test a slow connection and disabled JavaScript. Use actual PageSpeed Insights/Search Console observations for speed and indexing; content, images, ads, gadgets and the platform affect results.

`make check` validates XML, locales, documentation and code. `make preview` generates visual/continuation cases, including a home starting with only two posts. The preview does not compile Blogger XML. Actions runs checks and creates artifacts identified by commit.

## Automatic navigation — rc.9

In rc.9, navigation requests the summary page feed once per page load, at low priority with a six-second timeout. It revalidates the HTTP cache, allowing conditional responses, and does not access session storage. This trades rc.8’s avoided requests for refreshed published/draft links on reload. The observed four-page feed response measured 6,659 bytes and varies with content. There is no external library, API key or polling.

Automatic links are added by JavaScript; keep essential links in the native gadget for script-free access and initial HTML. Use `data-auto-pages='false'` for a fully manual menu without this request. [Modes and limits](PAGES.md).

## Optional contact — rc.13

The native widget is declared only for static pages, in its own section. A content marker activates presentation through CSS `:has()`, without URL detection, added JavaScript, feed requests or another library. Form markup also exists, hidden, on other static pages; it is not rendered on home or posts. Delivery depends on Blogger’s native runtime, which the theme does not copy or replace. [Setup](CONTACT.md).
