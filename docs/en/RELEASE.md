# Install and upgrade — v0.2.0-rc.10

[English](RELEASE.md) · [Português](../RELEASE.md)

rc.10 changes only search: the field opens to the left of the magnifier on the same row, without a duplicate icon. A small arrow submits. On phones, opening temporarily uses the title space; closing restores it without changing header height. Native script-free disclosure, layout, pages, widgets and continuation from rc.9 are preserved. Fresh rc.10 import verification is pending. [Download Portuguese XML](https://raw.githubusercontent.com/erickfaria/balaio-theme/main/theme/balaio.xml) · [Download English XML](https://raw.githubusercontent.com/erickfaria/balaio-theme/main/theme/balaio.en.xml). Use the current main XML; older packages contain other versions. [Validation](VALIDATION.md) · [Automatic/manual modes](PAGES.md).

## What this version preserves

- Two highlights followed by older posts, with rc.3 widget bodies and script. Ten-post target, up to four extra pages, deduplication and native pagination fallback. [Home](HOME.md).
- Pages navigation, extra menu links, header search, 22px reading text and color/font controls.
- Open SIL OFL Inter/Newsreader fonts, sidebar-free pastel layout and compact report-abuse footer.
- Active CI checks and install artifacts. Portuguese import and continuation are confirmed; previews do not compile Blogger XML.

## Candidate build assets

| File | Use |
| --- | --- |
| `balaio-0.2.0-rc.10.zip` | Install package: templates, bilingual guides, page/post examples, version, changelog and MIT/OFL notices |
| `balaio.xml` | Portuguese interface |
| `balaio.en.xml` | English interface |
| `SHA256SUMS.txt` | SHA-256 checksums for the three assets above |

The ZIP extracts into `balaio-0.2.0-rc.10/`. Select an XML inside `theme/`; do not upload the ZIP as a Blogger theme. The install package excludes development scripts, development tests, backups and generated previews. GitHub's automatic source archives include tracked development files.

## Upgrade from v0.1.0

1. Back up your current Blogger XML and record custom gadgets, links and Designer values. Use a separate test blog first.
2. In **Theme → menu → Edit HTML**, paste the complete candidate XML in the chosen language and save. The CSS source comment identifies `v0.2.0-rc.10`.
3. Check published pages in automatic navigation. **Layout → Pages** sets leading links and order; use [manual mode](PAGES.md) to choose only some pages. **Menu** is for extra links. Create page content through Pages; XML does not create or replace those records.
4. Review Introduction and menu links. The legacy sidebar is hidden through CSS. Footer links are no longer rendered: move necessary links to Pages/Menu before updating. Inherited Profile/Attribution blocks are hidden.
5. In **Theme → Customize → Advanced**, check colors and **Post and page font**. Saved settings may retain an old size; choose 22px if needed. Reading width and pastel defaults remain documented in [CUSTOMIZATION.md](CUSTOMIZATION.md).
6. If a separate legacy mobile theme appears, choose **Desktop** under Mobile settings. The theme itself adapts to phone width. Start with ten posts under **Settings → Posts**; Blogger may paginate earlier. See [INSTALLATION.md](INSTALLATION.md).
7. Check that home continuation fills the list and that the older-posts link resumes correctly. Test home, full articles, static pages, search, pagination and comments before updating your main blog. Restore your backup to roll back presentation if necessary.

Your posts, images and URLs are not migrated by this theme. Keep customized XML backups outside the repository. Do not overwrite the existing stable tag or assets when preparing a future stable release.

## Verify downloads

Download the three assets and checksum file into one directory:

```sh
sha256sum -c SHA256SUMS.txt
```

## Licenses and reproducible packaging

Original code/design/examples are MIT. Inter and Newsreader are SIL OFL 1.1; notices remain in `licenses/`. Google Fonts is optional hosting and Blogger is an external platform. [Resource inventory](PROVENANCE.md).

From the matching Git tag, with Python 3.10+, Node.js 22+ (syntax checks) and Git:

```sh
make check
python3 scripts/build_release.py --output /tmp/balaio-release
```

The builder requires a clean committed checkout, uses a tracked-file allowlist and deterministic ZIP entries, and creates SHA-256 checksums. Keep generated assets outside the repository or in ignored `dist/`.
