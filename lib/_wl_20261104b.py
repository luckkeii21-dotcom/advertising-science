# Pass-2 2026-11-04: record the UK date-format defect fix in Watchlist.md and the cache.
import io, json, shutil, datetime

SCI = r"E:\claude code marketing skill\Obsidian God-level Marketing Vault\God-level Marketing\wiki\science"
WL = SCI + r"\Watchlist.md"
CACHE = r"E:\claude code marketing skill\.claude\skills\advertising-science\cache\watchlist-seen.json"

NOTE = """
**Transport and parsing note, 2026-11-04 pass 2. THE UK SHELF HAS ALWAYS CARRIED CARD DATES AND OUR OWN REGEX COULD NOT SEE THEM.** The 04:46 pass recorded the US body as carrying 24 parseable card dates and the UK body as carrying zero, and concluded that a UK read needing a date ceiling still had to go through WebFetch. **That conclusion is wrong and is retired here.** Re-parsing the UK body saved this morning (`cache/bn-uk-20261104.html`, 231,511 bytes) finds **24 parseable card dates, 8 distinct, newest 27 October 2026**, confirming the ceiling that had been carried over from yesterday unverified. The two shelves render dates in **different formats**, and our parser only ever tries one of them:

| Shelf | Rendered format | Example |
|---|---|---|
| `?locale=en_US` | month first, with a comma | `October 28, 2026` |
| `en-gb` host | **day first, no comma, no ordinal suffix** | `27 October 2026` |

**So the fix is a second pattern, not a different transport.** Accept `(\\d{1,2})\\s+(Month)\\s+(20\\d\\d)` alongside the existing `(Month)\\s+(\\d{1,2}),\\s+(20\\d\\d)`, and keep the ordinal-optional `(st|nd|rd|th)?` the Merchant Center lane already needs, because none of the three forms covers the other two. The ordinal form matched zero times on both bodies today, so the ordinal bug and this one are separate defects on separate sources.

**Ceilings confirmed from today's own bodies, both locales, no WebFetch and no browser:** US newest **28 October 2026** (9 distinct dates, 15 September to 28 October), UK newest **27 October 2026** (8 distinct dates, 14 May to 27 October). The UK shelf reaching back to May against the US shelf's September is a separate observation worth keeping: the two shelves rotate at different speeds, so a slug ageing off the UK shelf is weaker evidence of a publishing event than the same slug ageing off the US one.

**Plain fetch returned HTTP 400 on both pinned URLs at 18:42 IST**, roughly 14 hours after both answered HTTP 200 at 04:49. That is the fourth separate confirmation that the 400 is intermittent rather than a wall, and the first measurement of how fast a working window closes. Route order is unchanged: plain fetch, then WebFetch, then the browser. **No second shelf read was attempted or is owed**, under the one-read-per-day rule of 2026-10-09, which three pass-2 re-reads have now shown buys no coverage.
"""

t = io.open(WL, encoding="utf-8").read()
anchor = "**Transport note, 2026-10-25."
i = t.index(anchor)
j = t.index("\n\n", i)
out = t[:j] + "\n" + NOTE.rstrip() + t[j:]
io.open(WL, "w", encoding="utf-8").write(out)
print("Watchlist.md note inserted, %d -> %d chars" % (len(t), len(out)))

shutil.copy(CACHE, CACHE + ".bak-20261104-pass2")
c = json.load(io.open(CACHE, encoding="utf-8"))
p = c["pages"]["meta-business-news"]
p["note_2026_11_04_pass2_uk_date_format"] = (
    "DEFECT IN OUR OWN PARSER, FOUND AND NOT YET FIXED IN CODE. The morning pass reported the UK body "
    "carrying zero parseable card dates. It carries 24, 8 distinct, newest 27 October 2026. The en-gb host "
    "renders dates DAY FIRST with no comma and no ordinal suffix ('27 October 2026'); the ?locale=en_US shelf "
    "renders them month first with a comma ('October 28, 2026'). Our parser only tries the US form. FIX: accept "
    "both, plus the ordinal-optional form the Merchant Center lane needs; the ordinal form matched 0 times on "
    "both bodies today, so it is a separate defect on a separate source. Consequence: the standing instruction "
    "that a UK date ceiling needs WebFetch is RETIRED, the plain-fetch body is sufficient. Also: the UK shelf "
    "reaches back to 14 May 2026 while the US shelf stops at 15 September 2026, so the two shelves rotate at "
    "different speeds and a slug ageing off the UK shelf is weak evidence of a publishing event."
)
p["note_2026_11_04_pass2_transport"] = (
    "Plain fetch HTTP 400 on BOTH pinned URLs at 18:42 IST, about 14 hours after both answered HTTP 200 at 04:49. "
    "Fourth confirmation the 400 is intermittent, and the first measurement of how fast a working window closes. "
    "No second shelf read attempted or owed (one-read-per-day rule, 2026-10-09)."
)
p["result_2026_11_04_pass2"] = (
    "NO NEW READ. Shelves read once today at 04:49 (HTTP 200 both, 12 slugs each, 0 new, 4th consecutive flat day). "
    "Pass 2 re-parsed the SAVED bodies only and closed the UK date-ceiling gap: UK newest 27 October 2026 confirmed "
    "from today's own body rather than carried from yesterday. US newest 28 October 2026."
)
p["last_checked"] = "2026-11-04"
json.dump(c, io.open(CACHE, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("cache updated; meta-business-news keys now", len(p))
