# -*- coding: utf-8 -*-
"""2026-09-12 research pass: Harvest Log entry, inserted above the same day's teacher entry."""
from pathlib import Path

LOG = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\Harvest Log.md")
t = LOG.read_text(encoding="utf-8")

ANCHOR = "## 2026-09-12 (teacher run)"

ENTRY = """## 2026-09-12 (research run)

**1 transcript in, 1 watchlist post read in full. 4 claims added, 5 amended, 2 laws amended. 1 source genuinely unmonitored.** Backlog 0 in, 0 out.

### What came in

**YouTube, 1 new transcript out of 12 channels.** Nick Theriot, "We Cut This Brand's Facebook Ads CPA by 75%", 2026-09-11, 7 minutes, 1,525 words. One video skipped under the 150-second floor. Zero listing failures and zero errors, so every channel was genuinely read.

**⚠ 11 of 12 channels fell back from RSS to the /videos tab.** The RSS endpoint returned 404 or 500 for eleven channels; only Ben Heath answered on the primary route. The fallback lists fine and no channel was missed, so today's near-quiet YouTube result is real. It is worth flagging because the 2026-09-11 run recorded zero fallbacks and used that as its evidence that the quiet day was honest. **That evidence is not available today**, and the only reason the quiet is still trustworthy is that the harvester records fallback use explicitly and logs a genuine listing failure separately.

**Meta for Business News broke its own ceiling for the second time in nine days.** New post dated 10 September on the listing card and 11 Sep 2026 on the post itself, "Performance Spotlight: How Instant Hydration Built a System for AI to Scale". Read in full. The previous newest was the 3 September post banked at MD-153.

**Transport, and it flipped again.** The LISTING page answered a plain fetch with a locale override on the first attempt, HTTP 200, 237KB. The POST returned **HTTP 400 on six routes**: bare, trailing slash, en_US, en_GB, web.facebook.com and m.facebook.com. The Playwright browser opened it on the first attempt. That is the fourth different transport outcome on this source in five days, and the pattern across them is that the listing and the post do not behave alike. **Try the browser on a post body straight away rather than working through fetch routes.**

### Everything else on the watchlist

| Source | Result |
|---|---|
| Meta Engineering (RSS) | 0 new. Feed still built Tue 8 Sep 16:52 UTC, fourth day flat |
| Meta Newsroom (RSS) | 0 new. Feed still built Tue 8 Sep 18:45 UTC |
| Google Ads & Commerce (RSS) | 0 new. Feed built Thu 10 Sep 16:00 UTC |
| arXiv cs.IR (RSS) | Empty by construction. 892-byte Saturday build, `skipDays` names Saturday and Sunday |
| TikTok SDK changelog | Unchanged at v0.1.8 |
| Google Ads Announcements | 2,350 lines against 2,350 cached, 1 added / 1 removed, both render nonces |

Saturday, so the Monday-only sources were not due.

**The Google Ads Announcements nonce was re-confirmed live rather than assumed.** The checker was run twice minutes apart against the same cache and returned a different bare numeric ID as "added" each time (526795959019865150, then 11413881109636762997). Same behaviour as 2026-09-11. Line count identical. Not news.

**TikTok stays a blind spot and is not logged as clean.** The SDK changelog ships endpoint names, so it detects new ad products and misses every policy and creative announcement. The Newsroom and the for-Business blog are permanently India geo-blocked from our egress.

### The one source, and what it is worth

Instant Hydration, an electrolyte brand, DTC from mid-2024 and pushing into retail this summer. Kevin Cooper, Founding Partner and VP of Paid Acquisition, quoted by name throughout. Meta published it, Meta sells everything it praises, and no number on the page carries a method. Read with that discount and there is still real content, because the operating model is described in specifics.

**AT-117, new, T1 for what Meta published and T3 for the figure.** "About 35% higher net-new visits" from running the same ads under incremental attribution instead of a conversion campaign on 7-day click plus 1-day view, which Meta calls "a lift validated by their third-party MTA tool". **The validator is the finding.** Multi-touch attribution observes only exposed users, has no unexposed cell, and therefore cannot answer whether the visit would have happened anyway. Two models on the same exposed population agreeing is not a control. The outcome is also site VISITS, which is not what [[Attribution & Incrementality#AT-003|AT-003]] says the switch has to be read on.

**AT-035 amended, and this is the first Meta text this claim has ever held.** The claim has recorded since 2026-08-20 that all three competing accounts of how incremental attribution works come from practitioners and that no Meta documentation is quoted anywhere. Meta now has prose on the record: the setting "shifts delivery toward users the platform predicts wouldn't have visited otherwise". **The verb is evidence.** *Predicts* is a model scoring users, which argues against the permanent-10%-holdout position and sits comfortably with the factor-derived-from-other-advertisers position. It settles nothing about the training data, and a case study is not documentation, so the claim stays contested.

**CR-232, new, T3, and it is the more useful half of the day.** The advertiser says creative the team thought had burned out "can come back to life" when repurposed into incremental attribution campaigns, with the asset untouched. Nothing shown, vendor page, weak as evidence for the lever. **Strong as a reframe**, because it splits fatigue into two diagnoses that produce an identical Ads Manager row: an audience that has stopped responding, which only new creative fixes, or an asset the delivery system stopped selecting, which a different objective can reverse. Test costs one duplicate.

**CR-115 amended** with where a creator brief's SUBJECT comes from: analyse the creator's own organic posts, find the themes their audience responds to, brief on the overlap with the product. The named case is a health condition the creator posted about often that electrolytes help. **CR-068 amended** with a sixth operator position that is the first scoped by ad TYPE rather than by enhancement type: enhancements off on whitelisted creator ads specifically, so a creator's handle never appears on an asset they did not make, argued on brand integrity rather than performance. **MD-013 amended** with one line: Advantage+ audience and placements on every ad set, one manual lever, a lifecycle exclusion of existing customers, and the audience expansion credited to creator diversity rather than to any setting.

**LS-077, new, T4.** "It actually improves our Meta performance because there's more signals from these different channels coming in." Banked low and with the confound named, because the ordinary explanation is that spending on more channels raises total demand and Meta's last-click column catches some of it. Banked at all because this file had no entry for the question and the belief is widespread.

### The transcript

**CR-233, new, T2 for the numbers and T3 for attributing them to the format.** A fragrance account, statics only at a $491 cost per purchase on about $2,000 over the 30 days before onboarding, video only at $107 on about $3,400 over the 30 days after. He says 75%; the figures give 78%. The agency changed at the same time as the format, spend rose about 73%, no window is stated, and $107 on $3,400 is roughly 32 purchases.

**The mechanism is narrower and better than "video beats statics".** A fragrance cannot show its benefit, one person saying it smells good reads as bought, and several different people reacting inside one video is what makes the claim believable. **When a product's benefit cannot be seen on screen, the creative has to carry witnesses, and one witness is worse than none.** That is testable on our own book and it is not a format claim.

### Laws

**Two amended, none added, none retired.**

**Law 11a gains a third step.** Find the word, ask whether it names the method or the metric, then ask what the validator actually measures. A named third party raises the bar for nothing unless that party ran an unexposed cell. The law was written on 2026-09-10, amended on 2026-09-11 when Google triggered the metric-name false pass, and amended again today by a different false pass. **Three days, three versions, and each new failure mode was found by reading one page carefully.**

**Law 4b gains a free test that sits outside the asset.** The codex's longest-open question had been framed entirely as a question about recutting footage. Change the optimization setting before funding a reshoot.

### Counts

**1,191 claims** across 11 topic files at 10:30 IST: 101 T1, 121 T2, 811 T3, 158 T4; 1,085 active, 100 contested, 5 superseded, 1 refuted. Both columns sum to 1,191.

**The reconciliation from 1,185 runs through two passes, and this is the fix for the recount that was wrong twice in a row.** The 2026-09-11 teaching pass banked AT-116 after that day's research count was taken, the 2026-09-12 teaching pass banked AT-118, and this pass banked four. 1,185 plus 2 plus 4 is 1,191. **Any claim count published by either daily pass is a mid-day snapshot**, because both passes write claims into the same files.

**The counter is fixed and the fix is two lines.** It pairs each heading with the line immediately beneath it, and it reads only the 11 topic files. Scoping it to the topic files is what stops the Harvest Log's `### CR-231, new:` heading from being counted as a claim, which is exactly the one-line gap the 2026-09-11 log traced in the team-repo sync. **The sync counter has not been fixed and will still read one high until it is scoped the same way.**

### Errors and failures

- **Meta for Business News POST body: HTTP 400 on six routes.** The browser opened it first try. No data lost.
- **11 of 12 YouTube channels fell back from RSS to the /videos tab** (404 or 500). Fallback listed fine, nothing missed.
- No harvester errors, no listing failures, no watchlist script errors.

### Gaps noticed

- **The research and teacher lanes launched in the same second for the sixth consecutive day**, both write claims into the same files, and today the teacher pass held AT-117 as its next free ID while this pass was writing AT-117. It renumbered to AT-118 because somebody re-checked. **Three days running, the only thing preventing a duplicate ID has been a human-grade check.** Stagger the launches or have both passes reserve an ID atomically.
- **GeoX is still not installed**, a sixth consecutive run naming an instrument and not opening it. Today's teacher pass at least established that four of five of our accounts cannot supply a per-region outcome column, which makes installing it less urgent and the data problem more urgent.
- **The arXiv framing-sentence filter gap is still open.** It did not fire today only because the feed was empty.
- **Qualified Future Conversions still has no codex entry**, carried since 3 September.
- **Meta for Business News has no stable fetch route**, and the listing and post pages now demonstrably behave differently.
- **The launcher still cannot distinguish an auth failure from a quiet day**, carried a seventh time.
- **The day's substance again came from a watchlist source rather than from the channel roster**, second time in two days. Widening the watchlist beats widening the channel roster.

"""

assert t.count(ANCHOR) == 1
t = t.replace(ANCHOR, ENTRY + ANCHOR, 1)
LOG.write_text(t, encoding="utf-8")
print("harvest log entry written")
