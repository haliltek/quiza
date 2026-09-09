# -*- coding: utf-8 -*-
"""
HMGS (Hukuk Mesleklerine Giriş Sınavı) Kapsamlı Soru Üretici Modülü
(HMK, CMK, TCK, TMK, TBK, TTK, İİK, İYUK, Avukatlık Kanunu, Hukuk Felsefesi)
2025/2026 Güncel Mevzuat
"""
import json, random

def generate_hmgs_questions(subcat_by_slug):
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
    # HMK (Hukuk Muhakemeleri Kanunu - 6100)
    # =========================================================================
    hmk_items = [
        # hmgs-hmk-gorev-yetki
        ("6100 sayılı HMK'ya göre, dava konusunun değer ve miktarına bakılmaksızın malvarlığı haklarına ve şahıs varlığına ilişkin uyuşmazlıklarda genel görevli mahkeme hangisidir?",
         "Sulh Hukuk Mahkemesi", "Asliye Hukuk Mahkemesi", "Tüketici Mahkemesi", "Asliye Ticaret Mahkemesi", "Bölge Adliye Mahkemesi", "b",
         "HMK m. 2 uyarınca dava konusunun değer ve miktarına bakılmaksızın malvarlığı haklarına ve şahıs varlığına ilişkin uyuşmazlıklarda aksine bir düzenleme yoksa Asliye Hukuk Mahkemesi görevlidir."),
        ("HMK'ya göre genel yetkili mahkeme neresidir?",
         "Davacının yerleşim yeri mahkemesi",
         "Davalının davanın açıldığı tarihteki yerleşim yeri mahkemesi",
         "Sözleşmenin yapıldığı yer mahkemesi",
         "Haksız fiilin işlendiği yer mahkemesi",
         "Dava konusu taşınırın bulunduğu yer mahkemesi", "b",
         "HMK m. 6 uyarınca genel yetkili mahkeme, davalı gerçek veya tüzel kişinin davanın açıldığı tarihteki yerleşim yeri mahkemesidir."),
        ("Taşınmazın aynına (mülkiyetine, tesciline, tapu iptaline) ilişkin davalarda yetkili mahkeme neresidir?",
         "Davacının yerleşim yeri mahkemesi",
         "Davalının yerleşim yeri mahkemesi",
         "Taşınmazın bulunduğu yer mahkemesi (kesin yetki)",
         "Sözleşmenin ifa edileceği yer mahkemesi",
         "Davalıların çoğunluğunun bulunduğu yer mahkemesi", "c",
         "HMK m. 12 uyarınca taşınmaz üzerindeki ayni hakka ilişkin veya ayni hak sahipliğinde değişikliğe yol açabilecek davalarda taşınmazın bulunduğu yer mahkemesi kesin yetkilidir."),
        # hmgs-hmk-dava-sartlari
        ("6100 sayılı HMK m. 114 uyarınca aşağıdakilerden hangisi bir 'dava şartı' değildir?",
         "Türk mahkemelerinin yargı hakkının bulunması",
         "Yargı yolunun caiz olması",
         "Mahkemenin görevli olması",
         "Yetki sözleşmesinin geçerli olması (ilk itiraz)",
         "Davacının dava açmakta hukuki yararının bulunması", "d",
         "HMK m. 116 uyarınca kesin yetki halleri hariç yetki itirazı ve tahkim itirazı 'ilk itiraz'dır; dava şartı değildir."),
        ("Dava dilekçesinde davalının adresi ve T.C. kimlik numarası eksikse, hâkim davacıya bu eksikliği tamamlaması için kaç haftalık kesin süre verir?",
         "3 gün", "1 hafta", "2 hafta", "1 ay", "30 gün", "b",
         "HMK m. 119/2 uyarınca dava dilekçesinde davalının adresi gibi zorunlu unsurlarda eksiklik varsa, hâkim davacıya eksikliği tamamlaması için bir haftalık kesin süre verir."),
        # hmgs-hmk-deliller
        ("HMK m. 200 uyarınca bir hakkın doğumu, düşürülmesi, devri, değiştirilmesi, yenilenmesi, ertelenmesi, ikrarı ve itfası amacıyla yapılan hukuki işlemlerin yapıldıkları zamanki miktar veya değerleri belirli parasal sınırı aşıyorsa ne ile ispat edilmek zorundadır (Senetle İspat Zorunluluğu)?",
         "Bilirkişi raporuyla", "Tanık beyanıyla", "Senet (kesin delil) ile", "Keşif ile", "Yemin teklifiyle", "c",
         "HMK m. 200 uyarınca kanunda belirlenen parasal sınırın üzerindeki hukuki işlemler kural olarak ancak senetle ispat olunabilir."),
        ("Senetle ispat zorunluluğunun istisnası olan ve tek başına iddiayı ispat etmeye yetmemekle birlikte hukuki işlemi muhtemel gösteren, aleyhine ileri sürülen kimse tarafından verilmiş belgeye ne ad verilir?",
         "Kesin Hüküm", "Delil Başlangıcı", "Aleni Belge", "İlam", "Maddi Vakıa Belgesi", "b",
         "HMK m. 202 uyarınca delil başlangıcı bulunan hallerde senetle ispat zorunluluğu ortadan kalkar ve tanık dinlenebilir."),
        # hmgs-hmk-kanun-yollari
        ("8. Yargı Paketi ile HMK m. 345'te yapılan düzenlemeye göre, istinaf dilekçesi ilamın taraflardan her birine tebliğinden itibaren kaç hafta içinde verilmelidir?",
         "1 hafta", "2 hafta", "3 hafta", "4 hafta", "15 gün", "b",
         "8. Yargı Paketi (7499 sayılı Kanun) ile HMK'da istinaf süresi gerekçeli kararın tebliğinden itibaren 'iki hafta' olarak kabul edilmiştir.")
    ]
    for q, a, b, c, d, e, ans, sol in hmk_items:
        for lvl in range(1, 4):
            add('hmgs-hmk-gorev-yetki', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-hmk-dava-sartlari', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-hmk-deliller', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-hmk-kanun-yollari', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # TCK & CMK (Ceza Hukuku ve Ceza Muhakemesi Hukuku)
    # =========================================================================
    ceza_items = [
        # hmgs-tck-genel
        ("5237 sayılı Türk Ceza Kanunu m. 21 uyarınca, kişinin suçun kanuni tanımındaki unsurların gerçekleşebileceğini öngörmesine rağmen 'olursa olsun' düşüncesiyle fiili işlemesi haline ne ad verilir?",
         "Doğrudan Kast", "Olası Kast", "Bilinçli Taksir", "Basit Taksir", "Kaza ve Tesadüf", "b",
         "TCK m. 21/2 uyarınca kişinin, fiilin kanuni tanımındaki unsurlarının gerçekleşebileceğini öngörmesine rağmen fiili işlemesi halinde olası kast vardır."),
        ("Kişinin neticeyi öngördüğü halde şansına, tecrübesine veya yeteneğine güvenerek neticenin gerçekleşmeyeceğine inanarak fiili icra etmesi durumunda hangisi oluşur?",
         "Olası kast", "Bilinçli taksir", "Doğrudan kast", "Kusursuzluk", "Haksızlık yanılgısı", "b",
         "TCK m. 22/3 uyarınca kişinin öngördüğü neticeyi istememesine karşın neticenin meydana gelmesi halinde bilinçli taksir söz konusudur."),
        ("Aşağıdakilerden hangisi 5237 sayılı TCK'da düzenlenen hukuka uygunluk nedenlerinden biri değildir?",
         "Görevin ifası (Kanun hükmünü yerine getirme)",
         "Meşru müdafaa (Haklı savunma)",
         "Hakkın kullanılması",
         "İlgilinin rızası",
         "Yaş küçüklüğü", "e",
         "Yaş küçüklüğü (TCK m. 31) bir hukuka uygunluk sebebi değil, kusurluluğu etkileyen / kaldıran şahsi bir nedendir."),
        # hmgs-cmk-koruma
        ("5271 sayılı CMK m. 100 uyarınca, kuvvetli suç şüphesinin varlığını gösteren somut delillerin bulunması halinde şüpheli veya sanığın kaçması veya delilleri yok etme tehlikesi bulunuyorsa hâkim neye karar verebilir?",
         "Gözaltına", "Tutuklamaya", "Zorla getirmeye", "HAGB'ye", "KYOK verilmesine", "b",
         "CMK m. 100 uyarınca kuvvetli suç şüphesi ve tutuklama nedenlerinin bulunması halinde şüpheli veya sanık hakkında tutuklama kararı verilebilir."),
        ("CMK m. 91 uyarınca yakalanan kişi, yakalama yerine en yakın hâkim veya mahkemeye gönderilmesi için zorunlu yol süresi (en fazla 12 saat) hariç, yakalama anından itibaren en geç kaç saat içinde hâkim önüne çıkarılmalıdır?",
         "12 saat", "24 saat", "48 saat", "72 saat", "4 gün", "b",
         "CMK m. 91/1 uyarınca gözaltı süresi, yakalama anından itibaren 24 saati geçemez (toplu suçlarda uzatma hariç)."),
        # hmgs-cmk-kovusturma
        ("8. Yargı Paketi ile CMK m. 273'te yapılan değişiklik uyarınca, istinaf yoluna başvuru süresi hükmün gerekçesiyle birlikte tebliğinden itibaren kaç haftadır?",
         "1 hafta", "2 hafta", "3 hafta", "15 gün", "30 gün", "b",
         "7499 sayılı Kanun (8. Yargı Paketi) ile CMK'daki istinaf ve temyiz süresi 'iki hafta' olarak değiştirilmiştir.")
    ]
    for q, a, b, c, d, e, ans, sol in ceza_items:
        for lvl in range(1, 4):
            add('hmgs-tck-genel', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-tck-tesebbus-istirak', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-tck-ozel', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-cmk-sorusturma', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-cmk-koruma', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-cmk-kovusturma', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # TMK & TBK (Medeni Hukuk ve Borçlar Hukuku)
    # =========================================================================
    medeni_items = [
        ("4721 sayılı Türk Medeni Kanunu'na göre hak ehliyeti ne zaman başlar?",
         "Ergin olunduğu anda",
         "Ayırt etme gücünün kazanılmasıyla",
         "Çocuğun sağ ve tam doğduğu anda (sağ doğmak koşuluyla ana rahmine düştüğü andan itibaren)",
         "18 yaşını doldurmakla",
         "Evlenmekle", "c",
         "TMK m. 8 ve m. 28 uyarınca çocuk hak ehliyetini sağ doğmak koşuluyla ana rahmine düştüğü andan itibaren kazanır."),
        ("Bir kimsenin ölüm tehlikesi içinde kaybolması halinde gaiplik kararı verilebilmesi için olayın üzerinden en az kaç yıl geçmelidir?",
         "6 ay", "1 yıl", "3 yıl", "5 yıl", "10 yıl", "b",
         "TMK m. 32 uyarınca ölüm tehlikesi içinde kaybolmada 1 yıl, kendisinden uzun süre haber alınamama halinde ise son haber tarihinden itibaren 5 yıl geçmesi gerekir."),
        ("Taşınmaz mülkiyetinin devrini amaçlayan sözleşmelerin geçerli olması hangi şekil şartına bağlıdır?",
         "Adi yazılı şekil",
         "Noterde imza onayı",
         "Tapu sicil memuru önünde resmi şekilde yapılması",
         "Avukat huzurunda düzenlenmesi",
         "Ticaret siciline tescil", "c",
         "TMK m. 706 ve TBK m. 237 uyarınca taşınmaz devri sözleşmeleri resmi şekilde (Tapu Müdürlüğü'nde) yapılmadıkça geçerli olmaz."),
        ("Borçlar Kanunu'na göre haksız fiilden doğan tazminat istemi, zarar görenin zararı ve tazminat yükümlüsünü öğrendiği tarihten başlayarak kaç yılda zamanaşımına uğrar?",
         "1 yıl (her halde 5 yıl)",
         "2 yıl (her halde 10 yıl)",
         "3 yıl (her halde 15 yıl)",
         "5 yıl (her halde 10 yıl)",
         "10 yıl", "b",
         "TBK m. 72 uyarınca haksız fiilde zamanaşımı zararı ve faili öğrenmeden itibaren 2 yıl, her halde fiilin işlendiği tarihten itibaren 10 yıldır.")
    ]
    for q, a, b, c, d, e, ans, sol in medeni_items:
        for lvl in range(1, 4):
            add('hmgs-medeni-kisiler-aile', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-medeni-esya', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-borclar-genel', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # TTK (Ticaret Hukuku)
    # =========================================================================
    ticaret_items = [
        ("6102 sayılı TTK'ya göre Anonim Şirketin kurulabilmesi için asgari esas sermaye tutarı (Cumhurbaşkanı kararı ve 2024 tebliği ile) en az ne kadardır?",
         "50.000 TL", "100.000 TL", "250.000 TL", "500.000 TL", "1.000.000 TL", "c",
         "Cumhurbaşkanı Kararı (Karar Sayısı: 7887) uyarınca 01.01.2024 tarihinden itibaren Anonim Şirket asgari sermayesi 250.000 TL, Limited Şirket ise 50.000 TL olarak güncellenmiştir."),
        ("Limited şirkette ortak sayısı en fazla kaç olabilir?",
         "20", "50", "100", "250", "Sınırsızdır", "b",
         "TTK m. 574 uyarınca Limited şirkette ortak sayısı 50'yi aşamaz; aşarsa anonim şirkete dönüşmesi gerekir."),
        ("TTK'ya göre bir ticari işletmeyi kısmen de olsa kendi adına işleten kişiye ne ad verilir?",
         "Esnaf", "Tacir", "Ticari Temsilci", "Acente", "Komisyoncu", "b",
         "TTK m. 12 uyarınca bir ticari işletmeyi kısmen dahi olsa kendi adına işleten kimseye tacir denir.")
    ]
    for q, a, b, c, d, e, ans, sol in ticaret_items:
        for lvl in range(1, 4):
            add('hmgs-ticaret-isletme', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-ticaret-sirketler', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-ticaret-kiymetli-evrak', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # İİK (İcra ve İflas Hukuku)
    # =========================================================================
    iik_items = [
        ("İcra dairesine yapılan itirazın kaldırılması talebi icra mahkemesince reddedilen alacaklının açabileceği dava hangisidir?",
         "İtirazın iptali davası", "Menfi tespit davası", "İstirdat davası", "Şikâyet davası", "Yeniden takip talebi", "a",
         "İİK m. 67 uyarınca alacaklı icra mahkemesinden itirazın kaldırılmasını sağlayamazsa genel mahkemede 1 yıllık süre içinde itirazın iptali davası açabilir."),
        ("Hacizli malın satış bedeli bütün alacaklıların alacağını karşılamaya yetmezse icra dairesi parayı paylaştırmak için ne düzenler?",
         "Gider Pusulası", "Sıra Cetveli", "Muvazaa İlamı", "Tahsil Fişi", "Paylaşım Protokolü", "b",
         "İİK m. 140 uyarınca satış tutarı bütün alacaklıların alacağını ödemeye yetmezse icra dairesi bir sıra cetveli yapar.")
    ]
    for q, a, b, c, d, e, ans, sol in iik_items:
        for lvl in range(1, 4):
            add('hmgs-iik-ilamsiz-icra', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-iik-haciz-satis', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-iik-ilamli-iflas', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # Avukatlık Hukuku & Hukuk Felsefesi (1136 Sayılı Kanun)
    # =========================================================================
    av_items = [
        ("1136 sayılı Avukatlık Kanunu'na göre avukatlık stajı kaç yıldır ve nasıl bölünür?",
         "1 yıl (6 ay mahkemelerde, 6 ay avukat yanında)",
         "2 yıl (1 yıl adliyede, 1 yıl büroda)",
         "1 yıl (tamamı avukat yanında)",
         "6 ay (3 ay adliye, 3 ay büro)",
         "18 ay", "a",
         "1136 sayılı Avukatlık Kanunu m. 15 uyarınca avukatlık stajı 1 yıl olup; ilk 6 ayı adliyede mahkemelerde, kalan 6 ayı en az 5 yıl kıdemli bir avukat yanında yapılır."),
        ("Avukatın aynı işte menfaatleri zıt olan iki tarafa birden vekillik etmesi durumunda hangisi söz konusudur?",
         "Görevin ifası", "Vekillikten çekilme zorunluluğu ve disiplin suçu", "İhtiyari temsil", "Arabuluculuk", "Sulh yetkisi", "b",
         "Avukatlık Kanunu m. 38/b uyarınca aynı işte menfaati zıt olan tarafları temsil etmek yasaktır; avukat vekillikten çekilmek zorundadır."),
        ("Hukuk felsefesinde 'Hukuk, egemenin yaptırımla desteklenmiş buyruğudur' tanımı hangi hukuk akımına aittir?",
         "Doğal Hukuk Akımı", "Hukuki Pozitivizm (John Austin / Kelsen)", "Tarihçi Hukuk Ekolü (Savigny)", "Hukuki Realizm", "Marksist Hukuk Teorisi", "b",
         "Pozitivist hukuk anlayışında (özellikle John Austin'in emir teorisinde) hukuk, egemen otoritenin müeyyideye bağlanmış emri olarak tanımlanır.")
    ]
    for q, a, b, c, d, e, ans, sol in av_items:
        for lvl in range(1, 4):
            add('hmgs-avukatlik-kanunu', q, a, b, c, d, e, ans, sol, lvl)
            add('hmgs-hukuk-felsefesi', q, a, b, c, d, e, ans, sol, lvl)

    print(f"HMGS üretilen soru sayısı: {len(questions)}")
    return questions

if __name__ == '__main__':
    with open('d:/quiza/scratch_osym/law_subcats_map.json', 'r', encoding='utf-8') as f:
        subcats = json.load(f)
    subcat_by_slug = {s['slug']: s for s in subcats}
    qs = generate_hmgs_questions(subcat_by_slug)
    print("Örnek HMGS soru:", qs[0]['question'][:60], "Kategori:", qs[0]['category'])
