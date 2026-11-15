# -*- coding: utf-8 -*-
import io

P = (r"E:\claude code marketing skill\Obsidian God-level Marketing Vault"
     r"\God-level Marketing\wiki\science\Attribution & Incrementality.md")
t = io.open(P, encoding="utf-8").read()
assert "### AT-139" not in t, "already merged"

NEW = u"""### AT-139 \u00b7 Meta publishes the magnitude its whole calibration series left out: the median advertiser undervalues Meta by 31%, and at least a 1.45X multiplier was needed to reconcile rules-based attribution with lift, off 307 studies by 54 advertisers
Tier: T1 \u00b7 Status: active
Meta, "Building a suite of truth: A hybrid approach to measuring incrementality", the 20-page PDF at `facebook.com/business/f/1094917955782254`, downloaded and read in full 2026-11-15. This is the report named as a gap at [[Attribution & Incrementality#AT-138|AT-138]] and in the Harvest Log on 2026-11-13. It is **ungated**: the business URL 302s straight to a `scontent` PDF with no form and no login.

**The two numbers, verbatim.** "a meta analysis of calibration tests conducted on ads across Meta technologies showed that at the median advertisers undervalue Meta by 31% (meaning 31% of total incremental conversions caused by Meta are misattributed to other channels) when using rules-based attribution models, as compared with incrementality. **A multiplier of at least 1.45X was required to calibrate the results of the models to the true value driven by Meta.**" The footnote: "Based on 307 studies run by 54 advertisers between March 2022 and November 2024 across North America, EMEA, APAC and LATAM." The same 31% appears earlier in the report as "31% of incremental Meta conversions are misallocated to other channels based on non-incremental attribution models", on the same footnote.

**The two figures are one measurement stated twice, and seeing that stops anyone double-counting them.** If attribution reads 100 and lift reads 145, the misattributed share of the true total is 45/145 = 31.0%. So the 1.45X and the 31% are the same median expressed from the two ends. **They are not two independent findings and must never be cited as corroborating each other.**

**This is the number [[Attribution & Incrementality#AT-135|AT-135]] went looking for and did not find.** The October 2025 blog post teaches the multiplier method on a company Meta labels fictional, with a worked 1.5x that has no empirical basis stated anywhere on the page. The report supplies the real central tendency off 307 tests, and it lands at 1.45X, within 3% of the invented 1.5x. **The blog's teaching example sits on top of a measured median and never says so.**

**What the footnote still does not give, and the gaps are load-bearing.** A median with **no spread, no range, no interquartile band and no distribution**, over a 32-month window spanning the post-ATT recovery, with no per-vertical, per-objective or per-spend-tier breakdown, no minimum study size, no statement of how many of the 307 found no significant lift, and no definition of which rules-based models were in the comparison. "At least 1.45X" is a floor with no stated ceiling. 54 advertisers for 307 studies is 5.7 studies each, so the study count is not an advertiser count and the median is not a median over independent businesses. And Meta is measuring the undervaluation of Meta.

**The operating rule, and it is narrow.** This is the best single prior anyone has for how far a last-click count understates Meta. It is a reason to stop treating the platform number as a ceiling, and it is **not** a licence to multiply any client's reported conversions by 1.45. Our accounts are lead-gen, the 307 studies are conversion studies on advertisers large enough to run Conversion Lift, and [[Attribution & Incrementality#AT-074|AT-074]] is the standing reason to expect the sign and size of the error to be a property of the account. If it is ever quoted to a client, quote it as Meta's published median across 307 of its own studies and say the window.

**One mechanism sentence on the same page worth keeping.** Last-click "can over-index on bottom-funnel activities like search", which is the same effect [[Attribution & Incrementality#AT-137|AT-137]] turns into the branded-search-first test recommendation.
Sources: Meta, Building a suite of truth: A hybrid approach to measuring incrementality, PDF at facebook.com/business/f/1094917955782254, downloaded and read in full 2026-11-15; footnotes 1 and 7 (307 studies, 54 advertisers, 2022-03 to 2024-11, NA/EMEA/APAC/LATAM)
Last touched: 2026-11-15

### AT-140 \u00b7 Meta publishes a which-tool-when ladder tied to budget cadence, and a guard against acting on one study, which closes the "periodically" absence at AT-135
Tier: T1 \u00b7 Status: active
Same report as [[Attribution & Incrementality#AT-139|AT-139]], read in full 2026-11-15.

**The ladder, verbatim.** "When setting cross-publisher budgets (typically quarterly), we recommend advertisers use **single-cell** Conversion Lift tests to calibrate their model to ensure they're investing in the most incremental publishers." "When trying new campaign strategies across Meta technologies, we recommend advertisers use **multi-cell** Conversion Lift tests to validate performance." "In real time, we recommend advertisers use **incremental attribution**, our new incrementality reporting in Ads Manager for in-channel optimisation decisions."

**So each tool gets a decision and a frequency.** Single-cell for the quarterly cross-publisher allocation, multi-cell for strategy validation, the in-platform setting for day-to-day. [[Attribution & Incrementality#AT-135|AT-135]] records that the blog layer's entire cadence guidance was the word "periodically"; the report answers it with "typically quarterly" for the calibration test.

**The guard, and it is the sentence that matters most for how we would ever use a multiplier.** "When undertaking a calibration exercise it is advised to **run multiple tests to allow a pattern to emerge, as opposed to taking action on a single study.** Furthermore, it is recommended to run experiments across all channels where possible, to ensure all media is being evaluated through a consistent lens." **Meta's own doctrine therefore cautions against the one-test-one-multiplier move its own worked example at AT-135 demonstrates.** That bears directly on [[Attribution & Incrementality#AT-023|AT-023]], where the contested question is whether a static per-channel discount factor is safe: Meta now supplies both the method and a caution against applying it off a single read, while still saying nothing about decay or refresh interval.

**One advertiser's actual cadence, which is the only concrete test volume in the report.** Product Madness "opted to run **10 single-cell Conversion Lift studies each quarter**", across iOS and Android, on campaigns optimised for ROAS and purchase conversions using value optimisation and conversion optimisation.

**The experiment-volume figure, and it is the weakest number in the document.** "Businesses that conduct **15 or more experiments annually achieve 30% higher ad performance** compared to those that run no experiments", footnoted to Harvard Business Review, 2020, J. Runge, "Marketers underuse ad experiments. That's a big mistake." Third-party and not Meta, which is a point in its favour, and otherwise: six years old, pre-ATT, observational with no sample, no vertical and no definition of "ad performance", comparing 15-plus against **zero** experiments. A firm that runs 15 experiments a year differs from one that runs none in budget, headcount and analytical maturity, so the comparison cannot separate experimentation from everything that comes with it. **Never quote the 30% to a client.** Use the ladder and the multiple-tests guard, which cost nothing to follow.
Sources: Meta, Building a suite of truth, PDF, read in full 2026-11-15; HBR 2020 Runge cited as footnote 9 in that report
Last touched: 2026-11-15

### AT-141 \u00b7 Meta's one published effect size for incremental attribution is a 46% average performance lift, and the footnote restricts the sample to studies that already found significant incrementality
Tier: T1 for the sentence, T3 for the effect \u00b7 Status: active
Same report as [[Attribution & Incrementality#AT-139|AT-139]], read in full 2026-11-15.

**The claim, verbatim.** "Advertisers using incremental attribution saw an average **46% lift in performance** when their campaigns optimised for incremental conversions."

**The footnote is the finding, and it is a selection condition.** "Results based on **37 conversion lift studies (where statistically significant incrementality was detected in at least one cell)** run between July 2024 and October 2024. This set of studies compared campaign performance for **30 advertisers across 8 verticals** in North America, EMEA and APAC. These campaigns mainly target offsite conversion optimizations. This is provided to give you an idea of possible performance, but performance isn't guaranteed." **The denominator excludes every study that detected no significant lift.** So 46% is the average performance gain among campaigns already known to have a measurable incremental effect, which is the subset where an incrementality-trained optimiser has the most room to work. It is not the expected gain from switching on an arbitrary account, and Meta attaches its own non-guarantee.

**Why it still matters.** Every prior figure in this file for the incremental-attribution switch came from operators: Haus geo-holdouts at [[Attribution & Incrementality#AT-001|AT-001]] and [[Attribution & Incrementality#AT-002|AT-002]], Faris's whole-book move at [[Attribution & Incrementality#AT-004|AT-004]], the uncited "roughly 27%" recited from launch marketing at [[Attribution & Incrementality#AT-006|AT-006]]. **This is Meta's own number with a footnote, a window and a sample**, and it sits above Haus's up-to-38% for DTC-only brands, on a selected sample, over a four-month 2024 window.

**Do not collide this 46% with the other one.** [[Attribution & Incrementality#AT-085|AT-085]] records a 46% **cut in credited conversions** when one account switched its reporting column to incremental attribution. Same number, opposite direction, unrelated measurements: one is a reporting haircut on a single unnamed account, this is an average performance gain across 37 studies. A reader meeting both in one session will try to reconcile them. They do not reconcile and they do not need to.

**The case study attached, and it carries the only precision-adjacent figure in 20 pages.** Laura Geller, part of AS Beauty, ran a **three-cell Conversion Lift experiment**, one cell on business-as-usual click-based attribution and the others on incremental-attribution variants. The top cell delivered "**3.3X higher incremental return on ad spend (ROAS) than the business-as-usual cell with a 99.6% winning score**" and "**71% lower incremental cost-per-acquisition (CPA)**". Footnoted to Meta's own September 2024 case-study page. The "99.6% winning score" is a Meta-proprietary figure with **no definition given anywhere in the report** and is not a p-value or a confidence interval. Scott Kramer of AS Beauty states they have "since scaled nearly all of our campaigns to using incremental attribution as the primary optimization lever", which is a decision rather than a measurement. **The three-cell design is the transferable part**: run business-as-usual against the variant inside one lift study rather than switching the account and arguing about the before-and-after, which is also the circularity trap recorded at [[Attribution & Incrementality#AT-003|AT-003]].
Sources: Meta, Building a suite of truth, PDF, read in full 2026-11-15; footnotes 11 (37 studies, 30 advertisers, 8 verticals, 2024-07 to 2024-10) and 12 (Laura Geller, Meta for Business, 2024-09)
Last touched: 2026-11-15

### AT-142 \u00b7 Meta names bid strategy as a third calibration route, tailoring bids to a cohort's expected incremental lifetime value, and it is the only one of the three an account our size can run
Tier: T1 \u00b7 Status: active
Same report as [[Attribution & Incrementality#AT-139|AT-139]], read in full 2026-11-15. Meta lists three applications of calibration. Two are already banked: calibration of attribution at [[Attribution & Incrementality#AT-135|AT-135]], calibration of MMM at [[Attribution & Incrementality#AT-136|AT-136]]. The third is new here.

**Verbatim.** "**Calibration via bid strategy.** A common practice with direct response focused marketers is to tailor ad bids to the expected incremental lifetime value of the channel or cohort in question; e.g., branded vs. non-branded search, or social prospecting vs. social retargeting."

**Why this one is worth more to us than the other two.** It needs no lift test, no MMM and no holdout. It needs a view on which cohorts are less incremental and a willingness to bid them differently, which is a bid-cap decision we already make. It is also the mechanism behind two positions this file holds from the practitioner side: the retargeting and dynamic-product-ad haircut at [[Attribution & Incrementality#AT-040|AT-040]], where surface return reads 5-10x and corrects to about 2x, and the existing-customer spend argument at [[Auction Mechanics & Bidding#AU-059|AU-059]]. **Meta is describing, as common practice, bidding a retargeting cohort at the value you believe it adds rather than the value the platform credits it.**

**What Meta does not give.** No method for estimating a cohort's incremental lifetime value, no worked example, no figure, and no statement of how far apart the bids should sit. Meta names the practice and stops. So the mechanism is T1 and any specific bid ratio stays a judgment.

**The limit for our own book.** Our clients are lead-gen with no retargeting-versus-prospecting value split we can measure, and no lifetime-value figure on most accounts. Nearest usable form: when a prospecting and a retargeting ad set compete for the same budget, do not let the credited return decide the allocation, which is the rule [[Attribution & Incrementality#AT-040|AT-040]] already states as "never consolidate a DPA ad set into the same CBO as prospecting ads".
Sources: Meta, Building a suite of truth, PDF, read in full 2026-11-15
Last touched: 2026-11-15

### AT-143 \u00b7 Conversion Lift now runs off the Conversions API, which Meta names as its recommended source, and is self-serve in Experiments for "all qualified advertisers" with no definition of qualified
Tier: T1 \u00b7 Status: active
Same report as [[Attribution & Incrementality#AT-139|AT-139]], read in full 2026-11-15.

**Verbatim.** "Conversion Lift can now be powered by an expanded set of data sources, including the **Conversions API (recommended)**, the Meta Pixel, and App Events API. And we've made Conversion Lift available for **self-serve for all qualified advertisers in Experiments.**"

**Both halves change whether a lift test is reachable for us, which is why this is banked as product fact and not as doctrine.** Every Conversion Lift discussion in this file assumes a test brokered by a Meta Marketing Science team, which is how Product Madness and H&M ran theirs in the same report. Self-serve in Experiments is a different access model. And CAPI being the **recommended** source rather than the pixel matters directly: our client accounts send server-side events through the CRM, so the data source Meta prefers is the one we already run.

**The gating word is undefined.** "All qualified advertisers" carries no spend floor, no conversion-volume floor, no market list and no account-age condition anywhere in the report. [[Attribution & Incrementality#AT-125|AT-125]] holds Meta's only published duration guidance, 2 to 3 weeks at holiday conversion volume against 6 or more weeks in a quiet quarter, and that is a volume statement rather than an eligibility rule. **So whether any of our accounts can open a self-serve Conversion Lift is a question only the Experiments tab can answer, and nobody has opened it.** Logged as the cheapest unknown in this topic: it is a look, not a test.

**One caution on the CAPI line.** A CRM Conversions API echo is already known to double-count people on our accounts, recorded for Phoenix Truxx and SJR in September 2026. A lift study powered by a feed that counts some people twice inherits that defect, so the event feed needs checking before any holdout is read.
Sources: Meta, Building a suite of truth, PDF, read in full 2026-11-15
Last touched: 2026-11-15

### AT-144 \u00b7 The report named as the home of Meta's lift-test methodology contains no holdout size, no minimum detectable effect and no confidence interval, so Meta publishes nothing an advertiser could size a Conversion Lift test from
Tier: T1 \u00b7 Status: active
Recorded as a negative so nobody re-searches this document. Same report as [[Attribution & Incrementality#AT-139|AT-139]], all 20 pages read 2026-11-15.

**The gap this was meant to close.** [[Attribution & Incrementality#AT-135|AT-135]] records that the attribution-calibration post carries zero confidence intervals, no holdout size, no minimum conversion volume and no minimum detectable effect, and [[Attribution & Incrementality#AT-138|AT-138]] points at this report as the only plausible home for them. The Harvest Log called it the cheapest high-value item on the board. It was read today and **the parameters are not in it.**

**What is absent, checked across all 20 pages.** No holdout percentage or holdout size. No minimum detectable effect. No statistical power figure. No confidence interval on any number in the document. No minimum conversion volume or spend floor for a test. No geo-test design detail, and geo testing appears only as a two-word label on one diagram. No formula, no code, no model specification. The word "prior" never appears with a distribution attached, consistent with [[Attribution & Incrementality#AT-136|AT-136]].

**The one precision-adjacent figure, and it is not a statistic.** Laura Geller's "99.6% winning score" at [[Attribution & Incrementality#AT-141|AT-141]], a Meta-proprietary score the report never defines.

**Scope the absence correctly, because duration IS published elsewhere.** [[Attribution & Incrementality#AT-125|AT-125]] holds a real Meta duration figure, 2 to 3 weeks at holiday volume against 6 or more weeks in a quiet quarter, from a separate holiday post. So the honest statement is that **across the four-part calibration series and this 20-page methodology report, Meta publishes one duration heuristic tied to conversion volume and no other test-design parameter at all.**

**The consequence, and it is operational.** A practitioner cannot size a Conversion Lift test from Meta's public material. The holdout fraction, the power and the stopping rule all sit inside the Experiments tool or inside a Marketing Science conversation. **That makes the self-serve access question at [[Attribution & Incrementality#AT-143|AT-143]] the only route to the numbers**, and it means any proposal we write for a client lift test has to size the test from our own event volume rather than from anything Meta has published.

**What the report is instead.** A 20-page doctrine and case-study document: the incrementality ladder, the hybrid-measurement argument, the three core competencies of calibration, regular experimentation and measurement-informed ad delivery, and four branded case studies. Useful for vocabulary and for the ladder. Useless for designing a test.
Sources: Meta, Building a suite of truth, PDF, 20 pages, read in full 2026-11-15
Last touched: 2026-11-15

### AT-145 \u00b7 Meta's blog layer attaches the same Kantar percentage to a different proposition than Meta's own report does, so a Meta-recited survey figure is not safe to carry without the primary wording
Tier: T1 \u00b7 Status: active
A method claim about reading Meta's own citations, found by holding the report at [[Attribution & Incrementality#AT-139|AT-139]] against the blog post at [[Attribution & Incrementality#AT-136|AT-136]].

**The report's four figures, all footnoted to one survey:** "Kantar, May 2025, n=1,935 decision makers across regions, industries and company sizes", disclosed in the report body as commissioned by Meta.

| Figure | What the REPORT says it measures |
|---|---|
| 3.8 | "on average, advertisers have 3.8 measurement solutions in their toolkit today" |
| 55% | "of advertisers have experienced contradicting results across different solutions" |
| 51% | "When faced with inconsistencies, 51% of advertisers tend to **default to the solution that holds the most credibility within their organisation**" |
| 53% | "of advertisers leverage calibration as a means to reconcile contradictory results" |

**The discrepancy.** The MMM blog post banked at AT-136 prints the same 51% as "**51% of marketers using MMM alongside other tools**", with no footnote at all. That is a different proposition off the same survey: one is a tool count, the other is a behaviour when results conflict. The 55% survives the comparison roughly intact, "frequently encounter conflicting results" against "have experienced contradicting results". **One of the two 51% descriptions is wrong, and the report is the one carrying the footnote.**

**Two corrections to earlier handling, both made here rather than hidden.** On 2026-11-13 the 51% and 55% were **discarded** on the stated ground that they carried no footnote at all. That was correct about the blog post and wrong as a judgment about the figures: they come from a disclosed survey with an n and a date, and the report cites it properly. So the figures are usable with the report's wording and the Meta-commissioned caveat attached. Second, AT-135 records the blog's "nearly four different measurement solutions on average"; the report's primary figure is **3.8**, which is consistent.

**The operating rule, and it generalises past this survey.** When a Meta blog post recites a number from a study, the sentence attached to it in the blog is not reliable evidence of what the study measured. Find the report or the footnote before carrying the figure, and quote the primary wording. **This is the second defect of this shape in this file**, after the footnote question examined at [[Attribution & Incrementality#AT-120|AT-120]], and the first one where the blog and the primary document can be read side by side and demonstrably disagree.
Sources: Meta, Building a suite of truth, PDF, read in full 2026-11-15, footnotes 2, 4 and 6 (Kantar, May 2025, n=1,935); held against Meta for Business, Calibrating Marketing Mix Modeling with Incrementality Experiments, 2025-10-29
Last touched: 2026-11-15
"""

idx = t.index("### AT-138 ")
nxt = t.find("\n### ", idx + 5)
if nxt == -1:
    t = t.rstrip("\n") + "\n\n" + NEW
else:
    t = t[:nxt + 1] + NEW + "\n" + t[nxt + 1:]

io.open(P, "w", encoding="utf-8").write(t)
print("inserted AT-139..AT-145, new length", len(t))
