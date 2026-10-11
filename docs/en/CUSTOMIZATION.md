# Customize Balaio

[English](CUSTOMIZATION.md) · [Português](../CUSTOMIZATION.md)

## Content and navigation

- **Title, description and language:** Blogger Settings. The header displays your configured text.
- **Opening text:** Introduction gadget in Layout (Apresentação in Portuguese). Keep one `h1`; remove the gadget for a simpler home page.
- **Menu:** links to pages or labels. Home is already in the code; avoid adding a duplicate.
- **Topics:** the sidebar Labels gadget.
- **Sidebar and footer:** accept gadgets through Layout. Check every change on mobile.

## Opening cards

The first three posts on the home page are cards. Remaining posts appear once in the list. Search, labels and archives use the normal list. Selection is automatic, not manual.

With fewer than three posts, only the available entries appear. Without a thumbnail, text remains visible. To change the count, keep the three Blog widget conditions consistent: cards use `index < 3`, the list starts at `index >= 3`, and the list heading appears at `index == 3`.

## Colors and typography

Edit `:root` inside `b:skin` in the Portuguese XML, then regenerate the English variant. `--paper` is the background; `--ink` main text; `--muted` secondary text; `--accent` links and buttons; `--line` borders; `--wash` soft surfaces. The second and third card backgrounds use `--card-sand` and `--card-blue`; `--reading-width` controls the article column.

`--sans` selects interface fonts and `--serif` selects reading fonts. Inter and Newsreader are requested from Google Fonts with `display=swap`, with local fallbacks. This makes requests to `fonts.googleapis.com` and `fonts.gstatic.com`.

For local fonts only, remove the three font links from `head` and set the variables to `system-ui,sans-serif` and `Georgia,serif`. To host the open fonts yourself, use HTTPS URLs in `@font-face` and preserve their OFL notices. MIT does not require a visible theme credit; you may customize the footer while retaining license notices in redistributed code.

## Interface language

Use the matching XML from `theme/`. The English file is generated with `python3 scripts/build_locales.py`; shared styles stay identical. Post content and Blogger date formatting follow the blog's own settings.

## Verify changes

Regenerate the preview after XML changes. Check contrast, long titles, posts with and without images and keyboard navigation. Widget and expression changes must also be tested in Blogger.

## Quick pastel customization

Change only these values inside the existing `:root` block; no widget edits or build tools are needed when editing your chosen XML directly in Blogger:

```css
--wash:#edf5ef;
--card-sand:#f8f1e7;
--card-blue:#eef2f6;
--reading-width:760px;
```

Keep text and link colors dark enough for contrast. These are Balaio's original pastel defaults. For post content, see [POSTS.md](POSTS.md).
