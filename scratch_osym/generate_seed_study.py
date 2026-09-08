import subprocess
import json

notes = [
    # --- TARİH: HAP BİLGİLER (category_id = 1, note_type = 'spot') ---
    (52, 1, 1, 'spot', '1. Orta Asya İlk Türk Devletleri', 'İlk Türk devletleri bozkır kültürüne dayalıdır, göçebe ve konargöçer yaşam hâkimdir.', 1, 0),
    (52, 1, 1, 'spot', '1. Orta Asya İlk Türk Devletleri', 'Ordu-millet anlayışı gelişmiştir, kadınlar (Hatun) kurultayda ve devlet yönetiminde söz sahibidir.', 2, 0),
    (52, 1, 1, 'spot', '1. Orta Asya İlk Türk Devletleri', 'Kut inancı vardır: Hükümdara devleti yönetme yetkisinin Gök Tengri tarafından verildiğine inanılır.', 3, 0),
    (52, 1, 1, 'spot', '1. Orta Asya İlk Türk Devletleri', 'İkili teşkilat uygulanmıştır: Doğu merkez kabul edilir ve asıl kağan yönetir, batıyı ise yabgu unvanıyla hanedan üyesi yönetir.', 4, 0),
    (52, 1, 1, 'spot', '2. Asya Hun Devleti (Büyük Hun)', 'Tarihte bilinen teşkilatlı ilk Türk devletidir. Başkenti Ötüken\'dir.', 5, 0),
    (52, 1, 1, 'spot', '2. Asya Hun Devleti (Büyük Hun)', 'Kurucusu Teoman, en parlak ve güçlü dönemi Mete Han zamanıdır.', 6, 0),
    (52, 1, 1, 'spot', '2. Asya Hun Devleti (Büyük Hun)', 'Mete Han Türk tarihinde ilk düzenli orduyu (Onluk Sistem) kurmuştur (MÖ 209 - TSK kuruluş yılı).', 7, 0),
    (52, 1, 1, 'spot', '2. Asya Hun Devleti (Büyük Hun)', 'Orta Asya\'da tüm Türk boylarını tek bayrak altında toplayan ilk hükümdar Mete Han\'dır.', 8, 0),
    (52, 1, 1, 'spot', '3. I. ve II. Göktürk (Kutluk) Devleti', 'Türk adını ilk defa resmi devlet adı olarak kullanan devlettir. Kurucusu Bumin Kağan\'dır.', 9, 0),
    (52, 1, 1, 'spot', '3. I. ve II. Göktürk (Kutluk) Devleti', 'İlk Türk alfabesi olan 38 harfli Orhun Alfabesi\'ni hazırlamışlardır.', 10, 0),
    (52, 1, 1, 'spot', '3. I. ve II. Göktürk (Kutluk) Devleti', 'Türk tarihinin ve edebiyatının ilk yazılı kaynakları Orhun Abideleri (Bilge Kağan, Kül Tigin, Tonyukuk) Kutluk Devleti dönemindedir.', 11, 0),
    (52, 1, 2, 'spot', '4. Uygur Devleti', 'Maniheizm dinini kabul ederek yerleşik hayata geçen ilk Türk devletidir (Bögü Kağan dönemi).', 12, 0),
    (52, 1, 2, 'spot', '4. Uygur Devleti', 'Yerleşik hayat sonucu ilk Türk şehirleri (Balık), tapınak mimarisi, kütüphaneler ve matbaa gelişmiştir.', 13, 0),
    (52, 1, 2, 'spot', '4. Uygur Devleti', 'Hukuk kurallarını yazılı hale getiren ilk Türk devletidir.', 14, 0),
    (52, 1, 3, 'spot', '5. İlk Türk İslam Devletleri', 'Karahanlılar: Orta Asya\'da İslamiyet\'i kabul eden ilk Türk devletidir (Satuk Buğra Han). Resmi dilleri Türkçe\'dir.', 15, 0),
    (52, 1, 3, 'spot', '5. İlk Türk İslam Devletleri', 'Kutadgu Bilig (Yusuf Has Hacib) ve Divânu Lugâti\'t-Türk (Kaşgarlı Mahmud) Karahanlılar döneminde yazılmıştır.', 16, 0),
    (52, 1, 3, 'spot', '5. İlk Türk İslam Devletleri', 'Gazneli Mahmut, İslam dünyasında "Sultan" unvanını kullanan ilk Türk hükümdarıdır.', 17, 0),
    (52, 1, 3, 'spot', '5. İlk Türk İslam Devletleri', 'Büyük Selçuklular: Dandanakan Savaşı (1040) ile resmen kurulmuş, Malazgirt Savaşı (1071) ile Anadolu\'nun kapılarını Türklere açmıştır.', 18, 0),
    (52, 1, 4, 'spot', '6. Osmanlı Kuruluş & Yükselme', 'Osmanlı Devleti\'nde ilk kadı ataması (Dursun Fakih) ve ilk vergi (Bac) Osman Bey dönemindedir.', 19, 0),
    (52, 1, 4, 'spot', '6. Osmanlı Kuruluş & Yükselme', 'İlk düzenli ordu (Yaya ve Müsellem), ilk divan teşkilatı ve ilk medrese (İznik) Orhan Bey döneminde kurulmuştur.', 20, 0),
    (52, 1, 4, 'spot', '6. Osmanlı Kuruluş & Yükselme', 'Tımar sistemi, Kapıkulu Ocağı ve Yeniçeri Ocağı I. Murad döneminde kurulmuştur.', 21, 0),

    # --- COĞRAFYA: SPOT BİLGİLER (category_id = 2, note_type = 'spot') ---
    (52, 2, 8, 'spot', '1. Türkiye Coğrafi Konumu', 'Türkiye 36°-42° Kuzey paralelleri ile 26°-45° Doğu meridyenleri arasında yer alır.', 1, 0),
    (52, 2, 8, 'spot', '1. Türkiye Coğrafi Konumu', 'Türkiye\'nin en doğusu ile en batısı arasında 19 boylam ve 76 dakikalık yerel saat farkı vardır.', 2, 0),
    (52, 2, 8, 'spot', '1. Türkiye Coğrafi Konumu', 'Kuzey Yarım Küre\'de ve Orta Kuşak\'ta bulunması sebebiyle dört mevsim belirgin olarak yaşanır (Matematik Konum).', 3, 0),
    (52, 2, 8, 'spot', '1. Türkiye Coğrafi Konumu', 'Güneyden kuzeye gidildikçe güneş ışınlarının geliş açısı küçülür, sıcaklık azalır, gölge boyu uzar.', 4, 0),
    (52, 2, 9, 'spot', '2. Türkiye\'nin Yer Şekilleri', 'Türkiye genç oluşumlu (3. ve 4. jeolojik zaman) bir ülke olduğu için ortalama yükseltisi fazladır (1132 m) ve deprem riski yüksektir.', 5, 0),
    (52, 2, 9, 'spot', '2. Türkiye\'nin Yer Şekilleri', 'Karadeniz ve Akdeniz\'de dağlar denize paralel uzanırken, Ege\'de dik uzanır (Kıyı tipleri ve iklim etki alanı bu yüzden farklıdır).', 6, 0),
    (52, 2, 9, 'spot', '2. Türkiye\'nin Yer Şekilleri', 'Türkiye\'nin en yüksek volkanik dağı Büyük Ağrı Dağı\'dır (5137 m).', 7, 0),
    (52, 2, 10, 'spot', '3. Türkiye\'nin İklimi ve Bitki Örtüsü', 'Türkiye\'de yıllık sıcaklık farkının en az olduğu bölge Karadeniz, en fazla olduğu bölge Doğu Anadolu\'dur.', 8, 0),
    (52, 2, 10, 'spot', '3. Türkiye\'nin İklimi ve Bitki Örtüsü', 'Türkiye\'de en çok yağış alan yer Rize (Yamaç/Orografik yağış), en az yağış alan yer ise Iğdır ve Tuz Gölü çevresidir.', 9, 0),
    (52, 2, 10, 'spot', '3. Türkiye\'nin İklimi ve Bitki Örtüsü', 'İç Anadolu\'da ilkbaharda görülen konveksiyonel (yükselim) yağışlara halk arasında "Kırkikindi Yağışları" denir.', 10, 0),

    # --- VATANDAŞLIK: HAP NOTLAR (category_id = 3, note_type = 'spot') ---
    (52, 3, 13, 'spot', '1. Temel Hukuk Kavramları', 'Normlar Hiyerarşisi: Anayasa > Kanun = CBK (Olağanüstü) = Milletlerarası Antlaşma > CBK (Olağan) > Yönetmelik > Genelge.', 1, 0),
    (52, 3, 13, 'spot', '1. Temel Hukuk Kavramları', 'Hak ehliyeti: Tam ve sağ doğumla başlar (Pasif hak sahibi olabilme). Fiil ehliyeti: Ayırt etme gücü + Erginlik + Kısıtlı olmama.', 2, 0),
    (52, 3, 13, 'spot', '1. Temel Hukuk Kavramları', 'Normal erginlik yaşı 18\'dir. Evlenme ile erginlik olağan durumda 17, olağanüstü durumda mahkeme kararıyla 16\'dır.', 3, 0),
    (52, 3, 14, 'spot', '2. 1982 Anayasası Temel İlkeleri', 'Anayasa\'nın ilk 3 maddesi değiştirilemez ve değiştirilmesi teklif dahi edilemez (4. Madde güvencesi).', 4, 0),
    (52, 3, 14, 'spot', '2. 1982 Anayasası Temel İlkeleri', 'Devletin şekli Cumhuriyettir. Dili Türkçe, başkenti Ankara, milli marşı İstiklal Marşı, bayrağı al bayraktır.', 5, 0),
    (52, 3, 14, 'spot', '2. 1982 Anayasası Temel İlkeleri', 'Egemenlik kayıtsız şartsız milletindir. Türk milleti egemenliğini Anayasa\'nın koyduğu esaslara göre yetkili organlar eliyle kullanır.', 6, 0),
    (52, 3, 15, 'spot', '3. Yasama Organı (TBMM)', 'TBMM genel oyla seçilen 600 milletvekilinden oluşur. Milletvekili seçimleri 5 yılda bir CB seçimiyle birlikte yapılır.', 7, 0),
    (52, 3, 15, 'spot', '3. Yasama Organı (TBMM)', 'Milletvekili seçilme yaşı 18\'dir. En az ilkokul mezunu olmak zorunludur.', 8, 0),
    (52, 3, 15, 'spot', '3. Yasama Organı (TBMM)', 'TBMM toplantı yeter sayısı en az 200 (1/3), karar yeter sayısı ise toplantıya katılanların salt çoğunluğudur (en az 151).', 9, 0),
    (52, 3, 16, 'spot', '4. Yürütme ve Yargı', 'Yürütme yetkisi ve görevi Cumhurbaşkanı\'na aittir. Cumhurbaşkanı 5 yıl için seçilir, bir kişi en fazla iki kez seçilebilir.', 10, 0),
    (52, 3, 16, 'spot', '4. Yürütme ve Yargı', 'Anayasa Mahkemesi 15 üyeden oluşur (3\'ü TBMM, 12\'si Cumhurbaşkanı tarafından seçilir). Üyelerin görev süresi 12 yıldır.', 11, 0),

    # --- MATEMATİK: FORMÜLLER & KURALLAR (category_id = 5, note_type = 'formula') ---
    (52, 5, 87, 'formula', '1. Sayı Kümeleri & Tanımlar', 'Doğal Sayılar: N = {0, 1, 2, 3, 4, ...}\nSayma Sayıları: N+ = {1, 2, 3, 4, ...}\nEn küçük doğal sayı 0\'dır.', 1, 0),
    (52, 5, 87, 'formula', '1. Sayı Kümeleri & Tanımlar', 'Tam Sayılar: Z = {..., -2, -1, 0, 1, 2, ...}\nPozitif Tam Sayılar: Z+ = {1, 2, ...}\n0 sayısı nötrdür (işareti yoktur).', 2, 0),
    (52, 5, 87, 'formula', '1. Sayı Kümeleri & Tanımlar', 'Rasyonel Sayılar: Q = {a / b | a, b ∈ Z ve b ≠ 0}\nİrrasyonel Sayılar (Q\'): Virgülden sonrası devretmeyen köklü sayılar (√2, √3, π, e).', 3, 0),
    (52, 5, 87, 'formula', '1. Sayı Kümeleri & Tanımlar', 'Asal Sayılar: 1 ve kendisinden başka böleni olmayan 1\'den büyük doğal sayılar: {2, 3, 5, 7, 11, 13, ...}\nEn küçük asal sayı 2\'dir ve 2 haricinde çift asal sayı yoktur.', 4, 0),
    (52, 5, 87, 'formula', '2. Ardışık Sayı Formülleri', 'Terim Sayısı = [(Son Terim - İlk Terim) / Artış Miktarı] + 1', 5, 0),
    (52, 5, 87, 'formula', '2. Ardışık Sayı Formülleri', 'Terimler Toplamı = [(Son Terim + İlk Terim) / 2] × Terim Sayısı', 6, 0),
    (52, 5, 87, 'formula', '2. Ardışık Sayı Formülleri', '1\'den n\'ye kadar ardışık sayıların toplamı:\n1 + 2 + 3 + ... + n = [n × (n + 1)] / 2', 7, 0),
    (52, 5, 87, 'formula', '2. Ardışık Sayı Formülleri', '2\'den 2n\'ye kadar ardışık çift sayıların toplamı:\n2 + 4 + 6 + ... + 2n = n × (n + 1)', 8, 0),
    (52, 5, 87, 'formula', '2. Ardışık Sayı Formülleri', '1\'den 2n-1\'e kadar ardışık tek sayıların toplamı:\n1 + 3 + 5 + ... + (2n - 1) = n²', 9, 0),
    (52, 5, 88, 'formula', '3. Bölünebilme Kuralları', '2 ile Bölünebilme: Birler basamağı çift (0, 2, 4, 6, 8) olan sayılar.\n3 ile Bölünebilme: Rakamları toplamı 3 veya 3\'ün katı olan sayılar.', 10, 0),
    (52, 5, 88, 'formula', '3. Bölünebilme Kuralları', '4 ile Bölünebilme: Son iki basamağı 00 veya 4\'ün katı olan sayılar.\n5 ile Bölünebilme: Son basamağı 0 veya 5 olan sayılar.', 11, 0),
    (52, 5, 88, 'formula', '3. Bölünebilme Kuralları', '8 ile Bölünebilme: Son üç basamağı 000 veya 8\'in katı olan sayılar.\n9 ile Bölünebilme: Rakamları toplamı 9 veya 9\'un katı olan sayılar.', 12, 0),
    (52, 5, 88, 'formula', '3. Bölünebilme Kuralları', '11 ile Bölünebilme: Sağdan sola +, -, +, - işaretlenir. Pozitiflerin toplamından negatiflerin toplamı çıkarıldığında sonuç 0 veya 11\'in katı olmalıdır.', 13, 0),
    (52, 5, 91, 'formula', '4. Problem Bağıntıları', 'Hız Problemleri:\nYol = Hız × Zaman (X = V × t)\nZıt Yönlü Hareket: Karşılaşma Zamanı = Yol / (V1 + V2)\nAynı Yönlü Hareket: Yakalama Zamanı = Yol / (V1 - V2)', 14, 0),
    (52, 5, 91, 'formula', '4. Problem Bağıntıları', 'İşçi Problemleri:\n1. işçi tek başına a günde, 2. işçi b günde bitirirse birlikte t günde:\n(1/a + 1/b) × t = 1', 15, 0),
    (52, 5, 91, 'formula', '4. Problem Bağıntıları', 'Kar - Zarar Problemleri:\nSatış Fiyatı = Maliyet + Kar\nKar Oranı = (Kar / Maliyet) × 100\nZarar Oranı = (Zarar / Maliyet) × 100', 16, 0),

    # --- KONU ÖZETLERİ (note_type = 'summary') ---
    (52, 1, 1, 'summary', 'İslamiyet Öncesi Türk Tarihi', '• Türklerin ana yurdu Orta Asya\'dır; bozkır iklimi konargöçer yaşam tarzını zorunlu kılmıştır.\n• Boylar federasyonu şeklinde teşkilatlanmışlardır; boyların başında "Bey"ler bulunur.\n• Ordu teşkilatında Mete Han\'ın kurduğu Onluk Sistem temel alınmıştır.\n• Sosyal yapıda sınıflaşma ve kölelik yoktur; töre (sözlü hukuk) herkesi bağlar.\n• İnanç sisteminde Gök Tengri, Atalar Kültü ve Tabiat Kuvvetleri inancı vardır; kurganlara ölüler eşyalarıyla gömülür (ahiret inancı).', 1, 0),
    (52, 1, 2, 'summary', 'Uygurlar ve Kültürel Dönüşüm', '• Kutluk Bilge Kül Kağan tarafından Ötüken merkezli kurulmuş, sonradan Karabalgasun başkent yapılmıştır.\n• Bögü Kağan döneminde kabul edilen Maniheizm dini, et yemeyi ve savaşmayı yasakladığı için Uygurların savaşçılık özelliğini zayıflatmış ancak yerleşik kültürü ve sanatı zirveye taşımıştır.\n• İlk Türk şehir mimarisi, fresk (duvar resmi) sanatı, tiyatro (orta oyunu) ve minyatür Uygurlarla başlar.', 2, 0),
    (52, 2, 8, 'summary', 'Türkiye\'nin Konumu ve Sonuçları', '• Matematik Konum: 36-42 K paralelleri, 26-45 D meridyenleri. Kuzey Yarımküre\'de, 2. ve 3. saat dilimlerinde yer alır (Kalıcı olarak GMT+3 Iğdır saati kullanılır).\n• Dört mevsimin belirgin yaşanması ve Akdeniz iklim kuşağında olması matematik konumun, aynı anda farklı iklim özelliklerinin yaşanması ise özel konumun (yer şekilleri) sonucudur.\n• Jeopolitik Konum: Boğazlara sahip olması, Asya ile Avrupa arasında enerji köprüsü olması ve üç tarafının denizlerle çevrili olması stratejik önemini artırır.', 3, 0),
    (52, 3, 14, 'summary', '1982 Anayasası Genel Esaslar', '• 1982 Anayasası kazuistik (ayrıntılı) ve katı/sert bir anayasadır.\n• Madde 1: Türkiye Devleti bir Cumhuriyettir.\n• Madde 2: Cumhuriyetin nitelikleri: Demokratik, laik, sosyal ve hukuk devleti; Atatürk milliyetçiliğine bağlılık; insan haklarına saygılı.\n• Madde 3: Devletin bütünlüğü, resmi dili Türkçe, bayrağı, milli marşı ve başkenti Ankara\'dır.\n• Madde 4: İlk üç madde değiştirilemez ve değiştirilmesi teklif edilemez.', 4, 0),

    # --- BİLGİ KARTLARI / KARTI ÇEVİR (note_type = 'flashcard') ---
    (52, 4, 18, 'flashcard', '\'Damlaya damlaya göl olur.\' atasözünde hangi söz sanatı vardır?', 'Tekrir (Tekrar Etme) Sanatı.\n\nAçıklama: Aynı kelimenin etkiyi güçlendirmek amacıyla art arda yinelenmesidir. "Damlaya damlaya" ifadesinde kelime tekrar edilerek ahenk sağlanmıştır.', 1, 0),
    (52, 4, 18, 'flashcard', 'Kelimelerin hem gerçek hem mecaz anlama gelecek şekilde kullanılıp asıl mecaz anlamın kastedilmesine ne ad verilir?', 'Kinaye (Değinmece).\n\nAçıklama: Örneğin "Ateş düştüğü yeri yakar" sözünde hem gerçek anlam hem de asıl amaç olan mecaz acı kastı bulunur.', 2, 0),
    (52, 4, 18, 'flashcard', 'Bir sözcüğü benzetme amacı gütmeden başka bir sözcük yerine kullanma sanatına ne ad verilir?', 'Mecazımürsel (Ad Aktarması).\n\nAçıklama: Örneğin "Ankara bu karara tepki gösterdi" (Hükümet kastediliyor) veya "Sobayı yak" (İçindeki odun kastediliyor).', 3, 0),
    (52, 1, 1, 'flashcard', 'Türk tarihinde ilk kez düzenli orduyu kuran ve Onluk Sistemi getiren hükümdar kimdir?', 'Mete Han (Asya Hun Devleti).\n\nAçıklama: MÖ 209 yılında tahta çıkan Mete Han, Türk Kara Kuvvetleri\'nin de kuruluş tarihi kabul edilen Onluk Sistemi geliştirmiştir.', 4, 0),
    (52, 1, 1, 'flashcard', 'Maniheizm dinini kabul ederek Türk tarihinde ilk kez yerleşik hayata geçen devlet hangisidir?', 'Uygurlar (Bögü Kağan Dönemi).\n\nAçıklama: Yerleşik hayatla birlikte tarım, kütüphaneler, mimari yapılar ve matbaa kullanımı ilk defa Uygurlarda görülmüştür.', 5, 0),
    (52, 1, 3, 'flashcard', 'Türk-İslam tarihinde ilk siyasetname niteliği taşıyan ve Yusuf Has Hacib tarafından yazılan eser hangisidir?', 'Kutadgu Bilig (Mutluluk Veren Bilgi).\n\nAçıklama: Karahanlılar döneminde Uygur alfabesi ve Hakaniye Türkçesi ile yazılarak Karahanlı hükümdarı Tabgaç Buğra Han\'a sunulmuştur.', 6, 0),
    (52, 1, 3, 'flashcard', 'İslam dünyasında "Sultan" unvanını kullanan ilk Türk hükümdarı kimdir?', 'Gazneli Mahmut.\n\nAçıklama: Abbasi Halifesi\'ni Şii Büveyhoğulları baskısından kurtardığı için halife tarafından kendisine "Sultan" unvanı verilmiştir.', 7, 0),
    (52, 1, 4, 'flashcard', 'Osmanlı Devleti\'nde Yeniçeri Ocağı ve Tımar Sistemi hangi padişah döneminde kurulmuştur?', 'I. Murad (Hüdavendigar).\n\nAçıklama: Rumeli Beylerbeyliği, Kazaskerlik ve Defterdarlık makamları da I. Murad devrinde kurumsallaşmıştır.', 8, 0),
    (52, 2, 8, 'flashcard', 'Türkiye\'nin aynı anda dört mevsim özelliklerinin yaşanabilmesi matematik konumla mı özel konumla mı ilgilidir?', 'Özel Konum (Göreceli Konum).\n\nAçıklama: Aynı anda bir yerde kayak yapılırken diğer yerde denize girilmesi kısa mesafede değişen yer şekilleri ve yükselti farkından (özel konum) kaynaklanır.', 9, 0),
    (52, 2, 9, 'flashcard', 'Türkiye\'nin en büyük tektonik gölü ve en büyük tatlı su gölü hangileridir?', 'En büyük tektonik göl: Tuz Gölü.\nEn büyük tatlı su gölü: Beyşehir Gölü.\n\nNot: Van Gölü ise Türkiye\'nin en büyük gölü olup volkanik set gölüdür (sodalıdır).', 10, 0),
    (52, 3, 13, 'flashcard', 'Normlar Hiyerarşisi\'nde en üstte yer alan ve hiçbir kanunun aykırı olamayacağı metin hangisidir?', 'Anayasa.\n\nAçıklama: Hiyerarşi sırası: Anayasa > Kanun / CBK (OHAL) / Milletlerarası Andlaşma > CBK (Olağan) > Yönetmelik > Genelge.', 11, 0),
    (52, 3, 15, 'flashcard', '1982 Anayasası\'na göre TBMM üye tamsayısı ve milletvekili seçilme yaşı kaçtır?', 'Üye Tamsayısı: 600 Milletvekili.\nSeçilme Yaşı: 18 yaşını doldurmuş olmak.\n\nAçıklama: 2017 Anayasa değişikliği ile milletvekili sayısı 550\'den 600\'e çıkarılmış, seçilme yaşı 25\'ten 18\'e indirilmiştir.', 12, 0),
]

sql_statements = []
for n in notes:
    lang_id, cat_id, sub_id, ntype, title, content, order, is_prem = n
    esc_title = title.replace("'", "''")
    esc_content = content.replace("'", "''")
    sql_statements.append(f"({lang_id}, {cat_id}, {sub_id}, '{ntype}', '{esc_title}', '{esc_content}', {order}, {is_prem}, 1)")

values_sql = ",\n".join(sql_statements)
full_sql = f"INSERT INTO tbl_study_notes (language_id, category_id, subcategory_id, note_type, topic_title, content, note_order, is_premium, status) VALUES \n{values_sql};"

with open(r"d:\quiza\scratch_osym\seed_study.sql", "w", encoding="utf-8") as f:
    f.write(full_sql)

print(f"Generated {len(notes)} study notes SQL.")
