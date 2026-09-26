# -*- coding: utf-8 -*-
"""2026-09-26: rewrite the SKILL.md hot-layer paragraph.

Two law-level changes today: a new cross-platform column rule (GA-085) and the
vendor-figure pattern going from five inferred instances to a seventeen-figure
census with a standing reading rule (GA-086, GA-087, GA-088).
"""
import pathlib, sys

SKILL = pathlib.Path(".claude/skills/advertising-science/SKILL.md")

NEW = (
    "Updated only when the codex changes at law level. Each law cites its claims; depth lives in "
    "the codex. **The 2026-09-26 research pass refuted nothing and added one operating rule. The "
    "YouTube roster returned nothing for a second consecutive day, every watchlist lane returned "
    "nothing, and the whole day came out of closing a backlog this engine flagged yesterday** "
    "(5 new claims: GA-085, GA-086, GA-087, GA-088, CR-266; three merges, into GA-068, GA-081 and "
    "GA-083). "
    "**The new rule, and it governs every cross-channel table we hand a client.** Google has spent "
    "thirteen months shipping instruments that make Demand Gen comparable to other platforms on "
    "the OTHER platform's terms: platform comparable conversion columns that “match the "
    "default attribution used on other platforms”, Target CPC bidding to “compare "
    "performance across ad platforms with the same settings”, view-through-conversion "
    "optimisation “aligning with capabilities you may use on other ad platforms”, and "
    "Campaign Type Attribution plus Uplift Experiments (GA-085, T1). **Google's default columns "
    "and Meta's default columns are two different attribution models, so a side-by-side of the "
    "two default sets is not a comparison.** When the question is which channel to fund, use the "
    "matched set, say which column set produced every number, and never mix the two inside one "
    "table. The limit is unchanged: these are first-party instruments measuring their own "
    "product, and the only counterfactual this codex owns on Demand Gen is still a 21-day geo "
    "holdout that found no new-customer lift (GA-055, AT-072). "
    "**The vendor-figure pattern is now a census rather than five instances.** All thirteen "
    "Demand Gen Drops are read, 1 September 2025 through 24 September 2026, monthly with no month "
    "missing. Of the seventeen headline figures in the series, **three carry no footnote at all**, "
    "three name a real experiment or A/B test, one is a third-party retail panel of 127 brands, "
    "and the rest are averages over self-selected adopters with no control group (GA-088). Two "
    "constructions recur and both move what the sentence promises: “at the same ROI” is "
    "volume at constant efficiency, and “conversions or conversion value” lets the "
    "better of two metrics carry the line. "
    "**Two provenance defects, both found by reading the footnote against the sentence, and "
    "neither visible in the body.** One Google study, one May-to-June-2025 window and one "
    "over-fifty-products survivorship filter back BOTH a **20%** product-feed figure in October "
    "2025 and a **33%** product-feed figure in May 2026; the stated qualifier moved from "
    "“tROAS goals” to “large product selections” while the data stayed still, "
    "so the 33% is the same evidence as the 20% and seven months later (GA-086). And the October "
    "2025 drop footnotes its 11.5% new-customer figure with “internal studies conducted on "
    "Search & Shopping campaigns”, which is not the channel the post is about (GA-087). "
    "**Standing rule for every Google announcement: read the footnote before you read the "
    "sentence.** "
    "**One item to watch for our own creative lane.** Google wrote in November 2025 that "
    "Pathmatics-provided images and videos would arrive inside Google Ads so advertisers can "
    "“lift and shift top-performing creative assets from other platforms into Demand "
    "Gen” (CR-266, T1 for the statement, stated as coming and never confirmed shipped). If it "
    "ships, the collection half of competitor-creative work becomes a platform feature for anyone "
    "who pays for it, and the whole edge moves to judging which ad is actually winning and why."
)


def main():
    s = SKILL.read_text(encoding="utf-8-sig")
    lines = s.split("\n")
    idx = None
    for i, ln in enumerate(lines):
        if ln.startswith("Updated only when the codex changes at law level."):
            idx = i
            break
    if idx is None:
        print("hot-layer paragraph not found")
        sys.exit(1)
    before = len(lines[idx])
    lines[idx] = NEW
    SKILL.write_text("\n".join(lines), encoding="utf-8-sig", newline="")
    print("hot layer line %d rewritten: %d -> %d chars" % (idx + 1, before, len(NEW)))


if __name__ == "__main__":
    main()
