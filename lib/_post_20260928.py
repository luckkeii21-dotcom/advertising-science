import re, sys, urllib.request
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/127.0 Safari/537.36")
url = sys.argv[1]
req = urllib.request.Request(url, headers={"User-Agent": UA})
b = urllib.request.urlopen(req, timeout=60).read().decode("utf-8","replace")
m = re.search(r'<div class=["\']post-body[^>]*>(.*?)</div>\s*<div class=["\']post-footer', b, re.S)
if not m:
    m = re.search(r'<div class=["\']post-body(.*?)<div class=["\']post-footer', b, re.S)
body = m.group(1) if m else "NO POST-BODY MATCH; bytes=%d" % len(b)
body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
body = re.sub(r"<[^>]+>", " ", body)
body = re.sub(r"&nbsp;", " ", body)
body = re.sub(r"&amp;", "&", body)
body = re.sub(r"&#39;", "'", body)
body = re.sub(r"&quot;", '"', body)
body = re.sub(r"[ \t]+", " ", body)
body = re.sub(r"\n\s*\n+", "\n", body)
print(body.strip()[:9000])
