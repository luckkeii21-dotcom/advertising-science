import pathlib
V = pathlib.Path(r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science")
w = V / "Watchlist.md"
t = w.read_text(encoding="utf-8")

add = """

### Meta for Business News: a rotated-out slug can come BACK, so the shelf ceiling is not monotonic (2026-10-09)

| Locale | Ceiling | Slugs | Against the 2026-10-08 baseline |
|---|---|---|---|
| `?locale=en_US` | **8 October 2026** | 12 | **1 added, 1 removed** |
| `?locale=en_GB` | **10 September 2026, down from 6 October** | 12 | **1 added, 1 removed, both rotation** |

**Added on the US shelf and read in full at source:** `muse-smb-bennett-orchards`, "The Second Brain on a Sixth-Generation Farm", 8 October 2026. A Muse for Small Business customer story about a 50-acre Delaware fruit farm. **Every named use case is back office or agronomy and not one is advertising**, so it gets no ID and is filed as a dated watch note on [[Meta Delivery & Andromeda#MD-169|MD-169]], the claim that banks Muse connecting to ad accounts and drafting campaigns. **Rotated out:** `holiday-measurement-strategies`.

**The finding, and it corrects an assumption every entry above carries.** `creator-marketing-whitepaper` was yesterday's UK addition. Today it is gone from the UK shelf and `unlocking-the-value-of-q5marketing-for-mobile-game-developers` (10 October 2025) is back in its place, which is the same slug that rotated OUT yesterday to make room for it. So the rotation runs both ways over a single day, and the UK ceiling went **backwards**, from 6 October 2026 to 10 September 2026.

**Two standing rules come out of that.** First, **never report a ceiling drop on this source as a removal, an unpublishing or a retraction.** The white paper is still live at its own URL; only the shelf slice changed. Second, **a slug that has been read once must stay read.** The seen-set has to be cumulative, because a slug can leave and return and would otherwise re-fire as new. The committed baselines are per-date snapshots, so a future run diffing against yesterday alone will eventually re-read a post it already banked.

**And the locale gap is now confirmed worthless as a number, for the third run running.** It has read 11 days, 26 days, 0 days and today 28 days inside nine days. The 2026-10-08 entry already said to stop quoting it. Today it moved 28 days on a day when neither shelf published anything new in the UK. **The two-locale read still earns its place for the opposite reason: today the UK shelf was pure rotation and the US shelf carried the day's only new platform document, which is the reverse of yesterday.**

**Transport.** WebFetch rendered both locales on the first attempt, no Playwright profile used or needed. **Sixth consecutive browser-free read of both shelves.** The slug diff needed zero punctuation adjudication for the fourth run running.
"""

assert t.rstrip().endswith("Bank the article's own date, not the card's.")
w.write_text(t.rstrip() + add, encoding="utf-8")
print("Watchlist.md appended")
