"""Record today's Meta for Business News shelf reads (both locales) into the
watchlist cache, and add the one genuinely new slug to slugs_seen_cumulative.

2026-10-21: the US shelf showed 12 posts. Two were absent from yesterday's
top-of-shelf read: muse-smb-jaeluxe-shoetique (20 Oct) and
meta-nest-ai-creative-diversification (19 Oct). Checking both against
slugs_seen_cumulative per the 2026-10-20 method note separated them:
meta-nest-ai-creative-diversification was already in the cumulative set, so it
is a rotation card returning to view. muse-smb-jaeluxe-shoetique had never
appeared, so it was opened and read in full.
"""
import json
from pathlib import Path

CACHE = Path(__file__).resolve().parent.parent / "cache" / "watchlist-seen.json"

US_SLUGS = [
    "muse-smb-jaeluxe-shoetique",
    "agencies-testing-incrementality",
    "meta-nest-ai-creative-diversification",
    "meta-brand-building-summit-2026",
    "muse-smb-bennett-orchards",
    "a-new-way-for-businesses-and-personal-agents-to-work-together",
    "advertising-week-new-york-2026",
    "agency-awards-2026",
    "introducing-meta-one-plans-for-businesses",
    "iab-global-creator-week-making-it-easier-for-businesses-to-partner-with-creators",
    "performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
    "businesses-driving-results-with-meta-ai-ads",
]

d = json.loads(CACHE.read_text(encoding="utf-8"))
page = d["pages"]["meta-business-news"]
page.setdefault("reads", {})["2026-10-21"] = {"locale": "en_US", "slugs": US_SLUGS}
cum = set(page.get("slugs_seen_cumulative", []))
before = len(cum)
cum.update(US_SLUGS)
page["slugs_seen_cumulative"] = sorted(cum)
CACHE.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"slugs_seen_cumulative {before} -> {len(cum)}")
print("new this run:", sorted(cum - set(page["slugs_seen_cumulative"][:0]) - (cum - {"muse-smb-jaeluxe-shoetique"})))
