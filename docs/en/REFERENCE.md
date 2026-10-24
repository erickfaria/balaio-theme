# Guides, projects and reference content

[English](REFERENCE.md) · [Português](../REFERENCE.md)

The rc.14 candidate is in development on `feat/guides-navigation-authors`. The published main version remains rc.13. Local checks and previews do not replace a Blogger test import.

## A small library inside the blog

Pillar content can remain a post: highlight its URL rather than changing its address or duplicating its content. Handbooks, documentation and tutorials retain native titles, links and metadata. Static pages use the same reading column. The theme does not create or publish pages or change content.

The proposed layout offers three entry points:

- **Pages:** institutional links in the existing menu, such as About, Contact and Privacy.
- **Topics:** the native label gadget opens a header disclosure using touch or keyboard, without a library or extra category request.
- **Guides and projects:** a short home-page strip below the introduction for a curated selection of lasting resources.

## Highlight a handbook or project

Under **Layout → Guides and projects → Edit**, add the title and real URL of three to five important resources. This is a native Link List (`LinkList2`), accepting posts, pages and external destinations. An empty list shows no strip or reserved visual space. The distributed XML contains no demonstration links.

Selection is manual: labels do not automatically promote every matching post, and publication date does not determine the selection. Use short, specific titles. Changing links does not require editing code.

For a larger collection, create a **Library** page with sections and real chapter links and add it to the strip. The home page offers a few entry points; the library holds the detailed index. No extra Wiki engine is needed.

## Header pages and categories

**Layout → Pages** keeps the main links. **Menu** remains available for extras. Automatic page discovery is unchanged. If publishing many static chapters, consider the [manual page menu](PAGES.md) to select main entry points. No new silent page limit is introduced.

**Layout → Topics** configures the same `Label1` widget previously in the legacy sidebar, retaining its identity. Select relevant labels and use a short title. Blogger labels serve as categories; the theme does not create or reorganize them. The hidden legacy sidebar section remains reserved for import compatibility.

## Structure long content

Paste the [guide sample](../../examples/pages/guide.en.html) into a post or page HTML body. Blogger supplies the H1 from its title; use H2/H3 in the body. The contents disclosure uses native `details/summary`, links and IDs written into the content, starts collapsed and works without JavaScript. Update its links when adding sections.

Existing `class="post-toc"` indexes receive the same understated styling. The theme does not scan the article to build a contents list automatically. Text, headings, code and tables retain the reading column, without a permanent sidebar or fixed navigation covering content.

Editorial selection and descriptive links establish the emphasis. The strip adds neither duplicate article schema nor an extra H1, and does not guarantee rankings. Configured gadget links are in initial HTML; automatic page discovery retains its existing JavaScript dependency.

## A restrained author byline

Posts show **Written by**, the name and, when provided by Blogger, a profile link and public 32 × 32 px photo with a CSS circular crop. Reserved dimensions, lazy loading and asynchronous decoding limit its layout impact. The image has empty alternative text because the name is adjacent.

The name and `Person` microdata remain when photo/profile data is missing. Each post uses its own author data, including team blogs; no global owner photo is applied to every post. There is no additional JavaScript, API call or profile search. `post.authorPhoto.url` and `post.authorProfileUrl` depend on what Blog1 exposes in the installation; verify them after import. Static pages and card lists keep their previous authorship behavior.

Check the author's public profile photo if it is missing. When Blogger supplies no photo, the expected result is the name alone, without a mandatory generic avatar.

## Weight and validation on this branch

Against rc.13 (`e364e68`): CSS grows from **14,724 to 17,068 bytes**; isolated gzip from **3,704 to 4,089 bytes** (385 extra bytes). These are local-file measurements, not published HTML or page-speed results. Both existing scripts remain byte-for-byte identical: **9,295 bytes**, with no extra JavaScript. No library, font or service was added. The optional author photo is one image on an individual post and is not added to cards.

**35 local tests passed**, including home continuation, automatic navigation, widget structure, translations, optional author data and guide fragment targets. Fixtures cover populated/empty resources, missing topics/photo, long author names, Portuguese/English guides and 320, 360, 768 and 1440 px frames. The sample avatar is an original SVG generated only for preview, not a person's photo.

The review browser was unavailable in this session; visual responsiveness and a real Blogger import remain pending. The preview is a fixture, not a Blogger expression compiler. These checks do not confirm restoration or profile-data availability in production.
