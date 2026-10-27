import io, re, os

SCI = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science"
CS = os.path.join(SCI, "Creative Science.md")
SRC = "Ben Heath, This new Facebook Ads trend is crazy..., 2026-10-27"

t = io.open(CS, encoding="utf-8").read()
orig = t


def block(text, head):
    i = text.index(head)
    j = text.index("\n### ", i + 10)
    return i, j, text[i:j]


# ---------- CR-196 -> contested ----------
i, j, blk = block(t, "### CR-196 \u00b7 Do not put images and video in the same ad set")
assert "Tier: T3 \u00b7 Status: active" in blk
nb = blk.replace("Tier: T3 \u00b7 Status: active", "Tier: T3 \u00b7 Status: contested", 1)
add = """
**CONTESTED 2026-10-28, and the split runs down the middle of the claim: a second operator corroborates the MECHANISM and rejects the PRESCRIPTION.**

Ben Heath runs the opposite structure deliberately. "I like to put multiple ad formats in one adset. So we have a mixture of statics and videos and other and the meta can choose which ads to put in front of which people, where to allocate spend." He states three reasons: different people respond to different formats, Meta sequences them (his description is a video to build awareness then statics on retargeting), and Meta reads session length, so a long lunchtime session gets the video and a check of the phone before bed gets the image.

**The mechanism half of this claim survives and is now reported by two operators.** Heath's finding at [[Creative Science#CR-289|CR-289]] is that inside those mixed ad sets one format takes the budget. He names the direction as statics, where this entry's original source named videos. **So "one format cannibalises the other" has a second independent sighting, and which format wins is not fixed.** Neither operator publishes a spend split.

**The prescription half is genuinely contested and cannot be settled from the roster.** Mark Builds Brands says separate the formats so neither starves. Heath says mix them so Meta can allocate and sequence. **Meta's own measurement sits on Heath's side of the structural question and not on his reasoning for it:** [[Creative Science#CR-261|CR-261]] (T1) measures format diversity INSIDE the ad set and reports 7.3% lower cost per acquisition for ad sets carrying an image, a video and a vertical video with audio together. A T1 observational measurement does not refute a T3 delivery observation, because both can hold at once: the diverse ad set can perform better on average AND starve one of its formats.

**The reading rule both sides agree on, and it is the only instruction to carry today: check spend by format before judging a format.** A static that "failed" in a mixed ad set may never have been funded, and from 2026-10-28 the same sentence has to be read in reverse as well, because the video is now the one that can go unfunded.
"""
nb = nb.rstrip("\n") + "\n" + add.strip("\n") + "\n"
nb = nb.replace("Last touched: 2026-08-27", "Added source: " + SRC + "\nLast touched: 2026-10-28")
t = t[:i] + nb + t[j:]

# ---------- CR-031 ----------
i, j, blk = block(t, "### CR-031 \u00b7 Animating a winning static")
add = """
**A second operator predicts the two formats CONVERGE, added 2026-10-28, and it is a forecast rather than a finding.** Ben Heath, 2026-10-27: "I think we're going to see a blurring of the lines between what is a static and what is a video... instead of it just being there ready when someone scrolls, the text appears a split second after the background image, maybe one of the elements sort of flies in from the left." His reason is that the animated static keeps the static's advantage, the whole offer readable in a glance, and buys the one thing video has that matters to him, movement to interrupt a scroll.

**Tier it honestly: T4.** He names no account, no cost, and no comparison between an animated and a flat version of the same design, and he presents it as what he expects rather than what he has measured. **What makes it worth a line is the agreement with the source above on a point neither tested:** both treat the animated static as a format in its own right rather than as a cheap video, and both reach it from production economics. The entity-ID claim at the head of this entry is still hedged by its own source and still untested.
Added source: """ + SRC + """
"""
t = t[:i] + blk.rstrip("\n") + "\n" + add.strip("\n") + "\n" + t[j:]

# ---------- CR-239 ----------
i, j, blk = block(t, "### CR-239 \u00b7 A static gets a glance where a video gets seconds")
add = """
**A second independent operator on the audience half, and he adds the condition that makes it testable, 2026-10-28.** Cottrell places statics at the bottom of the funnel because the viewer already knows the brand. Ben Heath arrives at the same place from his own account and then states what has to be true for it to hold: "all my ads are going to warm audience... we just need to describe the offer, make sure my face is on it so there's recognition and then very quickly explain what they need to do. And if we have a video we get the drop off so it's not worth it." He generalises it to any advertiser with an organic following: "a lot of warm audience advertising we're seeing work well with statics, people who have followings, organic content as part of their strategy, then static ads are outperforming."

**He also names the inverse, which this entry did not have.** Video is the format when the thing being sold is NEW and has to be explained, or when the sale depends on believing the seller's expertise. "If you've invented something new or you've come up with a brand new concept, video is likely to perform better for you because you need the time and space to explain it." Both halves are asserted off his own and client accounts with no figures.

**So the two operators now agree on a conditional rather than on a format: the static's yield rises with what the viewer already knows, and falls toward nothing on an unexplained product sold to a stranger.** That is a cheaper rule than "statics are bottom of funnel", and it is checkable on any account running both a cold and a warm ad set.
Added source: """ + SRC + """
"""
t = t[:i] + blk.rstrip("\n") + "\n" + add.strip("\n") + "\n" + t[j:]

# ---------- CR-048 ----------
i, j, blk = block(t, "### CR-048 \u00b7 Statics still work across the awareness spectrum")
add = """
**The production-economics argument gets its creative-volume version, added 2026-10-28.** Blue Sense's case in this entry is cost of production against contribution margin per ad. Ben Heath makes the same case against the volume target instead of against margin: "if you're trying to hit 20 ads, if you're doing that with say 16 statics and four videos, a lot easier than 10 and 10." Post-Andromeda creative volume is a requirement this codex already carries, so the format mix is partly set by what the production budget can physically reach, before any performance comparison is run.

**His direction of travel runs against this entry's headline and is filed separately at [[Creative Science#CR-289|CR-289]]**, where the evidence and its weaknesses are set out. Read the two together: this entry holds that statics produce fewer winners than b-roll video on one operator's accounts, CR-289 holds that statics are now taking the budget on another's. **Neither is a format law, and the codex now contains shown instances in both directions, so a format decision made from this file alone is a coin flip. Split your own account's cost per result by format before deciding where the next production budget goes.**
Added source: """ + SRC + """
"""
t = t[:i] + blk.rstrip("\n") + "\n" + add.strip("\n") + "\n" + t[j:]

# ---------- CR-202 ----------
i, j, blk = block(t, "### CR-202 \u00b7 When the ad is obviously AI, stop hiding it")
add = """
**A flat contradiction from a second operator on the PHOTOREAL branch, added 2026-10-28, and it does not touch the stylised one.** Ben Heath, 2026-10-27: "you want to be careful making tons of statics and image ads that look like they're AI generated. We find them not perform well at all." His allowance is narrow and it is about concealment succeeding rather than about declaring the medium: a real product photograph placed by AI into a background or onto a model, "no one can tell. Brilliant. Go ahead and use those."

**Read carefully, the two operators are not contradicting each other, which is why nothing here changes status.** This claim's point is that the uncanny valley is escaped by declaring the format, in claymation or 3D character work. Heath is describing an ad that reads as AI while trying to pass as real, which is the failure mode this claim says to stop attempting. **The combined rule: either the render is undetectable or the format is openly not real. The ad that loses is the one caught in between.** Heath states no per-ad figures, so this is assertion against assertion on the photoreal side, and it matches our own house rule for photoreal work.
Added source: """ + SRC + """
"""
t = t[:i] + blk.rstrip("\n") + "\n" + add.strip("\n") + "\n" + t[j:]

# ---------- NEW CR-289 ----------
new = """
### CR-289 \u00b7 The format trend REVERSED: statics are taking the budget inside mixed-format ad sets, and the only number behind it is an audience poll
Tier: T3 \u00b7 Status: active
Ben Heath, 2026-10-27. Advertising on the platform since 2013, states more than $300 million of lifetime spend, "hundreds of clients at any one time" and "almost a hundred million dollars last year". He frames the finding as a reversal of the one creative trend that has held for a decade.

**Two pieces of evidence arrive together and they are not the same strength. Separate them before carrying either.**

**One, the delivery observation, and it is the more useful half.** His standard structure puts several formats in a single ad set and lets Meta allocate. "We started noticing a trend recently where Meta was allocating more and more budget to statics to images." Asserted across an agency book. No account named, no window, no spend split, no cost per result, nothing on screen.

**Two, the poll series, which is the only thing carrying numbers.** Four readings of his own YouTube audience, the same question each time, which format works best for you:

| Reading | Static or single image | Video |
|---|---|---|
| About 4 years before 2026-10-27 | 38% | 44% |
| About 3 years before | lower than 38% | 53% |
| About 2 years before | 27% | 60% |
| 3 days before the recording | **54%** | **38%** |

**The guard that sets the tier, and it is the whole reason this is T3 and not T2.** A poll of an advertising audience measures what advertisers BELIEVE their accounts returned. Not one of the four readings publishes a respondent count, none is weighted by spend, "best results" is never defined, the pool is self-selected, and its composition is four years apart between the first reading and the last. **A wave of newer advertisers producing cheap AI statics would move this poll with no change in the auction at all.** Carry the direction. Never quote the 54%, and never put any of these percentages in front of a client.

**Where the codex already stood, because the direction is not new here.** [[Creative Science#CR-167|CR-167]] is the same operator's screen share from 2026-02-24 showing video at 856 GBP against images at 189 and carousel at 222 in one account, with more of the budget sitting on the expensive format. [[Creative Science#CR-048|CR-048]] carries the production-economics case for over-indexing on images. Against it, [[Creative Science#CR-233|CR-233]] is a shown account where moving from statics to video cut cost per purchase from $491 to $119. **So the codex holds instances in both directions and no format law is available. What this adds is a second operator reporting the direction from the delivery side rather than from a cost column.**

**His stated mechanism is T4 and must not be repeated as a cause.** Shrinking attention spans and higher video drop-off, so an image delivers the whole offer to everyone who glances at it while a video delivers the call to action only to whoever survives to the end: "how many people even make it to the end where you've actually got your call to action? Like is your drop off rate 90%? That wouldn't be unusual." He says the higher drop-off is visible in his numbers and shows none. The second limb is a feed-contrast argument, that a static now interrupts a feed which is mostly video, exactly inverting the position statics held when Instagram was an image feed. Plausible, unmeasured, and it predicts its own decay as everyone moves back.

**The prescription is the part to act on, and it is not "switch to statics".** "Don't just make statics." He keeps both formats in the same ad set so Meta can allocate and sequence them, which contradicts [[Creative Science#CR-196|CR-196]] (now contested) and agrees with Meta's own measurement at [[Creative Science#CR-261|CR-261]]. He attaches one craft requirement specific to the format: a static has no room to explain, so it has to name its buyer narrowly. His worked example is running shorts sold not as running shorts but as shorts for sub-zero long-distance running that do not chafe. **That is the same move as cutting one broad ad into ten narrow ones, and the reason it is newly affordable is that statics are cheap, which closes the loop with the volume argument at [[Creative Science#CR-048|CR-048]].**

**Discarded from the same video, recorded so it is not mistaken for evidence.** A paid sponsor segment for a third-party attribution tool asserts Meta tracking is "consistently off by 20 to 30% and as much as 50% plus for long-term sales" and a usual result of "around a 10 to 15% increase in ad revenue". Vendor figures inside a disclosed paid slot with an affiliate commission named on camera. The band is the same folklore-grade range already flagged at [[Attribution & Incrementality#AT-020|AT-020]] and it is not banked.
Sources: """ + SRC + """
Last touched: 2026-10-28
"""
t = t.rstrip("\n") + "\n\n" + new.strip("\n") + "\n"

assert t != orig
io.open(CS, "w", encoding="utf-8").write(t)
print("CR-289 present:", "### CR-289 \u00b7" in t)
i = t.index("### CR-196")
print("CR-196 contested:", "Status: contested" in t[i:i + 300])
for cid in ("CR-031", "CR-239", "CR-048", "CR-202"):
    i = t.index("### " + cid + " \u00b7")
    j = t.index("\n### ", i + 10)
    print(cid, "touched:", "2026-10-28" in t[i:j])
