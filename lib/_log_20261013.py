import pathlib

ENTRY = """## 2026-10-13 (research run)

**0 transcripts in, 2 claims added, 0 merged, 0 contested, 0 refuted, 0 errors. One law amended.** The whole day came from one source: Meta Engineering published an ads post and it was read in full.

**MD-174 and MD-175, both T1, both from "Turning Opportunistic AI Inference Capacity Into Better Ads Recommendations" (Engineering at Meta, 2026-10-12).** Meta now spends idle, preemptible inference capacity on ads ranking through two levers. **Rank More Ads** raises the number of candidates the ranking stages evaluate; **Serve Better Models** raises the share of requests scored by a more powerful model, and holds candidate count constant so it can use accelerator-only surplus. Central controllers react on the order of minutes (RMA's reads observed tail latency through a PID loop), with value-aware load shedding at both server and client dropping the lowest-value optional work **within a few milliseconds** when capacity is reclaimed. Baseline capacity is protected physically for SBM and logically for RMA.

**The operator consequence, and it is a reading rule rather than a lever: the amount of ranking work an ad gets is partly a function of Meta's spare hardware in that region at that instant, and no account setting can see it or influence it.** That amends **law 23** in the hot layer, the law that says an ad-set A/B is not a test because identical twins diverge. Part of that noise floor now has a named T1 cause that is not auction competition and not anything in the account. It makes the floor no smaller and changes no instruction; it removes an explanation we were tempted by.

**MD-175 is banked separately because it is about who gets the good model.** The router segments requests by **predicted likelihood of user engagement**, then runs explore-and-exploit to measure the incremental benefit per segment, because, in Meta's own words, "the incremental benefit of the more powerful model does not always align with the absolute value of a request." It then **permanently preserves exploratory traffic across segments** "rather than reinforcing an outdated routing decision." That last line is the quotable one: a platform optimising for efficiency spends its own scarce capacity on exploration forever, which is the argument we make to clients about creative testing every week. The engagement signal itself is defined no further anywhere in the post, so it is not something to target.

**What Meta did NOT publish, and the claims say so.** No share of requests served by either lever, no size of the opportunistic pool, no swing range on candidate count or model coverage, and no conversion or CPM effect. "Drives significant advertiser value and capacity efficiency" is the entire claim of effect and it carries no number and no footnote, which is the construction MD-171 catalogues. The mechanism is T1; the size of its effect on any one account is unmeasurable from outside.

**Harvest: 0 new transcripts across all 12 channels, zero errors.** 8 uploads skipped as too short, 3 had no subtitles available, 0 out of window. No extraction backlog: every transcript in the vault is marked extracted.

**Watchlist: 4 new items, 1 relevant, 3 discarded.** Meta Engineering carried three new posts; the two not banked are OCP Summit networking hardware and QUIC for Instagram Live ingest, neither touching ads delivery. Meta Newsroom carried one, the Muse Wonder frontier models for agents, with nothing about ads ranking or delivery in it. Google Ads & Commerce blog: nothing new, feed still built 2026-10-01. TikTok business API SDK changelog unchanged at 0.1.8. Google Ads Announcements: 396 answer IDs, identical to cache, zero added and zero removed. Tuesday, so the 9 Monday-only weekly sources were not due.

**Two source notes.** **arXiv cs.IR published nothing today**, verified directly rather than inferred: the feed is 892 bytes with zero `<item>` elements and a build stamp of Tue 13 Oct 04:00. That is an arXiv-side empty day, not a filter or parser failure. **TikTok Newsroom and the TikTok blog were skipped: browser unavailable.** The Playwright MCP server failed to connect this session (connection timeout), and both sources are geo-blocked to a plain fetch from India, so there is no fallback for them.

**Gap noticed, and it is the same one as the last two Meta engineering posts.** Every T1 we hold about ranking compute now says the platform allocates quality unevenly, by user history (MD-090), by time and hardware (MD-174), and by predicted engagement segment (MD-175). **We have never measured hour-of-day or day-of-week variance in cost per result on a single one of our own accounts**, which is the cheapest instrument that would show any of this landing. A 30-day hourly breakdown on Phoenix Truxx or SJR Commercial costs nothing but an export.

"""

p = pathlib.Path(r"E:/claude code marketing skill/Obsidian God-level Marketing Vault/God-level Marketing/wiki/science/Harvest Log.md")
t = p.read_text(encoding="utf-8")
assert "## 2026-10-13" not in t
anchor = "## 2026-10-12 (research run)"
assert t.count(anchor) == 1
p.write_text(t.replace(anchor, ENTRY + anchor), encoding="utf-8")
print("harvest log entry written")
