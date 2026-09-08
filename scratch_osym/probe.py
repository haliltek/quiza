import os
import requests
import fitz  # PyMuPDF

urls = {
    "2024": "https://dokuman.osym.gov.tr/pdfdokuman/2024/KPSS/LISANS/GYGK14072024.pdf",
    "2023": "https://dokuman.osym.gov.tr/pdfdokuman/2023/KPSS/LISANS/gygk_23072023nfy.pdf",
    "2022": "https://dokuman.osym.gov.tr/pdfdokuman/2022/KPSS/LISANS/kpss_lisans_gygk_18092022.pdf",
    "2021": "https://dokuman.osym.gov.tr/pdfdokuman/2021/KPSS/SINAVSORULARI/2021_KPSS_Lisans_GYGK.pdf",
    "2020": "https://dokuman.osym.gov.tr/pdfdokuman/2020/KPSS/SINAVSORULARI/2020_KPSS_Lisans_GYGK.pdf",
    "2019": "https://dokuman.osym.gov.tr/pdfdokuman/2019/KPSS/SINAVSORULARI/2019_Lisans_GYGK.pdf",
    "2018": "https://dokuman.osym.gov.tr/pdfdokuman/2018/KPSS/InternetkitapcikGY-GK24072018.pdf",
    "2017": "https://dokuman.osym.gov.tr/pdfdokuman/2017/KPSS/SINAVSORULARI/2017KPSSALANGKGY.pdf",
    "2016": "https://dokuman.osym.gov.tr/pdfdokuman/2016/KPSS/2016KPSSGenelYetenekGenelKultur.pdf",
    "2015": "https://dokuman.osym.gov.tr/pdfdokuman/2015/KPSS/SINAVSORULARI/2015KPSSALANGKGY.pdf",
    "2014": "https://dokuman.osym.gov.tr/pdfdokuman/2014/KPSS/SINAVSORULARI/2014KPSSALANCSGKGY.pdf",
    "2013": "https://dokuman.osym.gov.tr/pdfdokuman/2013/KPSS1/CS.pdf",
    "2012": "https://dokuman.osym.gov.tr/pdfdokuman/2012/KPSS/Lisans/KPSS1_2012_CS_GYGK.pdf",
    "2011": "http://www.osym.gov.tr/Eklenti/1697,kpss1pdf.pdf?0",
    "2010": "https://dokuman.osym.gov.tr/pdfdokuman/2010/KPSS/Lisans/2010kpsscsgenyetgenkul.pdf",
    "2009": "https://dokuman.osym.gov.tr/pdfdokuman/2009/KPSS/Lisans/2009kpsscsgenyetgenkul2.pdf",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

out_dir = "d:/quiza/scratch_osym"
os.makedirs(out_dir, exist_ok=True)

# Test first 2 files
for year, url in list(urls.items())[:2]:
    local_path = os.path.join(out_dir, f"{year}.pdf")
    if not os.path.exists(local_path):
        print(f"Downloading {year} from {url}...")
        r = requests.get(url, headers=headers, timeout=30)
        with open(local_path, "wb") as f:
            f.write(r.content)
        print(f"  Downloaded {len(r.content)} bytes.")
    
    doc = fitz.open(local_path)
    print(f"=== {year} PDF: {len(doc)} pages ===")
    for pno in range(min(4, len(doc))):
        text = doc[pno].get_text()
        print(f"--- Page {pno+1} ({len(text)} chars) ---")
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        for l in lines[:10]:
            print("  ", l)
        print("   ...")
        for l in lines[-5:]:
            print("  ", l)
    
    # Check last page for answer key
    last_text = doc[-1].get_text()
    print(f"--- Last Page ({len(last_text)} chars) ---")
    for l in last_text.split('\n')[:20]:
        if l.strip():
            print("  [LAST PAGE]", l.strip())
