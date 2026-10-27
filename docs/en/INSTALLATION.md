# Install and use

[English](INSTALLATION.md) · [Português](../INSTALLATION.md)

## Before installation

Use the rc.16 XML on main: collapsible search beside the title, tighter spacing and revalidated published-page navigation, based on the imported rc.8 widget bodies. Fresh rc.16 import verification is pending. Before installing on another blog, retain a backup and check a test blog. Older release packages do not contain this version.

## Steps

1. Download `theme/balaio.en.xml` for English or `theme/balaio.xml` for Portuguese. Download the raw file, not GitHub's HTML page.
2. In Blogger, select the correct blog, then open **Theme → menu → Back up**.
3. Open **Theme → menu → Edit HTML**. Replace the contents with the entire XML, from its declaration to the closing `html` tag, then save.
4. Set title, description and blog language in **Settings**. Published pages automatically supplement navigation. In **Layout**, configure leading Pages links, Menu and Introduction; see automatic/manual modes in [PAGES.md](PAGES.md). This layout has no sidebar; inherited search/archive/featured gadgets are hidden. The Portuguese XML uses Portuguese gadget titles.
5. Add sample posts with and without images. The home page highlights the first two posts and lists the rest. Automatic continuation supplements short pages; see [HOME.md](HOME.md).
6. Check articles, pages, search, labels, pagination, comments and mobile layout. See [ROADMAP.md](ROADMAP.md).

## Use the responsive theme on phones

Blogger can serve a separate legacy mobile template. If the phone shows gray date bars, blue links and a different header at `?m=1`, while `?m=0` shows Balaio's pastel cards, the two requests are using different presentations.

In **Theme**, open the menu beside **Customize**. If **Mobile settings** is available, select **Desktop** (or the option to show the desktop theme on mobile) and save. Balaio adapts its own layout to the screen width; this setting selects which template Blogger serves. Menu labels can vary across Blogger interfaces.

Reopen the normal blog URL on a phone without manually adding `?m=0`. Check the home page, a full article and a static page. Also compare `?m=1` and `?m=0` to identify any remaining differences. Do not use a JavaScript redirect as a substitute for this setting.

The project owner's screenshots showed the legacy mobile presentation at `?m=1` and Balaio cards at `?m=0`. They do not confirm the installed release or the new Designer controls. [Official background on separate mobile templates](https://blogger-developers.googleblog.com/2011/11/introducing-custom-mobile-templates.html).

## Troubleshooting

| Problem | What to check |
| --- | --- |
| The editor rejects the file | Make sure the XML is complete, without Markdown fences or GitHub HTML. Include the exact editor message in an issue. |
| A card has no image | Try a post containing an image. Thumbnails depend on Blogger data; entries remain readable without an image. |
| Fonts look different | Check access to Google Fonts. Local fallback fonts are used when remote fonts are unavailable. |
| My pages are missing from the menu | Confirm rc.16, published pages, JavaScript and an enabled public page feed. Open or reload after publishing; drafts are excluded from the feed. Remove manually configured links in the gadget. In manual mode, add links under **Layout → Pages**. [Menu modes](PAGES.md). |
| The introduction has not changed | Edit Introduction/Apresentação in Layout and save. Keep a single `h1`. |
| Comments are missing | Check blog settings and post permissions. Embedded forms and threaded replies are not implemented yet. |
| I want the previous theme back | Restore the XML you backed up before installation from the theme menu. |

This theme does not migrate posts, images or URLs. Keep a copy of your customized XML. Installing a theme changes presentation; keep blog backups outside this repository.

[Customize](CUSTOMIZATION.md) · [Back to README](../../README.md) · [Official Blogger help](https://support.google.com/blogger/answer/176245?hl=en)

Before publishing, complete the [SEO configuration checklist](SEO.md).

## Basic pages

[About, Contact and Privacy samples](PAGES.md): About/Privacy use Lorem ipsum; Contact enables the included native form with a page-content marker, regardless of its URL. [Simple setup](CONTACT.md). XML does not create pages or replace their content. Original code is MIT; Inter/Newsreader are SIL OFL.

## Show more posts and fixed pages

The theme displays all posts supplied by Blogger: the first two in opening cards, followed by a list without duplicates. Home continuation follows up to four additional pages toward ten posts; other listing views keep native pagination. Set **Settings → Posts → Max posts shown on main page** to **10** as a starting point. This is a maximum, not a guarantee: Blogger may paginate earlier for large posts. If continuation does not load, check the network and older-posts link in [HOME.md](HOME.md). Add a native **jump break** after the introduction of long posts, then recheck. Do not change publication dates or duplicate posts. [Blogger settings](https://support.google.com/blogger/answer/9691230?hl=en) · [Post editor](https://support.google.com/blogger/answer/154172?hl=en).

The top navigation now includes **Pages** (`PageList1`), enabled on mobile. Publish About me, Contact and Privacy through **Pages**, then select them under **Layout → Pages**. The separate **Menu** gadget accepts extra links. Existing `PageList1` settings may be retained on import; verify its position in Layout. No page content or blog settings are changed by the XML.

## Restore failure

Local checks do not run Blogger’s compiler or widget migration. rc.6 recovers the complete rc.3 widget bodies; the legacy sidebar remains hidden through CSS. Back up before installation. If Restore fails or produces a blank page, try **Theme → Edit HTML** with the entire XML and record the editor’s exact message. Check that the file begins with `<?xml` and identifies `0.2.0-rc.16` in `balaio-version` metadata. Inspect the public URL outside the editor preview. Do not edit or reimport blog content to fix a presentation failure.

## Contact form

rc.13 already includes the native form outside the sidebar. Under Pages → Contact → HTML view, paste the sample containing `class="balaio-contact-page"` and publish. Any Blogger-generated URL works. Do not add another widget or edit template lines. [Setup and upgrading](CONTACT.md).

## Optional Google Analytics

After installing the updated XML, configure your `G-…` ID in **Settings → Basic → Google Analytics Measurement ID**. Without an ID, the integration stays disabled. [Enable, disable and verify GA4](ANALYTICS.md).
