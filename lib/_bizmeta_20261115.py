import json
P='cache/watchlist-seen.json'
d=json.load(open(P,encoding='utf-8'))
p=d['pages']['meta-business-news']
us=["from-measurement-to-capital-allocation","finding-his-squad-again-in-a-facebook-group",
"how-metas-ads-system-matches-your-ad-to-the-right-person","three-new-ai-innovations-in-ads-ranking",
"you-dont-beat-the-auction-you-brief-it","muse-smb-jaeluxe-shoetique",
"agencies-testing-incrementality","meta-nest-ai-creative-diversification",
"meta-brand-building-summit-2026","muse-smb-bennett-orchards",
"a-new-way-for-businesses-and-personal-agents-to-work-together","advertising-week-new-york-2026"]
uk=["meta-ai-now-available-in-hongkong","meta-agency-first-awards-winners-hongkong-2026",
"meta-marketing-summit-hongkong-2026","you-dont-beat-the-auction-you-brief-it",
"performance-spotlight-how-instant-hydration-built-a-system-for-ai-to-scale",
"businesses-driving-results-with-meta-ai-ads","closing-the-creator-measurement-gap",
"2026-winning-hearts-boosting-carts","conversations-2026-introducing-meta-business-agent",
"social-search-series-2","social-search-series-3","social-search-series-1"]
cum=set(p['slugs_seen_cumulative'])
print('cumulative before:',len(cum))
for lab,new,prev_key in (('US',us,'slugs_us_2026_11_13'),('UK',uk,'slugs_uk_2026_11_13')):
    prev=p[prev_key]
    print(f'{lab}: added vs 11-13 {sorted(set(new)-set(prev))} | removed {sorted(set(prev)-set(new))} | order-identical {new==prev}')
    print(f'{lab}: absent from cumulative -> {sorted(set(new)-cum)}')
# compare UK against all saved UK states
states={k:v for k,v in p.items() if k.startswith('slugs_uk_')}
matches=[k for k,v in states.items() if v==uk]
print('UK order-identical saved reads:',len(matches),matches[-6:])
