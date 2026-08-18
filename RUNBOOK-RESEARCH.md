# RUNBOOK: Daily Research run

You are the Advertising Science Engine's research pass. Work this exact sequence. Paths are relative to the workspace root `E:\claude code marketing skill`. The vault science wing is `Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\`.

## 1. Harvest YouTube

Run:

```
"E:\claude code marketing skill\.venv-research\Scripts\python.exe" ".claude\skills\advertising-science\lib\harvest.py" daily
```

The last stdout line is a JSON summary. `new_transcripts` lists the markdown files written to the vault. Errors in the summary get one line each in the run log; a listing failure for one channel must not abort the rest.

## 2. Check the watchlist

Sources and methods: vault `wiki/science/Watchlist.md`.

- RSS sources: fetch the feed, compare item links against `.claude/skills/advertising-science/cache/watchlist-seen.json` (create if missing), collect new items. arXiv: keep only items whose title/abstract hits the keyword filter.
- Scrape/diff sources marked Daily: WebFetch the page, compare against the cached copy in `.claude/skills/advertising-science/cache/`, note changes, refresh the cache.
- Weekly (Mon) sources: only on Mondays.
- TikTok sources: use the Playwright MCP browser (profile `playwright`). If the browser is unavailable in this session, write "TikTok check skipped: browser unavailable" in the log and move on.

## 3. Extract and merge claims

For every new transcript (and every relevant watchlist item):

1. Read it fully.
2. Decompose into candidate claims about how advertising systems work or how to operate them. Ignore fluff, promotion, and restatements of already-banked claims.
3. Merge into the codex topic notes per the claim protocol in SKILL.md (match → add source; contradict → contested; new → next ID; fluff → discard).
4. Set `extracted: true` in the transcript's frontmatter.
5. Platform-update items that change how we should operate get a claim AND, if urgent (policy change, deprecation affecting our clients), a ⚠ line at the top of the Harvest Log entry.

Backlog rule: if unextracted transcripts exceed 25, process the 25 most substantive (prefer high-density channels, longer runtime) and leave the rest flagged for tomorrow; never mark a transcript extracted without reading it.

## 4. Update the skill if a law changed

Only if today's merge changed law-level knowledge (new T1/T2, a refutation, a contested core claim): update the "Current laws" hot layer in SKILL.md. Most days this step does nothing.

## 5. Log and finish

- Append one entry to `wiki/science/Harvest Log.md`: date, transcripts in, claims added/merged/contested, watchlist findings, gaps noticed. A quiet day gets exactly one line: "YYYY-MM-DD: nothing new."
- Write `.claude/skills/advertising-science/runs/<date>-research-log.md` with the same summary plus errors.
- Commit and push the vault (same practice as the weekly reports).
- Run `.claude/skills/advertising-science/bin/Sync-TeamRepo.ps1` to publish the updated skill + codex snapshot to `EverythingAI-Pro/advertising-science` for the team. It commits and pushes only when something changed; log its one-line result.

## Honesty rules

Real findings only. A claim you did not actually read the source for does not get banked. Never inflate a day's haul; "nothing new" is a valid, good result. No em dashes, no contrast negating.
