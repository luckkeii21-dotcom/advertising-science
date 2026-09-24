"""Rewrite the SKILL.md hot-layer opening paragraph for 2026-09-24. No law moved."""
from pathlib import Path

SKILL = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\SKILL.md")

NEW = (
    "Updated only when the codex changes at law level. Each law cites its claims; depth lives in "
    "the codex. **The 2026-09-24 research pass changed NO law. It corrected one call this file "
    "made nine days ago, and it produced the first stated COUNT on an argument that has run "
    "unquantified since August** (7 new claims: MD-166, MD-167, AU-095, SC-171, SC-172, CR-265, "
    "GA-080; merges into MD-157, MD-125, SC-044, SC-008, SC-161, AU-051, LS-074, GA-043). "
    "**The correction first, because it was ours.** On 2026-09-15 this engine banked Meta One at "
    "MD-157 and deliberately withheld a warning line, on the reasoning that Meta One \"removes "
    "nothing, bans nothing and breaks nothing\". Meta's own help centre, read at source today, "
    "says otherwise: a Facebook Page is limited to **2 organic posts or comments carrying links "
    "per month** on the free tier and on the $14.99 Essential tier, rising to 8 at $49.99, 20 at "
    "$149.99 and unlimited at $499.99 (MD-166, T1). Meta's announcement frames links in posts as "
    "a new feature. The help article is the same change written as a cap, and it does take away "
    "something that was free. **The one line that keeps this out of every ad decision: links in "
    "ads are explicitly exempt**, along with links to Meta properties, affiliate-partnership "
    "links, and extra links in the comments of a post that already carries one. **Meta also "
    "publishes the article with its own hedge, and it should be quoted every time:** \"Limits on "
    "posts and comments with links may not apply to all Pages.\" Check the client's Page rather "
    "than assuming. Two widely-repeated specifics from the practitioner video that broke this "
    "story do not survive the source: the per-tier Instagram splits are not in the article at "
    "all, and a link in the comments of an already-linked post is exempt rather than counted. "
    "**Meta's own two surfaces also disagree on the Expert and Max prices by a dollar on the same "
    "day**, which is the third documented case of this source contradicting itself after the "
    "card-date drift and the locale partition. **The count, and it is the most useful thing "
    "banked today.** SC-008, whether to kill an ad that is eating an entity's budget, has been "
    "`contested` since 2026-08-19 with four operators asserting one way, one the other, and zero "
    "numbers from anybody. Nick Theriot ran 51 ad-set tests and reports that killing the "
    "top-spending ad to push spend toward a better-converting sibling **failed to hold "
    "performance 99% of the time** (SC-172, T2), and he responded by refusing to make any "
    "ad-level decision inside a testing campaign. It does not close SC-008, because it is "
    "ABO-within-ad-set rather than CBO-within-campaign and because 99% of 51 is recalled on "
    "camera with no log shown. It is still the only number either side has ever produced. **One "
    "operating rule changed shape and it affects every rescue account we take on.** SC-044's 3x "
    "kill gate has been stated against TARGET cost per result by two operators and against "
    "ACCOUNT AVERAGE by a third, and nobody noticed those are different numbers in a failing "
    "account. On an account at a $300 cost per purchase against a $100 target, the "
    "account-average version burns $900 an ad set to learn nothing. **Read the gate as 3x the "
    "smaller of target CPA and AOV, over at least 3 days.** **What did NOT move, said plainly.** "
    "AU-095 is the first shown-account cost-cap procedure in the codex, a ratchet from $30 up in "
    "$5 steps against a $50-to-$60 account average, clearing at a $55 new-customer cost per "
    "acquisition on a $65 target, with the budget set at $3,000 a day precisely because a cap "
    "cannot force spend. The operator who ran it still declines to say it beat the alternative, "
    "because he never ran the alternative. **The count of controlled capped-versus-uncapped "
    "comparisons on the same account across this entire roster is still zero** (AU-051). And "
    "Google's new unified Search-ads-journey report for AI Max is a within-Search attribution "
    "view with no ship date, so the AI-surface spend blind spot at GA-043 stays open for the "
    "second time in eight days (GA-080)."
)

text = SKILL.read_text(encoding="utf-8")
lines = text.split("\n")
# The hot-layer opening paragraph is the first non-empty line after the heading.
i = lines.index("## Current laws (hot layer)")
j = i + 1
while not lines[j].strip():
    j += 1
assert lines[j].startswith("Updated only when the codex changes at law level"), lines[j][:80]
lines[j] = NEW
SKILL.write_text("\n".join(lines), encoding="utf-8")
print("hot layer rewritten, %d chars" % len(NEW))
