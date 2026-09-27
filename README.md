# Aarambh Yoga — Web UI Foundation capstone

The finished site from the capstone of
[Web UI Development Foundation](https://riztechacademy.com/learn/web-ui-foundation)
at RizTech Academy.

A four-page site for a small yoga studio in Kothrud, Pune. **HTML and CSS only** —
no framework, no build step, and no JavaScript anywhere.

**Live: <https://riztech-academy.github.io/web-ui-foundation/>**

**This is here to compare against when you are stuck, not to start from.** Build
your own and look at this when something will not work.

## Running it

There is nothing to install.

```bash
git clone https://github.com/RizTech-Academy/web-ui-foundation.git
cd web-ui-foundation
python3 -m http.server 5601
```

Then open <http://localhost:5601>.

To open it on your phone, bind to your network instead and use your machine's
address — `ipconfig getifaddr en0` on a Mac:

```bash
python3 -m http.server 5601 --bind 0.0.0.0
```

## What is here

```
index.html        home: hero, the three class types, hours, location
classes.html      the weekly timetable, what to bring, fees
about.html        the studio and the two teachers
contact.html      the booking form
404.html          a not-found page with the full navigation on it
styles.css        one file, in cascade layers
images/           JPEG and WebP at several widths, plus SVG
build-pages.py    regenerates the shared header and footer across the pages
fetch-photos.py   re-downloads the photographs and cuts them to size
make-images.py    regenerates the one remaining generated image, the map
make-webp.sh      makes a WebP beside every JPEG
```

`build-pages.py` exists because a static site has no includes, and four copies of
a header drift apart. Edit the Python, not the four HTML files.

## What it demonstrates, by module

| Module | In this site |
|---|---|
| 1 HTML | landmarks, a real `<table>` with `scope` and `<caption>`, a labelled form, `tel:` and `wa.me` links |
| 2 CSS | cascade layers, two-layer colour tokens, `#767676` borders, `system-ui` |
| 3 Layout | `auto-fit` card grids, a hero built from overlapping grid items, `margin-inline-end: auto` |
| 4 Responsive | `clamp()` type with a `rem` term, `srcset`/`sizes`, dark mode, reduced motion |
| 5 Accessibility | skip link, `:focus-visible`, `aria-current`, `alt` that replaces the image |
| 6 Modern CSS | container queries on the cards, `:has()` for form errors, `accent-color` |
| 7 Best practices | one class per rule, no ids, no `!important` outside the motion safety net |

## Measured

On the home page of the **deployed** site, unthrottled:

```
Requests           6         (7 after scrolling to the lazy map)
Transferred        35.2 KB   (43.3 KB after that scroll)
Largest file       hero-2000.webp, 16.5 KB
Stylesheet         15 KB
Contrast           every text element passes AA in both light and dark mode
Keyboard           16 stops, all with a visible ring, order matches the page
320px              no horizontal scroll; the timetable scrolls inside its wrapper
```

The hero text was measured against the **composited image and gradient**, pixel by
pixel, not against an assumed background — the worst pixel under any hero text is
7.09:1.

## About the images

The photographs are real, from [Pexels](https://www.pexels.com/). `fetch-photos.py`
downloads them and crops each one to the width and aspect ratio the HTML already
asks for, so the filenames never change.

| File | Photo |
|---|---|
| `hero-*` | <https://www.pexels.com/photo/29490926/> |
| `studio-*` | <https://www.pexels.com/photo/25599832/> |
| `class-hatha-*` | <https://www.pexels.com/photo/8436610/> |
| `class-vinyasa-*` | <https://www.pexels.com/photo/8436577/> |
| `class-pranayama-*` | <https://www.pexels.com/photo/3059892/> |
| `teacher-meera-*` | <https://www.pexels.com/photo/3822454/> |
| `teacher-anil-*` | <https://www.pexels.com/photo/6787354/> |

The Pexels licence allows commercial use and requires no attribution. Crediting
the source anyway costs nothing and is the decent thing to do.

`map-kothrud-800.jpg` is the exception: it is still a generated plan view from
`make-images.py`. Map tiles carry their own licence and attribution rules, so a
drawn stand-in keeps the repository free of someone else's terms.

Because the photographs are real, every `alt` describes what is actually in the
frame. The hero keeps `alt=""` — the `<h1>` beside it carries the meaning, so the
photograph is decorative. The map sits inside a link, so its `alt` names the
destination rather than the picture.

WebP saves **45%** across these photographs (790 KB of JPEG becomes 436 KB), and
**50%** on the hero alone. The generated map saves 75% — smooth, flat images
compress far better than photographs do, which is why a placeholder-based
measurement flatters the format. 45% is the number to expect from real work.

There is no AVIF here because this machine had no AVIF encoder. Add `avifenc`
and a third `<source>` if you have one.

## Licence

The code is free to use for any purpose. The business, its address, the phone
number and the teachers are invented.
