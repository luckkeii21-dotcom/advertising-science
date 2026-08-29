import re, pathlib, json
root = pathlib.Path(r'Obsidian God-level Marketing Vault/God-level Marketing/wiki/sources/transcripts')
picks = [
 "Mastering the Cash Conversion Cycle",
 "How To Breakdown An eCommerce PL As A Marketer - Part 3",
 "Where To Allocate Agency Fees",
 "The Two Highest ROI Activities",
 "Seperate's 7 & 8 Figure", "Seperates 7  8 Figure",
 "An Agency Doesnt Create Business Growth", "An Agency Doesn't Create",
 "What Metrics Matter In The Shopify Analytics",
 "How To Increase Margin While Discounting",
 "How to Improve Profit When Flat Discounting",
 "Why eCommerce Is So Difficult",
 "How We Accelerated KOOKA",
 "Blue Illusion",
 "4 Changes That Recovered",
 "You Are Getting This Wrong",
 "The Most Important Lever for eCommerce Subscription",
 "Why eCommerce Brands Fail To Launch Into The USA",
 "The 3 Pillars to A Successful US Launch",
 "VIRAL AI Claymation",
 "Pixar Style Ad in 30 Minutes",
 "Canva Layers Update",
 "Seedance 2.0 to Create AI UGC",
 "How to use AI to Copy Winning Ads",
 "Academy News #9",
]
found = {}
for p in root.rglob('*.md'):
    t = p.read_text(encoding='utf-8', errors='replace')
    if 'extracted: false' not in t:
        continue
    for k in picks:
        norm = re.sub(r'[^a-z0-9]', '', k.lower())
        if norm in re.sub(r'[^a-z0-9]', '', p.name.lower()):
            found.setdefault(k, str(p))
print(json.dumps(found, indent=1))
print('matched', len(set(found.values())))
