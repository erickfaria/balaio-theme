# Native Blogger contact — rc.11

[English](CONTACT.md) · [Português](../CONTACT.md)

The theme includes **ContactForm1**, a native Blogger widget with an original minimal, responsive design. Visitors do not need to sign in: name is optional; email and message are required. This is not complete anonymity: recipients receive the supplied email address and Blogger processes delivery.

## One-time setup per blog

1. Back up and import the updated XML in your preferred language. Retain rc.10 while confirming the new installation.
2. Select your blog language in **Settings**. Theme labels follow the chosen XML; native delivery/error messages follow Blogger’s language.
3. Under **Pages → New page**, create **Contact** (English) or **Contato** (Portuguese). Reuse an existing page if available.
4. In HTML view, copy only the body of [contact.en.html](../../examples/pages/contact.en.html) or [contact.pt-BR.html](../../examples/pages/contact.pt-BR.html). The generic text is editable. Do not paste a second form, a complete document or the theme XML.
5. Publish and check the path: **`/p/contact.html` or `/p/contato.html`**. The theme displays the form on these static pages, not on the home, posts, search or other pages. Automatic navigation discovers the published page on reload.
6. Open the public page and confirm delivery to your own inbox, including spam. Local checks do not send email or establish Blogger delivery.

The condition compares canonical page and blog URLs, keeping contact available with mobile parameters such as `?m=1`.

The XML installs the widget and its layout; **it does not create page records**. Publishing the page in the dashboard is the only content step required. The theme does not replace an existing page or change its text. [Create Blogger pages](https://support.google.com/blogger/answer/165955?hl=en).

## Delivery and operation

No recipient, API key, password or fixed token is embedded in the theme. Blogger generates session data and determines the destination from the blog and its configuration. Check the blog account and administrators when validating delivery. Balaio does not include the recipient’s address in its HTML.

Delivery requires **Blogger’s native JavaScript**, including its session data. Do not copy just the form HTML into a post/page or remove ContactForm1 or the native theme scripts. Name/email support autofill; labels are associated with inputs; errors and status use accessible live regions. With JavaScript disabled, a note explains that the form needs it.

There is no iframe, paid form service or added delivery library. Balaio does not send messages itself or register forms with external providers. [Blogger community guidance about widget/session data](https://support.google.com/blogger/thread/252064400/how-to-edit-contact-form-gadget-texts?hl=en).

## Different path or disabling

For a path such as `/p/get-in-touch.html`, edit only the paths in **ContactForm1**’s `cond` attribute, preserving `data:blog.pageType == "static_page"`. Do not change **Blog1**’s condition or includes. No fixed domain is needed. See [PAGES.md](PAGES.md) for manual navigation.

To disable, remove **Contact form** in Layout. If a blog already has an older ContactForm, keep one widget and check IDs after importing to avoid duplicate registrations. Retain customizations before reimporting XML.

## Code, privacy and validation

Original markup, CSS and samples are MIT. **Blogger/Google’s delivery, abuse protection, JavaScript and infrastructure are external services**, not open-source code distributed or licensed by this repository. No copy of that library is included in the package. Inter and Newsreader retain SIL OFL.

The form includes a note about Blogger processing. Adapt the blog’s privacy page to the actual use of contact; the privacy sample remains a placeholder. The theme adds no message store, analytics or trackers to the form.

Local previews disable Send and make no contact requests. They check layout, languages, labels, fields and illustrative feedback states. **rc.11 import and delivery still require confirmation on Blogger.** [Evidence and limits](VALIDATION.md).
