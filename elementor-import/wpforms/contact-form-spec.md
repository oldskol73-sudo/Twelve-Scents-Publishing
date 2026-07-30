# WPForms Field Specification — Contact Page

This replaces the placeholder `{{ goContact }}` / `{{ submitForm }}` mockup contact functionality
from `index.html`'s Contact screen (`sc-if value="{{ isContact }}"`). Build this as a real WPForms
form and embed it on the Contact page (via the Elementor WPForms widget, or the WPForms block/shortcode)
in place of the placeholder text block left in `elementor-import/pages/contact.json`.

## Form name
**Contact Us — Twelve Scents Publishing**

## Fields (in order, matching the source mockup's form)

| # | Field Type | Label | Placeholder | Required | Notes |
|---|-----------|-------|-------------|----------|-------|
| 1 | Single Line Text | Name | "Your full name" | Yes | Maps to source `formName` |
| 2 | Email | Email | "you@email.com" | Yes | Maps to source `formEmail` |
| 3 | Phone | Phone | "(888) 212-1212" | No | Maps to source `formPhone`; source mockup did not mark phone required |
| 4 | Paragraph Text | Message | "How can we help?" | Yes | Maps to source `formMessage`; use a 5-row textarea to match source `rows="5"` |
| 5 | Checkbox (single) | I agree to be contacted about my inquiry | — | No (recommended, not in source) | Not present in the original mockup — recommended addition for consent/GDPR-style compliance; add only if the site owner wants it |

## Submit button
Label: **Send Message**

## Confirmation behavior
On successful submit, show a "Thank You" confirmation message matching the source mockup's success
state:

> **Thank you!**
> Your message is on its way. We'll be in touch within one business day.

Configure this as a WPForms "Message" confirmation type (no redirect needed) to mirror the mockup's
in-place `sent` / `notSent` toggle.

## Notifications
Send a notification email to `salessupport@twelve12scents.com` (the address shown throughout the
site's Contact section and footer) with all submitted field values.

## Placement
Embed the form inside the left column of the two-column Contact layout described in
`elementor-import/pages/contact.json`, replacing the `form_placeholder` container's note text block.
The right column (email/phone/address/social links/map) is already built natively in that same file.

## One-line note
This WPForms form fully replaces the JS-only `{{ goContact }}` / `submitForm` contact functionality
from the static HTML mockup — no custom code is needed once the form above is built and embedded.
