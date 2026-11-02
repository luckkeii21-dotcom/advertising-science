---
title: "Lesson 068 - Permission Became A Requirement"
type: lesson
lesson: 68
date: 2026-11-02
topic: Meta Delivery & Andromeda
claims: [MD-193, MD-149, MD-061, MD-156, MD-098, MD-038]
tags: [advertising-science, lesson, meta-delivery, policy, verification, truck-lane]
---

# Lesson 068 · Permission Became A Requirement

Topic: Meta Delivery & Andromeda, the law layer. Harvest-driven, so the rotation pointer holds at 4. This morning's research pass caught a three-character edit on Meta's Advertising Standards page and banked it as [[Meta Delivery & Andromeda#MD-193|MD-193]]. It reaches two of our accounts and only two.

## 1. The mechanism

Meta's Advertising Standards page carries a section called Financial and Insurance Products and Services. One sentence in it used to read:

> "Advertisers promoting financial products and services **may be required to** verify their business and/or individual identity..."

As of this morning it reads:

> "Advertisers promoting financial products and services **are required to** verify their business and/or individual identity..."

Seven characters out, four in. Nothing else in the sentence moved, including the clause "where this is a requirement", which still ties the *regulatory authorisation* half to local law. The verification half now carries no qualifier at all.

The thing to understand is the difference between a right Meta reserves and a condition Meta states. Think of a venue door. "We may check ID" means most nights nobody asks you, and if they do, you deal with it then. "We check ID" means the ID is something you bring before you leave the house. The night inside the venue is identical. What changed is whether the document is a problem you solve in advance or a problem you solve standing in the doorway with everyone behind you.

That is the whole lesson. The ads do not change. The spend does not change. **The timing of one errand changes**, and it moves from reactive to preparatory.

Two things this does not say, and both matter more than the change itself. It does not say enforcement has started. No account of ours has been asked for anything. And it does not say anybody is in violation today. This is the policy text moving, nothing else.

## 2. The evidence

[[Meta Delivery & Andromeda#MD-193|MD-193]] is **T1**, because it is Meta's own published policy text read off Meta's own page, both the US and UK locales, in one browser session. T1 does not mean important. It means we are reading the machine's own documentation rather than somebody's account of it.

The honest limits are large and they are recorded in the claim:

- **The page carries no date marker of any kind.** The change landed somewhere between 26 October, when all 32 section hashes across both locales were verified byte-identical, and today. It cannot be dated tighter than that week.
- **Meta announced it nowhere.** No changelog entry, no Newsroom post, nothing on the Engineering feed, nothing on Meta for Business News. We found it by diffing hashes, not by being told.
- **No effective date, no enforcement date, and no statement about existing advertisers.**

Now the part that makes this more than a footnote. [[Meta Delivery & Andromeda#MD-149|MD-149]] is **T1** and it was banked 66 days ago, on 28 August, off a Polish-language Meta Newsroom post. Two figures from it: verification required of **100% of financial-services advertisers** directing ads to Poland, and a global target of **90% of Meta's worldwide ad revenue coming from verified advertisers by the end of 2026, against 70% in 2025.**

Read those two claims next to each other. MD-149 named the direction, the deadline and the mechanism: category-plus-geography expansion of an identity check. MD-193 is that mechanism arriving in the global policy text, one category wide. **A claim we banked in August predicted the shape of a change we caught in November.** That is what a codex is for. The August entry even wrote the operating consequence in advance: the cheapest time to have verified documents in order is before a category sweep reaches the account, not during one.

Two guards to carry.

[[Meta Delivery & Andromeda#MD-156|MD-156]] is **T1** and says Advertising Standards changes stage by locale, so two people reading the same page the same day can see different rules. MD-193 broke that pattern, both locales moved together. One simultaneous change does not retire the rule. Read both locales every time, and do not expect a gap.

[[Meta Delivery & Andromeda#MD-098|MD-098]] is **T3**, one operator's first-hand account, and it is the reason this is not a five-minute errand to shrug at. Automated ID verification failed on a 15-year clean profile, with no explanation, no retry path and no appeal route found, still unresolved a week later. Treat verification as a process that can fail opaquely. That is exactly why you want it attempted on a calm Tuesday rather than on the day delivery stops. [[Meta Delivery & Andromeda#MD-038|MD-038]] is **T2** and sits behind it: account shutdowns reach clean accounts, and recovery infrastructure is something you provision early or not at all.

## 3. Our accounts

**The clinic lane is untouched.** StayWell, Mattia, Chiropraise: nothing in those offers is a financial product. Do not raise this with them.

**The exposure is the two truck dealerships, and they are not equally exposed.**

**SJR Commercial is the harder case, because SJR is the lender.** The locked dump angle is the approval-reversal pitch, and its hero line is "SJR owns the bank. Low credit, no credit, doesn't matter." That claim clears compliance precisely because it is literally true: SJR owns NJ Auto Lending and underwrites in-house. Which means SJR is not an advertiser mentioning financing near a truck. It is an advertiser promoting its own credit product. Both halves of the MD-193 sentence point at it, the identity-verification half with no qualifier, and the "authorised by the relevant regulatory authorities" half.

**Phoenix Truxx is squarely inside the category too, on volume.** September form answers: **93% of respondents need or may need financing.** Financing is the offer, not a feature of it. And Phoenix already has enforcement history in this exact policy family: the Hino tow and rollback ad was **disapproved 8 October under Meta's financial products policy, after $98.83 of spend and 6 leads**, and "Box Truck Ad" v1 was disapproved alongside it. That is this policy touching our money 25 days before its text hardened.

**One thing this does not reopen.** Kartik ruled on 9 October that neither account declares the financial-services special ad category. That decision stands and this lesson does not argue with it. Understand why they are different gates. [[Meta Delivery & Andromeda#MD-061|MD-061]] is the **special ad category**: a campaign-level declaration that strips ad-set targeting in exchange for staying out of rejection and disablement risk. MD-193 is **account-level business and identity verification**. One is a targeting trade you choose. The other is a document you either have on file or do not. Declining the first has no bearing on the second, and conflating them is the mistake this section exists to prevent.

What we actually know about our verification status on either account: **nothing.** Nobody has looked. Same shape as yesterday's unrun label check.

## 4. The decision rule

**On any account whose ads mention financing, a credit application or a payment term, treat business and identity verification as a precondition to satisfy while nothing is wrong, not a request to answer when delivery stops.**

The errand this creates is one person, two accounts, one afternoon: open Business Manager on SJR Commercial and Phoenix Truxx, read the current verification status, and write down what it says. Nothing more. If both are verified, this lesson cost an afternoon and bought a known floor. If either is not, you found it on a day when no money was at stake, which per MD-098 is the only good day to find it.

## 5. Quiz

Answers go in `_answers-inbox.md`.

**Q1.** Quote the MD-193 change, state its tier, and name the two things the claim explicitly refuses to say. Then explain why the clause "where this is a requirement" does not soften the verification half.

**Q2.** MD-149 was banked on 28 August off a Polish Newsroom post about one country. MD-193 is a global policy edit caught on 2 November. Explain what MD-149 contributed that MD-193 alone cannot give you, and name the one number in MD-149 that makes it structural rather than regional.

**Q3.** Applied. A teammate reads this lesson and writes in the Phoenix channel: "we should declare the financial special ad category now that verification is mandatory." Say what you send back. Name both gates, say what each one actually costs, and name the standing decision that governs one of them.

**Q4.** Applied. Rank SJR Commercial and Phoenix Truxx by exposure to MD-193 and defend the order with one fact from each account. Then say which single sentence of SJR creative is the reason it ranks where it does, and why that sentence is still correct to run.

**Q5.** Applied. MD-193 was found by diffing per-section hashes on a page with no date marker, no changelog and no announcement. Say what that tells you about the reliability of Meta announcements as a change-detection method, and name the one claim in this lesson that warns you the reverse case is also live: a rule that changes for some readers and not others. Then say what you would do differently if the UK locale had moved and the US had not.

> [!note]- Answer key
>
> **A1.** The sentence under Restricted goods and services, Financial and Insurance Products and Services, moved from "Advertisers promoting financial products and services **may be required to** verify their business and/or individual identity" to "**are required to** verify". Tier **T1**, Meta's own policy text read off Meta's own page on both locales. The two refusals: it does not say enforcement has started, and it does not say when the change landed, because the page carries no date marker and the window is only narrowable to 26 October through 2 November. Why the qualifier does not help: "where this is a requirement" attaches to the regulatory-authorisation half of the sentence, demonstrating authorisation by the relevant authorities. The identity and business verification half sits before it and now carries no condition at all. Full marks for noting Meta published no effective date and no statement about existing advertisers either.
>
> **A2.** MD-149 contributes the **direction, the deadline and the mechanism**, none of which are visible in a three-character edit. It states that Meta is expanding an existing identity check by category and geography, that financial services is the named first category, and that there is a hard date attached. Without it, MD-193 is one sentence that got firmer and could plausibly be tidier wording. With it, MD-193 is a predicted step in a programme. The structural number is the **90% of global ad revenue from verified advertisers by end of 2026, against 70% in 2025**: a 20-point move in who is allowed to buy inventory inside sixteen months. Credit for noting the 70% baseline appears only in the 28 August post and must keep being quoted from it, since the September restatement dropped it.
>
> **A3.** Send back: those are two different gates and only one of them changed today. The **special ad category** (MD-061) is a campaign-level declaration. Its cost is real and immediate, declaring strips ad-set targeting. Its benefit is avoiding rejection and, per one unverified operator account, account disablement. **Verification** (MD-193) is account-level business and identity confirmation. Its cost is paperwork and time, and it strips nothing. The standing decision: Kartik, 9 October, neither SJR nor Phoenix declares the financial-services category, on reach grounds, and it is not to be re-proposed. So the answer is to run the verification check and leave the category alone. Full marks for naming that declining one has no effect whatsoever on the other, and that the teammate's sentence assumed it did.
>
> **A4.** **SJR Commercial first.** It owns NJ Auto Lending and underwrites in-house, so it is promoting its own credit product rather than mentioning a third party's, which puts both halves of the sentence on it, including the regulatory-authorisation half. **Phoenix Truxx second**, still clearly inside the category: 93% of September form respondents need or may need financing, so financing is the offer. Credit for naming Phoenix's actual enforcement history as a counter-argument for ranking it first, the Hino tow and rollback ad disapproved 8 October under the financial products policy after $98.83 and 6 leads, plus "Box Truck Ad" v1. Either order defends if the facts are right; the ranking matters less than knowing both are in scope. The SJR sentence is **"SJR owns the bank. Low credit, no credit, doesn't matter."** It is still correct to run because it is literally true, which is exactly what makes SJR a financial-services advertiser rather than a dealership near a lender.
>
> **A5.** It tells you Meta announcements are **not a change-detection method at all** for policy text. A binding requirement moved on both locales with no changelog, no Newsroom post and nothing on any watched feed, and the only thing that caught it was diffing the page against a stored baseline. Announcements tell you about things Meta wants you to know. The policy page is where the rules actually live. The claim warning about the reverse case is **[[Meta Delivery & Andromeda#MD-156|MD-156]]**, T1: Advertising Standards changes stage by locale, so two people reading the same page the same day see different rules. If the UK had moved alone, the correct read is that the change is real and staged, so it is coming, and the operating consequence is the same preparatory errand on a longer fuse. What you must not do is report a locale-staged change as not applying to us. Credit for naming that MD-193 moving on both locales at once does not retire MD-156, it only means a gap is not guaranteed, and for noting that the UK delta was four characters against the US three and could not be localised because no raw UK body text had ever been cached.
