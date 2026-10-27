import io, os

HL = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\Harvest Log.md"
t = io.open(HL, encoding="utf-8").read()
assert "## 2026-10-28 (Wednesday)" not in t

entry = """

## 2026-10-28 (Wednesday) \u00b7 1 transcript in \u00b7 3 claims added, 5 merged, 1 contested

**Not a quiet day. The claim count moves 1,393 to 1,396, and the three additions come from three different source types: a practitioner video, a platform engineering paper and a measurement corpus.**

**The headline, and the weakest-evidenced of the three (CR-289, T3).** Ben Heath, 27 October, reports the one creative trend that has held for a decade reversing: inside his mixed-format ad sets "Meta was allocating more and more budget to statics to images". His only quantified limb is a poll of his own YouTube audience, which has run four times and moved from 44% video / 38% image four years ago to **54% static / 38% video** three days before recording. **No respondent count on any of the four readings, no spend weighting, no definition of "best results", a self-selected pool whose composition is four years apart end to end.** It measures what advertisers believe their accounts returned. Carry the direction, never the 54%, and never show a client any of it. The mechanism he offers, shrinking attention spans and a video drop-off he says is visible in his numbers and does not show, is T4.

**It contested a structure claim we answer weekly (CR-196 \u2192 contested).** That claim held, from one operator, that images and video in the same ad set starve each other, so separate them. Heath runs the opposite on purpose and reports the starvation too, with the winner reversed. **So "one format cannibalises the other" now has two independent sightings and which format wins is not fixed.** Neither operator publishes a spend split. Meta's own T1 measurement at CR-261, 7.3% lower cost per acquisition for an ad set carrying an image, a video and a vertical video with audio together, sits on the mix-them side of the structure question. **Instruction: check spend by format before judging a format, and from today read it in both directions.**

**Four other merges off the same transcript.** CR-031 takes his animated-static convergence forecast (T4, no account, no comparison). CR-239 gains a second independent operator on the warm-audience condition plus the inverse he adds, that video is the format when the product is new and unexplained or the sale depends on believing the seller. CR-048 takes the creative-volume version of the production-economics argument, 16 statics plus 4 videos being an easier route to 20 ads than 10 and 10. CR-202 takes a flat contradiction on the photoreal branch, "we find them not perform well at all" for statics that read as AI, which on a close read is the same rule rather than a competing one: either the render is undetectable or the format is openly not real, and the ad caught in between loses.

**The strongest item of the day is the auto-bidding architecture (AU-101, T1).** Pinterest published its deployed system, RLBP. **The fast loop is a classical PID controller and it stays**; the reinforcement-learning part is a meta-controller that picks each campaign's PID parameters once a day. So the learned component acts on the controller's tuning rather than on the bid. A daily parameter update is a mechanism for a bid change settling over about a day. The same paper states the objective weighting MOVES over a campaign's life, cost efficiency early "when budgets roll over" and delivery urgency near the deadline, which voids a first-week-against-last-week cost comparison. **No magnitude is published for the result, only "a statistically significant reduction in effective cost-per-click" with a two-month holdout**, so there is nothing to quote. Pinterest, not Meta, and we do not buy it.

**And the first instrument that measures what happens between a Google impression and a Google click (GA-098, T2).** Eye-gaze and click telemetry on 2,776 real Google result pages: **99.7% of top-ads carousels are fixated and only 10% of clicks land on them**, ads take about 16% of main-axis clicks, and People Also Ask is fixated 44% of the time for two clicks in the entire corpus. The dissociation belongs to the element type, not to ads. Diagnostic use only: on a Search campaign with high impression share and a weak click-through rate, "nobody saw it" is close to ruled out for the top block. Lab tasks, no vertical, no device mix, no date range, so nothing transfers to an account, and the 10% is a share of clicks rather than a click-through rate.

**Read and deliberately NOT banked, three items.** Meta Engineering's *PrivacyLib* of 27 October, read in full, zero advertising, ranking, delivery or measurement content, the only "ads" string on the page being a sidebar link to another post. Meta Engineering's Python typing survey of the same date, screened on title and category. And arXiv 2610.35695, *OptIDC*, a model-agnostic input-side selection framework for deep CTR prediction: genuinely on topic, offline AUC on four benchmark datasets, no deployment and no operating consequence, so T4 with nothing to do. The Hyros sponsor segment inside the Heath video, asserting Meta tracking is off "20 to 30% and as much as 50% plus", is a vendor figure in a disclosed paid slot with an affiliate commission named on camera; it is recorded inside CR-289 and not banked, and its band is the folklore-grade range already flagged at AT-020.

**One platform-watch pointer, not a claim.** Heath closes by pointing at Meta's Ads Creative Studio (MD-168) as the thing that will make static production cheaper. He describes nothing new about it here, so there is nothing to merge. It is still on none of our accounts.

**⚠ A defect in OUR OWN run record, found today.** The 2026-10-27 run log states the watchlist cache was "committed and verified". The file mtime proves a write happened at 07:03:31, and the `meta-business-news` entry was never touched: `last_checked` still read 2026-10-26 and no `slugs_us_2026_10_27` key was ever written. **Same shape as the defect recorded for the 2026-10-23 run, which makes it a recurrence rather than a one-off.** Consequence: today's slug diff ran against a two-day-old baseline, so a post that rotated in and back out on 27 October is invisible to us. Today's entry is written and verified.

Gaps: the six carried items all still stand, none closed. **The live ad set count against the LS-089 formula is now seven days old and still the cheapest open item on our own book.** Carried defect, seventh day: the Harvest Log still has two write ends, research at the bottom and teacher at the top. This entry is at the bottom.

### Errors

Harvest: none. All 12 channels listed, zero errors, zero RSS fallback used (yesterday it carried 9 of 12). 8 uploads skipped under the 150-second floor, 3 had no subtitles available, 0 out of window. Watchlist checker: none, every source HTTP 200. Plain fetch on Meta for Business News: HTTP 400 again, documented behaviour from our egress, read via WebFetch. TikTok Newsroom and for-Business blog: not retried, permanent India geo-block, not an outage, so the TikTok lane is the SDK changelog alone and is not a clean TikTok check. `rizzdial` returned ENDPOINT_NOT_FOUND and is not a research source. No source went unread.
"""

t = t.rstrip("\n") + "\n" + entry.rstrip("\n") + "\n"
io.open(HL, "w", encoding="utf-8").write(t)
print("harvest log appended at bottom:", t.rstrip().endswith("No source went unread."))
