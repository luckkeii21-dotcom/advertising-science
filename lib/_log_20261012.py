"""Insert the 2026-10-12 Harvest Log entry at the top of the log."""
from pathlib import Path

LOG = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\Harvest Log.md")
ANCHOR = "## 2026-10-10 (research run)"

ENTRY = """## 2026-10-12 (research run)

**Quiet on advertising, busy on method. 0 transcripts in, 0 claims added, 0 merged, 0 contested, 0 refuted, 0 errors.** Two new platform documents were read in full and both were deliberately not banked. No law changed, so the hot layer is untouched. **Monday, so the weekly lane ran: all seven sources read, and the one that mattered came back clean.**

**The highest-value result: the Advertising Standards hash lane is CLOSED and the policy is unchanged.** The 2026-10-07 entry left this source as a partial close and named the risk plainly, that the per-section hash map could not be diffed through WebFetch and a silent rewrite under an unchanged heading was undetected. **A Playwright browser connected today for the first time in eight runs**, so the hash lane was run. Whole-page `innerText` **32,505 chars, exactly the 2026-09-28 figure. All 16 sections located, zero not-found.** *Restricted goods and services*, the section ChiroWorks and StayWell depend on, is **6,531 chars at `75a81517aee32a45`, byte-identical to the 2026-09-14 baseline**, so that body text is unchanged across 28 days. "Health and Wellness" and "Privacy Violations and Personal Attributes" are both still present. The full 16-section map is now stored, so the next run diffs sixteen hashes instead of one.

**And the same read corrects the 2026-10-07 method note.** It said the heading check is browser-optional. It is not, quite: today's WebFetch read returned *Introduction to the Advertising Standards* as item 1 and **omitted "Overview" entirely**, producing a 16-item list shifted by one that reads exactly like a rename of section 1. The browser carries both strings, Overview as section 1 at 958 chars and the Introduction as the H1. **A correct heading list and the hash map both need the browser.**

**Two method findings that kill false positives, both on Google.** First, **the Google Ads API release notes page carries a per-render nonce.** The weekly fetch reported `changed: true` with the top version unchanged at v25.2, so it was tested with two fetches seconds apart and they differ: a `<script nonce>` value and the key order in the inline analytics blob, 366,207 bytes then 366,203. That flag has probably been firing falsely since the weekly script was written, and it is the same defect already banked on the Google Ads Announcements page. **Never report a raw byte diff on `developers.google.com` as news; diff a stable key.** Second, **on the Merchant Center changelog a max over parsed dates returns an effective date, not a publication date.** The 2026-10-07 rule "take the max over parsed dates on every listing source" returns September 30, 2026 here, which is a sub-heading *inside* the 28 April 2026 pickup-cost entry, a forward-looking EEA compliance deadline. Counting only dates that stand alone on their own line gives 72 entries and the true newest, **24 September 2026, unchanged**. Page order is not date order at either end on that page: 11 August renders first and the two newest render last.

**The two documents read and not banked.** *Launching Structured Data Files v11*, Google Ads Developer Blog, 8 October 2026, the only new post on that blog since 23 September. It is **Display and Video 360 only**: SDF v11 general availability, Lookalike inclusion and exclusion extended to all ad groups except those under YouTube Ad Sequence line items, Business Chain proximity targeting added to the line item format, four YouTube third-party vendor columns reformatted, new columns for YouTube Instant Deal line items in allowlisted beta, and a January 2027 sunset for versions earlier than v10. Zero Search, Shopping or Performance Max content, no delivery or measurement mechanism, and no client on our book runs DV360. Full content recorded in [[Watchlist]] so a future run does not re-read it. Second, **arXiv cs.IR returned exactly one item past the advertising filter and it does not survive reading**: `UxSID` (arXiv:2605.09040v4), a semantic-group shared interest memory architecture for ultra-long user sequences. It is a recommendation-architecture paper, it is a `replace-cross` revision rather than a new submission, and its only advertising content is one clause, **a 0.337% revenue lift in a large-scale advertising A/B test** with no platform named. The filter's standing rule is that ranking, retrieval and recommendation never qualify alone, and having read it there is no advertising mechanism in it. **1 passed the filter, 1 read, 0 banked** is the honest line.

**Everything else quiet.** Harvest: all 12 roster channels listed clean, 0 new, 6 skipped short, 3 no subtitles, 0 errors, 0 RSS fallbacks. Backlog zero against 484 transcripts. Meta for Business: both locales 0 added 0 removed and **identical in order** to the 10 October baseline, US ceiling 8 October, UK ceiling 6 October, cumulative slug set still 26, eighth consecutive browser-free read of both shelves. Meta Engineering 0 new, build Tue 6 Oct, 6 days stale. Meta Newsroom 0 new, build Thu 8 Oct. Google Ads Announcements 396 answer ids, 0 added 0 removed. Ads and Commerce 0 new, build 1 Oct and now **11 days stale**, so the Demand Gen Drops hub was read directly again: **13 cards, newest September 2026, unchanged**, and the October drop is out on neither surface, expected around 24 October. The hub's two cached text anchors no longer render and the page carries zero parseable dates, so the card count is the only stable key left on it. Weekly lane: Graph API unchanged at v26.0 (29 July 2026); Marketing API index **under-rendered to v25.0 for the third time**, with the true newest confirmed as v26.0 on the Graph API page in the same session, so the 2026-09-28 "treat it as fixed" stays withdrawn; AI at Meta newest post 27 July 2026, **77 days flat**, nothing in lane. TikTok SDK changelog unchanged at v0.1.8. **TikTok Newsroom and the for-Business blog were not retried even though a browser was available**, because the India geo-block was verified in August across the browser and curl on four paths each and a browser does not move an egress. Known permanent blind spot, not an outage.

**The 2026-10-11 run did not complete, and it cost one observation.** The harvest JSON exists and is clean; there is no research log and no entry in this file, so the Sunday run died after step 1, and today's watchdog relaunched at 12:55. The weekly lane was unaffected because 11 October was a Sunday. What it cost is the falsifier the 2026-10-10 entry named: an 11 October read of the UK shelf would have held the `creator-marketing-whitepaper` one-day alternation at five points. Today the whitepaper is present and the shelf is identical to 10 October, which is consistent with the alternation **and** with no rotation at all since 10 October. **It distinguishes neither, so the alternation stays at n=4 and must not be reported as holding at five.**

**Gap noticed.** Unchanged for a fourth run and still the cheapest item on the board: the Muse for Small Business adoption question cannot be closed from Meta's own publishing. One ChiroWorks, StayWell or Phoenix Truxx owner answering whether Muse has offered them anything about their ads is worth more than the next three case studies. **Second gap, new today and nearly as cheap:** three of the seven weekly sources fetch cleanly and none of them has a stable diff key, so each is one nonce away from the false positive the release-notes page just produced.

"""


def main():
    txt = LOG.read_text(encoding="utf-8")
    if "## 2026-10-12 (research run)" in txt:
        print("entry already present, nothing written")
        return
    if ANCHOR not in txt:
        raise SystemExit("anchor not found: " + ANCHOR)
    txt = txt.replace(ANCHOR, ENTRY + ANCHOR, 1)
    LOG.write_text(txt, encoding="utf-8")
    print("Harvest Log entry inserted above", ANCHOR)


if __name__ == "__main__":
    main()
