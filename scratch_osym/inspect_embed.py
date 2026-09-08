import re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/quiza/scratch_osym/scribd_embed.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

print("HTML length:", len(html))

# Search for page count
m_pages = re.findall(r'"page_count":\s*(\d+)', html)
print("Page count:", m_pages)

# Search for outer_page or page divs
page_divs = re.findall(r'class="[^"]*outer_page[^"]*"', html)
print("Outer pages count:", len(page_divs))

# Search for page images
imgs = re.findall(r'<img[^>]+src="([^"]+)"', html)
print("Images found:", len(imgs))
for img in imgs[:5]:
    print("  img:", img)

# Search for text content
text_nodes = re.findall(r'<span class="a[^"]*"[^>]*>(.*?)</span>', html)
print("Text spans found:", len(text_nodes))
if text_nodes:
    print("Sample spans:", text_nodes[:15])

# Search for json or script tags containing doc data
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
for i, s in enumerate(scripts):
    if 'page' in s or 'doc' in s:
        print(f"Script {i} matches: length={len(s)}, preview={repr(s[:100])}")
