with open('d:/quiza/scratch_osym/2019_layout.txt', 'r', encoding='utf-8', errors='ignore') as f:
    pages = f.read().split('\x0c')

ans_page = pages[33] if len(pages) >= 34 else pages[-1]
for line in ans_page.split('\n')[5:15]:
    print(repr(line))
