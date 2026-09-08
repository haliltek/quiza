import os, re
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

html_urls = [
    "http://www.osym.gov.tr/TR,3219/2008-kamu-personel-secme-sinavi-lisans-sorulari-ve-yanitlari.html",
    "http://www.osym.gov.tr/TR,3275/2007-kpss1-sorulari-ve-yanitlari.html",
    "http://www.osym.gov.tr/TR,3329/2006-kpss1-sorulari-ve-yanitlari.html",
]

for url in html_urls:
    print(f"Checking {url}...")
    try:
        r = requests.get(url, headers=headers, timeout=15)
        print("  Status:", r.status_code)
        # find pdf links
        pdf_links = re.findall(r'href=[\'"]([^\'"]+\.pdf[^\'"]*)[\'"]', r.text, re.IGNORECASE)
        print("  PDF links found:", pdf_links)
    except Exception as e:
        print("  Error:", e)
