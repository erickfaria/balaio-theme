# Development roadmap

[English](ROADMAP.md) · [Português](../ROADMAP.md)

## Current base

Stable v0.1.0 XML templates, three opening cards on the home page, lists, articles, static pages, search, labels, pagination, basic comments, gadgets and responsive CSS. Cards do not repeat in the list; search and archives use the normal list. The owner confirmed import. Thumbnail/snippet output, locale and empty-list behavior still need specific runtime checks.

## Platform checklist

- [x] Successful Blogger import confirmed by the project owner.
- [ ] Record the imported language variant and test both language variants explicitly.
- [ ] Check zero, one and multiple posts; missing titles and images.
- [ ] Check search with and without results, labels and date archives.
- [ ] Check pagination with more posts than the home-page limit.
- [ ] Check long articles, static pages, captions, lists, tables, code and video.
- [ ] Check open/closed comments, deleted comments and the add-comment link.
- [ ] Check menu, introduction, title, description and gadgets after saving Layout.
- [ ] Check mobile/desktop, keyboard, 200% zoom and printing.
- [ ] Check page titles, canonical URLs and native head metadata.
- [ ] Implement and verify a dedicated 404 layout.

## Future work

1. Optional image logo and Theme Designer controls.
2. Higher-resolution images and topic navigation.
3. Embedded comments and threaded replies.
4. Reading time, sharing and related articles using progressive enhancement.
5. A public demo and visual review with downloaded fonts.
