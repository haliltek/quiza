import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open('d:/quiza/scratch_osym/2019.pdf')
p = doc[2]
words = p.get_text('words')
for w in words:
    if any(w[4].startswith(opt) for opt in ['A)', 'B)', 'C)', 'D)', 'E)', 'A', 'B', 'C', 'D', 'E']):
        if len(w[4]) <= 3:
            print(f'x0={w[0]:.1f}, y0={w[1]:.1f}, txt="{w[4]}"')
