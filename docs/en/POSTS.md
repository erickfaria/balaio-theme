# Write responsive, search-friendly Blogger posts

[English](POSTS.md) · [Português](../POSTS.md)

The theme renders the post title as H1 and uses the visible title, author, body and permalink in article microdata. Write your body with H2 sections and H3 subsections; do not insert another H1 or a second article schema block. The layout and schema describe the same content on mobile and desktop. Schema properties do not change at screen breakpoints.

## Start with an editable example

Copy [post.en.html](../../examples/post.en.html) into the Blogger post editor's HTML mode. Replace all sample content, then set a meaningful post title and search description. The example includes a summary, method, findings, accessible table, limitations and references. Use only the sections your article needs.

## Images and media

For an informative image, write an accurate alt attribute and use the actual image dimensions. A caption can carry attribution and context:

```html
<figure>
  <img src="YOUR_HTTPS_IMAGE_URL" alt="Describe what the image explains"
       width="1200" height="800" loading="lazy" decoding="async">
  <figcaption>Context, source and credit.</figcaption>
</figure>
```

Replace the URL and dimensions with your image's values. Use eager loading for an important image visible immediately; keep secondary images lazy. Theme CSS constrains images and native video to the reading column. Images are content, not a replacement for the article's text.

For a 16:9 video iframe, use the optional wrapper below. It fills the reading column without a fixed desktop width:

```html
<div class="video">
  <iframe src="YOUR_HTTPS_EMBED_URL" title="Descriptive video title"
          loading="lazy" allowfullscreen></iframe>
</div>
```

Use an embed URL from your video provider. Other aspect ratios need a matching `aspect-ratio`. Supply a transcript or text summary where useful. The wrapper does not imply video structured data.

## Tables, code and links

Wide tables and code scroll within their containers. Give tables captions and header cells with `scope`. Avoid fixed-width inline styles on body elements. Use descriptive link text, including links to related posts and original sources. Keep authorship accurate in Blogger settings; show meaningful update notes in the text when an article changes.

Check long titles, media, tables and code at a narrow phone width after publishing. The local preview demonstrates layout; [SEO checks](SEO.md) inspect the rendered metadata. Neither substitutes for a test import on Blogger.

## Reading and list previews

Version v0.2.0-rc.6 uses Newsreader at 22px with a 1.75 line height for post/page bodies. H2/H3 scale relative to the selected reading size. Avoid fixed font sizes copied from other editors, which can override theme typography. For long posts, insert Blogger’s native jump break after the introduction; it leaves the full article available on its permalink and can help home-page pagination. The maximum home-page count is a Blogger setting, not a theme limit. [Post editor](https://support.google.com/blogger/answer/154172?hl=en) · [Installation](INSTALLATION.md).
