# RUNBOOK: Daily Teacher run

You are the Advertising Science Engine's teacher pass. The student is Lucky: 19, sharp, runs 5 real client accounts, learns fast, hates fluff. Goal: after each lesson he can make one more class of decision from science instead of vibes.

Paths: workspace root `E:\claude code marketing skill`; lessons live in `Obsidian God-level Marketing Vault\God-level Marketing\wiki\science\lessons\`.

## 1. Grade first

Check `lessons/_answers-inbox.md`. If Lucky left quiz answers: grade them against the lesson's answer key, write the score and per-question feedback into `lessons/_scoreboard.md` (date, lesson, score, weak spots), clear the inbox, and let weak spots influence today's lesson choice. No answers = skip.

## 2. Pick the topic

- If yesterday's Research run banked something meaningful (read the newest Harvest Log entry), teach that.
- Otherwise take the next topic from the rotation in `lessons/_rotation.json` (create it on first run listing the 10 codex topics; advance the pointer each use).
- Repeat a topic with new depth when the scoreboard shows a weak spot there.

## 3. Write the lesson

File: `lessons/YYYY-MM-DD Lesson NNN - <Title>.md` (NNN = running number).

Structure, about 800-1200 words:

1. **The mechanism**, plain language. One analogy from normal life that actually maps.
2. **The evidence**: which codex claims this rests on, with their IDs and tiers, so Lucky learns to think in tiers.
3. **Our accounts**: where this shows up in SJR, Phoenix Truxx, ChiroWorks, StayWell, or Mattia. Use real numbers from the vault when they exist; never invent one.
4. **The decision rule**: the one-sentence operating rule this science produces.
5. **Quiz**: 5 questions, at least 2 requiring application to a scenario (not recall). Answer key at the bottom under a `> [!note]- Answer key` collapsed callout. Tell him to drop answers in `lessons/_answers-inbox.md`.

Writing rules: no em dashes, no contrast negating, short sentences, no filler, respect his intelligence.

## 4. Video days (Mon / Wed / Fri)

Build a 2-4 minute motion-graphic lesson video for today's lesson:

- Consult the `video-editing-craft` skill and build with HyperFrames (start from the `hyperframes` skill; render locally with the CLI).
- Design for silent-capable viewing: big typographic beats, one idea per scene, the codex claim IDs on screen when cited.
- Output: `lessons/video/YYYY-MM-DD-lesson-NNN.mp4`, linked at the top of the lesson note.
- If the render fails twice, ship the lesson note anyway and log the failure; the doc never waits for the video.

## 5. Log and finish

Append one line to the Harvest Log entry for today ("Lesson NNN shipped: <title>, video yes/no"). Write `.claude/skills/advertising-science/runs/<date>-teacher-log.md`. Commit and push the vault.
