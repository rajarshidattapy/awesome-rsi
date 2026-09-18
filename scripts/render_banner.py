"""One-shot AgentR README banner. Colors and type match agentr.dev."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONTS = ASSETS / "fonts"

BG = (9, 11, 10)
CREAM = (243, 238, 223)
ORANGE = (231, 91, 49)
ACID = (213, 223, 114)
GOLD = (239, 166, 76)
LINE = (255, 255, 255, 26)

W, H = 1800, 540


def load(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


def draw_text(draw: ImageDraw.ImageDraw, xy, text, font, fill, tracking=0):
    x, y = xy
    if tracking == 0:
        draw.text((x, y), text, font=font, fill=fill)
        return
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking


def main() -> None:
    img = Image.new("RGBA", (W, H), (*BG, 255))
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)

    d.ellipse((-180, -220, 740, 700), fill=(101, 68, 103, 48))
    d.ellipse((880, -60, 2020, 820), fill=(42, 74, 61, 55))
    d.ellipse((1260, 160, 1900, 740), fill=(231, 91, 49, 18))
    img = Image.alpha_composite(img, overlay.filter(ImageFilter.GaussianBlur(80)))

    noise = Image.effect_noise((W, H), 22).convert("L")
    grain = Image.merge("RGBA", (noise, noise, noise, Image.new("L", (W, H), 12)))
    img = Image.alpha_composite(img, grain)

    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, W - 1, H - 1), outline=LINE, width=1)

    mono = load("JetBrainsMono-Medium.ttf", 22)
    serif = load("Newsreader-Regular.ttf", 86)
    italic = load("Newsreader-Italic.ttf", 28)
    credit_sans = load("HankenGrotesk-Bold.ttf", 30)
    credit_size = 30

    draw_text(draw, (64, 148), "Awesome RSI", serif, CREAM, tracking=-3.4)
    draw_text(
        draw,
        (68, 256),
        "Self-learning begins when experience becomes more than memory.",
        italic,
        GOLD,
    )
    draw.rectangle((64, 308, 318, 310), fill=ORANGE)

    mark = Image.open(ASSETS / "agentr-mark.png").convert("RGBA")
    mark.thumbnail((44, 44), Image.Resampling.LANCZOS)

    credit = "Curated by "
    brand = "agentr"
    credit_w = draw.textlength(credit, font=mono) + 1.8 * (len(credit) - 1)
    brand_w = sum(draw.textlength(c, font=credit_sans) - 1.4 for c in brand) + 1.4
    us_w = draw.textlength("_", font=credit_sans)
    gap = 12
    total_w = credit_w + mark.width + gap + brand_w + us_w
    cx = W - 64 - total_w
    cy = H - 88
    draw_text(draw, (cx, cy + 5), credit, mono, ACID, tracking=1.8)
    mark_y = int(cy + (credit_size - mark.height) / 2)
    img.paste(mark, (int(cx + credit_w), mark_y), mark)
    bx = cx + credit_w + mark.width + gap
    draw_text(draw, (bx, cy), brand, credit_sans, CREAM, tracking=-1.2)
    draw_text(draw, (bx + brand_w + 1, cy), "_", credit_sans, ORANGE)

    rgb = img.convert("RGB")
    png = ASSETS / "banner.png"
    jpg = ASSETS / "banner.jpg"
    rgb.save(png, "PNG", optimize=True, compress_level=9)
    rgb.save(jpg, "JPEG", quality=90, optimize=True)
    print(f"wrote {png} ({png.stat().st_size} bytes)")
    print(f"wrote {jpg} ({jpg.stat().st_size} bytes)")

    thumb = Image.open(ASSETS / "agentr-mark.png").convert("RGBA")
    thumb.thumbnail((256, 256), Image.Resampling.LANCZOS)
    thumb.save(ASSETS / "agentr-mark-256.png", "PNG", optimize=True)
    print(f"wrote mark-256 ({(ASSETS / 'agentr-mark-256.png').stat().st_size} bytes)")


if __name__ == "__main__":
    main()
