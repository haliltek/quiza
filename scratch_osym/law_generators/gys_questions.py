# -*- coding: utf-8 -*-
"""
Adalet Bakanlığı Görevde Yükselme Sınavı (GYS) Kapsamlı Soru Üretici Modülü
(657 DMK, 7201 Tebligat, Yazı İşleri Yönetmeliği, Harçlar Kanunu, HMK/CMK İlkeleri, UYAP)
"""
import json
import random

def generate_gys_questions(subcat_by_slug):
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
    # 1. gys-ay-yargi: Anayasa & Yargı Organları
    # =========================================================================
    ay_items = [
        ("1982 Anayasası'na göre, Hâkimler ve Savcılar Kurulu (HSK) kaç üyeden oluşur ve kaç daire halinde çalışır?",
         "11 üye - 2 daire", "13 üye - 2 daire", "15 üye - 3 daire", "17 üye - 3 daire", "21 üye - 4 daire", "b",
         "1982 Anayasası m. 159 uyarınca HSK 13 üyeden oluşur ve iki daire halinde çalışır. Kurulun başkanı Adalet Bakanıdır."),
        ("1982 Anayasası'na göre Hâkimler ve Savcılar Kurulu'nun Başkanı aşağıdakilerden hangisidir?",
         "Yargıtay Birinci Başkanı", "Danıştay Başkanı", "Adalet Bakanı", "Adalet Bakanlığı Bakan Yardımcısı", "Cumhurbaşkanı", "c",
         "Anayasa m. 159 uyarınca HSK'nın başkanı Adalet Bakanı, tabii üyesi ise Adalet Bakanlığı ilgili Bakan Yardımcısıdır."),
        ("1982 Anayasası'na göre, adli ve idari yargı mercileri arasındaki görev ve hüküm uyuşmazlıklarını kesin olarak çözmeye yetkili yüksek mahkeme hangisidir?",
         "Anayasa Mahkemesi", "Yargıtay", "Danıştay", "Uyuşmazlık Mahkemesi", "Sayıştay", "d",
         "Anayasa m. 158'e göre adli ve idari yargı mercileri arasındaki görev ve hüküm uyuşmazlıklarını Uyuşmazlık Mahkemesi kesin karara bağlar."),
        ("1982 Anayasası'na göre Anayasa Mahkemesi kaç üyeden oluşur?",
         "12", "15", "17", "19", "21", "b",
         "2017 Anayasa değişikliği ile Askeri Yargı kaldırılmış ve Anayasa Mahkemesi üye sayısı 15 olarak düzenlenmiştir (m. 146)."),
        ("Anayasa Mahkemesi üyelerinin görev süresi kaç yıldır ve bir kimse kaç defa üye seçilebilir?",
         "9 yıl - Bir kez daha seçilebilir", "12 yıl - İki defa seçilebilir", "12 yıl - Bir kimse iki defa üye seçilemez", "6 yıl - Yeniden seçilebilir", "Ömür boyu (65 yaşına kadar)", "c",
         "Anayasa m. 147 uyarınca AYM üyeleri 12 yıl için seçilirler ve bir kimse iki defa Anayasa Mahkemesi üyesi seçilemez."),
        ("1982 Anayasası'na göre Danıştay üyelerinin kaçta kaçını Hâkimler ve Savcılar Kurulu seçer?",
         "1/2'sini", "2/3'ünü", "3/4'ünü", "1/3'ünü", "Tamamını", "c",
         "Anayasa m. 155 uyarınca Danıştay üyelerinin 3/4'ünü HSK, 1/4'ünü ise Cumhurbaşkanı seçer."),
        ("Yargıtay Cumhuriyet Başsavcısı ve Vekilini, Yargıtay Genel Kurulu'nun gösterdiği adaylar arasından kim seçer?",
         "TBMM", "HSK", "Cumhurbaşkanı", "Adalet Bakanı", "Yargıtay Birinci Başkanı", "c",
         "Anayasa m. 154 uyarınca Yargıtay Cumhuriyet Başsavcısı ve Vekilini, Yargıtay Genel Kurulu'nun belirlediği 5'er aday arasından 4 yıl için Cumhurbaşkanı seçer."),
        ("1982 Anayasası'na göre hâkimler ve savcılar idari görevleri yönünden nereye bağlıdırlar?",
         "Hâkimler ve Savcılar Kuruluna", "Adalet Bakanlığına", "Yargıtay Başkanlığına", "Cumhurbaşkanlığına", "Danıştay Başkanlığına", "b",
         "Anayasa m. 140/6 uyarınca hâkimler ve savcılar adli görevlerinde bağımsız olup, idari görevleri yönünden Adalet Bakanlığına bağlıdırlar."),
        ("Hâkimler ve savcılar kural olarak kaç yaşını dolduruncaya kadar hizmet görürler (hâkimlik teminatı)?",
         "60", "63", "65", "67", "70", "c",
         "Anayasa m. 144 uyarınca hâkim ve savcılar kendileri istemedikçe 65 yaşından önce emekliye sevk edilemezler."),
        ("Aşağıdakilerden hangisi 1982 Anayasası'nda sayılan Yüksek Mahkemeler arasında yer almaz?",
         "Yargıtay", "Danıştay", "Uyuşmazlık Mahkemesi", "Sayıştay", "Anayasa Mahkemesi", "d",
         "Anayasa'nın Yargı bölümünde Yüksek Mahkemeler; AYM, Yargıtay, Danıştay ve Uyuşmazlık Mahkemesidir. Sayıştay mali denetim organıdır.")
    ]
    for q, a, b, c, d, e, ans, sol in ay_items:
        for lvl in range(1, 4):
            add('gys-ay-yargi', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 2. gys-dmk-haklar-odevler: 657 DMK Haklar, Ödevler ve Yasaklar
    # =========================================================================
    dmk_hak_items = [
        ("657 sayılı Devlet Memurları Kanunu'na göre, memurların kanunda belirtilen süre ve şartlarla kademe ilerlemesi ve derece yükselmesi yapabilmelerini sağlayan temel ilke hangisidir?",
         "Liyakat", "Kariyer", "Sınıflandırma", "Eşitlik", "Tarafsızlık", "b",
         "657 sayılı DMK m. 3 uyarınca 'Kariyer', devlet memurlarına yaptıkları hizmetler için lüzumlu bilgilere ve yetişme şartlarına uygun şekilde, sınıfları içinde en yüksek derecelere kadar ilerleme imkanını sağlamaktır."),
        ("657 sayılı Kanun'a göre memurların görevlerini yerine getirirken dil, ırk, cinsiyet, siyasi düşünce, felsefi inanç ayrımı yapamayacaklarını belirten temel ilke/ödev hangisidir?",
         "Sadakat", "Tarafsızlık ve devlete bağlılık", "Davranış ve işbirliği", "Liyakat", "Kariyer", "b",
         "657 sayılı DMK m. 7 uyarınca Devlet memurları siyasi partiye üye olamazlar ve hiçbir şekilde ayrım yapmaksızın tarafsızlık ilkesine bağlı kalmak zorundadırlar."),
        ("657 sayılı DMK'ya göre devlet memurlarının hediye alma yasağının kapsamını belirlemeye ve uygulamayı izlemeye yetkili kurul hangisidir?",
         "Devlet Personel Başkanlığı", "Kamu Görevlileri Etik Kurulu", "Hakimler ve Savcılar Kurulu", "Sayıştay", "Cumhurbaşkanlığı İdari İşler Başkanlığı", "b",
         "657 DMK m. 29 ve 5176 sayılı Kanun uyarınca hediye alma yasağının kapsamını Kamu Görevlileri Etik Kurulu belirler."),
        ("657 sayılı Devlet Memurları Kanunu'na göre devlet memurları sonu (0) ve (5) ile biten yıllarda en geç hangi ayın sonuna kadar mal bildiriminde bulunmak zorundadırlar?",
         "Ocak ayı sonuna kadar", "Şubat ayı sonuna kadar", "Mart ayı sonuna kadar", "Nisan ayı sonuna kadar", "Mayıs ayı sonuna kadar", "b",
         "3628 sayılı Kanun ve 657 DMK m. 14 uyarınca genel mal bildirimi sonu 0 ve 5 ile biten yıllarda en geç Şubat ayı sonuna kadar verilir."),
        ("Devlet memuruna amiri tarafından verilen emir, Anayasa, kanun, tüzük veya yönetmelik hükümlerine aykırı ise memur ne yapmalıdır (Kanunsuz Emir)?",
         "Emri derhal yerine getirmelidir.",
         "Bu aykırılığı emri verene bildirir; amir emrinde ısrar eder ve emrini yazı ile yenilerse emri yerine getirir ve sorumluluk emri verene ait olur.",
         "Cumhuriyet Başsavcılığına suç duyurusunda bulunmalıdır.",
         "Emri hiçbir surette yerine getiremez ve derhal sendikasına başvurur.",
         "Doğrudan bir üst amire şikayet eder.", "b",
         "657 DMK m. 11 ve Anayasa m. 137 uyarınca kanunsuz emir yazılı olarak yenilenirse yerine getirilir; ancak konusu suç teşkil eden emir hiçbir surette yerine getirilemez."),
        ("657 sayılı DMK'ya göre konusu suç teşkil eden bir emirle karşılaşan memurun tutumu ne olmalıdır?",
         "Yazılı olarak verilirse yerine getirir.",
         "Sözlü emirle de yerine getirir.",
         "Emri kesinlikle yerine getirmez; yerine getiren kimse sorumluluktan kurtulamaz.",
         "İki şahit huzurunda emri uygular.",
         "Vali veya Kaymakam onaylarsa uygular.", "c",
         "Anayasa m. 137 ve 657 DMK m. 11: Konusu suç teşkil eden emir hiçbir suretle yerine getirilmez; yerine getiren kimse cezai sorumluluktan kurtulamaz."),
        ("Devlet memurlarının ticaret ve diğer kazanç getirici faaliyetlerde bulunma yasağına göre memurlar aşağıdakilerden hangisini yapabilirler?",
         "Anonim şirkette yönetim kurulu üyesi olmak",
         "Limited şirkete müdür olarak atanmak",
         "Tacir veya esnaf sayılmalarını gerektirecek faaliyette bulunmak",
         "Anonim şirkette pay sahibi (hissedar) olmak",
         "Ticari vekil veya ticari mümessil olmak", "d",
         "657 DMK m. 28 uyarınca memurlar anonim şirketlerin hisse senetlerini alarak pay sahibi olabilirler; ancak şirketlerin yönetim ve denetim organlarında görev alamazlar."),
        ("Hizmet süresi 1 yıldan 10 yıla kadar (10 yıl dahil) olan devlet memurlarının yıllık izin süresi kaç gündür?",
         "15 gün", "20 gün", "25 gün", "30 gün", "35 gün", "b",
         "657 sayılı DMK m. 102 uyarınca hizmeti 1 yıldan 10 yıla kadar olan memurların yıllık izni 20 gün, 10 yıldan fazla olanların izni 30 gündür.")
    ]
    for q, a, b, c, d, e, ans, sol in dmk_hak_items:
        for lvl in range(1, 4):
            add('gys-dmk-haklar-odevler', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 3. gys-dmk-disiplin: Disiplin Cezaları ve Zamanaşımı
    # =========================================================================
    dmk_ceza_items = [
        ("657 sayılı DMK'ya göre aşağıdakilerden hangisi kanunda sayılan disiplin cezalarından biri değildir?",
         "Uyarma", "Kınama", "Aylıktan kesme", "Görevden uzaklaştırma", "Kademe ilerlemesinin durdurulması", "d",
         "657 DMK m. 125'te disiplin cezaları Uyarma, Kınama, Aylıktan Kesme, Kademe İlerlemesinin Durdurulması ve Memurluktan Çıkarma olarak 5 tanedir. Görevden uzaklaştırma bir ceza değil ihtiyati tedbirdir."),
        ("657 sayılı DMK'ya göre disiplin soruşturması açılması için eylemin öğrenildiği tarihten itibaren öngörülen zamanaşımı süresi uyarma, kınama ve aylıktan kesmede kaç aydır?",
         "1 ay", "3 ay", "6 ay", "1 yıl", "2 yıl", "a",
         "657 DMK m. 127 uyarınca uyarma, kınama, aylıktan kesme ve kademe ilerlemesinin durdurulmasında fiilin öğrenildiği tarihten itibaren 1 ay içinde soruşturmaya başlanmalıdır."),
        ("Disiplin cezasını gerektiren fiil ve hallerin işlendiği tarihten itibaren kaç yıl geçmişse artık disiplin cezası verilemez (nihai ceza zamanaşımı)?",
         "1 yıl", "2 yıl", "3 yıl", "5 yıl", "10 yıl", "b",
         "657 DMK m. 127 uyarınca disiplin cezasını gerektiren fiil ve hallerin işlendiği tarihten itibaren 2 yıl içinde ceza verilmezse ceza verme yetkisi zamanaşımına uğrar."),
        ("657 sayılı DMK'ya göre memura savunma hakkı tanınmadan ceza verilemez. Memura savunmasını yapması için verilen süre en az kaç gündür?",
         "3 gün", "5 gün", "7 gün", "10 gün", "15 gün", "c",
         "657 DMK m. 130 uyarınca savunma için memura en az 7 gün süre tanınır. Bu sürede savunma yapmayan vazgeçmiş sayılır."),
        ("Devlet memurluğundan çıkarma cezası kimin kararı ile verilir?",
         "Atamaya yetkili amir", "Disiplin Amiri", "Yüksek Disiplin Kurulu", "İl Disiplin Kurulu", "Cumhuriyet Başsavcısı", "c",
         "657 DMK m. 126 uyarınca Devlet memurluğundan çıkarma cezası amirlerin bu yoldaki isteği üzerine Yüksek Disiplin Kurulu kararı ile verilir."),
        ("Aylıktan kesme cezasında memurun brüt aylığından hangi oranda kesinti yapılır?",
         "1/30 - 1/8", "1/10 - 1/5", "1/4 - 1/2", "Yarısı", "Tamamı", "a",
         "657 DMK m. 125 uyarınca aylıktan kesme cezası memurun brüt aylığından 1/30 ile 1/8 arasında kesinti yapılmasıdır."),
        ("Özürsüz olarak bir yılda toplam 20 gün göreve gelmeyen memura hangi disiplin cezası uygulanır?",
         "Kınama", "Aylıktan kesme", "Kademe ilerlemesinin durdurulması", "Devlet memurluğundan çıkarma", "Görevden uzaklaştırma", "d",
         "657 DMK m. 125/E-d uyarınca özürsüz veya izinsiz olarak bir yılda toplam 20 gün göreve gelmemek Devlet memurluğundan çıkarma cezasını gerektirir."),
        ("Uyarma ve kınama cezalarının özlük dosyasından silinmesi için cezanın uygulanmasından itibaren kaç yıl geçmesi gerekir?",
         "3 yıl", "5 yıl", "7 yıl", "10 yıl", "Silinemez", "b",
         "657 DMK m. 133 uyarınca uyarma ve kınama cezaları 5 yıl, diğer cezalar ise 10 yıl sonra sicilden/özlükten silinmesi için başvurulabilir.")
    ]
    for q, a, b, c, d, e, ans, sol in dmk_ceza_items:
        for lvl in range(1, 4):
            add('gys-dmk-disiplin', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 4. gys-tebligat-uets & gys-tebligat-madde21-35: 7201 Tebligat Hukuku
    # =========================================================================
    tebligat_items = [
        ("7201 sayılı Tebligat Kanunu m. 7/a uyarınca, elektronik yolla tebligat, muhatabın elektronik adresine ulaştığı tarihi izleyen kaçıncı günün sonunda yapılmış sayılır?",
         "Ulaştığı gün", "İkinci günün sonunda", "Üçüncü günün sonunda", "Beşinci günün sonunda", "Yedinci günün sonunda", "d",
         "7201 sayılı Tebligat Kanunu m. 7/a ve Elektronik Tebligat Yönetmeliği gereğince e-tebligat, adrese ulaştığı tarihi izleyen 5. günün sonunda tebliğ edilmiş sayılır."),
        ("7201 sayılı Tebligat Kanunu'na göre aşağıdakilerden hangisine elektronik tebligat yapılması zorunlu değildir?",
         "Baro levhasına kayıtlı avukatlara", "Noterlere", "Anonim ve Limited Şirketlere", "Gerçek kişi tacirlere (şahıs işletmeleri)", "Kamu iktisadi teşebbüslerine", "d",
         "Elektronik Tebligat Yönetmeliği m. 5 uyarınca gerçek kişi tacirlere UETS zorunlu olmayıp isteğe bağlıdır; sermaye şirketleri, avukatlar ve noterler ise zorunludur."),
        ("Tebligat yapılacak kimse veya adına tebellüğ edebilecek kimselerden hiçbiri gösterilen adreste bulunmazsa, posta memuru tebliğ evrakını nereye teslim eder (Tebligat K. Madde 21/1)?",
         "İlgili karakola teslim eder.",
         "O yerin muhtarına veya ihtiyar heyeti azasından birine ya da zabıta amir veya memuruna teslim eder ve ihbarnameyi kapıya yapıştırır.",
         "Evrakı kapının altından atar.",
         "Komşusuna imza karşılığı teslim eder.",
         "Doğrudan mahkemeye iade eder.", "b",
         "Tebligat Kanunu m. 21/1 gereğince evrak muhtar/ihtiyar heyeti/zabıta amirine teslim edilir, tesellüm makbuzu alınır ve muhatabın kapısına 2 numaralı ihbarname yapıştırılır."),
        ("Tebligat Kanunu Madde 21/1'e göre yapılan tebligatta tebliğ tarihi hangi tarihtir?",
         "Evrakın muhtara verildiği tarih", "İhbarnamenin kapıya yapıştırıldığı tarih", "Muhatabın evrakı muhtardan aldığı tarih", "Tebligatın postaya verildiği tarih", "İhbarnameden 5 gün sonraki tarih", "b",
         "Yargıtay İçtihadı Birleştirme Kararları ve Tebligat Kanunu m. 21 uyarınca ihbarnamenin kapıya yapıştırıldığı tarih tebliğ tarihi sayılır."),
        ("Muhatabın bilinen en son adresine çıkartılan tebligatın bila-tebliğ dönmesi üzerine, MERNİS (Adres Kayıt Sistemi) adresine doğrudan Tebligat K. m. 21/2 şerhiyle tebligat çıkarılması durumunda posta memuru ne yapar?",
         "Muhatap o adreste hiç oturmamış olsa bile evrakı muhtara teslim edip ihbarnameyi kapıya yapıştırır.",
         "Komşularına sorar, komşuları tanımıyorsa evrakı iade eder.",
         "Muhatabın telefonunu arar.",
         "MERNİS adresinde muhatap bulunmadığı için evrakı mahkemeye iade eder.",
         "Tebligatı iptal eder.", "a",
         "Tebligat Kanunu m. 21/2 uyarınca MERNİS adresine yapılan tebligatta memur adres araştırması yapmaz, evrakı doğrudan muhtara teslim eder ve ihbarnameyi kapıya yapıştırır."),
        ("7201 sayılı Tebligat Kanunu'na göre kural olarak gece vakti tebligat yapılabilir mi?",
         "Hiçbir surette yapılamaz.",
         "Gece vakti tebligat yapılabilir (Gece tebligatı yasağı 2003 yılında kaldırılmıştır).",
         "Yalnızca hâkimin özel izniyle yapılabilir.",
         "Yalnızca kolluk marifetiyle yapılabilir.",
         "Sadece iflas takiplerinde yapılabilir.", "b",
         "7201 sayılı Tebligat Kanunu m. 33'teki gece tebligat yasağı 4829 sayılı Kanun ile yürürlükten kaldırılmıştır; gece vakti de tebligat yapılması caizdir."),
        ("Vekil ile takip edilen işlerde tebligat kime yapılmalıdır?",
         "Asile (müvekkile)", "Vekile (avukata)", "Hem asile hem vekile", "Asilin ailesine", "Asilin muhtarına", "b",
         "Tebligat Kanunu m. 11 ve HMK m. 73 uyarınca vekil ile takip edilen davalarda tebligatın zorunlu olarak vekile yapılması gerekir; asile yapılan tebligat geçersizdir.")
    ]
    for q, a, b, c, d, e, ans, sol in tebligat_items:
        for lvl in range(1, 4):
            add('gys-tebligat-uets', q, a, b, c, d, e, ans, sol, lvl)
            add('gys-tebligat-madde21-35', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 5. gys-yazi-tevzi-tensip & gys-yazi-tutanak-kesinlesme: Yazı İşleri Yönetmeliği
    # =========================================================================
    yazi_items = [
        ("Bölge Adliye ve Adli Yargı İlk Derece Mahkemeleri Yazı İşleri Hizmetlerinin Yürütülmesine Dair Yönetmelik'e göre, dava harç ve gider avansının ödendiği tarihte ne gerçekleşmiş sayılır?",
         "Tensip zaptı düzenlenmiş sayılır.", "Dava açılmış sayılır.", "Ön inceleme duruşması yapılmış sayılır.", "Cevap dilekçesi verilmiş sayılır.", "Hüküm kesinleşmiş sayılır.", "b",
         "HMK m. 118 ve Yazı İşleri Yönetmeliği m. 47 uyarınca dava dilekçesinin kaydedildiği ve harcın yatırıldığı tarihte dava açılmış sayılır."),
        ("Yazı İşleri Hizmetleri Yönetmeliği'ne göre, hâkim ve zabıt kâtibince güvenli elektronik imza ile imzalanan duruşma tutanakları ne zaman onaylanmalıdır?",
         "En geç duruşmanın bittiği gün mesai bitimine kadar",
         "Duruşma biter bitmez derhal hâkim ve zabıt kâtibi tarafından e-imza ile imzalanır ve UYAP'ta onaylanır",
         "Duruşmadan sonraki 3 iş günü içinde",
         "Haftalık dosya inceleme gününde",
         "Gerekçeli karar yazılırken", "b",
         "Yönetmelik m. 56 gereğince duruşma tutanağı duruşma biter bitmez zabıt kâtibi ve hâkim tarafından güvenli elektronik imza ile imzalanarak sisteme aktarılır."),
        ("HMK ve Yazı İşleri Yönetmeliği'ne göre ilk derece mahkemelerinde gerekçeli karar, hükmün tefhiminden itibaren en geç ne kadar süre içinde yazılmalıdır?",
         "7 gün", "15 gün", "1 ay", "45 gün", "2 ay", "c",
         "HMK m. 294/4 uyarınca gerekçeli karar, hükmün tefhim edildiği tarihten başlayarak 1 ay içinde yazılır ve mahkeme yazı işleri müdürlüğünce taraflara tebliğ edilir."),
        ("Mahkeme ilamının kesinleşmesi üzerine yazı işleri müdürü veya yetkilendirilen personel tarafından kararın altına yazılan ve kararın bağlayıcı olduğunu gösteren belgeye ne ad verilir?",
         "Tevzi Formu", "Tensip Şerhi", "Kesinleşme Şerhi", "Derkenar", "Tebellüğ Belgesi", "c",
         "Yazı İşleri Yönetmeliği m. 63 uyarınca kanun yolları tüketilmiş veya kanun yoluna başvurulmamış kararların altına 'Kesinleşme Şerhi' yazılarak onaylanır."),
        ("Adli Emanet Memurluğuna teslim edilen suç eşyası hangi deftere/kayda işlenir?",
         "Tevzi Kaydı", "Duruşma Defteri", "Adli Emanet Defteri (Suç Eşyası Kaydı)", "Kasa Defteri", "Muhabere Defteri", "c",
         "Suç Eşyası Yönetmeliği ve Yazı İşleri Yönetmeliği uyarınca emanete alınan kıymetli evrak, para ve suç eşyası Adli Emanet Kaydına sıra numarası ile kaydedilir.")
    ]
    for q, a, b, c, d, e, ans, sol in yazi_items:
        for lvl in range(1, 4):
            add('gys-yazi-tevzi-tensip', q, a, b, c, d, e, ans, sol, lvl)
            add('gys-yazi-tutanak-kesinlesme', q, a, b, c, d, e, ans, sol, lvl)
            add('gys-yazi-emanet-arsiv', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 6. gys-harclar-yargi & gys-gider-avansi: Harçlar Kanunu ve Gider Avansı
    # =========================================================================
    harc_items = [
        ("492 sayılı Harçlar Kanunu'na göre, konusu para veya para ile değerlendirilebilen davalarda peşin karar ve ilam harcı, nispi harcın kaçta kaçı oranında peşin alınır?",
         "1/2'si", "1/3'ü", "1/4'ü", "1/5'i", "Tamamı", "c",
         "492 sayılı Harçlar Kanunu m. 28/a uyarınca nispi karar ve ilam harcının dörtte biri (1/4) peşin alınır, bakiye karar kesinleşince tahsil edilir."),
        ("HMK m. 120 uyarınca dava açılırken yatırılan gider avansının yeterli olmadığının dava sırasında anlaşılması halinde mahkemece davacıya verilen kesin süre kaç haftadır?",
         "1 hafta", "2 hafta", "3 hafta", "1 ay", "30 gün", "b",
         "HMK m. 120/2 uyarınca avansın yetersiz kalması halinde mahkemece 2 haftalık kesin süre verilir; verilen sürede tamamlanmazsa dava usulden reddedilir."),
        ("Davanın başında yatırılan gider avansından yargılama sonunda arta kalan kısım ne şekilde işlem görür?",
         "Hazineye irat kaydedilir.",
         "Yazı işleri müdürü tarafından ilgilinin bildireceği banka hesabına iade edilir.",
         "Baroya aktarılır.",
         "Adalet Bakanlığı döner sermayesine devredilir.",
         "Temyiz harcına mahsup edilir.", "b",
         "Gider Avansı Tarifesi m. 5 uyarınca kullanılmayan avans bakiye kısmı, karar kesinleştikten sonra davacıya re'sen iade edilir.")
    ]
    for q, a, b, c, d, e, ans, sol in harc_items:
        for lvl in range(1, 4):
            add('gys-harclar-yargi', q, a, b, c, d, e, ans, sol, lvl)
            add('gys-gider-avansi', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 7. gys-hmk-sureler & gys-cmk-kararlar: HMK / CMK İlkeleri
    # =========================================================================
    usul_items = [
        ("8. Yargı Paketi ile Hukuk Muhakemeleri Kanunu ve Ceza Muhakemesi Kanununda yapılan değişiklik sonucu, istinaf ve temyiz kanun yolu başvuru süresi nasıl yeknesaklaştırılmıştır?",
         "Gerekçeli kararın tebliğinden itibaren 15 gün",
         "Gerekçeli kararın tebliğinden itibaren 2 hafta",
         "Gerekçeli kararın tefhiminden itibaren 7 gün",
         "Hükmün verilmesinden itibaren 1 ay",
         "Tebliğden itibaren 30 gün", "b",
         "8. Yargı Paketi (7499 sayılı Kanun) ile HMK ve CMK'daki istinaf ve temyiz başvuru süreleri tebliğden itibaren '2 hafta' olarak yeknesaklaştırılmıştır."),
        ("Her yıl adli tatil hangi tarihler arasında uygulanır?",
         "1 Temmuz - 1 Eylül", "20 Temmuz - 31 Ağustos", "15 Temmuz - 15 Ağustos", "1 Ağustos - 15 Eylül", "20 Haziran - 1 Eylül", "b",
         "HMK m. 102 ve CMK m. 331 uyarınca adli tatil her yıl yirmi temmuzda başlar ve otuz bir ağustosta sona erer. Yeni adli yıl 1 Eylülde başlar."),
        ("Adli tatile denk gelen ve adli tatilde işlemeyen sürelerin bitimi adli tatilin bittiği günden itibaren ne kadar uzar?",
         "3 gün", "1 hafta", "10 gün", "15 gün", "1 ay", "b",
         "HMK m. 104 uyarınca adli tatile rastlayan süreler, tatilin bittiği günden itibaren bir hafta uzatılmış sayılır (yani 7 Eylül mesai bitimi)."),
        ("Cumhuriyet Savcısının soruşturma evresi sonunda kamu davası açılması için yeterli şüphe oluşturacak delil elde edilememesi durumunda verdiği karar hangisidir?",
         "Davanın Düşmesi Kararı",
         "Kovuşturmaya Yer Olmadığına Dair Karar (KYOK)",
         "Beraat Kararı",
         "Görevsizlik Kararı",
         "Kamu Davasının Açılmasının Ertelenmesi Kararı", "b",
         "CMK m. 172 uyarınca yeterli şüphe bulunmaması veya kovuşturma olanağının kalmaması halinde Cumhuriyet savcısı Kovuşturmaya Yer Olmadığına (KYOK) karar verir.")
    ]
    for q, a, b, c, d, e, ans, sol in usul_items:
        for lvl in range(1, 4):
            add('gys-hmk-sureler', q, a, b, c, d, e, ans, sol, lvl)
            add('gys-cmk-kararlar', q, a, b, c, d, e, ans, sol, lvl)

    # =========================================================================
    # 8. gys-uyap-e-imza & gys-resmi-yazisma: UYAP ve Resmi Yazışma
    # =========================================================================
    uyap_items = [
        ("5070 sayılı Elektronik İmza Kanunu'na göre, aşağıdakilerden hangisinde güvenli elektronik imza kullanılamaz?",
         "Mahkeme kararlarında", "Tensip zaptında", "Kanunların resmi şekle veya özel merasime bağladığı işlemler ile teminat sözleşmelerinde", "Dava dilekçesinde", "Duruşma tutanağında", "c",
         "5070 sayılı Kanun m. 5 uyarınca kanunların resmi şekle veya özel merasime bağladığı hukuki işlemler ile teminat sözleşmeleri güvenli e-imza ile yapılamaz."),
        ("Resmî Yazışmalarda Uygulanacak Usul ve Esaslar Hakkında Yönetmelik'e göre, belgeye metin içinde veya ekte belirtilen sürede cevap verilmemesi halinde gönderilen yazıya ne ad verilir?",
         "İhbar", "Tekit Yazısı", "Tensip", "Müzekkere", "Talimat", "b",
         "Resmî Yazışma Yönetmeliği uyarınca süresi içinde cevaplandırılmayan yazılara ilişkin muhataba gönderilen uyarıcı ikinci yazıya 'Tekit Yazısı' denir."),
        ("UYAP sistemi üzerinden mahkemeye sunulan elektronik imzalı dava dilekçesinin sisteme kaydedildiği tarih olarak hangisi kabul edilir?",
         "Hâkimin dilekçeyi incelediği an", "Dilekçenin UYAP sunucusuna girdiği ve harcın ödendiği zaman damgası", "Yazı işleri müdürünün mesaiye başladığı saat", "Karşı tarafa tebliğ edildiği gün", "Mahkeme kaleminin onayladığı gün", "b",
         "Hukuk Muhakemeleri Kanunu Yönetmeliği uyarınca UYAP üzerinden açılan davalarda evrakın sisteme yüklendiği ve harcın tahsil edildiği an dava açılış anıdır.")
    ]
    for q, a, b, c, d, e, ans, sol in uyap_items:
        for lvl in range(1, 4):
            add('gys-uyap-e-imza', q, a, b, c, d, e, ans, sol, lvl)
            add('gys-resmi-yazisma', q, a, b, c, d, e, ans, sol, lvl)

    print(f"GYS üretilen soru sayısı: {len(questions)}")
    return questions

if __name__ == '__main__':
    with open('d:/quiza/scratch_osym/law_subcats_map.json', 'r', encoding='utf-8') as f:
        subcats = json.load(f)
    subcat_by_slug = {s['slug']: s for s in subcats}
    qs = generate_gys_questions(subcat_by_slug)
    print("Örnek GYS soru:", qs[0]['question'][:60], "Kategori:", qs[0]['category'])
