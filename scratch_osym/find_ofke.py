import pymupdf

doc = pymupdf.open('d:/quiza/scratch_osym/2009.pdf')
for i, page in enumerate(doc):
    text = page.get_text()
    if 'öfkelendiriyorsa' in text or 'fkelendiriyorsa' in text or 'öfkelenme' in text:
        print(f"=== PAGE {i+1} ===")
        print(text)
