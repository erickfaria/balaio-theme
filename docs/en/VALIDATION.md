# Release validation — 2026-10-11

[English](VALIDATION.md) · [Português](../VALIDATION.md)

## Blogger import confirmed

On October 11, 2026, the project owner reported successful import and explicitly approved promotion to stable `v0.1.0`. This is maintainer-reported platform evidence. The language variant and complete widget test results were not recorded, so it is not a claim that both variants or every behavior were independently tested. The XML templates are unchanged from the imported alpha.

## Automated checks

Thirteen regression tests cover malformed widget sections, duplicate IDs, missing includes, locale equivalence, metadata ownership and HTML SEO auditing. Both XML variants parse; locale generation is current; local Markdown links and Git whitespace checks pass. GitHub CI repeats these checks and builds the preview. External documentation links and heading anchors are not checked automatically.

## Responsive preview evidence

- Home and article DOM measured at 320, 360, 480, 600, 768, 900, 1050 and 1440 px without horizontal page overflow.
- Long unbroken titles, URLs, tables and code checked at 320, 360, 768 and 1440 px; scrolling remains contained.
- Editable post example, figure and empty 16:9 iframe checked at 320, 360, 768 and 1440 px. Media stays within the reading column.
- Privacy page checked at 320, 768 and 1440 px: one H1, WebPage microdata, current menu link highlighted and working navigation to Contact.
- The home fixture contains three opening cards plus one distinct list entry.

## Limits and next checks

These are CSS/DOM fixture checks, not a Blogger compiler. Import is confirmed by the owner. Full testing of native data, gadgets, comments, pagination and published structured data remains pending. Screenshot capture was unavailable, and remote font faces were not confirmed loaded; measurements reflect fallback typography. No Core Web Vitals or ranking claims are established.

The owner authorized stable status after import confirmation; the remaining [platform checklist](ROADMAP.md) documents follow-up testing. Use [SEO.md](SEO.md) for published HTML auditing and [RELEASE.md](RELEASE.md) for package contents and installation.
