# Home posts and pagination

[English](HOME.md) · [Português](../HOME.md)

The theme shows up to **two highlights** and lists the other posts below. When Blogger supplies a short home with an older-posts link, continuation can follow native pagination toward **ten posts**.

## Why were only two posts visible?

On 11 October 2026, the v0.2.0-rc.1 home at `www.balaiocientifico.com` contained two posts even though the next link requested `max-results=20`. More posts appeared through pagination. This is consistent with [Blogger auto pagination](https://blogger.googleblog.com/2010/02/auto-pagination-on-blogger.html): the platform can reduce the supplied count based on HTML and images. A theme cannot display a third native post that was not in the initial response.

v0.2.0-rc.2 was observed published on the same blog with `max-results=50`, but continuation did not execute: Blogger retained `<![CDATA[` and `]]>` inside the script and the browser reported `Unexpected token '<'`. **rc.3 makes both markers JavaScript comments**. A replay of the published HTML displayed two highlights and eight list entries after only this change. The old preview stripped the markers while parsing XML and therefore missed the failure.

The configured count is a maximum. Start with **10** under **Settings → Posts**. A native **jump break** after the introduction of long posts can also help native pagination while preserving the full article at its permalink. [Settings help](https://support.google.com/blogger/answer/9691230?hl=en) · [Post editor](https://support.google.com/blogger/answer/154172?hl=en).

The owner confirmed rc.3, and it was observed working live on October 11, 2026 with ten distinct posts and no console errors. rc.6 restores that version’s widget structure and script. The owner confirmed rc.6 import on October 12, 2026; public inspection found two highlights plus eight older posts and no console errors. [Performance and measurements](PERFORMANCE.md).

## How continuation works

1. Initially supplied posts remain HTML: two opening cards and any remaining list entries.
2. The Blog1 widget includes the script only on a nonempty home below the post target, with an older-posts URL and a positive page budget. It waits for the initial HTML and uses idle time when available. Requests use low priority and ask for the remaining count.
3. The theme rebuilds text, author/date, labels and thumbnails from entries received inside `Blog1`. Visible permalinks are not repeated. Fetched scripts, styles and event handlers are never inserted into the active page.
4. A complete page is displayed before advancing the older-posts link. The target never cuts a page midway and skips unseen entries; a larger response can exceed ten posts.
5. Loading stops at the target, after four extra pages, on failure, on a cycle without new entries, or at the end of the archive. Each request has an eight-second timeout. Native pagination remains available at the first undisplayed section; it is hidden only when the archive end is confirmed.

Results depend on available posts and the network. Without JavaScript/fetch support or on network failure, initial posts and native navigation remain usable. Search, labels, archives, articles and static pages do not trigger these extra requests. Published URLs, content and Blogger settings are not changed.

## Customize or disable

Find the `homePostTarget` and `homePageLimit` variables inside Blog1 in the XML. Their values control both template rendering and browser behavior.

- `homePostTarget`: target including highlights. Default 10, supported range 2–40.
- `homePageLimit`: maximum number of additional pages. Default 4, supported range 0–6. Set it to 0 to omit the script and use native pagination alone.

Larger settings may increase traffic. When updating a customized theme, transfer any previous `data-home-posts` or `data-page-limit` settings to these variables.

## Verify after importing

Check two highlights, the list below, unique entries and the destination of **Older posts**. Open a list article, search and a static page. Test a slow network or JavaScript disabled. If only two posts remain, confirm the published version and check the native next-page link. If rc.2 is installed, import the complete current candidate XML; raising the post count cannot fix the syntax error. The browser console should not report `Unexpected token '<'` in the theme script.

Native posts and pagination links remain available to crawlers. JavaScript continuation supplements the reader experience; execution by search engines is not guaranteed. [SEO and crawlers](SEO.md) · [Validation and limits](VALIDATION.md) · [Installation](INSTALLATION.md).
