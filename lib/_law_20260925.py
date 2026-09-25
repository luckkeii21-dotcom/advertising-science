"""Rewrite the SKILL.md hot-layer opening paragraph for 2026-09-25. No law moved."""
from pathlib import Path

SKILL = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")

NEW = (
    "Updated only when the codex changes at law level. Each law cites its claims; depth lives in "
    "the codex. **The 2026-09-25 research pass changed NO law. The YouTube roster returned "
    "nothing for the first time in this engine's history, and the whole day came out of one "
    "Google blog post that turned out to be an instalment of a monthly series nobody here knew "
    "existed** (4 new claims, all Google: GA-081, GA-082, GA-083, GA-084; one merge into "
    "GA-068). **The finding that a media buyer should act on first.** Google's September Demand "
    "Gen drop moves Gmail image ads from a two-click to a one-click format, and Google's own "
    "help centre says a Gmail click is counted from the teaser tap \"whether the click expands "
    "the ad body or navigates directly to the advertiser's site\" (GA-082, T1). **One counter, "
    "two different actions.** Before the switch a Gmail click meant the ad opened; after it, the "
    "same counter means a person reached the landing page. Any before-and-after read of Gmail "
    "clicks, CTR or cost per click across this boundary is comparing an expand against a site "
    "visit. Judge it on conversions and cost per conversion only. The honest limit: that help "
    "article is written for Display and the change lands in Demand Gen, and Google does not "
    "restate the rule on the Demand Gen page, so the mechanism is established and the Demand Gen "
    "application is an assumption to verify in an account. **The number in that post is the "
    "clearest specimen yet of a pattern now at five instances.** Google prints a 40% increase in "
    "conversions at the same ROI, footnoted \"Google Internal Data, Global, Gmail Ads, February "
    "2026\". It measures ADDING GMAIL as a channel, not the one-click change it sits under; the "
    "data window is seven months before the feature shipped; and \"at the same ROI\" makes it a "
    "volume statement at constant efficiency, which is the arithmetic of buying more inventory "
    "(GA-081). **Expect one average-uplift figure over self-selected adopters on every Google "
    "release, and expect none of them to be a lift measurement.** **The process failure of the "
    "day, and it is the third time this engine has found the same shape.** The post linked a "
    "Demand Gen Drops Hub. The drops are MONTHLY and run back to October 2025, and this codex "
    "held exactly one of them. Reading two re-dated the September announcement: Maps inventory "
    "reached Demand Gen in **May 2026**, not September, and product feeds reached **automotive** "
    "in May, which is the line that matters for our two truck dealerships (GA-083). May also "
    "shipped **Uplift Experiments** for Demand Gen, so the channel our own 21-day geo holdout "
    "found no new-customer lift on (GA-055, AT-072) now has a first-party counterfactual "
    "instrument. July's copy says Google's Demand Gen tROAS had been \"overly cautious early "
    "on\" and shipped an upgrade with no toggle and no figure, so **do not compare Demand Gen "
    "tROAS performance across the July 2026 boundary** (GA-084). Eight drops remain unread. "
    "**Said plainly because it is ours: a source can be watched daily and still have a year of "
    "unread instalments behind it.** That is the same failure recorded on Meta for Business News "
    "on 2026-09-20 and again on 2026-09-23, arriving a third time on a Google source. **What did "
    "NOT move.** The affiliate-location half of the September drop names \"dealerships\" and has "
    "no published eligibility rule: the help article Google links for it contains the word "
    "\"affiliate\" zero times, so an SJR Commercial or Phoenix Truxx fit is unverified rather "
    "than available (GA-081)."
)

text = SKILL.read_text(encoding="utf-8")
lines = text.split("\n")
i = lines.index("## Current laws (hot layer)")
j = i + 1
while not lines[j].strip():
    j += 1
assert lines[j].startswith("Updated only when the codex changes at law level"), lines[j][:80]
lines[j] = NEW
SKILL.write_text("\n".join(lines), encoding="utf-8")
print("hot layer rewritten, %d chars" % len(NEW))
