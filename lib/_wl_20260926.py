# -*- coding: utf-8 -*-
"""2026-09-26: write today's browser reads into the watchlist cache.

watchlist_check.py --commit covers the fetchable lanes. The two Meta for
Business News locales are browser-only, and the Demand Gen Drops hub backlog
closed today, so both are recorded by hand here.
"""
import json, pathlib
from datetime import datetime

SEEN = pathlib.Path(".claude/skills/advertising-science/cache/watchlist-seen.json")

US = [
    "Meet the 2026 Meta Agency Award Winners",
    "Introducing Meta One plans for businesses",
    "IAB Global Creator Week: Making it Easier for Businesses to Partner with Creators and Turn Discovery into Purchase",
    "Performance Spotlight: How Instant Hydration Built a System for AI to Scale",
    "How Businesses Are Driving Results with Meta's AI-Powered Ads",
    "Small to Scale: How Sydney Sock Project Scaled a Cause",
    "New Meta AI Features for Small Businesses",
    "Game Changers: Why the fastest-growing audience in sports lives across Meta technologies",
    "Performance Spotlight: How Laura Geller Turned Creative Volume and AI Into a Competitive Edge",
    "How do advertisers increase holiday ad budgets?",
    "Win over shoppers with ad formats they're engaging with",
    "Get your holiday ads in front of high-intent shoppers",
]

UK = [
    "Performance Spotlight: How Instant Hydration Built a System for AI to Scale",
    "How businesses are driving results with Meta's AI-powered ads",
    "Closing the creator measurement gap: How L'Oreal turned a reporting function into a strategic lever for growth",
    "How winning hearts before peak season boosts baskets when it matters most",
    "Conversations 2026: Introducing Meta Business Agent",
    "How to optimise content for social search on Meta technologies",
    "The trends reshaping search and the ROI that justifies moving now",
    "Why social search and traditional search aren't in competition - they coexist",
    "Performance Spotlight: Trends from Around the World",
    "Meta Growth Drivers: Putting Your Digital Marketing Strategy on \"Auto-Pilot\"",
    "Cyber 5 2025: What worked, what changed and how to win Q5",
    "Unlocking the Value of Q5 Marketing for Mobile Game Developers",
]


def main():
    d = json.loads(SEEN.read_text(encoding="utf-8-sig"))
    pages = d.setdefault("pages", {})

    prev = pages.get("meta-business-news", {})
    us_new = sorted(set(US) - set(prev.get("titles_us", [])))
    us_gone = sorted(set(prev.get("titles_us", [])) - set(US))
    uk_new = sorted(set(UK) - set(prev.get("titles_uk", [])))
    uk_gone = sorted(set(prev.get("titles_uk", [])) - set(UK))

    pages["meta-business-news"] = {
        "last_checked": "2026-09-26",
        "method": "browser (playwright), BOTH locales, TITLE-set diff",
        "result": (
            "US 12 titles, %d new, %d removed, ceiling 21 Sep 2026; "
            "UK 12 titles, %d new, %d removed, top card rendered 11 Sep 2026 today "
            "against 10 Sep yesterday, same post, one-day drift artefact"
            % (len(us_new), len(us_gone), len(uk_new), len(uk_gone))
        ),
        "titles_us": US,
        "titles_uk": UK,
    }

    pages["demand-gen-drops-hub"] = {
        "last_checked": "2026-09-26",
        "url": "https://business.google.com/us/accelerate/demand-gen-drops/",
        "method": "plain fetch HTTP 200; body anchored on 'Social Module' to 'Return to top of page'",
        "result": (
            "BACKLOG CLOSED. All 13 instalments read (intro 2025-09-01 plus 11 monthly "
            "drops plus the Sep 2026 drop on blog.google). Hub lists 12; it lags the blog "
            "by about a month. Watch the Ads & Commerce RSS for new drops, not this page."
        ),
        "instalments_read": [
            "intro 2025-09-01", "2025-10-13", "2025-11-17", "2025-12-11", "2026-01-22",
            "2026-02-24", "2026-03-26", "2026-04-23", "2026-05 (read 09-25)",
            "2026-06-25", "2026-07 (read 09-25)", "2026-08-27 (blog)", "2026-09-24 (blog)",
        ],
    }

    d["last_run"] = datetime.now().strftime("%Y-%m-%dT%H:%M IST")
    SEEN.write_text(json.dumps(d, indent=2), encoding="utf-8")
    print("US new %d removed %d | UK new %d removed %d" % (len(us_new), len(us_gone), len(uk_new), len(uk_gone)))
    print("last_run", d["last_run"])


if __name__ == "__main__":
    main()
