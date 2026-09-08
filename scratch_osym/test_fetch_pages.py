import re, urllib.request, gzip, sys
sys.stdout.reconfigure(encoding='utf-8')

# Extract all page URLs from scribd_embed.html
with open('d:/quiza/scratch_osym/scribd_embed.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Pattern for addPage: pageNum and contentUrl
matches = re.findall(r'pageNum:\s*(\d+).*?contentUrl:\s*"([^"]+)"', html, re.DOTALL)
print(f"Total pages with contentUrl: {len(matches)}")

page_urls = {int(p): url for p, url in matches}

def fetch_page_text(pnum):
    if pnum not in page_urls:
        return f"[Page {pnum} not in contentUrls]"
    url = page_urls[pnum]
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            raw = resp.read()
            if raw[:2] == b'\x1f\x8b':
                data = gzip.decompress(raw).decode('utf-8', errors='ignore')
            else:
                data = raw.decode('utf-8', errors='ignore')
            # Extract plain text from HTML
            # Replace span/div tags
            text = re.sub(r'<[^>]+>', ' ', data)
            text = re.sub(r'&nbsp;', ' ', text)
            text = re.sub(r'\s+', ' ', text).strip()
            return text
    except Exception as e:
        return f"[Error fetching {pnum}: {e}]"

for p in range(4, 12):
    txt = fetch_page_text(p)
    print(f"\n==================== PAGE {p} (Length: {len(txt)}) ====================")
    print(txt[:600])
