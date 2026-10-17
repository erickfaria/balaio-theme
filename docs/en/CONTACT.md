# Contact with simple opt-in — rc.13

[English](CONTACT.md) · [Português](../CONTACT.md)

Both theme XML files already include the native contact widget in its own area outside the hidden sidebar. **Create or edit your Contact page and paste the content below in HTML view.** No template-line editing, extra gadget or special URL is required.

## Enable in three steps

1. Import the current theme XML in your preferred language. Retain your previous theme when upgrading.
2. Under **Blogger → Pages**, open your existing Contact page or create one. Select **HTML view** and paste:

```html
<p>Have a question, suggestion or proposal?</p>
<p class="balaio-contact-page">Fill out the form below to get in touch.</p>
```

3. Publish or update the page and open its public URL. Send a test message and check delivery, including spam.

The same content is in [contact.en.html](../../examples/pages/contact.en.html); [contact.pt-BR.html](../../examples/pages/contact.pt-BR.html) is the Portuguese version. The theme provides H1 and the fields. You may edit the wording: **keep `class="balaio-contact-page"` on an element in the page body**.

Any page name and URL works, including numeric suffixes. Do not delete, recreate or rename a page to obtain `/p/contact.html`. Importing XML does not create page records or modify their content. [Blogger page instructions](https://support.google.com/blogger/answer/165955?hl=en).

## What appears

- Optional name, required reply email and required message.
- Associated labels, visible focus, accessible error/success feedback and a rounded button.
- A responsive column using the theme palette and interface font. The marked page hides the return link that would otherwise precede the form.
- No login screen added by the theme. Check behavior and delivery in a private window too; processing and abuse protection are controlled by Blogger.

Activation uses CSS `:has()`, already used by theme search, in current browsers. Delivery requires the native JavaScript and session data that Blogger injects for `ContactForm1`. The theme does not copy that library, implement an email service or require an API key/password. Keep Blogger’s standard JavaScript enabled. [Widget structure](https://support.google.com/blogger/answer/46888?hl=en) · [Gadget guidance](https://support.google.com/blogger/answer/176245?hl=en).

## Disable or use another channel

Remove `balaio-contact-page` from your page content to hide the form. Keep the page with your own contact channels or a separately configured form if preferred. Do not add a second `ContactForm1` or move this gadget into the hidden legacy sidebar.

Use the class only in **Pages**, not posts. The widget renders only on static pages; it is not included on home or individual posts. Pages without the class keep the form hidden.

## Upgrade from rc.11/rc.12 or manual edits

Download the complete current main XML and update the theme. On your existing Contact page, replace the old text reference with the snippet above. Do not paste `<b:section>` or `<b:widget>` into the page editor; those elements are now included in repository XML.

rc.13 defines the complete `ContactForm1` in `contactpage`, outside `sidebar`, without domain/URL conditions. If **Restore** retains an old widget position, condition or body, use **Theme → Edit HTML**, replace the editor with the entire current XML and save. Check `balaio-version` is `0.2.0-rc.13`, the public page and a real delivery. Do not reimport posts to repair presentation.

## Data and validation

Blogger processes email and message data to forward inquiries to the blog administrators. Update your privacy policy for the actual configuration; the repository’s privacy example is not a replacement for that disclosure.

Local examples disable sending and do not load Google transport. They check appearance and opt-in, not inbox delivery. Fresh import and delivery still need confirmation on Blogger. [Evidence and limits](VALIDATION.md).

Original code/examples are MIT; Inter/Newsreader retain SIL OFL. Blogger is an external service with its own terms.
