"""Monday weekly lane, 2026-11-16. Read-only diffs, caches bodies."""
import re, urllib.request, os
UA=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
C=r"E:\claude code marketing skill\.claude\skills\advertising-science\cache"
def fetch(url, timeout=90):
    req=urllib.request.Request(url, headers={"User-Agent":UA,"Accept":"*/*","Accept-Language":"en-US,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read().decode("utf-8","replace")

def try_(label, fn):
    print("\n==",label,"==")
    try: fn()
    except Exception as e: print("  FAIL:",type(e).__name__,e)

# 1. Google Ads API release notes
def g1():
    st,b=fetch("https://developers.google.com/google-ads/api/docs/release-notes")
    print("  HTTP",st,len(b),"bytes")
    vers=sorted(set(re.findall(r"\bv(\d{2})\b", b)), reverse=True)[:8]
    print("  version tokens:",vers)
    heads=[h.strip() for h in re.findall(r'<h2[^>]*>(?:<[^>]+>)*([^<]{2,80})', b)][:12]
    print("  h2:",heads)
    open(os.path.join(C,"_wk_relnotes_20261116.html"),"w",encoding="utf-8").write(b)
try_("GOOGLE ADS API RELEASE NOTES", g1)

# 2. Google Ads Developer Blog
def g2():
    st,b=fetch("http://feeds.feedburner.com/GoogleAdsDeveloperBlog")
    ents=re.findall(r"<entry>(.*?)</entry>", b, re.S)
    print("  HTTP",st,len(b),"bytes,",len(ents),"entries")
    for e in ents[:6]:
        t=re.search(r"<title[^>]*>(.*?)</title>", e, re.S)
        d=re.search(r"<published>(.*?)</published>", e, re.S)
        print("   ",(d.group(1)[:10] if d else "?"), re.sub(r"<[^>]+>","",t.group(1)).strip()[:110] if t else "?")
    open(os.path.join(C,"_wk_devblog_20261116.xml"),"w",encoding="utf-8").write(b)
try_("GOOGLE ADS DEVELOPER BLOG", g2)

# 3. Merchant Center changelog: answer-id SET diff vs 11-09
def g3():
    st,b=fetch("https://support.google.com/merchants/announcements/6192467")
    ids=sorted(set(re.findall(r"/merchants/answer/(\d+)", b)), key=int)
    print("  HTTP",st,len(b),"bytes, answer ids:",len(ids))
    prevp=os.path.join(C,"_wk_mc_20261109.txt")
    if os.path.exists(prevp):
        prev=set(open(prevp).read().split())
        print("  vs 11-09: added",sorted(set(ids)-prev),"removed",sorted(prev-set(ids)))
    open(os.path.join(C,"_wk_mc_20261116.txt"),"w").write("\n".join(ids))
try_("MERCHANT CENTER CHANGELOG", g3)

# 4. Meta Marketing API changelog
def m1():
    st,b=fetch("https://developers.facebook.com/docs/marketing-api/marketing-api-changelog")
    print("  HTTP",st,len(b),"bytes")
    vs=sorted(set(re.findall(r"\bv(\d{1,2})\.0\b", b)), key=lambda x:int(x), reverse=True)[:8]
    print("  version tokens:",vs)
    for kw in ("gender","demographic","targeting","October 2026","November 2026"):
        print(f"  '{kw}' occurrences:", len(re.findall(kw, b, re.I)))
    open(os.path.join(C,"_wk_mktapi_20261116.html"),"w",encoding="utf-8").write(b)
try_("META MARKETING API CHANGELOG", m1)

# 5. Meta Graph API changelog
def m2():
    st,b=fetch("https://developers.facebook.com/docs/graph-api/changelog")
    print("  HTTP",st,len(b),"bytes")
    vs=sorted(set(re.findall(r"\bv(\d{1,2})\.0\b", b)), key=lambda x:int(x), reverse=True)[:8]
    print("  version tokens:",vs)
    open(os.path.join(C,"_wk_graphapi_20261116.html"),"w",encoding="utf-8").write(b)
try_("META GRAPH API CHANGELOG", m2)

# 6. Meta Advertising Standards
def m3():
    st,b=fetch("https://transparency.meta.com/policies/ad-standards/")
    print("  HTTP",st,len(b),"bytes")
    open(os.path.join(C,"_wk_adstd_20261116.html"),"w",encoding="utf-8").write(b)
try_("META ADVERTISING STANDARDS", m3)

# 7. AI at Meta blog
def m4():
    st,b=fetch("https://ai.meta.com/blog/")
    print("  HTTP",st,len(b),"bytes")
    titles=re.findall(r'<h[23][^>]*>(?:<[^>]+>)*([^<]{6,120})', b)[:10]
    print("  headings:",[t.strip() for t in titles])
    open(os.path.join(C,"_wk_aimeta_20261116.html"),"w",encoding="utf-8").write(b)
try_("AI AT META BLOG", m4)
