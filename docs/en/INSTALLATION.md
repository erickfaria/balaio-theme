# Install and use

[English](INSTALLATION.md) · [Português](../INSTALLATION.md)

## Before installation

Use a test blog with several posts and a static page. Keep a backup of your current theme. This is an experimental version; successful Blogger import has not yet been confirmed.

## Steps

1. Download `theme/balaio.en.xml` for English or `theme/balaio.xml` for Portuguese. Download the raw file, not GitHub's HTML page.
2. In Blogger, select the correct blog, then open **Theme → menu → Back up**.
3. Open **Theme → menu → Edit HTML**. Replace the contents with the entire XML, from its declaration to the closing `html` tag, then save.
4. Set title, description and blog language in **Settings**. In **Layout**, configure Menu, Introduction, labels, sidebar and footer. The Portuguese XML uses Portuguese gadget titles.
5. Add sample posts with and without images. The home page uses the first three posts as cards; configure more than three posts per page if you also want the list below them.
6. Check articles, pages, search, labels, pagination, comments and mobile layout. See [ROADMAP.md](ROADMAP.md).

## Troubleshooting

| Problem | What to check |
| --- | --- |
| The editor rejects the file | Make sure the XML is complete, without Markdown fences or GitHub HTML. Include the exact editor message in an issue. |
| A card has no image | Try a post containing an image. Thumbnails depend on Blogger data; entries remain readable without an image. |
| Fonts look different | Check access to Google Fonts. Local fallback fonts are used when remote fonts are unavailable. |
| My pages are missing from the menu | Add their URLs to the Menu gadget. The theme does not create blog pages. |
| The introduction has not changed | Edit Introduction/Apresentação in Layout and save. Keep a single `h1`. |
| Comments are missing | Check blog settings and post permissions. Embedded forms and threaded replies are not implemented yet. |
| I want the previous theme back | Restore the XML you backed up before installation from the theme menu. |

This theme does not migrate posts, images or URLs. Keep a copy of your customized XML. Installing a theme changes presentation; keep blog backups outside this repository.

[Customize](CUSTOMIZATION.md) · [Back to README](../../README.md) · [Official Blogger help](https://support.google.com/blogger/answer/176245?hl=en)
