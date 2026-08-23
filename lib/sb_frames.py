"""Explode a yt-dlp storyboard .mhtml into timestamped JPEG frames.

Usage: python sb_frames.py <sb.mhtml> <outdir> [tile_width]
  tile_width: sb0=320 (default), sb1=160, sb2=80, sb3=48

The mhtml parts are RAW JPEG bytes with no Content-Transfer-Encoding, so the
stdlib email parser mangles them. Split on the MIME boundary at the byte level
instead. Each part is one grid sheet; its X.yt-dlp.Duration header says how
many seconds that sheet covers. Frames are written named by real timestamp.
"""
import os, re, sys, io
from PIL import Image

src, outdir = sys.argv[1], sys.argv[2]
TW = int(sys.argv[3]) if len(sys.argv) > 3 else 320
TH = round(TW * 9 / 16)
os.makedirs(outdir, exist_ok=True)
raw = open(src, "rb").read()
m = re.search(rb'boundary="([^"]+)"', raw)
sep = b"--" + m.group(1)
t0, n, step = 0.0, 0, 0
for chunk in raw.split(sep)[1:]:
    head, _, body = chunk.partition(b"\r\n\r\n")
    if b"\r\n\r\n" not in chunk:
        head, _, body = chunk.partition(b"\n\n")
    if b"image/jpeg" not in head:
        continue
    d = re.search(rb"X\.yt-dlp\.Duration:\s*([\d.]+)", head)
    dur = float(d.group(1)) if d else 0.0
    body = body.rstrip(b"\r\n")
    sheet = Image.open(io.BytesIO(body))
    cols, rows = max(sheet.width // TW, 1), max(sheet.height // TH, 1)
    tiles = []
    for r in range(rows):
        for c in range(cols):
            t = sheet.crop((c*TW, r*TH, (c+1)*TW, (r+1)*TH))
            if t.convert("L").getextrema()[1] < 8:
                continue
            tiles.append(t)
    step = dur / max(len(tiles), 1)
    for i, t in enumerate(tiles):
        ts = int(t0 + i*step)
        t.save(os.path.join(outdir, f"{ts//60:02d}m{ts%60:02d}s.jpg"), quality=88)
        n += 1
    t0 += dur
print(f"{n} frames every ~{step:.1f}s -> {outdir}")
