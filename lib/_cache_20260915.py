# -*- coding: utf-8 -*-
"""2026-09-15: give Meta for Business News a real TITLE baseline.

The 2026-09-14 rule says diff this source on post TITLE, because the link set
rotates and the card dates drift by a day. No title baseline had ever been
stored, so the rule had nothing to diff against. This writes one.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
SEEN = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science"
            r"\cache\watchlist-seen.json")

# Read from the live listing at 13:30 IST 2026-09-15 via the Playwright browser.
CARDS = [
    ("2026-09-11", "Performance Spotlight: How Instant Hydration Built a System for AI to Scale"),
    ("2026-09-03", "How Businesses Are Driving Results with Meta's AI-Powered Ads"),
    ("2026-08-26", "Small to Scale: How Sydney Sock Project Scaled a Cause"),
    ("2026-08-19", "New Meta AI Features for Small Businesses"),
    ("2026-08-19", "Game Changers: Why the fastest-growing audience in sports lives across Meta technologies"),
    ("2026-08-12", "Performance Spotlight: How Laura Geller Turned Creative Volume and AI Into a Competitive Edge"),
    ("2026-08-11", "How do advertisers increase holiday ad budgets?"),
    ("2026-08-11", "Win over shoppers with ad formats they\u2019re engaging with"),
    ("2026-08-11", "Get your holiday ads in front of high-intent shoppers"),
    ("2026-08-07", "Performance Spotlight: What Your CFO Actually Wants to Hear About Marketing with Common Thread Collective"),
    ("2026-07-28", "Getting Your Small Business Holiday-Ready: Free Insights, AI Tools, and a Playbook to Help You Grow"),
    ("2026-07-15", "Small to Scale: How ROBINMAY Used Reels to Unlock a New Audience and a New Market"),
]

d = json.loads(SEEN.read_text(encoding="utf-8-sig"))
rec = d["pages"]["meta-business-news"]
rec["last_checked"] = "2026-09-15"
rec["method"] = ("Playwright MCP profile 'playwright', opened first try. Diff on post TITLE "
                 "per the 2026-09-14 rule: the link set rotates and the card dates drift by a "
                 "day, so neither is a stable key. Read the date only to decide whether a "
                 "genuinely new title is worth opening.")
rec["result"] = ("2026-09-15: 12 cards, TITLE set identical to 2026-09-14 and 2026-09-13. Zero new. "
                 "All five dates that drifted one day earlier on 2026-09-14 drifted back today, "
                 "confirming the drift is a rendering artefact and titles are the stable key. "
                 "Newest post still 11 September 2026, banked 2026-09-13 at AT-117, CR-232, CR-233.")
rec["newest_post_seen"] = "2026-09-11"
rec["titles_2026_09_15"] = [t for _, t in CARDS]
rec["dates_2026_09_15"] = {t: dt for dt, t in CARDS}
rec["baseline_note"] = ("TITLE BASELINE SEEDED 2026-09-15. Before today this record still held the "
                        "2026-09-07 slug set, eight days stale, because the 09-10 through 09-14 runs "
                        "read the page in the browser and never wrote back. Compare "
                        "titles_2026_09_15 first; anything not in that list is a candidate, and only "
                        "then open it and read its date.")
d["last_run"] = "2026-09-15T13:40 IST"
SEEN.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
print("meta-business-news title baseline seeded,", len(CARDS), "titles")
