# -*- coding: utf-8 -*-
"""2026-09-26 step 5: Watchlist.md backlog-closed amendment + Harvest Log research entry.

The research pass ran in two sessions. The 16:12 session completed runbook steps
1 to 4 (harvest, watchlist, merge, SKILL.md hot layer) and exited without a log,
so the watchdog relaunched at 21:52. This script writes what step 5 owes.
"""
import pathlib, sys

V = pathlib.Path("Obsidian God-level Marketing Vault/God-level Marketing/wiki/science")
WL = V / "Watchlist.md"
HL = V / "Harvest Log.md"


def read_raw(p):
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        return f.read()


def write_raw(p, s):
    with p.open("w", encoding="utf-8-sig", newline="") as f:
        f.write(s)


WL_OLD = """**Backlog, eight posts, queued:** June 2026, April 2026, March 2026, February 2026, January 2026,
December 2025, November 2025, October 2025, plus the introduction post. Body extraction: strip tags,
then anchor on `Social Module` and read to `Return to top of page`. Anchoring on the post title fails
on some of them because the chrome repeats it."""

WL_NEW = """**BACKLOG CLOSED 2026-09-26.** The nine remaining instalments were read in full at source in one
pass: the introduction post of 1 September 2025, then October, November and December 2025 and January,
February, March, April and June 2026. With the two read on 2026-09-25 and the August and September 2026
drops already banked, the series is complete at **thirteen instalments, monthly with no month missing,
1 September 2025 through 24 September 2026**.

Body extraction, confirmed working on all nine: strip tags, then anchor on `Social Module` and read to
`Return to top of page`. Anchoring on the post title fails on some of them because the chrome repeats
it. **Footnotes are reachable only through the `#footnote-1` anchor**, and a tag-strip plus line-dedup
drops them, which is where both of today's provenance findings were hiding.

**What closing the shelf produced:** GA-085, GA-086, GA-087 and GA-088 in
[[Google Auction & Smart Bidding]] and CR-266 in [[Creative Science]], plus amendments to GA-068,
GA-081 and GA-083. Two of those are provenance defects invisible in the body text of the posts.

**Maintenance from here:** the hub is the back catalogue and the Ads & Commerce RSS is the alarm. One
new instalment is expected per month. Read its footnote before its body."""

HL_ENTRY = """## 2026-09-26 (research run)

**0 transcripts in, 5 new claims, 3 merges, 0 contested, 0 refuted. 0 harvest errors, 0 watchlist errors. One new operating rule.**

Every live lane returned nothing. The whole day came out of closing a backlog this engine flagged on 2026-09-25: **nine unread Demand Gen Drops read in full at source**, which completes the series at thirteen instalments and turns a five-instance pattern into a seventeen-figure census.

**Harvest.** `harvest.py daily` clean, 12 of 12 channels listed, 0 new transcripts, 8 skipped short, 1 no subs, 0 errors, 0 RSS fallbacks. Second consecutive zero-transcript day and the fifth on record, after 2026-09-06, 09-07, 09-23 and 09-25. Unextracted backlog 0.

**Watchlist, 0 new across every lane.** Meta Engineering 200 build 24 Sep, 0 new. Meta Newsroom 200 build 24 Sep, 0 new. Google Ads & Commerce 200 build 24 Sep, 0 new. Google Ads Announcements 200, **396 answer ids, 0 added, 0 removed**, unchanged for a third day. Meta for Business News read in the browser in **both locales**: US 12 titles 0 new, ceiling 21 Sep 2026; UK 12 titles 0 new, top card rendering 11 Sep against 10 Sep yesterday, the same post and a one-day drift artefact. arXiv cs.IR 200 with **an empty feed body, Saturday build**, the documented weekend condition. TikTok SDK changelog 200, unchanged at v0.1.8; TikTok policy and creative remain unmonitored behind the India geo-block. Weekly (Mon) sources not due.

**Claims banked.** [[Google Auction & Smart Bidding#GA-085|GA-085]] T1: Google has spent thirteen months shipping instruments that make Demand Gen comparable to other platforms on the other platform's terms, and six of the thirteen drops carry one. [[Google Auction & Smart Bidding#GA-086|GA-086]] T1: one study, one May-to-June-2025 window and one over-fifty-products survivorship filter back **both** a 20% product-feed figure in October 2025 and a 33% one in May 2026, the qualifier moving from "tROAS goals" to "large product selections" while the data stood still. [[Google Auction & Smart Bidding#GA-087|GA-087]] T1: the October 2025 drop footnotes its 11.5% new-customer figure with "internal studies conducted on **Search & Shopping campaigns**", which is not the product the post is about. [[Google Auction & Smart Bidding#GA-088|GA-088]] T1: a census of all seventeen headline figures in the series, where **three carry no footnote at all**, three name a real experiment or A/B test, one is a third-party retail panel of 127 brands, and the rest are averages over self-selected adopters with no control group. [[Creative Science#CR-266|CR-266]] T1 for the statement only: Google wrote in November 2025 that Pathmatics-provided images and videos would arrive in the Google Ads asset picker so advertisers can "lift and shift top-performing creative assets from other platforms into Demand Gen", stated as coming and never confirmed shipped.

Merges into **GA-068** (backlog closed, forward pointer to the census), **GA-081** (the pattern it called stable is now measured across the whole series) and **GA-083** (its footnote has an October 2025 twin behind a different number).

**Law moved once.** The SKILL.md hot layer carries a new cross-channel rule: Google's default columns and Meta's default columns are two different attribution models, so a side-by-side of the two default sets is not a comparison. Use the matched set when the question is which channel to fund, say which column set produced every number, and never mix the two inside one table. The limit is unchanged, these are first-party instruments measuring their own product, and the only counterfactual this codex owns on Demand Gen is still a 21-day geo holdout that found no new-customer lift (GA-055, AT-072). Alongside it, a standing reading rule: **read the footnote before you read the sentence.**

**Gaps carried forward.** The arXiv single-hit-in-first-or-last-sentence fix now has three supporting observations and zero counter-examples and is still an instruction rather than code in `lib/watchlist_check.py`. The Google Ads Announcements page is confirmed for a third day as not a superset of Google ads product news. TikTok policy and creative stay unmonitored until a non-India egress exists.

**Run split across two sessions.** The 16:12 session completed the harvest, the watchlist, the merge and the hot layer and exited without writing a log, so the watchdog relaunched at 21:52. The second session verified the merge on disk, spot-checked the October 2025 footnotes at source against GA-086 and GA-087, both matching word for word, and wrote this entry, the run log, the commit and the team sync.

"""


def main():
    # 1. Watchlist.md, preserve whichever line ending that paragraph uses
    s = read_raw(WL)
    for eol in ("\r\n", "\n"):
        old = WL_OLD.replace("\n", eol)
        if s.count(old) == 1:
            new = WL_NEW.replace("\n", eol)
            write_raw(WL, s.replace(old, new))
            print("Watchlist.md amended, eol=%s" % repr(eol))
            break
    else:
        print("WATCHLIST AMEND FAIL")
        sys.exit(1)

    # 2. Harvest Log.md, research entry above today's teacher entry
    s = read_raw(HL)
    eol = "\r\n" if s.count("\r\n") > s.count("\n") - s.count("\r\n") else "\n"
    anchor = "## 2026-09-26 (teacher run;"
    n = s.count(anchor)
    if n != 1:
        print("HARVEST LOG ANCHOR FAIL count=%d" % n)
        sys.exit(1)
    before = len(s)
    entry = HL_ENTRY.replace("\n", eol)
    s = s.replace(anchor, entry + anchor, 1)
    write_raw(HL, s)
    print("Harvest Log.md: %d -> %d chars, eol=%s" % (before, len(read_raw(HL)), repr(eol)))


if __name__ == "__main__":
    main()
