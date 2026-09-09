# -*- coding: utf-8 -*-
"""
Hâkim ve Savcı Yardımcılığı Sınavı Kapsamlı Soru Üretici Modülü
(Anayasa, İdare, Ceza Genel/Özel, CMK, Medeni, Borçlar, İYUK)
2025/2026 Güncel Mevzuat
"""
import json, random

def generate_hakimlik_questions(subcat_by_slug):
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
    # 1. hakimlik-anayasa & hakimlik-idare-hukuku
    # =========================================================================
    ay_idare = [
        ("1982 Anayasası'na göre, Anayasa Mahkemesi'nde doğrudan doğruya iptal davası (soyut norm denetimi) açma süresi, iptali istenen kanunun Resmî Gazete'de yayımlanmasından başlayarak kaç gündür?",
         "15 gün", "30 gün", "60 gün", "90 gün", "1 yıl", "c",
         "1982 Anayasası m. 151 uyarınca kanunların, Cumhurbaşkanlığı kararnamelerinin veya TBMM İçtüzüğünün iptali için doğrudan iptal davası açma süresi Resmî Gazete'de yayımdan başlayarak 60 gündür."),
        ("Bir davaya bakmakta olan mahkemenin, uygulanacak bir kanun veya Cumhurbaşkanlığı kararnamesi hükmünü Anayasaya aykırı görmesi veya tarafların iddiasını ciddi bulması halinde Anayasa Mahkemesine başvurmasına ne ad verilir?",
         "Soyut norm denetimi", "Somut norm denetimi (İtiraz yolu)", "Bireysel başvuru", "Yorumlu ret kararı", "Kanun yararına temyiz", "b",
         "Anayasa m. 152 uyarınca somut norm denetimi (itiraz yolu), derdest bir davada uygulanacak normun AYM'ye taşınmasıdır."),
        ("Anayasa Mahkemesi'ne somut norm denetimi (itiraz yolu) ile başvuran mahkemenin başvurusunu AYM esastan reddederse, aynı kanun hükmü hakkında ret kararının Resmî Gazete'de yayımlanmasından itibaren kaç yıl geçmedikçe aynı gerekçeyle itiraz başvurusu yapılamaz?",
         "1 yıl", "2 yıl", "5 yıl", "10 yıl", "Süresizdir", "d",
         "Anayasa m. 152/son uyarınca AYM'nin işin esasına girerek verdiği ret kararının yayımlanmasından başlayarak 10 yıl geçmedikçe aynı kanun hükmü için itiraz yoluyla başvurulamaz."),
        ("Anayasa Mahkemesine bireysel başvuru yapabilmek için olağan kanun yollarının tüketildiği tarihten itibaren kaç gün içinde başvurulmalıdır?",
         "15 gün", "30 gün", "60 gün", "3 ay", "1 yıl", "b",
         "6216 sayılı Anayasa Mahkemesinin Kuruluşu Kanunu m. 47/5 uyarınca bireysel başvuru süresi iç hukuk yollarının tüketildiği tarihten itibaren 30 gündür."),
        ("1982 Anayasası'na göre 'yetki genişliği' (adem-i temerküz) ilkesi Anayasa'da açıkça sadece hangi idari birim/makam için öngörülmüştür?",
         "Belediye Başkanları", "İller (Valiler)", "Köy Muhtarları", "Bakanlık Müsteşarları", "Bölge İdare Mahkemeleri", "b",
         "Anayasa m. 126 uyarınca illerin idaresi 'yetki genişliği' esasına dayanır ve bu yetki sadece il genel idaresinin başı olan valiler tarafından kullanılır.")
    ]
    for q, a, b, c, d, e, ans, sol in ay_idare:
        for lvl in range(1, 4):
            add('hakimlik-anayasa', q, a, b, c, d, e, ans, sol, lvl)
            add('hakimlik-idare-hukuku', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 2. hakimlik-ceza-genel & hakimlik-ceza-ozel
    # =========================================================================
    tck_items = [
        ("5237 sayılı TCK m. 29 uyarınca haksız bir fiilin meydana getirdiği hiddet veya şiddetli elemin etkisi altında suç işleyen kimse hakkında hangi ceza indirimi kurumu uygulanır?",
         "Meşru müdafaa", "Haksız tahrik", "Zorunluluk hali", "Haksızlık yanılgısı", "Gönüllü vazgeçme", "b",
         "TCK m. 29 gereğince haksız bir fiilin doğurduğu şiddetli elem veya hiddet altında suç işleyen fail haksız tahrik indiriminden yararlanır."),
        ("Failin suçun icra hareketlerine başladıktan sonra kendi serbest iradesiyle icra hareketlerini tamamlamaktan vazgeçmesi veya neticenin gerçekleşmesini önlemesi halinde hangi kurum söz konusu olur?",
         "Etkin Pişmanlık", "Gönüllü Vazgeçme", "Eksik Teşebbüs", "İşlenemez Suç", "Mecburiyet Hali", "b",
         "TCK m. 36 uyarınca fail, suçun icra hareketlerinden gönüllü vazgeçer veya neticenin meydana gelmesini engellerse teşebbüsten dolayı cezalandırılmaz; tamam olan kısım suç teşkil ediyorsa o suçtan cezalandırılır."),
        ("Kamu görevlisinin görevi sebebiyle zilyetliği kendisine devredilmiş olan veya koruma ve gözetimiyle yükümlü olduğu para veya malı kendisinin veya başkasının zimmetine geçirmesi halinde hangi suç oluşur?",
         "Görevi Kötüye Kullanma", "İrtikap", "Zimmet", "Rüşvet", "Güveni Kötüye Kullanma", "c",
         "TCK m. 247 uyarınca görevi dolayısıyla kendisine devredilen veya gözetimi altında bulunan malı kendisinin veya başkasının menfaatine geçiren kamu görevlisi 'Zimmet' suçunu işlemiş olur.")
    ]
    for q, a, b, c, d, e, ans, sol in tck_items:
        for lvl in range(1, 4):
            add('hakimlik-ceza-genel', q, a, b, c, d, e, ans, sol, lvl)
            add('hakimlik-ceza-ozel', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 3. hakimlik-cmk-koruma & hakimlik-cmk-kovusturma
    # =========================================================================
    cmk_items = [
        ("5271 sayılı CMK m. 217 uyarınca, yüklenen suç hukuka uygun bir şekilde elde edilmiş her türlü delille ispat edilebilir. Ancak hukuka aykırı yöntemlerle elde edilen deliller hakkında kural nedir?",
         "Hâkim takdirine göre hükme esas alabilir.",
         "Hükme esas alınamaz.",
         "Ağır cezalık suçlarda delil sayılır.",
         "Sanık itiraf ederse geçerli sayılır.",
         "Cumhuriyet savcısı onaylarsa geçerlidir.", "b",
         "CMK m. 217/2 ve Anayasa m. 38/6 uyarınca kanuna aykırı olarak elde edilmiş bulgular delil olarak kabul edilemez ve hükme esas alınamaz."),
        ("CMK m. 231 uyarınca Hükmün Açıklanmasının Geri Bırakılması (HAGB) kararı verilebilmesi için mahkum olunan hapis cezası süresi en fazla ne kadar olmalıdır?",
         "1 yıl veya daha az", "2 yıl veya daha az", "3 yıl veya daha az", "5 yıl veya daha az", "6 ay", "b",
         "CMK m. 231/5 uyarınca sanığa yüklenen suçtan dolayı yapılan yargılama sonunda hükmolunan ceza 2 yıl veya daha az süreli hapis veya adli para cezası ise HAGB kararı verilebilir.")
    ]
    for q, a, b, c, d, e, ans, sol in cmk_items:
        for lvl in range(1, 4):
            add('hakimlik-cmk-koruma', q, a, b, c, d, e, ans, sol, lvl)
            add('hakimlik-cmk-kovusturma', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 4. hakimlik-medeni & hakimlik-borclar
    # =========================================================================
    tmk_items = [
        ("Türk Medeni Kanunu m. 2'de yer alan 'Herkes, haklarını kullanırken ve borçlarını yerine getirirken dürüstlük kurallarına uymak zorundadır. Bir hakkın açıkça kötüye kullanılmasını hukuk düzeni korumaz' ilkesi hangisidir?",
         "İyiniyet İlkesi (Subjektif)", "Dürüstlük Kuralı (Objektif İyiniyet)", "Hak Düşürücü Süre", "Temsil İlkesi", "Sözleşme Serbestisi", "b",
         "TMK m. 2 Dürüstlük Kuralı (Objektif İyiniyet) olup, hakların kullanılması ve borçların ifasında geçerlidir. TMK m. 3 ise hakkın kazanılmasındaki subjektif iyiniyettir."),
        ("6098 sayılı TBK m. 138 uyarınca sözleşmenin yapıldığı sırada taraflarca öngörülemeyen ve öngörülmesi beklenmeyen olağanüstü bir durum ortaya çıkar ve borcun ifası aşırı derecede güçleşirse borçlu mahkemeden ne talep edebilir?",
         "Sözleşmenin feshini veya şartlara uyarlanmasını",
         "Borcun tamamen affedilmesini",
         "Karşı tarafın tazminata mahkum edilmesini",
         "Sözleşmenin kendiliğinden hükümsüz sayılmasını",
         "Cezai şartın iki katına çıkarılmasını", "a",
         "TBK m. 138 uyarınca aşırı ifa güçlüğü halinde borçlu hâkimden sözleşmenin yeni koşullara uyarlanmasını, bu mümkün olmadığı takdirde sözleşmeden dönmeyi talep edebilir.")
    ]
    for q, a, b, c, d, e, ans, sol in tmk_items:
        for lvl in range(1, 4):
            add('hakimlik-medeni', q, a, b, c, d, e, ans, sol, lvl)
            add('hakimlik-borclar', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 5. hakimlik-iyuk-sureler & hakimlik-iyuk-kanun-yollari
    # =========================================================================
    iyuk_items = [
        ("2577 sayılı İdari Yargılama Usulü Kanunu'na göre, genel dava açma süresi Danıştay ve İdare Mahkemelerinde kaç gündür?",
         "15 gün", "30 gün", "60 gün", "90 gün", "1 yıl", "c",
         "2577 sayılı İYUK m. 7/1 uyarınca dava açma süresi özel kanunlarında ayrı süre gösterilmeyen hallerde Danıştay'da ve idare mahkemelerinde altmış (60), vergi mahkemelerinde otuz (30) gündür."),
        ("İYUK m. 27 uyarınca İdari Mahkemenin idari işlemin yürütülmesinin durdurulmasına (YD) karar verebilmesi için aranan iki yasal şart nedir?",
         "Davacının teminat yatırması ve harcı ödemesi",
         "İdari işlemin uygulanması halinde telafisi güç veya imkansız zararların doğması ve idari işlemin açıkça hukuka aykırı olması (birlikte gerçekleşmesi)",
         "Davalı idarenin savunma vermemesi",
         "Danıştay Başsavcısının olumlu mütalaası",
         "Davanın duruşmalı açılmış olması", "b",
         "İYUK m. 27/2 uyarınca yürütmenin durdurulması için 'telafisi güç veya imkânsız zararların doğması' ve 'işlemin açıkça hukuka aykırı olması' şartlarının birlikte gerçekleşmesi zorunludur.")
    ]
    for q, a, b, c, d, e, ans, sol in iyuk_items:
        for lvl in range(1, 4):
            add('hakimlik-iyuk-sureler', q, a, b, c, d, e, ans, sol, lvl)
            add('hakimlik-iyuk-kanun-yollari', q, a, b, c, d, e, ans, sol, lvl)

    print(f"Hakimlik üretilen soru sayısı: {len(questions)}")
    return questions

if __name__ == '__main__':
    with open('d:/quiza/scratch_osym/law_subcats_map.json', 'r', encoding='utf-8') as f:
        subcats = json.load(f)
    subcat_by_slug = {s['slug']: s for s in subcats}
    qs = generate_hakimlik_questions(subcat_by_slug)
    print("Örnek Hakimlik soru:", qs[0]['question'][:60], "Kategori:", qs[0]['category'])
