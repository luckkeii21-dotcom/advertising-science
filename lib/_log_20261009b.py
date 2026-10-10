import pathlib
V = pathlib.Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
h = V / "Harvest Log.md"
t = h.read_text(encoding="utf-8")

entry = """## 2026-10-09 (research run, second pass same day)

**Quiet. 0 transcripts in, 0 claims added, 0 merged, 0 refuted, 0 errors.** Fired 14:43 IST, 10 hours after the 04:32 run. No law changed, so the hot layer is untouched. Two method findings, both about the engine rather than about advertising, and both written into [[Watchlist]].

**The Meta for Business rotation is at most DAILY.** This morning's entry found a UK slug rotating out and back inside 24 hours and left the cadence open. Both shelves were read again 10 hours later and both returned **the identical 12 slugs in the identical order**, 0 added and 0 removed on each, US ceiling still 8 October and UK still 10 September. So the rotation is not per-render and not sub-daily, which rules out the cheap explanation: the slug did not flicker on a short timer, Meta genuinely re-cut the slice between one day and the next. **One read per day is sufficient on this source and a second same-day pass is wasted fetches.** The cumulative slug seen-set this morning asked for now exists, seeded at 26 slugs from every per-date baseline already in the cache, so a slug that leaves and returns will no longer re-fire as new.

**arXiv is the one daily source where a second same-day pass does advance.** The 04:32 run read the Thursday 8 October 04:00 UTC build, 27 items, 0 new. This pass read the **Friday 9 October build, 28 items, 24 new, 0 passing the advertising filter.** This morning's entry predicted tomorrow's run would pick it up; it was read today instead, which costs nothing either way because the seen-set is cumulative. The 04:00 UTC build lands at 09:30 IST, between the two slots, so a pre-dawn IST run always trails by one build and an afternoon run reads the current day. **Nothing is lost by running pre-dawn.** All 24 abstracts were read. The four closest to the lane are `LIFT` (unified retrieval and ranking), page-level layout decisions in e-commerce search, `LIME` (user-item interaction modelling) and a spatiotemporal intent recommender from Amap, and **all four are ranking, retrieval or recommendation with no advertising content**, which the filter's standing rule says must never qualify alone.

**Everything else quiet.** Harvest: all 12 channels listed clean, 0 new, 2 skipped short, 0 no-subtitles, 0 errors. Backlog zero against 484 transcripts. Meta Engineering 0 new, build Tue 6 Oct. Meta Newsroom 0 new, build Thu 8 Oct. Google Ads Announcements 396 answer ids, 0 added 0 removed. Ads & Commerce 0 new, build 1 Oct, now 8 days stale, so the Demand Gen Drops hub was read directly against the 2026-09-25 rule that a ceiling check says nothing about the shelf: **newest instalment is still September 2026 and all 13 are banked, so the stale feed is hiding nothing.** TikTok SDK changelog unchanged at v0.1.8; Newsroom and the for-Business blog remain India geo-blocked and were not retried. Weekly (Monday) lane not due, next due Monday 12 October.

**Gap noticed.** Unchanged from this morning and still the cheapest item on the board: the Muse for Small Business adoption question cannot be closed from Meta's own publishing, and one ChiroWorks, StayWell or Phoenix Truxx owner answer about whether Muse has offered them anything on their ads is worth more than the next three case studies.

"""

anchor = "One line per Research run: what came in, what changed. Quiet days get one line and nothing else.\n\n"
assert anchor in t, "anchor not found"
t = t.replace(anchor, anchor + entry, 1)
h.write_text(t, encoding="utf-8")
print("Harvest Log appended, second-pass entry")
