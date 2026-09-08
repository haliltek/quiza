import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open('d:/quiza/scratch_osym/2019.pdf')

# Find GY 6
for pno in range(len(doc)):
    txt = doc[pno].get_text()
    if '6.' in txt and ('roman' in txt or 'Uykuların Doğusu' in txt or 'romanıma' in txt):
        print(f"GY 6 found on page {pno+1}:")
        for b in doc[pno].get_text('blocks'):
            if b[0] < 300: # left col
                print("L:", b[4].strip()[:100])
            else:
                print("R:", b[4].strip()[:100])
        break
