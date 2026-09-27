import os
D = os.path.dirname(os.path.abspath(__file__))

LOGO = '''<svg viewBox="0 0 32 32" fill="none" aria-hidden="true" focusable="false">
          <path d="M16 3c3.6 3.9 5.4 7.6 5.4 11.2 0 3.6-1.8 7.3-5.4 11.1-3.6-3.8-5.4-7.5-5.4-11.1C10.6 10.6 12.4 6.9 16 3Z" fill="currentColor"/>
          <path d="M6 16.5c3.4-.7 6.1-.2 8.2 1.4 2 1.6 3.3 4.2 3.8 7.9-3.6.5-6.4-.1-8.4-1.8-2-1.6-3.2-4.2-3.6-7.5Z" fill="currentColor" opacity=".55"/>
          <path d="M26 16.5c-.4 3.3-1.6 5.9-3.6 7.5-2 1.7-4.8 2.3-8.4 1.8.5-3.7 1.8-6.3 3.8-7.9 2.1-1.6 4.8-2.1 8.2-1.4Z" fill="currentColor" opacity=".55"/>
        </svg>'''

NAV = [("index.html", "Home"), ("classes.html", "Classes"),
       ("about.html", "About"), ("contact.html", "Contact")]

def head(title, desc, canonical, og_image="images/hero-1200.jpg"):
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="https://aarambhyoga.example/{canonical}">
  <link rel="icon" href="images/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="styles.css">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="https://aarambhyoga.example/{og_image}">
  <meta property="og:url" content="https://aarambhyoga.example/{canonical}">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>

  <header class="site-header">
    <div class="container site-header__inner">
      <a class="logo" href="index.html">
        {LOGO}
        Aarambh Yoga
      </a>
      <nav aria-label="Main">
        <ul class="nav-list">
'''

def nav(current):
    out = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ''
        out.append(f'          <li><a href="{href}"{cur}>{label}</a></li>')
    return "\n".join(out)

def after_nav():
    return '''
        </ul>
      </nav>
      <a class="button" href="contact.html">Book a free class</a>
    </div>
  </header>

  <main id="main" tabindex="-1">
'''

FOOT = '''  </main>

  <footer class="site-footer">
    <div class="container site-footer__inner">
      <p>© 2026 Aarambh Yoga, Kothrud, Pune</p>
      <p><a href="contact.html">Contact</a> · <a href="tel:+912025431987">020 2543 1987</a></p>
    </div>
  </footer>
</body>
</html>
'''

def page(filename, title, desc, body, current=None):
    html = head(title, desc, filename) + nav(current or filename) + after_nav() + body + FOOT
    with open(os.path.join(D, filename), "w", encoding="utf-8") as f:
        f.write(html)
    return filename, len(html)

# ------------------------------------------------------------------ classes
CLASSES_BODY = '''    <section class="section">
      <div class="container stack">
        <h1>Classes and timetable</h1>
        <p class="prose">Every class is capped at twelve people. Drop in for any of them, or book ahead if you would rather be sure of a mat.</p>

        <div class="table-wrap">
          <table class="timetable">
            <caption>Weekly class timetable, from 1 October 2026</caption>
            <thead>
              <tr>
                <th scope="col">Time</th>
                <th scope="col">Mon</th>
                <th scope="col">Tue</th>
                <th scope="col">Wed</th>
                <th scope="col">Thu</th>
                <th scope="col">Fri</th>
                <th scope="col">Sat</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">6:30</th>
                <td>Hatha</td><td>Vinyasa</td><td>Hatha</td><td>Vinyasa</td><td>Hatha</td><td>Hatha</td>
              </tr>
              <tr>
                <th scope="row">8:00</th>
                <td>Pranayama</td><td></td><td>Pranayama</td><td></td><td>Pranayama</td><td>Vinyasa</td>
              </tr>
              <tr>
                <th scope="row">9:00</th>
                <td>Hatha (gentle)</td><td>Hatha (gentle)</td><td>Hatha (gentle)</td><td>Hatha (gentle)</td><td>Hatha (gentle)</td><td></td>
              </tr>
              <tr>
                <th scope="row">17:30</th>
                <td>Vinyasa</td><td>Hatha</td><td>Vinyasa</td><td>Hatha</td><td>Vinyasa</td><td></td>
              </tr>
              <tr>
                <th scope="row">19:00</th>
                <td>Hatha</td><td>Pranayama</td><td>Hatha</td><td>Pranayama</td><td>Hatha</td><td></td>
              </tr>
            </tbody>
            <tfoot>
              <tr>
                <td colspan="7">Sunday closed. Public holidays are announced on WhatsApp.</td>
              </tr>
            </tfoot>
          </table>
        </div>

        <h2 id="what-to-bring">What to bring</h2>
        <ul class="prose">
          <li>Loose clothes you can bend in. That is genuinely all.</li>
          <li>Mats, blocks and straps are here, and free to use.</li>
          <li>Water. There is a filter on the landing if you forget.</li>
          <li>Come ten minutes early for your first class so we can say hello.</li>
        </ul>

        <h2 id="fees">Fees</h2>
        <dl class="hours prose">
          <div><dt>First class</dt><dd>Free</dd></div>
          <div><dt>Drop in</dt><dd>₹300</dd></div>
          <div><dt>Ten classes</dt><dd>₹2,400</dd></div>
          <div><dt>Monthly, unlimited</dt><dd>₹3,200</dd></div>
        </dl>
        <p class="prose">Cash, UPI or card at the desk. We do not take payment online.</p>
      </div>
    </section>
'''

# ------------------------------------------------------------------ about
ABOUT_BODY = '''    <section class="section">
      <div class="container stack">
        <h1>About the studio</h1>
        <p class="prose">Aarambh means beginning. We opened in 2019 above a bookshop on Karve Road, with eight mats and a leaking skylight. The skylight is fixed and the class size is still small on purpose — twelve people, so the teacher can actually see you.</p>

        <figure class="figure prose">
          <picture>
            <source type="image/webp" srcset="images/studio-400.webp 400w, images/studio-800.webp 800w, images/studio-1200.webp 1200w" sizes="(min-width: 48rem) 40rem, 100vw">
            <img src="images/studio-800.jpg" srcset="images/studio-400.jpg 400w, images/studio-800.jpg 800w, images/studio-1200.jpg 1200w" sizes="(min-width: 48rem) 40rem, 100vw" alt="The studio floor in morning light, with mats rolled along one wall" width="800" height="533" loading="lazy">
          </picture>
          <figcaption>The main room, before the 6:30 class.</figcaption>
        </figure>

        <h2>Who teaches</h2>
        <ul class="grid-auto">
          <li>
            <article class="card">
              <div class="card__media">
                <picture>
                  <source type="image/webp" srcset="images/teacher-meera-240.webp 240w, images/teacher-meera-480.webp 480w" sizes="(min-width: 48rem) 15rem, 100vw">
                  <img src="images/teacher-meera-480.jpg" srcset="images/teacher-meera-240.jpg 240w, images/teacher-meera-480.jpg 480w" sizes="(min-width: 48rem) 15rem, 100vw" alt="Meera Deshpande" width="480" height="480" loading="lazy">
                </picture>
              </div>
              <div class="card__body">
                <h3 class="card__title">Meera Deshpande</h3>
                <p>Teaches hatha and pranayama. Trained in Pune and Rishikesh; nineteen years of teaching, most of them here.</p>
                <p class="card__meta">Mornings, Monday to Saturday</p>
              </div>
            </article>
          </li>
          <li>
            <article class="card">
              <div class="card__media">
                <picture>
                  <source type="image/webp" srcset="images/teacher-anil-240.webp 240w, images/teacher-anil-480.webp 480w" sizes="(min-width: 48rem) 15rem, 100vw">
                  <img src="images/teacher-anil-480.jpg" srcset="images/teacher-anil-240.jpg 240w, images/teacher-anil-480.jpg 480w" sizes="(min-width: 48rem) 15rem, 100vw" alt="Anil Kulkarni" width="480" height="480" loading="lazy">
                </picture>
              </div>
              <div class="card__body">
                <h3 class="card__title">Anil Kulkarni</h3>
                <p>Teaches vinyasa. Came to yoga after a running injury and is sympathetic about stiff hamstrings.</p>
                <p class="card__meta">Evenings, Monday to Friday</p>
              </div>
            </article>
          </li>
        </ul>

        <h2>If you have never done this before</h2>
        <p class="prose">You do not need to be flexible, and you do not need to be able to touch your toes. Nobody will ask you to do a headstand. Come to a gentle hatha class at 9:00, stand at the back, and stop whenever you like — that is entirely normal and the teacher expects it.</p>
      </div>
    </section>
'''

# ------------------------------------------------------------------ contact
CONTACT_BODY = '''    <section class="section">
      <div class="container stack">
        <h1>Book a free class</h1>
        <p class="prose">Fill this in and we will message you back to confirm a time. Your first class is free, whichever one you choose.</p>

        <form class="form" action="https://example.invalid/enquiry" method="post">
          <div class="field">
            <label for="name">Your name</label>
            <input type="text" id="name" name="name" autocomplete="name" required>
            <p class="field__error"><span aria-hidden="true">⚠</span> Please tell us your name.</p>
          </div>

          <div class="field">
            <label for="phone">Phone number</label>
            <p class="field__hint" id="phone-hint">Ten digits, starting 6 to 9. We reply on WhatsApp.</p>
            <input type="tel" id="phone" name="phone"
                   inputmode="numeric" autocomplete="tel"
                   pattern="[6-9][0-9]{9}" maxlength="10" required
                   aria-describedby="phone-hint"
                   title="A ten-digit Indian mobile number, starting 6 to 9">
            <p class="field__error"><span aria-hidden="true">⚠</span> Enter a ten-digit number starting 6 to 9.</p>
          </div>

          <div class="field">
            <label for="email">Email <span class="field__hint">(optional)</span></label>
            <input type="email" id="email" name="email" autocomplete="email">
            <p class="field__error"><span aria-hidden="true">⚠</span> That does not look like an email address.</p>
          </div>

          <div class="field">
            <label for="class">Which class</label>
            <select id="class" name="class" required>
              <option value="">Choose a class</option>
              <option value="hatha">Hatha — slow, for beginners</option>
              <option value="hatha-gentle">Hatha (gentle) — 9:00 weekdays</option>
              <option value="vinyasa">Vinyasa — continuous, some experience</option>
              <option value="pranayama">Pranayama — seated breathing</option>
              <option value="unsure">I am not sure yet</option>
            </select>
            <p class="field__error"><span aria-hidden="true">⚠</span> Please choose a class.</p>
          </div>

          <fieldset class="field">
            <legend>When suits you</legend>
            <label class="checkbox"><input type="radio" name="when" value="morning" checked> Mornings, 6:30 to 10:00</label>
            <label class="checkbox"><input type="radio" name="when" value="evening"> Evenings, 17:30 to 20:00</label>
            <label class="checkbox"><input type="radio" name="when" value="either"> Either is fine</label>
          </fieldset>

          <div class="field">
            <label for="notes">Anything we should know <span class="field__hint">(optional)</span></label>
            <textarea id="notes" name="notes" rows="4" maxlength="500"
                      placeholder="An injury, a recent operation, or simply that you have never done yoga before."></textarea>
          </div>

          <label class="checkbox">
            <input type="checkbox" name="whatsapp" value="yes" checked>
            <span>It is fine to reply on WhatsApp</span>
          </label>

          <div>
            <button class="button" type="submit">Send enquiry</button>
          </div>
        </form>

        <h2 id="other-ways">Other ways to reach us</h2>
        <p class="prose">
          <a href="tel:+912025431987">020 2543 1987</a> ·
          <a href="https://wa.me/919876543210">WhatsApp</a> ·
          <a href="mailto:hello@aarambhyoga.example">hello@aarambhyoga.example</a>
        </p>
        <p class="prose">
          Second floor, Shivneri Building<br>
          Karve Road, Kothrud, Pune 411038
        </p>
        <a class="map-link" href="https://www.openstreetmap.org/search?query=Karve%20Road%20Kothrud%20Pune">
          <img src="images/map-kothrud-800.jpg" alt="Map showing Aarambh Yoga on Karve Road, Kothrud, Pune. Opens OpenStreetMap." width="800" height="500" loading="lazy">
        </a>
      </div>
    </section>
'''

# ------------------------------------------------------------------ 404
NOTFOUND_BODY = '''    <section class="section">
      <div class="container stack prose">
        <h1>That page is not here</h1>
        <p>The link may be old, or we may have moved something. These are all the pages there are:</p>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="classes.html">Classes and timetable</a></li>
          <li><a href="about.html">About the studio</a></li>
          <li><a href="contact.html">Book a free class</a></li>
        </ul>
        <p>Or call us on <a href="tel:+912025431987">020 2543 1987</a>.</p>
      </div>
    </section>
'''

made = [
  page("classes.html", "Classes and timetable — Aarambh Yoga",
       "The weekly timetable for hatha, vinyasa and pranayama classes at Aarambh Yoga, Kothrud, Pune. Fees, and what to bring to your first class.",
       CLASSES_BODY),
  page("about.html", "About the studio — Aarambh Yoga",
       "A small yoga studio on Karve Road, Kothrud, open since 2019. Meet the two teachers, and what to expect if you have never done yoga before.",
       ABOUT_BODY, current="about.html"),
  page("contact.html", "Book a free class — Aarambh Yoga",
       "Book your first class at Aarambh Yoga in Kothrud, Pune. Your first class is free. Phone, WhatsApp and the studio address.",
       CONTACT_BODY, current="contact.html"),
  page("404.html", "Page not found — Aarambh Yoga",
       "That page could not be found. Here is everything on the Aarambh Yoga site.",
       NOTFOUND_BODY, current="none"),
]
for n, size in made:
    print(f"{n:16s} {size:6d} bytes")
