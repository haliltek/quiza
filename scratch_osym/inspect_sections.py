import fitz, os

for year in ["2024", "2020", "2017", "2014", "2013", "2010", "2009"]:
    path = f"d:/quiza/scratch_osym/{year}.pdf"
    if not os.path.exists(path): continue
    doc = fitz.open(path)
    print(f"\n================ {year}.pdf ({len(doc)} pages) ================")
    headers = set()
    for pno in range(len(doc)):
        txt = doc[pno].get_text()
        first_lines = [l.strip() for l in txt.split('\n') if l.strip()][:5]
        for l in first_lines:
            if any(k in l.upper() for k in ["GENEL YETENEK", "GENEL KÜLTÜR", "GENEL KULTUR", "HUKUK", "İKTİSAT", "CEVAP ANAHTARI", "TESTİ"]):
                headers.add(l)
    print("Found test sections / headers:")
    for h in sorted(headers):
        print("  -", h)
