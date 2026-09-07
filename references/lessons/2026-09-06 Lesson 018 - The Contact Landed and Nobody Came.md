---
title: "Lesson 018 - The Contact Landed and Nobody Came"
type: lesson
lesson: 18
date: 2026-09-06
topic: Attribution & Incrementality
claims: [AT-114, AT-030, AT-057]
tags: [advertising-science, lesson, attribution, tracking, landing-pages, ghl]
---

# Lesson 018 - The Contact Landed and Nobody Came

## 1. The mechanism

A native form belongs to the platform. You drop a GoHighLevel form element on a GoHighLevel page and GoHighLevel knows a submission happened. The record and the routing are one event.

A coded form belongs to you. It is HTML you wrote, it collects the answers into JSON, and it POSTs them somewhere. Now the record and the routing are two separate things that both have to work, and the browser can only tell you about the first one.

Here is the part that makes this an attribution problem rather than a build note. **The person filling in the form sees success either way.** They hit submit, the thank-you page loads, and they go and wait for a phone call. Nothing in Ads Manager shows an error. Nothing in the CRM shows an error. The ad account reports the click, the landing page view and the cost, because every one of those is true.

Think about a hospital admissions desk. The patient is entered into the system. Name right, phone right, address right. Then nobody ticks the box that says which ward. The patient is in the system. Anyone who searches finds them. They will sit in reception all day, because a record is what proves you exist and a routing tag is what makes somebody come and get you.

That is the failure shape on a coded form, and it is worse than a form that dies outright. A dead form produces zero contacts, and zero contacts is loud. A form that creates the contact and drops the tag produces a CRM that looks completely healthy and a phone that never rings.

## 2. The evidence

**[[Attribution & Incrementality#AT-114|AT-114]], T3, active.** An operator rebuilds a GoHighLevel funnel as custom HTML and keeps the platform's native form on the page, hidden in a column, filled and submitted by JavaScript when the visible form completes. His stated reason is attribution, in his own words: he wanted to keep the click data for the people who visit. The generalisable claim is that a coded form replacing a native one drops the submission and the tracking together.

Read what the source actually did before you copy the pattern. He tested it live on camera. **The hidden form did not fire.** The video ends with him in the browser console still debugging, and he says plainly that he does not know how it works. So the recipe is not the value here. The value is two things: the failure mode, and the check that caught it. He submitted a real entry and went and looked for it in the platform's own submissions view.

That is why this claim is T3 and stays T3. One operator, no test, a demo that failed. What survives at that tier is the shape of the problem. Never the build.

It sits with two claims you already know. **[[Attribution & Incrementality#AT-030|AT-030]], T3**, on deliberate pixel placement so bad leads never train the event. **[[Attribution & Incrementality#AT-057|AT-057]], T2**, on clicks that never reach the page at all, where a 62% ratio turns a $4.50 cost per click into a real $8 to $9. All three are breaks between the ad and the record. **None of the three raises an error anywhere in the ad account.** That is the family resemblance, and it is why you have to go and look on purpose.

## 3. Our accounts

Four live accounts run Meta Instant Forms. Eight Instant Form builds are on file across those four. Instant Forms are native, so this claim does not touch them. One account has ever run a coded form, and it is worth the whole lesson.

Mattia Spinal Care, onboarded 2026-06-29, offboarded 2026-07-24. Two hand-coded landing pages were the live ad destinations. Page A, spinal decompression, at `toporlandochiro.com/landing-page`. Page B, shockwave, at `toporlandochiro.com/shock-wave/offer-landing-page`.

We solved AT-114's problem a better way than the source did. Rather than hiding a native form on the page and hoping JavaScript fires it, the form POSTs to a Cloudflare Worker we own, and the Worker calls the GHL Contacts API with the token held server-side. That removes the paid Inbound Webhook, which needs the Workflow Pro plan and bills $0.01 per execution after the first 100. Cloudflare's free tier is 100,000 requests a day. Ten custom field IDs are mapped, `gclid` and the UTMs write to the native attribution object, and the payload retries three ways so a mapping fault never loses a lead. **One line changed on the shockwave page**, the webhook URL at roughly line 1157.

Page B was verified end to end. A do-not-contact test lead and Kartik's own live submit both landed with fields, tags and `gclid` mapped, and the test lead came back `tier:1`.

**Page A was never verified, and six records disagree about whether it was even wired.**

| Where you look | What it says about the decompression path |
|---|---|
| The deployed page, `10-...landing-page.html` line 1247 | Points at the Worker. Declares `funnel: 'spinal-decompression'` at line 1534. |
| The Worker source on disk | Reads that key and applies a different tag set, `sd-lead`, not `sw-lead`. |
| The Worker's git repo | Three commits, all 2026-07-07. **The decompression routing is uncommitted.** 14 insertions sitting in the working tree, never pushed. |
| `GHL-WORKFLOW-SETUP.md`, the only wiring instruction on file | Names `sw-lead` as the trigger. **`sd-lead` appears nowhere in it.** |
| The vault relay note | Lists decompression replication under **Pending**. |
| The `_HOT.md` hot sheet | Lists it under closed by the churn, meaning never done. |

Line up what that produces. A decompression opt-in upserts fine, because the contact payload is funnel-agnostic. It gets tagged `sd-lead`. The only documented workflow triggers on `sw-lead`. If nobody built the second trigger in the account, that person is a healthy-looking contact in GoHighLevel with no SMS, no email and no agent call behind them.

**Say only what the record supports.** We cannot read the deployed Worker or the GHL workflow list from here, and `wrangler deploy` ships from the working tree without needing a commit, so the live code may well be correct. The honest finding is not that it broke. **It is that six places record six different states and not one of them is a confirmed submission.** That is the same hole AT-114 describes, and we walked into it with the better architecture.

One more real item. `01-spinal-decompression-multistep-form.html` still POSTs to the paid Inbound Webhook at line 516. It is not one of the two deployed pages, and it is the file anyone would reach for next.

**This is live work, not history.** The 2026-08-27 MetaTechAI decision puts paid traffic on our own landing page carrying the six-question form. Nothing is built yet. Our own build skill already carries the check as one line in a go-live checklist, and it names the tag `website-lead` while the Mattia build used a tag per funnel. A checklist item is weaker than a gate, and the tag name is the thing that has to match the workflow.

## 4. The decision rule

**A coded form is not live until one real submission has been found in the platform's own record, with its tag attached, and that tag is the one the workflow actually triggers on. Test the page you are sending traffic to, not the page next to it.**

## 5. Quiz

Answers go in `_answers-inbox.md`. Partial answers still get graded.

**Q1.** A coded form fails in two different ways. In one, no contact is created. In the other, the contact is created and the routing tag is dropped. Explain which one costs more money and why, in terms of what each looks like from the outside.

**Q2.** AT-114 is T3, comes from a single operator, and his own live demo of the pattern failed on camera. State what we are allowed to take from that claim and what we are not, and name the one thing in the source worth copying exactly.

**Q3 (application).** You are shipping the MetaTechAI landing page this week with a six-question form feeding a relay into GoHighLevel. Write the go-live sequence as an ordered list, and mark the single step that is the proof. Then say what you would do differently from the Mattia build, given what Page A shows.

**Q4 (application, and this is the harder one).** Take the six records in the table above. Rank them by how much they can be trusted about whether decompression leads were routed, strongest first, and justify the top and the bottom. Then name the two things you would go and look at to close the question, and say why the git repository is not one of them.

**Q5 (judgement, reporting).** A client's Meta account shows 40 opt-ins in a week. Their CRM shows 40 contacts created and 0 calls attempted. The account uses a coded landing-page form. Name the first three things you check, in order. Then name the sentence you must not write in the weekly report until you have checked them, and say why writing it early is a reporting failure rather than just a guess.

> [!note]- Answer key
>
> **Q1.** The dropped-tag failure costs far more. Zero contacts is loud: the CRM is empty, somebody notices inside a day, and spend gets paused. A created contact with no tag is silent. The CRM fills up normally, every contact looks complete, the opt-in count in Ads Manager matches the contact count in the CRM, and the only symptom is that nobody is being called. That can run for a whole flight. The person who filled in the form saw a thank-you page and is waiting, so the reputational cost lands on the client. Full credit needs the point that the two systems agree with each other while both are wrong about what happened next.
>
> **Q2.** Allowed: the failure mode, that a coded form can drop the submission and the attribution together while showing success to the person filling it in. Not allowed: treating the hidden-native-form bridge as a working recipe. It is one operator, no test, no data, and the demo failed while he was recording it, and he says outright he does not know how it works. **The thing worth copying exactly is his check**: submit a real entry yourself and go and find it in the platform's own record before traffic touches the page. The check is the durable part of a T3 claim. The build is not.
>
> **Q3.** Ordered: settle the six questions and the consent line; map the field IDs by pulling them live from the account and match the form input names exactly; deploy the relay with the token as a secret and the location id set; point the form at the real relay URL and the real thank-you URL; decide the tag name and build the GoHighLevel workflow on that exact tag; **then submit one real entry yourself and find that contact in GoHighLevel with the tag on it and the workflow showing it enrolled**; then delete the test contact; then lock the allowed origin to the real domain. Step six is the proof, and it is the only step that tests both halves at once. Differences from Mattia: use one tag name and write it into the workflow doc and the relay code in the same sitting, verify the page you are actually buying traffic to rather than its sibling, and commit the relay code before deploying so the repository and the running Worker cannot disagree. Also fair: warn the owner before creating a live test contact, because their AI caller may fire on it.
>
> **Q4.** Strongest is **the deployed page source**, because it is the artefact the browser actually loads and it names its own funnel key at line 1534. Then the Worker source on disk, since `wrangler deploy` ships the working tree and this is most likely what is running. Then the workflow document, which is genuine evidence that `sd-lead` was never wired, though it is only a document. Then the vault relay note and the hot sheet, both status records that were never updated after the code changed, and they contradict the code and each other. Weakest is **the git repository**, which is the point of the second half: an uncommitted change proves the repository is stale and proves nothing about the deployed Worker, because deployment does not require a commit. The two things to look at are **the live Worker version in the Cloudflare dashboard** and **the GoHighLevel workflow list, checking whether any trigger exists on `sd-lead`**. Full marks require naming both, because either one alone still leaves the lead landing and nobody coming.
>
> **Q5.** Check, in order: **one, does a workflow trigger exist on the exact tag the relay applies**, since that is the most likely break and the cheapest to look at. **Two, do the contacts actually carry that tag**, which separates a relay problem from a workflow problem. **Three, is the workflow published and how is re-entry set**, because an unpublished workflow and a double-enrol guard both produce zero calls. The sentence you must not write is any version of **"the leads were bad"** or "the opt-ins did not qualify". Writing it early is a reporting failure rather than a guess because it names a cause that moves blame onto the client and the traffic, it closes the investigation, and all three checks above are faster than the argument that sentence starts. On MetaTechAI and Phoenix Truxx the real failure was the back end both times and it was argued as lead quality both times. Also worth credit: you must not report the 40 as delivered opt-ins without stating that none were contacted, because a report showing only the top of the funnel reads as success.

---

**Sources in the codex:** [[Attribution & Incrementality#AT-114|AT-114]] (T3), [[Attribution & Incrementality#AT-030|AT-030]] (T3), [[Attribution & Incrementality#AT-057|AT-057]] (T2).

**Account facts read this run, all from the files themselves:** `Clients/Mattia-Spinal-Rhab [Chiropraise]/Funnel/10-spinal-decompression-landing-page.html` (lines 1247, 1533-1534), `11-shockwave-therapy-landing-page.html` (line 1111), `01-spinal-decompression-multistep-form.html` (line 516), `ghl-relay/src/worker.js` with `git diff HEAD` and `git log`, `ghl-relay/GHL-WORKFLOW-SETUP.md`. Vault: [[Mattia GHL Lead Relay - 2026-07-07]], [[Free GHL Lead Relay (Cloudflare Worker)]], [[Mattia Spinal Care - Landing Page URLs - 2026-07-08]], [[Mattia Spinal Care/_HOT|Mattia hot sheet]], [[MetaTechAI Front Door and Domain Decision 2026-08-27]].

**Previous lesson:** [[2026-09-05 Lesson 017 - A Spend Floor Is a Share, Not a Dollar]]
