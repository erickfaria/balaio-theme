# Customize Balaio

[English](CUSTOMIZATION.md) · [Português](../CUSTOMIZATION.md)

## Content and navigation

- **Title, description and language:** Blogger Settings. The header displays your configured text.
- **Opening text:** Introduction gadget in Layout (Apresentação in Portuguese). Keep one `h1`; if removing the gadget, keep a single descriptive home H1 elsewhere.
- **Pages:** select published pages in Layout and arrange their top-navigation order.
- **Menu:** add extra label or external links; avoid duplicating Home.
- **Topics:** add label links in Menu.
- **Sidebar:** removed in the development layout; search remains in the header.

## Opening cards

The first two posts on the home page are cards. Remaining posts appear once in the list. Search, labels and archives use the normal list. Automatic continuation runs only on the home page; see [HOME.md](HOME.md) for its target, request limit and off switch. Selection is automatic, not manual.

With fewer than two posts, cards show only the available entries. Without a thumbnail, text remains visible. To change the count, keep the three Blog widget conditions consistent: cards use `index < 2`, the list starts at `index >= 2`, and the list heading appears at `index == 2`.

## Native color and font controls

Version v0.2.0-rc.7 includes controls under **Theme → Customize → Advanced** using [Blogger's documented color/font variables](https://support.google.com/blogger/answer/46871?hl=en). Import the updated XML in a test blog first. These controls still need confirmation in the live Designer. They are absent from the previous stable v0.1.0.

The controls cover page background, main and secondary text, links/buttons, dividers, green/sand/blue pastel surfaces, interface font and post/page font. Choose pale backgrounds and dark text. The default palette passes a 4.5:1 contrast check for normal text on its four reading/card surfaces. Custom colors need a new contrast check.

The interface starts at 17px and article/page text at 22px, including phones. The reading font applies to titles too, with their existing responsive sizes preserved. Reading width, spacing and layouts remain defined by the theme: a centered column, plain background and restrained separators.

Inter and Newsreader remain the open defaults under SIL OFL. Choosing another font does not add its assets to the repository; check its license before redistributing font files. The default Google Fonts links use `display=swap` and contact `fonts.googleapis.com` and `fonts.gstatic.com`.

### Editing the XML directly

Inside the CSS comment at the beginning of `b:skin`, edit a `<Variable>` declaration. Set both `default` and `value` when defining a new source default; installed Designer choices are stored in `value`. For example:

```xml
<Variable name="washcolor" description="Pastel green surface" type="color" default="#edf5ef" value="#edf5ef"/>
```

Keep `$variable` references in `:root` connected to those declarations. The preview resolves saved values and validates unknown or duplicate names. For local fonts only, remove the three font links from `head` and set `interfacefont` to `normal 400 17px system-ui, sans-serif` and `readingfont` to `normal 400 22px serif`. Self-hosted fonts can use HTTPS `@font-face` URLs with their OFL notices preserved.

`--reading-width:760px` and `--width:1120px` remain advanced CSS options. Change them only after checking mobile layout and line length. When editing repository source, edit Portuguese and regenerate English with `python3 scripts/build_locales.py`. No build tool is needed for an installed XML edited directly in Blogger.

## Interface language

Use the matching XML from `theme/`. The English file is generated with `python3 scripts/build_locales.py`; shared styles stay identical. Post content and Blogger date formatting follow the blog's own settings.

## Verify changes

Regenerate the preview after XML changes. Check contrast, long titles, posts with and without images and keyboard navigation. Widget and expression changes must also be tested in Blogger.

## Basic pages

[About, Contact and Privacy samples](PAGES.md): About/Privacy use Lorem ipsum; Contact enables the included native form with a page-content marker, regardless of its URL. [Simple setup](CONTACT.md). XML does not create pages or replace their content. Original code is MIT; Inter/Newsreader are SIL OFL.

## Compact mobile layout

On screens up to 800px, the header and introduction use shorter spacing. There is no sidebar or monthly archive. Listings use the available content width. Posts and static pages retain their reading layout and pastel palette.

## End of posts and pages

Recommended rc.7 hides the sidebar on every page and keeps only Report abuse in a compact footer. The last published v0.2.0-rc.4 package still retains the listing sidebar. Inherited Profile, Attribution, BlogSearch, BlogArchive, FeaturedPost and ReportAbuse gadgets are hidden by CSS. Remove old gadgets in Layout if Blogger retains them on import, to eliminate their HTML too. Select Contact and Privacy in the top Pages gadget. License notices remain in the source and distribution. Reimport the updated XML to apply these changes; the stable v0.1.0 package retains its original footer.

The reading default is 22px with a 1.75 line height. Installed Designer settings may preserve a previous size: choose 22px in **Post and page font** after importing if needed.

## Search and spacing

The magnifier stays beside the title at every width. Tap/click it or use Enter/Space to open; Tab reaches the field and Enter submits native search. Toggle the magnifier again to close. In rc.10, the field opens to the left on the same row as the magnifier; a small arrow submits. On phones the title yields its space while search is open; closing restores it without shifting content. The brief transition respects reduced-motion preferences. Native `details/summary` needs no additional JavaScript. `.search` sets the open field’s maximum width; `.intro` and `.content-grid` control the gap before posts. Native introduction-section/widget margins are reset to avoid doubled spacing.
