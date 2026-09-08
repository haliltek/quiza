import os
import requests
import fitz

pdf_urls = {
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

results = {}

for year, url in pdf_urls.items():
    path = os.path.join(out_dir, f"{year}.pdf")
    if not os.path.exists(path) or os.path.getsize(path) < 10000:
        print(f"Downloading {year} ({url})...")
        try:
            r = requests.get(url, headers=headers, timeout=25)
            if r.status_code == 200 and len(r.content) > 10000:
                with open(path, "wb") as f:
                    f.write(r.content)
                print(f"  OK: {len(r.content)} bytes")
            else:
                print(f"  FAILED: Status {r.status_code}, len={len(r.content)}")
                continue
        except Exception as e:
            print(f"  ERROR: {e}")
            continue
    
    try:
        doc = fitz.open(path)
        pages = len(doc)
        title = doc[0].get_text()[:120].replace('\n', ' ')
        results[year] = {"pages": pages, "size": os.path.getsize(path), "title": title}
        print(f"[{year}] {pages} pages, {os.path.getsize(path)} bytes. Title: {title[:60]}")
    except Exception as e:
        print(f"[{year}] Error opening PDF: {e}")

print("\n--- Summary of Downloaded PDFs ---")
for y, info in results.items():
    print(f"Year {y}: {info['pages']} pages, {info['size']//1024} KB")
