# Performance and a clean Blogger theme

[English](PERFORMANCE.md) · [Português](../PERFORMANCE.md)

v0.2.0-rc.4 keeps the minimal pastel layout, 22px reading text and open Inter/Newsreader fonts. No analytics, third-party JavaScript library, carousel or new runtime dependency was added. Install the complete XML; this guide does not change your Blogger content or settings.

## What the theme optimizes

- Requests Inter weights 400–750 and Newsreader weights 400–700 as variable ranges, including the existing 650/750 interface weights. One Google Fonts stylesheet, two preconnections, `display=swap` and local fallbacks remain. [Google Fonts CSS2 ranges](https://developers.google.com/fonts/docs/css2).
- Omits the sidebar section from article/static-page HTML instead of only hiding it. Home, search, label and date listings retain the sidebar. Profile/Attribution CSS remains a migration safeguard.
- Starts home continuation after `load`, then an idle opportunity with a one-second timeout, or a yielded timer cycle if `requestIdleCallback` is absent. The first two posts and native navigation remain usable while extra posts arrive. The timeout starts after `load`; a slow initial resource can delay continuation. [Idle scheduling](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestIdleCallback).
- Sends a low-priority fetch hint; browsers decide how to apply it. Keeps sequential requests, a ten-post target, four-page budget, eight-second request timeouts, duplicate filtering and native pagination on failure. No prefetching of the entire archive. [Request options](https://developer.mozilla.org/en-US/docs/Web/API/RequestInit#priority).
- Reads cards and pagination only inside `Blog1`. Rebuilds safe text/link/thumbnail nodes; fetched scripts, styles and event handlers remain inert. Appended post/label links lose only the mobile `m` parameter; other query parameters and fragments survive.
- Preserves Blogger's native title/canonical/metadata and visible-content microdata. It adds no crawler-specific scripts or duplicate metadata.

## Measured evidence and limits

Measurements taken on October 11, 2026 from the public Portuguese rc.3 blog and official font responses, before importing rc.4:

| Observation | Baseline | Optimized or avoidable |
| --- | --- | --- |
| Google Fonts decoded CSS, Chrome 130 user agent | 13,667 bytes / 37 font-face blocks | 3,772 bytes / 10 blocks: about 72% less CSS |
| Same stylesheet, gzip response | 847 bytes | 689 bytes in this sample |
| Hidden sidebar in the inspected article HTML | 10,086 bytes / 192 opening tags | Candidate condition omits this block; final compiled output needs a fresh import |
| Distinct home posts in local replay of public HTML | 10 in working rc.3 | 10 with candidate script: two highlights and eight list entries |

The two font responses referenced the **same ten unique font file URLs**. This is a stylesheet reduction, not evidence of fewer downloaded font files. Responses vary with user agent, caching and the font provider. Sidebar size depends on saved gadgets; Blogger may retain gadgets from an earlier theme.

The inspected initial home HTML was 37,049 bytes decoded (9,744-byte gzip response); the article was 44,477 bytes (11,048-byte gzip response). The native Blogger widget CSS and JavaScript responses were 36,892 and 152,070 bytes decoded. They support platform gadgets and remain enabled. Additional native pages include their own markup; inert parsing does not insert their styles/scripts into the active document, but their HTML still costs bandwidth.

These are byte/DOM/runtime observations, **not** Lighthouse scores, Core Web Vitals or proof of ranking improvements. No mobile throttling or before/after production loading-time comparison was performed. The optimized XML has not yet been imported; English output and every native gadget have not been independently verified in Blogger. [Validation scope](VALIDATION.md).

## Keep your installation fast

1. Start with ten posts in Blogger Settings and keep the default continuation budget. Raising the target can increase traffic. Set `data-page-limit='0'` to disable automatic continuation while retaining native older-post links. [Home settings](HOME.md).
2. Under Layout, review optional sidebar gadgets. A second search, repeated Featured Post or a large archive adds markup to listings. Remove only gadgets you do not use. Reimporting a template does not guarantee removal of saved gadgets.
3. Resize/compress post images before upload; give them dimensions and descriptive alt text. Keep above-the-fold article images eager; use native lazy loading for later images and embeds. Decorative listing thumbnails already have dimensions and lazy loading/asynchronous decoding. [Browser image loading](https://web.dev/articles/browser-level-image-lazy-loading).
4. Avoid pasted fixed widths, oversized inline styles and scripts in post bodies. Use the [post sample](POSTS.md) and Blogger jump breaks after long introductions.
5. For installed-font fallbacks only, remove the three Google Fonts links from the XML head. This stops those external requests; available fonts vary by reader device. When self-hosting fonts, retain their OFL notices and update CSS/URLs yourself. [Font licensing](PROVENANCE.md).
6. Enable and fill Blogger search descriptions, including per-post descriptions. The audited home and article lacked `meta name="description"`; the theme intentionally relies on the native head rather than inventing summaries. [SEO setup](SEO.md).

## Validate on your published blog

After importing, test the first load on a phone and a slow connection, then open an article, a static page, search and older posts. Check ten distinct entries, correct next-page destination, native navigation without JavaScript, no console errors and no horizontal page overflow. Save actual results from PageSpeed Insights/Search Console before claiming a Core Web Vitals improvement; initial resources, content, ads, gadgets and Blogger itself affect the result.

Developers should run `make check` and `make preview` locally. Four Node checks include both CDATA serializations and deferred scheduling with/without idle support. `responsive-reading.html` checks article/privacy/stress layouts; `responsive-home.html` exercises 320, 360, 768 and 1440px frames; `short-mobile-links.html`, `short-mixed.html` and `short-missing-blog.html` exercise the new link/scope cases. These fixtures do not compile Blogger XML. GitHub Actions remains disabled and the saved workflow is manual-only.
