---
title: "Scaling Models"
type: codex-topic
claim_prefix: SC
created: 2026-08-18
tags: [advertising-science, codex]
---

# Scaling Models

How spend scales without efficiency collapse: budget moves, consolidation, structure, cost controls.

Part of the [[00-Codex|Advertising Science Codex]]. Claims follow the tier system (T1 docs, T2 shown test, T3 practitioner, T4 theory).

## Claims

## When and how much to raise budget

### SC-001 · How big a budget step is safe is contested: prescriptions range from 5% or less to 20% per day to "the 20% rule is folklore"
Tier: T3 · Status: contested
Professor Charley T says scale at the campaign level by 5% or less, and only when 7-day performance is about 10% better than target CPA (example: target CPA $50, actual $45), so even zero incremental conversions keep you under target. Sam Piliero scales the move to the margin above target: 5-10% just above goal (2.1 vs 2.0), 20-30% comfortably above (2.5 vs 2.0), 50%+ when far exceeding (3-4x a 2.0 target), and already-scaled accounts should move in absolute increments of $500-$2,000, which may only be 5-15% of budget. Nick Theriot moves CBO budgets in 20% steps up or down gated by KPI, and when a client is under KPI he bumps 20% per day; he showed a client launched March 27 at $56 cost per purchase on $3,900 day spend falling to $33 CPP as new ad sets took spend, then scaling proceeded. Ben Heath rejects any fixed 20% rule as not nuanced: tripling $3/day to $10/day is fine, but at $100k/month even $120k in one step is a reasonably large increase and $300k would almost certainly kill the results, because the good-prospect pool is already saturated. Blue Sense Digital goes furthest: no Meta documentation supports the 20% rule, and his agency raises budgets by more than 20% routinely with no issue.

Platform split added 2026-08-18, which partly dissolves the disagreement. Blue Sense Digital says the 20% rule is real and it is a Google rule: "the rule that you've always heard, increase budgets in 20% increments. Uh, it's real. It applies on Google. On Meta, Tik Tok, you have a bit more flexibility." Google is the more stable platform, converts more consistently, and rewards slow methodical changes, so doubling a budget overnight or halving a target CPA overnight is a bad idea there. The move is asymmetric: bringing Google budgets down fast, including halving them, produces little instability or performance drop-off. Every prescription above is Meta-centric, so read the 5%-to-folklore spread as a Meta argument and the 20% step as a Google constraint. Practitioner observation across an agency book, no test data shown.

Charley T's own number as of Feb 2026 is +5% three times a week, or a flat +$10/day on an established campaign, both conditional on the business absorbing the volume. His arithmetic that 5% x3/week doubles the budget monthly is wrong: 1.05^12 = 1.80, so it is about 1.8x. The +$10/day version checks out (a $400/day campaign reaches $4,050/day in 365 days).
Sources: Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10; Professor Charley T, The NEW SIMPLE EASY WAY to Scale BIG with Meta Ads, 2026-02-07; Sam Piliero, Easiest Way to Scale Facebook Ads in 2026, 2026-08-03; Nick Theriot, I Spend $100k/Day On Facebook Ads, 2026-08-03; Nick Theriot, My Full Process For Scaling Facebook Ad Clients In 2026, 2026-07-20; Ben Heath, $100 vs $100,000 Facebook Ads Strategy, 2026-08-12; Blue Sense Digital, How The Meta Ads Algorithm Works in 2026, 2026-07-28; Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, The Only Google Ads Strategy You Need for 2026, 2026-06-22
Last touched: 2026-08-18

### SC-002 · A ROAS dip after a budget raise is time-to-purchase lag from newly reached upper-funnel people, not a learning reset
Tier: T3 · Status: active
Multiple independent sources give the same mechanism: Meta serves the cheapest, most-likely buyers first, so added impressions go to upper-funnel people who need days to convert. Sam Piliero's illustrative averages: bottom-of-funnel converts in ~0 days, middle-of-funnel 1-2 days, top-of-funnel 5-10 days, so moving $1,000 to $1,500/day shows an immediate ROAS dip that partially recovers as the new cohort matures. Blue Sense Digital makes the same argument: tripling budget today does not triple revenue today because newly reached audiences need multiple exposures over their time-to-purchase window, and people misread the lag as the algorithm punishing the change. The correct response is patience, not resetting the account. Professor Charley T extends the same mechanism from budget raises to campaign launch: a new one-campaign build reliably performs well for about three days and then degrades, because the machine harvests existing bottom-funnel demand first and then pushes delivery up-funnel. His prescription is to let it ride, and "if you can't afford that struggle, work on the business before you run ads." He adds that high CPMs at launch on this structure are normal and come down. All asserted, no shown curve.
Sources: Sam Piliero, Easiest Way to Scale Facebook Ads in 2026, 2026-08-03; Sam Piliero, Do THIS and the Meta Andromeda Algorithm Will LOVE You!, 2026-08-14; Blue Sense Digital, How The Meta Ads Algorithm Works in 2026, 2026-07-28; Professor Charley T, The BEST AD ON META after Andromeda, 2026-01-10
Last touched: 2026-08-18

### SC-003 · Scale only when target is beaten across stacked lookbacks: 30-day, 14-day, 7-day, 3-day, and yesterday, weighting recent windows most
Tier: T3 · Status: active
A 30-day view can read 8.46 against an 8.0 target while the 14-day is 7.3 and the 7-day 6.94; that regression means do not scale despite the healthy monthly number. Only when all windows, especially the most recent, sit above the goal is the account ready for a budget move. Demonstrated on a live account's real numbers but as a decision heuristic, not a validated backtest.
Sources: Sam Piliero, Easiest Way to Scale Facebook Ads in 2026, 2026-08-03
Last touched: 2026-08-18

### SC-004 · Account diagnostic is two questions: if you can spend more profitably, touch nothing and scale; if not, test one new 322 against the single worst-performing ring
Tier: T3 · Status: active
When the answer to "can I spend more money and stay profitable" is yes, launching new ads or restructuring is the single worst move. When no, identify the prospecting ring or ad set consuming disproportionate spend with the worst results relative to target, and build new 322 ads designed to do that ring's job better, run in the test ad sets. One change, one test; if the new 322 earns spend away from the underperformer it is doing the job better.

The metric that answers question one is spend concentration inside the flexible ad, and he states it as the only KPI that matters: "There is no rush to pull post IDs. You do not need to get winning ads. You need to be good enough to increase your budget. That's it." Spend allocation is the system reporting what it believes in, so a 322 that earns spend and lets you raise budget is finished work. Hunting the winning permutation inside it, or interrupting learning to extract a post ID, is named as one of the most common mistakes. Weekly review collapses to one question: can I increase the budget, yes or no. Asserted from managing "well over a million dollars a week", no data shown.
Sources: Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10; Professor Charley T, The BEST AD ON META after Andromeda, 2026-01-10
Last touched: 2026-08-18

### SC-005 · Break results down by attribution setting before any scale or pause decision; scaling view-through-inflated campaigns fails
Tier: T2 · Status: active
Advertisers who take standard-attribution results at face value scale campaigns propped up by non-incremental view-through and engage-through conversions, then are confused when scaling collapses, or they pause a genuinely better ad because its comparator is view-through-inflated. Before any scale/pause decision, check how many conversions Meta itself flags as incremental via compare attribution settings.

Documented case, SHOWN as a per-campaign attribution comparison plus a CAC-over-time chart and a gross-profit-on-first-purchase chart. An agency pushed 60-70% of account-wide daily budget into the campaign with the best default-attribution ROAS at 2.21. On 7-day click that campaign was the worst in the account. It was a sales campaign with no audience exclusions, so it retargeted warm and existing customers and collected non-incremental conversions; it looked best precisely because it was least incremental. Result was the highest blended CAC in the brand's history and a negative first-time-customer P&L. Operator move: run the attribution comparison per campaign before reallocating, not at account level.
Sources: Jon Loomer, Most Advertisers Should Only Use Incremental Attribution, 2026-07-29; Blue Sense Digital, How To Structure Your Meta Ads for Profit (Free Live Webinar), 2025-02-19
Last touched: 2026-08-18

### SC-006 · Scale an existing entity in place rather than duplicating; the duplicate-at-higher-budget trick is only a temporary bug workaround, and never run replicas simultaneously
Tier: T3 · Status: active
In-place scaling keeps accrued learning, so results are better; duplicating on every increase produces dozens or hundreds of entities and an unmanageable account; and duplicates can reshuffle delivery, for example an ad set where 80% of spend went to 2 of 20 ads can, after duplication, give those two proven winners no spend at all. During a 2026 delivery bug, the fix was duplicating the winning campaign/ad set directly at the higher budget and turning the original OFF; running the original alongside the duplicate, or 8 replica ad sets, is data fragmentation and a disaster. Explicitly framed as a temporary fix, not the normal scaling method.

Two more sources name the same anti-pattern, and both call it the most common structural mistake they see: pausing a winner in order to relaunch it inside a scaling campaign. Blue Sense Digital: "if something works, don't touch it," and the two costs are a learning-phase reset and, for operators who do not carry the post ID, the loss of all accumulated social proof on the creative. The rule extends to adding creative: injecting new ads into a performing ad set disrupts the sequencing Meta has learned there, so new creative for a winning concept goes into a NEW ad set named for the same concept, while an underperforming ad set can be edited freely because its sequencing is not working anyway. At KPI, raise budget and touch nothing else. See also [[Scaling Models#SC-028|SC-028]] for the scaling-campaign move done correctly, by post ID, with the original left running.
Sources: Ben Heath, Urgent Message For Facebook Advertisers!, 2026-08-03; Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, How To Structure Your Meta Ads for Profit (Free Live Webinar), 2025-02-19
Last touched: 2026-08-18

### SC-044 · A concept test needs 3x target CPA of spend before a verdict, 5x preferred, run over about a week
Tier: T3 · Status: active
Multiply target CPA by three; that is the spend floor before deciding on or off. At 3x, three or more conversions is a pass, two is a yellow light worth another increment, zero or one is a kill. He prefers 5x because early spend is the algorithm learning who to target and efficiency improves after that, and at 5x the decision is binary with no yellow light. The one-week duration floor exists for two separate reasons: launching on a strong or weak weekday biases the read, and buyers typically need 2-4 impressions across 3-4 days, so a one-day test kills top-of-funnel openers whose conversions land later on other creative. Adjust to 3-4 days for large stable businesses and 10-14 days for small budgets with long purchase cycles. Asserted, no shown test.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15
Last touched: 2026-08-18

### SC-045 · Percentage of spend equals percentage of change equals percentage of confidence, so size every account action by the entity's spend share
Tier: T4 · Status: active
"If an ad spends 1% of your budget, turning it off is a 1% change with 99% confidence. But if an ad spends 50% of your budget, turning that off is a 50% change with 50% confidence and could very well reset everything." This puts pausing and budget moves on one scale and generalises [[Scaling Models#SC-008|SC-008]] from rank (never kill the top two spenders) to spend share (never make a change larger than your confidence). He restates that a +/-20% budget change will almost certainly disrupt learning. The operating instruction is to make the smallest move with the highest confidence of a net positive impact, then measure, then repeat: audit, plan, optimize, measure, repeat. Reasoning only, no test.
Sources: Professor Charley T, The NEW BEST Meta Ads Andromeda Course to Scale in 2026, 2026-01-24
Last touched: 2026-08-18

### SC-046 · Reallocate asymmetrically with automated rules: cut the liability by ~$100/day while adding only ~$25/day to the winner
Tier: T3 · Status: active
Reported case from a coaching member: pulling $50-100/day off one campaign and adding $25-35/day to two others meant $9,000 less spend in a week, two fewer sales out of well over a hundred (under 2%), and cost per result improved about 20%. The mechanism claimed is that the above-average-cost campaign shrinks off the balance sheet within a week with no manual work, while the good campaign grows slowly enough not to destabilise. Named trap, the "siren song": as budget is pulled back the losing campaign's own metrics improve, which tempts the operator to stop pulling. Asserted from a coaching call, nothing shown. Note the direct tension with [[Scaling Models#SC-008|SC-008]] if the liability is also a top spender.
Sources: Professor Charley T, The NEW SIMPLE EASY WAY to Scale BIG with Meta Ads, 2026-02-07
Last touched: 2026-08-18

### SC-047 · Cap hands-on Ads Manager work at 90 minutes a week; scarcity forces the operator to only remove large liabilities and raise budget
Tier: T3 · Status: active
Literal timer on the phone. The claim is that 90 minutes a week is enough to take an account from $20/day to $1,000/day, because the constraint forces prioritisation: with that little time you only kill the ads taking heavy spend at unacceptable results and you raise budget, which is the whole job. Creative production, analysis and copy happen outside the 90 minutes; the cap applies only to changes made inside Ads Manager. Supporting case, asserted: a clothing brand went from $400/week to $3,000/day with 10 ads launched in a month, 90 minutes a week of management, repeat purchase rate from ~20% to ~40%, and AOV nearly doubled. Record the caveat: his own two streams state the same engagement inconsistently, once as "400 a week to 3,000 a day" and once as "400 a day to a little over 3,000 in about 45 days," and the engagement was a flat fee plus performance incentive. Nothing was shown on either stream.
Sources: Professor Charley T, How to CRUSH Facebook Ads with a Low Budget, 2026-02-28; Professor Charley T, The NEW SIMPLE EASY WAY to Scale BIG with Meta Ads, 2026-02-07
Last touched: 2026-08-18

### SC-048 · Run a weekly OS: launch creative on a fixed day, pause ads on a fixed day, change budgets on a fixed day
Tier: T3 · Status: active
Named alongside consolidation as one of the two changes that would improve most accounts. Two stated benefits: better decisions, because a fixed cadence removes emotional reactivity to daily numbers, and cleaner data, because a change is attributable to a known day instead of being smeared across continuous fiddling. This is the media-buying complement to a fixed-cadence creative pipeline. No test data; presented as standard practice across the agency's book.
Sources: Andrew Faris, Your Meta Ads Account Has Too Many Campaigns: Here's Why And What To Do, 2026-05-12
Last touched: 2026-08-18

## Kill and pause decisions

### SC-007 · Whether manual ad on/off decisions matter at all is contested: CTC's study found no discernible impact, while Nick Theriot kills ads above his top spenders' NCPA
Tier: T2 · Status: contested
CTC side (via Andrew Faris and Taylor Holiday, on billions of dollars of managed spend): manually turning ads off or on made things neither better nor worse ("you think you're doing something but you are doing nothing"), and their old internal stop-loss rule, auto-kill at 5x CPA with zero purchases, was back-tested against outcomes after threshold-crossing and found non-beneficial; the "$20k spent at zero sales" horror story fails because there is no counterfactual. Nick Theriot side: benchmark every ad's NCPA against the account's highest-spending ads and turn off anything above that number; on a real account ($80k/7-day sales, $4,000/day CBO, $50 NCPA target, campaign averaging $65 NCPA) the top two spenders sat at ~$69 NCPA and ads at $76/$80/$88 got turned off, running on last-7-days attribution data. Both positions carry shown data; they have not been tested against each other.
Sources: Andrew Faris, Do Cost Caps Work? Taylor Holiday Brings $200M Of Data, 2026-08-06; Nick Theriot, When to Turn Facebook Ads Off in 2026, 2026-08-07
Last touched: 2026-08-18

### SC-008 · Never turn off the two highest-spending ads in a CBO; 9 times out of 10 it hurts overall account performance
Tier: T3 · Status: active
Even when a top spender's CPA runs above target, killing it degrades overall performance in roughly 9 of 10 cases in his accounts, because high spenders anchor the CBO's delivery. If a top spender's CPA turns genuinely bad, run a reversible test: turn it off for 2-3 days, watch overall performance, and turn it back on if performance worsens.
Sources: Nick Theriot, When to Turn Facebook Ads Off in 2026, 2026-08-07
Last touched: 2026-08-18

### SC-009 · Audit low-spend zero-purchase ads on lifetime windows, not 7 days
Tier: T3 · Status: active
Ads spending a little each week never look bad in a 7-day view. Periodically switch the timeframe to 30 days or lifetime/maximum; ads with a couple hundred dollars of cumulative spend and zero purchases get turned off. This catches slow budget leaks a rolling 7-day report structurally hides.
Sources: Nick Theriot, When to Turn Facebook Ads Off in 2026, 2026-08-07
Last touched: 2026-08-18

### SC-010 · Same-day kill exception: a new ad taking overall spend at ~3x target CPA and dragging account performance more than 50% gets turned off within the day
Tier: T3 · Status: active
The 7-day rule has one override: a newly launched ad that immediately dominates campaign spend at roughly triple the target CPA and causes a greater-than-50% decrease in overall performance is turned off within a day, sometimes the same day. Otherwise new ads get their full window. He also keeps a daily change log (Google Sheet) of every account action to correlate adjustments with performance shifts.
Sources: Nick Theriot, When to Turn Facebook Ads Off in 2026, 2026-08-07
Last touched: 2026-08-18

### SC-011 · Make kill/scale decisions at the ad-set level, not the ad level: at KPI increase spend, off KPI decrease ~20% and wait days before touching individual ads
Tier: T2 · Status: active
Because ads in one ad set sequence together, single-ad metrics mislead. Protocol: ad set at KPI, raise budget; off KPI, cut budget ~20% and give it a couple more days; only then kill the top spend-soaker and force spend to the rest, and usually the better move is launching new ads instead. In his live retargeting ad set one ad booked a call at $8 and another at $118 and both stay on because ad-set cost per call is good.
Sources: Dr. Matt Shiver, How the Facebook Ads Algorithm Actually Works, 2026-07-21; Dr. Matt Shiver, The 'Right Way' to Run Facebook Retargeting Ads in 2026, 2026-07-28
Last touched: 2026-08-18

### SC-012 · The doom cycle / death loop of killing ads and launching replacements is the most common reason accounts stop scaling
Tier: T2 · Status: active
Two independent sources describe the same failure. Professor Charley T (attributed to $1B+ of managed spend): operators turn off ads that appear to be dying, but those are often the higher-funnel ads that were building the audience making everything else work; each replacement launch is tested again at the bottom of the funnel, so spend concentrates lower and lower chasing less incremental performance. Sam Piliero shows an account audited that week: $24,000 spent at 1.4 ROAS against a 2.0 target, with 1,060 campaigns launched over its lifetime and dozens active, budget spread causing the collapse. The fix is a stable structure that adds ad sets inside one prospecting campaign instead of new campaigns.
Sources: Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10; Sam Piliero, Easiest Way to Scale Facebook Ads in 2026, 2026-08-03
Last touched: 2026-08-18

### SC-013 · Handle fatigued ad sets with spend maximums instead of pausing, because CBO redistribution after a pause is rarely clean
Tier: T3 · Status: active
A fatiguing ad set normally forces an ultimatum: keep it active and lose money, or pause it and hope the budget redistributes well, which rarely happens evenly. Setting a spend maximum on the fatigued ad set throttles it while letting the rest of the CBO keep its learned distribution.
Sources: Sam Piliero, Do THIS and the Meta Andromeda Algorithm Will LOVE You!, 2026-08-14
Last touched: 2026-08-18

### SC-049 · Two-axis kill rule: turn an ad off only when CPA is above the account average AND gross profit per transaction is below average
Tier: T3 · Status: active
Both conditions, not either. This survives the objection banked in [[Scaling Models#SC-008|SC-008]] and MD-010: a top-spending demand driver legitimately runs an above-average CPA, and it is only a liability if its profit per transaction is also below average. He states it in two separate streams as "the simplest way to start" on a messy account. The prerequisite is GPT per ad, which most accounts cannot compute without an order-level data source. He is productising the same logic into a quadrant tool (waster / scaler / qualifier) with a claimed ~95% accuracy; treat that number as marketing for his own $100/month SaaS, not evidence. Rule itself asserted, no test shown.
Sources: Professor Charley T, The NEW SIMPLE EASY WAY to Scale BIG with Meta Ads, 2026-02-07
Last touched: 2026-08-18

### SC-050 · Case: cutting a campaign from 89 ads to 4 and launching nothing new for six weeks 10x'd spend in 90 days while platform ROAS fell from 2.9-3.8 to under 2 and weekly gross profit per transaction held at 136/133/137/124
Tier: T2 · Status: active
SHOWN, 12 weeks of weekly rows in the live account. The weeks start in April, so this is a summer period and not a Black Friday tailwind. Scale came entirely from subtraction: no new creative, no budget-rule changes, ad count down from 89 to 4, and no new ad launched in over a month and a half. The campaign is now set to spend over $100,000 a week on its own. The load-bearing observation is the variance split. Cost per acquisition swung hard week to week (158, then 193, then under 100) while gross profit per transaction barely moved (136, 133, 137, 124). That is the argument for managing on profit per transaction rather than CPA, and the reason the ROAS decline was not a problem: the platform number fell while the profit per order that funds the business did not. He states the corollary that once an account is scaling smoothly, launching new ads is the worst thing you can do. This is the strongest single counter-case in the codex to high-volume creative doctrine, and it is one campaign in one account, so read it as an existence proof rather than a general law.
Sources: Professor Charley T, The NEW BEST Meta Ads Andromeda Course to Scale in 2026, 2026-01-24
Last touched: 2026-08-18

### SC-051 · Spend concentration is a risk metric in its own right: three ads holding $1,000/day at 4x is strictly better than one ad holding $1,000/day at 4x
Tier: T3 · Status: active
Same efficiency, same spend, different survival odds. Blue Sense Digital cites 8-10 clients over six years arriving at his agency 40% down year on year in new-customer acquisition, every one of them built on 2-3 creatives that had held roughly $1M in spend and then fatigued together; he now refuses those accounts because the fix needed to happen 6-8 months earlier. Every creative has a maximum spend threshold and will fatigue, so the portfolio shape (how many ads hold how much spend) is the health metric, not blended ROAS. Andrew Faris reports the same target state from the other direction: a breakout ad fell from ~50% of account spend to the number three ad at ~5% within two months while the account grew, and the end state he wants is "bunches of ads all spending a few grand a day", winner stacked on winner, not one dominant ad. Faris's window also included a budget raise and added inventory, so the ad-count shift is correlation. Both accounts described, neither shown. Note the direct tension with [[Scaling Models#SC-058|SC-058]], where CBO's Pareto compounding into ~4% of ads is treated as the efficiency-maximising choice: concentration is what buys the ROI and what carries the risk.
Sources: Blue Sense Digital, Meta Ads Creative Strategy in 2026: The Full System, 2026-05-11; Andrew Faris, From A 65% Decline To All-Time Revenue Profit Highs With Richie Mashiko, 2026-04-27
Last touched: 2026-08-18

## Consolidation vs segmentation

### SC-014 · Campaign/ad-set structure exists for data siloing; hyper-segmentation fragments conversion data and hurts performance on Meta, Google and TikTok alike
Tier: T3 · Status: active
Campaigns learn in isolation with their own models; segmentation is the advertiser's signal that audiences are genuinely different (e.g. ice baths vs saunas sub-brands). Most accounts over-segment for reporting comfort, spreading conversions too thin per silo. Consolidating structure pools conversion data and improves performance; segment only when the audiences truly differ.

The siloing is not uniform by level, which is the operationally important part. Conversion data is siloed hardest at the campaign level and shared far more freely at the ad-set level, so ad-set segmentation swings efficiency only 5-10% while campaign segmentation fragments the signal outright: four campaigns on 100 conversions/month leaves each with 25 and guarantees small-sample bias. Stated inflection threshold: accounts start performing meaningfully better once they clear 100-200 conversions per month. Operator rule that falls out of it, consolidate aggressively at campaign level and segment relatively freely at ad-set level. Professor Charley T states a stronger version, that campaigns do not merely dilute each other but actively cannibalise: "campaigns don't talk to each other. So, if you're running multiple campaigns or multiple adsets within an ADL, which is basically just multiple campaigns in an ad account, those are all combative." That version is reasoning only, and it should be scoped to undifferentiated duplication, because the same speaker deliberately runs multiple differentiated ad sets in [[Scaling Models#SC-021|SC-021]] and [[Scaling Models#SC-022|SC-022]].
Sources: Blue Sense Digital, How The Meta Ads Algorithm Works in 2026, 2026-07-28; Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01; Professor Charley T, The BEST Facebook Ads Strategy for 2026 Post Andromeda, 2025-12-27
Last touched: 2026-08-18

### SC-015 · Structure follows conversion volume: consolidate to one campaign and one ad set at low volume, diversify into themed ad sets of 5-10 ads at high volume
Tier: T3 · Status: active
Shiver's thresholds across two videos: under 3 conversion events/day everything consolidates into a single ad set of about 5 creatives with new hypotheses launched inside it; at 3-10 schedules/day, new ads go into separate testing ad sets ($100-200/day, roughly 1x cost per call) and only winners move into the scaling ad set ($300-500/day); above 10 schedules/day run several ad sets around $500 each, themed by pain point, angle, or creative style (5-10 statics, 5-10 videos, 5-10 b-roll), because one big ad set at scale produces volatile swings and a single tanking ad set then takes the whole account with it. Funnel-specific consolidation thresholds: webinar funnels ~20 conversions/day, VSL/application funnels ~5-10/day. He abandoned recommending the one-campaign method universally after finding it failed for lower-volume accounts.

Restated 2026-08-18 with the same three tiers and four additions. First, the reason the low-volume tier must consolidate: an isolated test ad set that produces no pixel fires yields no significant result, so there is nothing to read and the test was not really run. He concedes this tier gets messy and that viewers will object that results tank when new ads go into a working ad set, and holds the position anyway on the signal argument. Second, his ideal tier is now stated as ABO with about five ad sets, one hypothesis per ad set, at 3-5 booked calls per day per ad set, with winners iterated into a fresh ad set carrying the next hypothesis; the risk rationale is explicit, that several ad sets mean one bad day in one ad set does not zero the account. Third, a self-caveat on the middle tier: an ad that wins inside a testing ad set sometimes does not perform when moved into the scaling ad set, so the promote-the-winner move is not bulletproof. Fourth, one ad per ad set is rejected except as a deliberate short forced test, with at least five ads per ad set preferred on the grounds that learning happens at the ad set level, CPMs stay lower, and ads work as a unit. He notes he rewrites this structure recommendation roughly every three to six months as accounts change, which is a reason to date any structure rule before applying it.

Two additions from other speakers. First, a usable definition of "low volume" that is not a dollar figure. Professor Charley T: "I classify a low budget as I can't get more than one ad set out of the learning phase," and separately, "I dealt with a guy where it cost him 600 bucks to make a sale. Then he was spending $45,000 a day. It was still a low budget campaign." Brands spending $3,000/day at $600-700 cost per purchase get 4-5 conversions a day and are operationally low-budget. The consequence is that a high-spend, high-CPA account must run the same consolidated structure as a $20/day account, and it answers the recurring objection that consolidation advice is only for small accounts. Asserted, no data.

Second, the unit of segmentation inside an ad set is the concept, not the awareness stage. Blue Sense Digital: targeting still resolves at ad-set level, so mixing three concepts in one ad set confuses delivery and, because ad-level ROAS is unreliable, leaves you unable to say which concept worked when the ad set hits KPI. But top, middle and bottom-of-funnel ads for the SAME persona should sit together in one ad set. His reason is not machine learning, it is human bias: split out, the TOF ad set reads 2x and the BOF ad set reads 6x, and almost no operator or client will fund the 2x that is feeding the 6x, so they defund the traffic source. Consolidated, the same concept reads as one 4x and the decision is obvious. He allows the split works if you can genuinely hold that discipline. See [[Scaling Models#SC-067|SC-067]] for the naming convention this requires.
Sources: Dr. Matt Shiver, How to Run Facebook Ads for Coaches & Agency Owners (FREE COURSE), 2026-08-04; Dr. Matt Shiver, How the Facebook Ads Algorithm Actually Works, 2026-07-21; Dr. Matt Shiver, The BEST Way to Scale Facebook Ads in 2026, 2026-08-18; Professor Charley T, How to CRUSH Facebook Ads with a Low Budget, 2026-02-28; Professor Charley T, Meta advertisers: We've got a big problem, 2026-01-17; Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### SC-016 · At ~$100/month ($3/day), run one campaign, one ad set, one offer, broad targeting with Advantage+, to concentrate conversion volume for learning
Tier: T3 · Status: active
Meta ideally wants 50+ conversions per week per optimization unit; at $100/month you almost certainly cannot hit that, and fragmenting across multiple campaigns/ad sets makes it worse. The single-cell structure is the only chance the algorithm gets enough concentrated signal to learn. The small-budget job is described as protecting the algorithm's ability to learn.
Sources: Ben Heath, $100 vs $100,000 Facebook Ads Strategy, 2026-08-12
Last touched: 2026-08-18

### SC-017 · A single-campaign / single-ad-set setup strips every lever except launch, pause, and budget up/down; Meta's control tools require differentiated ad sets
Tier: T3 · Status: active
ROAS goals, target cost per result, value rules, and ad set spend minimums/maximums all operate at the ad set level, so with one ad set there is no differentiation for them to act on. Manual ABO is the opposite failure: user-controlled budgets cap the highest-ROAS ad sets and misallocate spend at the ad level. The middle path is a CBO with multiple concept-grouped ad sets.

Scoped qualifier added 2026-08-18. Brad Plock, relaying a Meta rep, says an ad set carrying no differentiated targeting and no differentiated bid type is "a folder", so for a landing-page test it barely matters whether the duplicate goes into the same ad set or a new one inside the same CBO. He defaults to the same ad set because he is maxing ad sets out anyway, and uses a per-lander ad set only for labelling. Both statements can hold: the rep's point is about delivery, this claim is about which control levers exist. The one constraint he names is keeping enough volume in the ad set for Meta to run efficiently. Relayed rep statement, no test.
Sources: Sam Piliero, Do THIS and the Meta Andromeda Algorithm Will LOVE You!, 2026-08-14; Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26; Andrew Faris, The Right Way To Test Landing Pages On Meta Ads In 2026 With Brad, 2026-06-22
Last touched: 2026-08-18

### SC-018 · Five 322 flexible ads give the creative equivalent of 60 ads consolidated into 5 data buckets, so learning is faster than 60 separate ads
Tier: T3 · Status: active
5 flexible ads x 12 combinations = 60 creative combinations, but only 5 data buckets. Because every signal is shared within each bucket, the system is claimed to make smarter decisions faster with every impression versus fragmenting data across 60 individual ads. The arithmetic is exact but the learning-speed benefit is asserted, not demonstrated.
Sources: Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10
Last touched: 2026-08-18

### SC-052 · Consolidation's second mechanism is reach, not conversion data: campaign reach does not sum, and fewer ad sets lowers frequency, lowers CPMR, and buys more reach at the same spend
Tier: T3 · Status: active
Distinct from [[Scaling Models#SC-014|SC-014]], which is about fragmenting conversion signal. Here the cost is fragmenting reach. Every auto-bid ad set independently hunts the same highest-intent in-market pool, so the Venn diagrams overlap and the same people absorb impressions from many entities at once: ten campaigns reaching 1,000 people each give account reach nearer 7,000. Kiel calls 30% overlap low and reports auditing an account at 80% overlap between summed campaign reach and account reach. He frames it as structural, since no ad set can hold a frequency of 1, so overlap multiplies with the number of live entities. The chain runs: fewer ad sets, fewer independent audience definitions, lower frequency, and because CPMR = CPM x frequency, lower CPMR and more reach at the same spend, sometimes the same reach on less spend. Ad sets are the real unit because that is where the audience is set; fewer campaigns matters mostly because it forces fewer ad sets. Moving to CBO compounds the gain, since Meta can starve weak entities instead of being forced to fund each one. Faris's parallel framing is that a fully split account gives Meta no ability to RANK ads, so it serves ad A, B, C and D to the same most-likely buyer instead of extending the best ad to the next person. The diagnostic that follows: the common failure shape is 10 campaigns x 5 ad sets at $2,000/day, and in audits the problem is almost never too many ads, it is too many campaigns and ad sets for the spend level. The 80% figure is an asserted audit read, not a shown dashboard.
Sources: Andrew Faris, Your Meta Ads Account Has Too Many Campaigns: Here's Why And What To Do, 2026-05-12
Last touched: 2026-08-18

### SC-053 · Full consolidation into one campaign and one ad set is wrong for about 90% of advertisers, for three reasons: divergent unit economics, non-overlapping audiences, and high-AOV low-conversion-volume accounts
Tier: T3 · Status: active
Unit economics: if a lower grade of inventory carries the same gross margin but only sells at deep discount, consolidating routes spend into the compressed-margin items and degrades both contribution margin and brand positioning. Audiences: his repeatable audit on any brand selling to both men and women is to open a consolidated ad set and pull the gender breakdown, where women's ads serve to men and vice versa, because targeting resides at ad-set level and gets confused. He notes the effect is not symmetric, women buying for male partners is real, the reverse much less so. High AOV: with a $10,000 AOV and roughly five orders a day at ~$50k/day spend, Meta has too little conversion signal to distribute ad-set budget on purchases or ROAS, so a CBO falls back to upstream proxies (CTR, CPC, hold rate). His stated finding from large datasets is that CPC correlates with ROI only at the extremes; within the normal band the correlation is weak to nil. So a CBO on a high-AOV account systematically funds the best soft-metric ads rather than the best converting ads, and the answer there is ABO with forced budget and longer read windows sized to conversion volume. He concedes about 10% of brands can consolidate totally. Asserted from an agency book, no comparative data shown.
Sources: Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### SC-054 · Segment by product-level unit economics, because bidding on lowest CPA or even on ROAS routes spend to the worse contribution-margin product
Tier: T3 · Status: active
Worked example on Meta: a $90 hoodie with $21 COGS and a $45 CAC yields $24 contribution margin; a t-shirt with $27 gross margin and a $15 CAC yields $12. Maximize conversions funds the t-shirt because its CPA is lower, and switching to conversion value does not fix it because the t-shirt's ROAS is also better. Only campaign segmentation forces spend onto the higher-contribution product. A second question falls out of the same table: a product acquiring that cheaply may have organic pull and would sell anyway, in which case the right move is to stop paying for it entirely and redirect the budget to the product that needs paid support to hit sell-through. Kiel and Faris reach the same conclusion from AOV: "a product with a $200 AOV and a product with a $300 AOV require a really different CAC to be successful. And even if it's the same ROAS," combining them in one volume-maximising ad set buys one of them at the wrong price. Their mental model is a department store, one campaign per section. Both agree the legitimate reason to split is economic (different AOV, margin, inventory constraint, or genuinely distinct audiences like menswear vs kids vs pets) and never a "sandbox" reason. The cost of that structure is that it needs stronger exclusions and active CPMR, frequency and new-visitor-percentage monitoring. This is the main commercial argument against the consolidation default. Reasoning plus worked arithmetic, no shown test.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Andrew Faris, Your Meta Ads Account Has Too Many Campaigns: Here's Why And What To Do, 2026-05-12
Last touched: 2026-08-18

### SC-055 · Campaign-level segmentation mirrors business units and stays fixed; ad-set-level segmentation mirrors the question you currently want answered and rotates
Tier: T3 · Status: active
Campaigns split where the business KPIs, forecasts and budgets split, for example denim as its own unit at 40% of revenue with different LTV dynamics, or basics separated from seasonal. Ad sets are the reporting instrument: split by format when you need to prove UGC beats campaign shoots to a CMO, split by concept when you are testing concepts, split by product when you need product-level reads. The misconception he names is treating ad-set structure as permanent; it should change whenever the question changes, while campaign structure does not. He adds that format-splitting is not his preferred structure and is justified only when the organisation needs that specific data to move budget. Asserted.
Sources: Blue Sense Digital, Why Most Fashion Brands Are Running Paid Media Wrong, 2026-05-25
Last touched: 2026-08-18

### SC-056 · An ad set needs a minimum of three ads so the algorithm can sequence across them; 3-15 is the working band and there is no meaningful upper limit at scale
Tier: T3 · Status: active
The lower bound is mechanistic, not statistical: sequence learning needs multiple candidates inside the siloed targeting unit to construct a purchase journey, and a single-ad ad set cannot sequence, so it cannot convert people who need 2-6 exposures. A sub-three ad set is a structural defect regardless of budget. He runs accounts with 200 creatives in one ad set, so his upper bound is far above the 4-8 per pack other operators use. Asserted from agency practice, no comparative test.
Sources: Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### SC-057 · Five ad sets holding four to six creatives each is unreadable at ANY budget, because the campaign is making two nested spend decisions the operator cannot separate
Tier: T4 · Status: active
Distinct from the volume-threshold argument in [[Scaling Models#SC-015|SC-015]] and from budget dilution. The objection is decision-layer count and operator legibility. Asked about $230/day across 5 ad sets with 4-6 creatives each, he says the structure would still be bad at $23,000/day: "There's no way for you to have any understanding what's going on. I mean, you've got 20 to 30 ads. There's the campaign is choosing which ad set to spend on the ad. It's choosing which ad creative to spend on." A 100x budget increase does not fix it. Useful as the direct counter to "I will consolidate once I can afford more spend." Reasoning only, no data.
Sources: Professor Charley T, Record Profits: the Meta Ads Andromeda Playbook, 2026-01-03
Last touched: 2026-08-18

### SC-058 · CBO versus ABO is a risk-versus-efficiency choice, not a performance question, because CBO compounds Pareto until about 4% of ads hold roughly 64% of spend and revenue
Tier: T3 · Status: active
The compounding is the distinctive part: 20% of ads take 80%, and inside that top 20% the same distribution repeats, so ~4% of ads carry ~64% of the account. He reports seeing this in every ad-profile breakdown he has run, across two separate videos, but showed no dataset. CBO therefore delivers the higher ROI and the higher fatigue risk, and skews product sell-through because Pareto applies at SKU level too, so a CBO across a wide catalogue pushes the whole business toward 20% of SKUs and de-funds things you paid for, such as an expensive shoot or a partnership ad. ABO gives lower risk at roughly 10% lower ROI. He treats the choice as seasonal rather than architectural: CBO in Q4, when you want maximum spend and efficiency in a short window and do not care which creatives get funded, then back to ABO in Q1, when conversion rates are no longer artificially inflated so tests read honestly and the business has low risk appetite anyway. He says he has seen both run successfully on accounts spending a quarter of a million dollars a day. Read alongside [[Scaling Models#SC-051|SC-051]], which treats the same concentration as the thing that kills eight-figure brands.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, Meta Ads Creative Strategy in 2026: The Full System, 2026-05-11; Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### SC-059 · The default structure at scale is a CBO with minimum and maximum spend limits controlling ~60% of budget while ~40% flows wherever Meta wants
Tier: T3 · Status: active
Stated across two videos as what the agency actually runs on most accounts. It is the explicit hybrid between the ABO and CBO poles in [[Scaling Models#SC-058|SC-058]]: you keep Meta's allocation efficiency on the free 40% and force spend onto assets you have a commercial reason to fund with the controlled 60%, such as new creative from a $20k shoot, a paid influencer partnership ad, or a product category the business must sell through. He concedes that once both minimums and maximums are set you are functionally running an ABO with more management overhead, which is why he gates it on account size: "if you're managing like 10k a month in ad spend, this is it's just kind of overkill," and at that level you pick plain ABO or plain CBO on risk preference and move on. Asserted, no comparative test.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### SC-060 · Catalog/DPA ads and manual product ads never share a campaign: manual ads carry acquisition, catalog ads exist to suppress blended CPA
Tier: T3 · Status: active
Catalog ads naturally target the bottom of the funnel and take the conversion credit, so mixing them with manual acquisition ads makes it impossible to know which campaign to fund. "Never put catalog and non-catalog in the same campaign." Stated in two videos, the second framing it as the answer to the complaint that catalog ads eat all the spend from newly launched concepts, since catalog and 322 prospecting have different definitions of success and therefore belong to different business objectives. His prescription for a multi-SKU store: one manual campaign promoting the single product best at acquiring repeat-likely new customers, judged on CAC, plus a separate catalog campaign that backfills revenue and drags the blended number down. Asserted from client work, nothing shown.
Sources: Professor Charley T, Meta advertisers: We've got a big problem, 2026-01-17; Professor Charley T, The BEST AD ON META after Andromeda, 2026-01-10
Last touched: 2026-08-18

### SC-061 · Ad count is not the spend ceiling: five or six ads in one campaign have carried over $100,000 a day
Tier: T3 · Status: active
"Remember, the amount of ads in your ad account has very little to do with how much money you can spend on the business." His framing is that the business sets spend capacity, not the ad account, and ad spend is a ramification of profit in the business. He argues the reverse case too, that a $10,000/day campaign should not be split across five or six SKUs. Practical use: when an account will not scale, do not default to diagnosing insufficient creative volume. ASSERTED, no account shown, and it sits against the creative-volume doctrine banked in the CR topic, so treat it as one operator's observed ceiling rather than a refutation.
Sources: Professor Charley T, The BEST Facebook Ads Strategy for 2026 Post Andromeda, 2025-12-27
Last touched: 2026-08-18

### SC-062 · Funnel allocation of 70-90% top, ~20% middle, 5-10% bottom is now enforced through the awareness-stage mix of creative you produce, not through campaign budgets
Tier: T3 · Status: active
The structural point matters more than the ratio. The historic implementation was three campaigns with three budgets. Under consolidation there is no separate TOF or MOF campaign to fund, so the same allocation has to move upstream: 70-90% of the assets you produce should be written for high stages of awareness (unaware, problem aware) and ~20% for middle-to-bottom. That reframes the creative brief as the budget-allocation lever. Stated in two videos. He treats the percentages as a rough split rather than a rule, allows that a bottom-of-funnel campaign may still sit separately, and points to the existing-customer dollar formula in [[Scaling Models#SC-072|SC-072]] as the better method for the bottom-of-funnel number. Asserted.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, Meta Ads Creative Strategy in 2026: The Full System, 2026-05-11
Last touched: 2026-08-18

## Account structure blueprints

### SC-019 · Run one CBO campaign per business goal (per product/category and per country); test and scale inside the same campaign
Tier: T2 · Status: active
Across an agency spending $4M in the last 30 days (~$100k/day): one CBO per product or product category and one CBO per country advertised to; some accounts have 1 CBO, some 10, but testing and scaling both happen within the same campaign. In the live client walkthrough, Canada+USA share one campaign, a new country expansion or new category gets its own CBO, and each new ad idea launches as its own ad set holding three creatives; after 7 days the batch is marked successful/unsuccessful in a learnings sheet and left running if it has no negative impact. He tested bid caps in that account and abandoned them, and a Europe expansion was tested and cut.

Professor Charley T, who originated the one-campaign framing, gives the operational definition and two boundaries. The definition: a business objective is one number written on a sticky note that every element in the campaign is measured against. Boundary one, offers stay apart, "Do not combine your offers inside of one campaign". A discounts/offers CBO and a strong-product CBO are separate campaigns, and he names mixing offers (or running one campaign with one ad set and dumping every ad in it) as the failure that produces most public "the one-campaign method doesn't work" rebuttals. Boundary two, catalog ads never sit with 322s, banked separately as [[Scaling Models#SC-060|SC-060]]. Two ad sets per campaign is fine, one per product or collection, and two campaigns for two similar products is fine when the definitions of success differ; he describes accounts as accordions that expand and contract. He states he changed how he communicates this rule after years of being misread, so any pre-2025 version of it is stale.

The delivery mechanism behind preferring CBO here: the ad is the pitch, the ad set decides which ad for which person, and the campaign allocates money between ad sets, re-deciding "millions of times in micro seconds". ABO removes the allocator's job, so "Each adset still has to spend the budget you've assigned. Even if it's targeting the wrong people or running bad ads," which forces bad ads to keep buying impressions and starves the ad sets that could scale. Under his user-experience model that forced spend is an active negative-signal generator, not merely wasted money. Reasoning, no test shown.
Sources: Nick Theriot, I Spend $100k/Day On Facebook Ads, 2026-08-03; Nick Theriot, My Full Process For Scaling Facebook Ad Clients In 2026, 2026-07-20; Professor Charley T, The BEST AD ON META after Andromeda, 2026-01-10; Professor Charley T, The BEST Facebook Ads Strategy for 2026 Post Andromeda, 2025-12-27; Professor Charley T, The NEW BEST Meta Ads Andromeda Course to Scale in 2026, 2026-01-24
Last touched: 2026-08-18

### SC-020 · Separate testing campaigns at scale are contested: Ben Heath carves out 10-30% of budget for them at $100k/month, while Nick Theriot runs no separate testing campaigns at $100k/day
Tier: T3 · Status: contested
Heath side: at $100k/month, the majority of spend goes through proven winners while 10-30% funds separate testing campaigns that trial new creative at low risk; the large-budget operator role is risk/portfolio manager reallocating by performance. At small budgets he explicitly opposes separate test campaigns because they split budget across too many variables. Theriot side: no separate testing or scaling campaigns exist anywhere in his $4M/30-day agency; everything tests and scales inside the same per-goal CBO. Charley T's Andromeda 1 structure and Sam Piliero's pack system also test inside the main campaign, via dedicated test ad sets rather than separate campaigns.

Two mechanisms added to the anti side 2026-08-18, both reasoning rather than data. First, attribution theft: the same humans exist across campaigns, so a test ad entering at the bottom of the funnel intercepts conversions the scaling campaign already worked for. "those testing campaigns often all of their success comes by stealing credit from scaling campaigns. They just come in at the 11th hour and when you get a new win, it comes at the expense of an old one." The account nets zero while the dashboard shows a new winner. The practical test that follows: judge a new creative on whether the campaign total improved, not on the new ad's own ROAS. Second, the cost condition. A separate testing campaign with a cost control is viable for operators comfortable ribboning spend into tests, but if the account is already at its spend ceiling, forcing spend does not tell you whether the thing you tested expanded the pipeline. Brad Plock's preferred landing-page method is therefore the in-place duplicate, which costs nothing when the lander loses. Neither side of this claim has produced a comparative test.
Sources: Ben Heath, $100 vs $100,000 Facebook Ads Strategy, 2026-08-12; Nick Theriot, I Spend $100k/Day On Facebook Ads, 2026-08-03; Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10; Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26; Professor Charley T, Meta advertisers: We've got a big problem, 2026-01-17; Andrew Faris, The Right Way To Test Landing Pages On Meta Ads In 2026 With Brad, 2026-06-22
Last touched: 2026-08-18

### SC-021 · The Olympic Rings method: exactly five ad concepts with distinct jobs, three cold-intro concepts and two lower-funnel closers, so no ads compete for the same person at the same journey stage
Tier: T3 · Status: active
Rings 1-3 are three completely different prospecting concepts (different format, angle, reason to care) for cold audiences; ring 4 closes people who saw rings 1-2 and ring 5 closes people who saw rings 2-3, built around direct offers, objection handling, or urgency. Static images are said to work well in the two closing rings. The design goal is that every ring reaches a different person at a different point in the sequence rather than competing for last touch.
Sources: Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10
Last touched: 2026-08-18

### SC-022 · The Andromeda 1 account is one CBO campaign with three ad sets: a control of 4-6 proven post IDs covering all five rings, plus two parallel test ad sets each holding one 322 flexible ad
Tier: T3 · Status: active
Always CBO at campaign level; ABO is dismissed as "a folder of one-ad-set CBO campaigns", complexity with no benefit. Control starts with the existing top 6-8 running ads and matures into harvested unicorn post IDs. The two test ad sets run one 322 each as parallel proving grounds, giving max 24 active combinations testing against the control. If the account cannot get multiple ad sets out of learning, collapse to one ad set with 4-8 ads covering all five rings. Later number for the control (his "all-star") ad set: "I wouldn't go past six or seven max. Probably five to eight is the good range." Same speaker, later date, so read 5-8 with a soft ceiling at 6-7 as his current band rather than a competing claim. He gives no mechanism beyond self-control and the sequencing argument, and answers a separate question about a broad scaling campaign with the same range.
Sources: Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10; Professor Charley T, Meta advertisers: We've got a big problem, 2026-01-17
Last touched: 2026-08-18

### SC-023 · Harvesting a unicorn means copying its post ID into the control ad set while leaving the source 322 running; the standalone post ID will not replicate the 322's performance
Tier: T3 · Status: active
When one permutation dominates (roughly every 3-4 months if things are done right), grab the post ID from the ad's URL via the inbox timestamp and add it as a new ad in the control ad set. Never turn off the source 322; it is performing, which is why you are harvesting from it. The post ID performed as one of 12 with shared-data benefits; as a standalone it contributes differently, which is expected.

Budget caveat he concedes when challenged: harvesting by comment volume only works above the spend level that generates comment volume. "if your comment volume isn't big enough to pick the ad out, then it sounds like you're not doing well enough to increase the spend." Small accounts should not attempt unicorn harvesting and should keep raising budget until the signal is legible. His supporting assumption, itself testable, is that spend share and engagement share move together, so the ad taking 80% of spend cannot be taking 2% of engagement.
Sources: Professor Charley T, Copy This Simple Meta Ads Strategy, 2026-08-10; Professor Charley T, The BEST AD ON META after Andromeda, 2026-01-10
Last touched: 2026-08-18

### SC-024 · Pack system: launch every new creative round as a NEW concept-grouped ad set inside one prospecting CBO, named avatar_concept_pack-N
Tier: T3 · Status: active
Each pack (ad set) holds one avatar x concept; new launches never interfere with existing packs except through budget distribution, and over time the continual addition of packs forces CBO budget to the best-performing ad sets. Packs launch on a regular drumbeat every 1-3 weeks, so one pack is always on a spend minimum. This preserves per-segment levers such as value rules on an ad set skewed to an age/gender and maximums on fatigued packs. Claimed basis: 80+ brands and a $30M+ monthly portfolio.
Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26; Sam Piliero, Do THIS and the Meta Andromeda Algorithm Will LOVE You!, 2026-08-14
Last touched: 2026-08-18

### SC-025 · New packs launch with a 7-day ad set spend minimum equal to target CPA, capped at 20% of total budget; remove the minimum after 7 days
Tier: T3 · Status: active
The minimum forces new creatives to get test spend so produced ads never sit at $0 delivery. Set the daily minimum to 1x target CPA in dollars; if that exceeds 20% of total campaign budget, switch to percentage and cap at 20%, because never more than 20% of budget should go to testing. After 7 days, unselect the minimum (this does not reset learning): a winner keeps spending above the threshold on its own, a loser dies without overspending.
Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26
Last touched: 2026-08-18

### SC-026 · Core account structure is two required campaigns (prospecting CBO with packs, retention CBO on past purchasers) plus optional retargeting and scale campaigns
Tier: T3 · Status: active
Prospecting CBO excludes purchasers and only acquires new customers; retention runs winning/evergreen/promo ads at high frequency to 180-day and all-time purchaser audiences in 1-2 ad sets, because most e-commerce businesses make their money on repeat purchase, not the first sale. The same system is shown on three account sizes: $7,900/30d at 6.94 ROAS, $27,000/30d at 9.5 ROAS, and $1.8M/30d spend driving $2.9M revenue (nearly $1M spend and $1.5M revenue in the last 7 days). The accounts are real, but the results demonstrate the accounts, not a controlled effect of the structure.
Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26
Last touched: 2026-08-18

### SC-027 · Add a separate retargeting campaign only when audience segment reporting shows the prospecting campaign overspending on engaged audiences
Tier: T3 · Status: active
Retargeting mostly happens inside prospecting by default. Set audience segment reporting (engaged = add-to-cart 90 days + site visitors 30 days; existing = all-time purchasers) and watch the new/engaged/existing split; only if engaged spend is disproportionate do you carve out a retargeting campaign and exclude engaged from prospecting. Typical retargeting audiences: FB/IG engagers, 30-60-day site visitors, 90-day+ add-to-carts/initiated-checkouts, flexed by business size; creative heavies up on objections, sales, and offers.
Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26
Last touched: 2026-08-18

### SC-028 · A scale campaign is a broad single-ad-set holding only the ~5 absolute top proven ads, existing solely to force more spend on them
Tier: T3 · Status: active
Sits at the top of the account, above prospecting. Only ads you know like the back of your hand qualify, roughly 5 total, nothing more; its only job is forcing additional delivery against proven winners. No incrementality data for the scale campaign shown.

Size of the prize, stated in two videos: the move buys roughly 20% additional daily spend on an already-maxed ad, "on a good day". That sets a threshold. An ad capped at $60/day gains about $10/day, which does not pay for the structural complexity; an ad at $400/day gains about $80/day, and running the move across ten top ads at once can unlock ~$1,000/day. Preconditions he names: the scaling campaign has no purpose unless you already have creative pushed to its equilibrium daily spend, the original must stay live and you copy the post ID rather than moving the winner (see [[Scaling Models#SC-006|SC-006]]), and exclusions must be set. Named rookie errors: rolling a $60/day ad into a scaling campaign and calling the result a scaling problem when the real bottleneck is the landing page, the offer or the absence of a working concept, and testing inside the scaling campaign. The 20% figure is asserted, not shown.
Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26; Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### SC-029 · Testing structure: one campaign per landing page, four ad sets each locked to one concept/format pair, 3-5 large-variation ads per ad set, fully broad with audience network excluded
Tier: T2 · Status: active
Each ad set = one format (AI animation, native static, founder ad, mini podcast VSL) carrying one concept, with 3-5 variations inside. Variations must be large swings; a variation as small as a new hook typically gets no spend because one ad takes it all, whereas big variations within the concept give Facebook room to find which resonates. Targeting was 100% broad, no exclusions, US only, with audience network and associated placements excluded at account level. This is the exact structure used in the documented $1k/day case study whose revenue dashboard is shown.
Sources: Mark Builds Brands, ZERO to $1k/day in 3 days with ai dropshipping [full case study], 2026-07-30
Last touched: 2026-08-18

### SC-030 · All creatives go into one CBO; ads that fail to gain spend stay on unless they hurt performance
Tier: T3 · Status: active
Everything is tossed into a single CBO campaign and the budget algorithm decides: an ad must gain enough spend to drop cost per acquisition to matter for scaling. Ads that do not take spend are left running (they cost nothing) unless they actively hurt performance. This replaces manual test/kill structures at the ad-set level.
Sources: Nick Theriot, Simple Creative Testing Framework I Use To Scale Facebook Ads In 2026, 2026-08-12; Nick Theriot, When to Turn Facebook Ads Off in 2026, 2026-08-07
Last touched: 2026-08-18

### SC-031 · Whitelisted ads live inside the main testing/scaling CBO, one ad set per content creator, never a separate campaign
Tier: T3 · Status: active
Create a new ad set in the existing main CBO, put all of that creator's whitelisted ads in it, and name the ad set for the creator. With five creators you get five ad sets, all inside the one CBO where everything else tests and scales, no dedicated whitelisting campaign.
Sources: Nick Theriot, You Just Found a Winning Ad… Here's Exactly What To Do Next, 2026-07-31
Last touched: 2026-08-18

### SC-032 · To test listicles/advertorials against product pages, duplicate the ads (or ad sets) with only the URL changed, all inside the same CBO, and let Facebook allocate spend
Tier: T3 · Status: active
Two equally valid setups: duplicate the 3 videos within one ad set and change destination URL per copy (listicle set, advertorial set, product-page set, quiz-funnel set inside the same ad set), or duplicate the whole ad set per destination. The only rule is everything stays inside the same CBO so Facebook distributes spend across destinations itself.
Sources: Nick Theriot, You Just Found a Winning Ad… Here's Exactly What To Do Next, 2026-07-31
Last touched: 2026-08-18

### SC-033 · Run every ad in both a value-optimized and a volume-optimized setup because they reach different parts of the customer-value distribution
Tier: T3 · Status: active
Faris duplicates every ad into a value (min ROAS / highest value) setup and a volume (highest volume) setup in every account. With a fixed budget, volume optimization inevitably gravitates to the cheapest products/customers, while value optimization climbs the order-value distribution; which side takes more spend varies by account. Meta's incoming "max conversions with a ROAS control" (volume-optimized with a ROAS target) attempts to reach the modal-order-value customer without optimizing up the value chain.
Sources: Andrew Faris, Do Cost Caps Work? Taylor Holiday Brings $200M Of Data, 2026-08-06
Last touched: 2026-08-18

### SC-063 · Do not split countries into separate ad accounts; the only defensible reason is billing in local currency
Tier: T3 · Status: active
"I would advise against segmenting countries out at an ad account level." Stated across two videos. The cost is labour: he cites clients running seven ad accounts for seven regions and says management overhead scales badly against any benefit. Every other justification dissolves, and the reporting argument (plugging each account into a dashboard) is answered by filter rules on country or a campaign-name convention. Currency is genuine, a US web presence billing a US bank needs a USD account. Country segmentation belongs at campaign level instead, and even there it is conditional: separate campaigns are warranted when you hold inventory per market with its own sell-through targets or when regions use different subdomains or URLs, but if all stock ships from one warehouse you can consolidate regions and push segmentation down to ad-set level. Note the tension with [[Scaling Models#SC-019|SC-019]], where Theriot runs one CBO per country inside a single account. Asserted from agency practice.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### SC-064 · A second ad account on the same pixel and page running different bid logic wins auctions the primary account is not bidding on, and doubles as ban insurance
Tier: T3 · Status: active
Mechanism: if the primary account runs maximize conversions, the second runs maximize conversion value or cost/bid caps, so the same creative enters auctions the first account's bidding never reaches. The counter-argument he raises and does not resolve is self-competition raising your own CPMs; he argues same-pixel same-page limits cross-bidding and states plainly that nobody has proven it either way. The de-risking benefit is concrete and independent of the auction argument: a secondary account holding even 10% of spend can be scaled immediately if the primary is banned or its billing fails. He flags the tactic as fast-moving and likely stale within six months of 2026-06-15, so date-check it before use. Asserted, no test.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15
Last touched: 2026-08-18

### SC-065 · Worked example of a ~$25k/day account: five campaigns, each with a stated commercial reason (ABO testing, CBO scaling on cost caps, promo, advertorial, DPA)
Tier: T3 · Status: active
Testing stays ABO and also scales in place, with individual ad sets inside it spending multiple thousands per day. Winners are copied into the scaling campaign by post ID every one to two weeks and are never turned off in testing: "they're not turned off in the testing campaign." The scaling campaign is a CBO, one ad set, cost caps. The promo campaign is separated because promos run every 3-4 weeks and turning creative over constantly would disrupt learning in the evergreen campaigns, and promo buyers are more price-sensitive. The advertorial campaign was carved out only after advertorials organically took ~30% of spend and earned their own KPIs as a distinct funnel. DPA sits at the bottom, capped by frequency and read on incremental attribution. He also rejects the idea that big accounts stop testing, citing accounts at $300,000/day still running tests. The point of the example is that each split has a commercial justification, which is the same test [[Scaling Models#SC-054|SC-054]] applies. Account described, not shown.
Sources: Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### SC-066 · Spend-tier playbook for fashion e-commerce: under $50k/month is 2-3 campaigns and 30-50 new ads; $75-200k is 4-6 campaigns with incremental attribution and 65-200 ads; $250k+ mirrors business complexity
Tier: T3 · Status: active
Bottom tier: one testing campaign with a separate ad set per product launch or concept, one scaling CBO only if assets can run long enough to justify it, and one existing-customer retargeting campaign. Measurement is 7-day click plus 180-day LTGP:CAC held between 2 and 3. Google is 80%+ Shopping, with feed fixes as the highest-leverage work. Creative is 80% evergreen, 20% seasonal. Mid tier adds lift studies, cohort analysis feeding the forecast, aMER and aMER-adjusted as daily measures, ad sets split by concept, capped DPAs, existing-customer frequency capped at 7, size-curve management on Google, and inventory-aware creative allocation. Top tier adds daily and monthly P&L reconciliation, contribution margin tracked separately for first-time and existing customers, 200+ ads a month, at least 10% of ad spend into production, geo-lift, omni dedup, TikTok and YouTube. YouTube only becomes viable at the top tier because it needs both geo-lift capability and budgets large enough to read. Prescriptive, drawn from an agency book of fashion clients; nothing was shown and the numbers are vertical-specific.
Sources: Blue Sense Digital, Why Most Fashion Brands Are Running Paid Media Wrong, 2026-05-25
Last touched: 2026-08-18

### SC-067 · Name ad sets by persona, angle, offer, content type and launch date; batch-date names like "March 7 creatives" destroy the ability to KPI a concept
Tier: T4 · Status: active
A date-batch name signals the concepts were bundled rather than structured, so no filter groups the same concept across ad sets and no concept-level verdict can be fed back to the creative team. When the agency inherits accounts named this way they retrospectively rename historical ad sets purely to recover a readable structure before deciding what to double down on. This is the naming layer of the data-integrity requirement, and it is the precondition for the concept-per-ad-set rule in [[Scaling Models#SC-015|SC-015]]. Reasoning, no test.
Sources: Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### SC-068 · Account restart method: relaunch the entire historical creative archive at once into bid caps and target ROAS, no creative testing, and let the bid do the filtering
Tier: T3 · Status: active
Applied to She's Birdie in Oct-Nov 2025 after roughly seven months of zero spend. The mechanism is that a manual bid makes ad count costless: ads that cannot hit the target simply do not spend, so there is no need to pre-select or stagger launches. Newly produced ads still took spend immediately alongside the archive. Faris reports most of the old ads could not produce a return at the required performance level and self-eliminated. This is the manual-bid analogue of [[Scaling Models#SC-030|SC-030]], where everything goes into one CBO and non-spenders are left on. Asserted on a podcast, no screen share, and it is one restart on one brand.
Sources: Andrew Faris, From A 65% Decline To All-Time Revenue Profit Highs With Richie Mashiko, 2026-04-27
Last touched: 2026-08-18

### SC-069 · Non-converting campaigns (traffic, reach, video views) are the last intervention for a reach problem, after every structural lever, and by then are usually unnecessary
Tier: T3 · Status: active
Kiel's team keeps tactics for it but treats it as end-of-list, applied only once consolidation, exclusions, placements, partnership ads and creative diversity are all in order. Faris rejects it outright and cites a Meta rep pushing exactly this play, video-view campaigns in October to build a pool for the November-December peak, which his own data did not support. Operator rule: never treat a top-of-funnel objective campaign as the first fix for rising CPMR. Fix the entity count first, per [[Scaling Models#SC-052|SC-052]]. Faris's counter-evidence is described, not shown.
Sources: Andrew Faris, Your Meta Ads Account Has Too Many Campaigns: Here's Why And What To Do, 2026-05-12
Last touched: 2026-08-18

### SC-070 · Dead media-buying levers are daily bid tweaks, daily budget pacing, interest targeting and lookalikes; the live levers are account architecture, concept-level ad-set segmentation, existing-customer allocation and landing-page/CRO testing
Tier: T3 · Status: active
The framing is return on the operator's time, not whether a tactic technically still functions. "What 99% of people shouldn't be doing is daily bid tweaks." A daily bid tweak might squeeze 5% for an hour of work a day; the same hour on creative can double or triple the account. Daily budget pacing decides on sample sizes too small to be real. Page and CRO split testing replaces interest testing as the higher-inflection use of the same effort. Useful as a defensible deprioritisation list rather than a general "creative is king" statement. He pairs it with his own bounds: consolidation beats segmentation, media buying still moves 10-20% above roughly $100-300k/month, and no universal structure exists. Asserted.
Sources: Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### SC-071 · Superseded: the Feb 2025 prescription to pause winners into a dedicated Advantage+ scaling campaign with 0% existing-customer budget caps
Tier: T3 · Status: superseded
Recorded because it still circulates. The Feb 2025 structure was a dedicated testing campaign, promotion of winning post IDs into an Advantage+ scaling campaign with existing-customer budget capped at 0%, plus a separate retargeting campaign. The speaker time-boxed it himself: "this will probably be outdated in 3 to 6 months cuz these things change all the time." Codex-current practice moved away from it during 2026. [[Scaling Models#SC-020|SC-020]] records that Theriot at $100k/day, Charley T's Andromeda 1 and Piliero's pack system all test inside the main campaign via dedicated test ad sets, and [[Scaling Models#SC-022|SC-022]] gives the one-CBO/three-ad-set structure that replaced it. [[Scaling Models#SC-006|SC-006]] separately rules out the pause-and-relaunch step. What survives from that webinar is orthogonal to structure and still current: 7-day-click reads, heavy exclusions on cold campaigns, and concept-level testing. Treat the structure section as stale from roughly mid-2025; keep the measurement sections.
Sources: Blue Sense Digital, How To Structure Your Meta Ads for Profit (Free Live Webinar), 2025-02-19
Last touched: 2026-08-18

## Retargeting budget at scale

### SC-034 · Budget retargeting at ~10% of total daily ad spend, scaled with top-of-funnel traffic volume
Tier: T2 · Status: active
At $1,000-1,500/day total spend he runs the retargeting ad set at $100-200/day, started at $100. Because the audience is only people who already touched the brand (followers, site visitors, subscribers), the sustainable retargeting budget scales with top-of-funnel traffic: more TOF spend, more retargeting spend; the ad set is throttled up when call volume and lead quality hold and down when they slip. His own ad account shows $14K spent on the retargeting ad set producing $60-70K revenue (5x cash collected) at these budgets.

Blue Sense Digital pushes the same layer harder in the other direction and inverts the operating question: on cold, ask where you can spend more; on retargeting, ask where you can take money out. "you want to be at all times minimizing retargeting spend as much as possible." In audits he repeatedly finds ~50% of account spend going to existing plus engaged audiences, which he calls support spend that drives no new-customer growth, found via the audience-segment breakdown at the bottom of Ads Manager. Two rules follow: KPI retargeting on frequency plus incremental ROAS rather than reported ROAS, and treat a rising DPA share as a warning, because DPA ROAS is a direct reflection of top-of-funnel investment. He names a "DPA death spiral" from six fashion audits in two weeks, all spending ~80% on DPAs while declining, where cutting TOF to fund DPAs collapses the funnel that feeds them. The 10% figure and the ~50% audit figure are both asserted; only Shiver's account was shown.
Sources: Dr. Matt Shiver, The 'Right Way' to Run Facebook Retargeting Ads in 2026, 2026-07-28; Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15
Last touched: 2026-08-18

### SC-035 · Run retargeting as ONE ad set holding every warm source (website 180d, IG engagers 180d, FB engagers 180d, customer lists) because low budget means too few pixel fires to feed multiple ad sets
Tier: T3 · Status: active
Splitting warm sources into separate ad sets starves each of conversion signal at $100-200/day. All custom audiences go into one bucket as suggested audiences; 180 days is the window so the pool self-refreshes and the ad set can run indefinitely, with 30-60 day windows only for very large audiences.

Blue Sense Digital adds a cost argument that holds at any budget, not just at low budget: "That hyper segmentation and retargeting. All it does is increase CPMs." Splitting by warmth tier (add-to-cart vs initiate-checkout vs site visitors vs product category) raises CPMs, and the CPM increase is never outweighed by the conversion-rate increase. He labels six-tier warmth structures 2019-era practice and challenges anyone to justify them. Asserted from audits, no shown CPM comparison.
Sources: Dr. Matt Shiver, The 'Right Way' to Run Facebook Retargeting Ads in 2026, 2026-07-28; Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### SC-072 · Set existing-customer budget as a dollar calculation (customers x desired monthly frequency x CPM / 1000), never as a percentage of spend
Tier: T3 · Status: active
Worked example: 300,000 existing customers x 3 impressions/month x a $2.50 CPM = $2,250/month. The argument against percentages is that the same 20% can mean a frequency of 50 or a frequency of 1 depending on customer-pool size and cold budget, so the percentage carries no information; 20% at a frequency of 50/month is obviously broken and 20% at a frequency of 1 is obviously underspent. He blames Advantage+'s existing-customer spend-cap percentage field for framing the whole industry around the wrong input. The formula produces numbers most operators find shockingly small: even very large brands land in the $10-40k/month range at a 3-6 monthly frequency, and he reports seeing tiny businesses put $40k/month against their own list. His CPG example runs about $20/day. Companion diagnostic, and the two videos disagree on the window: pull the frequency column on existing-customer segments and keep it under 8 on the last 7 days, or under 7 on a 30-day rolling window. Reconcile the window before writing an internal rule. Stated in three videos, always asserted, never shown. This cuts against the flat percentage framing in [[Scaling Models#SC-034|SC-034]].
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026: The Full System, 2026-06-15; Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01; Blue Sense Digital, Everything You Need to Know About Finance in eCommerce, 2026-05-04
Last touched: 2026-08-18

### SC-073 · At small budget, run acquisition against warm 30-day audiences only and let larger competitors pay for the prospecting
Tier: T3 · Status: active
He calls it broad retargeting, and here warm-only IS the acquisition campaign, which is different from [[Scaling Models#SC-034|SC-034]] and [[Scaling Models#SC-035|SC-035]], where retargeting is ~10% of a larger account. The argument: the small advertiser's job is being the better choice for someone whose credit card is already out, not building awareness. People in the 30-day pool (site visitors, Instagram, Facebook and WhatsApp engagers) are already brand, solution and product aware, so the creative job is a reminder plus one specific reason to pick you. He calls the standard full-funnel prescription a waste of money at small budget, which directly contradicts it. He claims accounts spending $10,000-50,000/day still operate this way. Asserted, no account shown, and the ceiling on this approach is the size of the warm pool, which he does not address.
Sources: Professor Charley T, How to CRUSH Facebook Ads with a Low Budget, 2026-02-28
Last touched: 2026-08-18

### SC-074 · Allocate at least 10% of budget to engagement campaigns at every budget level
Tier: T3 · Status: active
Three named allocation points: a luxury men's goods brand taken from ~$8,000/day to ~$60,000/day average over about 18 months while running ~$10,000/day (17%) in engagement; a health and wellness account at 10-15%; and an unnamed 8-figure brand running 80% engagement and 20% catalog with no conversion prospecting at all. The stated goal of the amplified organic content is explicitly NOT virality: content that appeals to people outside the buying niche degrades the delivery model, and his failure example is his wife's Los Angeles Pilates studio going viral in Denmark. All figures asserted in conversation, nothing shown, and the underlying claim that engagement campaigns improve conversion outcomes is itself contested elsewhere in the codex. Treat the 10% floor as one operator's allocation habit, not a validated threshold.
Sources: Professor Charley T, How to CRUSH Facebook Ads with a Low Budget, 2026-02-28
Last touched: 2026-08-18

## New-product launch and verdict cycles

### SC-036 · New-product test structure: one CBO sales campaign, one Advantage+ ad set, ~12 creatives, $100/day for 7 days, purchase-optimized even on a fresh pixel
Tier: T3 · Status: active
One campaign, one ad set (conversions, website, maximize conversions, purchase event selected even if the pixel has no purchase history), Advantage+ audience, US, 18+. Budget $100/day for 7 days (a $700 gamble); scale down to $50 or $25/day if needed but never below $25/day, which he says is almost impossible to run at. Load ~12 recreated competitor winners (top 3-4 each from top-performing, longest-active, most-duplicated), one image or video per ad, enhancements off.
Sources: Nick Theriot, The Most Braindead Way To Find Winning Products in 2026, 2026-08-17
Last touched: 2026-08-18

### SC-037 · Product verdict cycle: 7 days per avatar, 20%/day budget bumps if profitable, kill and swap avatar if not, drop the product after 2-3 avatar attempts
Tier: T3 · Status: active
After 7 days profitable, raise the CBO budget ~20% per day. If unprofitable, turn off the whole campaign, rebuild brand/creatives for the second-highest-occurrence avatar, and relaunch a fresh CBO (a new campaign is justified here because the avatar IS the scaling thesis, unlike testing inside an established account). Two, at most three, avatar attempts before abandoning the product entirely.
Sources: Nick Theriot, The Most Braindead Way To Find Winning Products in 2026, 2026-08-17
Last touched: 2026-08-18

## Scaling beyond budget: geography and positioning

### SC-038 · Geo expansion makes winning ads behave like fresh launches; businesses have 2-3x'd within a month of exporting winners to one or two new countries
Tier: T3 · Status: active
Taking proven winning ads from one country into a new country "almost makes it feel like you're just simply running those ads for the first time ever again," producing a surge of traffic and sales. He has seen businesses two to three X within a month of expanding to a new country or two with existing winners. No named account or shown data.
Sources: Nick Theriot, I Spend $100k/Day On Facebook Ads, 2026-08-03
Last touched: 2026-08-18

### SC-039 · Repositioning the same product for a new avatar or a new desire unlocks scale jumps: one client to ~$100k/month profit, another from $100k/month to $1M/month
Tier: T3 · Status: active
A product positioned for college kids (same as all competitors) was repositioned for cigar smokers with new creative, copy, and product pages, and that single avatar change helped the client scale to about $100k a month profit; the mechanism is being the first brand to speak to that avatar. A second client's product positioned against anxiety plateaued around $100k/month; repositioning it as a fun girls' night activity (different avatar AND different desire) scaled it to $1M/month. The claim: the desire you attach the product to can be worth 10x more scale than the product's original positioning. Both are named result figures from his client roster, told not shown.
Sources: Nick Theriot, It Took Me 10 Years to Learn This Secret Facebook Ads Scaling Strategy, 2026-07-24
Last touched: 2026-08-18

### SC-040 · Australian e-commerce spend has a practical ceiling around $500k/month before frequency saturates the TAM
Tier: T3 · Status: active
In a small market you start hitting everyone roughly every 30 days above this level and frequency goes through the roof, making further scale very hard. This is the structural argument for expanding a $10M+ AU brand into the US rather than pushing local spend higher.
Sources: Blue Sense Digital, The US Launch Playbook for Non-US Brands, 2026-08-17
Last touched: 2026-08-18

### SC-041 · US-wide and state-by-state launches both work; choose state-level only for seasonality, low budget, or retail-presence reinforcement
Tier: T3 · Status: active
US-wide targeting naturally gravitates spend toward the right (e.g. warm-weather) states, so seasonality alone rarely forces state targeting. Around $10k/month across the whole US is called "sketchy" thin; consolidating into states concentrates frequency. State-level also fits when reinforcing a select-state retail rollout. Counterweight: state sales-tax thresholds mean concentrating millions of revenue in one state can worsen margin vs diversifying US-wide.
Sources: Blue Sense Digital, The US Launch Playbook for Non-US Brands, 2026-08-17
Last touched: 2026-08-18

### SC-075 · Cutting the account down to its best two or three customer avatars is itself a scale lever: Key Cafe went from ~$4,000/day to ~$20,000/day after they stopped advertising to everyone else
Tier: T3 · Status: active
The sequence was to attract many lead types first, identify the three best-performing ideal customer avatars, then deliberately kill spend against every other type on the grounds that they were a liability. Mechanism claimed is the same as the product-mix argument in [[Scaling Models#SC-054|SC-054]]: a thousand buyers arriving for a thousand different reasons make the machine's job harder and make a second purchase nearly impossible. This runs directly against the "test all angles across all avatars" default he is answering, and it is the account-level counterpart to [[Scaling Models#SC-039|SC-039]], where repositioning to a single avatar unlocked the scale jump. ASSERTED, no account shown, single named client.
Sources: Professor Charley T, The BEST Facebook Ads Strategy for 2026 Post Andromeda, 2025-12-27
Last touched: 2026-08-18

### SC-076 · Whether CAC necessarily rises with scale is contested
Tier: T3 · Status: contested
Ben Heath's model: the pool of high-affinity buyers is finite and gets exhausted, forcing progressively colder audiences, so accept a lower ROAS at higher volume because absolute profit is larger (4x at $1M/month beats 10x at $10,000/month). Professor Charley T concedes only that a new customer costs more than a returning one and rejects the general law: "there are plenty of businesses that get better at customer acquisition cost the more they spend because they get better and better at understanding who that customer is and they have more brand equity." Both positions were asserted in the same joint session with no cohort data on either side. Practical resolution the operator can run: track NCPA by month against cumulative spend in your own account. The answer is account-specific and directly observable.
Sources: Professor Charley T, How to CRUSH Facebook Ads with a Low Budget, 2026-02-28
Last touched: 2026-08-18

## Cross-channel allocation

### SC-077 · Allocate the next dollar by the profit frontier: push each channel until its incremental acquisition MER hits breakeven, and only open a new channel once every current channel is at its frontier
Tier: T4 · Status: active
The operating question is "if we had another $10,000 next month, which channel returns most on that specific $10,000", which is a different question from which channel has the best average ROAS. The inverse move matters equally: pulling $10k out of Google where the marginal dollar returns 2x and moving it to Meta where the marginal dollar returns 4x on new-customer revenue. He is explicit that the only rigorous read is controlled incrementality tests per channel, with MMM or experienced intuition as the substitute at seven figures, which is a real limitation since most accounts can do neither. This is the argument against opening tertiary channels while the core channels are still below frontier. Reasoning, no data shown.
Sources: Blue Sense Digital, Everything You Need to Know About Finance in eCommerce, 2026-05-04
Last touched: 2026-08-18

## Spend ladders and automation

### SC-042 · Ad spend scales with revenue stage assuming a 2-4x front-end return: $30/day boosted posts to $20k/mo, $100-200/day to $50k, $500-1000/day to $100k, $1000-2000/day beyond
Tier: T3 · Status: active
His coaching-business ladder: at $10-20k/mo just boost posts at $30/day; at $20-50k/mo run DM/VSL/webinar ads at $100-200/day minimum booking calls at $100-500 each; reaching $50-100k/mo requires roughly $500-1000/day; past $100k/mo requires $1000-2000/day and produces at least 50-100 leads/day. The arithmetic driver is working backwards from a 2-4x front-end cash multiple on spend. He cites his own $2.25M revenue / $643k profit result, but the ladder itself is prescriptive without shown account data.
Sources: Dr. Matt Shiver, How I Built a $2.25M/Year Coaching Business, 2026-08-11
Last touched: 2026-08-18

### SC-043 · API-connected AI agents can run rule-based Meta account management: scheduled daily digests, threshold alerts, and automatic execution such as pausing ads past a CPA cap
Tier: T3 · Status: active
Heath demos an agent connected to the Meta Marketing API via an app token executing changes (it doubled a campaign budget on a ~£10/day test account and verified via the API). The operating pattern he proposes: scheduled daily summaries (spend, impressions, CPM, issues), alerts when ROAS drops more than 20% or CPA breaches a cap (his example: ~$40 CPA, kill ads above $50), and cross-platform Meta-vs-Google weekly budget-allocation comparisons. The automation layer is rules-on-top-of-API, not new Meta functionality; only the trivial budget action was shown running, and the video carries heavy sponsor framing.
Sources: Ben Heath, How To Automate Facebook Ads Like An Expert, 2026-07-28
Last touched: 2026-08-18

