# -*- coding: utf-8 -*-
"""2026-10-24: record the Meta for Business News US-shelf read in the cache."""
import json
from pathlib import Path

P = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\cache\watchlist-seen.json")
d = json.loads(P.read_text(encoding="utf-8"))
m = d["pages"]["meta-business-news"]

US = [
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
    "iab-global-creator-week-making-it-easier-for-businesses-to-partner-with-creators",
    "performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
]

m["slugs_us_2026_10_24"] = US
cum = m.setdefault("slugs_seen_cumulative", [])
added = [s for s in US if s not in cum]
cum.extend(added)
m["last_checked"] = "2026-10-24"
m["method"] = ("Playwright browser, ?locale=en_US, SLUG set diff against slugs_seen_cumulative. "
               "A plain HTTPS fetch returned HTTP 400 again on 2026-10-24, both bare and with "
               "?locale=en_US, so the browser is required for this source. Never read the bare URL: "
               "from our egress it is an INDIA shelf.")
m["result"] = ("US shelf read in the browser, 12 slugs. 1 GENUINELY NEW at slot 1: "
               "you-dont-beat-the-auction-you-brief-it, Best Practice, dated 21 October 2026, absent "
               "from slugs_seen_cumulative. Opened and read in full. Banked as LS-089, LS-090, MD-187, "
               "AT-132, with merges into LS-001 and MD-171. Ceiling 21 October 2026, up from "
               "19 October. UK shelf NOT read this pass, so the UK ceiling is unverified since "
               "2026-10-20. Gap recorded in the run log.")
m["note_2026_10_24"] = ("The 2026-10-23 run log states the cache was committed and it was NOT: the file "
                        "mtime was 21 Oct 15:13 and the 23 Oct findings (the Google holiday-bidding "
                        "teaser, the arXiv OneLatent re-submission, a Meta Newsroom Forum admin post) "
                        "all resurfaced as new on 24 Oct. They were re-dispositioned against the 23 Oct "
                        "log rather than re-banked, and the cache is committed today. A run log claiming "
                        "a commit is not evidence of one; check the file mtime.")
m["note_2026_10_24_added"] = added

P.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")
print("OK  cache updated. cumulative %d -> %d, added: %s" % (len(cum) - len(added), len(cum), added))
