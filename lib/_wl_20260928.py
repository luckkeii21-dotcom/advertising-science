# -*- coding: utf-8 -*-
"""Watchlist.md method notes from the 2026-09-28 run."""
import io

P = (r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing"
     r"\wiki\science\Watchlist.md")

NEW = u"""
### Merchant Center: the 2026-09-22 "transport artefact" was an ORDINAL-DATE BUG, and the fix belongs in every date regex in this file (corrected 2026-09-28)

The 2026-09-22 note above records a plain fetch showing a newest entry of 15 July 2026 against a 2026-09-07 WebFetch showing 11 August 2026, concludes the two transports render the page differently, and rules that the older-looking result is the artefact.

**That conclusion is wrong and it is retired.** Both transports render the same page. Today a plain urllib fetch and a real Playwright browser BOTH reported 15 July as newest, which should have been impossible under the transport theory. The actual cause is in our own pattern: the page renders that entry as **"August 11th, 2026"**, with an ordinal suffix, and a `Month D, YYYY` regex cannot match it, so the scraper skipped the entry entirely and reported the next one down. Widening the pattern to `(st|nd|rd|th)?` and an optional comma surfaced it immediately, along with "August 24th 2026" in the body, which also has no comma at all.

**This is the SECOND occurrence of the same bug in this file.** The Meta for Business News section already warns that the page "uses UK date format ('13th October 2025') on some posts, which a `Month D, YYYY` regex silently misses". The lesson did not travel to the Google lane.

**Two standing rules.**
- Every date regex used against any source in this watchlist must accept an optional ordinal suffix and an optional comma: `(January|...|December)\\s+\\d{1,2}(st|nd|rd|th)?,?\\s+20\\d{2}`.
- **Never explain a newest-entry date moving backwards as a transport artefact or a rollback before re-reading with an ordinal-aware pattern.** The failure looks identical to a page change and it is a bug on our side. Merchant Center's true newest entry has been 11 August 2026 throughout, and GP-043 already covers it.

### Meta Advertising Standards: the baseline's offset-150 anchor is brittle, and it failed on a 106-character header change (found 2026-09-28)

The per-section SHA-256 method added 2026-09-14 says to search for the 16 section names in order, starting the first search at offset 150. That offset is load-bearing and undocumented as such, and it broke today.

The page's leading chrome shrank by 106 characters, so `1. Overview` now sits at offset **102**. Starting at 150 skips it and locks onto the page's FOOTER "On this page" navigation list, where all 16 names appear again in order. Every section then hashes 12 to 74 characters of nav text and section 16 comes back not-found. **The output looks exactly like a full-page rewrite and the page had not changed at all.** Re-anchoring on the first occurrence of `Overview` reproduced all 16 baseline lengths and hashes byte-for-byte.

**Two fixes to the baseline, both in `cache/meta-ad-standards-baseline.md`.**
- Anchor on the **first** occurrence of `Overview`, or start at offset 0. Do not use a magic offset that assumes a fixed amount of page chrome.
- Section 16's stored name is `Transparency requirements under the EU DSA`. The page renders **`Transparency requirements under the EU Digital Services Act`**. Match on the rendered string, or on the prefix `Transparency requirements under the EU`.

**The result once anchored correctly: UNCHANGED.** All 16 slices byte-identical to 2026-09-14, including *Restricted goods and services* at 6,531 chars / `75a81517aee32a45`, which is the section carrying Health and Wellness that ChiroWorks and StayWell depend on. Whole-page text is 32,505 chars against a baseline 32,611, and the 106-character difference is entirely header chrome above section 1.

### The Marketing API changelog MOVED, and the index under-rendering artefact did not reproduce (2026-09-28)

`https://developers.facebook.com/docs/marketing-api/marketing-api-changelog` now redirects to **`https://developers.facebook.com/documentation/ads-commerce/marketing-api/marketing-api-changelog`**. The old URL still resolves through the redirect, so nothing is broken, but the table at the top of this file should carry the new path.

Separately, the index under-rendering artefact recorded three times (2026-08-24, 2026-09-07 and once before, where the index showed only through v25.0) **did not reproduce**. The index rendered v26.0, v25.0 and v24.0 in a dated table on the first read. Treat it as fixed and re-open it if it returns. Newest Marketing API version is unchanged at v26.0, 29 July 2026, and **v24.0 carries an Available Until of 6 October 2026**, which is eight days out.

### arXiv filter: the pending first-or-last-sentence rule would have been WRONG today (2026-09-28)

One paper passed the bank-list filter, arXiv 2609.31045, *KuaFu: Compressing Long User Behavior into Understanding at Billion Scale*. It carries exactly two bank-list hits, both the term `advertis`, one in the first sentence ("conversational agents, generative recommenders, and personalized advertising all rest on one capability") and one in the last ("has run on the Tencent advertising and recommendation platform for ten months, lifting overall GMV by 1.37%").

**That is the precise shape of the three recorded false positives, and this one is a TRUE positive.** The paper describes the production user-understanding layer of a real advertising platform at billion-user scale, with deployment numbers, and it was banked as LS-083.

So the rule proposed on 2026-09-07 and carried as a gap ever since, discount a bank-list hit confined to the first or last sentence of an abstract, **would have suppressed a genuine finding today.** The co-occurrence variant (require two distinct bank terms) would also have suppressed it, because both hits are the same term. This is the first counter-example against a rule that previously had three supporting observations and none against. **The gap stays open and the rule stays unshipped, and the reason has changed: it is no longer only that enforcing a judgement in code is Lucky's call, it is that the rule as specified is now known to produce false negatives.** Reading the abstract remains the only method that has never been wrong.
"""

with io.open(P, encoding="utf-8") as f:
    s = f.read()
if not s.endswith("\n"):
    s += "\n"
with io.open(P, "w", encoding="utf-8", newline="") as f:
    f.write(s + NEW)
print("Watchlist.md updated, +%d chars" % len(NEW))
