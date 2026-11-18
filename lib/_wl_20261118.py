# -*- coding: utf-8 -*-
"""Record the 2026-11-18 manual lane: Meta for Business News shelves, and mark the transcript extracted."""
import json
import shutil
from pathlib import Path

ROOT = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science")
SEEN = ROOT / "cache" / "watchlist-seen.json"
TR = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing"
         r"\wiki\sources\transcripts\ben-heath"
         r"\2026-11-17--ben-heath--Facebook Ads Super Burst Just Launched.md")

us = ["from-measurement-to-capital-allocation", "finding-his-squad-again-in-a-facebook-group",
      "how-metas-ads-system-matches-your-ad-to-the-right-person", "three-new-ai-innovations-in-ads-ranking",
      "you-dont-beat-the-auction-you-brief-it", "muse-smb-jaeluxe-shoetique",
      "agencies-testing-incrementality", "meta-nest-ai-creative-diversification",
      "meta-brand-building-summit-2026", "muse-smb-bennett-orchards",
      "a-new-way-for-businesses-and-personal-agents-to-work-together",
      "advertising-week-new-york-2026"]
uk = ["meta-ai-now-available-in-hongkong", "meta-agency-first-awards-winners-hongkong-2026",
      "meta-marketing-summit-hongkong-2026", "you-dont-beat-the-auction-you-brief-it",
      "performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
      "businesses-driving-results-with-meta-ai-ads", "closing-the-creator-measurement-gap",
      "2026-winning-hearts-boosting-carts", "conversations-2026-introducing-meta-business-agent",
      "social-search-series-2", "social-search-series-3", "social-search-series-1"]

d = json.loads(SEEN.read_text(encoding="utf-8"))
bn = d["pages"]["meta-business-news"]
cum = set(bn["slugs_seen_cumulative"])
assert not [s for s in us + uk if s not in cum], "unexpected new slug"

bn["last_checked"] = "2026-11-18"
bn["slugs_us_2026_11_18"] = us
bn["slugs_uk_2026_11_18"] = uk
bn["result_2026_11_18"] = (
    "Plain fetch HTTP 400 on BOTH pinned URLs, so route step 2, WebFetch, read both. "
    "US 12 slugs, newest 12 Nov 2026, identical in set and order to 11-16. "
    "UK 12 slugs, newest 27 Oct 2026, the 2026-10-31/11-08 ordered state. "
    "0 new against slugs_seen_cumulative, which stays at 41. "
    "Playwright MCP unavailable this session (connect timeout, all profiles), so one read only; "
    "the two-read UK rule of 2026-11-10 pass 2 was not satisfied and today is one sample, not full UK coverage."
)
bn["note_2026_11_18_muse_australia"] = (
    "Meta Newsroom item 'Muse Is Now Available in Australia', 17 Nov 2026, opened and read in full "
    "because MD-181 holds a business-and-personal-agents post. No advertising content: the only 'ads' "
    "strings on the page are the cookie banner and a footer link. Connectors run one way, a person's "
    "agent out to named partner apps (Canva, Kogan, MECCA, Officeworks, Ticketek, ShopBack and others), "
    "with no business onboarding, no lead capture and no directory. Not banked."
)
shutil.copy(SEEN, str(SEEN) + ".bak-20261118")
SEEN.write_text(json.dumps(d, indent=2), encoding="utf-8")
print("seen cache updated; cumulative still", len(cum))

t = TR.read_text(encoding="utf-8")
assert "extracted: false" in t
TR.write_text(t.replace("extracted: false", "extracted: true", 1), encoding="utf-8")
print("transcript marked extracted")
