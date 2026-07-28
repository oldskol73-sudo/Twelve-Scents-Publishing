# Elementor Import Kit — Twelve Scents Publishing

This folder converts the static-HTML/proprietary-templating mockup in the repo root (`index.html`,
`blog.html`, and the eight individual book/article pages) into native-Elementor, Container-based
template JSON files, ready for manual import into a WordPress + Elementor + XPRO + WPForms site.

## What's in here

```
elementor-import/
  README.md                        ← this file
  pages/                           ← 14 page templates (Elementor "single template" export JSON)
    home.json
    about.json
    shop.json
    listings.json
    contact.json
    blog.json
    meet-abraham.json
    isaac-the-promised-son.json
    jacobs-journey.json
    sarahs-obedience.json
    men-of-valor.json
    daughters-of-scripture.json
    why-1611-kjv.json
    reading-the-word-together.json
  header-footer/                   ← 2 templates for the XPRO header/footer builder
    header.json
    footer.json
  wpforms/
    contact-form-spec.md           ← exact WPForms field list for the Contact page form
```

Every page/header/footer JSON uses the standard Elementor **single template export** shape:

```json
{ "content": [ ... ], "page_settings": [], "version": "0.4", "title": "...", "type": "page" }
```

Every top-level element in `content` is `"elType": "container"` (Elementor's modern flex Container),
never the legacy `section` / `column` structure. Nested rows/columns are inner containers
(`"isInner": true`). Only native/classic Elementor widgets are used — `heading`, `text-editor`,
`image`, `button`, `spacer`, `divider`, `icon-list`, `icon-box`, `testimonial`, `video`, `icon` — no
Atomic-editor elements, and no raw HTML widgets (per the site owner's Atomic editor being disabled).

## Content fidelity

All headings, paragraph copy, blurbs, testimonials, blog article bodies, Scripture quotes, and stats
are reproduced verbatim (or lightly reformatted from inline styles into semantic HTML inside
`text-editor` widgets) from the source HTML/JS. No new marketing copy was invented.

`index.html` is a single-page-app-style file that gates four screens (Home/About/Shop/Listings) plus
a fifth Contact screen behind `sc-if value="{{ isHome/isAbout/isShop/isListings/isContact }}"`, with
the real book/testimonial/shop data defined in the embedded `<script type="text/x-dc">` component
class (`books()`, `dosBooks()`, `renderVals()`), not as literal HTML. That script was read in full and
used as the source of truth for all `sc-for`-looped content (the 3 Mighty Men of Valor books, the 5
Daughters of Sarah books, the 3 home-page testimonials, the featured Abraham/Sarah spotlight panels).
Each `sc-for` loop was hard-coded into literal, repeated Elementor widget instances rather than
reproduced as dynamic/data-bound content, per scope.

## Import order

1. **Header & footer first** (via XPRO — see its own section below), so pages preview correctly once
   built.
2. **Home** (`pages/home.json`) — import and assign as the WordPress homepage (see below).
3. **About, Shop, Listings, Contact** — the other four core pages from `index.html`.
4. **Blog** (`pages/blog.json`) — the Journal/blog listing page.
5. **The 8 article/book pages** — `meet-abraham.json`, `isaac-the-promised-son.json`,
   `jacobs-journey.json`, `sarahs-obedience.json`, `men-of-valor.json`,
   `daughters-of-scripture.json`, `why-1611-kjv.json`, `reading-the-word-together.json`.

## How to import each page template

1. In WordPress admin, go to **Templates → Saved Templates** (Elementor's template library).
2. Click **Import Templates**, then upload the `.json` file (e.g. `pages/home.json`).
3. Once imported, it appears in **Saved Templates**. Create a new WordPress Page (e.g. titled
   "Home"), edit it with Elementor, and insert the imported template into the page (the folder icon
   in Elementor's panel → **My Templates** → select the imported template → Insert).
4. Repeat for each file in `pages/`. Give each new WordPress Page a slug matching its nav target
   (`/`, `/about`, `/shop`, `/listings`, `/blog`, `/contact`, and a slug per article, e.g.
   `/blog/meet-abraham`).
5. Publish each page once its content looks correct.

## Setting the WordPress homepage

After importing and publishing the Home page:

1. Go to **Settings → Reading**.
2. Under "Your homepage displays," choose **A static page**.
3. Set **Homepage** to the WordPress Page you created from `pages/home.json`.
4. Save Changes.

## Building the Menu (Appearance → Menus)

The nav in `index.html`'s header (and mirrored in the footer "Explore" column) is:

| Menu label | Target page |
|---|---|
| Home | the Home page (`pages/home.json`) |
| About | the About page (`pages/about.json`) |
| Shop | the Shop page (`pages/shop.json`) |
| Listings | the Listings page (`pages/listings.json`) |
| Blog | the Blog page (`pages/blog.json`) |
| Contact | the Contact page (`pages/contact.json`) |

Steps:

1. Go to **Appearance → Menus**.
2. Click **Create a new menu**, name it e.g. "Primary Menu."
3. Add the six pages above, in the order listed, as menu items.
4. Under **Menu Settings**, check the box for **Primary Menu** (or the location your active theme /
   XPRO exposes) as the **Menu Location**, then click **Save Menu**. This assigns it as the Primary
   Menu location.
5. In the XPRO header template (`header-footer/header.json`), the nav is currently built as a static
   `icon-list` widget with hard-coded links (`/`, `/about`, etc.) rather than a dynamic WordPress Nav
   Menu widget — once you've built the Appearance → Menus menu above, you may optionally swap that
   icon-list for Elementor's native **Nav Menu** widget (classic, non-atomic) pointed at the "Primary
   Menu" location for a menu that stays in sync with WordPress automatically.

## Header & footer (XPRO)

`header-footer/header.json` and `header-footer/footer.json` are built the same
Container/native-widget way. Import them the same way as page templates
(**Templates → Saved Templates → Import Template**), then in XPRO's header/footer builder
(**XPRO → Theme Builder** or similar, depending on your XPRO version) create a new Header template
and a new Footer template, and insert the corresponding imported Elementor template into each. Set
XPRO's display conditions to "Entire Site" for both so they appear on every page.

- **Header** contains: the "12 / Twelve Scents Publishing" logo lockup, the six nav links
  (Home/About/Shop/Listings/Blog/Contact), a "Contact Us" button, and a cart icon.
- **Footer** contains: the four-column footer grid (brand blurb + social icons, "Explore" links,
  "Series" links, "Contact" details) and the bottom copyright/tagline bar — reproduced from the
  `footer-grid` section near the end of `index.html`.

## Cart icon / interactivity — decorative only

The source mockup's header cart icon, cart-count badge, and slide-out cart drawer, the mobile
hamburger menu toggle, the "Look Inside" image flip-through prev/next controls on the Home page, and
the Shop/Listings "Coming Soon" vs. "Pre-Order" toggle were all driven by custom JavaScript
(`support.js` / the embedded component class) that has **not** been ported — Elementor's native/
classic widgets cannot replicate stateful JS behavior without a plugin. In the converted JSON:

- The cart icon is a **static, decorative icon** (Elementor `icon` widget) — wire it up to a real
  cart/e-commerce plugin (e.g. WooCommerce) if live cart functionality is needed, or leave it
  decorative and link it to the Shop page.
- The mobile menu toggle is omitted — Elementor/your theme's native responsive nav handles mobile
  menus automatically once the header is built with the Nav Menu widget.
- The "Look Inside" flip-through galleries (Abraham's 5 spreads, Sarah's 6 spreads) are represented as
  a single static cover image plus a note in `pages/home.json` suggesting an Elementor **Image
  Carousel** widget (native/classic) as the closest static equivalent if a click-through gallery is
  wanted.
- "Pre-Order" vs. "Coming Soon" states on Shop/Listings are hard-coded per book (matching each book's
  actual `status` in the source data) rather than reactive.

## Images & video — swap after uploading to the WordPress Media Library

Every image and video URL in the converted JSON is a placeholder in the form:

```
__REPLACE_WITH_WORDPRESS_MEDIA_URL__/<original-filename>
```

e.g. `__REPLACE_WITH_WORDPRESS_MEDIA_URL__/abraham-cover.png`. Before or after importing each
template:

1. Upload all image/video files from the repo root (`Founded.png`, `MenofValorPatriarchs.png`,
   `OurStory.png`, `Readingtochild.mp4`, `abraham-collage.png`, `abraham-cover.png`, `dos-*.png`,
   `first-frame.jpg`, `isaac-cover.png`, `jacob-cover.png`, `look-*.png`, `sarah-*.png`) to the
   WordPress Media Library.
2. In each Elementor page, click each image/video widget and re-select the correct uploaded media
   item (Elementor will let you search the Media Library), replacing the placeholder URL. Do a
   find-and-replace of `__REPLACE_WITH_WORDPRESS_MEDIA_URL__/` → your site's real uploads path if you
   prefer to bulk-edit the JSON files directly before importing.

## Contact form (WPForms)

The Contact page (`pages/contact.json`) intentionally does **not** build a native Elementor form —
see `wpforms/contact-form-spec.md` for the exact WPForms field list, confirmation message, and
notification email to configure. Once built in WPForms, embed it in the left column of the Contact
page template, replacing the placeholder note left there.

## Content not present in the source (had to infer / flag)

- **Listings page filter buttons** ("All Series" / "Mighty Men of Valor" / "Daughters of Sarah") were
  JS `sc-for` filter pills in the source with no static equivalent — rebuilt as three static Button
  widgets linking to `#`; wire these up manually (e.g. to WooCommerce category links) if filtering is
  needed.
- **Newsletter signup form** in the Blog sidebar (`pages/blog.json`) was a JS-only demo form in the
  source with no backend — flagged with a note recommending a real email-marketing
  plugin/widget instead of rebuilding it as a non-functional Elementor form.
- **Google Map embed** on the Contact page (an iframe of "Delaware, USA" in the source) was **not**
  rebuilt as an `iframe`/HTML widget (disallowed per the Atomic-editor-off / native-widgets-only
  constraint) — flagged with a note recommending Elementor's native **Google Maps** widget instead.
- A dedicated **Contact** screen *does* exist in the source (`sc-if value="{{ isContact }}"` in
  `index.html`), so no inference was needed there — all Contact page copy is faithfully reproduced.
- The Blog page's sidebar widgets (categories, popular posts, newsletter, "About the Publisher") were
  reproduced as a stacked container beneath the main post grid rather than a true side-by-side
  sidebar, since Elementor Containers don't have a dedicated "sidebar" concept — rearrange into a
  two-column container in the live editor if a literal side-by-side layout is wanted.

## Blog & article pages

`blog.html` and the eight article pages (`meet-abraham.html`, etc.) were already close to
plain/portable HTML (the file even contains WordPress-porting comments from the original author,
e.g. mapping `.entry-title a` → `the_title()`), so their conversion to Elementor JSON is more direct
than the `x-dc`-templated `index.html` screens.
