---
title: "Lesson 076 - The Error List Was The Only Place The Rules Were Written"
type: lesson
lesson: 76
date: 2026-11-09
topic: Google PMax & Shopping
claims: [GP-050, GP-048, GA-096, GP-022, GP-023, GP-036, GP-051]
tags: [advertising-science, lesson, google, pmax, local-services, account-structure, constraints, evidence-tiers]
---

# Lesson 076 · The Error List Was The Only Place The Rules Were Written

Topic: Google PMax & Shopping, taken from the rotation at index 7 in the ordinary way, so the pointer advances 7 to 8. This is the least-served topic on the board at four lessons out of seventy-six, and the 8 November scoreboard reserved the next ordinary slot for it. No research run exists for today in either lane, so the newest entry on the Harvest Log is still 8 November, which was quiet: zero new transcripts, zero claims, no law change. Both ends of that file were read. There was no harvest to teach, so the rotation decided. Sunday, so no video.

The claim is [[Google PMax & Shopping#GP-050|GP-050]], untaught since it was banked on 19 October. It is the only untaught claim on the board that belongs to this topic and touches local service businesses, which is the whole book.

## 1. The mechanism

In October Google opened a new campaign type to the outside world: Local Services Performance Max. Before that you could read that the setting existed but you could not switch it on yourself. Now you can.

The release note describes it in about six lines of neutral product language. The actual rules are not in those lines. They are in the list of new error codes shipped beside them.

Four rules, read off the errors.

**One per account.** `LOCAL_SERVICES_MULTIPLE_PERFORMANCE_MAX_CAMPAIGNS_NOT_ALLOWED`. You get one Local Services PMax campaign in an account. Not one per service, not one per location. One.

**One Business Profile listing.** `listing_id` is required at creation, and `LOCATION_ASSET_DOES_NOT_MATCH_CAMPAIGN_LISTING_ID` means every location asset on the campaign has to match the listing it was built against. The campaign is welded to one Google Business Profile.

**The goal is locked.** A family of four errors says the Local Services conversion goal cannot be unlinked, cannot be overridden, and cannot be used by any other campaign type. The usual Performance Max freedom to pick and weight conversion goals does not exist here.

**The category list is not published.** `UNSUPPORTED_LOCAL_SERVICES_CATEGORY` tells you a list exists and that your category has to be on it. Google did not print the list.

One more field matters and it is easy to skim past. `local_services_enabled` moved from output-only to **immutable**. Immutable means you set it when you create the campaign and you can never change it. There is no switching an ordinary PMax campaign into this one, and no switching back out.

The analogy that maps. You are opening a shop and the landlord hands you a lease. The brochure talks about footfall and signage. The rules are in the small print: one shop under this lease, at this address, selling from an approved trade list you will be shown after you sign, and the shopfront can never be changed. None of that tells you whether the shop will make money. All of it tells you what shape of business can exist there at all. You read the small print first, because it decides whether the rest of the conversation is worth having.

That is the move to learn. **A new campaign type is a shape before it is a performance question, and the shape is usually written in the error list rather than the announcement.** Product copy describes what the thing is for. Errors describe what the thing refuses to do, and refusals are the real specification.

## 2. The evidence

[[Google PMax & Shopping#GP-050|GP-050]], **T1**. Google Ads API v26 release notes, 14 October 2026, read in full at source, plus Google's own developer blog post of the same date. T1 because the field changes, the required fields and the error names are Google's published documentation of its own system.

Note what T1 buys here and what it does not. It buys certainty about the constraints. It buys nothing at all about results: **no cost figure, no lead-volume figure, no comparison against a standard Search campaign appears anywhere in the source.** Nothing in GP-050 says this campaign type performs.

That distinction is worth naming properly, because it is new to this series rather than a restatement of it. Lessons 073, 074 and 075 all landed on the same rule from different sides: tier is provenance, not usefulness. Today's claim splits usefulness itself in two.

- A **constraint claim** tells you what is possible. It is durable, it is checkable against the platform today, and it decides architecture.
- A **performance claim** tells you what happened. It decays, it carries a context that may not be yours, and it decides spend.

GP-050 is a pure constraint claim. It is T1, it recommends nothing, and it still decides something real: it rules out a structure. Ruling out a structure before you build it is worth more than most performance numbers, because a structure is the expensive thing to get wrong.

[[Google PMax & Shopping#GP-048|GP-048]], **T1**, is the sibling and it was read three weeks earlier off API v25.2. Google will generate a Performance Max draft from an existing Smart campaign, paused and incomplete so nothing goes live by accident, and `validate_only` makes a dry run free. Two options error instead of degrading gracefully: `gbp_enabled` and `image_enabled` both return hard errors on that conversion. For a local service advertiser that is the whole point of the Smart campaign being thrown away at the door. Same pattern again. The useful sentence was an error name.

[[Google Auction & Smart Bidding#GA-096|GA-096]], **T1**, shipped in the same v26 release and is the same species of fact: Google now names a budget floor in two places, a Search recommendation that fires when a daily budget is too low for performance, and a per-currency minimum daily budget for Demand Gen exposed as an API field. Constraints, not results.

Two older claims give the one-per-account cap its meaning. [[Google PMax & Shopping#GP-022|GP-022]] and [[Google PMax & Shopping#GP-023|GP-023]] are both **T3**, asserted from agency experience with no test shown, and they say campaign count should follow spend and that only four reasons justify splitting at all. Read with GP-050, the cap stops looking like a restriction and starts looking like a default those claims would have recommended anyway. **Google has imposed the consolidation that a good operator would have chosen.** That is a much better reason to accept a limit than compliance is.

[[Google PMax & Shopping#GP-036|GP-036]], **T3**, is the gate that fires before any of this: constrain yourself to one asset group per $50 of daily spend, and at $50 a day the operator's own advice is to skip Performance Max and run standard Shopping instead.

## 3. Our accounts

Say the honest thing first, same as the last two Google lessons. **We hold zero live Google lanes.** No Search, no Shopping, no PMax, no Demand Gen, on any account in this book. Everything we run is Meta and everything is lead generation. Nothing in this lesson changes a number this week.

What it does change is the answer we would give if a client asked about this next month, and one client fits the shape closely enough that the exercise is real.

**StayWell Spine & Joint Specialists** is one clinic at one address in Novi, Michigan, and it is a local service business in the plainest sense. One address means one Business Profile listing, which is the shape GP-050 requires, so the listing constraint does not bite. Whether a verified listing exists and what category it carries is a check we have never run, not a fact we hold.

The one-per-account cap does bite. StayWell runs **two distinct programmes under two physicians**: Dr. Binder on regenerative knee and joint care, Dr. Cole Schneider on back, neck and sciatica. On Meta we treat those as separate things on purpose, with separate landing pages built for each. Under Local Services PMax they would share a single campaign, a single locked conversion goal, and a single pool of accumulated learning. You could not fund knee separately from sciatica, and you could not read them apart without the per-asset-group tracking that GP-048 only just made possible.

Then the budget gate closes the door anyway. The live Schneider campaign checked on 31 October runs **$45 a day** as one CBO, spread across **six live ad sets**, producing roughly **nine leads a week**. GP-036 says below $50 a day you do not run Performance Max at all. At nine leads a week the problem on that campaign is already too little volume split too many ways, which is why Kartik's recorded view is fewer ad sets at the next creative refresh rather than more entities now. A campaign type whose first rule is one per account would at least not make that worse, and the budget floor means we never find out.

Scale for the rest of the book, from our own file, 23 to 29 October: **SJR Commercial $767.78 spend, 136 CRM people, $5.65 each. StayWell $562.63, 23 people, $24.46 each.** Phoenix Truxx currently sits at $160 a day on statics plus $40 on dump since 3 November. RK Consumer Services is built and paused at $50 a day. Every one of those is under or around the single-campaign Performance Max floor, before we get to the fact that none of them is a Google account.

The two dealerships fail the shape test outright rather than the budget test. SJR Commercial and Phoenix Truxx both sell several body types, and the SJR account is shared and holds **166 campaigns**. One campaign welded to one listing with one locked goal is not a structure that describes a dealership.

The only Google build this vault holds is **Mattia Spinal Care**: PMax built to spec and pasted by the client on 8 July 2026, roughly a twelve-mile presence-only ring around 32835 in Orlando, offboarded 24 July with campaigns left running to 16 August. Billing was $1,297 a month for management, a $997 Google package and a $250 second-campaign add-on, and on 4 July the decision was taken to put 100% of the $4,000 monthly budget on Google. Carry one operational fact out of it every time Google comes up: **a second unrelated Google Ads account was contaminating that client's landing-page traffic data**, IDs 24031060460 and 24031057880. Check for shadow accounts before trusting anybody's on-page conversion rate.

Two guards.

**Do not carry the immutability point to Meta.** Nothing in Meta's product behaves like `local_services_enabled`. The nearest shape on our side is the opposite failure, where [[Google PMax & Shopping#GP-051|GP-051]] and lesson 062 showed a default switching itself on and an account-level off switch quietly stopping governing new campaigns from 4 December. A constraint you cannot change and a default that changes under you are different problems and they need different habits. The first one you read before you build. The second one you re-read after the platform ships.

**There is no basis here for recommending this campaign type to anyone.** If a client asks, the honest answer is that it exists, that it is tightly bounded in four ways we can name, that the supported-category list is unpublished so we cannot even confirm chiropractic is eligible, and that Google has published no performance evidence of any kind. The next step on GP-050 is a category-list check, not a build.

## 4. The decision rule

**Read a new campaign type's constraints before its claims: one per account, which listing, which goal, which categories, what is immutable. If the constraints rule out the structure the business needs, the performance question never comes up.**

## 5. Quiz

Drop your answers in `_answers-inbox.md` with the lesson number. Five questions, three of them applied.

**Q1.** GP-050 is T1 and it contains no cost figure, no lead-volume figure and no comparison to a Search campaign. Explain why it still decides something, using the difference between a constraint claim and a performance claim.

**Q2.** A client with one clinic, one address and three separately marketed treatment programmes asks whether to put all three into Local Services Performance Max. Walk through which two constraints you check first, and say which one fails before budget is even discussed.

**Q3.** Someone on the team reads the one-per-account cap as Google restricting advertisers. Give the better reading, naming the two claims that support it and their tier.

**Q4.** StayWell's live Schneider campaign runs $45 a day across six ad sets at about nine leads a week. Two separate claims in this lesson each independently rule out Performance Max for that campaign. Name both, and say which one would still rule it out if the budget doubled tomorrow.

**Q5.** A teammate wants to cite the immutability of `local_services_enabled` in a note arguing that Meta settings are safer because they can always be changed back. What is wrong with the comparison, and which lesson already covered the Meta-shaped version of the problem?

> [!note]- Answer key
>
> **A1.** A constraint claim tells you what the platform allows; a performance claim tells you what happened somewhere else. Constraints are durable, checkable against the platform today, and they decide architecture. Performance figures decay and carry a context that may not be yours. GP-050 decides something by ruling out a structure, which is the expensive thing to get wrong, and it does that without recommending anything. Full marks also require noting that T1 here buys certainty about the constraints and nothing about results.
>
> **A2.** First the listing constraint: `listing_id` is required and all location assets must match it, so check whether the business is one Business Profile. One clinic at one address passes. Second the one-per-account cap plus the locked conversion goal: three separately marketed programmes would share one campaign, one goal and one pool of learning, so they cannot be funded or read apart. **The one-per-account cap fails first**, before budget. The unpublished category list is a fair third answer and also fires before budget.
>
> **A3.** Google has imposed the consolidation a good operator would have chosen. GP-022 (**T3**) says campaign count should follow spend and fewer is usually better. GP-023 (**T3**) says only four reasons justify a split: brand versus non-brand, geography, different margin or efficiency goals, and genuinely distinct categories. Both are asserted with no test shown, so the tier has to be said out loud. The cap removes a decision most accounts get wrong.
>
> **A4.** GP-036 (**T3**), the $50-a-day floor, rules it out at $45. The one-per-account cap plus locked goal (GP-050, **T1**) rules it out because Binder's knee programme and Schneider's back and sciatica programme would have to share one campaign and one goal. **The structural one still rules it out at $90 a day.** A budget fixes the budget gate and cannot fix the shape.
>
> **A5.** The comparison swaps two different problems. GP-050's immutability is a constraint you read before you build and then live with. GP-051, taught in lesson 062, is the opposite failure: a default that switches itself on and an account-level off switch that quietly stops governing new campaigns from 4 December. Meta has its own instances of that shape, so changeable is not the same as safer, and the two need different habits. Read constraints before building. Re-read defaults after the platform ships.

---

Last lesson: [[2026-11-08 Lesson 075 - The Price Is Set By Something That Happens After The Click]]
