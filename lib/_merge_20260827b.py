"""2026-08-27 research pass, part 2: attribution, learning, Google, math, auction."""
import io
from pathlib import Path

SCI = Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")

AT = r'''
### AT-103 · Brand search is NOT incremental: two accounts, a falsification method, and the clicks migrate straight back to organic
Tier: T2 · Status: active
The best-designed test in this pass, because it is built to be falsifiable and the operator states the failing condition up front.
**The method, which costs nothing and we can run it on any Google client.** "You just need to do an export out of Google Search Console for just the search term of your branded key term", chart daily organic against paid clicks for the branded term, switch brand search off, and watch where the clicks go.
**The decision rule, stated as a clean binary:** "And if total click volume remains and it all shifts into organic, it's not incremental. If it doesn't shift and you actually see a decline in the..." Both outcomes are named in advance, which is what makes it a test.
**Account one.** Roughly $15/day bought 50-60 paid clicks a day, about half cannibalised from organic. After a full shutoff: "we're actually getting more organic clicks than they've ever gotten before. It's all been cannibalized back into organic traffic."
**Account two.** "previously, about 30% of click volume from brand came from paid clicks. Now, almost 100% of it comes from organic." Total click volume held.
**The SERP mechanic underneath, and it also explains why the reported CTR moves.** A branded query showing both a paid and an organic result counts an impression on each: "you're double serving on the one user". So paid spend inflates total impressions without adding a click.
**Guards, and there are real ones.** The headline generalisation is unsourced: "I'll be proving to you why brand search for 80% plus of e-commerce brands is not incremental" rests on two accounts. **Account two is confounded and he says so twice in contradictory ways**, first "this was actually a bidding strategy change. This wasn't a budget decrease", then seconds later "we actually decided to pull some spend as well to run this model". He also disqualifies total CTR as a measure because of the double-serving above, and then uses a CTR comparison as supporting evidence.
He supplies the honest counter-condition himself: click loss is not conversion loss, because "those people that pathway to a competitor and that pathway back to you anyway".
**Arithmetic note.** Account two's saving is overstated. He states $100/day cut to "$5 to $10" a day, which is $2,700 to $2,850 a month, not the "$3,000" he quotes, and brand search is still running, so "cutting brand search out" is not what happened.
Sources: Blue Sense Digital, Heres Why Your Should Turn Brand Search Off, 2025-04-14
Last touched: 2026-08-27

### AT-104 · The 7-day-click reconciliation: default Meta ROAS against Acquisition MER, and the residual gap is returning-customer revenue
Tier: T3 · Status: active
A concrete procedure for the gap that [[Attribution & Incrementality#AT-098|AT-098]] measured but did not give a workflow for. AT-098 showed Meta's own incremental column cutting a prospecting campaign from 108 purchases to 29. This is the cheaper first cut of the same problem.
**The symptom:** "Your acquisition mode will be a 2.5, but your return on ad spend is a four."
**Step one, strip view-through.** "go and click on columns, come down, click on compare attribution setting, and then come through and click on 7-day click". Result on his example: it "drops to a 2.5 once you switch your reporting over to 7-day click".
**Step two, attribute the residual.** Whatever gap survives 7-day click is returning-customer click revenue, and the structural fix is separation: "Exclude existing customers from all your cold campaigns. Pull existing customers into their own dedicated campaign."
**The error bar is the part worth carrying into client reporting.** Two campaigns showing the same default ROAS can differ roughly 2x in true value: "if a campaign says it's at a full return on ad spend, that could be at a 1.8, it could be at a 3.7." **That is a direct argument for never presenting a default-attributed number to a client without saying what it is**, which is already our standing rule.
He claims "90% of ad accounts that I look at don't do it", unsourced. On Google the equivalent fix is campaign-level brand and cold separation "rather than having a Pmax that encapsulates branded key terms", which pairs with [[Attribution & Incrementality#AT-103|AT-103]].
**⚠ He contradicts this three months later and the carve-out is never stated in this file.** Here: "You can actually trust Facebook's attributed numbers as long as you can draw correlation directly into the P&L." On 2025-09-16, on long purchase windows: "attribution really falls apart in these particular instances." The June procedure is presented as general and is not.
Sources: Blue Sense Digital, How to Trust Meta ROAS and Tie It Directly to Your PL, 2025-06-17; Blue Sense Digital, Why You Shouldnt Measure Results Daily or Even Monthly in eCommerce, 2025-09-16
Last touched: 2026-08-27

### AT-105 · Cost per net new reach: a real saturation instrument, and the operator dismisses it in April then leans on it in September
Tier: T2 for the account, T4 for the thresholds · Status: active
**The method, which is reproducible from Ads Manager alone.** Pull cumulative account reach from day one to month N, pull it again one month further out, and the difference is net new reach; spend divided by that delta is cost per net new reach. "you go to the very first day the ad account ever existed and you go up to March 2024 and you grab that reach number".
**The account, and the numbers are on screen.** An Australian female-only product with a stated addressable pool of 5.6M for ages 18-50, against 9M cumulative account reach. Cost per net new reach rose roughly 5x: "they used to reach new users for about 40 and now they're spending nearly $2 to reach a new user". The derived ratio he actually recommends is monthly new reach over monthly reach, which fell from 28% to 8%: "you can see for this brand, 16%, 25%, 28%, and then recently this is heavily declined down to 8%".
**⚠ ARITHMETIC FAILURE, and it is in the headline framing.** He says "the reach on the ad account right now is 9 million. And so we have reached effectively nearly double our TAM". **9 / 5.6 = 1.6x, not double.** He also states the same pool three different ways in one video, "approximately 5.6 million", "we know we have a TAM of about 5.5", and "our TAM is really like 5 million". Even against the smallest, 9/5 = 1.8x, still short. The saturation finding survives; the word "double" does not.
**⚠ SOURCE CONTRADICTION, and it is the third consecutive pass where re-reading an operator's corpus rather than our own claim produced the finding.** The April video opens by dismissing the metric: "In this video, I'll be running through the concept of rolling reach and why it kind of doesn't even matter." In September, on an account at exactly the saturation level he said it stops mattering at, net-new-reach cost is his primary evidence that creative diversity forces Meta cold. **Same metric, opposite status, five months apart.** His provenance story also changes, from "I got it from the marketing operators podcast" to crediting a different origin in September.
**Thresholds are T4 and unowned.** He is uncomfortable at 8% and also at 25%, with no evidence for either bound, and the 6% figure for the following months is explicitly an unrun estimate he flags as such.
Sources: Blue Sense Digital, Why Rolling Reach Doesnt Matter in eCommerce And What Actually Does, 2025-04-16; Blue Sense Digital, Cold vs Warm Tactics on Meta Google Ads with Caden, 2025-09-10
Last touched: 2026-08-27
'''

LS = r'''
### LS-072 · The multi-day conversion ramp operators call "learning phase" may be funnel fill plus time-to-purchase, not algorithmic learning
Tier: T4 · Status: active
A competing explanation for the single most-cited phenomenon in media buying, and it deserves a place precisely because it is cheap to state and nobody has separated the two.
Blue Sense, 2025-09-16: "This isn't a learning phase getting developed. This is simply the fact that all the people that you serve to on day one won't purchase instantaneously."
**The mechanism.** If time from first impression to purchase is distributed over days, then daily conversions on a newly launched campaign must ramp even if the delivery system learned nothing at all, because day three's conversions include day one's and day two's impressions maturing. The observed curve is the integral of a lag distribution, and it looks identical to a system improving.
**Why this is worth keeping despite being T4.** Every learning-phase claim in this topic rests on the same observed curve. **If two mechanisms predict the same curve, the curve is not evidence for either.** Separating them needs a cohort read, conversions attributed to their impression date rather than their conversion date, which no operator in this codex has published.
**The measurement discipline that follows, which is the practical half.** Decision cadence should be set by the business's actual time to purchase: "So this is time to purchase from first impression with the brand." On a 40-day window, January's spend does not fully mature until mid-March, so January's own CAC is meaningless, and his rule is to front-load changes into month one of a quarter and grade on quarterly CAC.
**Guards, and they are total. Every number in this file is hypothetical.** The 100 / 1,500 / 2,000 daily-customer series and the 100 / 90 / 94 CAC series are whiteboard illustrations with no account behind them. **NO ACCOUNT DATA IS SHOWN ANYWHERE.**
**⚠ Arithmetic slip.** He sets the window at 40 days, then says "It's going to take 45 days" for the second half of January while the dates he states, "Feb 24th through to the 11th of March", are computed off 40 days, not 45. The dates follow the original constant and the "45" is never corrected. Two smaller off-by-ones run the same direction.
Sources: Blue Sense Digital, Why You Shouldnt Measure Results Daily or Even Monthly in eCommerce, 2025-09-16
Last touched: 2026-08-27
'''

GA = r'''
### GA-064 · Raising target ROAS narrows the bid onto warm traffic and collapses prospecting into a self-feeding spiral
Tier: T3 · Status: active
The mechanism claim that explains a failure pattern most operators diagnose backwards. A Google specialist on Blue Sense's channel, 2025-09-10: "it causes prospecting to fall off and then it sort of eats itself into essentially what we call the death spiral".
**The lever runs the opposite way to intuition. To buy cold, drop the target hard:** "Instead of going to 300% maybe we'll be going down to 100% or 40%."
**The diagnostic is the useful part, because it catches the failure from inside the reports.** A high target makes a campaign look like it is buying cold in the search-term data while it is actually buying warm clicks, and the tell is a conversion rate that cold traffic cannot produce: "why is this campaign converting at 14% on cold traffic? It's like, well, it obviously isn't."
**The general heuristic he attaches, which is the same shape as the attribution work at [[Attribution & Incrementality#AT-104|AT-104]]:** "if it looks worse in platform, it might actually be better. And if it looks way better in platform, oh my god, something's probably broken."
**A related format claim:** product listing ads bias the system bottom-funnel and self-reinforce, and on audits their incremental ROAS on cold sits "70% 80% lower" than attributed, with "I've honestly like never seen them above a 1.5 rorowaz" on cold.
**Guards.** No account, no shown data, no test. The 70-80% incrementality gap is stated from audit memory with no study, no denominator and no methodology. Treat the mechanism as a strong hypothesis and the percentages as unbanked.
Sources: Blue Sense Digital, Cold vs Warm Tactics on Meta Google Ads with Caden, 2025-09-10
Last touched: 2026-08-27
'''

GP = r'''
### GP-042 · PMax's "new customer acquisition" setting is overridden by the conversion action, so it skews warm anyway
Tier: T3 · Status: active
A direct operating claim against a setting whose name promises the opposite. Google specialist on Blue Sense's channel, 2025-09-10: "the algorithm is going to prioritize the conversion action over the audience every single time."
**The consequence, with a frequency estimate attached.** Where other channels are also driving repeat purchases, PMax follows the conversion signal into the warm pool: "greater than 50% of the time performance max goes after repeat".
**The structural fix is the same one that appears at [[Attribution & Incrementality#AT-104|AT-104]]:** separate cold from branded and repeat at CAMPAIGN level rather than trusting an in-campaign audience toggle, "rather than having a Pmax that encapsulates branded key terms".
**Why this belongs next to [[Meta Delivery & Andromeda#MD-019|MD-019]] and law 1a.** It is the Google-side instance of the same pattern the Meta half of this codex has spent five passes on: an audience-labelled control that turns out to be a suggestion, or in this case a signal that loses to the optimisation event. **On both platforms, the conversion event beats the audience setting.** That is close to a cross-platform rule and it is worth testing as one.
**Guards.** T3, no account shown, no data. "Greater than 50% of the time" has no denominator and no measurement behind it. He does not say whether the setting was verified as enabled in the accounts he is describing.
Sources: Blue Sense Digital, Cold vs Warm Tactics on Meta Google Ads with Caden, 2025-09-10
Last touched: 2026-08-27
'''

MM = r'''
### MM-173 · MER is disqualified as a paid-media KPI once returning customers exceed ~20% of revenue, and Acquisition MER replaces it
Tier: T3 for the thresholds, T4 for the framework · Status: active
Blue Sense, 2025-05-09, on the metric he is best known for using: "we're talking total net revenue divided by total advertising spend inclusive of all paid media channels", and then "This is a terrible metric because it includes returning customer revenue."
**The failure mode is structural, not situational.** Returning-customer revenue sits in the numerator and paid media did not produce it, so MER improves when retention improves and reads as a media win.
**The thresholds, from audit experience rather than a study.** Above roughly 20% returning-customer revenue MER stops tracking paid media; above 60% it is purely a retention signal.
**The replacement:** Acquisition MER, new-customer net revenue divided by ad spend, on the principle that "the purpose of paid media spend is to drive new customer revenue, not total revenue". He gives two interchangeable reads, contribution margin three on a first-time-customer P&L and 30-day LTGP:CAC, with bands "If you're between a one to a two, you're in an okay not great position depending on your acquisition model and retention. And then two to three is an optimal zone."
**What MER is still for, and this is the part usually lost:** holding the P&L allocation stable. "It's a great metric for keeping your P&L in check, but not for saying whether we're doing a good job on paid media or not." Four-quarter accounting is credited to Common Thread Collective.
**One piece of arithmetic here CHECKS OUT and is worth carrying:** at 60% cost of delivery, break-even ROAS is 1/(1-0.60) = 2.5, which is exactly what he states.
**Guards.** The 20% and 60% thresholds, the LTGP:CAC bands and the "90% of businesses" figure are all asserted with nothing behind them. The 2.0/2.2/2.6/2.4 sequence is a whiteboard illustration, not an account.
Sources: Blue Sense Digital, MER Is A Terrible KPI for Marketing, 2025-05-09
Last touched: 2026-08-27

### MM-174 · The same operator held THREE different positions on existing-customer spend in eight months, and one of them is an on-record reversal
Tier: T3 · Status: contested
Recorded because [[Meta Delivery & Andromeda#MD-019|MD-019]] took its under-10% existing-customer threshold from this operator on 2026-08-26 and stated it as our line for all five accounts. **The threshold is not a settled position. It is one point on a swing.**
**April 2025:** "I'm a big proponent of not spending on existing customers on the platform. I cannot stress that enough."
**May 2025, an explicit reversal:** "I was wrong and we need to be more careful when thinking about exclusions on existing customers."
**November 2025, back again:** "90% plus of ad accounts and brands are spending way too much on bottom of funnel."
**The May file is the strongest of the three because it is the only one carrying account evidence, and the evidence is incomplete.** Heavy exclusions on one account produced "this has caused a slight reduction in daily revenue" and a steady decline in 7-day-click purchases. **NO NUMBER GIVEN for either.** A second account reopened Advantage+ "from 0% to 30% and 40% respectively to existing customers" from an April baseline of "attributed return on ad spend here was a 4.64". **The after figure is never stated.** A before-and-after case study with only the before.
He scopes his own reversal hard, "this only applies in sub 5% of circumstances", and the qualifying profile is an old brand with 60-70% of daily revenue from existing customers. **None of our five accounts is that profile, so the under-10% line at MD-019 probably still holds for us. It just holds on weaker ground than MD-019 implies.**
**A second inconsistency in the same corpus.** His retargeting frequency ceiling is 2 in November, "how incremental is it serving an ad to a user more than two times", and 5 in May, where his own budget calculator defaults to five impressions and he endorses it: "you're still going to hit all these people five times once a quarter. That's more than enough". He also puts paid media's share of returning-customer revenue at 10% and 20% within one file.
**The calculator itself is sound and reusable:** lapsed headcount x impressions x CPM. Every step recomputes correctly, 95,000 x 5 x $15 CPM = $7,125 against his stated "$7,000".
Sources: Blue Sense Digital, Meta Traffic Campaigns Destroys This Business, 2025-04-02; Blue Sense Digital, Heres Why You Need To Spend on Existing Customers, 2025-05-22; Blue Sense Digital, Why Youre Overspending on Retargeting How To Fix It, 2025-11-26
Last touched: 2026-08-27

### MM-175 · A case study titled "traffic campaigns destroyed this business" shows those months were the account's MOST profitable, and the author says so
Tier: T2 for the P&L, T3 for the thesis · Status: contested
Banked because the gap between a headline and its own evidence is exactly what this engine exists to catch, and because the operator catches it himself, on camera, which is rare enough to be worth preserving.
**The account.** Pre-agency "this business was spending $109,000 a month on paid media" at roughly 2.5 to 2.8 attributed ROAS. Under traffic campaigns, September spend fell to $75K at 1.6 attributed, and half of October ran $35K at 1.9. Returning to conversion campaigns in November: "they went back up to spending $97,000" at 3.64 headline, which he discounts to about 2.6 on 7-day click because "I am not a big fan of one day view through attribution".
**The finding that contradicts the title:** "these were the three most profitable months on this entire P&L that we're looking at", and he flags it explicitly, "Really counterintuitive to the title, the thumbnail of this video".
**His rescue is that profit came from the spend cut rather than the objective, and he cannot separate them, which he also concedes.** Two changes shipped at once, the traffic objective and heavy exclusions, and: "Now, was this necessarily due to heavy audience exclusions? It's hard to say", over "a six to eight weeks of murky data". **So this account cannot adjudicate traffic objectives at all.** His blanket position, "I've never seen a conclusive data set that has ever proven that traffic campaigns work", is unchanged by his own case study.
**The genuinely reusable finding is the spend-cut lag, and it is the one thing here with a mechanism:** "you can cut spend by 50 to 60% tomorrow and your revenue won't decline by 50 to 60%", because in-flight purchase journeys still land. **That is the same lag mechanism as [[Learning & Signal#LS-072|LS-072]], pointed the other way, and it means any month in which spend was cut will overstate efficiency.** That is very likely what produced the "most profitable months" here.
**Arithmetic and consistency failures.** He shows returning-customer revenue dropping in two consecutive $50K steps, then states the loss as "$50,000 in net revenue on returning customers"; the two are not reconciled. He describes the business as "500,000 in topline and 70% of that was returning customer revenue" and elsewhere as $614K first-time plus $600K returning, which is 49% returning on $1.2M. **The measurement lesson he draws is the right one:** the agency "wasn't tracking first-time customer P&L data and returning customer P&L data" separately, so nobody could defend or refute the strategy.
Sources: Blue Sense Digital, Meta Traffic Campaigns Destroys This Business, 2025-04-02
Last touched: 2026-08-27
'''

AU = r'''
### AU-080 · The CPC and CPA identities recompute correctly; the "expected action rate drives CPM" mechanism attached to them has nothing behind it
Tier: T4 for the mechanism, arithmetic verified for the identities · Status: active
Separated deliberately, because the sound half is doing credibility work for the unsound half.
**The identities, both stated and both correct on recompute.** "cpcs equal CPM / 1,000 / CTR", which at a $10 CPM and 2% CTR gives $0.50, exactly as he states. And CPA = CPC / CVR: "if you have a $1 CPC and you have a 2% conversion rate you'll end up with a $50 CPA". Correct. These are definitional and safe to use.
**The mechanism, which is not.** "the main predict of cpms is actually expected action rate", with ad quality folded into the same variable, and a feedback loop from the landing page: "as your conversion rate improves your CPM also drops simultaneously". **No documentation is cited anywhere in the file, and this operator reads no platform document in any of the six transcripts read this pass.** It is directionally consistent with [[Auction Mechanics & Bidding#AU-002|AU-002]]'s documented relevance-as-a-bid finding, which is why it is easy to accept without noticing that nothing supports this particular formulation.
**The diagnostic rule it produces is stated as an absolute and should not be:** "if your ctrs are greater than 1% has nothing to do with c GTRs it has everything to do with conversion rate", against a stated CTR floor of 1% and target of 1.5%.
**Useful context numbers, tiered T3 because they come from named client accounts.** Conversion rate anchors to price: a $50 product at 10.5% against a $2,000 product at 0.88%. He also notes Meta normalises the expected-action-rate premium to the vertical, so the 10.5% client does not get a $1 CPM.
**⚠ Several failures in the same file's illustrative numbers.** A $3 CPC at 2% CVR is $150 exactly, stated as "a $100 $150 CPA". 10.5% against 3% is 3.5x, stated as "3x lower". A CPA improvement from $150 to $50 is 66.7%, transcribed as "a 7% drop in your CPA". The last is probably a transcription artefact for 67%, and as written it understates the effect by a factor of ten.
Sources: Blue Sense Digital, How To Fix High CPCs on Meta Ads, 2025-03-18
Last touched: 2026-08-27

### AU-081 · Two industrial ad-ranking papers land the same week, both feeding CREATIVE CONTENT into the prediction model as a first-class input
Tier: T1 for the systems described, T4 as evidence about Meta · Status: active
arXiv cs.IR, both announced 2026-08-26, both from large e-commerce advertising platforms, neither from Meta. Banked as analogues, and the tier split is the whole point of the entry.
**2608.24091, Native Multimodal Representation Learning for CTR Prediction.** The premise is that multimodal representations of the ITEM, its imagery and text, are standard inputs to industrial CTR models, and the paper's contribution is training the multimodal encoder against the CTR objective rather than pre-training it separately. Its stated failure finding is the interesting half: naive end-to-end training does not help, because "user behaviors in raw CTR data are driven by both multimodal semantics and non-multimodal factors, leading to ambiguous supervision". Their fix mines the subset of clicks that are actually explainable by content.
**2608.24034, TAGR, live-streaming advertising.** Refreshes each ad's semantic ID as its live content changes, and reports "8.5%" and "7.4%" lifts on live-room entry and cart click with "a 16.1% revenue lift over the production baseline" in deployment.
**What these license and what they do not.** They corroborate that reading ad creative content into the ranking model is ordinary industrial practice, which is the general form of law 1. **They say nothing whatsoever about Meta's architecture, and must never be cited as if they do.** For Meta the only documentary basis remains [[Meta Delivery & Andromeda#MD-120|MD-120]] and [[Meta Delivery & Andromeda#MD-119|MD-119]].
**The genuinely transferable finding is the negative one, and it cuts against a lazy version of law 1.** A serious industrial team reports that content signal is entangled with non-content drivers strongly enough that training on raw click data produces ambiguous supervision. **So "the creative decides who sees it" is an oversimplification even in systems built to read creative.** That is a useful corrective to hold beside MD-001.
**Guard.** Read from the abstracts only, and 2608.24091's abstract is truncated in the feed before its results are stated, so no figure from that paper is banked. TAGR's lifts are the authors' own deployment claims with no independent replication.
Sources: arXiv 2608.24034 (TAGR), 2026-08-26; arXiv 2608.24091 (Native Multimodal Representation Learning for CTR Prediction), 2026-08-26
Last touched: 2026-08-27
'''

def append(fname, text):
    p = SCI / fname
    with io.open(p, 'a', encoding='utf-8') as f:
        f.write(text)
    print("appended ->", fname)

append('Attribution & Incrementality.md', AT)
append('Learning & Signal.md', LS)
append('Google Auction & Smart Bidding.md', GA)
append('Google PMax & Shopping.md', GP)
append('Marketing Math & Unit Economics.md', MM)
append('Auction Mechanics & Bidding.md', AU)
