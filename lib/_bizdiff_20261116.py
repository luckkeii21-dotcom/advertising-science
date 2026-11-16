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
keys=sorted(k for k in p if k.startswith('slugs_us_'))
print('last saved US key:',keys[-1])
ukeys=sorted(k for k in p if k.startswith('slugs_uk_'))
print('last saved UK key:',ukeys[-1],'| total saved UK reads:',len(ukeys))
for lab,new,prev_key in (('US',us,keys[-1]),('UK',uk,ukeys[-1])):
    prev=p[prev_key]
    print(f'{lab}: vs {prev_key} added {sorted(set(new)-set(prev))} | removed {sorted(set(prev)-set(new))} | order-identical {new==prev}')
    print(f'{lab}: absent from cumulative -> {sorted(set(new)-cum)}')
states={k:v for k,v in p.items() if k.startswith('slugs_uk_')}
distinct=[]
for k,v in states.items():
    if v not in distinct: distinct.append(v)
print('distinct ordered UK states among saved reads:',len(distinct))
print('UK today order-identical to saved reads:',[k for k,v in states.items() if v==uk])
# commit today's reads
p['slugs_us_2026_11_16']=us
p['slugs_uk_2026_11_16']=uk
p['last_checked']='2026-11-16'
p['result_2026_11_16']='WebFetch both pinned URLs (plain fetch HTTP 400 both); US newest 12 Nov 2026, UK newest 27 Oct 2026; both shelves flat, order-identical'
p['slugs_seen_cumulative']=sorted(cum | set(us) | set(uk))
print('cumulative after:',len(p['slugs_seen_cumulative']))
json.dump(d, open(P,'w',encoding='utf-8'), indent=2)
print('committed')
