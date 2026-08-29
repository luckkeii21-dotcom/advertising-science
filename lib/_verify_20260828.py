import pathlib, re, sys
R = pathlib.Path(r'Obsidian God-level Marketing Vault/God-level Marketing/wiki/sources/transcripts')
CH = {p.name: p for p in R.iterdir() if p.is_dir()}
def find(chan, frag):
    hits = []
    for p in CH[chan].rglob('*.md'):
        t = p.read_text(encoding='utf-8', errors='replace')
        if frag.lower() in re.sub(r'\s+',' ',t).lower():
            hits.append(p.name)
    return hits
CHECKS = [
 ('nick-theriot', '97% of our accounts use a CBO campaign'),
 ('nick-theriot', 'spends over $5 million a month on ads'),
 ('nick-theriot', 'three times account average'),
 ('nick-theriot', 'it takes about 72 hours for Facebook to fully optimize'),
 ('nick-theriot', '20% a day is pretty average'),
 ('nick-theriot', 'nine times out of ten we\u2019re wrong'),
 ('nick-theriot', 'this is probably a scenario that happens maybe 20% of the time'),
 ('bluesense-digital', 'a regular hit rate for an e-commerce brand sits at about 15%'),
 ('bluesense-digital', 'each individual ad unit has a maximum spend threshold'),
 ('bluesense-digital', 'You will never have a duplicated ad set perform consistently'),
 ('bluesense-digital', 'attribution is an unknowable reality'),
 ('bluesense-digital', 'we have taken existing customer lists, spent more on them'),
 ('bluesense-digital', '70% of budgets on existing customers'),
 ('bluesense-digital', 'They actually didn\u2019t even have audience segments defined in Meta'),
 ('bluesense-digital', 'incremental ROI of 5.6'),
 ('bluesense-digital', 'you really need to be able to spend at least 25% of your revenue on marketing'),
 ('bluesense-digital', 'break even rorowaz increases relatively linearly'),
 ('bluesense-digital', 'do not launch in the US unless you\u2019re doing at bare minimum 3 mil'),
 ('bluesense-digital', 'the key to growth is usually not diversification'),
 ('bluesense-digital', 'they were spending $20,000 a month. There should have been probably 200 active creative'),
 ('bluesense-digital', 'scaling isn\u2019t just increasing spend'),
 ('bluesense-digital', 'It is physically impossible for your sales to decrease'),
 ('bluesense-digital', 'Shopify for whatever reason decides to keep all of the bot traffic'),
 ('fraser-cottrell', 'we\u2019re normally going back and doing label replacement'),
 ('fraser-cottrell', 'you can\u2019t upload references of people'),
 ('fraser-cottrell', 'we pretty much stay away from using AI when it comes to health and wellness'),
 ('fraser-cottrell', 'images are much cheaper to generate than video'),
 ('charley-t', 'optimizing for the ad that is closest to converting'),
 ('charley-t', 'getting bigger by being smaller'),
 ('matt-shiver', 'at least one times your cost per call'),
]
bad = 0
for chan, frag in CHECKS:
    h = find(chan, frag)
    ok = 'OK ' if h else 'MISS'
    if not h: bad += 1
    print(f'{ok} [{chan}] "{frag[:62]}" -> {h[:1]}')
print()
print('misses:', bad, 'of', len(CHECKS))
