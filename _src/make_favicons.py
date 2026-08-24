#!/usr/bin/env python3
"""Generate square favicons from the WEL logo.

    python _src/make_favicons.py

The logo is 400x220 - roughly 1.8:1. Browsers squeeze whatever you hand them
into a square slot, so using the logo directly makes it look condensed. This
letterboxes it onto a square canvas with a little padding instead, so it keeps
its proportions.

The canvas is white rather than transparent: the logo's darker blue would
disappear against a dark browser tab strip.

Needs Pillow (pip install pillow). Only run when the logo changes.
"""
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "assets", "img", "site", "wel-logo.png")
OUT = os.path.join(ROOT, "assets", "img", "site")

BG = (255, 255, 255, 255)
PAD = 0.08          # share of the canvas left as margin on each side


def mark_only(logo):
    """Crop to the WEL mark, dropping the tagline underneath it.

    At favicon sizes "Think it. Make it. Prove it." is unreadable mush and it
    shrinks the mark to make room. This trims to the artwork, then looks for a
    blank horizontal band in the lower part of the image - the gap above the
    tagline - and cuts there.
    """
    box = logo.getbbox()
    if box:
        logo = logo.crop(box)
    w, h = logo.size
    alpha = logo.split()[-1]
    rows = [sum(alpha.crop((0, y, w, y + 1)).tobytes()) for y in range(h)]
    peak = max(rows) or 1

    blank = [y for y, v in enumerate(rows) if v <= peak * 0.01]
    # a gap in the bottom third means a tagline sits below it
    lower = [y for y in blank if y > h * 0.6]
    if lower:
        logo = logo.crop((0, 0, w, min(lower)))
        box = logo.getbbox()
        if box:
            logo = logo.crop(box)
    return logo


def square(size):
    logo = mark_only(Image.open(SRC).convert("RGBA"))
    canvas = Image.new("RGBA", (size, size), BG)

    inner = int(size * (1 - 2 * PAD))
    w, h = logo.size
    scale = min(inner / w, inner / h)          # fit, never distort
    new = (max(1, round(w * scale)), max(1, round(h * scale)))
    logo = logo.resize(new, Image.LANCZOS)

    canvas.paste(logo, ((size - new[0]) // 2, (size - new[1]) // 2), logo)
    return canvas


def main():
    for size, name in [(32, "favicon-32.png"),
                       (180, "apple-touch-icon.png"),
                       (512, "favicon-512.png")]:
        img = square(size)
        img.convert("RGB").save(os.path.join(OUT, name))
        print("  %-22s %dx%d" % (name, size, size))

    # .ico bundles several sizes for older browsers and Windows shortcuts
    ico = square(256)
    ico.convert("RGB").save(os.path.join(ROOT, "favicon.ico"),
                            sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print("  %-22s 16/32/48/64" % "favicon.ico")


if __name__ == "__main__":
    main()
