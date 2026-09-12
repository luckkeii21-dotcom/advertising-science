# -*- coding: utf-8 -*-
"""2026-09-12 research merge, phase 3: MD-013 source add."""
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")

p = SCI / "Meta Delivery & Andromeda.md"
t = p.read_text(encoding="utf-8")

OLD = ("Sources: Dr. Matt Shiver, How the Facebook Ads Algorithm Actually Works, 2026-07-21 (UI shown) "
       "and Facebook Ads Tutorial for Beginners Updated for 2026, 2026-03-24 (UI shown, toggle demonstrated live);")

ADD = """**A large advertiser states the same build as its whole targeting policy, 2026-09-12.** Instant Hydration, in a Meta-published case study, runs Advantage+ audience and Advantage+ placements on every ad set, with one manual lever: a lifecycle exclusion of existing customers. "We take a very hands-off approach to Meta. Instead of getting reliant on the technical side of Ads Manager, we diversified the creators we work with, which let us expand to different audiences organically." This adds nothing mechanical to the claim and it is worth one line, because it is the exclusion-is-the-only-real-control position stated by a spending advertiser rather than by an agency, and because the audience expansion is credited to CREATOR DIVERSITY rather than to any setting, which is [[Meta Delivery & Andromeda#MD-001|MD-001]] restated from the buy side. Vendor-published, nothing shown.
"""

assert t.count(OLD) == 1
t = t.replace(OLD, ADD + OLD, 1)

OLDTAIL = ("Ben Heath, Facebook Ads Targeting Just Changed Here's What It Means, 2026-03-27\n"
           "Last touched: 2026-08-23")
NEWTAIL = ("Ben Heath, Facebook Ads Targeting Just Changed Here's What It Means, 2026-03-27; "
           "Meta for Business News, Performance Spotlight: How Instant Hydration Built a System for AI to Scale, 2026-09-10\n"
           "Last touched: 2026-09-12")
assert t.count(OLDTAIL) == 1
t = t.replace(OLDTAIL, NEWTAIL, 1)

p.write_text(t, encoding="utf-8")
print("phase 3 done")
