# Harvest Log write for the 2026-11-09 research run. The teacher lane wrote this date's heading
# first and recorded that no research pass existed; this corrects that and inserts the research lane above it.
import io

P = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\Harvest Log.md"
s = io.open(P, encoding="utf-8").read()

OLD_HEAD = "## 2026-11-09 (teacher run; no research run exists for today in either lane)"
NEW_HEAD = "## 2026-11-09 (research run, and the teacher run that preceded it)"
assert s.count(OLD_HEAD) == 1
s = s.replace(OLD_HEAD, NEW_HEAD)

OLD_PARA = ("**No research pass ran today.** At topic-lock the newest entry on this file was still 8 November, and both write "
            "ends of this file were read before deciding that.")
assert s.count(OLD_PARA) == 1, s.count(OLD_PARA)
NEW_PARA = ("**Corrected by the research pass that ran later the same day: a research run DID happen on 9 November, at 16:19 "
            "to 17:00 IST, and its entry sits above this one.** The teacher lane fired first and was right about the state of "
            "the file at its own topic-lock, so the reasoning below stands on what it could see. At that moment the newest "
            "entry on this file was still 8 November, and both write ends of this file were read before deciding that.")
s = s.replace(OLD_PARA, NEW_PARA)

RESEARCH = """
### Research lane

**Not a quiet day. 0 new transcripts, 3 claims touched (2 banked, 2 merged), and the Monday weekly lane moved on three of its eight sources.** The one urgent item: **Marketing API v27.0 shipped on 4 November 2026 and v24.0 stops working tomorrow, 10 November 2026.**

**⚠ Marketing API v27.0, read off the changelog's own version table.** v27.0 Date Introduced **November 4, 2026**, Available Until TBD. The baseline five days earlier topped at v26.0. Full table today: v27.0 4 Nov 2026 TBD, v26.0 29 Jul 2026 TBD, v25.0 18 Feb 2026 until 23 Feb 2027, **v24.0 8 Oct 2025 until 10 November 2026**. Nothing of ours is pinned to v24.0, and the thing that is worth fixing is one level down: our real-numbers puller runs **Graph API v21.0** (`.claude/skills/real-numbers/scripts/real_numbers.py`), which the Graph table ends on **21 January 2027**. The lane that produces every daily and weekly number has a hard stop about ten weeks out. **What v27.0 actually changes is not published**: `docs/graph-api/changelog/version27.0` returns HTTP 404, and no claim was banked about its contents because there is nothing to read.

**Two Meta pages now give v24.0 two different end-of-life dates.** The Marketing API changelog says 10 November 2026. The Marketing API table printed on the Graph API changelog page says 6 October 2026, a date already past. The Graph API page also still ends its own availability table at v26.0 while its headline sentence, and the separate versioning guide, both read "The latest Graph API version is v27.0". Record the changelog page as the authority on Marketing API dates and treat the Graph page's copy of that table as stale.

**Banked, [[Attribution & Incrementality#AT-134|AT-134]], T1.** The Marketing API out-of-cycle shelf moved for the first time since 22 October: it now declares "Updated: Nov 5, 2026" and carries one new entry dated **5 November 2026**, an Ads Insights breakdown `pa_creator_ig_handle` that groups partnership-ads results by the creator's Instagram handle, on all versions and all four insights endpoints. **The supported-field list is impressions, reach, `inline_link_clicks` and `video_p25` through `video_p100`, and it stops there.** No conversions, no leads, no cost per result. So the breakdown says which creator's identity was seen and clicked and not which produced a customer, and it cannot be combined with any other breakdown. Guard attached from [[Attribution & Incrementality#AT-128|AT-128]]: nothing says whether this breakdown is behind per-account enablement, so an empty result is to be tested rather than reported.

**Banked, [[Google Auction & Smart Bidding#GA-100|GA-100]], T1.** Google's Data Manager API accepts a lead form's `lead_id` today and does not attribute on it. Google's own line, one sentence in the middle of the 4 November release post: "Attribution using `lead_id` and `match_id` isn't available yet. Until it is, include other identifiers to ensure events are attributed." **The field accepts the value, the ingestion request succeeds, and the conversion does not land**, which is the same silent-success shape the release's new row-level diagnostics exist to expose. No client on the book runs Google lead forms with an offline upload, so this is a trap recorded before we can walk into it.

**Merged, [[Google Auction & Smart Bidding#GA-073|GA-073]].** The same release gives item four of that claim its first real detail. "Built-in diagnostics" now means a `record_indices` field on every `ErrorCount` and `WarningCount`, naming the 0-based positions of the failed rows, against Google's statement that "a successful ingestion request doesn't guarantee that every record was processed". It also adds call conversions through a new `call_info` field with a `start_timestamp` and a hashed phone number in `user_data`.

**Merged, [[Auction Mechanics & Bidding#AU-084|AU-084]], and it is a rejection rather than a finding.** The arXiv cs.IR filter returned one hit, RedMall (arXiv 2611.08519v1), reporting **advertiser value +2.24% and CTR +0.59%** on e-commerce advertising plus GMV +1.08% and daily active buyers +0.95%. Read and **NOT banked** on the BRIDGE and CoGR ground: semantic-ID generative retrieval with no auction, no bidding and no ads-ranking content, and the advertising surface is only the venue for the test. The platform is never named and the authors state no affiliation, so it cannot be attributed to any company. The four percentages are written into AU-084 so a later run does not mistake them for fresh evidence.

**Read in full and deliberately not banked, two Google developer posts.** *Upcoming changes to multi-party approvals in the Google Ads API* (4 November): deferred access-invitation creation, a new `STALE_MULTI_PARTY_AUTH_REQUEST` error in v26.2, and a review batch limit going from 1 to 100, all effective the week of **7 December 2026**. Access plumbing, nothing that changes how an account is bought or measured. *Prepare for CocoaPods read-only mode* (6 November): Google Mobile Ads SDK distribution for iOS publishers after 2 December 2026, and no client of ours ships an app.

**Harvest: 0 new transcripts, 0 errors.** All 12 roster channels listed clean, 3 skipped as too short, 1 with no subtitles, 0 out of window, 0 RSS fallbacks. Extraction backlog zero.

**Daily watchlist.** Meta Engineering 0 new (build 3 Nov, 6 days stale), Meta Newsroom 0 new, Google Ads & Commerce 0 new (build 28 Oct, now **12 days stale**), Google Ads Announcements 396 answer ids with 0 added and 0 removed, TikTok SDK unchanged at 0.1.8. **Meta for Business News: US shelf flat for a fifth day, UK shelf moved and brought nothing new** — the three Hong Kong posts rotated out and three items from the back catalogue rotated in, all six already in the 36-slug cumulative set, and the UK ceiling went **backwards** from 27 to 22 October, which is the documented rotation and not a retraction. **Demand Gen Drops Hub read directly again because the Ads & Commerce alarm is stale: no November instalment exists**, the newest is still October and its content is banked at [[Google Auction & Smart Bidding#GA-093|GA-093]]. TikTok Newsroom and the for-Business blog stay logged as geo-blocked, not skipped.

**Advertising Standards unchanged on both locales, and the UK side is now provable.** US: 16 of 16 sections located, every hash byte-identical to the post-change state of 2 November. UK: 16 of 16 located, and the **266-line body vector is identical index by index** to the 2 November baseline, sum 30,371, total 33,583 on both days. A full UK per-section hash map now exists for the first time, which closes the gap the 2 November run named.

**Two defects in our own tooling, both found and both fixed today rather than carried.** The section-anchor regex collapsed each separator CHARACTER with `[- ]?`, which cannot match the UK rendering "Product**-** and format-specific policies"; the first UK pass therefore reported that section missing and inflated the section above it from 550 to 12,476 characters. **That is a false policy-removal finding on a page four chiropractic-adjacent accounts depend on, and it came from the same section the 19 October note already flagged for sentence case.** The separator class is `[- ]+`. Separately, the business-news script read the cumulative slug key from the top level of the cache where it does not exist and the UK date pattern was month-first only; both are corrected in `lib/_bizmeta_20261109.py`. The UTC stamping defect in `lib/watchlist_check.py` did not bite today because the run fired at 16:23 IST, well past 05:30, and it remains unfixed.

**One honesty note on a key we have been quoting.** The US Advertising Standards total innerText is 32,502 today against 32,611 recorded for a pre-change read, a 106-character drop, while all 16 section hashes match. The delta sits outside the hashed span, in nav or footer chrome. **Total innerText is not a usable key on that page and should not be reported as movement.**

"""
anchor = "\n### Teacher lane\n"
assert s.count(anchor) >= 1
i = s.index(anchor)
s = s[:i] + "\n" + RESEARCH.strip("\n") + "\n" + s[i:]
io.open(P, "w", encoding="utf-8", newline="").write(s)
print("harvest log written")
