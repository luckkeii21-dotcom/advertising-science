import pathlib
V = pathlib.Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
w = V / "Watchlist.md"
t = w.read_text(encoding="utf-8")

add = """

### The shelf rotation is at most DAILY, so a same-day second pass buys nothing on Meta for Business News (2026-10-09, pass 2)

The entry above found a UK slug rotating out and back inside 24 hours and left the cadence open. **Both
shelves were read again 10 hours later on the same calendar day, 04:35 IST then 14:50 IST, and both
returned the identical 12 slugs in the identical order.** 0 added, 0 removed on each. US ceiling still
8 October 2026, UK ceiling still 10 September 2026.

So the rotation is **not per-render and not sub-daily.** It moves at most once a day. **One read per day
is sufficient on this source, and a second same-day pass is wasted fetches.** That also rules out the
cheaper explanation for the non-monotonic ceiling: the slug did not flicker on a short timer, Meta
genuinely re-cut the slice between one day and the next.

**The cumulative seen-set the entry above asked for now exists**, at
`cache/watchlist-seen.json` -> `pages.meta-business-news.slugs_seen_cumulative`, seeded at 26 slugs from
every per-date baseline already in the file. A slug that leaves and returns will no longer re-fire as new.

### arXiv is the ONE daily source where a second same-day pass does advance the lane (2026-10-09, pass 2)

The 04:32 IST run read the **Thursday 08 October 04:00 UTC** build, 27 items, 0 new. The 14:45 IST run
read the **Friday 09 October 04:00 UTC** build, 28 items, **24 new.** 0 passed the advertising filter in
both passes.

This is the 2026-08-20 scheduling-lag entry and the 2026-09-07 run-time correction shown end to end in a
single day. **A pre-dawn IST run always reads the previous calendar day's build; an afternoon IST run
reads the current day's.** The 04:00 UTC build lands at 09:30 IST, between the two slots.

Practical consequence: the pre-dawn slot is never wrong, it is just one build behind, and the next day's
run picks the missed build up because the seen-set is cumulative. **Nothing is lost by running pre-dawn.**
Worth knowing only if the schedule is ever argued about, or if a specific build has to be read on its
own publication day.

Today's 24 were read as titles plus abstracts and every one is genuinely non-advertising. The four closest
were `LIFT` (unified retrieval and ranking), `Language Models for Page-Level Layout Decisions in E-commerce
Search`, `LIME` (user-item interaction modelling) and a spatiotemporal intent recommender from Amap.
**All four are ranking, retrieval or recommendation with no advertising content**, which is exactly what
the filter's standing rule says must never qualify on its own.
"""

anchor = "**Sixth consecutive browser-free read of both shelves.** The slug diff needed zero punctuation adjudication for the fourth run running."
assert t.rstrip().endswith(anchor), f"unexpected tail: {t.rstrip()[-120:]!r}"
w.write_text(t.rstrip() + add, encoding="utf-8")
print("Watchlist.md appended, 2 method findings")
