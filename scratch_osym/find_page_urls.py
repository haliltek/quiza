import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/quiza/scratch_osym/scribd_embed.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Search for scribdassets
urls = re.findall(r'https?://[^"\'\s>]+scribdassets\.com[^"\'\s>]*', html)
print("Unique scribdassets URLs found:", len(set(urls)))
for u in sorted(set(urls))[:15]:
    print(" ", u)

# Check Script 105 (prefetchResource)
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
if len(scripts) > 105:
    print("\nScript 105:")
    print(scripts[105][:500])

# Check how addPage is called in Script 103
if len(scripts) > 103:
    print("\nScript 103 snippet:")
    print(scripts[103][:600])
