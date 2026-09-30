"""Commit the 2026-09-30 Meta for Business News read and file the transport finding."""
import json
from pathlib import Path

SKILL = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science")
WL = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\Watchlist.md")

US_TODAY = [
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

seen_path = SKILL / "cache" / "watchlist-seen.json"
seen = json.loads(seen_path.read_text(encoding="utf-8"))
page = seen.setdefault("pages", {}).setdefault("meta-business-news", {})

cached_us = page.get("titles_us") or []
added = [t for t in US_TODAY if t not in cached_us]
removed = [t for t in cached_us if t not in US_TODAY]

page["last_checked"] = "2026-09-30"
page["method"] = "WebFetch with ?locale=en_US; TITLE set diff. Browser unavailable, all 4 Playwright profiles CONNECT_TIMEOUT"
page["titles_us"] = US_TODAY
page["result"] = (
    "US 12 titles, %d added, %d removed, set identical to 2026-09-28 baseline. Ceiling holds at 21 September 2026. "
    "UK NOT READ: the bare URL renders the INDIA catalogue in Hindi from our egress, so titles_uk is left at its "
    "2026-09-28 value and is now 2 days stale." % (len(added), len(removed))
)
seen_path.write_text(json.dumps(seen, indent=2), encoding="utf-8")
print("cache: US %d titles, %d added, %d removed. titles_uk left untouched." % (len(US_TODAY), len(added), len(removed)))

NOTE = """
### The US shelf IS readable on a zero-browser day, through WebFetch with `?locale=en_US` (found 2026-09-30)

The 2026-09-22 entry above rules that "the whole Meta lane is unreadable when no Playwright profile connects", on the
evidence that every Meta property this watchlist tracks serves HTTP 400 to a plain fetch. **That ruling is about PLAIN
FETCH and it over-reaches to the lane.** Today all four Playwright profiles failed CONNECT_TIMEOUT at session start, a
plain fetch returned HTTP 400 on both Business News URLs, and **WebFetch rendered `?locale=en_US` in English (US) with
all 12 card titles and dates**. Diffed against `pages.meta-business-news.titles_us`: **0 added, 0 removed, set identical
to the 2026-09-28 baseline.** Ceiling holds at 21 September 2026, "Meet the 2026 Meta Agency Award Winners".

That is the first clean title-set diff ever run on the US lane without a browser, and it makes the most important source
on this watchlist browser-optional rather than browser-only.

**The `?locale=en_US` parameter is load-bearing and yesterday's run is the control.** On 2026-09-29 WebFetch was pointed
at the bare URL and rendered the India catalogue, which that run correctly refused to commit. Today the bare URL did the
same thing again, in Hindi, while the parameterised URL rendered US English in the same session. **The parameter
controls the render. The absence of it does not fall back to UK or to US, it falls back to our egress.**

### The bare URL does NOT give us the UK shelf, so `titles_uk` cannot be diffed from here without a browser (2026-09-30)

The 2026-09-20 standing instruction says to read BOTH the bare URL and `?locale=en_US` every day and diff the two title
sets separately, on the finding that the bare URL "renders en_GB from our New Delhi egress". **That was true on
2026-09-20 and it is not a property of the URL.** The bare URL rendered Hindi/India on 2026-09-29 and again on
2026-09-30, and the India catalogue is a third shelf, not the UK one.

Today's India set against the cached UK set: **8 of 12 titles overlap** (Instant Hydration, Meta AI ads, winning hearts
before peak season, Conversations 2026, optimise content for social search, trends reshaping search, why social search
and traditional search coexist, Cyber 5 2025). The four that do not are all back catalogue: 15 September 2025,
17 June 2024, 28 February 2023, 29 July 2022. **Byte-for-byte the same 8-and-4 split as 2026-09-29**, so the India shelf
is stable day over day and is not quietly rotating past us.

**Standing instruction, amended.** Read `?locale=en_US` and diff it against `titles_us`; that lane works with or without
a browser. **A bare-URL read from our egress is an INDIA read and must never be committed against `titles_uk`.** The UK
shelf needs a browser with an explicit `en-gb` path, or a UK egress. Until one of those runs, log the UK lane as not
checked and say how stale the baseline is, rather than logging the source as clean.

### Meta's HTTP 400 pages can be 267 KB and still contain nothing (2026-09-30)

Recorded so no future run chases the byte count. `transparency.meta.com/policies/ad-standards/` returned **HTTP 400 with
a 266,875-byte body** on a plain fetch, against the 1,542-byte error body the 2026-09-22 entry records for
`facebook.com/business/news`. The large body looks like a successful render and is not one: strip scripts and tags and
**the visible text is 7 characters and reads "Error"**. None of the 16 section names appears. Both localess behaved the
same way. **Judge a Meta 400 on its rendered text, never on its content length.**
"""

body = WL.read_bytes()
nl = "\r\n" if b"\r\n" in body else "\n"
text = body.decode("utf-8").replace("\r\n", "\n").rstrip("\n")
text = text + "\n" + NOTE
WL.write_bytes(text.replace("\n", nl).encode("utf-8"))
print("Watchlist.md: 3 method notes appended")
