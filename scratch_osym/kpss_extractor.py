import sys, os, re
sys.path.append(r'd:\quiza\scratch_osym')
import pymupdf
from parse_answer_keys import parse_answer_keys

def extract_lines_from_words(words):
    lines = []
    words = sorted(words, key=lambda item: (item[1], item[0]))
    cur_line = []
    cur_y = None
    for word in words:
        if cur_y is None:
            cur_y = word[1]
            cur_line.append(word)
        elif abs(word[1] - cur_y) < 4.5:
            cur_line.append(word)
        else:
            cur_line.sort(key=lambda item: item[0])
            lines.append(' '.join(item[4] for item in cur_line))
            cur_line = [word]
            cur_y = word[1]
    if cur_line:
        cur_line.sort(key=lambda item: item[0])
        lines.append(' '.join(item[4] for item in cur_line))
    return lines

def get_subcategory_mapping(category, qnum, qtext):
    q_lower = qtext.lower()
    if category == 1: # Tarih
        if any(k in q_lower for k in ['hun', 'göktürk', 'uygur', 'iskit', 'kutluk', 'kurultay', 'islamiyet öncesi', 'töre', 'kağan', 'hakan', 'balbal', 'toygun']):
            return 1 # İslamiyet Öncesi Türk Tarihi
        elif any(k in q_lower for k in ['karahanlı', 'gazneli', 'selçuklu', 'dandanakan', 'malazgirt', 'divanü lügat', 'kutadgu bilig', 'nizamiye', 'atabey']):
            return 2 # İlk Türk-İslam Devletleri
        elif any(k in q_lower for k in ['osman bey', 'orhan bey', 'fatih', 'yavuz', 'kanuni', 'rumeli', 'istimalet', 'tımar', 'devşirme', 'yükselme']):
            return 3 # Osmanlı Devleti Kuruluş & Yükselme
        elif any(k in q_lower for k in ['ilmiye', 'seyfiye', 'kalemiye', 'divan-ı hümayun', 'bedesten', 'kervansaray', 'vakıf', 'lonca', 'medrese', 'enderun', 'şeriat', 'örfi']):
            return 4 # Osmanlı Kültür ve Medeniyeti
        elif any(k in q_lower for k in ['mondros', 'sevr', 'amasya', 'erzurum', 'sivas kongresi', 'kuva-yı milliye', 'misakımilli', 'inönü', 'sakarya', 'büyük taarruz', 'lozan', 'mudanya']):
            return 5 # Kurtuluş Savaşı ve Cepheler
        elif any(k in q_lower for k in ['atatürk', 'inkılap', 'laiklik', 'cumhuriyetçilik', 'halifeliğin kaldırılması', 'saltanatın kaldırılması', 'medeni kanun', 'harf inkılabı', 'menemen', 'şeyh sait']):
            return 6 # Atatürk İlkeleri ve İnkılap Tarihi
        elif any(k in q_lower for k in ['ikinci dünya savaşı', 'birinci dünya savaşı', 'soğuk savaş', 'kore savaşı', 'nato', 'varşova', 'kıbrıs', 'avrupa birliği', 'balkan antantı', 'sadabat']):
            return 7 # Çağdaş Türk ve Dünya Tarihi
        # Fallback by question number
        if qnum <= 3: return 1
        elif qnum <= 6: return 2
        elif qnum <= 10: return 3
        elif qnum <= 13: return 4
        elif qnum <= 19: return 5
        elif qnum <= 24: return 6
        else: return 7

    elif category == 2: # Coğrafya
        if any(k in q_lower for k in ['paralel', 'meridyen', 'enlem', 'boylam', 'jeopolitik', 'matematik konum', 'özel konum', 'yerel saat', 'saat dilimi', 'uç nokta']):
            return 8 # Türkiye Coğrafi Konumu ve Etkileri
        elif any(k in q_lower for k in ['dağ', 'plato', 'ova', 'delta', 'vadi', 'kıyı', 'karstik', 'fay', 'deprem', 'volkan', 'göl', 'akarsu', 'morfoloj']):
            return 9 # Türkiye Yer Şekilleri, Dağlar ve Platolar
        elif any(k in q_lower for k in ['iklim', 'sıcaklık', 'yağış', 'rüzgar', 'nem', 'bitki örtüsü', 'maki', 'bozkır', 'orman yangın']):
            return 10 # Türkiye İklimi ve Bitki Örtüsü
        elif any(k in q_lower for k in ['nüfus', 'göç', 'yerleşme', 'kentleşme', 'demograf', 'yoğunluk']):
            return 11 # Türkiye Nüfus ve Yerleşme
        elif any(k in q_lower for k in ['tarım', 'hayvancılık', 'maden', 'enerji', 'sanayi', 'turizm', 'ulaşım', 'ticaret', 'bor', 'linyit']):
            return 12 # Türkiye Tarım, Hayvancılık ve Madenler
        # Fallback by question number (GK 28-45)
        rel_q = qnum - 27
        if rel_q <= 3: return 8
        elif rel_q <= 7: return 9
        elif rel_q <= 10: return 10
        elif rel_q <= 13: return 11
        else: return 12

    elif category == 3: # Vatandaşlık & Anayasa
        if qnum >= 55: # Güncel Bilgiler
            return 17 # Güncel Bilgiler ve Uluslararası Kuruluşlar
        if any(k in q_lower for k in ['hak ehliyeti', 'fiil ehliyeti', 'hukuk kuralı', 'müeyyide', 'borçlar', 'iyiniyet', 'dava', 'yargı', 'kanun']):
            return 13 # Temel Hukuk Kavramları
        elif any(k in q_lower for k in ['1982 anayasası', '1921', '1924', '1961', 'değiştirilemez', 'temel haklar', 'siyasi haklar']):
            return 14 # 1982 Anayasası ve Temel Esaslar
        elif any(k in q_lower for k in ['tbmm', 'milletvekili', 'cumhurbaşkanı', 'bakan', 'anayasa mahkemesi', 'yargıtay', 'danıştay', 'sayıştay']):
            return 15 # Yasama, Yürütme ve Yargı Organları
        elif any(k in q_lower for k in ['belediye', 'vali', 'kaymakam', 'il idaresi', 'idare hukuku', 'devlet memur', 'hiyerarşi', 'idari vesayet']):
            return 16 # İdare Hukuku ve Türkiye İdari Teşkilatı
        # Fallback by question number
        if qnum <= 48: return 13
        elif qnum <= 50: return 14
        elif qnum <= 53: return 15
        else: return 16

    elif category == 4: # Türkçe
        if any(k in q_lower for k in ['yazımı yanlıştır', 'yazım kural', 'noktalama', 'noktalı virgül', 'kesme işareti', 'büyük harf']):
            return 21 # Yazım Kuralları ve Noktalama İşaretleri
        elif any(k in q_lower for k in ['öge', 'yüklem', 'özne', 'nesne', 'tümleç', 'fiilimsi', 'çatı', 'ses olayı', 'ünlü düşmesi', 'türemiş']):
            return 20 # Dil Bilgisi ve Cümlenin Ögeleri
        elif any(k in q_lower for k in ['boş bırakılan yerlere', 'altı çizili söz', 'anlamca birleştirilmiş', 'yakın anlam', 'karşıt anlam']):
            return 18 # Sözcük ve Cümlede Anlam
        elif any(k in q_lower for k in ['bu parçada', 'paragraf', 'yazar', 'ana düşünce', 'çıkarılamaz', 'değinilmemiştir', 'hangisine ulaşılamaz']):
            return 19 # Paragrafta Anlam ve Ana Düşünce
        # Fallback by question number
        if qnum <= 5: return 18
        elif qnum <= 12: return 19
        elif qnum <= 16: return 20
        elif qnum <= 20: return 21
        elif qnum <= 26: return 19
        else: return 22 # Sözel Mantık

    return 0

def clean_question_text(txt):
    # Remove exam headers/footers
    txt = re.sub(r'Diğer sayfaya geçiniz.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'GENEL YETENEK.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'GENEL KÜLTÜR.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'CEVAPLARINIZI KONTROL EDİNİZ.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Bu testte \d+ soru vardır.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Cevaplarınızı,.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Bu soruların telif hakları.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Ö S Y M.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'\s+', ' ', txt).strip()
    return txt

def clean_option_text(txt):
    txt = re.sub(r'Diğer sayfaya geçiniz.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'GENEL YETENEK.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'GENEL KÜLTÜR.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Bu soruların telif hakları.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Ö S Y M.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'^\s*[:\-\.]\s*', '', txt)
    txt = re.sub(r'\s+', ' ', txt).strip()
    return txt
