# Customize Balaio

[English](CUSTOMIZATION.md) · [Português](../CUSTOMIZATION.md)

## Content and navigation

- **Title, description and language:** Blogger Settings. The header displays your configured text.
- **Opening text:** Introduction gadget in Layout (Apresentação in Portuguese). Keep one `h1`; remove the gadget for a simpler home page.
- **Menu:** links to pages or labels. Home is already in the code; avoid adding a duplicate.
- **Topics:** the sidebar Labels gadget.
- **Sidebar:** accept gadgets through Layout. Check every change on mobile.

## Opening cards

The first three posts on the home page are cards. Remaining posts appear once in the list. Search, labels and archives use the normal list. Selection is automatic, not manual.

With fewer than three posts, only the available entries appear. Without a thumbnail, text remains visible. To change the count, keep the three Blog widget conditions consistent: cards use `index < 3`, the list starts at `index >= 3`, and the list heading appears at `index == 3`.

## Native color and font controls

This development branch adds controls under **Theme → Customize → Advanced** using [Blogger's documented color/font variables](https://support.google.com/blogger/answer/46871?hl=en). Import the updated XML in a test blog first. These controls are not included in stable v0.1.0 and still need confirmation in the live Designer.

The controls cover page background, main and secondary text, links/buttons, dividers, green/sand/blue pastel surfaces, interface font and post/page font. Choose pale backgrounds and dark text. The default palette passes a 4.5:1 contrast check for normal text on its four reading/card surfaces. Custom colors need a new contrast check.

The interface starts at 17px and article/page text at 20px, including phones. The reading font applies to titles too, with their existing responsive sizes preserved. Reading width, spacing and layouts remain defined by the theme: a centered column, plain background and restrained separators.

Inter and Newsreader remain the open defaults under SIL OFL. Choosing another font does not add its assets to the repository; check its license before redistributing font files. The default Google Fonts links use `display=swap` and contact `fonts.googleapis.com` and `fonts.gstatic.com`.

### Editing the XML directly

Inside the CSS comment at the beginning of `b:skin`, edit a `<Variable>` declaration. Set both `default` and `value` when defining a new source default; installed Designer choices are stored in `value`. For example:

```xml
<Variable name="washcolor" description="Pastel green surface" type="color" default="#edf5ef" value="#edf5ef"/>
```

Keep `$variable` references in `:root` connected to those declarations. The preview resolves saved values and validates unknown or duplicate names. For local fonts only, remove the three font links from `head` and set `interfacefont` to `normal 400 17px system-ui, sans-serif` and `readingfont` to `normal 400 20px serif`. Self-hosted fonts can use HTTPS `@font-face` URLs with their OFL notices preserved.

`--reading-width:760px` and `--width:1120px` remain advanced CSS options. Change them only after checking mobile layout and line length. When editing repository source, edit Portuguese and regenerate English with `python3 scripts/build_locales.py`. No build tool is needed for an installed XML edited directly in Blogger.

## Interface language

Use the matching XML from `theme/`. The English file is generated with `python3 scripts/build_locales.py`; shared styles stay identical. Post content and Blogger date formatting follow the blog's own settings.

## Verify changes

Regenerate the preview after XML changes. Check contrast, long titles, posts with and without images and keyboard navigation. Widget and expression changes must also be tested in Blogger.

## Basic pages

[About, Contact and Privacy samples](PAGES.md) use Lorem ipsum. Create the pages in Blogger, then add their real URLs to Menu. No page URLs or contact data are hardcoded in the theme. All included code and design assets are MIT; Inter and Newsreader are open fonts under SIL OFL.

## Compact mobile layout

On screens up to 800px, the header and introduction use shorter spacing. Sidebar topics form two plain columns with wrapping labels and clickable counts; all topics remain visible. Each topic link has a minimum 44px height. Only the outer sidebar gets a top divider. Posts and static pages retain their reading layout and pastel palette.

## End of posts and pages

This development version has no visible footer or credits. Articles and static pages hide the sidebar at every screen width. Profile and Attribution widgets inherited from a previous installation are hidden by theme CSS. Contact and Privacy links belong in the top Menu. License notices remain in the source and distribution. Reimport the updated XML to apply these changes; the stable v0.1.0 package retains its original footer.
