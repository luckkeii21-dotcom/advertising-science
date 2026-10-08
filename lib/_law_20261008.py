# -*- coding: utf-8 -*-
"""Hot-layer (Current laws) update for the 2026-10-08 research pass.

One law-level statement written on 2026-10-07 is wrong on today's evidence and
is corrected here: the hot layer says Meta's Customer Lifecycle Strategy
rollout means "a product default will now push accounts one way". The ad-set
default is the neutral one, so it does not.
"""
import io, sys

SKILL = r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md"

OLD_LEAD = (
    "**The 2026-10-07 research pass refuted nothing, widened one standing rule to cover every "
    "platform, and added a diagnostic worth memorising** (13 new claims: AU-097, AU-098, MM-226 "
    "to MM-229, CR-284, CR-285, SC-174, MD-170, MD-171, GP-049, LS-085; seven merges, into "
    "AU-034, AU-035, AU-060, AU-080, AU-094, MM-128 and MM-133)."
)

NEW_LEAD = (
    "**The 2026-10-08 research pass corrected one law-level statement written the day before, "
    "closed a question this file had carried open since August, and banked an operating rule for "
    "a control that is now in every client account** (4 new claims: MD-172, MD-173, MM-230, "
    "SC-175; ten merges, into MD-122, MD-123, MD-159, MD-170, AU-019, AU-061, AT-006, LS-001, "
    "LS-007 and LS-027). The 2026-10-07 pass before it refuted nothing, widened the "
    "read-the-footnote rule to cover every platform, and added the CPM-CPA-AOV diagnostic "
    "below (13 new claims: AU-097, AU-098, MM-226 to MM-229, CR-284, CR-285, SC-174, MD-170, "
    "MD-171, GP-049, LS-085)."
)

OLD_CLS = (
    "**\u26a0 One platform change lands in client accounts now.** Meta's Customer Lifecycle "
    "Strategy is available to ALL advertisers, carrying automatic recommendations to exclude "
    "existing customers, and campaign creation itself is moving into an agent with memory of the "
    "account's history and seasonality (MD-170, T1). The exclusion default matters because this "
    "codex argues both sides of it, AU-059 against excluding past purchasers on worked arithmetic "
    "and AU-061 for exclusions because Meta otherwise prioritises warm audiences. A product "
    "default will now push accounts one way."
)

NEW_CLS = (
    "**\u26a0 One platform change is live in client accounts, and yesterday's reading of it was "
    "wrong on the part that mattered.** Meta's Customer Lifecycle Strategy is available to ALL "
    "advertisers, and campaign creation itself is moving into an agent with memory of the "
    "account's history and seasonality (MD-170, T1). This file said a product default would now "
    "push accounts one way on the exclusion question it argues both sides of, AU-059 against "
    "excluding past purchasers on worked arithmetic and AU-061 for exclusions because Meta "
    "otherwise prioritises warm audiences. **It does not. The ad-set default is \"get conversions "
    "from all audiences\", leaving it alone changes nothing, and even after choosing \"acquire new "
    "customers\" the ENGAGED audience is not excluded unless an operator adds those audiences by "
    "hand.** Meta made the choice easier to express and did not take a side. The place a default "
    "could still appear is the campaign-creation agent, because a recommendation surfaced at build "
    "time is a far stronger nudge than a radio button that starts neutral. **Two operating rules "
    "come with it.** The control survived Marketing API v26.0, which this file had carried open "
    "since 24 August (MD-122). And if you are going to exclude existing customers, do it through "
    "Customer Lifecycle Strategy in a NEW ad set, never by editing exclusions into a live one: one "
    "operator reports the exclusion field collapsing delivery where the ad-set control does not, "
    "and his comparison is confounded because editing targeting on a running ad set resets the "
    "learning phase under LS-002, so the mechanism is unproven while the instruction is safe "
    "either way (MD-172, T3). **Never promise a client that a new-customer-only offer will be seen "
    "only by new customers.** List matching is roughly half, estimated and unmeasured, so the "
    "exclusion leaks (MD-123). **And the first audience-segment breakdown anyone has actually "
    "shown says the fear is account-specific, not general:** 581 purchases over 30 days split 310 "
    "new, 227 engaged and 43 existing, so existing customers took 7.4% while carrying the highest "
    "frequency and the cheapest cost per result (MD-173, T3). The drift mechanism is real and in "
    "that account it was cheap. Read the breakdown before telling a client it is happening to them."
)

OLD_WIDE = (
    "**The rule now reads: on ANY platform announcement, find the population and the counterfactual "
    "before carrying the number, and when there is no footnote the number is an illustration, not a "
    "measurement.**"
)

NEW_WIDE = (
    "**The rule now reads: on ANY platform announcement, find the population and the counterfactual "
    "before carrying the number, and when there is no footnote the number is an illustration, not a "
    "measurement.** It earned its keep the next day. Meta's creator white paper of 7 October "
    "carries one real number, an IPA long-term ROI index of 151 for creator content against a "
    "short-term index of 99 across 220 campaigns and 144 brands, and the page states no index base, "
    "no methodology, no markets and no date range, on a databank built from cases advertisers "
    "submit for awards. **Quote the direction, never the digits: creator content pays back long "
    "rather than fast, so a creator ad judged on a 7-day window is being judged on its weakest "
    "axis** (MM-230, T3). The same page also restates the 4x creator-growth multiple that Meta "
    "footnoted in September, with the footnote gone (MD-159)."
)

def main():
    t = io.open(SKILL, encoding="utf-8").read()
    ok = True
    for name, old, new in [("lead", OLD_LEAD, NEW_LEAD),
                           ("cls", OLD_CLS, NEW_CLS),
                           ("widened-rule", OLD_WIDE, NEW_WIDE)]:
        n = t.count(old)
        if n != 1:
            print("!! %s : found %d occurrences, expected 1" % (name, n))
            ok = False
            continue
        t = t.replace(old, new, 1)
        print("UPDATED  -> hot layer : %s" % name)
    if not ok:
        print("\nNO WRITE. Fix the anchors first.")
        return 1
    io.open(SKILL, "w", encoding="utf-8", newline="").write(t)
    print("\nHOT LAYER UPDATED")
    return 0

if __name__ == "__main__":
    sys.exit(main())
