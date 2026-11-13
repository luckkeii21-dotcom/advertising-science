# Watchlist cache commit for the 2026-11-13 research run: Meta for Business
# News shelf reads for both pinned locales, plus the four slugs read today.
import io, json
from datetime import datetime

C = (r"E:\claude code marketing skill\.claude\skills\advertising-science"
     r"\cache\watchlist-seen.json")

US = ["from-measurement-to-capital-allocation",
      "finding-his-squad-again-in-a-facebook-group",
      "how-metas-ads-system-matches-your-ad-to-the-right-person",
      "three-new-ai-innovations-in-ads-ranking",
      "you-dont-beat-the-auction-you-brief-it",
      "muse-smb-jaeluxe-shoetique",
      "agencies-testing-incrementality",
      "meta-nest-ai-creative-diversification",
      "meta-brand-building-summit-2026",
      "muse-smb-bennett-orchards",
      "a-new-way-for-businesses-and-personal-agents-to-work-together",
      "advertising-week-new-york-2026"]

UK = ["meta-ai-now-available-in-hongkong",
      "meta-agency-first-awards-winners-hongkong-2026",
      "meta-marketing-summit-hongkong-2026",
      "you-dont-beat-the-auction-you-brief-it",
      "performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
      "businesses-driving-results-with-meta-ai-ads",
      "closing-the-creator-measurement-gap",
      "2026-winning-hearts-boosting-carts",
      "conversations-2026-introducing-meta-business-agent",
      "social-search-series-2",
      "social-search-series-3",
      "social-search-series-1"]

# Read in full today. The last three were NEVER on either shelf and were only
# reachable by following links out of the 12 November post.
READ_TODAY = ["from-measurement-to-capital-allocation",
              "finding-his-squad-again-in-a-facebook-group",
              "calibrating-attribution-with-incrementality",
              "calibrating-MMM-with-incrementality",
              "suite-of-truth"]

RESULT = (
 "2026-11-13: plain fetch HTTP 400 on BOTH pinned URLs, read through WebFetch. "
 "US shelf MOVED after fourteen consecutive flat reads: 2 in at slots 1 and 2, "
 "2 out from the bottom. IN: from-measurement-to-capital-allocation (12 Nov 2026, "
 "banked AT-137) and finding-his-squad-again-in-a-facebook-group (11 Nov 2026, "
 "Muse customer story, merged into MD-169). OUT: agency-awards-2026 and "
 "introducing-meta-one-plans-for-businesses, both already in the cumulative set, "
 "the ordinary 12-slot rotation. US ceiling moves 28 Oct 2026 to 12 NOVEMBER 2026. "
 "UK shelf 12 slugs, 0 new, order-identical to eight saved reads (10-31, 11-01, "
 "11-02, 11-03, 11-04, 11-05, 11-08, 11-10), so still no sixth distinct UK state. "
 "No 2026-11-12 read exists, so this read covers two days.")

NOTE_LINK = (
 "THE 12-SLOT SHELF IS STRUCTURALLY BLIND TO THE BACK CATALOGUE, AND LINK-FOLLOWING "
 "IS THE ONLY ROUTE IN. The new 12 Nov post links two companion posts, "
 "calibrating-attribution-with-incrementality and calibrating-MMM-with-incrementality, "
 "and the second links a third, suite-of-truth. All three were read in full today and "
 "ALL THREE WERE ABSENT from the 36-slug cumulative set built over seven weeks of daily "
 "reads of both locales. Their own page dates are 22 October (no year printed, placed "
 "2025 by the sequel's back-reference), 29 October 2025 and 28 May 2025. So a four-part "
 "Meta methods series spanning 18 months was invisible to this lane by construction: the "
 "cumulative-slug method can only ever detect a post that enters one of the 12 visible "
 "slots, and the shelf is a curated slice, not a feed. Note the sharpest instance: the "
 "shelf carried a 22 October post at slot 5 (you-dont-beat-the-auction-you-brief-it) "
 "while a different 22 October post sat unseen. METHOD CHANGE: every post read on this "
 "source gets its outbound /business/news/ links extracted and diffed against the "
 "cumulative set, and any miss is read before the run closes. Both 'Show More' controls "
 "render as href='#', so pagination still needs a browser and was not attempted today.")

NOTE_READS = (
 "Four posts banked from today's link-following, all read in full at source: AT-135 "
 "(attribution calibration, the scalar-multiplier recipe and the residual-to-organic "
 "rule), AT-136 (the three-tier MMM calibration taxonomy), AT-137 (the 12 Nov capstone, "
 "incrementality as a finance control), AT-138 (the May 2025 root post, the tool ranking "
 "and the thin Gen Z footnote). The series' actual methodology sits in a report at "
 "facebook.com/business/f/1094917955782254 which was NOT read and is carried as a gap.")

d = json.load(io.open(C, encoding="utf-8"))
m = d["pages"]["meta-business-news"]
cum = set(m["slugs_seen_cumulative"])
added = sorted((set(US) | set(UK) | set(READ_TODAY)) - cum)
m["slugs_us_2026_11_13"] = US
m["slugs_uk_2026_11_13"] = UK
m["last_checked"] = "2026-11-13"
m["result_2026_11_13"] = RESULT
m["note_2026_11_13_shelf_misses_back_catalogue"] = NOTE_LINK
m["note_2026_11_13_posts_read"] = NOTE_READS
m["slugs_seen_cumulative"] = sorted(cum | set(US) | set(UK) | set(READ_TODAY))
d["last_run"] = datetime.now().isoformat(timespec="seconds")
json.dump(d, io.open(C, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("added to cumulative (%d):" % len(added))
for s in added:
    print("  ", s)
print("cumulative now:", len(m["slugs_seen_cumulative"]))
