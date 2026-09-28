# -*- coding: utf-8 -*-
"""Hot-layer update for 2026-09-28. Law 4b: the 80% folklore verdict was conceded by its own source."""
import io

P = r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md"

ANCHOR = "4c. **Opportunity Score is a vendor recommendation engine"

NEW = u"""**\u26a0 2026-09-28: THE OPERATOR RETRACTED THE 80% HIMSELF, and this file called it folklore first.** The line above says the 80% and 90% figures are folklore traceable to an Ogilvy print-headline observation, with no retention curve behind any of them. Blue Sense, the source of two of the three percentages in circulation, opened a 181-minute scripting masterclass by withdrawing his: "I have said quite often that the hook is 80% of performance... This is not true. This wording is actually bad by me. The hook is not driving 80% of performance." **His replacement is narrower and it survives: the hook is 80% of the AUDIENCE, and it sells nobody.** "There's nowhere near enough scripting within the first 3 seconds to actually be able to sell someone." The operating consequence he draws: "you need to actually focus on the other 57 seconds of the 60-second script." He reports scraping 360 YouTube ad-writing transcripts while preparing and finding 70 to 75% of their runtime spent on hooks. **What this changes for us: keep the audience-selection half, which still carries the production arithmetic and the revival cases, and stop repeating the persuasion half in any form, internally or to a client.** Nothing here touches the open empirical question, which is still whether re-cutting the first 3 to 5 seconds of an EXISTING shoot revives a fatigued winner. Nobody has run it (CR-124, still contested).

**The same pass banked the body-side craft that the retraction points at, 14 new claims off one source.** The nine-beat script and what each beat is for (CR-267); **agitate the ACCOMMODATION, never the symptom**, which is the life change the buyer already made and never admitted, and is the sharpest single idea in the batch (CR-268); **the promise must precede the mechanism**, and a feature with no mechanism gets cut or swapped for proof (CR-269); the proof ladder and the rule that proof must outrank the claim (CR-270); six objections mapped to six script elements in the order they arrive (CR-271); **retention falls at the BRIDGES between beats, and hooks generated in a batch and stitched on are what causes the first drop** (CR-272); length is bought from the problem and mechanism beats and nowhere else (CR-273); **believing is not wanting, which is why a logically perfect ad passes every review meeting and sells nothing** (CR-274); storytelling as a delivery mechanism across all beats rather than a tenth beat (CR-275); sentence craft and the two AI tells, uniform staccato and contrast negation (CR-276); AI scripting is retrieval not invention, and selection is the human job (CR-277); the five research sources and the five outputs that feed five of the nine beats (CR-278); the three-question differentiator test and the specificity ladder (CR-279); the offer outranks the copy and most offer wins are repackaging (CR-280). **All T3.** It is a teaching video from an operator at about $1M a day of spend, with worked rewrites and no split test behind any of it. Brief with it, grade scripts with it, and do not quote a lift figure off it because there is none.

**A Google mechanic that was operator folklore is now in Google's own schema (GA-089, T1).** Google Ads API v25.2, 23 September 2026, adds `RAISE_TARGET_CPA_PERFORMANCE_BID_TOO_LOW` and `LOWER_TARGET_ROAS_PERFORMANCE_BID_TOO_LOW`, in Google's words "when bids are too low for Search campaigns to **enter auctions**." The failure named is non-participation, not underdelivery: a Search campaign that will not spend is target-blocked rather than demand-blocked. Each recommendation returns a `recommended_target_multiplier` sizing the gap. **Read the multiplier as a diagnostic, never as an instruction**, because Google publishes no threshold or confidence behind it and both recommendations point the same way, toward a looser target.

"""


def main():
    with io.open(P, encoding="utf-8") as f:
        s = f.read()
    i = s.find(ANCHOR)
    if i < 0:
        print("ANCHOR NOT FOUND")
        return 1
    s = s[:i] + NEW + s[i:]
    with io.open(P, "w", encoding="utf-8", newline="") as f:
        f.write(s)
    print("hot layer updated, inserted", len(NEW), "chars before 4c")
    return 0


raise SystemExit(main())
