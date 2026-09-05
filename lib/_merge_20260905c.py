# -*- coding: utf-8 -*-
"""Merge pass 3 for 2026-09-05: CR-086 observational note."""
import io, os

SCI = os.path.join(
    "E:\\claude code marketing skill",
    "Obsidian God-level Marketing Vault", "God-level Marketing", "wiki", "science")


def amend(fn, tag, body, add_source=None, touched="2026-09-05"):
    path = os.path.join(SCI, fn)
    lines = io.open(path, encoding="utf-8").read().split("\n")
    s = None
    for i, l in enumerate(lines):
        if l.startswith("### " + tag + " "):
            s = i
            break
    assert s is not None, (fn, tag)
    e = len(lines)
    for j in range(s + 1, len(lines)):
        if lines[j].startswith("### "):
            e = j
            break
    blk = lines[s:e]
    si = max(k for k, l in enumerate(blk) if l.startswith("Sources:"))
    ti = max(k for k, l in enumerate(blk) if l.startswith("Last touched:"))
    if add_source:
        blk[si] = blk[si].rstrip() + "; " + add_source
    blk[ti] = "Last touched: " + touched
    blk = blk[:si] + body.split("\n") + [""] + blk[si:]
    io.open(path, "w", encoding="utf-8", newline="\n").write(
        "\n".join(lines[:s] + blk + lines[e:]))
    print("amended", fn, tag)


amend("Creative Science.md", "CR-086", """**A live instance of the practice this claim says does not work, recorded 2026-09-05 as an observation rather than as evidence.** An operator opens a build video by stating that his funnel's conversion rate has dropped, and rebuilds the page in response. What he changes is the visual and interaction layer: hover states, a shimmering button, a rotating testimonial bar, a styled pop-up form. What he explicitly does not change is the message, instructing the model "we're just going to keep this as same exact copy" and asking only for "a visual refresh, just make this thing look a whole lot better".

**He publishes no outcome.** The video ends with the page deployed and the form integration still broken, and there is no follow-up figure of any kind. So this is not a counter-example to the claim above and it is not support for it either. It is worth carrying for one reason: **it shows how a measured conversion-rate drop actually gets handled in practice, which is a design rebuild that leaves the ad-to-page argument untouched.** That is the exact response the claim above predicts will not produce a win, and it is the response a page-building tool makes cheapest. He does set the rebuild up correctly as a page variation against the original so the two can be compared, and then never reports the comparison.""",
      add_source="Dr. Matt Shiver, How to Use Claude to Build Sales Funnels on GoHighLevel, 2026-04-07")

print("pass 3 done")
