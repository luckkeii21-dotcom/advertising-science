import re, json
from pathlib import Path
p = Path(r"E:\claude code marketing skill\.claude\skills\advertising-science\cache\wk-google-ads-dev-blog.html")
b = p.read_text("utf-8","replace")
entries = re.findall(r"<entry>(.*?)</entry>", b, re.S)
if not entries:
    entries = re.findall(r"<item>(.*?)</item>", b, re.S)
rows=[]
for e in entries[:15]:
    t = re.search(r"<title[^>]*>(.*?)</title>", e, re.S)
    d = re.search(r"<published>(.*?)</published>", e) or re.search(r"<pubDate>(.*?)</pubDate>", e)
    u = re.search(r"<link[^>]*rel=['\"]alternate['\"][^>]*href=['\"](.*?)['\"]", e) or re.search(r"<link>(.*?)</link>", e)
    rows.append({"date": d.group(1) if d else None,
                 "title": re.sub(r"<[^>]+>","", t.group(1)).strip() if t else None,
                 "url": u.group(1) if u else None})
print(json.dumps(rows, indent=2))
