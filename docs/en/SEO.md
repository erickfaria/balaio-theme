# SEO and discovery in AI search

[Português](../SEO.md) · [English](SEO.md)

The theme provides a technical foundation. Rankings, indexing and citations also depend on the published content, Blogger settings and search engines. There is no guaranteed position or universal “LLM SEO” switch.

## What the theme does

- Keeps one native document title and Blogger's `all-head-content` for canonical URLs, feeds, sharing metadata and configured indexing controls. Do not paste duplicate metadata blocks into the template.
- Uses a main heading for articles, static pages and non-home listings. The editable home introduction supplies its H1; keep one meaningful H1 when editing it.
- Describes visible article content with schema.org `BlogPosting` microdata (headline, author, body and permalink). Static pages use `WebPage`. Microdata avoids constructing JSON from unescaped post text. No invented dates, ratings, organization or publisher credentials are emitted.
- Uses normal HTML links, responsive reading layouts and decorative card images with empty alt text, dimensions and asynchronous decoding. Descriptive images inside posts still need your own alt text.

Google supports article microdata and recommends applicable, accurate properties. The current schema is deliberately partial: publication/modification dates and representative high-resolution images need verified Blogger data bindings before they can be added. Validate the **published** page with [Rich Results Test](https://search.google.com/test/rich-results), then inspect it in Search Console. A valid template XML is not proof that Blogger renders the schema correctly. [Article documentation](https://developers.google.com/search/docs/appearance/structured-data/article).

## Configure Blogger before publishing

1. In **Settings → Privacy**, enable visibility to search engines for your public blog.
2. In **Settings → Meta tags**, enable search descriptions and write a concise, accurate description of the blog. In each post editor, fill **Search description** with a specific summary. Check the resulting HTML for a nonempty `meta name="description"`; the theme relies on Blogger's native head output.
3. Set the correct language and HTTPS redirects. Check that alternate hostnames redirect to the preferred HTTPS URL and that each article's canonical points to that article.
4. Review custom robots.txt and robots header settings carefully. Keep intended private/search pages excluded; ensure public articles are not accidentally `noindex` or blocked. Do not copy a generic “allow everything” recipe.
5. Verify the domain in [Google Search Console](https://search.google.com/search-console) and [Bing Webmaster Tools](https://www.bing.com/webmasters/). Submit the Blogger `/sitemap.xml`, inspect representative articles and monitor indexing errors.
6. Give posts specific titles, useful headings, descriptive internal links, source references and visible authorship. Show real publication/update dates when relevant. Avoid keyword stuffing and unsupported claims. Compress images and include descriptive alt text in the post editor.
7. After import, test home, an article, a static page, search, a label archive and pagination. Run mobile performance checks on the real blog; preview fixtures cannot establish Core Web Vitals.

[Blogger's search setup guide](https://support.google.com/blogger/answer/41373?hl=en).

## AI search and crawler choices

Google's AI search features use the existing SEO foundation; no special AI file or schema is required. Eligible pages need indexing and snippet availability. [Google AI search documentation](https://developers.google.com/search/docs/appearance/ai-features).

For ChatGPT search, `OAI-SearchBot` handles discovery; `GPTBot` handles model training independently. `ChatGPT-User` handles user-triggered visits. Decide retrieval and training permissions separately; the theme changes neither policy. Check robots.txt and any firewall rules on your published domain. [Official OpenAI crawler documentation](https://developers.openai.com/api/docs/bots).

This repository does not generate `llms.txt`, hidden AI instructions or a replacement sitemap. Blogger serves robots.txt and sitemaps outside the template.

## Inspect rendered HTML

No dependencies are required:

```sh
python3 scripts/audit_seo.py --url https://www.example.com/
python3 scripts/audit_seo.py --url https://www.example.com/2026/10/example.html
python3 scripts/audit_seo.py --file /tmp/saved-page.html
```

The JSON report checks title, canonical, description, H1, language, missing image alt attributes, JSON-LD syntax and search restrictions. Exit code 1 means a structural error; warnings require context and do not change the exit code. Robot restrictions retain their agent scope. The audit does **not** prove indexing, schema completeness, robots.txt access or performance. Never run it on uncompiled template XML. HTTP failures propagate as errors; it follows redirects and checks their final HTML.

## Live baseline — 2026-10-11

Read-only observations at `https://www.balaiocientifico.com/` **before installing this branch's theme**:

- Home and `/2025/04/analise-de-dados-do-cnes-no-jamovi.html` return HTTP 200 and self-referencing HTTPS canonicals.
- The inspected article has the blog name as H1 rather than the article title. The new theme assigns the article title to H1.
- Both inspected pages lack a standard meta description; the home sharing description is empty. Configure Blogger search descriptions and recheck the output.
- `/robots.txt` allows general crawling of public articles and excludes `/search` and `/share-widget`; it advertises `/sitemap.xml`.
- The sitemap responds successfully with a populated XML URL set. Its `X-Robots-Tag: noindex` applies to the sitemap response and does not establish that articles are excluded.

These observations do not establish actual search indexing, AI citations or performance. No published settings or content were changed during this audit.
