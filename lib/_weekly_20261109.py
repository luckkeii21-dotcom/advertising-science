"""Monday weekly lane, Google sources, 2026-11-09. Read-only, no cache write."""
import json, re, urllib.request
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*",
                                               "Accept-Language": "en-US,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.status, r.read().decode("utf-8", "replace")

# 1. Google Ads API release notes: VERSION-HEADING set
st, b = fetch("https://developers.google.com/google-ads/api/docs/release-notes")
heads = re.findall(r'<h2[^>]*>(?:<[^>]+>)*([^<]{2,80})', b)
vers = sorted(set(re.findall(r"\bv(\d{2})\b", b)), reverse=True)[:6]
print("RELEASE NOTES HTTP", st, len(b), "bytes")
print("  h2 headings:", [h.strip() for h in heads][:12])
print("  version tokens:", vers)

# 2. Google Ads Developer Blog, Feedburner Atom: titles + dates
st, b = fetch("http://feeds.feedburner.com/GoogleAdsDeveloperBlog")
ents = re.findall(r"<entry>(.*?)</entry>", b, re.S)
print("\nDEV BLOG HTTP", st, len(b), "bytes,", len(ents), "entries")
for e in ents[:5]:
    t = re.search(r"<title[^>]*>(.*?)</title>", e, re.S)
    d = re.search(r"<published>(.*?)</published>", e, re.S)
    print("  ", (d.group(1)[:10] if d else "?"), re.sub(r"<[^>]+>", "", t.group(1)).strip()[:110] if t else "?")

# 3. Merchant Center changelog: answer-id SET
st, b = fetch("https://support.google.com/merchants/announcements/6192467")
ids = sorted(set(re.findall(r"/merchants/answer/(\d+)", b)), key=int)
print("\nMERCHANT CENTER HTTP", st, len(b), "bytes")
print("  answer ids:", len(ids))
open(r"E:\claude code marketing skill\.claude\skills\advertising-science\cache\_wk_mc_20261109.txt", "w").write("\n".join(ids))
