# Performance and a clean Blogger theme

[English](PERFORMANCE.md) · [Português](../PERFORMANCE.md)

Recommended rc.6 restores rc.3 widgets and continuation, retaining the pastel layout, 22px reading text and open Inter/Newsreader fonts. There is no external JavaScript library, analytics or carousel. Portuguese import and home continuation were confirmed by the owner and checked on the public blog. [Status and evidence](VALIDATION.md).

## How the theme limits work

- One Google Fonts stylesheet, two preconnections, `display=swap` and local fallbacks. Inter 400–750 and Newsreader 400–700 use variable ranges. [Google Fonts CSS2](https://developers.google.com/fonts/docs/css2).
- Two HTML highlights and a continuation list targeting ten posts. The restored script starts inside Blog1 after the post markup, fetching at most four sequential pages. Requests have eight-second timeouts; it does not download the entire archive. [Home settings](HOME.md).
- Inert template parsing; entries are rebuilt with text, links and thumbnails. Fetched scripts, event handlers and styles are never inserted into the active document. Native pagination remains on failure.
- Decorative thumbnails have dimensions, lazy loading and asynchronous decoding. Entries without thumbnails remain readable.
- Native title, canonical and metadata, with visible-content microdata. No special crawler scripts or duplicated metadata.
- The legacy sidebar is hidden through CSS to retain the importable structure. This does not remove its HTML: remove unused optional gadgets in Layout, such as duplicate search, date archives or Featured Post. Header, Pages, Menu and Posts remain core gadgets.

The experimental rc.4 script optimizations — load/idle scheduling, low priority, Blog1 scope and mobile-parameter cleanup — are not part of the recovered script. This candidate prioritizes confirmed behavior; future changes must preserve the post list in actual Blogger import tests.

## Earlier measurements

On October 11, 2026 official font responses measured 13,667 → 3,772 decoded CSS bytes using variable ranges. Both referenced the same ten font-file URLs: less stylesheet CSS, without proof of fewer font downloads. Responses vary with browser and cache.

The inspected rc.3 home HTML measured 37,049 decoded bytes (9,744 gzip). One article measured 44,477 bytes (11,048 gzip), including 10,086 bytes of hidden sidebar. Native Blogger widget CSS/JavaScript measured 36,892/152,070 decoded bytes and remains enabled. These are not Lighthouse scores, Core Web Vitals or proof of better rankings. No production speed comparison was performed with this recovery.

## Keep your installation fast

1. Start with ten posts in Settings and retain the default continuation budget. Set `data-page-limit='0'` to disable extra requests. Higher targets increase traffic.
2. Review inherited optional gadgets in Layout. Blogger can retain them when installing a theme.
3. Resize/compress images before upload; include dimensions and descriptive alt text. Keep initial article images eager; use lazy loading for later images. [Browser image loading](https://web.dev/articles/browser-level-image-lazy-loading).
4. Avoid fixed widths and excessive post styles/scripts. Use the [post sample](POSTS.md) and a native jump break after long introductions.
5. For device fonts, remove the three Google Fonts links from the XML head. Preserve OFL notices when self-hosting fonts. [Licenses](PROVENANCE.md).
6. Fill blog and post search descriptions. The theme uses native metadata rather than inventing summaries. [SEO](SEO.md).

## Verify on the public blog

After import, check two highlights plus the list below, correct pagination, an article, a static page, search, mobile layout, no horizontal overflow and no console errors. Test a slow connection and disabled JavaScript. Use actual PageSpeed Insights/Search Console observations for speed and indexing; content, images, ads, gadgets and the platform affect results.

`make check` validates XML, locales, documentation and code. `make preview` generates visual/continuation cases, including a home starting with only two posts. The preview does not compile Blogger XML. Actions runs checks and creates artifacts identified by commit.
