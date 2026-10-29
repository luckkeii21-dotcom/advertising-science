# -*- coding: utf-8 -*-
# Research run 2026-10-29: write the meta-business-news key the checker does not write.
import io, json

P = r"E:\claude code marketing skill\.claude\skills\advertising-science\cache\watchlist-seen.json"

SLUGS_US = [
    "how-metas-ads-system-matches-your-ad-to-the-right-person",
    "three-new-ai-innovations-in-ads-ranking",
    "you-dont-beat-the-auction-you-brief-it",
    "muse-smb-jaeluxe-shoetique",
    "agencies-testing-incrementality",
    "meta-nest-ai-creative-diversification",
    "meta-brand-building-summit-2026",
    "muse-smb-bennett-orchards",
    "a-new-way-for-businesses-and-personal-agents-to-work-together",
    "advertising-week-new-york-2026",
    "agency-awards-2026",
    "introducing-meta-one-plans-for-businesses",
]

d = json.load(io.open(P, encoding='utf-8'))
mb = d["pages"]["meta-business-news"]

mb["slugs_us_2026_10_29"] = SLUGS_US
mb["last_checked"] = "2026-10-29"
mb["result_2026_10_29"] = (
    "TWO NEW, both dated 28 Oct 2026, both advertising, both read and banked. "
    "Ends seven consecutive flat days on this source. Added: "
    "how-metas-ads-system-matches-your-ad-to-the-right-person (banked MD-191, MD-192, AU-102; "
    "merged MD-022, MD-093, MD-188, SC-182) and three-new-ai-innovations-in-ads-ranking "
    "(banked MD-188, MD-191; merged MD-177, MD-186 contested). "
    "Dropped off the bottom of the twelve-item shelf: "
    "iab-global-creator-week-making-it-easier-for-businesses-to-partner-with-creators and "
    "performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale, both already in "
    "slugs_seen_cumulative. Shelf stays twelve items. "
    "Transport: plain curl returns HTTP 200 today (400 yesterday) but serves a 1,542-byte JS stub "
    "with zero slugs, so the 200 is not a usable read. Shelf read via WebFetch on ?locale=en_US. "
    "UK shelf not read this pass."
)

cum = set(mb.get("slugs_seen_cumulative", []))
before = len(cum)
cum.update(SLUGS_US)
mb["slugs_seen_cumulative"] = sorted(cum)

json.dump(d, io.open(P, 'w', encoding='utf-8', newline='\n'), indent=2, ensure_ascii=False)

# read back to verify
d2 = json.load(io.open(P, encoding='utf-8'))
mb2 = d2["pages"]["meta-business-news"]
assert mb2["last_checked"] == "2026-10-29"
assert mb2["slugs_us_2026_10_29"] == SLUGS_US
print("key written and verified. last_checked=%s, slugs=%d, cumulative %d -> %d"
      % (mb2["last_checked"], len(mb2["slugs_us_2026_10_29"]), before,
         len(mb2["slugs_seen_cumulative"])))
