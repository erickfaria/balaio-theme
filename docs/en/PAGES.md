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
5. In **Layout → Pages**, select your published About me, Contact and Privacy pages and arrange their order. Use the separate **Menu** gadget for extra links; avoid duplicating Home.

The theme XML installs layouts and gadgets, not page records. Samples are separate so importing the theme cannot overwrite your page content. You can rename pages, reorder navigation, remove links or add other pages through Layout without changing XML. [Blogger page instructions](https://support.google.com/blogger/answer/165955?hl=en).

## Page layout

Static pages use the same responsive reading column as articles, without post author/date or comments. Their structured data uses `WebPage`, rather than `BlogPosting`. The body starts at H2; the page title supplies H1. Images, figures, tables and optional video containers share the [post styles](POSTS.md).

The upper menu uses ordinary links, wraps on small screens and highlights the current link when its URL exactly matches Blogger's page URL. There is no dropdown script or hamburger dependency. Keep labels short and URLs accurate; aliases, query strings or trailing-slash differences may not receive the current-page highlight.

Test each page and both menus on a phone after import. Local previews use fictitious content and do not verify live Blogger behavior.
