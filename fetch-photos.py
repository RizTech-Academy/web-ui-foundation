"""Fetch the capstone's photographs from Pexels and cut them to the sizes the
HTML already asks for.

Pexels licence: free to use, commercial use allowed, no attribution required.
The README credits the photographers anyway.

Re-run this to refresh the imagery. The filenames, widths and aspect ratios are
fixed by the HTML, so nothing else has to change.
"""
import os, urllib.request
from PIL import Image, ImageFilter

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".raw")
os.makedirs(OUT, exist_ok=True); os.makedirs(RAW, exist_ok=True)

# name -> (pexels photo id, aspect ratio, widths, crop focus as a 0-1 y offset)
PHOTOS = {
    "hero":             (29490926, 16/9, [400, 800, 1200, 2000], 0.45),
    "studio":           (25599832, 3/2,  [400, 800, 1200],       0.50),
    "class-hatha":      (8436610,  3/2,  [400, 800],             0.45),
    "class-vinyasa":    (8436577,  3/2,  [400, 800],             0.50),
    "class-pranayama":  (3059892,  3/2,  [400, 800],             0.40),
    "teacher-meera":    (3822454,  1.0,  [240, 480],             0.00),
    "teacher-anil":     (6787354,  1.0,  [240, 480],             0.00),
}

def fetch(pid):
    dest = os.path.join(RAW, f"{pid}.jpg")
    if os.path.exists(dest) and os.path.getsize(dest) > 10000:
        return dest
    url = (f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg"
           "?auto=compress&cs=tinysrgb&w=2400")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
        f.write(r.read())
    return dest

def crop_to(img, ratio, focus):
    w, h = img.size
    target = ratio
    if w / h > target:                      # too wide: trim the sides
        nw = int(h * target)
        x = (w - nw) // 2
        img = img.crop((x, 0, x + nw, h))
    else:                                   # too tall: trim top/bottom to the focus
        nh = int(w / target)
        y = int((h - nh) * focus)
        img = img.crop((0, y, w, y + nh))
    return img

rows = []
for name, (pid, ratio, widths, focus) in PHOTOS.items():
    src = fetch(pid)
    base = Image.open(src).convert("RGB")
    base = crop_to(base, ratio, focus)
    for w in widths:
        h = round(w / ratio)
        im = base.resize((w, h), Image.LANCZOS)
        if w <= 480:
            im = im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=60, threshold=3))
        p = os.path.join(OUT, f"{name}-{w}.jpg")
        im.save(p, "JPEG", quality=80, optimize=True, progressive=True)
        rows.append((f"{name}-{w}.jpg", w, h, os.path.getsize(p), pid))

for n, w, h, b, pid in rows:
    print(f"{n:26s} {w:5d}x{h:<5d} {b/1024:7.1f} KB   pexels/{pid}")
print(f"\n{len(rows)} JPEGs, {sum(r[3] for r in rows)/1024:.0f} KB")
