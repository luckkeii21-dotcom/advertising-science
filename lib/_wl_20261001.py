# -*- coding: utf-8 -*-
"""2026-10-01: mark transcript extracted, ship the ad-hoc arXiv filter fix, commit the
Meta Business News slug baselines for BOTH locales (first browser-free UK read)."""
import json
import re
from pathlib import Path

ROOT = Path("E:/claude code marketing skill")
SKILL = ROOT / ".claude/skills/advertising-science"

# ---------------------------------------------------------- 1. transcript extracted
tr = (ROOT / "Obsidian God-level Marketing Vault/God-level Marketing/wiki/sources/transcripts"
      / "jon-loomer" / "2026-09-30--jon-loomer--An Ad Solution for Metas Restriction on Organic Link Sharing.md")
t = tr.read_text(encoding="utf-8")
assert "extracted: false" in t
tr.write_text(t.replace("extracted: false", "extracted: true", 1), encoding="utf-8")
print("transcript marked extracted: true")

# ------------------------------------------- 2. arXiv filter: exclude "ad-hoc" / "ad hoc"
wc = SKILL / "lib/watchlist_check.py"
s = wc.read_text(encoding="utf-8")
old = '    r"advertis", r"\\bads?\\b", r"ad auction", r"sponsored",'
new = ('    # "ad-hoc" / "ad hoc" excluded 2026-10-01: the hyphen is a word boundary, so\n'
       '    # \\bads?\\b matched the "ad" in "ad-hoc heuristics" in the GEAR abstract. The\n'
       '    # whole-word rule in Watchlist.md was written against substring matches\n'
       '    # (adaptive, advanced, gradient) and does not catch this one. Narrow literal\n'
       '    # exclusion only: "ad-level", "ad-set" and "ad auction" stay genuine.\n'
       '    r"advertis", r"\\bads?\\b(?![- ]hoc)", r"ad auction", r"sponsored",')
assert s.count(old) == 1, "anchor not unique"
wc.write_text(s.replace(old, new), encoding="utf-8")

BANK = re.compile("|".join([
    r"advertis", r"\bads?\b(?![- ]hoc)", r"ad auction", r"sponsored",
    r"CTR prediction", r"bid landscape", r"bidding", r"conversion lift",
    r"incrementality", r"budget pacing", r"creative selection", r"\bGSP\b",
    r"second-price",
]), re.I)
cases = [
    ("pure recsys using 'ad-hoc' once", "We stabilise gradient dynamics without ad-hoc heuristics for retrieval.", False),
    ("pure recsys using 'ad hoc' once", "An ad hoc rule is replaced by a learned ranker.", False),
    ("GEAR (genuine)", "Generative End-to-end Ad Retrieval at Douyin. Serves users on Douyin Ads without ad-hoc heuristics.", True),
    ("Interactor (genuine)", "Ad description generation in sponsored search, serving 140k advertisers.", True),
    ("ad-level wording stays genuine", "We report ad-level calibration for the auction.", True),
]
ok = True
for label, txt, want in cases:
    got = bool(BANK.search(txt))
    ok &= got == want
    print(f"   filter test {'PASS' if got == want else 'FAIL'}: {label} -> {got} (want {want})")
assert ok, "filter regression"
print("arXiv filter fix shipped and tested")

# ------------------------------------------- 3. Meta Business News slug baselines, both locales
SLUGS_US = [
    "agency-awards-2026",
    "introducing-meta-one-plans-for-businesses",
    "iab-global-creator-week-making-it-easier-for-businesses-to-partner-with-creators",
    "performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
    "businesses-driving-results-with-meta-ai-ads",
    "sydney-sock-project-scaled-cause",
    "meta-ai-for-small-businesses",
    "game-changers-series-1",
    "laura-geller-creative-volume",
    "holiday-measurement-strategies",
    "holiday-advantage-is-creative-advantage",
    "skip-the-single-surface-holiday-strategy",
]
SLUGS_UK = [
    "performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
    "businesses-driving-results-with-meta-ai-ads",
    "closing-the-creator-measurement-gap",
    "2026-winning-hearts-boosting-carts",
    "conversations-2026-introducing-meta-business-agent",
    "social-search-series-2",
    "social-search-series-3",
    "social-search-series-1",
    "2026-trends-from-around-the-world",
    "meta-growth-drivers-putting-your-digital-marketing-strategy-on-auto-pilot",
    "cyber-5-2025-what-worked",
    "unlocking-the-value-of-q5marketing-for-mobile-game-developers",
]
seen_p = SKILL / "cache/watchlist-seen.json"
seen = json.loads(seen_p.read_text(encoding="utf-8-sig"))
mb = seen["pages"]["meta-business-news"]


def norm(x):
    return x.strip().rstrip("/").split("/business/news/")[-1]


base_us = {norm(x) for x in mb["slugs_us_2026_09_28"]}
base_uk = {norm(x) for x in mb["slugs_uk_2026_09_28"]}
assert set(SLUGS_US) == base_us, sorted(set(SLUGS_US) ^ base_us)
assert set(SLUGS_UK) == base_uk, sorted(set(SLUGS_UK) ^ base_uk)
print("slug diff verified: US 0 added 0 removed, UK 0 added 0 removed")

mb.update({
    "last_checked": "2026-10-01",
    "method": ("WebFetch with ?locale=en_US AND ?locale=en_GB; SLUG set diff. No browser needed: "
               "all 4 Playwright profiles CONNECT_TIMEOUT and both shelves still read clean."),
    "result": ("US 12 slugs 0 added 0 removed, ceiling 21 September 2026. UK 12 slugs 0 added 0 removed, "
               "ceiling 10 September 2026. FIRST browser-free UK read: ?locale=en_GB renders English (UK), "
               "retiring the 2026-09-30 ruling that the UK shelf needs a browser or a UK egress."),
    "slugs_us_2026_10_01": SLUGS_US,
    "slugs_uk_2026_10_01": SLUGS_UK,
    "note_2026_10_01": ("?locale=en_GB is the UK key and WebFetch renders it. The bare URL is still an INDIA "
                        "read from our egress and must never be committed against the UK baseline. "
                        "US-to-UK ceiling gap is 11 days, unchanged from 2026-09-23."),
})
seen_p.write_text(json.dumps(seen, indent=2), encoding="utf-8")
print("meta-business-news baselines committed for both locales")
