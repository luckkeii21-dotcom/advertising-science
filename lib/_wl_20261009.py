import json, pathlib
C = pathlib.Path(__file__).resolve().parent.parent / "cache" / "watchlist-seen.json"
d = json.loads(C.read_text(encoding="utf-8-sig"))
p = d["pages"].setdefault("meta-business-news", {})

us = ['muse-smb-bennett-orchards','a-new-way-for-businesses-and-personal-agents-to-work-together',
      'advertising-week-new-york-2026','agency-awards-2026','introducing-meta-one-plans-for-businesses',
      'iab-global-creator-week-making-it-easier-for-businesses-to-partner-with-creators',
      'performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale',
      'businesses-driving-results-with-meta-ai-ads','sydney-sock-project-scaled-cause',
      'meta-ai-for-small-businesses','game-changers-series-1','laura-geller-creative-volume']
uk = ['performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale',
      'businesses-driving-results-with-meta-ai-ads','closing-the-creator-measurement-gap',
      '2026-winning-hearts-boosting-carts','conversations-2026-introducing-meta-business-agent',
      'social-search-series-2','social-search-series-3','social-search-series-1',
      '2026-trends-from-around-the-world',
      'meta-growth-drivers-putting-your-digital-marketing-strategy-on-auto-pilot',
      'cyber-5-2025-what-worked','unlocking-the-value-of-q5marketing-for-mobile-game-developers']

p["last_checked"] = "2026-10-09"
p["slugs_us_2026_10_09"] = us
p["slugs_uk_2026_10_09"] = uk
p["result"] = ("US 12 slugs, 1 ADDED 1 removed: muse-smb-bennett-orchards in (8 Oct 2026, read in full, "
               "no advertising content, filed as a watch note on MD-169), holiday-measurement-strategies "
               "rotated out. US ceiling MOVED from 6 October to 8 October 2026. UK 12 slugs, 1 added 1 "
               "removed and both are rotation, not news: unlocking-the-value-of-q5marketing-for-mobile-game-developers "
               "(10 Oct 2025) rotated back in and creator-marketing-whitepaper rotated out, so the UK ceiling "
               "fell back from 6 October to 10 September 2026.")
p["note_2026_10_09"] = ("A UK slug can rotate BACK IN after rotating out, and the shelf ceiling can go "
                        "BACKWARDS as a result. creator-marketing-whitepaper was the 2026-10-08 UK addition "
                        "and is gone today, with a 2025 post in its place. Every earlier note here treats the "
                        "ceiling as monotonic. It is not. Never report a ceiling drop on this source as a "
                        "removal or a retraction: the module is a rotating slice of the back catalogue and the "
                        "post is still live at its own URL. US-to-UK ceiling gap is 28 days today against 11 "
                        "days on 2026-10-02, and the gap is a reading artefact of the rotation, not a "
                        "publishing-cadence measurement.")
C.write_text(json.dumps(d, indent=2), encoding="utf-8")
print("meta-business-news baselines recorded for 2026-10-09")
