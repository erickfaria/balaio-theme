# Basic Blogger pages and navigation

[English](PAGES.md) · [Português](../PAGES.md)

Balaio includes editable page-body samples for About, Contact and Privacy. About/Privacy use Lorem ipsum; the privacy sample is not a privacy policy. Contact contains `class="balaio-contact-page"`, which displays the native form included in the theme with any Blogger-generated URL. [Simple setup](CONTACT.md).

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
5. In **Layout → Pages**, choose which published pages appear in the menu and arrange their order. Use **Menu** for extra links and keep Home in one place.

Use **Pages** to create content and **Layout → Pages** to select links. If you used feed discovery in an older theme, move the links you want into the Pages or Menu gadgets before upgrading. [Blogger page instructions](https://support.google.com/blogger/answer/165955?hl=en).

## Page layout

Static pages use the same responsive reading column as articles, without post author/date or comments. Their structured data uses `WebPage`, rather than `BlogPosting`. The body starts at H2; the page title supplies H1. Images, figures, tables and optional video containers share the [post styles](POSTS.md).

The upper menu uses ordinary links, wraps on small screens and highlights the current page with an underline and font weight, without a colored background. There is no dropdown script or hamburger dependency. Keep labels short and URLs accurate; aliases, query strings or trailing-slash differences may not receive the current-page highlight.

Test each page and the top navigation on a phone after import. Local previews use fictitious content and do not verify live Blogger behavior.

## Select only some pages or control the complete order

Under **Layout → Pages → Edit**, select the pages to show and arrange their order. If the gadget offers **Add a new item**, use the published URL and the label you want. Save the gadget and Layout.

## Important links for search and disabled JavaScript

Both native gadgets render links in the initial HTML. Put About, Contact and Privacy in either gadget to give readers and crawlers a direct link.

Current-page links use a subtle underline and font weight, without a colored background. Navigation height follows wrapped links, overriding Blogger’s native 30px navbar height.

## Handbooks, projects and small Wikis

The [reference-content guide](REFERENCE.md) covers curated home links and the [long-page sample](../../examples/pages/guide.en.html), with native contents and anchors. Pillar content can remain a post at its current permalink.
