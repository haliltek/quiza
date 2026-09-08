import pymupdf

doc = pymupdf.open('d:/quiza/scratch_osym/2009.pdf')
for i, page in enumerate(doc):
    text = page.get_text()
    if 'Göktürk' in text or 'Gktrk' in text or 'Budist' in text:
        print(f"=== PAGE {i+1} ===")
        print(text)
