import fitz # PyMuPDF

doc = fitz.open('d:/quiza/scratch_osym/2009.pdf')
print("Total pages:", len(doc))
for i, page in enumerate(doc):
    text = page.get_text()
    if '60.' in text or '60 ' in text:
        print(f"--- Page {i+1} ---")
        lines = [l for l in text.split('\n') if l.strip()]
        for l in lines[-30:]:
            print(l)
