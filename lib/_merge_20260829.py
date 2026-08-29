# -*- coding: utf-8 -*-
"""Codex amendments and new claims for the 2026-08-29 research pass."""
import pathlib, re

S = pathlib.Path(r'Obsidian God-level Marketing Vault/God-level Marketing/wiki/science')
TODAY = '2026-08-29'


def read(fn):
    return (S / fn).read_text(encoding='utf-8')


def write(fn, t):
    (S / fn).write_text(t, encoding='utf-8')


def amend(fn, cid, add_body=None, add_source=None, new_status=None):
    """Insert a paragraph into an existing claim, extend Sources, bump Last touched."""
    lines = read(fn).split('\n')
    start = None
    for i, l in enumerate(lines):
        if re.match(r'^### ' + re.escape(cid) + r'[ ·\-]', l):
            start = i
            break
    if start is None:
        raise SystemExit('claim not found: ' + cid + ' in ' + fn)
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith('### '):
            end = j
            break
    blk = lines[start:end]
    si = li = None
    for k, l in enumerate(blk):
        if l.startswith('Sources:'):
            si = k
        if l.startswith('Last touched:'):
            li = k
    if si is None or li is None:
        raise SystemExit('no Sources/Last touched in ' + cid)
    if new_status is not None:
        blk[1] = re.sub(r'Status: \w+', 'Status: ' + new_status, blk[1])
    if add_body:
        blk[si:si] = [add_body.strip()]
        si += 1
        li += 1
    if add_source:
        blk[si] = blk[si].rstrip() + '; ' + add_source
    blk[li] = 'Last touched: ' + TODAY
    lines[start:end] = blk
    write(fn, '\n'.join(lines))
    print('amended', cid)


def append_claim(fn, cid, title, tier, status, body, sources):
    """Append a brand new claim to the end of a topic file."""
    t = read(fn)
    if re.search(r'^### ' + re.escape(cid) + r'[ ·\-]', t, re.M):
        raise SystemExit('claim already exists: ' + cid)
    block = (
        '\n### ' + cid + ' · ' + title + '\n'
        'Tier: ' + tier + ' · Status: ' + status + '\n'
        + body.strip() + '\n'
        'Sources: ' + sources + '\n'
        'Last touched: ' + TODAY + '\n'
    )
    write(fn, t.rstrip('\n') + '\n' + block)
    print('added', cid)


# ---------------------------------------------------------------- watchlist

append_claim(
    'Meta Delivery & Andromeda.md', 'MD-149',
    'Meta is driving toward 90% of global ad revenue coming from VERIFIED advertisers by end-2026, up from 70% in 2025, and it is now demanding identity verification from 100% of financial-services advertisers in a named market',
    'T1', 'active',
    "Announced by Meta in a Polish-language Newsroom post on 2026-08-28. Two figures, both quoted from the source rather "
    "than paraphrased. The market-level rule: **\"weryfikacji będziemy wymagać od 100% reklamodawców usług finansowych "
    "kierujących reklamy do Polski\"**, that is, verification will be required from 100% of financial-services advertisers "
    "directing ads to Poland, expanding an existing process that previously fired only on suspicion. Completion is stated "
    "as within weeks of the announcement.\n"
    "**The transferable half is the global target attached to it:** \"do końca 2026 roku 90% przychodów reklamowych Mety na "
    "świecie pochodziło od zweryfikowanych reklamodawców – wobec 70% w 2025 roku\", by the end of 2026, 90% of Meta's "
    "worldwide advertising revenue should come from verified advertisers, against 70% in 2025. **A 20-point move in the "
    "share of revenue that must be identity-verified, inside sixteen months, is a structural change to who is allowed to "
    "buy inventory, not a regional compliance note.**\n"
    "What it does and does not say. It names one category (financial services) and one country, so nothing here states "
    "that a chiropractic or a truck-dealership account faces a new check. What it does state is the direction and the "
    "deadline, and the mechanism Meta is using to reach the 90% is category-plus-geography expansion of an existing "
    "identity check. **The operating consequence for us is preparatory rather than urgent: an account that cannot complete "
    "business verification is on a shrinking runway, and the cheapest time to have verified documents in order is before a "
    "category sweep reaches the account, not during one.** The post also describes AI fraud detection work in Poland, "
    "which is content moderation and carries no advertiser-facing rule.\n"
    "No prior claim in this codex covered advertiser verification at all, so this opens the topic rather than joining one.",
    'Meta Newsroom, Wzmacniamy w Polsce ochronę przed oszustwami, 2026-08-28')

append_claim(
    'Google Auction & Smart Bidding.md', 'GA-068',
    "Google's August 2026 Demand Gen drop ships messaging-app conversations, travel personalisation and generally-available multimodal video, and carries a vendor 30% conversion figure that sits directly against our own measured Demand Gen holdout",
    'T1', 'active',
    "Three product changes, from Google's own Ads & Commerce blog on 2026-08-27.\n"
    "**One, messaging-app conversations.** Google is \"testing new ways for viewers to start conversations with brands on "
    "messaging apps directly from Demand Gen ads on YouTube\". Stated as a test, not a launch. This is the first Demand Gen "
    "surface on file that produces a conversation rather than a click, which makes it the first version of the format that "
    "maps onto a lead-gen funnel at all.\n"
    "**Two, travel and hospitality personalisation.** Surfacing \"local activities, events, and real-time offers\" and "
    "personalising hotel ads by audience. Vertical-specific, no read-across for our book.\n"
    "**Three, multimodal video creation in Asset Studio is now generally available**, previously in testing. It produces "
    "\"horizontal and vertical assets in one workflow\" from the storyboarding stage, so one build covers every Demand Gen "
    "inventory type. This is the only one of the three that changes production economics rather than delivery.\n"
    "**The number, and why it must be quoted with its label attached.** Google states a \"30% average increase in "
    "conversions or conversion value\" for campaigns using Demand Gen improvements, sourced on the page as \"Google Internal "
    "Data, Global, H2 2025\". **That is a vendor aggregate over self-selected adopters with no control group, no holdout, "
    "and no methodology published. It is not a lift measurement and must never be repeated to a client as one.**\n"
    "**Read it against what this codex already measured.** [[Google Auction & Smart Bidding#GA-055|GA-055]] holds a 21-day "
    "Demand Gen geo holdout that produced no statistically relevant NEW-customer lift, 85 orders against the 166 required, "
    "while returning-customer orders rose 6.8%; [[Attribution & Incrementality#AT-072|AT-072]] holds the same test as the "
    "new-versus-returning split rule and [[Google PMax & Shopping#GP-040|GP-040]] holds the channel verdict. "
    "[[Google Auction & Smart Bidding#GA-056|GA-056]] holds the same operator's reading that Demand Gen harvests users "
    "already in the funnel. **The two are not strictly in contradiction, because they measure different things: Google is "
    "reporting attributed conversions across adopters, our banked test is reporting incremental new customers on one "
    "advertiser. They are, though, the exact pair a rep will use to argue for budget, so the honest position is that "
    "Google's 30% and our null result can both be true at once, and only the null one was measured against a counterfactual.** "
    "That same operator time-stamps his own verdict and tells viewers to check the publication date because Google keeps "
    "changing the product, which is the correct posture toward this entry too.",
    'Google Ads & Commerce Blog, Reach your audience in new ways with August’s Demand Gen Drop, 2026-08-27')

# ---------------------------------------------------------------- methodology

append_claim(
    'Attribution & Incrementality.md', 'AT-107',
    'A duplicated ad set NEVER performs like its twin, so an ad-set-level A/B is not a test, and the operator who ran one disowns his own 2-3x result because of it',
    'T3', 'active',
    "The strongest statement in the codex of why in-platform ad-set tests do not answer the questions we point them at, and "
    "it comes with the author killing his own finding.\n"
    "**The core mechanic.** Launch two ad sets with identical ads, identical audience, identical placements, identical "
    "budget, and change nothing at all: \"those two ad sets will perform wildly different. It will always be the case. You "
    "will never have a duplicated ad set perform consistently with its adjacent ad set.\" They optimise differently, serve "
    "to different people, and the environmental conditions of whoever gets served change continuously. Duplicate one ad set "
    "many times and \"some will perform terrible, some will perform incredible. It's just random.\" **The consequence is "
    "that any single-pair ad-set test has a noise floor nobody has measured, so a difference between the cells cannot be "
    "attributed to the variable that was changed.**\n"
    "**The disowned result, recorded because the discipline is the point.** He ran 7-day click against 7-day click plus "
    "1-day view as the optimisation setting, measured on a consistent attribution model, and the 7-day-click-1-day-view ad "
    "set **outperformed by about 2 to 3x**. He then refuses to bank it: \"how do we know that that natural random noise "
    "that exists within duplications of identical ad sets isn't just presenting itself here and giving us a biased read? We "
    "don't. Therefore, it's not helpful.\" He names both theoretical directions as equally arguable, more attributed data "
    "helping the model, or view-through conversions dragging optimisation toward warm audiences who were going to buy "
    "anyway, and concludes nobody has resolved it. **Do not quote the 2-3x. It is in this entry so that nobody re-extracts "
    "it later from the same video as a finding.**\n"
    "**What he says a real test needs, in order.** Use Meta's own A/B experiment tool, whose single real value he says is "
    "that it guarantees ad set A and ad set B do not target the same people. Raise the sample size to at least 10 or 20 "
    "runs across multiple accounts and pool them. Even then it is not causation, which needs a controlled geo-lift, ideally "
    "multi-cell across states whose revenue tracks each other, reading incremental revenue lift or incremental CPA between "
    "the regions. This is the same ladder as "
    "[[Attribution & Incrementality#AT-022|AT-022]], stated from the failure end.\n"
    "**The one-change-at-a-time reversion method, shown working on a real account.** A client made three changes in one "
    "week: cross-sells at checkout, new site offers, and an account restructure. Average order value rose 2% and conversion "
    "rate **halved, from 4% to 2%**. The team guessed the offers, killed them, and conversion rate did not move. Guessed "
    "the restructure, reverted it, and conversion rate did not move. Removed the checkout cross-sells and conversion rate "
    "**immediately returned to 4%**. **The cross-sells, the change credited with the AOV win, were the thing destroying the "
    "conversion rate.** The method that found it was serial reversion, not analysis.\n"
    "**Endogeneity, which is the version of this that bites us on seasonality.** Ad spend affects revenue, and expected "
    "revenue also decides how much you spend, so \"ad spend is often endogenous to revenue due to seasonality, which makes "
    "any kind of naive attribution analysis just misleading.\" You spend more in November because you know November is big. "
    "The relationship is bidirectional, and a chart of spend against revenue cannot tell you which direction is operating.\n"
    "**The organisational failure mode he names is the reason this claim matters more than the mechanics.** A correlation "
    "read once inside an account becomes a story, the story is shared internally, and the agency then rolls out standard "
    "operating procedures across a client portfolio on the strength of it. Asserted from agency practice with one shown "
    "client sequence; no distribution of duplicated-ad-set outcomes has ever been published by anyone, which is itself the "
    "gap.",
    'Blue Sense Digital, You Are Getting This Wrong., 2025-05-23')

append_claim(
    'Attribution & Incrementality.md', 'AT-108',
    'A multi-store retailer’s "new customer" count is wrong by construction until offline retail data is joined to it, and the fix changes CAC, the P&L and which campaigns get funded',
    'T3', 'active',
    "Shown case, Blue Illusion, an Australian fashion retailer with 100-plus stores, first six months of the engagement.\n"
    "**The measurement defect.** A shopper who bought in store and later buys online is not in the ecommerce database, so "
    "the online platform registers them as a new customer. They are not. For a retailer at eight or nine figures with a "
    "large store estate this silently inflates new-customer counts, which deflates measured CAC and makes acquisition look "
    "healthier than it is. The fix was joining the client's existing offline customer data to the online record so a prior "
    "in-store purchaser is excluded from the new-customer count. **That joined figure then becomes the denominator for CAC "
    "and the basis of the new-customer P&L.** The same offline data was also pushed back into campaign exclusions so "
    "prospecting stops paying to reach existing customers.\n"
    "**The KPI change that went with it.** Off blended MER (total spend against total revenue) and onto acquisition MER "
    "(new-customer revenue against new-customer spend) plus new-customer profit contribution, reviewed weekly with the "
    "client. This is [[Marketing Math & Unit Economics#MM-066|MM-066]] applied, and the offline join is what makes the "
    "numerator honest.\n"
    "**The incrementality method, which is unusual and worth carrying.** Geo-lift experiments run around **clusters of "
    "physical stores**, reading two outcomes at once: online revenue lift in those areas, and store lift in the same areas "
    "measured on foot traffic and in-store new-customer sales. That is the omnichannel answer to the blindness recorded at "
    "[[Attribution & Incrementality#AT-048|AT-048]]. He states the limit himself: you cannot run many geo-lifts "
    "synchronously, so the KPI layer above has to carry the weeks when no experiment is live.\n"
    "**Results, quoted with the framing he insists on.** He reports YEAR-ON-YEAR growth RATES rather than raw period growth, "
    "and says why: onboarding a brand in February and riding the seasonality curve while claiming the growth is the "
    "standard case-study dishonesty. On Google, new-customer growth ran 2 to 3% year-on-year from December to February, then "
    "130% in March and 89% in April. On Meta, new-customer attributed sales on 7-day click only were running -25 to -30% "
    "year-on-year and were taken to 0%, which he presents as a 36% improvement in the growth rate rather than as growth, "
    "then 50% year-on-year in April. By August the business recorded its all-time-high month for online new-customer "
    "acquisition, beating a November Black Friday peak. A separate site change prioritising full-price over discounted "
    "items, combined with merchandising and pricing work he does not claim sole credit for, accompanied a 59% rise in gross "
    "profit.\n"
    "**Two honesty notes.** He withholds the y-axis on the new-customer chart and does not name the specific site "
    "mechanic, so the shape is shown and the magnitudes are not. And this is a vendor case study about a vendor's own "
    "client, which is exactly the class of evidence [[Attribution & Incrementality#AT-107|AT-107]] warns about. What "
    "survives that discount is the method, not the percentages: **the new-customer count is a measurement you have to build, "
    "and on any client with a physical location it is wrong until you build it.**",
    'Blue Sense Digital, Blue Illusion x Blue Sense: How We Achieved Record New-Customer Growth, 2025-10-27')

# ---------------------------------------------------------------- creative

append_claim(
    'Creative Science.md', 'CR-199',
    'Test creative in the BAD months, because in a good month roughly half your ads look like winners and the false winners corrupt the next round of iteration',
    'T3', 'active',
    "The cleanest statement on file of why a testing calendar should be inverted relative to a spending calendar.\n"
    "**The mechanic, in his words.** \"Your top 20% winners will win all the time. Like they will always win. In good "
    "months like 50% of your ads will win. And so you get this artificial inflation in ads that actually won't perform in a "
    "colder market ... So you kind of get your best, cleanest data signals in really bad months.\" **The damage is not the "
    "wasted spend on a false winner. It is the feedback loop: a false winner gets iterated on, and the next round of "
    "creative is built off a message that never worked.** He states that consequence directly, \"which actually builds a "
    "worse feedback loop for future creative iteration\".\n"
    "**The operating conclusion:** Q1 is the period to load creative volume into, because winners still surface in a bad "
    "month and they surface honestly, and then you scale them into the good month. The mirror rule is that they run **no "
    "evergreen testing during Black Friday**, because the budget is committed and the correct move in that window is to run "
    "content that was already proven: \"that's the time where we're taking all the content we've already tested. Why would "
    "we test evergreen content during that time?\"\n"
    "**Three independent supports, which is what lifts this above one operator's preference.** The same operator reaches "
    "the same conclusion from a completely different direction in [[Creative Science#CR-200|CR-200]], where Q1 performance "
    "at ad level is proposed as the proxy for how an ad will perform in a cold market with no brand presence. Charley T "
    "arrives there from the structure side in [[Scaling Models#SC-058|SC-058]], moving from CBO in Q4 back to ABO in Q1 "
    "precisely because \"conversion rates are no longer artificially inflated so tests read honestly\". And "
    "[[Marketing Math & Unit Economics#MM-097|MM-097]] already banks the same window for OFFER testing. **Four entries, two "
    "operators, one underlying claim: a depressed baseline is a measurement instrument, not a problem to survive.**\n"
    "**What is missing.** Nobody has published the win-rate distribution by month that would turn \"50% in good months\" "
    "into a number. Treat the 50% as an illustration of the direction, not a figure to plan against.\n"
    "**The annual-planning frame this sits inside, from the same conversation:** build the forecast first, decide "
    "what share of media spend goes to content production, plan product launches and manufactured revenue moments, and set "
    "per-month test themes off historical seasonality. A geographic expansion inverts that calendar completely, since "
    "summer messaging, local pain points and the holiday set all flip.",
    'Blue Sense Digital, Here’s What You Should Be Focusing On in 2026, 2025-10-28')

append_claim(
    'Creative Science.md', 'CR-200',
    'Home-market ad results are inflated by existing brand presence, so winners do not travel, and a 10 ROAS ad can be a 2 in a market that has never heard of you',
    'T3', 'active',
    "**The claim this entry was reserved for.** Referenced from "
    "[[Attribution & Incrementality#AT-009|the attribution-error-tracks-brand-presence rule]] before it existed; written "
    "here on 2026-08-29 from the source read in full.\n"
    "**The observation.** A brand at $5M-plus online takes its one to ten proven Meta ads into the US and watches a 10 "
    "ROAS become a 2. The operator's verdict is blunt: the cause \"has nothing to do with the ad ... nothing to do with the "
    "landing page, the offer, the nuances of the market\". He names the standard explanation as a sales motion, \"the US is "
    "a very different market, you need a local agency\", and rejects it for the big English-speaking markets: \"UK, "
    "Australia, US, Canada, etc., all of these regions respond to ads very, very similarly.\"\n"
    "**The mechanism.** Existing brand presence does the work the creative is being credited with. \"So many people know "
    "about you in your primary market that you can really throw any ad into the account and it's going to do decent because "
    "people have heard of you before.\" Move the same ad somewhere with no presence and \"it performs like it should as an "
    "okay ad\". **So the home-market number is not a measure of the ad. It is a measure of the ad plus years of brand "
    "building, and the two are only separable by moving the ad.**\n"
    "**He runs the test on his own agency, which is the most useful part.** Their own ads launched into the US or UK "
    "\"perform half as well\" and their **cost per qualified booked call doubles**. His account of why is recognition: in "
    "Australia a viewer thinks \"oh, those guys, Blue Sense, I think I've seen a YouTube video from them\" and clicks; in "
    "the UK or US, \"I have no idea who these guys are. I'm definitely not clicking.\" **That is a lead-gen number, not an "
    "ecommerce one, which is why it transfers to our book: brand presence is worth a 2x on cost per qualified call.**\n"
    "**The stress test, and it is free.** Q1 performance at ad level is his proxy for cold-market performance, because "
    "market sentiment is depressed and only genuinely good ads clear. Run the testing programme through Q1 and the "
    "surviving winners are the ones that will travel. His volume illustration: a brand spending $100k/month planning 130 "
    "new ads a month should push to about 160, and three months of that yields roughly **7 genuinely high-performing "
    "winners**, enough to open a US launch at around $100k/month. Run the identical programme in Q2 and you get about **15 "
    "\"winners\" of which more than half are not**, so you translate false positives and buy a wrong read on the launch. "
    "The common real-world case is worse on both axes, far less volume tested in the easy quarter, so what looks like eight "
    "winners at a 10 ROAS is really about two at a 3.5. **These figures are illustrative arithmetic spoken over a "
    "whiteboard, not measured outcomes. The ranking is the finding; the numbers are not evidence.**\n"
    "**Three secondary causes he ranks below this one, having put this one at roughly 80% of cases.** Region-specific "
    "conversion work, because the landing page has to read as a local business or the buyer prices in tariffs, long "
    "shipping and international returns. Full replication of the lifecycle setup, since he has seen launches run 20% under "
    "where they should because basics like abandoned-cart flows were never rebuilt, \"a thousand golden BBs, not one silver "
    "bullet\". And SKU prioritisation, where launching two of five winning products, or going out of stock on key sizes, "
    "suppresses the whole market.\n"
    "**The forward claim, stated without evidence and worth testing rather than believing:** \"a really high performing ad "
    "will scale into every other region effectively ... you can go and run that thing worldwide and it works like almost "
    "everywhere.\" Read with [[Creative Science#CR-199|CR-199]], which is the same Q1 argument reached from the creative "
    "feedback-loop side.",
    'Blue Sense Digital, Why eCommerce Brands Fail To Launch Into The USA, 2025-11-21')

append_claim(
    'Creative Science.md', 'CR-201',
    'When lead volume stalls the leak is usually after the click, and the diagnostic order is message match, mobile form rendering, creative intent, form length, trust placement, then segmented retargeting, with the leak VERIFIED on session recordings before anything is rebuilt',
    'T3', 'active',
    "A Google-side lead-gen agency's standing ladder, stated for home-services style local businesses, which is our book. "
    "The framing is the useful part: \"ads do their job, they get attention, they get clicks, and the traffic looks decent. "
    "Then lead volume feels stuck. And everyone wants to overhaul targeting. Most of the time, the conversion is getting "
    "lost after the click.\"\n"
    "**He refuses form fills as the objective in the same breath, which matters for how we report:** \"form fills alone can "
    "be very misleading. What we really want is qualified leads and real opportunities, not just volume.\"\n"
    "**The order.**\n"
    "1. **Message match.** The page must confirm the exact next step the ad promised. His worked line: if the ad says get a "
    "free estimate for bathroom remodelling, the page confirms that specific step immediately, and reads as a continuation "
    "rather than a new conversation.\n"
    "2. **Mobile rendering of the form itself**, which he treats as a distinct failure from page speed. Serving a desktop "
    "layout to a phone \"takes twice the amount of time to fill out the form\" and forces zooming to find fields and "
    "scrolling to find the call to action.\n"
    "3. **Creative as an intent filter.** Creative that is too broad or aimed at the wrong pain point still buys traffic, "
    "and the page is then trying to convert people who were never close to submitting. His example is deliberately "
    "unresolved: for bathroom remodelling, sometimes a before-and-after angle pulls the higher intent and sometimes a "
    "plain \"here's the process and this is what you get\" angle converts better because it sets expectations. **He gives no "
    "rule, which is the honest answer.** The ecommerce twin of this from the same source is sharper because it was "
    "measured on an account: a women's vitamins brand ran men in the creative, generated clicks and impressions from men, "
    "and swapping the imagery to women lifted conversion rate and click-through rate \"almost immediately\". No figures "
    "given.\n"
    "4. **Form length, treated like an ecommerce checkout.** \"The most common issue is asking for too much too soon.\" "
    "Scale the ask to the offer: lightweight for an early-stage offer, more permissible for something high-value like an "
    "in-home estimate, \"as long as it feels reasonable and the benefit is clear\".\n"
    "5. **Trust placed where hesitation happens**, meaning reviews, testimonials and a clear statement of what happens "
    "after submission, positioned next to the form and the main call to action rather than elsewhere on the page. His "
    "reason is category-specific and correct for home services: the buyer is letting a team into their home, so the anxiety "
    "is about communication, professionalism and follow-through, and the proof has to answer that specific anxiety.\n"
    "6. **Retargeting segmented by behaviour, never one message to everyone.** Early visitors need clarity and "
    "credibility; higher-intent visitors need a straightforward next step and fewer unknowns.\n"
    "**Then, and only then, the delivery-side cleanup:** find which placements and segments actually produce the leads you "
    "want and stop funding the ones that look busy without producing opportunities.\n"
    "**The gate on all of it.** \"Verify the leak before you change anything.\" He uses Microsoft Clarity heat maps and "
    "session recordings to see where people stop scrolling, where they get stuck, and which fields trigger abandonment. The "
    "ecommerce reading of the same tool is the more portable heuristic: **not scrolling means the value proposition is not "
    "landing or the page is not clear; scrolling everywhere and tapping randomly means the path is not obvious.**\n"
    "**Where this sits against our own standing rule.** It independently supports the position that a lead form's job is to "
    "qualify and capture contact rather than to carry the whole intake, since every item on his list makes the form shorter "
    "or the promise clearer. Asserted from agency practice across a client book, no test shown, no conversion-rate figures "
    "attached to any of the six levers.",
    'Solutions 8, Conversion Challenges Solved: Elevate Your Lead Generation Impact, 2026-01-16; Solutions 8, Maximize E-commerce Conversions: Techniques for Post-Click Ad Success, 2026-01-15')

# ---------------------------------------------------------------- scaling

append_claim(
    'Scaling Models.md', 'SC-151',
    'Every PRODUCT has a maximum profitable daily spend the same way every ad does, and past that ceiling the only growth axis is a second product, never more creative and never a new agency',
    'T3', 'active',
    "**The claim this entry was reserved for.** Referenced from [[Meta Delivery & Andromeda#MD-137|MD-137]] before it "
    "existed; written here on 2026-08-29 from the source read in full.\n"
    "**The ceiling, stated at product level.** \"There is a limit to how many standup desks you can sell to the Australian "
    "population.\" The addressable market for a product bought direct-to-consumer through paid media alone is much smaller "
    "than any market-size figure suggests, and for a genuinely niched product, which is where he says most of his "
    "profitable clients sit, the cap can be as low as a few thousand dollars a day. **What makes it a ceiling rather than a "
    "target is the list of things that do not move it:** \"no matter what you do, whether it's you go on ramp creative "
    "testing up to thousands of ads a month, you go and test a bunch of different angles, you're using five different "
    "agencies ... there will be a limit on how much you can spend profitably within this particular product.\"\n"
    "**The curve underneath it.** Efficiency against spend declines logarithmically. The job is to find the spend level "
    "that maximises profit contribution, and then to look for changes that shift the curve right so the maximum sits at a "
    "higher spend. That is the same shape as the per-ad ceiling in [[Meta Delivery & Andromeda#MD-137|MD-137]], where an ad "
    "holds $1,000 a day, $100 a day or $40 a day and the account's honest total is the sum of what its ads can hold.\n"
    "**The failure mode, and it is the one a client puts us in.** A single-product brand with a revenue target keeps "
    "pushing spend past the maximum and \"you just push negative profit contribution into the P&L and you make less money\". "
    "The visible symptom is agency churn: \"let's just jump from agency to agency to agency to try to solve this problem, "
    "someone surely can figure out why we can't spend more\". **He rates that a bad use of the founder's time explicitly: "
    "\"I don't think the best exercise is for you to just go to a different agency every 3 months and see who can get your "
    "spend from $2,000 a day to 2.5.\"** The alternative he argues for is holding the first product at its profitable "
    "maximum and launching a second that can carry its own load, which doubles the business without touching the first "
    "product's efficiency.\n"
    "**Second-order benefits he claims for the second product:** it is almost a separate business with its own ceiling, and "
    "cross-sell raises lifetime value on the original, improving 90-day lift and possibly letting the original hold "
    "slightly more spend than it could alone.\n"
    "**The structural evidence he offers.** Most of the largest Australian direct-to-consumer brands by revenue are "
    "fashion, and his explanation is portfolio width rather than category magic: 100-plus products turning over every two "
    "to three weeks, each holding a little spend. A fashion brand at $100,000 a month spends about $3,300 a day, which "
    "across 100 products is roughly **$30 a day each**. *He says $300 first and corrects himself to $30 on camera; the "
    "corrected figure is the right one.* Pareto still applies inside that, 20% of products taking 80% of spend.\n"
    "**Two numbers and one honest gap.** He puts the ad hit rate at about **15%, seven unique ads launched for one that "
    "works and scales**, and says 20% is roughly the ceiling on that rate. On product-launch hit rate he refuses to give a "
    "figure: \"I don't have a direct percentage on a large set of data ... it's not 100%, it's probably not even 50%\", and "
    "attributes the variance to founder skill. **Recording the refusal matters, because the whole argument rests on "
    "launching more products and he cannot tell you how often that works.**\n"
    "**Why this is in our codex at all, given we run local service businesses.** [[Meta Delivery & Andromeda#MD-137|MD-137]] "
    "already draws the translation: on a client with one service there is no second product to launch, so the horizontal "
    "axis is a second OFFER. The per-ad, per-product and per-offer ceilings are one claim stated at three altitudes by one "
    "operator, and none of the three has been measured. Asserted throughout, no dataset shown.",
    'Blue Sense Digital, The Two Highest ROI Activities for an eCommerce Founder, 2025-01-29')

# ---------------------------------------------------------------- marketing math

append_claim(
    'Marketing Math & Unit Economics.md', 'MM-184',
    'Never allocate operating expenses, and never allocate the agency fee, into a split first-time-customer P&L: it is wrong as accounting and it changes what the media buyer does',
    'T3', 'active',
    "**The structure first, because the rest depends on it.** Net revenue, minus cost of delivery, gives gross profit. "
    "Gross profit minus direct advertising and marketing gives contribution profit, which he also calls contribution "
    "margin 3. Contribution profit minus operating expenses gives EBITDA. That P&L can then be split into a first-time-"
    "customer P&L and a returning-customer P&L, with identical structure on both sides.\n"
    "**The rule: the split stops at profit contribution.** Operating expenses cannot be allocated across a conceptual "
    "split. You could apportion a marketing manager's salary 70/30 on revenue share, but \"it's just not really a "
    "productive exercise\", and EBITDA on a conceptual split P&L is not a meaningful number. What you want instead is a "
    "profit contribution figure on each side, whose **sum** should exceed total operating expenses.\n"
    "**Why the agency fee specifically must not go into the first-time-customer side.** If the buyer is scored on "
    "new-customer profit contribution minus their own fee, that becomes the only number that matters, and two things break.\n"
    "**One, incentives.** There is then zero reason to move any budget to returning customers even where that shift makes "
    "the business more money, which he sizes as an edge case affecting roughly 10% of brands, typically those with high "
    "product-drop cadence or a demographic that repeat-buys through paid media.\n"
    "**Two, and this is the bigger one, it hides scaling decisions that are correct.** His worked case, arithmetic intact. "
    "$40,000 of Meta spend buys 800 new customers at a $250 average order value, so $200,000 of new-customer revenue; at "
    "60% gross margin less the ad spend that is **$80,000 of new-customer profit contribution**. Double spend to $80,000 "
    "and blended CAC rises 50%, from $50 to $75, giving 1,066 customers and $266,000 of revenue, and **profit contribution "
    "does not move**. On a fashion-style 45% cumulative gross-profit lift by day 365, the first cohort goes on to "
    "contribute about **$54,000** and the second about **$72,000**, a delta of roughly **$18,000 a month** which compounds "
    "toward a quarter of a million over the year. **The aggressive scenario is substantially better and is invisible in the "
    "KPI the fee was attached to.** He states the caveat himself: the incremental customers arrive at roughly break-even on "
    "first purchase, so the business is deliberately floating profit contribution to collect it later, and that is a "
    "financing decision the owner has to actually want. He then runs the more realistic CPG version, $80,000 spend at a "
    "$130 CAC producing $150,000 of new-customer revenue and only $12,000 of profit contribution, where doubling spend "
    "takes profit contribution to zero.\n"
    "**The mechanism he names is \"what's measured is managed\"**, and the accounting objection underneath it is that the "
    "first-time-customer P&L causes the returning-customer P&L: \"this is the chicken and this is the egg\". Load all opex "
    "onto acquisition and acquisition looks unprofitable while retention looks excellent, and the business starts "
    "defunding the thing that creates the other. He points out the rig works both ways: reclassify 30% of spend as "
    "retargeting into the returning P&L and acquisition suddenly looks superb.\n"
    "**Read against** [[Marketing Math & Unit Economics#MM-066|MM-066]] on KPIing paid media at acquisition MER, and "
    "[[Marketing Math & Unit Economics#MM-002|MM-002]] on why the LTGP:CAC numerator has to be stated out loud. Asserted "
    "with worked spreadsheet arithmetic; no account named and no before-and-after shown.",
    'Blue Sense Digital, Where To Allocate Agency Fees On The P&L, 2025-06-10')

append_claim(
    'Marketing Math & Unit Economics.md', 'MM-185',
    'A paid media agency is worth a 10 to 30% efficiency delta, not a growth engine, and the operator making the argument runs one',
    'T3', 'active',
    "The most useful expectation-setting claim in the codex, and it is unusual because it argues against the person saying "
    "it.\n"
    "**The claim.** \"I do not think that it is a marketing agency's responsibility to take your business from being a $6 "
    "million business to being an $18 million business.\" What an agency actually does is allocate media spend the client "
    "was going to spend anyway more efficiently, worth **\"a 10 to 20% delta either on topline revenue or on your growth "
    "rate\"**. His illustration: a business growing at 30% grows at 35 to 40% with a better partner. In a second video he "
    "states the same magnitude as a P&L efficiency figure, \"you can add 10, 20, 30% efficiency to the P&L\", so read the "
    "band as roughly 10 to 30% and note that both numbers are asserted, neither measured.\n"
    "**His proof is by absurdity and it is worth repeating verbatim to a client.** If an agency really did 3x a business, "
    "\"that would be an absolute money hack and all you would have to do is scale to being a $7 million business, you can "
    "immediately print to 18 mil, you can exit on a 25% EBITDA and make like 40 million and retire forever. It would be the "
    "easiest arbitrage that exists. And it's because it's not real.\"\n"
    "**The metaphor he ends on:** product and brand are the logs, marketing is the fuel poured on them. Marketing "
    "accelerates a fire that has to already exist, which is also why he argues an agency should want clients that have "
    "already established a footprint.\n"
    "**The warning that follows, and it is aimed at agencies selling on P&L language.** If you position on optimising the "
    "client's profit and loss, accountability for the P&L shifts to you, \"which I think is a bad idea\", because the "
    "levers that actually decide whether a consumer business becomes eight figures, product and brand, are not ones the "
    "agency controls. He calls it an especially bad frame for low-seven-figure brands because it tells the owner they no "
    "longer carry responsibility for growing the business.\n"
    "**A market observation attached to it.** In Australia roughly 30% of the market has moved from agencies to coaching "
    "groups, and he argues that is rational at high six to low seven figures: \"a bad agency at that revenue level will do "
    "way more damage to you than no agency at all\", and the lower in the market an agency serves the worse it tends to be, "
    "because it cannot charge enough to fund good work. Learning the fundamentals yourself first is what makes you able to "
    "vet an agency later.\n"
    "**Where the founder's time goes instead**, from the companion video: product portfolio expansion (banked at "
    "[[Scaling Models#SC-151|SC-151]]) and deliberately manufacturing revenue peaks across the year through launch timing, "
    "sponsorships, sale timing and cultural moments. He argues the second cannot be outsourced, because an agency's "
    "strength is large data sets and distillation, and any idea an agency has gets rolled out across its whole client "
    "portfolio, which destroys the differentiation that made the idea work.\n"
    "**Use, and its limit.** This is the right frame for what we promise at the start of an engagement, and it pairs with "
    "our standing rule never to promise volume. It is one operator's assertion from a large book, with no measurement "
    "behind either the 10-20% or the 10-30%. **Quote it as a position held by an agency owner against his own commercial "
    "interest, never as a finding.**",
    "Blue Sense Digital, An Agency Doesn't Create Business Growth, 2025-09-18; Blue Sense Digital, The Two Highest ROI Activities for an eCommerce Founder, 2025-01-29")

append_claim(
    'Marketing Math & Unit Economics.md', 'MM-186',
    'Shown recovery from near-bankruptcy: LTGP:CAC of 0.5 to above 1.2 in two months and CAC down ~70% in three, on four changes of which cutting a whole channel was the first',
    'T3', 'active',
    "A named-shape case study from an agency auditing over 1,000 ad accounts and working with 300-plus clients. Dates and "
    "ratios given, absolute revenue withheld.\n"
    "**The starting position.** CAC inflated month over month through December to February to an all-time high of **$164**, "
    "against gross profit on first purchase that had improved from about $30 to about **$70**. That is an **LTGP:CAC of "
    "0.5**, so the business was paying $100 to $160 to acquire a customer who returned $70 on first purchase. Lifetime did "
    "not rescue it: average lift by day 365 was **55%**, taking $70 to about $105, so CAC payback sat well beyond a year, "
    "which a small business cannot finance. Engagement began 20 March. Month one, with seven days to work, reached 0.8. "
    "Month two, 1.2. By month three, **CAC down about 70% from its all-time high with new-customer acquisition up about "
    "5x**.\n"
    "**Change one, cut a channel to zero.** The previous agency had ramped TikTok from $3,000 a month in November to "
    "$20,000 a month in January and February. It was cut straight to zero \"and it had pretty much no impact on total "
    "volume\". The reason it had looked good was view-through attribution on what was essentially retargeting. **The "
    "portable heuristic he states from it is the cheapest incrementality test that exists: \"if you go and start spending "
    "on another channel and your new customer volume goes down, it's probably a sign that that channel isn't working for "
    "you.\"**\n"
    "**Change two, creative volume against spend.** About **10 active creatives** were carrying **$30,000 to $40,000 a "
    "month** of Meta spend. He is careful about the rule: 10 ads is fine at a $10 blended CAC when the account is printing, "
    "and becomes the problem when the account is not profitable on acquisition. They moved to roughly **45 new creatives a "
    "month**, reaching close to **200 active ads** by the time of recording.\n"
    "**Change three, stop paying to reach people you already have.** 55% of daily revenue came from returning customers "
    "and this was not delineated anywhere in the account. Meta had **no audience segments defined at all** and was spending "
    "about **70% of budget on existing customers**. On Google, nearly all budget sat in brand across Shopping and Search. "
    "They defined the audiences, pulled spend off returning customers, split brand into its own campaigns and launched "
    "prospecting.\n"
    "**Change four, offers and landing pages as one thing.** The ads carried an entry offer and drove to a homepage that "
    "did not display that offer. There was no offer testing at all, on a brand whose customers rarely bought at full "
    "price. They introduced two to three offers and bundles aimed at raising first-purchase average order value, which "
    "raises gross profit, **which is what permits a higher CAC**. The winning offer then got dedicated landing pages "
    "carrying the same creative as the ad, built both natively and on a landing-page tool.\n"
    "**The diagnosis he wants remembered above the four changes.** Two successive agencies let this happen because nobody "
    "was measuring first-purchase profitability, so the loss was invisible until \"your quarterly P&L gets delivered to you "
    "by your accountant 2 months late and it's been 5 months since that negative profit started to hit\". Diagnose on "
    "LTGP:CAC and gross profit on first purchase, not on in-platform ROAS, which is [[Attribution & Incrementality#AT-022|AT-022]] "
    "and [[Marketing Math & Unit Economics#MM-002|MM-002]] applied to a live account.\n"
    "**Evidence quality.** Ratios, percentages and monthly spend figures were shown on a chart; revenue was not, no brand "
    "was named, and it is the agency's own case study of its own work with no counterfactual. Four changes were made "
    "simultaneously, so **the attribution of the recovery to any one of them is exactly the error "
    "[[Attribution & Incrementality#AT-107|AT-107]] describes**, from the same agency.",
    'Blue Sense Digital, 4 Changes That Recovered An eComm Bankruptcy, 2025-12-19')

append_claim(
    'Marketing Math & Unit Economics.md', 'MM-187',
    'A business that cannot afford to spend about 25% of revenue on marketing will not reach eight figures online, and the accounts that beat that maths are buying a halo from channels that are not paid media',
    'T3', 'active',
    "From an operator who has moved his own book from seven-figure to eight- and nine-figure ecommerce clients over four "
    "years, with direct account exposure to over a thousand businesses. Offered explicitly as generalisation, and he "
    "invites disagreement on camera.\n"
    "**The spend-capacity floor.** \"You really need to be able to spend at least 25% of your revenue on marketing ... or "
    "you just simply won't achieve 8 figures online.\" That capacity is not a decision, it is an output of a low cost of "
    "delivery and a compressed operating expense line. **The operating consequence is that a margin problem presents as a "
    "media problem: an account that cannot be scaled is often an account that is not allowed to be scaled.** Read with "
    "[[Marketing Math & Unit Economics#MM-008|MM-008]], where opex bloat kills sub-$300k/month brands through cash flow "
    "rather than ratio.\n"
    "**The retail exception he raises against himself.** He has seen nine-figure retail businesses running **25% gross "
    "margin** and low-single-digit net profit. His own preference, stated as a judgement not a finding: a $10M business at "
    "25% and a $100M business at 2% make the same money, and the second carries vastly more inventory and headcount risk.\n"
    "**The halo effect, which is the part that changes how we read an account.** Two businesses with near-identical "
    "products, ads, angles and creative can show **a 10 ROAS in platform against a 4**, and \"the only difference is that "
    "the one with 10 is heavily investing in other channels\". Named mechanisms: influencer activations that create a "
    "social moment, collaborations with other brands including into their email lists, and three to four years of SEO "
    "investment that later compounds. He describes the loop concretely: paid media does top of funnel, the user later "
    "searches a cold term, the brand ranks organically, trust is built, the purchase happens, **and acquisition cost drops "
    "across the board**. **So an in-platform ROAS comparison between two accounts is not a comparison of two media buyers.** "
    "This is the same phenomenon measured from the opposite direction in [[Creative Science#CR-200|CR-200]], where removing "
    "brand presence by changing country halves ad performance.\n"
    "**The rest of his seven-to-eight-figure model, recorded briefly because it is context rather than advertising "
    "science.** Product-market fit is close to a prerequisite. Portfolio width matters, since a single niched product caps "
    "out (banked at [[Scaling Models#SC-151|SC-151]]). Distribution skill alone can carry an average product to eight "
    "figures but not to nine, because \"a 9 figure business is excellent across everything\". Talent is the ceiling above "
    "that: \"the total revenue capacity of a business is the function of the summation of all skills across the talent "
    "pool\", with seven-figure ecommerce typically run by two to four core operators and limited by the founder's own "
    "ability to identify the current bottleneck; he claims one excellent hire against a merely acceptable one compounds "
    "5-10% of annual growth, leaving one business ~40% larger after two to three years. And growth is finally capped by "
    "the owners' appetite for risk, because a fast-growing business cannot distribute earnings while free cash flow is "
    "consumed by inventory and the cash conversion cycle.\n"
    "Every figure here is asserted from a consulting book. Nothing was shown, no brand named, and he flags the talent and "
    "risk sections as subjective.",
    "Blue Sense Digital, Here's What Seperate's 7 & 8 Figure eCommerce Businesses, 2025-06-23")

# ---------------------------------------------------------------- amendments

amend('Marketing Math & Unit Economics.md', 'MM-007', add_body=(
    "**PRECISION PROBLEM on the fashion day-365 figure, found 2026-08-29, and it needs resolving before the band is quoted "
    "again.** This claim banks fashion at ~55% cumulative gross-profit lift by day 365, with a day-90 checkpoint of ~15%. "
    "In a June 2025 video the SAME operator states the fashion band as \"90-day growth ... at about the 15% mark\" and "
    "\"at 365 ... around the 45% mark\". **The day-90 figure replicates exactly. The day-365 figure does not: 45% there "
    "against 55% here.** He is loose about it in the second telling, calling them \"relatively broad index metrics\" and "
    "\"generalized ballpark figures\", and the 45% is the number he then runs his worked scaling arithmetic on at "
    "[[Marketing Math & Unit Economics#MM-184|MM-184]]. Neither figure is sourced to a dataset in either video. **Quote "
    "fashion day-365 as roughly 45 to 55% from one operator's recall, never as 55%, until a shown cohort curve settles it.** "
    "The CPG ~110% figure is restated unchanged in the second video and is unaffected."),
    add_source='Blue Sense Digital, Where To Allocate Agency Fees On The P&L, 2025-06-10')

amend('Marketing Math & Unit Economics.md', 'MM-097', add_body=(
    "**The same window, now claimed for CREATIVE testing as well as offer testing, by a second route and with a mechanism "
    "attached, added 2026-08-29.** The argument here was that a depressed baseline makes a genuine offer improvement easier "
    "to detect. Blue Sense extends it to creative and states the cost of testing in the good months instead: \"in good "
    "months like 50% of your ads will win ... you get this artificial inflation in ads that actually won't perform in a "
    "colder market\", which \"builds a worse feedback loop for future creative iteration\". Full entry with the Black Friday "
    "mirror rule at [[Creative Science#CR-199|CR-199]], and the cold-market-proxy version of the same Q1 argument at "
    "[[Creative Science#CR-200|CR-200]]. **This claim is no longer T4-asserted-alone: three separate arguments from two "
    "operators now land on the same window, though still none of them with a shown win-rate-by-month distribution.**"),
    add_source='Blue Sense Digital, Here’s What You Should Be Focusing On in 2026, 2025-10-28')

amend('Scaling Models.md', 'SC-044', add_body=(
    "**A THIRD operator on the same 3x multiple, added 2026-08-29, and he supplies the DURATION FLOOR the other two never "
    "state.** Nick Theriot, at over $5 million a month: turn an ad set off once it has spent three times the account's "
    "average cost per result with zero sales, worked on screen as $150 against a $50 cost per purchase. **The addition is "
    "that the 3x alone is not sufficient for him; the spend has to have accumulated over at least 3 days.** His stated "
    "reason is delivery rather than statistics: \"it takes about 72 hours for Facebook to fully optimize\". He names the "
    "failure the floor prevents, which is the useful part for anyone running automated rules: an ad set that burns $150 "
    "between midnight and 2am has hit the 3x gate and has told you nothing, \"it wouldn't make sense to turn that off "
    "because it's just way too soon\". **So the gate is a pair, spend multiple AND elapsed time, and a rule written on the "
    "multiple alone will kill ad sets on intraday spikes.** Three operators, three verticals, one multiple, and still "
    "nobody has shown why 3x rather than 2x or 5x. Charley T sets a one-week duration, Theriot 3 days, and Matt Shiver "
    "states none."),
    add_source='Nick Theriot, ABO vs CBO in 2026: Which One Should You Actually Use?, 2026-08-28')

amend('Scaling Models.md', 'SC-019', add_body=(
    "**Theriot's account shown running the rule at both boundaries at once, added 2026-08-29.** Three parallel CBOs on one "
    "account, $54,000 of spend across the previous seven days, split by PRODUCT CATEGORY and described exactly as this "
    "claim's test predicts: \"if we're selling t-shirts, we could put all of our t-shirts in that one CBO campaign. Whereas, "
    "if we have a t-shirt campaign, a jeans campaign, and a jacket campaign, that's perfectly okay.\" He applies the second "
    "boundary in the same account by launching separate CBOs per COUNTRY for a European and English-speaking-market test, "
    "which he then turned off because it did not work. **The negative outcome is the useful half: a per-country campaign is "
    "the correct structure for a geographic test and structure alone does not make the geography work.**"),
    add_source='Nick Theriot, ABO vs CBO in 2026: Which One Should You Actually Use?, 2026-08-28')

amend('Creative Science.md', 'CR-118', add_body=(
    "**A fourth figure for the same hit rate, added 2026-08-29, and it is the most quotable because it is stated as a "
    "count rather than a percentage.** Blue Sense: \"a regular hit rate for an e-commerce brand sits at about 15%, which "
    "means that you have to go and launch seven unique ads and only one of these will work and actually be able to scale\", "
    "with roughly 20% named as the ceiling on that rate for anyone. **One in seven is the same order as the 5-10% "
    "hold-spend figure this claim already carries, and it is measuring a slightly easier bar (works and scales, rather "
    "than holds spend), which is consistent with it landing a little higher.** Asserted from a consulting book, no dataset "
    "shown. The same operator refuses to state a hit rate for PRODUCT launches on the grounds that he has no data for it, "
    "recorded at [[Scaling Models#SC-151|SC-151]]."),
    add_source='Blue Sense Digital, The Two Highest ROI Activities for an eCommerce Founder, 2025-01-29')

print('merge complete')
