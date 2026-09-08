import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open('d:/quiza/scratch_osym/2019.pdf')
p = doc[2]
words = p.get_text('words')
for w in words:
    if w[0] < 60: # left margin
        print(f'x0={w[0]:.1f}, y0={w[1]:.1f}, txt="{w[4]}"')
