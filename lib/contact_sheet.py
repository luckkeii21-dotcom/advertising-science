"""Build one labeled contact sheet from a frames dir so a model can read the
whole video's visual language in a single image.
Usage: python contact_sheet.py <frames_dir> <out.jpg> [every_nth] [cols]
"""
import os, sys
from PIL import Image, ImageDraw
d, out = sys.argv[1], sys.argv[2]
nth = int(sys.argv[3]) if len(sys.argv) > 3 else 6
cols = int(sys.argv[4]) if len(sys.argv) > 4 else 5
files = sorted(f for f in os.listdir(d) if f.endswith(".jpg"))[::nth]
ims = [Image.open(os.path.join(d, f)) for f in files]
TW, TH, PAD, LBL = 320, 180, 6, 18
rows = (len(ims) + cols - 1) // cols
sheet = Image.new("RGB", (cols*(TW+PAD)+PAD, rows*(TH+LBL+PAD)+PAD), (18, 18, 20))
dr = ImageDraw.Draw(sheet)
for i, (im, f) in enumerate(zip(ims, files)):
    x = PAD + (i % cols)*(TW+PAD)
    y = PAD + (i // cols)*(TH+LBL+PAD)
    sheet.paste(im.resize((TW, TH)), (x, y))
    dr.text((x+2, y+TH+3), f[:-4], fill=(235, 235, 235))
sheet.save(out, quality=90)
print(f"{len(ims)} frames -> {out} ({sheet.width}x{sheet.height})")
