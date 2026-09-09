# -*- coding: utf-8 -*-
"""
İcra Müdürlüğü ve Müdür Yardımcılığı Seçme Sınavı Kapsamlı Soru Üretici Modülü
(İcra İflas Kanunu, HMK, TTK Kıymetli Evrak, Harçlar Kanunu, Cezaevi Harcı, TBK Faiz)
"""
import json, random

def generate_icra_questions(subcat_by_slug):
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
    # 1. icra-ilamsiz-takip: İlamsız Takip, Ödeme Emri & İtiraz
    # =========================================================================
    ilamsiz_items = [
        ("2004 sayılı İcra ve İflas Kanunu'na göre, genel haciz yolunda borçlunun ödeme emrine itiraz süresi, ödeme emrinin tebliğinden itibaren kaç gündür?",
         "3 gün", "5 gün", "7 gün", "10 gün", "15 gün", "c",
         "2004 sayılı İİK m. 62 uyarınca genel haciz yolunda borçlu, ödeme emrinin tebliğinden itibaren 7 gün içinde dilekçeyle veya sözlü olarak icra dairesine itiraz edebilir."),
        ("Genel haciz yolunda ödeme emrine süresi içinde itiraz eden borçlunun itirazı üzerine takip ne şekilde etkilenir?",
         "Takip re'sen iptal edilir.",
         "Takip kendiliğinden durur.",
         "Alacaklı derhal haciz isteyebilir.",
         "Borçlu teminat yatırırsa takip durur.",
         "İcra müdürü takibin devamına karar verir.", "b",
         "İİK m. 66 uyarınca süresi içinde yapılan itiraz takibi kendiliğinden durdurur."),
        ("İtiraz ile duran ilamsız takibe devam edebilmek için alacaklının genel mahkemede açabileceği 'İtirazın İptali Davası' açma süresi ne kadardır?",
         "İtirazın tebliğinden itibaren 6 ay",
         "İtirazın tebliğinden itibaren 1 yıl",
         "Takip tarihinden itibaren 2 yıl",
         "Ödeme emri tarihinden itibaren 5 yıl",
         "Her zaman açılabilir (zamanaşımı yoktur)", "b",
         "İİK m. 67 uyarınca alacaklı, itirazın kendisine tebliğinden itibaren bir yıl içinde itirazın iptali davası açabilir."),
        ("Alacaklının elinde İİK m. 68'de sayılan kesin veya adi senet belgeleri varsa, icra mahkemesinden 'İtirazın Kaldırılması' talebinde bulunma süresi ne kadardır?",
         "İtirazın tebliğinden itibaren 3 ay",
         "İtirazın tebliğinden itibaren 6 ay",
         "İtirazın tebliğinden itibaren 1 yıl",
         "30 gün",
         "15 gün", "b",
         "İİK m. 68 uyarınca alacaklı itirazın tebliğinden itibaren altı ay içinde icra mahkemesinden itirazın kaldırılmasını isteyebilir."),
        ("İtirazın iptali davasında haksız çıkan tarafa hükmolunan icra inkar tazminatı oranı en az yüzde kaçtır?",
         "%10", "%15", "%20", "%25", "%50", "c",
         "İİK m. 67 uyarınca itirazın haksızlığına karar verilirse, borçlu diğer tarafın talebi üzerine takip konusu alacağın en az yüzde yirmisi (%20) oranında tazminata mahkum edilir."),
        ("Borçlu imzaya itiraz etmek istiyorsa bu itirazını ödeme emrine itirazında nasıl bildirmelidir?",
         "Genel itiraz beyanı yeterlidir.",
         "Ayrıca ve açıkça bildirmek zorundadır; aksi halde senetteki imzayı kabul etmiş sayılır.",
         "Noterden ihtarname çekmelidir.",
         "Bilirkişi raporu eklemelidir.",
         "İcra mahkemesine dava açmalıdır.", "b",
         "İİK m. 62/5 uyarınca borçlu senet altındaki imzayı reddediyorsa, bunu itirazında ayrıca ve açıkça bildirmelidir; aksi halde imza kabul edilmiş sayılır.")
    ]
    for q, a, b, c, d, e, ans, sol in ilamsiz_items:
        for lvl in range(1, 4):
            add('icra-ilamsiz-takip', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 2. icra-haciz-satis: Haciz, Satış ve Paylaştırma
    # =========================================================================
    haciz_items = [
        ("İİK m. 82 uyarınca aşağıdakilerden hangisi borçlunun borcundan dolayı kesinlikle haczedilemez (Haczi Caiz Olmayan Mallar)?",
         "Borçlunun birden fazla olan gayrimenkulleri",
         "Borçlunun haline münasip evi (meskeniyeti)",
         "Borçlunun bankadaki vadeli mevduat hesabı",
         "Borçlunun binek otomobili",
         "Borçlunun limited şirket ortaklık payı", "b",
         "İİK m. 82/1-12 uyarınca borçlunun haline münasip evi haczedilemez (meskeniyet iddiası)."),
        ("İcra dairesi tarafından haczedilen taşınır malların satışını isteme süresi hacizden itibaren ne kadardır?",
         "3 ay", "6 ay", "1 yıl", "2 yıl", "5 yıl", "c",
         "7343 sayılı Kanun reformu ile taşınır ve taşınmaz satış isteme süreleri eşitlenmiş olup, İİK m. 106 uyarınca hacizden itibaren '1 yıl' içinde satış istenmelidir."),
        ("Satış talebi süresi içinde yapılmaz veya talep geri alınıp süresinde yenilenmezse o mal üzerindeki haciz ne olur?",
         "Takip düşer.", "Haciz kendiliğinden kalkar.", "Borç sona erer.", "Mal alacaklıya geçer.", "İcra müdürü resen yeniler.", "b",
         "İİK m. 110 uyarınca kanuni süresi içinde satış istenmez veya avans yatırılmazsa o mal üzerindeki haciz kendiliğinden kalkar."),
        ("İİK uyarınca haczedilen malların satışı hangi usul ile gerçekleştirilir?",
         "Kapalı zarf usulüyle adliye bahçesinde",
         "UYAP bünyesindeki Elektronik Satış Portalı üzerinden açık artırma yoluyla",
         "Pazarlık usulüyle doğrudan icra müdürünce",
         "Tellal marifetiyle sokakta",
         "Gazete ilanı sonrası adliye mezat salonunda fiziki teklifle", "b",
         "7343 sayılı Kanun ile İİK m. 111/b uyarınca satışlar UYAP Elektronik Satış Portalı üzerinden tamamen elektronik ortamda teklif verilerek yapılır."),
        ("Elektronik ortamda yapılan artırmada teklif edilecek asgari bedel, malın muhammen kıymetinin yüzde kaçından aşağı olamaz?",
         "%30", "%40", "%50", "%60", "%75", "c",
         "İİK m. 115 uyarınca açık artırmada teklif, malın muhammen kıymetinin yüzde ellisini (%50) ve rüçhanlı alacaklar ile satış masraflarını karşılamak zorundadır.")
    ]
    for q, a, b, c, d, e, ans, sol in haciz_items:
        for lvl in range(1, 4):
            add('icra-haciz-satis', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 3. icra-kambiyo-takibi: Kambiyo Senetlerine Özgü Haciz Yolu
    # =========================================================================
    kambiyo_items = [
        ("Kambiyo senetlerine özgü haciz yolunda (bono, poliçe, çek), borçlunun borcu ödeme süresi ödeme emrinin tebliğinden itibaren kaç gündür?",
         "5 gün", "7 gün", "10 gün", "15 gün", "30 gün", "c",
         "İİK m. 168/1-2 uyarınca kambiyo takiplerinde ödeme süresi 10 gündür."),
        ("Kambiyo senetlerine özgü haciz yolunda borçlunun hem imzaya hem de borca itiraz süresi kaç gündür ve itiraz nereye yapılır?",
         "7 gün içinde İcra Dairesine",
         "5 gün içinde İcra Mahkemesine",
         "10 gün içinde Asliye Ticaret Mahkemesine",
         "7 gün içinde İcra Mahkemesine",
         "5 gün içinde İcra Dairesine", "b",
         "İİK m. 168/1-4 ve 5 uyarınca kambiyo takibinde borca veya imzaya itiraz ödeme emrinin tebliğinden itibaren 5 gün içinde bir dilekçe ile İcra Mahkemesine yapılır."),
        ("Kambiyo senedindeki imzaya itiraz kural olarak icra takibini durdurur mu?",
         "Evet, kendiliğinden durdurur.",
         "Hayır, durdurmaz; ancak icra mahkemesi hâkimi takibin geçici olarak durdurulmasına karar verebilir.",
         "Alacaklı teminat verirse durdurur.",
         "İcra müdürü takibi durdurmak zorundadır.",
         "Takip derhal iptal olur.", "b",
         "İİK m. 170 uyarınca kambiyo takibinde imzaya itiraz takibi kendiliğinden durdurmaz. İcra mahkemesi inceleme yapıncaya kadar takibin geçici durdurulmasına tensiben karar verebilir.")
    ]
    for q, a, b, c, d, e, ans, sol in kambiyo_items:
        for lvl in range(1, 4):
            add('icra-kambiyo-takibi', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 4. icra-kiymetli-evrak: TTK Kıymetli Evrak Hukuku
    # =========================================================================
    ttk_items = [
        ("6102 sayılı Türk Ticaret Kanunu'na göre aşağıdakilerden hangisi bir bonoda (emre yazılı senet) bulunması zorunlu yasal unsurlardan biri değildir?",
         "Senet metninde 'bono' veya 'emre yazılı senet' kelimesi",
         "Kayıtsız ve şartsız belirli bir bedeli ödeme vaadi",
         "Lehtarın (kime veya kimin emrine ödenecek ise) adı ve soyadı",
         "Düzenleyenin (keşidecinin) ıslak veya güvenli e-imzası",
         "Faiz oranı ve ödeme şartı", "e",
         "TTK m. 776 uyarınca bonoda faiz şartı zorunlu unsur değildir; görüldüğünde ödenecek bonolar hariç vadeli bonolara yazılan faiz kaydı yazılmamış sayılır."),
        ("TTK'ya göre çekte muhatap (ödemeyi yapacak olan) ancak kim olabilir?",
         "Herhangi bir tacir", "Bir banka", "Noter", "Sigorta şirketi", "İcra dairesi", "b",
         "TTK m. 780/1-c ve m. 781 uyarınca çekte muhatap ancak ve sadece bir banka olabilir."),
        ("Aynı yerde (aynı belediye/büyükşehir sınırları içinde) ödenecek bir çekin ibraz süresi keşide gününden itibaren kaç gündür?",
         "5 gün", "10 gün", "1 ay", "3 ay", "6 ay", "b",
         "TTK m. 796 uyarınca çek, düzenlendiği yerde ödenecekse 10 gün; başka bir yerde ödenecekse 1 ay içinde muhatap bankaya ibraz edilmelidir.")
    ]
    for q, a, b, c, d, e, ans, sol in ttk_items:
        for lvl in range(1, 4):
            add('icra-kiymetli-evrak', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 5. icra-harclar-tarifesi & icra-damga-vergisi: Harçlar Kanunu ve Cezaevi Harcı
    # =========================================================================
    harc_icra_items = [
        ("492 sayılı Harçlar Kanunu'na göre, icra takibinde borçlu ödeme emrinin tebliğinden sonra fakat hacizden önce borcunu öderse tahsil harcı oranı yüzde kaçtır?",
         "%2.27", "%4.55", "%9.10", "%11.38", "%15", "b",
         "Harçlar Kanunu (1) sayılı Tarife B/I-3 uyarınca ödeme emrinden sonra hacizden önce yapılan ödemelerde tahsil harcı oranı %4.55'tir (hacizden sonra %9.10, satıştan sonra %11.38)."),
        ("2548 sayılı Kanun uyarınca icra dairelerince tahsil edilen alacaklar üzerinden alınan yüzde iki (%2) oranındaki 'Cezaevi Yapı Harcı' kimin üzerinde kalır?",
         "Borçludan ayrıca tahsil edilir.",
         "Alacaklıya aittir ve borçluya yükletilemez (tahsil olunan paradan kesilir).",
         "İcra müdürünün kefalet sandığından ödenir.",
         "Baro pulu fonundan karşılanır.",
         "Adalet Bakanlığı bütçesinden karşılanır.", "b",
         "2548 sayılı Kanun m. 1 uyarınca %2 cezaevi harcı doğrudan tahsil olunan alacaktan kesilir ve hiçbir suretle borçluya yükletilemez."),
        ("İcra müdürünün işlemlerinin kanuna aykırı olması veya bir hakkın yerine getirilmemesi sebebiyle İcra Mahkemesine şikâyet süresi kural olarak kaç gündür?",
         "3 gün", "7 gün", "10 gün", "15 gün", "30 gün", "b",
         "İİK m. 16 uyarınca şikâyet süresi öğrenme tarihinden itibaren 7 gündür. Ancak bir hakkın yerine getirilmemesinden veya sebepsiz sürüncemede bırakılmasından dolayı her zaman şikâyet olunabilir.")
    ]
    for q, a, b, c, d, e, ans, sol in harc_icra_items:
        for lvl in range(1, 4):
            add('icra-harclar-tarifesi', q, a, b, c, d, e, ans, sol, lvl)
            add('icra-damga-vergisi', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 6. icra-hmk-tedbirler: İhtiyati Haciz
    # =========================================================================
    ihtiyati_items = [
        ("İİK m. 257 uyarınca rehinle temin edilmemiş ve muaccel olmuş bir para borcunun alacaklısı mahkemeden ne talep edebilir?",
         "İflasın açılmasını", "İhtiyati haciz", "Doğrudan ilamlı icra", "Şirketin feshini", "Konkordato mühleti", "b",
         "İİK m. 257 gereğince rehinle temin edilmemiş ve vadesi gelmiş para alacakları için ihtiyati haciz talep edilebilir."),
        ("İhtiyati haciz kararı alan alacaklı, bu kararın verildiği tarihten itibaren kaç gün içinde icra dairesinden kararın infazını istemelidir?",
         "3 gün", "7 gün", "10 gün", "15 gün", "1 ay", "c",
         "İİK m. 261 uyarınca alacaklı ihtiyati haciz kararının verildiği tarihten itibaren 10 gün içinde kararı veren mahkemenin yargı çevresindeki icra dairesinden infazını istemek zorundadır."),
        ("İhtiyati haczi infaz ettiren alacaklı, borçluya karşı kaç gün içinde esas takibe geçmek (ödeme emri göndermek veya dava açmak) zorundadır?",
         "5 gün", "7 gün", "10 gün", "15 gün", "30 gün", "b",
         "İİK m. 264 uyarınca ihtiyati haczi tutturan alacaklı, haciz tutanağının tebliğinden itibaren 7 gün içinde takip talebinde bulunmalı veya dava açmalıdır.")
    ]
    for q, a, b, c, d, e, ans, sol in ihtiyati_items:
        for lvl in range(1, 4):
            add('icra-hmk-tedbirler', q, a, b, c, d, e, ans, sol, lvl)
            add('icra-hmk-tebligat-sureler', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 7. icra-borclar-ifa-faiz & icra-borclar-sona-erme: Borçlar Hukuku
    # =========================================================================
    tbk_items = [
        ("6098 sayılı Türk Borçlar Kanunu'na göre, sözleşmeyle kararlaştırılacak yıllık temerrüt faizi oranı, yasal faiz oranının en fazla yüzde kaç fazlası olabilir?",
         "%25", "%50", "%100", "%200", "Sınırsızdır", "c",
         "TBK m. 120 uyarınca sözleşme ile kararlaştırılacak yıllık temerrüt faizi oranı, mevzuat uyarınca belirlenen yıllık yasal faiz oranının yüzde yüz fazlasını aşamaz."),
        ("TBK'ya göre kanunda başka bir süre öngörülmedikçe genel zamanaşımı süresi kaç yıldır?",
         "1 yıl", "2 yıl", "5 yıl", "10 yıl", "20 yıl", "d",
         "TBK m. 146 uyarınca kanunda aksine bir hüküm bulunmadıkça her alacak 10 yıllık genel zamanaşımına tabidir."),
        ("Aşağıdaki alacaklardan hangisi için Türk Borçlar Kanunu'nda 5 yıllık zamanaşımı süresi öngörülmüştür?",
         "Ödünç sözleşmesinden doğan ana para borcu",
         "Kira bedelleri ve anapara faizleri",
         "Trafik kazasından doğan maddi tazminat alacağı",
         "Sebepsiz zenginleşme davası",
         "Haksız rekabet davaları", "b",
         "TBK m. 147/1 uyarınca kira bedelleri, anapara faizleri ve dönemsel edimler 5 yıllık zamanaşımına tabidir.")
    ]
    for q, a, b, c, d, e, ans, sol in tbk_items:
        for lvl in range(1, 4):
            add('icra-borclar-ifa-faiz', q, a, b, c, d, e, ans, sol, lvl)
            add('icra-borclar-sona-erme', q, a, b, c, d, e, ans, sol, lvl)

    print(f"İcra Müdürlüğü üretilen soru sayısı: {len(questions)}")
    return questions

if __name__ == '__main__':
    with open('d:/quiza/scratch_osym/law_subcats_map.json', 'r', encoding='utf-8') as f:
        subcats = json.load(f)
    subcat_by_slug = {s['slug']: s for s in subcats}
    qs = generate_icra_questions(subcat_by_slug)
    print("Örnek İcra soru:", qs[0]['question'][:60], "Kategori:", qs[0]['category'])
