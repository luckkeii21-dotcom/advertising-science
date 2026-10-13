import pathlib

p = pathlib.Path(r"E:/claude code marketing skill/.claude/skills/advertising-science/SKILL.md")
t = p.read_text(encoding="utf-8")

anchor = "See law 4g.**"
assert t.count(anchor) == 1, t.count(anchor)
assert "MD-174" not in t

addition = (
    anchor
    + "\n\n**2026-10-13: part of that unmeasured noise floor now has a NAMED T1 CAUSE, and it is not the auction (MD-174, T1).** "
    "Meta published the system that spends idle inference capacity on ads ranking. Two levers move with whatever hardware happens to be "
    "free at that moment: **Rank More Ads** raises the number of candidates the ranking stages evaluate, and **Serve Better Models** raises "
    "the share of requests scored by a more powerful model. Both are governed by controllers that react on the order of minutes, with "
    "value-aware load shedding underneath that drops optional work **within a few milliseconds** when capacity is reclaimed. The practical "
    "statement: **the amount of ranking work your ad gets is a function of Meta's spare hardware in that region at that instant, and no "
    "account setting can see it or influence it.** This does not make the noise floor any smaller and it does not change a single instruction "
    "in this law. It removes an explanation we were tempted by, that a twin divergence must mean the twins were competing or that something in "
    "the account changed, and it adds a cause that is invisible from inside Ads Manager. Meta publishes no magnitude for any of it, so this "
    "stays a reading rule and never a lever. [[Meta Delivery & Andromeda#MD-175|MD-175]] carries the companion finding worth quoting to a "
    "client: Meta permanently spends its own scarce capacity on exploratory traffic rather than locking in the allocation that currently looks best."
)

p.write_text(t.replace(anchor, addition), encoding="utf-8")
print("law 23 updated")
