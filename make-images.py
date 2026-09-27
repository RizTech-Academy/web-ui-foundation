"""Generate the capstone's placeholder imagery.

Real photographs should replace these; the filenames, dimensions and aspect
ratios are what the HTML expects, so a swap is a straight file replacement.
"""
from PIL import Image, ImageDraw, ImageFilter
import math, os, random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(OUT, exist_ok=True)

def lerp(a, b, t): return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))

def compose(w, h, top, bottom, blobs, seed):
    """A soft vertical gradient with blurred blobs over it."""
    rnd = random.Random(seed)
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        d.line([(0, y), (w, y)], fill=lerp(top, bottom, y / max(1, h - 1)))
    layer = Image.new("RGB", (w, h), (0, 0, 0))
    ld = ImageDraw.Draw(layer)
    mask = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(mask)
    for colour, cx, cy, r, alpha in blobs:
        x, y = int(cx * w), int(cy * h)
        rr = int(r * min(w, h))
        ld.ellipse([x - rr, y - rr, x + rr, y + rr], fill=colour)
        md.ellipse([x - rr, y - rr, x + rr, y + rr], fill=alpha)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=max(8, min(w, h) // 8)))
    img = Image.composite(layer, img, mask)
    # a little grain so it compresses like a photograph rather than flat colour
    px = img.load()
    for _ in range((w * h) // 12):
        x, y = rnd.randrange(w), rnd.randrange(h)
        r, g, b = px[x, y]
        n = rnd.randint(-9, 9)
        px[x, y] = (max(0, min(255, r + n)), max(0, min(255, g + n)), max(0, min(255, b + n)))
    return img.filter(ImageFilter.GaussianBlur(radius=0.4))

SKY   = (207, 229, 220)
DEEP  = (21, 53, 42)
MID   = (47, 122, 97)
SAND  = (246, 243, 236)
WARM  = (214, 186, 146)

SCENES = {
    # hero: 16/9, wide, calm, light at the top
    "hero": dict(ratio=16/9, top=(226, 238, 232), bottom=(31, 79, 63),
                 blobs=[(MID, 0.22, 0.62, 0.42, 150), (SAND, 0.78, 0.30, 0.34, 120),
                        (DEEP, 0.60, 0.88, 0.40, 170), (WARM, 0.12, 0.22, 0.20, 90)],
                 widths=[400, 800, 1200, 2000], seed=11),
    "class-hatha": dict(ratio=3/2, top=SAND, bottom=(198, 220, 210),
                 blobs=[(MID, 0.30, 0.70, 0.40, 140), (WARM, 0.75, 0.35, 0.30, 110)],
                 widths=[400, 800], seed=21),
    "class-vinyasa": dict(ratio=3/2, top=(214, 232, 224), bottom=(31, 79, 63),
                 blobs=[(DEEP, 0.68, 0.66, 0.42, 160), (SAND, 0.24, 0.28, 0.28, 120)],
                 widths=[400, 800], seed=22),
    "class-pranayama": dict(ratio=3/2, top=(235, 240, 232), bottom=(176, 205, 192),
                 blobs=[(MID, 0.50, 0.78, 0.38, 130), (WARM, 0.20, 0.30, 0.26, 100)],
                 widths=[400, 800], seed=23),
    "studio": dict(ratio=3/2, top=SAND, bottom=(205, 224, 214),
                 blobs=[(WARM, 0.30, 0.40, 0.34, 120), (MID, 0.80, 0.75, 0.36, 140)],
                 widths=[400, 800, 1200], seed=31),
    "teacher-meera": dict(ratio=1, top=(226, 236, 230), bottom=(47, 122, 97),
                 blobs=[(DEEP, 0.50, 0.72, 0.40, 150), (SAND, 0.40, 0.28, 0.24, 120)],
                 widths=[240, 480], seed=41),
    "teacher-anil": dict(ratio=1, top=SAND, bottom=(176, 205, 192),
                 blobs=[(MID, 0.52, 0.70, 0.38, 140), (WARM, 0.42, 0.26, 0.22, 110)],
                 widths=[240, 480], seed=42),
}

made = []
for name, s in SCENES.items():
    for w in s["widths"]:
        h = round(w / s["ratio"])
        img = compose(w, h, s["top"], s["bottom"], s["blobs"], s["seed"] + w)
        p = os.path.join(OUT, f"{name}-{w}.jpg")
        img.save(p, "JPEG", quality=78, optimize=True, progressive=True)
        made.append((f"{name}-{w}.jpg", w, h, os.path.getsize(p)))

# a static map stand-in: a plain plan-view, deliberately flat so it stays small
def static_map(w=800, h=500):
    img = Image.new("RGB", (w, h), (238, 238, 233))
    d = ImageDraw.Draw(img)
    for x in range(0, w, 96):
        d.line([(x, 0), (x, h)], fill=(226, 226, 220), width=2)
    for y in range(0, h, 96):
        d.line([(0, y), (w, y)], fill=(226, 226, 220), width=2)
    d.rectangle([0, int(h * 0.44), w, int(h * 0.56)], fill=(252, 250, 242))
    d.rectangle([int(w * 0.62), 0, int(w * 0.72), h], fill=(252, 250, 242))
    d.ellipse([int(w * 0.40), int(h * 0.36), int(w * 0.40) + 46, int(h * 0.36) + 46],
              fill=(31, 79, 63))
    return img

p = os.path.join(OUT, "map-kothrud-800.jpg")
static_map().save(p, "JPEG", quality=72, optimize=True)
made.append(("map-kothrud-800.jpg", 800, 500, os.path.getsize(p)))

for n, w, h, b in made:
    print(f"{n:28s} {w:5d}x{h:<5d} {b/1024:7.1f} KB")
print(f"\n{len(made)} JPEGs, {sum(x[3] for x in made)/1024:.0f} KB total")
