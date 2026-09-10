# -*- coding: utf-8 -*-
"""Append the 2026-09-09 Ads Manager a11y-snapshot trap to the Playwright Meta memory."""
from pathlib import Path

P = Path(r"E:\ClaudeCode\.claude\projects\E--claude-code-marketing-skill\memory\reference_meta_ads_export_via_playwright.md")
t = P.read_text(encoding="utf-8-sig")

ANCHOR = "Related: [[feedback_browser_vs_api_for_meta]]"
assert t.count(ANCHOR) == 1, "anchor not unique"

ADD = """**Reading a SETTING (not exporting data): scan the raw DOM, never the accessibility snapshot. Found 2026-09-09,
after it produced two false findings before being caught.** The Ads Manager **ad-set edit form mounts
progressively**, so `browser_snapshot` and `browser_find` both reported "no Placements section" on two different
ad sets that each had one. The working method:

1. `browser_wait_for` on a string you know sits in the form (`Conversion location`) so it has settled.
2. `browser_evaluate` scanning `document.querySelectorAll('*')` for leaf nodes matching your regex, plus
   `[role=heading]` text. That found Placements instantly where the snapshot saw nothing.
3. For a collapsed section, find the element whose `textContent` equals `Show more settings`, then
   `.closest('[role=button],[role=link],a,div[tabindex]').click()`. **Do not filter the expander on
   `children.length === 0`** — the label is wrapped, and a leaf-only filter misses it.

**An absent section in an Ads Manager a11y snapshot means nothing.** Confirm with a DOM text scan before
reporting that a control is gone. This is how the 2026-09-09 science run checked whether Meta's placement-control
withdrawal had reached our accounts.

"""

t = t.replace(ANCHOR, ADD + ANCHOR, 1)
P.write_text(t, encoding="utf-8")
print("memory updated:", P.name)
