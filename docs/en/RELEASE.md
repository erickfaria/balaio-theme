# Install and upgrade — v0.2.0-rc.17

[English](RELEASE.md) · [Português](../RELEASE.md)

**v0.2.0-rc.17** simplifies the header and homepage, consolidates Topics into the navigation and sets the reading default to 24px. The Pages widget supplies the menu in the initial HTML. Automatic discovery is optional. [Menu configuration](PAGES.md).

An article or static page puts its title first. Blogger supplies canonical links and search descriptions. Responsive thumbnail candidates use 320w and 640w when available. The short-home continuation runs at low priority, and the legacy sidebar section is reserved for the Layout editor. [SEO](SEO.md) · [Performance](PERFORMANCE.md).

Use a separate test blog before updating production. [Release downloads](https://github.com/erickfaria/balaio-theme/releases/tag/v0.2.0-rc.17) · [Validation](VALIDATION.md).

## Other features

- Two highlighted posts and native pagination. A short home can fetch up to four additional pages toward a total of ten posts. [Home](HOME.md)
- Native search, configurable appearance, optional contact and Analytics when configured in Blogger. [Customization](CUSTOMIZATION.md) · [Contact](CONTACT.md) · [Analytics](ANALYTICS.md)
- Inter and Newsreader under SIL OFL 1.1, plus MIT-licensed theme and examples. [Provenance](PROVENANCE.md)

## Candidate build assets

| File | Use |
| --- | --- |
| `balaio-0.2.0-rc.17.zip` | Install package: templates, bilingual guides, HTML/Markdown page and material examples, version, changelog and MIT/OFL notices |
| `balaio.xml` | Portuguese interface |
| `balaio.en.xml` | English interface |
| `SHA256SUMS.txt` | SHA-256 checksums for the three assets above |

The ZIP extracts into `balaio-0.2.0-rc.17/`. Select an XML inside `theme/`; do not upload the ZIP as a Blogger theme. The install package excludes development scripts, development tests, backups and generated previews. GitHub's automatic source archives include tracked development files.

## Upgrade from an earlier version

1. Back up your current Blogger XML and record custom gadgets, links and Designer values. Use a separate test blog first.
2. In **Theme → menu → Edit HTML**, paste the complete candidate XML in the chosen language and save. The CSS source comment identifies `v0.2.0-rc.17`.
3. Review the links in **Layout → Pages** and use **Menu** for extra links. If you relied on feed-discovered links, add them to the gadget or [enable automatic mode](PAGES.md#optional-automatic-pages). Create page content through Pages.
4. Review the Introduction, Topics and any legacy widgets in Layout. Move any links you still need into Pages or Menu. Shorten a saved Introduction if you want the compact homepage.
5. In **Theme → Customize → Advanced**, check colors and **Post and page font**. Saved settings may retain an old size; choose 24px if needed. Reading width and pastel defaults remain documented in [CUSTOMIZATION.md](CUSTOMIZATION.md).
6. If a separate legacy mobile theme appears, choose **Desktop** under Mobile settings. The theme itself adapts to phone width. Start with ten posts under **Settings → Posts**; Blogger may paginate earlier. See [INSTALLATION.md](INSTALLATION.md).
7. Check that home continuation fills the list and that the older-posts link resumes correctly. Test home, full articles, static pages, search, pagination and comments before updating your main blog. Restore your backup to roll back presentation if necessary.

Your posts, images and URLs are not migrated by this theme. Keep customized XML backups outside the repository. Do not overwrite the existing stable tag or assets when preparing a future stable release.

### Check the imported theme

In a test blog, check the title, canonical URL and description on the home page, an article and a static page, including `?m=1`. Test the Topics disclosure by keyboard, search, the native older-posts link and both thumbnail sizes. Review legacy widgets in Layout. [SEO auditor](SEO.md) · [Validation checklist](VALIDATION.md).

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

## Configure web materials

In **Layout → Guides and projects**, select up to three published URLs, such as your Library, handbook or project. **Topics** configures header labels. [Models and the publishing contract](MATERIALS.md) cover ordinary HTML and Markdown-generated indexes. Importing the XML does not create content or change schedules. The optional author photo depends on fields exposed by Blogger.

Use the [short Layout setup](LAYOUT.md) to select five to seven topics, a few menu links and up to three highlights. The theme imposes no category names and does not automatically cut configured links.
