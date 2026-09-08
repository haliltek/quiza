import pymupdf
import re

def inspect_pdf(pdf_path, year):
    doc = pymupdf.open(pdf_path)
    print(f"==================== {year} ({len(doc)} pages) ====================")
    
    # Check for "DOĞRU CEVAP" in text across all pages
    total_answers_found = 0
    pages_with_answers = []
    for i, page in enumerate(doc):
        text = page.get_text()
        matches = re.findall(r'DOĞRU CEVAP\s*:\s*([A-E])', text, re.IGNORECASE)
        if matches:
            total_answers_found += len(matches)
            pages_with_answers.append(i + 1)
            
    print(f"Inline answers ('DOĞRU CEVAP:'): {total_answers_found} found on pages {pages_with_answers[:10]}...")
    
    # Check last 3 pages for Answer Key table
    for p in range(max(0, len(doc)-3), len(doc)):
        txt = doc[p].get_text()
        if "CEVAP" in txt.upper():
            print(f"Page {p+1} mentions CEVAP:")
            lines = [l.strip() for l in txt.split('\n') if l.strip()][:15]
            print("   " + "\n   ".join(lines))

for y in [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2010, 2009]:
    inspect_pdf(f"d:/quiza/scratch_osym/{y}.pdf", y)
