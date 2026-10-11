# Release validation — 2026-10-11

[English](VALIDATION.md) · [Português](../VALIDATION.md)

## Automated checks

Thirteen regression tests cover malformed widget sections, duplicate IDs, missing includes, locale equivalence, metadata ownership and HTML SEO auditing. Both XML variants parse; locale generation is current; local Markdown links and Git whitespace checks pass. GitHub CI repeats these checks and builds the preview. External documentation links and heading anchors are not checked automatically.

## Responsive preview evidence

- Home and article DOM measured at 320, 360, 480, 600, 768, 900, 1050 and 1440 px without horizontal page overflow.
- Long unbroken titles, URLs, tables and code checked at 320, 360, 768 and 1440 px; scrolling remains contained.
- Editable post example, figure and empty 16:9 iframe checked at 320, 360, 768 and 1440 px. Media stays within the reading column.
- Privacy page checked at 320, 768 and 1440 px: one H1, WebPage microdata, current menu link highlighted and working navigation to Contact.
- The home fixture contains three opening cards plus one distinct list entry.

## Limits and next checks

These are CSS/DOM fixture checks, not a Blogger compiler. Import, native data bindings, gadgets, comments, pagination and published structured data remain unverified. Screenshot capture was unavailable, and remote font faces were not confirmed loaded; measurements reflect fallback typography. No Core Web Vitals or ranking claims are established.

The release is an alpha until the [platform checklist](ROADMAP.md) is completed. Use [SEO.md](SEO.md) for published HTML auditing and [RELEASE.md](RELEASE.md) for package contents and installation.
