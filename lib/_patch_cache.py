import json

P = r"E:\claude code marketing skill\.claude\skills\advertising-science\cache\watchlist-seen.json"
d = json.load(open(P, encoding="utf-8-sig"))

live = [
    "closing-the-creator-measurement-gap",
    "2026-winning-hearts-boosting-carts",
    "conversations-2026-introducing-meta-business-agent",
    "social-search-series-2",
    "social-search-series-3",
    "social-search-series-1",
    "2026-trends-from-around-the-world",
    "meta-growth-drivers-putting-your-digital-marketing-strategy-on-auto-pilot",
    "cyber-5-2025-what-worked",
    "unlocking-the-value-of-q5marketing-for-mobile-game-developers",
    "sports-consumer-research-2025",
    "watch-meta-global-agency-summit",
]

e = d["pages"]["meta-business-news"]
prev = set(e["seen_slugs"])
new = [s for s in live if s not in prev]
result = (
    f"{len(live)} slugs live, {len(new)} new against the {len(prev)}-slug cache union. "
    "Newest date on page still 11 June 2026 (UK format; 0 US-format dates present). "
    "Live slug set identical to 2026-08-20."
)
e.update({
    "last_checked": "2026-08-23",
    "method": "playwright browser (plain fetch returns HTTP 400); slug UNION plus per-page date scan",
    "result": result,
    "seen_slugs": sorted(prev | set(live)),
})

for k in ("tiktok-newsroom", "tiktok-business-blog"):
    d["pages"][k]["last_checked"] = "2026-08-23"
    d["pages"][k]["method"] = "NOT RETRIED"
    d["pages"][k]["result"] = (
        "Deliberately not retried. India geo-block confirmed 2026-08-20 and permanent. "
        "Not an outage. Only the SDK changelog was read, so TikTok is NOT a clean check."
    )

json.dump(d, open(P, "w", encoding="utf-8"), indent=2)
print("new slugs:", new)
print("union size:", len(e["seen_slugs"]))
print(result)
