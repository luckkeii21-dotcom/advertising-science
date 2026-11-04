# Merge pass 2, 2026-11-04. Jon Loomer "Your Extra Ad Sets Are Costing You 28% More"
# plus arXiv ReuseGR. Amendments only, no new claim IDs.
import io

SCI = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science"
LS = SCI + r"\Learning & Signal.md"
MD = SCI + r"\Meta Delivery & Andromeda.md"

LOOMER = 'Jon Loomer, "Your Extra Ad Sets Are Costing You 28% More", 2026-11-04'
REUSEGR = 'arXiv:2611.04259, "ReuseGR: Offline-Online Decoupled Generative Retrieval via Adaptive Prefix Reuse", abstract read 2026-11-04'


def patch(path, claim_id, new_text, newdate, source):
    t = io.open(path, encoding="utf-8").read()
    i = t.index("### " + claim_id + " \u00b7")
    j = t.index("\nSources:", i)
    k = t.index("\nLast touched:", j)
    eol = t.index("\n", k + 1)
    src_line = t[j + 1:k]
    if source not in src_line:
        src_line = src_line.rstrip() + "; " + source
    out = (t[:j] + "\n" + new_text.strip() + "\n"
           + src_line + "\nLast touched: " + newdate + t[eol:])
    io.open(path, "w", encoding="utf-8").write(out)
    print("patched", claim_id, "in", path.rsplit("\\", 1)[-1])


LS035 = """
FOURTH OPERATOR, AND HE PUTS A NUMBER ON THE TWO-AD-SET CASE, 2026-11-04. Jon Loomer arrives at the same gate from Meta's newly published formula at [[Learning & Signal#LS-089|LS-089]] and lands harder than anyone else on file: "if you're struggling to get the results you want, start by consolidating your budget. One campaign and one ad set. Only consider a second ad set if you're generating at least 100 conversions per week." **That is a 2x headroom rule, and it is stricter than the arithmetic.** Meta's own formula permits two ad sets at exactly 100 conversions a week; Loomer makes 100 the floor at which a second one may be CONSIDERED. **His second condition is the part no other operator states: clearing the arithmetic is necessary and not sufficient.** "But even then, only do it because you have a really good reason for it. Typically, that means there's a problem you're solving with that second adset." He names the two reasons he most often finds insufficient, and both are common on our own book: "unnecessary targeting segmentation reasons" and "separate adsets just for creative testing". On creative-testing ad sets specifically he does not oppose them in principle, only on budget: "I don't necessarily oppose separate campaigns or adsets for creative testing if your budget can support it, but more often than not, it can't." His evidence is the same class as Charley T's and Heath's, pattern recognition from audits and one-on-one sessions, with no account on screen and no comparison run: "I see struggling accounts all the time, whether it's an audit or a one-on-one session... this is so, so common." So the count of operators on the consolidation side goes to four and the quality of evidence on that side does not change. Theriot's contesting account at 10 to 20 live ad sets nowhere near the threshold still stands unanswered by any of them.
"""

LS089 = """
INDEPENDENT ENDORSEMENT OF THE FORWARDS READING, 2026-11-04, AND IT IS THE DIRECTION THIS CLAIM ARGUES FOR. Jon Loomer read the same post and used the formula exactly the way the reconciliation above prescribes, forwards from a budget he already has to a ceiling on ad set count. He works it on screen: $2,000 a week at a $20 cost per result gives $20 x 50 = $1,000, and $2,000 / $1,000 = two ad sets maximum. **He also judges the formula unnecessary, which is worth carrying because it is a check on treating a published formula as a new finding:** "I don't think you should need this formula to understand this concept because it's not that complicated. Are you getting fewer than 50 optimized conversions per week per adset? If you are, you're probably running too many adsets at once." His operating line off the back of it is stricter than the arithmetic and lives at [[Learning & Signal#LS-035|LS-035]].

**AND HE PROPAGATES THE 28% WITHOUT THE FOOTNOTE, WHICH IS A FINDING ABOUT THE FIGURE AND NOT EVIDENCE FOR IT.** Loomer quotes "in our analysis, adsets under that threshold ran about 28% more expensive per purchase", reads it as Meta finally supplying data ("For the first time, Meta is providing data to support the recommendation of 50 conversions per week"), sharpens it into an average ("on average, if you're under the threshold of 50 conversions per week, it will result in about a 28% higher cost per purchase"), and closes on it as a decision input: "Not 2% or 8%, but 28%. That's a really big deal and difficult to ignore... Why would you intentionally increase your costs by 28%." **He does not remark on the missing population, sample, window or control, and he does not notice that the sub-50 versus over-50 comparison is also a small-accounts versus large-accounts comparison, which is the selection defect [[Meta Delivery & Andromeda#MD-171|MD-171]] exists to catch.** This changes nothing about the figure and everything about how we will meet it: the 28% is now in circulation through a credible operator with Meta's hedge stripped off and an "on average" added that Meta never wrote. **The standing instruction holds unchanged. Carry the direction, never the 28%, and expect to hear it quoted back by clients and operators who got it from here rather than from Meta.** Note also what he is honest about and Meta is not: he states plainly he has been giving this advice "for years" on mechanism alone, so the post changed his evidence and not his position. He is also the first source anywhere to call the post's provenance into question on its face, "it was obviously written entirely by AI", twice, which is not an argument against the content and is a reason the unfootnoted-figure pattern at law level keeps recurring.
"""

LS060 = """
SECOND OPERATOR ON THE DO-NOT-CHASE-IT SIDE, 2026-11-04, AND HE HOLDS BOTH HALVES AT ONCE. Jon Loomer reaches this claim's conclusion from the opposite starting point, having just endorsed Meta's 28% penalty figure as real and difficult to ignore ([[Learning & Signal#LS-089|LS-089]]). He then names the single-ad-set sub-threshold account explicitly and tells it to carry on: "maybe a response is that your entire budget is running through a single ad set and you're not getting 50 optimized conversions per week. This is a common problem, especially when trying to get sales. You would need to double your budget just to give yourself the chance of reaching 50 per week, and that sounds incredibly risky. So, as long as you're getting results that are good enough to make it worthwhile, which is entirely possible, keep doing what you're doing. I have no problem with that." **The tension inside one source is the useful part, because it is the position our own book has to hold.** On his own reading those accounts are paying the 28%, and he still rules out doubling the budget to escape it and still calls the results potentially good enough. So the decision rule he lands on is unit economics, not the label and not the threshold: results good enough to make it worthwhile. He gives the platform its say rather than hiding it ("Meta would probably say that your costs would likely improve once you were to reach that magic number of 50") and declines to act on it. **For our book this is the second independent operator, now from ecommerce-weighted practice rather than high-ticket lead gen, declining to manage toward the threshold.** His sharp distinction is which account is actually making the mistake: not the one that cannot reach 50 on its whole budget, but the one that "has the budget to achieve 50 optimized conversions per week" and splits it anyway. Nothing measured, no account shown, and the 100-per-week line he offers instead is at [[Learning & Signal#LS-035|LS-035]].
"""

MD191 = """
**EXTERNAL CORROBORATION THAT THIS ARCHITECTURE IS A DEPLOYED PRODUCTION TECHNIQUE IN AD RETRIEVAL, AND IT ADDS ONE MECHANISM DETAIL META DID NOT STATE, 2026-11-04.** An arXiv paper on an industrial search-advertising system, ReuseGR, builds exactly the pipeline Meta describes here, generating Semantic IDs and matching them to catalogue items, and treats it as the established baseline rather than the novelty. Its own contribution is a latency optimisation, and the optimisation is the informative part: **it splits the work into a query-level plan that can be shared and cached across people, and a request-level completion that cannot, because "when different users submit the same query, generating complete Semantic IDs (SIDs) for every request repeats computation, while their interaction histories call for different results".** A 7B offline planner produces SID prefix sets shared by everyone issuing the same query; a 0.5B online model then uses the individual's own history to choose a prefix and generate the remaining tokens. **Read against the claim above, that says the person-specific half of the ideal-ad description is the expensive half, and the platform-side incentive is to cache everything that is not person-specific.** It is also independent support for the thing operators find hardest to accept here, that two people issuing the identical query should be matched to different ads by design.

**Guards, and they are heavy.** This is not Meta and it is not Google, the platform is never named, and we do not buy it. Same treatment as [[Auction Mechanics & Bidding#AU-101|AU-101]] (Pinterest): read as how this class of system is built, never as a statement about any account we run. Its numbers are infrastructure results on an unnamed advertising platform, 3.83 percentage points of query-level HR@100, 38.9% lower mean online latency, and a 14-day A/B at +0.93% click-through rate and +1.05% revenue per thousand requests on roughly 2M query-item records. **None of those travel anywhere near a client, and nothing in the paper is a lever: there is no setting, no report and no advertiser surface in any of it.** The scale is also far below Meta's: a 3.38M-item catalogue against the billion-ads-per-second pool at [[Meta Delivery & Andromeda#MD-188|MD-188]].
"""

patch(LS, "LS-035", LS035, "2026-11-04", LOOMER)
patch(LS, "LS-089", LS089, "2026-11-04", LOOMER)
patch(LS, "LS-060", LS060, "2026-11-04", LOOMER)
patch(MD, "MD-191", MD191, "2026-11-04", REUSEGR)
print("merge pass 2 complete")
