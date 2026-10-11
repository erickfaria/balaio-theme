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

## Bing, DuckDuckGo and open-source metasearch

The theme exposes ordinary HTML text, links and article microdata without requiring theme JavaScript. It does not restrict a crawler by vendor. Crawl permissions belong to Blogger's robots.txt, robot headers and any domain firewall, not to a theme-specific allowlist.

| Search service | Discovery path | Publisher action |
| --- | --- | --- |
| Bing | Bingbot and Bing indexing | Verify in Bing Webmaster Tools, submit the sitemap and inspect public URLs. |
| DuckDuckGo | DuckDuckBot plus other sources, with traditional results largely from Bing | Check access for DuckDuckBot and Bingbot; no special theme tag is required. |
| SearXNG | Open-source metasearch combining its instance's selected engines | Make posts discoverable in those upstream sources; results vary by instance. |
| Other independent crawlers | Their own indexing and robots policies | Keep public HTML and normal links accessible; inspect their published crawler guidance. |

Sources: [Bing crawler controls](https://www.bing.com/webmasters/help/how-to-create-a-robots-txt-file-cb7c31ec), [DuckDuckGo search sources](https://duckduckgo.com/duckduckgo-help-pages/results/sources), [SearXNG documentation](https://docs.searxng.org/).

SearXNG is open source; Bing and DuckDuckGo are not described here as open-source search engines. Do not add invented `SearXNG-bot` rules or copy separate bot groups blindly: specific groups can replace a wildcard group's restrictions. The HTML audit reports scoped restrictions for Googlebot, Bingbot, DuckDuckBot and OAI-SearchBot; robots.txt still requires a separate check.

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
