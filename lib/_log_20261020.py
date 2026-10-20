# -*- coding: utf-8 -*-
"""Harvest Log entry + run log for the 2026-10-20 research run."""
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
           r"\God-level Marketing\wiki\science")
RUNS = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\runs")
TODAY = "2026-10-20"

ENTRY = """
## 2026-10-20

**0 transcripts, 6 claims banked, 12 merges, law layer amended. Codex 1,379 to 1,385.** Tuesday, so
the weekly lane was not due; the Monday lane ran yesterday and wrote its log, so nothing was owed.

**The day's haul came from one Meta engineering post published yesterday, and the most valuable thing
in it is a word rather than a number.** Meta published GenRecs Tokenization on 19 October. The ad's
own text and images are now stated by Meta to be what the model reads to build its representation of
the ad, which is the best T1 sentence law 1 has ever had (MD-184). The same post's framing word,
"generative", is the trap: the retrieval paper it cites for its own work, by its own first two
authors, is titled "The Case Against Generation for Retrieval" and keeps the discriminative two-tower
architecture (MD-186). **Meta is not generating ads, and the clearest refutation of that reading is
Meta's own citation.**

### 1. Harvest

`lib/harvest.py daily` across all 12 roster channels. **0 new transcripts, 0 errors.** 8 skipped
short, 3 no subtitles, 0 out of window, 0 listing failures, 0 RSS fallbacks. Ran 14:56:33 to
14:58:03. Unextracted backlog 0.

### 2. Watchlist

| Source | Result |
|---|---|
| Meta Engineering (RSS) | HTTP 200, 9 in feed, **3 new**, build Mon 19 Oct 13:26 UTC |
| Meta Newsroom (RSS) | HTTP 200, 10 in feed, 0 new, build Thu 15 Oct 10:31 UTC |
| Google Ads & Commerce (RSS) | HTTP 200, 20 in feed, 0 new, build Thu 15 Oct 13:00 UTC |
| Google Ads Announcements | HTTP 200, **396 answer ids, 0 added, 0 removed** |
| arXiv cs.IR | HTTP 200, 60 in feed, 53 new, **3 passed the ad filter**, build Tue 20 Oct 04:02 UTC |
| TikTok SDK changelog | HTTP 200, unchanged at v0.1.8 |
| Meta for Business News, `?locale=en_US` | **1 added, 1 removed, and the added slug is genuinely new** |
| Meta for Business News, `?locale=en_GB` | 0 added, 0 removed against the 2026-10-19 first pass |
| TikTok Newsroom and for-Business blog | Geo-block, not retried, not an outage |

**The 1-in-1-out on the US shelf was NOT a rotation, and one lookup is what separated the two
cases.** `agencies-testing-incrementality`, dated 19 October 2026, arrived at slot 1 while
`meta-ai-for-small-businesses` dropped off the bottom. The standing rotating-module rule would read
that shape as a returning card. Checking the added slug against `slugs_seen_cumulative` showed it had
never appeared in either locale, so it was opened and read in full. **Method consequence: a
1-in-1-out diff on this source has two possible causes and the cumulative-slug check is what tells
them apart. It costs one lookup and it bought today's AT-131.**

**arXiv read after the rebuild, so the lag note does not apply.** Build timestamp Tue 20 Oct 04:02
UTC against a run at 09:26 UTC, which is a full post-rebuild read under the 2026-09-07 correction.
`skipDays` Saturday and Sunday confirmed present.

### 3. Claims

**6 new.** MD-184 (semantic token vocabulary replaces the per-item ID, built from the ad's text and
images, +0.35% jointly attributed), MD-185 (item-side cold start and cross-campaign transfer),
MD-186 (the "generative" reading rule), CR-287 (Kuaishou generated-creative A/B, and what its numbers
do not say), AT-131 (four Meta agency lift studies, eleven numbers, no footnote), AU-100 (Meta names
three scaling axes and parameter count is not one).

**12 merges.** MD-001, MD-022, MD-070, MD-120, MD-171, MD-177, MD-178, MD-179, CR-003, AU-084,
AU-085, AT-130.

**Three things worth separating from the haul.**

One, **MD-070 was deliberately NOT upgraded.** Meta's sentence is that the MODEL's representation of
an item carries across campaigns. MD-070 claims an ad object's delivery performance carries across
campaigns. Those are different objects and reading the first as proof of the second would have been a
mis-bank. Tier stays T3.

Two, **the footnote rule changed shape rather than being confirmed.** MD-184 is the first Meta ads
figure in months with a footnote, and it reads in full "Meta Internal Data, measured in February
2026". A data owner and a month, published eight months after measurement, with no population, no
window, no control and no sample. So the test is not whether a footnote exists, it is whether a
population and a counterfactual exist (merged into MD-171).

Three, **MAPS's headline numbers were nearly mis-read.** CTR +2.87%, CVR +2.74%, ARPU +9.85% are
measured against a *generative* baseline, not against retrieval from a pre-produced creative set. The
paper's motivation is generation-versus-retrieval and its measurement is not. Nothing in it quantifies
generated creative against a human-made library, and CR-287 says so explicitly.

### 4. Read and NOT banked

- **FLMNet (arXiv 2610.26143)**, self-ensemble distillation for single-tower CTR prediction. A
  genuine advertising paper, not a false positive: CTR prediction is the method throughout, five
  benchmarks against seventeen baselines. Discarded anyway because it is an architecture-internals
  result with no deployed system, no online test and nothing an advertiser touches. We bank claims,
  not papers.
- **"The Thin Orchestrator" (Meta Engineering, 19 Oct)**, keyword-scanned: one occurrence of
  "recommendation", describing agent tooling for onboarding data columns. No advertising content.
- **"Inside Prometheus" (Meta Engineering, 19 Oct)**, keyword-scanned: zero advertising terms, the
  only matches were "bidirectional" in NVLink bandwidth figures.

### 5. Gaps and open leads

- **The Meta Q2 2026 earnings call transcript is the link Meta's own post uses to define "Generative
  Recommenders", and it was not pulled today.** First time a financial disclosure has appeared as a
  source in this lane. Logged as a lead, not a claim.
- Three Meta-authored arXiv papers were read at abstract level only (2607.25346, 2602.07774,
  2607.10016). The first two carry internal production results with no figures attached, so the full
  papers may hold numbers the abstracts do not.
- **Still open from 2026-10-14 and not closed today:** nothing on file measures whether our own
  accounts' results differ by how platform-active the buyer is (MD-180). MD-185 adds a second version
  of the same gap, since Meta now says the benefit concentrates on tail inventory and large catalogues
  and our book is neither.
- **One cheap check created today:** AT-131 claims Meta ads move dealership search behaviour. We run
  two commercial truck dealerships and have never read a search-behaviour column on either.
"""


def main():
    hl = SCI / "Harvest Log.md"
    text = hl.read_text(encoding="utf-8")
    if f"\n## {TODAY}\n" in text:
        raise SystemExit("REFUSING: Harvest Log already has today's entry")
    if not text.endswith("\n"):
        text += "\n"
    hl.write_text(text + ENTRY, encoding="utf-8")
    print("Harvest Log appended")

    run = RUNS / f"{TODAY}-research-log.md"
    run.write_text(
        f"---\ntitle: \"Research run {TODAY}\"\ndate: {TODAY}\ntype: run-log\n---\n\n"
        f"# Advertising Science research run, {TODAY}\n\n"
        "Started 14:56 IST, worked through 15:35. **0 transcripts, 6 claims banked, 12 merges, law "
        "layer amended. Codex 1,379 to 1,385.** Tuesday, so the weekly (Monday) lane was not due; the "
        "2026-10-19 Monday run completed and wrote its log, so no catch-up was owed.\n"
        + ENTRY.split("### 1. Harvest", 1)[0].split("Codex 1,379 to 1,385.**", 1)[1].strip()
        + "\n\n### 1. Harvest" + ENTRY.split("### 1. Harvest", 1)[1]
        + "\n## Errors\n\n**None.** Harvest reported 0 errors across 12 channels; the watchlist "
          "checker reported 0 errors across 6 automated sources; both WebFetch reads of Meta for "
          "Business News returned content. No source failed and no lane was skipped for a technical "
          "reason.\n\n## Honesty note\n\nEvery claim banked today cites a source read in this run: "
          "the GenRecs Tokenization post and the agencies-testing-incrementality post were read in "
          "full, and the five arXiv items were read at abstract level, which each claim states. "
          "Nothing was banked from a title, a feed summary or a search result.\n",
        encoding="utf-8")
    print("run log written:", run.name)


if __name__ == "__main__":
    main()
