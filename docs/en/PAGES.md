# Basic Blogger pages and navigation

[English](PAGES.md) · [Português](../PAGES.md)

Balaio includes editable **About**, **Contact** and **Privacy** page-body samples. They contain Lorem ipsum for layout development, not finished site content. The privacy sample is not a privacy policy. The contact sample has no form, recipient or data collection.

| Page title | Copy this body into Blogger |
| --- | --- |
| About | [about.en.html](../../examples/pages/about.en.html) |
| Contact | [contact.en.html](../../examples/pages/contact.en.html) |
| Privacy | [privacy.en.html](../../examples/pages/privacy.en.html) |

## Create the pages after importing the theme

1. Open **Blogger → Pages → New page**. Enter the page title separately.
2. Switch the editor to HTML mode and paste the sample's contents. Do not paste a whole HTML document; the theme supplies the page wrapper and H1.
3. Preview and save as a draft while using placeholder text. Replace the sample with your own content before publishing on your public blog.
4. After publishing, copy the actual URL shown by Blogger. Page URLs depend on the platform and your titles; the theme does not assume fixed `/p/` paths.
5. With rc.8, published pages automatically supplement the menu after the public feed loads. **Layout → Pages** also sets leading links, labels and order. Use **Menu** for extra links; avoid duplicating Home.

The theme XML installs layouts and gadgets, not page records. Samples are separate so importing the theme cannot overwrite your page content. Configured links retain their labels and order; automatic mode supplements the remaining public pages. To choose exactly which public pages appear, disable automatic mode as described below. [Blogger page instructions](https://support.google.com/blogger/answer/165955?hl=en).

## Page layout

Static pages use the same responsive reading column as articles, without post author/date or comments. Their structured data uses `WebPage`, rather than `BlogPosting`. The body starts at H2; the page title supplies H1. Images, figures, tables and optional video containers share the [post styles](POSTS.md).

The upper menu uses ordinary links, wraps on small screens and highlights the current page with an underline and font weight, without a colored background. There is no dropdown script or hamburger dependency. Keep labels short and URLs accurate; aliases, query strings or trailing-slash differences may not receive the current-page highlight.

Test each page and the top navigation on a phone after import. Local previews use fictitious content and do not verify live Blogger behavior.

## Automatic pages — rc.8

Navigation includes `data-auto-pages='true'` by default. Original code requests the blog’s own **public summary page feed**, without an API key or login, and adds up to 150 published pages. Configured links stay first; additional pages are sorted alphabetically. Duplicate URLs, including mobile variants, are skipped. Drafts are not part of the public feed.

Loading may take a moment. Only titles and URLs are cached in the browser session for **60 seconds**, avoiding repeat requests during navigation. After publishing, open or reload the blog; the menu can retain its previous list for that minute, plus Blogger’s own caching. There is no periodic background polling.

Requests have a six-second timeout and low priority. Network/feed failure or disabled JavaScript preserves native Pages-widget links. Page names, domain and URLs are not hardcoded for Balaio Científico or another blog.

## Select only some pages or control the complete order

Change only the navigation attribute in the XML:

```xml
<nav aria-label='Main navigation' class='navigation' data-auto-pages='false'>
```

Under **Layout → Pages → Edit**, add items using each published page’s actual URL and label, then arrange them. Some interfaces have page selection; others use **Add a new item**. Save the gadget and Layout. Manual mode respects exactly this list and makes no feed request.

In automatic mode, deselecting a page in the gadget does not exclude it from public-feed discovery. Use manual mode to choose which public pages appear.

## Important links for search and disabled JavaScript

Configured gadget links are server-rendered in the initial HTML. Automatically discovered links require JavaScript. Configure About, Contact and Privacy in the gadget for script-free access too; automatic mode will not duplicate them. This does not guarantee indexing or search ranking.

Current-page links use a subtle underline and font weight, without a colored background. Navigation height follows wrapped links, overriding Blogger’s native 30px navbar height.
