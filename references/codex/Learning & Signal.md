---
title: "Learning & Signal"
type: codex-topic
claim_prefix: LS
created: 2026-08-18
tags: [advertising-science, codex]
---

# Learning & Signal

Learning phase, optimization events, signal quality, EMQ, and how feeding the system better signal changes delivery.

Part of the [[00-Codex|Advertising Science Codex]]. Claims follow the tier system (T1 docs, T2 shown test, T3 practitioner, T4 theory).

## Claims

## Learning phase mechanics

### LS-001 · Ad sets exit the learning phase after about 50 results in the week following the last significant edit
Tier: T1 · Status: contested
Meta states the delivery system never stops learning, but ad sets exit the learning phase as soon as they can deliver stably, usually after about 50 results in the week after the ad set's last significant edit. The Delivery column reads "Learning" during this period, and Ads Manager exposes a "Last significant edit" column plus a Results column so you can count results since the reset. Exception: Shops ads need a minimum of 17 purchases through the website plus 5 through Meta to complete learning. Multiple independent sources confirm the threshold and its consequences: Ben Heath adds that most lead-gen businesses fall short of 50 leads a week, so early-funnel friction should be minimized to feed conversion volume, and Dr. Matt Shiver adds that learning happens at the ad-set level and that wave-like performance (great days alternating with dead days) is usually a symptom of too few event fires at the ad set.
CONTESTED ON USE, NOT ON FACT. Blue Sense Digital does not dispute that the threshold exists or that Meta defines learning exit this way. He disputes using it to size test budgets, and names "setting budgets at the adset level based on the 50 conversions in a 7-day window rule" as one of four common mistakes below $50k/month spend. The arithmetic he walks through: back-propagating 50 conversions in 7 days at a $100 expected CPA gives $714/day for one concept ad set, so five to ten concurrent concept tests demand $3,500 to $7,000/day of test budget alone. His replacement formula is (target conversions x expected CPA) / test duration in days, so 20 conversions at a $100 expected CPA over 14 days = $143/day. The operator picks the significance threshold and the learning speed, then derives the daily budget, rather than inheriting Meta's number. Boundary: the learning-phase exit threshold stands as Meta documentation, its use as a budgeting input does not. Arithmetic worked on screen in both videos, no account test shown. His cruder verdict rule for the same decision is banked at [[Learning & Signal#LS-023|LS-023]].
Sources: Meta Business Help Center, About the learning phase, https://www.facebook.com/business/help/112167992830700; Ben Heath, Facebook Ads Just Changed Forever!, 2026-07-23; Dr. Matt Shiver, How the Facebook Ads Algorithm Actually Works (And How to Beat It), 2026-07-21; Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01; Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026 The Full System, 2026-06-15
Last touched: 2026-08-18

### LS-002 · Six edits always reset the learning phase: targeting, creative, optimization event, adding a new ad, pausing 7+ days, and bid strategy
Tier: T1 · Status: active
Only a "significant edit" causes re-entry into learning; every edit affects delivery but not every edit resets learning. The always-significant list is: any change to targeting, any change to ad creative, any change to optimization event, adding a new ad to the ad set, pausing the ad set for 7 days or longer (learning restarts on unpause), and changing bid strategy. With Advantage+ campaign budget, switching the campaign bid strategy can reset multiple ad sets at once.
Blue Sense Digital adds the operating asymmetry that follows from the "adding a new ad" trigger. If the ad set is off KPI, add ads, remove ads, do whatever, because the sequencing the algorithm learned is not working anyway. If the ad set is hitting KPI, do not inject new ads at all. Launch them as a separate ad set named for the same concept (his example: "concept one shoot two") so the account stays filterable by concept. He grounds it in breaking a working ad set himself years ago. Same principle as [[Meta Delivery & Andromeda#MD-011|MD-011]]. Practitioner rule, no test shown.
Sources: Meta Business Help Center, Significant edits and learning phase, https://www.facebook.com/business/help/316478108955072; Blue Sense Digital, Meta Ads Creative Strategy in 2026 The Full System, 2026-05-11
Last touched: 2026-08-18

### LS-003 · Budget, spending-limit, and bid/cost/ROAS-goal changes reset learning only if the change is large; Meta's example is $100 to $101 (no reset) versus $100 to $1,000 (likely reset)
Tier: T1 · Status: active
Three areas are magnitude-dependent: ad set spending limit amount; bid control, cost-per-result goal or ROAS goal amount; and budget amount. Meta's own example: raising budget from $100 to $101 "isn't likely" to reset learning, while $100 to $1,000 "may" reset one or more ad sets. Under Advantage+ campaign budget, adjusting the campaign budget can push multiple ad sets back into learning.
Sources: Meta Business Help Center, Significant edits and learning phase, https://www.facebook.com/business/help/316478108955072
Last touched: 2026-08-18

### LS-004 · Advantage+ campaign budget's normal redistribution between ad sets does NOT reset learning, and an ad-set-level significant edit does not reset sibling ad sets
Tier: T1 · Status: active
Meta's FAQ states: ad sets won't re-enter learning as CBO distributes budget; a significant edit made at the ad set level does not reset other ad sets in the campaign; adding a new ad set to an Advantage+ campaign budget campaign does not reset the existing ad sets; and initial learning takes the same time as with ad set budgets. Changing a social-issues/elections/politics disclaimer IS a significant edit.
Sources: Meta Business Help Center, Significant edits and learning phase, https://www.facebook.com/business/help/316478108955072
Last touched: 2026-08-18

### LS-005 · "Learning limited" is diagnosed when an ad set is unlikely to receive about 50 optimization events in the week after the last significant edit
Tier: T1 · Status: active
Meta says learning limited "isn't a penalty" but a signal that budget isn't being spent effectively because the system can't optimize with the current setup. Named causes: small audience, low budget, low bid or cost control, high auction overlap, an infrequent optimization event, or running too many ads at once. Fixes Meta lists: combine ad sets/campaigns, expand the audience, raise budget, raise bid/cost control, or switch to a more frequent optimization event (for example purchase to add-to-cart). It clears to Active once enough events accrue. Shops ads become learning limited if they lack 17 website + 5 Meta purchases after 7 days.
Sources: Meta Business Help Center, About learning limited, https://www.facebook.com/business/help/269269737396981
Last touched: 2026-08-18

### LS-006 · During learning, ad sets are less stable with usually higher CPA; do not edit during learning, and too many concurrent ads per dollar starves every ad
Tier: T1 · Status: active
Meta's best practices: wait to edit until out of learning because editing resets learning and delays optimization; avoid unnecessary edits; avoid high ad volumes because "the delivery system learns less about each ad and ad set" when there are many, and combining similar ad sets combines learnings; use realistic budgets since very small or inflated budgets give the system an inaccurate signal, and frequent budget changes can re-trigger learning. Meta also says not to try to avoid the learning phase entirely because it is necessary for optimization. Fraser Cottrell independently confirms the overload mechanism from agency practice: too many concurrent creatives spreads budget so thin that no ad accumulates enough spend, ads fail to leave the learning phase, and results look like creative failure when the cause is budget dilution, which is why his volume prescriptions scale with spend.
Sources: Meta Business Help Center, About the learning phase, https://www.facebook.com/business/help/112167992830700; Fraser Cottrell, Creative Volume | How Many Ads You Actually Need at Each Spend Level, 2026-08-02
Last touched: 2026-08-18

### LS-023 · Spend 3x target CPA before a concept verdict, 5x for a clean yes/no, and run the test about one week
Tier: T3 · Status: active
The spend threshold: at 3x target CPA, three or more conversions keep it running, two is a yellow light worth one more increment, zero or one is a cut. At 5x there is no yellow light, only a decision, which he prefers because early spend is the system learning who to target and efficiency improves once it has. The one-week duration is derived from two forces rather than tradition. Day-of-week seasonality means a test launched on a good day reads better regardless of the creative. A 3 to 4 day time-to-purchase means a one-day test kills the top-of-funnel ad while its influenced buyers convert later through other creative. Stated ranges: 3-4 days for a large stable business with short purchase cycles, 10-14 days for a small business with long cycles and heavy daily seasonality. This is the practical companion to the budget formula in [[Learning & Signal#LS-001|LS-001]]: the formula sizes the daily budget, this sizes the verdict. [[Scaling Models#SC-010|SC-010]]'s same-day kill is the emergency override, not the normal window. Agency practice, no test shown.
Sources: Blue Sense Digital, How To Structure A Meta Ads Account At Every Spend Tier In 2026, 2026-06-01
Last touched: 2026-08-18

### LS-024 · Incumbent ads decaying the day new ads launch on a fixed budget is cannibalization, not fatigue
Tier: T3 · Status: active
On a fixed budget a new ad can only take spend from ads that were already working, so every launch is a zero-sum reallocation. The incumbent decay operators read as fatigue is an accounting artefact of that reallocation, and the same split explains why the new ad also underperforms. Concrete diagnostic: if incumbent performance drops on the same day new ads go live with no budget change, that is cannibalization. The argument runs against launch-heavy testing cadences, since more launches on flat budget means more reallocation and no more reach. Asserted from managing over a million dollars a week, no data shown. A spend-share breakdown before and after a launch would test it directly. Read next to [[Meta Delivery & Andromeda#MD-006|MD-006]], which describes the same launch-day degradation from the delivery side (new ads served to the warmest audience first).
Sources: Professor Charley T, The BEST AD ON META after Andromeda, 2026-01-10
Last touched: 2026-08-18

### LS-025 · Learning accrues at all three levels at once: the ad learns who to reach, the ad set learns which ad to show, the campaign learns which ad set to fund
Tier: T4 · Status: active
Stated explicitly against practitioners who claim learning lives at one level only. It is the mechanistic argument under the consolidation doctrine: every pause discards purchased learning at whichever level it accrued, and every new campaign restarts all three from zero. Asserted mechanism, no documentation cited and no test. Filed as T4 because [[Scaling Models#SC-014|SC-014]] and [[Scaling Models#SC-012|SC-012]] lean on this assumption and the codex had no entry stating it directly. Note the conflict with the platform record: Meta's own documentation in [[Learning & Signal#LS-001|LS-001]] and [[Learning & Signal#LS-004|LS-004]] describes the learning phase at the ad set level, and says an ad-set-level significant edit does not reset sibling ad sets, which is hard to reconcile with campaign-level learning being a real stored quantity.
Sources: Professor Charley T, The BEST Facebook Ads Strategy for 2026 Post Andromeda, 2025-12-27
Last touched: 2026-08-18

## Optimization event choice and signal gating

### LS-007 · Optimize for the purchase event 99.9% of the time; add-to-cart or initiate-checkout optimization yields many of that event and few purchases
Tier: T3 · Status: active
Meta delivers exactly what you optimize for: add-to-cart optimization produces a lot of add-to-carts and few purchases; initiated-checkout optimization produces last-second drop-offs. Start with "maximize number of conversions" for signal volume; use "maximize value" when selling many differently-priced products. Prospecting starting budget: minimum 1x target CPA per day.
Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26
Last touched: 2026-08-18

### LS-008 · Whatever hits the results column IS the targeting: Meta finds more people like your converters, so only qualified conversions should fire the optimization event
Tier: T3 · Status: active
Post-Andromeda, Meta seeds its expansion from whoever registers in the results column for the optimized event; if unqualified people book or lead, the pixel trains toward more of them. Shiver's implementation for high-ticket lead gen: run the Leads objective but set the conversion event to a custom schedule (booked call) event so Meta optimizes for booked calls rather than raw leads, and fire the event only for qualified people. The fix for unqualified signal is friction: an application before the calendar page, or a pixel-conditioning question so only qualified respondents fire the event. Unqualified people still get the resource; the pixel just never sees them. This makes Meta's native "max number of qualified leads" setting unnecessary since the event itself is already qualification-filtered. Doctrine from claimed $1,000+/day own spend and 600+ consulted accounts; no controlled data shown. Ben Heath states the same law from the delivery side and names the failure mode plainly: Meta's optimization system is "very literal" and goes out and gets exactly what it was told to get, so advertisers who complain about lead quality told Meta to fetch leads rather than qualified leads. His fix is the same one, built with instant-form conditional logic (see [[Creative Science#CR-096|CR-096]]). Shiver restated it 2026-08-18 as "optimize for what you want more of": on a VSL application funnel he optimizes for the schedule (booked qualified call) event, never for leads, and manually rebooked leads go through a pixel-free calendar link so the event never double-fires.
Sources: Dr. Matt Shiver, How to Run Facebook Ads for Coaches & Agency Owners (FREE COURSE), 2026-08-04; Dr. Matt Shiver, How the Facebook Ads Algorithm Actually Works (And How to Beat It), 2026-07-21; Ben Heath, Learn 97% of Meta Ads in Under 29 Minutes, 2026-08-18; Dr. Matt Shiver, The BEST Way to Scale Facebook Ads in 2026, 2026-08-18
Last touched: 2026-08-18

### LS-009 · Default friction posture on lead funnels: volume-first versus qualified-signal-first
Tier: T3 · Status: contested
Ben Heath's sequencing rule: launch calendar-booking lead campaigns with ZERO qualification friction so conversion volume is maximized and Meta can learn; add qualification gates only after bookings consistently no-show or fail criteria (for example a minimum budget for his agency). Friction is a response to measured quality problems, never a default. Dr. Matt Shiver holds the opposite default: qualification friction (application step or pixel-conditioning question) belongs in the funnel from the start so only qualified people ever fire the optimization event, because the results column trains the targeting. Both positions are practitioner doctrine without side-by-side test data; Heath optimizes toward the ~50-events-per-week learning threshold, Shiver toward clean signal even at lower volume. Professor Charley T offers a third position, banked at [[Learning & Signal#LS-026|LS-026]]: optimize on whatever event clears learning and move the quality judgment up to creative selection, so neither the funnel nor the pixel carries the qualification job.
Sources: Ben Heath, Facebook Ads Just Changed Forever!, 2026-07-23; Dr. Matt Shiver, How the Facebook Ads Algorithm Actually Works (And How to Beat It), 2026-07-21
Last touched: 2026-08-18

### LS-010 · Value-based optimization at scale: adopt it versus never use it
Tier: T3 · Status: contested
Ben Heath: small budgets should optimize for simple max-conversions because sophisticated optimizations need data volume the small account lacks, but at roughly $100k/month spend switch ecommerce to value optimization (a $200 customer versus a $20 customer, which he says yields a much better overall ROAS) and switch lead-gen to CRM-fed conversion-leads with per-customer values so Meta optimizes toward high-value leads. Dr. Matt Shiver: never use max value bidding or Meta's newer "max number of qualified leads" goal (which requires CRM integration); instead the qualification lives in the funnel, so max-conversions on a qualification-gated event is already optimizing on clean signal. Contexts differ (Heath spans ecommerce and lead-gen at scale, Shiver runs high-ticket coaching funnels) but the recommendations directly conflict for lead-gen accounts.
Sources: Ben Heath, $100 vs $100,000 Facebook Ads Strategy, 2026-08-12; Dr. Matt Shiver, How to Run Facebook Ads for Coaches & Agency Owners (FREE COURSE), 2026-08-04
Last touched: 2026-08-18

### LS-011 · A two-step form (name/email first, qualifier question second) captures every lead but fires the pixel only for qualified answers
Tier: T3 · Status: active
Step one captures name and email so no lead is lost. Step two asks "which best describes you" (for example coach/agency doing $10K+/mo versus under $10K versus other) and the conversion pixel fires only for the qualified answer. Everyone still receives the lead magnet; the optimization signal stays clean. He shows his own live funnel built this way but no performance comparison data.
Sources: Dr. Matt Shiver, How the Facebook Ads Algorithm Actually Works (And How to Beat It), 2026-07-21
Last touched: 2026-08-18

### LS-012 · At $1,000+/day you can gate the pixel manually: review each booked call and send the conversion event back only for qualified applicants via CRM automation
Tier: T3 · Status: active
Booked calls drop into a GoHighLevel pipeline; an AI (Claude) enriches the applicant (website, socials) so the team can judge quality; moving the card to a "send pixel" stage triggers an automation that fires the conversion event. Two automations total: intake on booking, pixel-send on manual approval. Recommended only above roughly $1,000/day spend because it reduces event volume. His own live system with the pipeline shown on screen, but no before/after numbers.
Sources: Dr. Matt Shiver, How the Facebook Ads Algorithm Actually Works (And How to Beat It), 2026-07-21
Last touched: 2026-08-18

### LS-013 · An ungated schedule pixel can train on reschedulers: Shiver spent roughly $10,000 and lost it all because the pixel optimized for people likely to book multiple times and reschedule
Tier: T3 · Status: active
Without qualification friction, people who rescheduled and re-booked repeatedly hit the results column, so Meta sought more reschedule-prone bookers and ROAS collapsed. He cites losing roughly $10,000 of spend to this failure mode before adding the manual pixel gate. Real-spend anecdote with a dollar figure but no account data shown for it.
Sources: Dr. Matt Shiver, How the Facebook Ads Algorithm Actually Works (And How to Beat It), 2026-07-21
Last touched: 2026-08-18

### LS-014 · Cleaning tracking and attribution so the right data hits the platform let a coaching client scale from roughly $5k/mo to $20-30k/mo ad spend
Tier: T3 · Status: active
The client (Andrew) was spending roughly $5k/month on ads with poor pixel conditioning and messy attribution, getting sporadic applications. After Shiver's team rebuilt the backend tracking so qualified conversion data fed the platform, spend scaled to $20-30k/month and continues climbing. The claimed mechanism is the qualified-signal training loop of LS-008: Meta optimizes on whatever events it receives. Named ongoing client relationship with specific before/after spend levels stated verbally, no dashboards.
Sources: Dr. Matt Shiver, How to Actually Grow a YouTube Channel (he has 3.5M subs), 2026-08-06
Last touched: 2026-08-18

### LS-026 · Optimize on the event that clears learning, then judge creative on lead quality at a separate layer using three lead-quality custom conversions inside one campaign
Tier: T3 · Status: active
This splits a decision most operators fuse. The optimization event is picked for volume so delivery gets out of learning. The qualitative filter moves one level up to creative selection instead of starving the pixel. Implementation: build three custom conversion events for bad, good and great lead tiers inside ONE campaign, then read which ads bring which tier. His tiering uses a hard observable, the prospect's daily ad spend: under $200/day is not ready, $500+/day carries a stated 90%+ program success rate and roughly a 1-in-2 close, $1,000+/day roughly an 80% close. He reports a 60-70% overall call close rate and attributes it to only attracting the tiers likely to convert. Structural rule attached: different lead types do NOT get their own campaigns, for the same reason different products do not. This extends [[Learning & Signal#LS-008|LS-008]], which is binary qualified or unqualified, into a three-tier reporting layer rather than an optimization gate, and it is a third position in the [[Learning & Signal#LS-009|LS-009]] friction contest. Real tension to carry: LS-008 says only qualified conversions should ever fire the optimization event, this says fire whatever clears learning. Asserted doctrine from his own lead-gen spend, dashboard described but not shown.
Sources: Professor Charley T, The BEST Facebook Ads Strategy for 2026 Post Andromeda, 2025-12-27
Last touched: 2026-08-18

### LS-027 · When the money event cannot sustain learning, switch to a cheaper event whose dollar value you already know and arbitrage it
Tier: T3 · Status: active
Named live client at roughly $1,000/day, unable to get more than one ad set out of learning on purchases at a $200-300 CPA. That client buys email addresses at A$1.26 against an email worth A$4, so the campaign optimizes on emails and the arbitrage is measurable in dollars. He is explicit this is NOT the same move as optimizing for add-to-cart or view content, which are soft proxies for the same purchase and are exactly what [[Learning & Signal#LS-007|LS-007]] warns against. The difference is that the substitute event has its own independently known value. Two hard prerequisites: you must already know what the cheaper action is worth, and you must be able to make sales without ads before paying for a conversion campaign. [[Learning & Signal#LS-021|LS-021]]'s warning still binds, since a cheap-event audience is not a buyer audience unless the event carries real value. Client numbers stated verbally, no dashboard shown. Recorded in a joint session with Ben Heath, who argues the opposite default for small budgets.
Sources: Professor Charley T, How to CRUSH Facebook Ads with a Low Budget, 2026-02-28
Last touched: 2026-08-18

### LS-028 · Sales objective when the money event fires on your own site, Leads when a human step sits between the form and the payment
Tier: T3 · Status: active
The decision rule is about what the pixel can physically observe, not ticket size or industry. Ecommerce and self-serve software go Sales because the transaction registers on a site you control. Quote requests, booked calls and showroom visits go Leads because the actual conversion happens off-platform and is untrackable. This sits under [[Learning & Signal#LS-007|LS-007]] and [[Learning & Signal#LS-022|LS-022]], which choose the deepest trackable event but never state the objective fork itself. [[Learning & Signal#LS-029|LS-029]] is the escape hatch when the money event is off-site but you can pipe it back as a standard event. Asserted, no data shown.
Sources: Ben Heath, The BEST Instagram Ads Tutorial for Beginners in 2026, 2026-04-28
Last touched: 2026-08-18

## Signal capture and attribution settings

### LS-015 · Weak signal capture degrades delivery: Pixel alone under-reports post-ATT so Pixel plus Conversions API are both required, and missing conversions understate your estimated action rate
Tier: T3 · Status: active
Multiple independent sources agree on the mechanism. Ben Heath: without the Pixel, Meta "is advertising blind"; since Apple's ATT changes a lot of conversion data the Pixel would have captured gets missed, so CAPI must run alongside it, and both should be installed before the first ad launches. Blue Sense Digital quantifies the auction cost: track 70 of 100 real conversions and Meta prices you as a 2% converter when you're a 3% converter, because Pixel/CAPI conversions feed the EMQ score and the estimated action rate, degrading the whole bid equation. Caveat from Blue Sense: server-side tracking's incremental impact is essentially unmeasurable against week-to-week noise (he has tried causal-impact models; variance is too small for confidence), so buy it only if it fits the P&L and expect no visible lift. Setup path shown live 2026-08-18: Events Manager, Overview, the "you could lower your cost per result by connecting the Conversions API" prompt, Get started, "Set up with Meta", Connect now. Heath says the one-click flow leaves no excuse for running Pixel-only, and adds that at meaningful budget levels third-party tracking is worth adding on top; he names obsessing over data quality as one of the things that actually separates high-spend operators, because every downstream decision is made off that data.
Sources: Ben Heath, What You NEED To Know To Get Started With Facebook Ads, 2026-08-06; Blue Sense Digital, How The Meta Ads Algorithm Works in 2026, 2026-07-28; Ben Heath, Learn 97% of Meta Ads in Under 29 Minutes, 2026-08-18
Last touched: 2026-08-18

### LS-016 · Run the maximum attribution setting (7-day click, 1-day view, 1-day engaged view) to feed the campaign the most signal; read stricter windows in reporting
Tier: T3 · Status: contested
The attribution setting controls what conversions the optimization system learns from, so set it to the widest window and count "all conversions". Incremental, 1-day-click, and 7-day-click views remain available for analysis without starving the optimizer of signal. Settings rationale from practice; no experiment comparing windows shown.
CONTESTED. Blue Sense Digital changes the campaign setting itself to 7-day click plus 1-day engaged and strips 1-day view, on the grounds that this setting correlates far more tightly to P&L efficiency. He offers reporting-only comparison (Columns, Compare attribution settings, 7-day click) as the lesser fallback, not the preferred fix. Both sides agree 1-day view is worthless for reading results. The live disagreement is whether feeding view-throughs to the optimizer is worth the reporting distortion: signal maximisation against optimisation-target purity. Neither side showed a window-versus-window test.
Sources: Sam Piliero, The Only Facebook Ads Video You Need in 2026, 2026-07-26; Blue Sense Digital, The 1 Bottleneck I See in 80 of eCommerce Audits, 2026-05-18
Last touched: 2026-08-18

### LS-029 · An offline conversion piped Google Sheet to Zapier to a Meta STANDARD event is treated by delivery like a server-side online event, so you can optimize toward it
Tier: T3 · Status: active
For businesses that close over WhatsApp, payment links or a CRM there is no website purchase to fire, so the pixel has nothing real to learn from. The build: one Google Sheet row per closed customer (email, phone, first name, last name, city, state; partial rows are fine and more fields are better), a Zapier trigger on new row, mapped to a STANDARD event rather than a custom one, polling every minute. The account WAS shown on screen: optimizing on Submit Application with 3 and 2 events at $20 (broad retargeting) and $24 (broad) against a $70 allowable on $150/day. The sample is tiny, and the load-bearing part, that delivery cannot tell the piped offline event from an online one, is asserted rather than tested. Sits next to [[Learning & Signal#LS-012|LS-012]] as the upstream half: LS-012 filters which events fire, this creates the event in the first place. Also the escape hatch for the Leads-objective side of [[Learning & Signal#LS-028|LS-028]].
Sources: Professor Charley T, Record Profits the Meta Ads Andromeda Playbook, 2026-01-03
Last touched: 2026-08-18

### LS-030 · Pixel contamination is an order-of-magnitude question, not a binary; a few days of low-quality traffic events does not poison a pixel
Tier: T3 · Status: active
A guest's pixel took link-click and traffic-optimized campaign events after a friend ran campaigns into the same pixel. Lead quality collapsed and delivery went erratic, with a $10/day budget spending $3 all day then $12 at 1am. The guest cut to a fresh pixel, got WORSE results, reverted, and recovered. The rule offered is magnitude: contamination only matters when the bad events dwarf the good ones, a thousand bad orders against fifty real ones, not a handful of junk events against a working history. He also reframes the initial spike-then-slump after any change as the funnel clearing rather than damage. This is practitioner judgment on someone else's described account. Nothing was shown, no numbers beyond the daily budget. Read against [[Learning & Signal#LS-031|LS-031]], where a fresh pixel is credited with unlocking a new product. The two are reconcilable only because the mechanisms differ: junk events diluting a history versus a pixel trained hard on the wrong buyer.
Sources: Professor Charley T, Record Profits the Meta Ads Andromeda Playbook, 2026-01-03
Last touched: 2026-08-18

### LS-031 · Carve out a validation budget big enough to rule out marketing before killing a new product, and treat a clean pixel as the tiebreaker
Tier: T3 · Status: active
A mutual acquaintance launched a product alongside his hero product, it would not work, and it started printing money when relaunched on a separate pixel. Implied mechanism: a pixel already trained on the hero product's converters keeps steering delivery toward that buyer, so a genuinely different product never gets a clean audience read. Operator move: before killing a new SKU on product-market-fit grounds, confirm the spend was large enough to be a real test, then try a clean pixel or account as the tiebreaker. Weakest class of T3 evidence, secondhand with no numbers and no test, and it cuts against the consolidation doctrine in [[Scaling Models#SC-014|SC-014]] and [[Scaling Models#SC-016|SC-016]], so treat it as a diagnostic escape hatch for new-product launches rather than a default structure.
Sources: Andrew Faris, One Packaging Tweak 375K In Profit (Mehtab Bhogal), 2026-06-18
Last touched: 2026-08-18

### LS-032 · The Klaviyo-to-Meta audience segment sync breaks periodically and silently reclassifies existing customers as new
Tier: T3 · Status: active
Presented as a recurring failure his team actively monitors, not a one-off incident. The consequence is not cosmetic. Audience-segment breakdowns are the tool used to police existing-customer spend and frequency, so a broken sync means you spend on existing customers while believing they are new, and every downstream exclusion, cold-versus-warm split and incrementality read degrades with it. Operator action: verify in advertiser settings that audience segments are configured and flowing, on a recurring schedule, rather than treating audience setup as configure-once. [[Meta Delivery & Andromeda#MD-019|MD-019]] describes the setup this claim says quietly breaks. Asserted from agency practice, no data shown.
Sources: Blue Sense Digital, How to Scale an eCommerce Brand Profitably in 2026 The Full System, 2026-06-15
Last touched: 2026-08-18

## What the model learns from

### LS-017 · GEM trains on ad content plus user engagement from both ads and organic interactions, over billions of daily user-ad interactions with very sparse conversion signal
Tier: T1 · Status: active
Inputs are sequence features (long activity histories of ad/content clicks, views, interactions, up to thousands of events) and non-sequence features (user and ad attributes such as age, location, ad format, and creative representation). Meaningful signals like clicks and conversions are "very sparse" inside billions of daily interactions, which is why pixel/CAPI event volume matters to what the model can learn about an account.
Sources: Engineering at Meta, Meta's Generative Ads Model (GEM), https://engineering.fb.com/2025/11/10/ml-applications/metas-generative-ads-model-gem-the-central-brain-accelerating-ads-recommendation-ai-innovation/, 2025-11-10
Last touched: 2026-08-18

### LS-018 · Meta found that a diverse mix of user action types (views, clicks, conversions) trains better ranking models than homogeneous event sequences
Tier: T1 · Status: active
The post states "sequence diversity beats sequence homogeneity" and recommends a balanced mix of action types over homogeneous sequences as one of four scaling levers. For advertisers this is Meta saying the system learns from the full engagement ladder, not conversions alone.
Sources: Engineering at Meta, From User Sequences to Scaling Laws, https://engineering.fb.com/2026/08/05/ml-applications/from-user-sequences-to-scaling-laws-a-multi-stage-architecture-for-metas-ads-ranking/, 2026-08-05
Last touched: 2026-08-18

### LS-019 · Threshold rule: over 100 pixel fires for the optimized event, go fully broad; under 100, stack 2-3 lookalikes as Advantage+ suggestions, each needing a 100-person seed
Tier: T3 · Status: active
With 100+ historical events for the optimization event, broad targeting (controls only: minimum age, language, location) outperforms. Below 100 events, suggest 2-3 lookalikes built off clients and qualified calls (optionally clients who spent $1,000+ or $5,000+), each seed needing at least 100 people, left as suggestions under Advantage+ rather than hard limits. Stated as his agency's rule of thumb from client work; no comparative data shown.
Sources: Dr. Matt Shiver, How the Facebook Ads Algorithm Actually Works (And How to Beat It), 2026-07-21
Last touched: 2026-08-18

### LS-020 · Under lead optimization, Meta chases cheapest lead volume and can dump a large budget share into a cheap-but-low-quality demographic; the fix is a bid-down value rule, not exclusion
Tier: T3 · Status: active
Loomer reports Meta spending roughly 40% of his lead-gen budget on people over 65 because those leads are cheaper, while his own back-end data shows they rarely become paying customers. Meta only optimizes the count of the optimization event, not downstream quality it cannot see. He lowers the bid on 65+ via a value rule rather than excluding, so a small share still delivers there in a more natural distribution. Same logic applies to LTV: Meta optimizes the single purchase, so if women have higher lifetime value than men, Meta will still overspend on cheap male purchases unless you bid down the lower-LTV group (he prefers bidding down the less desirable group rather than up on the desirable one). Own account observation, no screenshots shown.
Sources: Jon Loomer, Ask These Questions Before Using Value Rules, 2026-08-12
Last touched: 2026-08-18

### LS-021 · Optimizing for top-of-funnel events (clicks, post engagement, video views) delivers to whoever performs that cheap action regardless of purchase likelihood
Tier: T3 · Status: active
With a click or video-view goal, Meta does not care whether those people ever buy; ads go to the people who make the chosen event happen cheapest. Broad-demo advice is therefore conditional on purchase optimization; under TOF goals a real demographic misallocation can occur, and even then the first step is to confirm the problem exists before intervening (with a bid-down value rule, not a restriction).
Sources: Jon Loomer, You May Be Surprised Who Converts, 2026-07-22
Last touched: 2026-08-18

### LS-022 · Choose the deepest funnel event that clears roughly 20-25 conversions per week; below that, step one event back up the funnel
Tier: T3 · Status: active
The selection rule for the optimization event is "the lowest one down the funnel that you have enough conversion volume for", walked down an example webinar ladder of registrant, attendee, call booked, purchaser. The stated thresholds: at 20-25+ purchases per week optimize on purchase; below that move one event up; at fewer than 20-25 booked calls per week do not optimize on booked calls; at fewer than 20-25 webinar attendees per week do not optimize on attendance. He also prefers value optimization over volume optimization for e-commerce once conversion volume supports it, on the grounds that $30 of spend earning a $200 sale beats $10 earning a $20 sale even though the cost per conversion looks worse, with the explicit caveat that a handful of conversions a week is not enough data for value optimization. Two tensions worth naming when applying this: the 20-25/week floor sits below the ~50-events-per-week learning threshold in [[Learning & Signal#LS-001|LS-001]], and it is a softer rule than [[Learning & Signal#LS-007|LS-007]]'s "optimize for purchase 99.9% of the time". Shiver's funnel-volume structure thresholds in [[Scaling Models#SC-015|SC-015]] are the closest independent numbers on file and are lower (3-10 events/day).
Sources: Ben Heath, Learn 97% of Meta Ads in Under 29 Minutes, 2026-08-18
Last touched: 2026-08-18

### LS-033 · Meta scores the post-click experience, so a cheap click into a bad landing page raises costs account-wide
Tier: T4 · Status: active
The claimed model: every ad is a web page inside Facebook and Instagram, the feed is a search results page, and Meta measures click-through rate, bounce, time on page and engagement after the click the way Google ranks results. The consequence he draws is that an ad driving cheap clicks into a bad landing experience is not a neutral waste, it is an account-level cost increase. He uses the same model to explain why some ads with high CPMs, heavy frequency and fatigue flags keep performing, on the grounds that Meta learned they create specific positive experiences for specific people. No platform documentation cited and no test run. Bank as a hypothesis that raises the priority of landing-page quality beyond its conversion-rate effect. Counterweight to carry: Meta's own published ranking inputs in [[Learning & Signal#LS-017|LS-017]] name ad content plus on-platform engagement sequences, not advertiser-site behaviour.
Sources: Professor Charley T, The NEW BEST Meta Ads Andromeda Course to Scale in 2026, 2026-01-24
Last touched: 2026-08-18

### LS-034 · Five ads produce 125 possible journey orderings, so a 50-ad account can never accumulate enough data to know what any single ad contributed
Tier: T4 · Status: active
Stated basis for capping ad count. Andromeda optimizes the ORDER ads are shown in, not individual ads, so the unit being learned is the sequence and the sequence space explodes with ad count. The 125 figure implies 5^3, five ads across a three-touch journey; the derivation is not shown and the "more grains of sand than in the universe" comparison for 50 ads is rhetorical. Treat the exact numbers as illustrative. The operating rule is the load-bearing part: run few enough ads that the sequence space stays learnable, which directly opposes the 50-to-100-ads-a-day school he names. Consistent with [[Meta Delivery & Andromeda#MD-009|MD-009]] (personalization is a delivery-sequence problem needing few distinct ads) and with Meta's own Nov 2024 sequence-learning update in [[Meta Delivery & Andromeda#MD-004|MD-004]]. Reasoning only, nothing shown.
Sources: Professor Charley T, The BEST AD ON META after Andromeda, 2026-01-10
Last touched: 2026-08-18

