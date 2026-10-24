# Balaio — Free minimal Blogger theme

> **Candidate on this branch: rc.14, without a validated Blogger import yet.** The recommended main version remains rc.13. [Reference navigation proposal](docs/en/REFERENCE.md).


**Recommended version: rc.13 on main.** Optional native contact is included: paste a short content marker into your Contact page to enable it, with any page URL. No per-blog XML editing is required. Search, navigation and home continuation are preserved. [Contact guide](docs/en/CONTACT.md).

**[English](README.md) · [Português brasileiro](README.pt-BR.md)**

A **free Blogger XML template**: minimal, responsive, open source and easy to customize. Original editorial design with pastel green, sand and blue, readable typography and a technical SEO foundation for personal blogs and science communication.

**MIT licensed.** Use, modify and redistribute it, including for commercial projects. Keep the copyright and license notices with copies or substantial portions of the code. No visible site credit or paid permission is required by MIT. The software is provided without warranty. [Read the license](LICENSE) · [MIT explained by OSI](https://opensource.org/license/mit).

> **Default template:** `v0.2.0-rc.13`. [Download Portuguese XML](https://raw.githubusercontent.com/erickfaria/balaio-theme/main/theme/balaio.xml) · [Download English XML](https://raw.githubusercontent.com/erickfaria/balaio-theme/main/theme/balaio.en.xml) · [Validation evidence](docs/en/VALIDATION.md). Use these main-branch templates; older release packages contain different versions.
>
> **Earlier fallback:** [v0.1.0](https://github.com/erickfaria/balaio-theme/releases/tag/v0.1.0), with confirmed import but without the current home continuation and layout.

**GitHub Actions is enabled.** Pull requests, pushes to main and version tags validate the theme and build downloadable XML, install ZIP, checksums and preview artifacts. Local checks remain available. [Maintenance policy](https://github.com/erickfaria/balaio-theme/blob/main/MAINTAINERS.md).

## Choose your language

| Interface | Template |
| --- | --- |
| Brazilian Portuguese | [theme/balaio.xml](theme/balaio.xml) |
| English | [theme/balaio.en.xml](theme/balaio.en.xml) |

Set your Blogger blog language to match your chosen interface. Post content is yours and is not translated by the theme.

## Install on Blogger

No build tools are needed to install the theme.

1. Download the main-branch XML for your chosen language using the links above. No ZIP extraction or build is required.
2. Choose a **test blog** in Blogger. Back up the current theme from **Theme → menu → Back up**.
3. Open **Theme → menu → Edit HTML**. Replace the editor contents with the entire selected XML file, then save.
4. Configure your title, description and language in **Settings**.
5. Published pages automatically supplement the top menu. **Layout → Pages** sets leading links, their labels and order; **Menu** adds extra links. For a fully manual menu, set `data-auto-pages='false'` on the navigation element. [Page navigation](docs/en/PAGES.md).
6. Edit **Introduction** (English) or **Apresentação** (Portuguese) to change the opening text. Use Menu links for topics; this layout has no sidebar.
7. Start with 10 posts per home page under **Settings → Posts**; Blogger may paginate earlier. Check articles, pages, search, pagination and comments on mobile and desktop before moving to your main blog.

**Optional contact form:** create/edit a Contact page and paste the [ready-to-use HTML sample](examples/pages/contact.en.html). Keep `class="balaio-contact-page"` to show the built-in form; no fixed URL or template editing. [Three-step setup](docs/en/CONTACT.md).

[Performance guide](docs/en/PERFORMANCE.md) · [Home-page posts and pagination](docs/en/HOME.md) · [Detailed setup and troubleshooting](docs/en/INSTALLATION.md) · [Customization](docs/en/CUSTOMIZATION.md)

## What is included

- Two opening cards for the latest home-page posts, followed by an editorial list. When Blogger returns a short page, a small built-in script follows native pagination toward 10 posts, without duplicate entries.
- Responsive layouts for phones, tablets and desktop; optional thumbnails and full-width entries when no image is available.
- Native Blogger search in an icon-only disclosure, label links, pagination, article and static-page layouts. Click/tap the magnifier or press Enter/Space, then Tab to the field; toggle it again to close.
- Basic comment display and a link to add a comment; embedded forms and threaded replies remain pending.
- Editable introduction, automatic published-page navigation and extra Menu links; no sidebar and one header search.
- Keyboard focus, skip link, contained code/table scrolling and print styles.
- **Inter** for interface and **Newsreader** for titles and reading, served by Google Fonts with local fallbacks and `display=swap`. Post/page text defaults to 22px with a 1.75 line height. Both fonts use SIL OFL 1.1; their licenses remain separate from MIT.
- No third-party JavaScript libraries or Python package dependencies. The home continuation and page-menu enhancement are original MIT code; native pagination works without JavaScript.

Native color/font controls are included in the candidate; live Designer verification remains pending. A logo image and a dedicated 404 layout are not implemented yet. The preview is a visual fixture using real theme CSS; it does not compile Blogger expressions.

## Develop locally

Requires Python 3.10+; `make` is optional. Node.js 22+ runs JavaScript syntax and continuation startup checks; they are skipped locally without Node. CI includes Node. Installation needs neither Python nor Node.

```sh
python3 scripts/validate_docs.py
python3 scripts/build_locales.py --check
python3 scripts/validate_theme.py
python3 -m unittest discover -s tests -v
python3 scripts/build_preview.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory preview
```

Open `http://127.0.0.1:8765`. Stop the server with Ctrl+C. With Make installed, use `make check` and `make serve`. After editing the Portuguese source, run `make locales` or `python3 scripts/build_locales.py` to regenerate the English XML.

## Repository guide

| Path | Purpose |
| --- | --- |
| `theme/` | Installable XML templates; Portuguese is the source for the English variant |
| `examples/` | Editable post body samples in English and Portuguese |
| `scripts/` | Locale generation, XML validation and local preview |
| `tests/` | Validator regression checks |
| `docs/` / `docs/en/` | Portuguese / English guides and project notes |
| `licenses/` | Original font license notices |
| `.github/` | CI, issue and pull request templates |
| `preview/` | Generated local files, excluded from Git |

[Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md) · [Design](docs/en/DESIGN.md) · [Roadmap](docs/en/ROADMAP.md) · [Validation](docs/en/VALIDATION.md) · [Credits and third-party licenses](docs/en/PROVENANCE.md)

Backups, credentials and private blog content are excluded from distribution. Fonts keep their OFL licenses; your posts and images keep their own rights. The GitHub workflow validates templates, translations and preview generation; a green check does not confirm a successful Blogger import.

## SEO and AI discovery

The theme preserves Blogger metadata and adds visible-content article microdata. Follow the [SEO setup and audit guide](docs/en/SEO.md) to configure search descriptions, indexing and crawler access. Includes a dependency-free HTML auditor; rankings and AI citations are not guaranteed.

## Frequently asked questions

**Is this Blogger template really free?** Yes. MIT permits personal and commercial use, modification and redistribution with license notices preserved. No purchase or visible attribution is required.

**Can I change colors and layout?** Yes. Start with Layout gadgets and the native color/font controls. Reading width remains an advanced CSS option. [Customization guide](docs/en/CUSTOMIZATION.md).

**Is it built for SEO?** It provides native Blogger metadata, semantic headings, ordinary crawlable links and article microdata. The [search guide](docs/en/SEO.md) covers Google, Bing, DuckDuckGo, SearXNG and AI discovery. Published indexing and compatibility still need verification.

**How do I write responsive posts?** Use the [post guide and editable HTML sample](docs/en/POSTS.md). Titles, summaries, tables, images and video stay within the reading layout without requiring scripts in your posts.

## Basic pages

[About, Contact and Privacy samples](docs/en/PAGES.md): About/Privacy use Lorem ipsum; Contact includes a simple opt-in for the native form. [Contact setup](docs/en/CONTACT.md). XML does not create pages or replace their content. Original code is MIT; Inter/Newsreader are SIL OFL.

## Contribute through pull requests

Public forks and contributions are welcome. Contributor changes to `main` require CI and maintainer review; only `@erickfaria` integrates changes. See the [maintenance policy](https://github.com/erickfaria/balaio-theme/blob/main/MAINTAINERS.md) and [contribution guide](CONTRIBUTING.md).

## Reference content — in development

The `feat/guides-navigation-authors` branch prepares an optional **Guides and projects** strip, native header topic disclosure, a long-guide sample and an author byline with an optional profile photo. No extra JavaScript. [Proposal, setup and validation limits](docs/en/REFERENCE.md). Main remains recommended until the candidate is reviewed and imported.
