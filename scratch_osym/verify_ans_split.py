import re

with open('d:/quiza/scratch_osym/2019_layout.txt', 'r', encoding='utf-8', errors='ignore') as f:
    pages = f.read().split('\x0c')

ans_page = pages[33] if len(pages) >= 34 else pages[-1]
ans_keys = {'GY': {}, 'GK': {}}

lines = ans_page.split('\n')
for l in lines:
    m = list(re.finditer(r'(\d{1,2})\.\s+([A-E])\b', l))
    for match in m:
        qnum = int(match.group(1))
        ans = match.group(2).lower()
        if match.start() < 50:
            ans_keys['GY'][qnum] = ans
        else:
            ans_keys['GK'][qnum] = ans

print(f"GY count: {len(ans_keys['GY'])}, GK count: {len(ans_keys['GK'])}")
print("GY 1-10:", [ans_keys['GY'].get(i) for i in range(1, 11)])
print("GK 1-10:", [ans_keys['GK'].get(i) for i in range(1, 11)])
