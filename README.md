# Advertising Science

The EvrythingAI advertising science skill. A tiered claims codex on how Meta, Google, and TikTok advertising actually works, plus the operating laws distilled from it, packaged as a Claude Code skill for every ad decision: planning, structure, scaling, bidding, optimization events, creative volume, attribution, forecasting.

Built and updated by an automated research engine: 12 vetted practitioner YouTube channels harvested daily, official platform sources monitored (Meta engineering, Google Ads docs and announcements, TikTok docs, arXiv), every claim merged into the codex with an evidence tier.

## The tier system, in one breath

**T1** platform docs and engineering posts. **T2** a real test with shown data. **T3** practitioner claim from real spend, no shown test. **T4** theory. T1/T2 can decide; a T3-only decision is a named bet; T4 never decides. Contradictions are kept as `contested` with both sides, never silently overwritten.

## Install (Claude Code)

Clone into your skills directory:

```
# for one project
git clone https://github.com/EverythingAI-Pro/advertising-science.git .claude/skills/advertising-science

# or for every project on your machine
git clone https://github.com/EverythingAI-Pro/advertising-science.git ~/.claude/skills/advertising-science
```

Claude Code picks it up automatically. It triggers on media buying decisions and on phrases like "what does the science say", "Andromeda", "should I scale this", or invoke it directly with `/advertising-science`.

## Update

```
git pull
```

The engine pushes a fresh sync every morning after the daily research run (about 07:30 IST), but only on days something actually changed. Pull whenever you want the latest; pulling daily is ideal.

## What's inside

- `SKILL.md` — the protocol and the current laws (the hot layer)
- `references/codex/` — the full codex: 10 topic notes of tiered claims, the channel roster, the source watchlist, and the Harvest Log (the day-by-day changelog)
- `references/lessons/` — the daily teaching lessons with quizzes
- `lib/`, `bin/`, `RUNBOOK-*.md` — the research engine itself. It runs on Lucky's machine; you do not need to run anything.

## Rules for the team

- **Do not edit codex or lesson files in this repo.** The engine overwrites them on the next sync. Found an error or have a claim to add? Tell Lucky or open an issue; it enters through the engine so it gets tiered, sourced, and deduplicated.
- When you use a claim to justify a decision, say its ID and tier out loud ("MD-003, T3"). That habit is the whole point.
- Client account data beats the codex. When your account contradicts a claim, that is a finding; report it so the claim gets contested or upgraded.
