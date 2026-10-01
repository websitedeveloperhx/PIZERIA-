# PIZERIA

Premium wood-fired pizza website. Plain HTML, CSS and vanilla JavaScript. No build step, no dependencies.

## Run locally
Open `index.html` in a browser, or serve the folder:

    cd pizeria
    python3 -m http.server 8000      # then open http://localhost:8000

Fonts (Fraunces and DM Sans) load from Google Fonts when online. Offline, the CSS falls back to system serif/sans fonts.

## File structure
    index.html              all sections, semantic markup
    css/styles.css          design tokens (:root) and all styles, mobile-first
    js/app.js               nav, hero scroll sequence, cart, builder, reviews
    assets/*.svg            layered pizza ILLUSTRATIONS (not photographs)
    tools/generate-assets.py  regenerates the artwork in /assets

## Swapping in real photography
Replace files in `assets/` with the same names, or edit the `src` attributes in `index.html`.
The hero and builder use separate transparent layers (dough, sauce, cheese, toppings), so real
photography needs transparent PNG/WebP cutouts per layer. Menu cards use `card-*.svg` (square crops).

## What came from the reference video
The reference is a phone recording of a laptop screen (720x1280, 14.7 s). I sampled it at 2 frames per second and
read structure and motion from that. Fonts, exact colours and body copy were too small and blurry to read.

| Reference (observed) | PIZERIA implementation |
|---|---|
| Dark page, thin header: small wordmark, 4 links, red pill button; round red button bottom-right | Same arrangement. Red round cart button bottom-right opens the cart |
| Hero: one large pizza centred on near-black, big text swapping in over it as you scroll | Pinned scroll sequence (560vh): pizza, big overlay line, then layers |
| Pizza lifts apart into floating layers with a headline, then re-forms, then a final headline | Six image layers rise on a 3D tilt, labelled, then collapse back |
| "Signature pizzas": heading left, intro right, row of dark cards with image, name, gold price, light pill button | Same card anatomy, gold prices, cream pill "Add to cart" |
| "Build your masterpiece": round plate left, controls right, price and pill button bottom right | Same layout; plate shows real stacked ingredient layers and a live total |
| Row of four small icon features, then a centred quote | "Four things we refuse to rush" plus a story block (on cream for contrast) |
| Final section: huge two-line headline, white then red, two buttons | "Your next slice / starts here." with Order and Build buttons |

## Deliberate differences
- Headings use an editorial serif, as your brief requires. The reference appears to use a bold condensed sans.
- Four menu cards (your brief) instead of the three visible in the video. 4 columns on desktop, 2 on tablet, 1 on phone.
- Page order follows the video (hero, menu, builder, craft/story), then adds Visit and sample reviews from your brief.
- All images are generated illustrations, because no licensed photography was available offline. They are labelled as illustrations.
- No smoke or ember particles in the hero (video shows a smoke effect; I used a soft warm glow instead).
- All copy and branding are original. Nothing from the reference's text or logo was reused.

## Assumptions to confirm
- Menu prices ($14 / $17 / $19 / $16) are sample prices.
- Builder: $12 base; size +$0/+$2/+$4; cheese none/mozzarella +$1/extra +$2; pepperoni +$2; mushrooms, olives, basil, jalapeños +$1 each.
- Red onion is +$1. The brief gave no price for it.
- Address, hours, phone, email and social links are placeholders. Reviews are clearly marked sample content.
- Checkout is intentionally not connected: the button says so and nothing is ordered or charged.

## QA report (actually run)
Tested with Playwright and Chromium: 61 automated checks, all passing.
- Horizontal overflow checked while scrolling the full page at 360, 390, 430, 768, 1024 and 1440 px: none.
- No console or page errors at those six widths. All images load.
- Every in-page link has a target; no empty links. All five nav links scroll to the right section.
- Cart: add, merge duplicates, quantity +/-, remove, subtotal, empty state, persistence across reload, Esc closes,
  focus moves into the drawer, stays trapped while tabbing, and returns to the cart button.
- Builder: default $15, every option changes the price as listed, ingredient layers match selections, sauce swaps,
  custom pizza adds to the cart, arrow keys change radios.
- Mobile menu opens, closes on link tap and on Esc. Controls are at least 44px tall on a 390px screen.
- Reduced motion: hero becomes a single static screen, reveals are disabled.
- Visual review of screenshots at 390, 768 and 1440 px for the hero stages and every section.

## Not verified
- Google Fonts rendering (tested offline with the fallback fonts, so line breaks may shift slightly).
- Safari, Firefox, and real phones. Only Chromium was tested.
- Frame rate and performance of the 3D hero on low-end devices; no Lighthouse or axe audit was run.
- Pixel-level match to the reference: not possible from a low-resolution phone recording of a screen. Layout and motion were matched by eye.
- The floating cart button can sit over text near the bottom-right corner while scrolling (as in the reference).
