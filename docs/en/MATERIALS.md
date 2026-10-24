# Web library and reference materials

[English](MATERIALS.md) · [Português](../MATERIALS.md)

The theme presents reference materials with ordinary HTML and restrained CSS. It adds no scripts, requests, Wiki engine or printing mode. Inter and Newsreader retain their OFL licenses; original code and examples are MIT. Published text and images keep the rights selected by their authors.

## A simple structure

- **Library:** a page listing materials by type, each with a title, short summary and link.
- **Handbook:** an introduction and chapter index. A complete handbook may also remain in one existing post, keeping its URL.
- **Chapter:** text and links to the index, previous and next available chapters.
- **Documentation:** purpose, requirements, instructions and references. Include version/review information only when accurate.

Add the Library URL once to Pages or Guides and projects. Keep a small main menu. If chapters are static pages, use [manual navigation](PAGES.md) to avoid listing every chapter in the header.

## Use in the Blogger editor

Copy an example body into the HTML editor, replace the sample text and set links to published destinations:

- [Library](../../examples/pages/library.en.html).
- [Handbook introduction](../../examples/pages/book.en.html).
- [Chapter](../../examples/pages/chapter.en.html).
- [Project documentation](../../examples/pages/project.en.html).
- [Guide with a native contents disclosure](../../examples/pages/guide.en.html).

Blogger supplies H1 from the title. Bodies use H2/H3 and contain no widget tags, scripts, photos or external demo URLs. Example fragment links target sections in the same body; replace them with chapter URLs when separating pages. The theme does not publish pages or maintain editorial indexes by itself.

## Automate from Markdown

A publisher can compile the same blocks while sending Markdown to Blogger. The theme displays them. See the [portable front matter example](../../examples/material.en.md):

```toml
[params.material]
kind = "chapter"
collection = "jamovi-handbook"
order = 10
```

Suggested kinds are `guide`, `documentation`, `study`, `article`, `book`, `chapter` and `library`. A `book` introduces a collection; chapters have unique positive order numbers. `title` and `description` supply link labels and summaries. Version, review date and content license are optional and must be accurate.

The generator should use confirmed IDs and URLs, omit drafts/future content and refresh indexes during synchronization. It should not guess permalinks or fetch the archive in a reader's browser. Update frequency belongs to the publisher, not the theme. TOML custom fields are portable, but a Hugo theme needs templates that interpret them to recreate this navigation.

## A small HTML contract

| Class | Content |
| --- | --- |
| `material-meta` | Material kind and optional version/review context. |
| `material-license` | Optional content-license link with `rel="license"`. |
| `material-library` | H2 sections and material lists with summaries. |
| `material-index` | Chapter navigation and ordered links. |
| `collection-nav` | Index, previous (`rel="prev"`) and next (`rel="next"`) links. |

The HTML remains readable without styles and navigable without JavaScript. Text and links are in the initial response and identical for people, search engines and automated readers. It adds no hidden AI text, duplicate JSON representation or Book schema with unverified data. [SEO and platform limits](SEO.md).

Videos can use descriptive ordinary links, loading the video service only after the reader opens the destination. The theme does not rewrite videos in old posts. Contact and comments still depend on Blogger settings and services.

## Validation

Preview the Library, chapter, handbook and project documentation. Tests check fragment targets and script-free examples. Real Blogger import, device visuals and rendered HTML remain separate checks. This work does not change print styles or add PDF export features.

## Project documentation with chapters

A project index can use `kind = "documentation"` and `collection`, without `order`: [front matter example](../../examples/material-documentation.en.md). Inner pages use `kind = "chapter"`, the same collection and a positive order. A compatible publisher generates the index, a collection link near the beginning and previous/next links at the end; the theme cannot infer this relationship from Blogger titles or labels alone.

Documentation chapters can be static pages, keeping the home feed for posts. Select the main links once in manual-navigation mode to avoid listing every chapter in the header. An existing handbook may remain a single post with an internal section index, without duplication or a URL change.

In the local preview, open `project.html` and follow Installation, Getting started and Updates (the connected demonstration currently uses Portuguese labels). These examples use ordinary links, without navigation scripts or content delivery. Topics on this branch uses the same typography, line height, target height and alignment as main-menu links, without a pill, border, highlighted background or triangle. The styles add 761 CSS bytes (117 isolated gzip bytes); both scripts remain identical to rc.14. Visual browser review remains pending in this session.
