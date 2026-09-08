import re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\Halil\.gemini\antigravity-ide\brain\c6d98a08-2e4f-4268-9dc3-134a590c7dc4\.system_generated\steps\1052\content.md'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

print('HTML length:', len(html))

page_count = re.findall(r'"page_count":\s*(\d+)', html)
print('Page count:', page_count)

outer_pages = re.findall(r'class="[^"]*outer_page[^"]*"', html)
print('Outer pages:', len(outer_pages))

title_m = re.findall(r'<title>(.*?)</title>', html)
print('Title:', title_m)

# Search for any text content inside page divs
page_divs = re.findall(r'<div[^>]*class="[^"]*outer_page[^"]*"[^>]*>(.*?)</div>\s*</div>', html, re.DOTALL)
print('Page divs matched:', len(page_divs))

# Search for access_key or documentId
doc_id = re.findall(r'"document_id":\s*(\d+)', html)
access_key = re.findall(r'"access_key":\s*"([^"]+)"', html)
print('Doc ID:', doc_id, 'Access Key:', access_key)

# Check for JSON blobs
for m in re.finditer(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', html, re.DOTALL):
    print('LD JSON:', m.group(1)[:200])

# Search for text content or preview
text_content = re.findall(r'<span class="a[^"]*"[^>]*>(.*?)</span>', html)
print('Sample text spans:', len(text_content))
if text_content:
    print('First 10 spans:', text_content[:10])
