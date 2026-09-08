import re

WATERMARK_WORDS = set(['ösym', 'ösym’ye', 'ösym\'ye', 'telif', 'hakları', 'haklar', 'aittir', 'yazılı', 'yazl',
                       'izni', 'olmaksızın', 'olmakszn', 'hiçbir', 'hibir', 'kişi', 'kisi', 'kurum', 'kuruluş',
                       'kurulua', 'kurulus', 'tarafından', 'tarafndan', 'kullanılamaz', 'kullanlamaz', 'soruların',
                       'sorularn', 'sorular'])

def clean_watermark_text(text):
    # Remove boilerplate sentences
    text = re.sub(r'Bu soruların telif hakları.*?(?:kullanılamaz\.?)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Bu testlerin her hakkı saklıdır.*?(?:sayılır\.?)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Diğer sayfaya geçiniz\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'TEST BİTTİ\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'CEVAPLARINIZI KONTROL EDİNİZ\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'GENEL KÜLTÜR TESTİ BİTTİ\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'GENEL YETENEK TESTİ BİTTİ\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'GENEL KÜLTÜR TESTİNE GEÇİNİZ\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'GENEL YETENEK TESTİNE GEÇİNİZ\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'kısmına işaretleyiniz\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'ayrılan kısmına\.?', '', text, flags=re.IGNORECASE)
    
    # Clean scattered individual watermark tokens
    words = text.split()
    cleaned_words = []
    for w in words:
        w_clean = re.sub(r'[^\w]', '', w).lower()
        if w_clean in WATERMARK_WORDS:
            continue
        # standalone single letters from diagonal watermark like Ö, S, Y, M
        if len(w) == 1 and w.upper() in ['Ö', 'S', 'Y', 'M']:
            continue
        cleaned_words.append(w)
        
    result = ' '.join(cleaned_words)
    # Remove trailing page numbers or question numbers at the end of option or question
    result = re.sub(r'\s+\d{1,2}\s*$', '', result)
    result = re.sub(r'\s+', ' ', result).strip()
    return result

test_str1 = "ara verir - önceliğini S 2. ÖSYM'ye kurum hakları kişi, telif hiçbir soruların Bu 1 kısmına işaretleyiniz. 3. olmaksızın izni kullanılamaz. yazılı ÖSYM'nin tarafından Sorular aittir. kuruluş veya"
print("Cleaned 1:", clean_watermark_text(test_str1))

test_str2 = "Mutlak konumundan 21"
print("Cleaned 2:", clean_watermark_text(test_str2))

test_str3 = "10. sırada 10. sırada TEST BİTTİ. CEVAPLARINIZI KONTROL EDİNİZ."
print("Cleaned 3:", clean_watermark_text(test_str3))
