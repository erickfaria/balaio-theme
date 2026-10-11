# Install and upgrade — v0.2.0-rc.4

[English](RELEASE.md) · [Português](../RELEASE.md)

[Download candidate on GitHub](https://github.com/erickfaria/balaio-theme/releases/tag/v0.2.0-rc.4).

This is a **performance release candidate**. Twenty-four local checks pass without GitHub Actions. The owner confirmed rc.3 continuation; rc.4 needs a fresh import, including the conditional sidebar and native controls/widgets. [v0.1.0 remains the stable fallback](https://github.com/erickfaria/balaio-theme/releases/tag/v0.1.0). See [validation evidence](VALIDATION.md).

## What changed

- Smaller variable-font CSS, covering intermediate interface weights; Inter/Newsreader remain SIL OFL.
- Home continuation after initial loading and an idle opportunity, with a low-priority hint.
- Sidebar omitted from articles/pages, avoiding HTML previously sent and hidden by CSS.
- Appended links without `m`, preserving other parameters; parsing scoped to `Blog1`.
- Bilingual [performance guide](PERFORMANCE.md), measurements and limits. Actions remains disabled; checks run locally.

- Hotfix for rc.2: Blogger retained raw CDATA markers in the home script, causing `Unexpected token '<'` and preventing the extra post list. The markers are now JavaScript comments; previews retain them and local checks test both serializations.

- 22px post/page text, 1.75 line height, clearer H2/H3 sizes and the same open Inter/Newsreader fonts.
- Compact mobile header and topic list, native Pages at the top and corrected mobile search.
- Native pastel color/font controls; no visible footer, Profile or Attribution blocks.
- Two opening cards followed by a list supplemented through native pagination: a ten-post target, up to four extra requests and no duplicates. [Home behavior and settings](HOME.md).

## Assets

| File | Use |
| --- | --- |
| `balaio-0.2.0-rc.4.zip` | Install package: templates, bilingual guides, page/post examples, version, changelog and MIT/OFL notices |
| `balaio.xml` | Portuguese interface |
| `balaio.en.xml` | English interface |
| `SHA256SUMS.txt` | SHA-256 checksums for the three assets above |

The ZIP extracts into `balaio-0.2.0-rc.4/`. Select an XML inside `theme/`; do not upload the ZIP as a Blogger theme. The install package excludes development scripts, development tests, backups and generated previews. GitHub's automatic source archives include tracked development files.

## Upgrade from v0.1.0

1. Back up your current Blogger XML and record custom gadgets, links and Designer values. Use a separate test blog first.
2. In **Theme → menu → Edit HTML**, paste the complete candidate XML in the chosen language and save. The CSS source comment identifies `v0.2.0-rc.4`.
3. In **Layout → Pages**, select published About me, Contact and Privacy pages and check gadget placement. **Menu** is for extra links. Create page content through Pages; XML does not create or replace those records.
4. Review Introduction and sidebar gadgets. Footer links are no longer rendered: move necessary links to Pages/Menu before updating. Inherited Profile/Attribution blocks are hidden.
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
