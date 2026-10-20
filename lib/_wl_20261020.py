# -*- coding: utf-8 -*-
"""Meta for Business News shelf state for 2026-10-20, both locales, read via WebFetch."""
import json
from pathlib import Path

SEEN = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science"
            r"\cache\watchlist-seen.json")
TODAY = "2026-10-20"

US = [
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
    "sydney-sock-project-scaled-cause",
]
UK = [
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

RESULT = (
    "US shelf MOVED and the added slug is GENUINELY NEW, not a rotation: "
    "agencies-testing-incrementality, dated 19 October 2026, absent from slugs_seen_cumulative, "
    "arrived at slot 1 and meta-ai-for-small-businesses dropped off the bottom. 1 added, 1 removed, "
    "ceiling 19 October 2026. The post was opened and read in full and is banked at AT-131: four "
    "agency lift studies, eleven numbers, no footnote, no sample, no window and no spend. UK shelf "
    "identical in order to the 2026-10-19 FIRST pass, 12 slugs, 0 added 0 removed, ceiling still 10 "
    "September 2026. Against the 2026-10-19 SECOND pass it is 1 added "
    "(unlocking-the-value-of-q5marketing) and 1 removed (creator-marketing-whitepaper), which is the "
    "known slot-1 toggle inside a 12-slot window and banks nothing. Method note that held today: a "
    "1-in-1-out diff on the US shelf is NOT automatically a rotation. Checking the added slug against "
    "slugs_seen_cumulative is what separated a real post from a returning card, and it cost one "
    "lookup."
)


def main():
    seen = json.loads(SEEN.read_text(encoding="utf-8-sig"))
    bn = seen["pages"]["meta-business-news"]
    bn[f"slugs_us_{TODAY.replace('-', '_')}"] = US
    bn[f"slugs_uk_{TODAY.replace('-', '_')}"] = UK
    bn["slugs_seen_cumulative"] = sorted(set(bn.get("slugs_seen_cumulative", [])) | set(US) | set(UK))
    bn["last_checked"] = TODAY
    bn["result"] = RESULT
    for k in ("tiktok-newsroom", "tiktok-business-blog"):
        seen["pages"][k][f"note_{TODAY.replace('-', '_')}"] = (
            "NOT retried. India geo-block, verified 2026-08-19 across browser and curl on four paths "
            "each. Not an outage.")
    seen["last_run"] = TODAY + "T15:30 IST"
    SEEN.write_text(json.dumps(seen, indent=2), encoding="utf-8")
    print("business-news shelf state written;",
          len(bn["slugs_seen_cumulative"]), "slugs seen cumulatively")


if __name__ == "__main__":
    main()
