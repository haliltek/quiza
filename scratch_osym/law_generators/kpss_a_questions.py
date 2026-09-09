# -*- coding: utf-8 -*-
"""
KPSS A Grubu (Kariyer Meslek Kadroları) Soru Üretici Modülü
(Hukuk, İktisat, Maliye, Muhasebe, Kamu Yönetimi)
"""
import json, random

def generate_kpss_a_questions(subcat_by_slug):
    questions = []
    
    def add(slug, q, a, b, c, d, e, ans, sol, lvl=1):
        sub = subcat_by_slug.get(slug)
        if not sub:
            return
        questions.append({
            'category': sub['category_id'],
            'subcategory': sub['subcat_id'],
            'language_id': sub['language_id'],
            'question': q.strip(),
            'question_type': 1,
            'optiona': a.strip(),
            'optionb': b.strip(),
            'optionc': c.strip(),
            'optiond': d.strip(),
            'optione': e.strip(),
            'answer': ans.lower().strip(),
            'level': lvl,
            'note': sol.strip()
        })

    # =========================================================================
    # 1. İktisat (Mikro, Makro, Para-Banka)
    # =========================================================================
    iktisat_items = [
        ("Mikro iktisatta bir malın fiyatındaki yüzde değişimin, o mala olan talep miktarındaki yüzde değişime oranına ne ad verilir?",
         "Talebin Gelir Esnekliği", "Talebin Fiyat Esnekliği", "Çapraz Talep Esnekliği", "Arz Esnekliği", "Marjinal İkame Oranı", "b",
         "Talebin fiyat esnekliği, fiyattaki oransal değişimin talep edilen miktarda yarattığı oransal değişimi ölçer."),
        ("IS-LM modelinde para arzının artırılması (genişletici para politikası) LM eğrisini nasıl etkiler?",
         "Sola kaydırır, faiz artar.",
         "Sağa kaydırır, faiz düşer ve gelir artar.",
         "Eğrinin eğimini dikleştirir.",
         "Etkilemez, sadece IS eğrisi kayar.",
         "Yalnızca fiyatlar genel düzeyi artar.", "b",
         "Genişletici para politikası para arzını artırarak LM eğrisini sağa kaydırır; bu da denge faiz oranını düşürür ve hasılayı artırır."),
        ("TCMB'nin açık piyasa işlemleri (APİ) çerçevesinde piyasadan tahvil/bono satın alması piyasada neye yol açar?",
         "Piyasadaki likiditeyi (para arzını) artırır.",
         "Piyasadaki likiditeyi azaltır.",
         "Enflasyonu doğrudan düşürür.",
         "Döviz rezervlerini eritir.",
         "Bankaların zorunlu karşılık oranını yükseltir.", "a",
         "Merkez Bankası piyasadan menkul kıymet satın aldığında piyasaya Türk Lirası verir, dolayısıyla piyasadaki para arzı ve likidite artar.")
    ]
    for q, a, b, c, d, e, ans, sol in iktisat_items:
        for lvl in range(1, 4):
            add('a-iktisat-1', q, a, b, c, d, e, ans, sol, lvl)
            add('a-iktisat-2', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 2. Maliye (Kamu Maliyesi, 5018, Vergi Hukuku)
    # =========================================================================
    maliye_items = [
        ("5018 sayılı Kamu Malî Yönetimi ve Kontrol Kanunu'na göre, genel yönetim kapsamındaki kamu idarelerinin bütçe hazırlık sürecini başlatan ve her yıl en geç Eylül ayının ilk haftası sonuna kadar yayımlanan belge hangisidir?",
         "Orta Vadeli Program (OVP)", "Bütçe Çağrısı", "Maliye Raporu", "Kesin Hesap Kanun Teklifi", "Sayıştay Denetim Raporu", "a",
         "5018 sayılı Kanun m. 16 uyarınca Cumhurbaşkanı tarafından onaylanan Orta Vadeli Program en geç Eylül ayının ilk haftası sonuna kadar Resmî Gazete'de yayımlanır."),
        ("213 sayılı Vergi Usul Kanunu'na göre vergi alacağının kanunlarında gösterilen matrah ve nispetler üzerinden vergi dairesi tarafından hesaplanarak miktarının tespit edilmesi işlemine ne ad verilir?",
         "Tebliğ", "Tarh", "Tahakkuk", "Tahsil", "Terkis", "b",
         "VUK m. 20 uyarınca verginin tarhı, vergi alacağının kanunlarında gösterilen matrah ve nispetler üzerinden vergi dairesi tarafından hesaplanarak bu alacağı miktar itibariyle tespit eden idari muameledir."),
        ("VUK'a göre vergi borcunun ödenmesi gereken aşamaya gelmesine ne ad verilir?",
         "Tarh", "Tebliğ", "Tahakkuk", "Tahsil", "Terkin", "c",
         "VUK m. 22 uyarınca verginin tahakkuku, tarh ve tebliğ edilen bir verginin ödenmesi gereken bir safhaya gelmesidir.")
    ]
    for q, a, b, c, d, e, ans, sol in maliye_items:
        for lvl in range(1, 4):
            add('a-maliye-1', q, a, b, c, d, e, ans, sol, lvl)
            add('a-maliye-2', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 3. Muhasebe (Genel Muhasebe, Finansal Tablolar, Maliyet)
    # =========================================================================
    muh_items = [
        ("Tekdüzen Hesap Planı'nda '100 Kasa Hesabı' hangi hesap grubunda yer alır?",
         "Duran Varlıklar", "Dönen Varlıklar", "Kısa Vadeli Yabancı Kaynaklar", "Özkaynaklar", "Gelir Hesapları", "b",
         "Tekdüzen Hesap Planı'nda 1 ile başlayan hesaplar 'Dönen Varlıklar' grubudur (10 Hazır Değerler - 100 Kasa)."),
        ("İşletmenin belirli bir andaki/tarihteki mali durumunu (varlıklarını, borçlarını ve özkaynaklarını) gösteren finansal tablo hangisidir?",
         "Gelir Tablosu", "Bilanço", "Nakit Akış Tablosu", "Satışların Maliyeti Tablosu", "Fon Akım Tablosu", "b",
         "Bilanço, bir işletmenin belirli bir tarihte sahip olduğu varlıklar ile bu varlıkların sağlandığı kaynakları gösteren temel finansal tablodur.")
    ]
    for q, a, b, c, d, e, ans, sol in muh_items:
        for lvl in range(1, 4):
            add('a-muhasebe-genel', q, a, b, c, d, e, ans, sol, lvl)
            add('a-muhasebe-maliyet', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 4. Kamu Yönetimi (Siyaset, İdare Tarihi, Yerel Yönetimler)
    # =========================================================================
    kamu_items = [
        ("Büyükşehir belediyesi kurulabilmesi için 5216 sayılı Kanun'a göre aranan asgari nüfus kriteri nedir?",
         "250.000", "500.000", "750.000", "1.000.000", "2.000.000", "c",
         "5216 sayılı Büyükşehir Belediyesi Kanunu m. 4 uyarınca toplam nüfusu 750.000'den fazla olan il belediyeleri kanunla büyükşehir belediyesine dönüştürülebilir."),
        ("Max Weber'in ideal bürokrasi modelinin temel özellikleri arasında aşağıdakilerden hangisi yer almaz?",
         "Yazılılık ve belgelere dayanma",
         "Görevlerin hiyerarşik kademelendirilmesi",
         "Kişisellik ve duygusal bağlılık",
         "Uzmanlaşma ve işbölümü",
         "Kurallara sıkı sıkıya bağlılık", "c",
         "Max Weber'in rasyonel-yasal bürokrasi modelinde 'gayrişahsilik' (kişisel olmama) esastır; duygusallık ve kişisellik bürokrasiden dışlanır.")
    ]
    for q, a, b, c, d, e, ans, sol in kamu_items:
        for lvl in range(1, 4):
            add('a-kamu-siyaset-yonetim', q, a, b, c, d, e, ans, sol, lvl)
            add('a-kamu-idare-tarihi', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 5. A Grubu Hukuk
    # =========================================================================
    a_huk_items = [
        ("Ceza Muhakemesi Hukukunda 'şüpheli' sıfatı hangi aşamada başlar ve ne zaman sona erer?",
         "İddianamenin kabulüyle başlar, hükümle biter.",
         "Soruşturma evresinde suç şüphesinin yetkili mercilerce öğrenilmesinden iddianamenin kabulüne kadar sürer.",
         "Yakalama anından itibaren başlar.",
         "Gözaltı kararıyla başlar.",
         "Duruşmanın ilk celsesinde başlar.", "b",
         "CMK m. 2/1-a uyarınca soruşturma evresinde suç şüphesi altında bulunan kişi 'şüpheli', kovuşturma evresinde ise 'sanık' olarak adlandırılır.")
    ]
    for q, a, b, c, d, e, ans, sol in a_huk_items:
        for lvl in range(1, 4):
            add('a-hukuk-1', q, a, b, c, d, e, ans, sol, lvl)
            add('a-hukuk-2', q, a, b, c, d, e, ans, sol, lvl)
            add('a-hukuk-3', q, a, b, c, d, e, ans, sol, lvl)

    print(f"KPSS A Grubu üretilen soru sayısı: {len(questions)}")
    return questions

if __name__ == '__main__':
    with open('d:/quiza/scratch_osym/law_subcats_map.json', 'r', encoding='utf-8') as f:
        subcats = json.load(f)
    subcat_by_slug = {s['slug']: s for s in subcats}
    qs = generate_kpss_a_questions(subcat_by_slug)
    print("Örnek KPSS A soru:", qs[0]['question'][:60], "Kategori:", qs[0]['category'])
