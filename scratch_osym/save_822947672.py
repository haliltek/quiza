import urllib.request, re, sys
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.scribd.com/embeds/822947672/content'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
with urllib.request.urlopen(req) as resp:
    c = resp.read().decode('utf-8', errors='ignore')

with open('d:/quiza/scratch_osym/scribd_822947672.html', 'w', encoding='utf-8') as f:
    f.write(c)

m = re.findall(r'pageNum:\s*(\d+).*?contentUrl:\s*"([^"]+)"', c, re.DOTALL)
print(f"Total pages for 822947672: {len(m)}")
if m:
    print(f"Page 1: {m[0]}")
    print(f"Page 5: {[x for x in m if x[0] == '5']}")
