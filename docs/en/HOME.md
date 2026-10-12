# Home posts and pagination

[English](HOME.md) · [Português](../HOME.md)

v0.2.0-rc.6 preserves up to **two highlights** and lists the other posts below. When Blogger supplies a short page, the theme follows the blog’s native older-page links toward **ten posts in total**. It does not use public feeds, external libraries, carousels or infinite scrolling.

## Why were only two posts visible?

On 11 October 2026, the v0.2.0-rc.1 home at `www.balaiocientifico.com` contained two posts even though the next link requested `max-results=20`. More posts appeared through pagination. This is consistent with [Blogger auto pagination](https://blogger.googleblog.com/2010/02/auto-pagination-on-blogger.html): the platform can reduce the supplied count based on HTML and images. A theme cannot display a third native post that was not in the initial response.

v0.2.0-rc.2 was observed published on the same blog with `max-results=50`, but continuation did not execute: Blogger retained `<![CDATA[` and `]]>` inside the script and the browser reported `Unexpected token '<'`. **rc.3 makes both markers JavaScript comments**. A replay of the published HTML displayed two highlights and eight list entries after only this change. The old preview stripped the markers while parsing XML and therefore missed the failure.

The configured count is a maximum. Start with **10** under **Settings → Posts**. A native **jump break** after the introduction of long posts can also help native pagination while preserving the full article at its permalink. [Settings help](https://support.google.com/blogger/answer/9691230?hl=en) · [Post editor](https://support.google.com/blogger/answer/154172?hl=en).

The owner confirmed rc.3, and it was observed working live on October 11, 2026 with ten distinct posts and no console errors. rc.6 restores that version’s widget structure and script. Its fresh import still needs verification. [Performance and measurements](PERFORMANCE.md).

## How continuation works

1. Initially supplied posts remain HTML: two opening cards and any remaining list entries.
2. Only on home, the script inside `Blog1` follows the native older-posts link on the same origin. It requests the remaining count and uses web mode `m=0` for the responsive presentation. The restored script starts when the initial posts are already in the document.
3. The theme rebuilds text, author/date, labels and thumbnails from the received entries. Visible permalinks are not repeated. Fetched scripts, styles and event handlers are never inserted into the active page.
4. A complete page is displayed before advancing the older-posts link. The target never cuts a page midway and skips unseen entries; a larger response can exceed ten posts.
5. Loading stops at the target, after four extra pages, on failure, on a cycle without new entries, or at the end of the archive. Each request has an eight-second timeout. Native pagination remains available at the first undisplayed section; it is hidden only when the archive end is confirmed.

Results depend on available posts and the network. Without JavaScript/fetch support or on network failure, initial posts and native navigation remain usable. Search, labels, archives, articles and static pages do not trigger these extra requests. Published URLs, content and Blogger settings are not changed.

## Customize or disable

Find the `id='postlist'` element in the XML:

```xml
<div class='posts' id='postlist' data-home-posts='10' data-page-limit='4' data-list-title='More to read'>
```

- `data-home-posts`: total target, including highlights. Default 10; clamped to 2–40 by the script.
- `data-page-limit`: maximum additional pages. Default 4; clamped to 0–6. Set **0** to disable automatic continuation and keep native pagination only.
- `data-list-title`: heading used when the initial list is empty. The Portuguese variant already includes its translation.

Higher targets can increase traffic and loading time. Ten posts and four pages are the recommended defaults. The request limit prevents downloading the entire archive. Highlights remain automatic; the theme does not choose posts by interest or change chronological order.

## Verify after importing

Check two highlights, the list below, unique entries and the destination of **Older posts**. Open a list article, search and a static page. Test a slow network or JavaScript disabled. If only two posts remain, confirm the XML identifies `v0.2.0-rc.6` and the native next-page link works. If rc.2 is installed, import the complete current candidate XML; raising the post count cannot fix the syntax error. The browser console should not report `Unexpected token '<'` in the theme script.

Native posts and pagination links remain available to crawlers. JavaScript continuation supplements the reader experience; execution by search engines is not guaranteed. [SEO and crawlers](SEO.md) · [Validation and limits](VALIDATION.md) · [Installation](INSTALLATION.md).
