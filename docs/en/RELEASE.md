# Install release v0.1.0-alpha.1

[English](RELEASE.md) · [Português](../RELEASE.md)

[Download on GitHub](https://github.com/erickfaria/balaio-theme/releases/tag/v0.1.0-alpha.1).

This is an **experimental prerelease**, not a platform-verified stable theme. XML validation, thirteen local tests and CI pass; Blogger import still needs testing. See [known limits](../../CHANGELOG.md) and [validation evidence](VALIDATION.md).

## Assets

- `balaio-0.1.0-alpha.1.zip`: install package with both templates, page/post examples, bilingual documentation, version, changelog and license notices. No development tests, scripts, backup files or generated previews.
- `balaio.xml`: Portuguese interface.
- `balaio.en.xml`: English interface.
- `SHA256SUMS.txt`: checksums for the ZIP and both XML files.
- GitHub's automatic source archives: complete tracked development source, including useful scripts and tests.

The ZIP extracts into `balaio-0.1.0-alpha.1/`. Choose an XML from `theme/`; don't upload the ZIP as a Blogger theme. Standalone XML assets contain the same templates. Use the package if you also want examples and complete license notices.

## Quick installation

1. Back up your existing theme and use a separate test blog.
2. In **Theme → Edit HTML**, paste the complete chosen XML and save.
3. Set the blog language, title and descriptions. Configure Introduction, Menu and Footer links in Layout.
4. Create your basic pages using [PAGES.md](PAGES.md); placeholders are layout samples to replace before publishing.
5. Check home, articles, pages, search, pagination and comments on phone and desktop. Follow [INSTALLATION.md](INSTALLATION.md) and [SEO.md](SEO.md).

Optional integrity check after downloading the three assets and checksum file into one directory:

```sh
sha256sum -c SHA256SUMS.txt
```

## Licenses and services

Original code, design and examples are MIT. Inter and Newsreader are SIL OFL 1.1; preserve their notices when distributing font files. Google Fonts hosting is optional; Blogger is an external platform. [Resource inventory](PROVENANCE.md).

## Reproduce the package

From the matching Git tag, with Python 3.10+ and Git:

```sh
make check
python3 scripts/build_release.py --output /tmp/balaio-release
```

The script uses a tracked-file allowlist and produces deterministic archive entries and SHA-256 checksums. Keep release outputs outside the repository or in ignored `dist/`. Do not publish artifacts from an uncommitted checkout.
