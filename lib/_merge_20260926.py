# -*- coding: utf-8 -*-
"""2026-09-26 merge: the Demand Gen Drops backlog, nine instalments read at source.

Banks GA-085..GA-088 and CR-266, and amends GA-068, GA-081, GA-083.
"""
import pathlib, sys

V = pathlib.Path("Obsidian God-level Marketing Vault/God-level Marketing/wiki/science")
GA = V / "Google Auction & Smart Bidding.md"
CR = V / "Creative Science.md"


def read(p):
    return p.read_text(encoding="utf-8-sig")


def write(p, s):
    p.write_text(s, encoding="utf-8-sig", newline="")


GA_NEW = """
### GA-085 · Google has spent thirteen months shipping instruments that make Demand Gen comparable to other platforms on the OTHER platform's terms, and six of the thirteen drops carry one
Tier: T1 · Status: active
All thirteen Demand Gen Drops read at source on 2026-09-26, covering 1 September 2025 through 24 September 2026. T1 for existence and product copy only. Nothing here states that Demand Gen performs.

**Google keeps shipping measurement, and it keeps pointing it outward.** In order:

- **Platform comparable conversion columns**, introduction drop, 1 September 2025. Google's own words: they "help you measure campaigns in a way that matches the default attribution used on other platforms." Restated in the December 2025 drop as "empowering you to make better cross-platform comparisons."
- **Conversion lift at lower spend and lower conversion volume**, same drop, plus the ability to test "an entire manager account or specific campaigns to understand the incrementality of running multiple campaign types at the same time."
- **Target CPC bidding**, October 2025, which "now allows you to optimize and compare performance across ad platforms with the same settings."
- **View-through conversion optimisation for YouTube**, April 2026, "aligning with capabilities you may use on other ad platforms."
- **Campaign Type Attribution and Uplift Experiments**, May 2026, already recorded at [[Google Auction & Smart Bidding#GA-083|GA-083]].

**What this changes when you put a Google campaign next to a Meta campaign.** Google's default columns and Meta's default columns are two different attribution models, so a side-by-side of the two default sets is not a comparison. Google now ships a column set built to match the other platform's default. Use it when the question is which channel to fund, say which column set produced every number, and never mix the two sets inside one table.

**The honest limit, because a rep will overstate this.** Every instrument listed is first-party, measuring its own product. None of them is a holdout run by us. [[Google Auction & Smart Bidding#GA-055|GA-055]] and [[Attribution & Incrementality#AT-072|AT-072]] still hold the only counterfactual this codex owns on Demand Gen, a 21-day geo holdout on one e-commerce advertiser that found no new-customer lift. A matched column set makes two platforms' numbers comparable to each other. It does not make either number incremental.
Sources: Google Demand Gen Drops, introduction (2025-09-01), October 2025, December 2025 and April 2026, all read in full at source 2026-09-26
Last touched: 2026-09-26

### GA-086 · One Google study, one two-month window and one survivorship filter back BOTH a 20% product-feed figure and a 33% product-feed figure, seven months apart
Tier: T1 · Status: active
Found on 2026-09-26 by reading the October 2025 drop against the May 2026 drop banked at [[Google Auction & Smart Bidding#GA-083|GA-083]] on 2026-09-25.

**The two footnotes, quoted in full.**

- October 2025: "Google data, Global, May to June 2025, based on performance data **from** campaigns active since Q1 2024 with over 50 products in merchant feed."
- May 2026: "Google data, Global, May to June 2025, based on performance data **for** campaigns active since Q1 2024 with over 50 products in merchant feed."

Identical apart from one preposition. Same source, same geography, same two-month window of May to June 2025, same survivorship filter of campaigns still running more than a year after launch with more than fifty products.

**The headline numbers they back differ by 13 points.**

- October 2025: "Demand Gen campaigns that do so using **tROAS goals** typically see a **20%** increase in conversions."
- May 2026: "Advertisers with **large product selections** typically see a **33%** increase in conversions when adopting product feeds in their Demand Gen campaigns."

**The stated population moved between the two sentences and the underlying data did not.** October conditions on tROAS, which appears nowhere in the footnote. May conditions on large product selections, which is the footnote's own over-fifty-products filter promoted into the headline. Neither sentence tells the reader the other exists, and seven months separate them.

**The operating rule.** Compare the footnote against the sentence before quoting either. A vendor number can be restated with a different qualifier and a different value off one unchanged study, and only the footnote shows it. Do not cite the 33% as newer evidence than the 20%. They are the same May to June 2025 data, read twice.
Sources: Google, Demand Gen Drop October 2025, body and footnotes read in full 2026-09-26; Google, Demand Gen Drop May 2026, read 2026-09-25
Last touched: 2026-09-26

### GA-087 · The October 2025 Demand Gen drop footnotes its new-customer figure with an A/B test run on SEARCH AND SHOPPING campaigns
Tier: T1 · Status: active
**The sentence, in a post about Demand Gen:** "New customer acquisition goals are rolling out this month. Advertisers that use New Customer Only Mode have, on average, improved their new customer ratio by 11.5% with a -3% reduced acquisition cost."

**Its footnote, read at source:** "Average uplift in performance based on internal studies conducted on **Search & Shopping campaigns** using best practices. Individual results may vary according to campaign details. Google Internal Data, Global, All Verticals A/B Test, March 2025-May 2025."

**The channel in the footnote is not the channel in the post.** A reader takes 11.5% and -3% as Demand Gen evidence, because Demand Gen is the only product the page discusses. The measurement was run somewhere else.

**Two things are fair to say for it.** The footnote describes an A/B test, which makes it better evidence than the adopter averages censused at [[Google Auction & Smart Bidding#GA-088|GA-088]]. And Google printed the channel mismatch itself rather than hiding it.

**The operating rule.** Never carry a figure from one Google surface to another because it appeared in that surface's announcement. Read which campaign types the footnote names. This is the second provenance defect found in this series, after [[Google Auction & Smart Bidding#GA-086|GA-086]], and both are invisible from the body text.
Sources: Google, Demand Gen Drop October 2025, business.google.com/us/accelerate/resources/articles/learn-what-new-in-demand-gen-with-october-demand-gen-drop/, body and footnotes read in full 2026-09-26
Last touched: 2026-09-26

### GA-088 · Census of all seventeen headline figures across thirteen months of Demand Gen Drops, and the four constructions Google reuses
Tier: T1 · Status: active
The backlog flagged at [[Google Auction & Smart Bidding#GA-068|GA-068]] is closed. All thirteen instalments are read: the introduction post of 1 September 2025, eleven monthly drops, and the September 2026 drop that publishes on blog.google rather than on the hub. **The monthly cadence held for thirteen straight months with no month missing.**

**Every headline figure, with what actually backs it.**

| Drop | The figure | What the footnote says |
|---|---|---|
| Intro, 1 Sep 2025 | 26% more conversions per dollar "in the past year" from 60+ improvements | Google Internal Data, February 2025 to March 2025. A two-month window behind a one-year claim |
| Oct 2025 | 11.5% better new-customer ratio, 3% lower acquisition cost | An A/B test on **Search and Shopping** campaigns, see [[Google Auction & Smart Bidding#GA-087|GA-087]] |
| Oct 2025 | 20% more conversions from product feeds with tROAS | The same study that backs May 2026's 33%, see [[Google Auction & Smart Bidding#GA-086|GA-086]] |
| Nov 2025 | "over 20% increase in conversions **or conversion value**" across 100+ launches | "Based on an internal experiment, Global H1 2025." One experiment named for a hundred launches |
| Dec 2025 | 68% of Demand Gen conversions came from users who saw no Search ad in the prior 30 days | Google Internal Data, February 2025 to March 2025. Same window as the intro, nine months before publication |
| Jan 2026 | 7% additional conversions **at the same ROI** from TV screens | "Internal Experiment, Google data, Global, 2025." No months given |
| Jan 2026 | LG Electronics: 24% higher conversion rate than its own paid social, 91% lower CPA | **No footnote.** The post carries one marker and spends it on the 7% |
| Feb 2026 | "over 40% more conversions" for adopting 3 of the 4 best practices | Google Internal Data, Global, Apr 2024 to Dec 2025, "Demand Gen Analysis results". An adoption comparison over 21 months with no control group |
| Feb 2026 | Cropp: 50% ROAS uplift in online sales | **No footnote** |
| Mar 2026 | 30% increase in conversion lift on Shorts from creator partnerships boost | Google Data, Global, Jan 2025 to Jan 2026, "while maintaining CPA efficiency" |
| Apr 2026 | 18% higher share of new-customer conversions than the paid media average | **Fospha**, a third party. "n=127 Retail brands across fashion, cosmetics, consumer goods, 2024-2025" |
| May 2026 | 33% more conversions from product feeds | See [[Google Auction & Smart Bidding#GA-083|GA-083]] and GA-086 |
| Jun 2026 | 72% of YouTube incremental conversions come from new customers | **No footnote anywhere in the post.** Attributed inline to Measured, linking a vendor blog post |
| Jul 2026 | 6% conversion boost from Checkout URLs, and 94% of holiday shoppers | See [[Google Auction & Smart Bidding#GA-084|GA-084]] |
| Aug 2026 | 30% increase in conversions or conversion value | See GA-068 |
| Sep 2026 | 40% more conversions at the same ROI from adding Gmail | See [[Google Auction & Smart Bidding#GA-081|GA-081]] |

**Four constructions repeat, and each one moves what the sentence promises.**

1. **"At the same ROI."** January 2026 and September 2026. That is volume at constant efficiency, which is the arithmetic of adding inventory and spend. A client hears efficiency.
2. **"Conversions or conversion value."** November 2025 and August 2026. A disjunction lets the better of two metrics carry the sentence.
3. **Adoption comparisons printed as results.** February 2026's 40%, September 2026's 40%, August 2026's 30%, October 2025's 20% and May 2026's 33%. Advertisers who adopt a feature are self-selected, usually larger and better resourced, and none of these has a control group.
4. **Footnote silence.** Three of the seventeen figures carry no footnote at all: LG Electronics, Cropp and the June 2026 72%.

**How much of this is measured against a counterfactual: three footnotes out of seventeen.** The October 2025 A/B test, which was run on the wrong channel, the November 2025 internal experiment and the January 2026 internal experiment are the only three that name an experiment or an A/B test. A fourth, March 2026, reports an "increase in conversion lift", which implies a lift study without saying one was run. Everything else is an average over adopters.

**Standing rule for this series and for Google announcements generally: read the footnote before you read the sentence.** Most of what is wrong with these figures is invisible in the body and visible in the footnote, and one whole class of it is visible only in the absence of a footnote.
Sources: Google Demand Gen Drops, all thirteen instalments, business.google.com/us/accelerate/demand-gen-drops/; the nine previously unread ones read in full at source 2026-09-26
Last touched: 2026-09-26
"""

CR_NEW = """
### CR-266 · Google says it is shipping Pathmatics competitor-ad creative into the Google Ads asset picker
Tier: T1 · Status: active
Demand Gen Drop, November 2025, published 17 November 2025, read in full at source 2026-09-26. T1 for the product statement only. Google states it as coming rather than shipped.

**Google's sentence, quoted:** "The availability of Pathmatics-provided images and videos in Google Ads will soon enable advertisers to easily lift and shift top-performing creative assets from other platforms into Demand Gen."

Pathmatics is a paid competitive-intelligence service that indexes ads running across platforms. Google is describing putting that index inside its own ad builder, so an advertiser picks a creative already running elsewhere and pushes it into a Demand Gen campaign in one session.

**Why it matters to how we work.** Our competitor-creative lane runs on the Meta Ad Library and the Google Ads Transparency Center, harvested by hand and by script. If Google ships a first-party route from somebody else's running ad into your campaign, the collection half of that work becomes a platform feature for anyone who pays for it, and the whole edge moves to judgment about which ad is actually winning and why it is winning.

**Two limits, stated because they are real.** Google wrote "will soon" in November 2025 and this codex has no confirmation that it shipped. And a lifted asset arrives without the hook, the offer or the audience that made it work, which is the part a real teardown produces.
Sources: Google, Demand Gen Drop November 2025, business.google.com/us/accelerate/resources/articles/demand-gen-drop-november-2025/, read in full 2026-09-26
Last touched: 2026-09-26
"""

AMEND_1_OLD = (
    "**Eight further drops back to October 2025 remain unread.** The 30% figure recorded here "
    "is the second of five vendor aggregates now catalogued across the series, and the running "
    "note on how to read them is at GA-081."
)
AMEND_1_NEW = (
    "**Backlog closed 2026-09-26. All thirteen instalments are now read**, and the full census of "
    "what every headline figure in the series rests on is at "
    "[[Google Auction & Smart Bidding#GA-088|GA-088]]. The 30% recorded here is one of seventeen "
    "such figures, and its “conversions or conversion value” phrasing also carries the "
    "November 2025 drop, which makes it a house construction rather than a one-off. The running "
    "note on how to read them is at GA-081."
)

AMEND_2_OLD = (
    "**Source-lane note worth keeping.** The three help-article ids this post links (16040527, "
    "16024357, 16388390) are **not** among the 396 answer ids on the Google Ads Announcements "
    "page. That page does not carry Demand Gen drops. The Ads & Commerce RSS feed is the only "
    "watchlist lane that catches them."
)
AMEND_2_NEW = AMEND_2_OLD + (
    "\r\n\r\n**Amendment, 2026-09-26.** The pattern called stable here is now measured across the "
    "whole series instead of inferred from three instances. Seventeen headline figures across "
    "thirteen instalments are censused at [[Google Auction & Smart Bidding#GA-088|GA-088]]: three "
    "carry no footnote at all, three name a real experiment, one cites a third-party retail panel, "
    "and the rest are averages over adopters. The “at the same ROI” construction used for "
    "this 40% also carries the January 2026 TV-screen figure, so it is house style."
)

AMEND_3_OLD = (
    "Sources: Google, Demand Gen Drop July 2026, read in full 2026-09-25\r\n"
    "Last touched: 2026-09-25"
)
AMEND_3_NEW = AMEND_3_OLD  # placeholder, replaced below

AMEND_GA083_OLD = (
    "Sources: Google, Demand Gen Drop May 2026, read in full 2026-09-25\r\n"
    "Last touched: 2026-09-25"
)
AMEND_GA083_NEW = (
    "**Amendment, 2026-09-26.** The footnote quoted above is not unique to this drop. The October "
    "2025 drop carries the same sentence, the same May to June 2025 window and the same "
    "over-fifty-products filter behind a **20%** figure instead of 33%. Both readings of the one "
    "study are at [[Google Auction & Smart Bidding#GA-086|GA-086]].\r\n"
    "Sources: Google, Demand Gen Drop May 2026, read in full 2026-09-25; October 2025 twin "
    "footnote read 2026-09-26\r\n"
    "Last touched: 2026-09-26"
)

AMENDMENTS = [
    (GA, AMEND_1_OLD, AMEND_1_NEW),
    (GA, AMEND_2_OLD, AMEND_2_NEW),
    (GA, AMEND_GA083_OLD, AMEND_GA083_NEW),
]


def main():
    for path, old, new in AMENDMENTS:
        s = read(path)
        n = s.count(old)
        if n != 1:
            print("AMEND FAIL count=%d for: %s" % (n, old[:70]))
            sys.exit(1)
        write(path, s.replace(old, new))
        print("amended %s | %s" % (path.name, old[:55]))

    for path, block in ((GA, GA_NEW), (CR, CR_NEW)):
        before = len(read(path))
        s = read(path).rstrip("\r\n") + "\r\n" + block.replace("\n", "\r\n").lstrip("\r\n")
        write(path, s)
        print("%s: %d -> %d chars" % (path.name, before, len(read(path))))


if __name__ == "__main__":
    main()
