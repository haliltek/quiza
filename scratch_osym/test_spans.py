import re, sys
sys.stdout.reconfigure(encoding='utf-8')
from test_parse_full_scribd import fetch_page_raw, page_urls

def clean_span_text(html_fragment):
    text = re.sub(r'<[^>]+>', ' ', html_fragment)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def parse_spans_page(raw_html, pnum):
    # Find all span.a elements
    # Pattern: <span class=a style=\"([^\"]*)\">(.*?)</span>
    # Note: spans can have nested spans, so let's match outer span.a
    spans = re.findall(r'<span class=a style=\\"left:(\d+)px;top:(\d+)px;([^"]*)\\"(?:>(.*?))</span>\s*(?=<span class=a|<div|$)', raw_html, re.DOTALL)
    
    # Let's extract items: (left, top, text)
    items = []
    for m in re.finditer(r'<span class=a style=\\"left:(\d+)px;top:(\d+)px;([^"]*)\\"[^>]*>(.*?)(?=(?:<span class=a style=\\"left:|<div class=ff|$))', raw_html, re.DOTALL):
        left = int(m.group(1))
        top = int(m.group(2))
        raw_txt = m.group(4)
        clean_txt = clean_span_text(raw_txt)
        if clean_txt:
            items.append({'left': left, 'top': top, 'text': clean_txt})
            
    # Sort items by top, then left
    items = sorted(items, key=lambda x: (x['top'], x['left']))
    return items

raw = fetch_page_raw(page_urls[5])
items = parse_spans_page(raw, 5)
print(f"Total span items on page 5: {len(items)}")
for i, item in enumerate(items[:20]):
    print(f"[{item['top']}, {item['left']}]: {item['text']}")
