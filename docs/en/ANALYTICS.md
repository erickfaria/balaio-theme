# Optional Google Analytics

[English](ANALYTICS.md) · [Português](../ANALYTICS.md)

Starting with rc.16, both XMLs use Blogger's native integration with Google Analytics 4 (GA4). The theme reads the ID configured by the owner in the blog Settings. It contains neither a demo ID nor an author's ID.

## Enable

1. In Google Analytics, create a GA4 property and a Web data stream for your blog. Copy its **Measurement ID**, starting with `G-`.
2. Install the updated Balaio XML in your chosen language. [Installation](INSTALLATION.md).
3. In Blogger, open **Settings → Basic → Google Analytics Measurement ID**, paste your `G-…` ID and save.
4. Visit your public blog and check Analytics' **Realtime** report. Data may take some time to appear; blockers and your consent choices may also prevent delivery.

If you already added an Analytics snippet or Tag Manager manually for the same property, choose a single installation path to avoid duplicate events. The native integration does not require pasting Google's code into the XML or an HTML/JavaScript gadget.

[Google's Blogger setup instructions](https://support.google.com/analytics/answer/14854594?hl=en) · [Blogger Analytics help](https://support.google.com/blogger/answer/7039627?hl=en).

## Behavior and disabling

The global call is placed just before the closing `body`, outside the gadgets and theme scripts:

```xml
<b:if cond='data:blog.analyticsAccountNumber'>
  <b:include data='blog' name='google-analytics'/>
</b:if>
```

Without a configured ID, this call is not executed. To disable the integration, clear the ID in Blogger Settings. Home, posts, pages and search use the same call; no per-post setup is needed. It does not change Blogger's own dashboard statistics.

Blogger provides and maintains the tracking code; the repository does not copy it or distribute another library. The [native include](https://blogger-developers.googleblog.com/2011/10/today-we-have-made-change-to-layouts.html) connects to the platform; Google's help above documents the current GA4 setup.

## Performance, data and validation

When enabled, Analytics adds external JavaScript and requests to Google. Without an ID, the base retains its previous behavior, with no Analytics added by this integration. No CSS, fonts, gadgets or custom scripts were added. Google Analytics retains its own terms and is not part of the MIT code distributed by this repository.

Update your Privacy text to describe the services you choose to use. The theme does not configure consent or replace controls your installation may require.

Local checks validate XML, locales, packaging and preservation of scripts/gadgets. They do not execute Blogger's include or prove data collection. Import and actual events reaching a real property must be checked after setup. The local preview does not load Analytics.
