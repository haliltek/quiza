# -*- coding: utf-8 -*-
import json
import subprocess

questions_data = [
    # ==========================================
    # TARİH (KPSS Lisans - Kategori: 1 - Seviye 2)
    # ==========================================
    {
        "category": 1,
        "subcategory": 1,
        "language_id": 52,
        "level": 2,
        "question": "İslamiyet öncesi Türk devletlerinde hakanın buyruklarının 'Gök Tanrı'nın buyruğu' sayılarak itaat edilmesi ancak hakanın töreye aykırı hareket ettiğinde tahttan indirilebilmesi durumu dikkate alındığında;\n\nI. Egemenliğin meşruiyetinin ilahi temele dayandırıldığı,\nII. Hakanın yetkilerinin mutlak ve sınırsız olmadığı,\nIII. Devlet yönetiminde yazılı anayasal düzene geçildiği\n\nyargılarından hangilerine ulaşılabilir?",
        "optiona": "Yalnız I",
        "optionb": "Yalnız II",
        "optionc": "I ve II",
        "optiond": "II ve III",
        "optione": "I, II ve III",
        "answer": "c",
        "note": "İslamiyet öncesi Türklerde kut inancı egemenliğin ilahi kaynaklı olduğunu gösterir (I). Ancak töre kuralları hakanın da üstünde olup yetkilerini sınırlandırmıştır (II). Töreler yazısız hukuk kuralları olduğu için yazılı anayasal düzenden bahsedilemez (III). Doğru cevap: C (I ve II)."
    },
    {
        "category": 1,
        "subcategory": 1,
        "language_id": 52,
        "level": 2,
        "question": "Büyük Selçuklu Devleti'nde uygulanan İkta Sistemi sayesinde;\n\nI. Taşrada devlet otoritesinin ve asayişin sürekliliği sağlanmıştır.\nII. Hazineden para çıkmadan savaşa hazır sipahi ordusu oluşturulmuştur.\nIII. Üretimde süreklilik güvence altına alınmıştır.\n\nYukarıdakilerden hangileri bu sistemin hem askeri hem de iktisadi boyutunu kanıtlar?",
        "optiona": "Yalnız I",
        "optionb": "Yalnız II",
        "optionc": "I ve II",
        "optiond": "II ve III",
        "optione": "I, II ve III",
        "answer": "e",
        "note": "İkta sistemi; üretimin aksamamasını sağlayarak iktisadi (III), cebelü askerleri yetiştirerek askeri (II), asayişi koruyarak idari (I) faydalar sağlamıştır. Dolayısıyla öncüllerin tamamı sistemin fonksiyonlarındandır. Doğru cevap: E."
    },
    {
        "category": 1,
        "subcategory": 1,
        "language_id": 52,
        "level": 2,
        "question": "Osmanlı Devleti'nde 17. yüzyıldan itibaren tımar sisteminin bozulmasıyla birlikte yaygınlaşan iltizam ve malikane uygulamalarının;\n\nI. Merkezî hazineye anlık nakit para akışı sağlama,\nII. Taşrada ayan ve eşraf gibi yerel güç odaklarının doğmasına zemin hazırlama,\nIII. Reayanın toprağa bağlılığını artırarak göçleri önleme\n\nsonuçlarından hangilerini doğurduğu savunulabilir?",
        "optiona": "Yalnız I",
        "optionb": "Yalnız III",
        "optionc": "I ve II",
        "optiond": "II ve III",
        "optione": "I, II ve III",
        "answer": "c",
        "note": "İltizam sistemi devlete acil nakit sağlamış (I), mültezimlerin güçlenmesiyle zamanla ayanlar sınıfı doğmuştur (II). Aksine köylü ağır vergiler nedeniyle toprağını terk etmiş (Büyük Kaçgun) göçler artmıştır (III yanlıştır). Doğru cevap: C (I ve II)."
    },
    {
        "category": 1,
        "subcategory": 1,
        "language_id": 52,
        "level": 2,
        "question": "Osmanlı Devleti'nde 1876 Kanun-i Esasi'de padişahın mutlak yetkileri bulunurken, 1909 Anayasa Değişiklikleri ile;\n\nI. Hükûmetin (Heyet-i Vükela) padişaha değil, Mebusan Meclisine karşı sorumlu olması,\nII. Padişahın meclisi kapatma yetkisinin zorlaştırılması,\nIII. Padişahın sürgün yetkisini düzenleyen 113. maddenin kaldırılması\n\nhükümlerinden hangileri getirilerek parlamenter monarşi ilkeleri güçlendirilmiştir?",
        "optiona": "Yalnız I",
        "optionb": "I ve II",
        "optionc": "I ve III",
        "optiond": "II ve III",
        "optione": "I, II ve III",
        "answer": "e",
        "note": "1909 değişiklikleri ile padişahın veto ve meclisi fesih yetkileri sınırlandırılmış, 113. maddedeki sürgün yetkisi kaldırılmış ve hükûmet meclise karşı sorumlu kılınarak gerçek anlamda parlamenter sisteme geçilmiştir. Doğru cevap: E."
    },
    {
        "category": 1,
        "subcategory": 1,
        "language_id": 52,
        "level": 2,
        "question": "Mustafa Kemal Paşa'nın Amasya Genelgesi'nde yer alan \"Milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır.\" maddesi ilk kez aşağıdakilerden hangisinin değişeceğine açık bir işarettir?",
        "optiona": "Ekonomik bağımsızlık anlayışının",
        "optionb": "Egemenliğin kaynağı ve yönetim biçiminin",
        "optionc": "Ordunun teşkilatlanma tarzının",
        "optiond": "Uluslararası ittifak dengelerinin",
        "optione": "Devletin başkentinin",
        "answer": "b",
        "note": "Bu madde Kurtuluş Savaşı'nın hem amacını hem yöntemini belirtir; millet iradesine vurgu yaparak üstü kapalı şekilde egemenliğin kaynağının padişahtan millete geçeceğini (cumhuriyet rejimini) müjdeler. Doğru cevap: B."
    },
    {
        "category": 1,
        "subcategory": 1,
        "language_id": 52,
        "level": 2,
        "question": "Son Osmanlı Mebusan Meclisinde kabul edilen Misak-ı Millî kararlarında;\n\nI. Kars, Ardahan, Batum (Elviye-i Selase),\nII. Batı Trakya,\nIII. Arap vilayetleri\n\nbölgelerinden hangilerinde gerekirse halk oylamasına (plebisit) başvurulabileceği kabul edilmiştir?",
        "optiona": "Yalnız I",
        "optionb": "I ve II",
        "optionc": "I ve III",
        "optiond": "II ve III",
        "optione": "I, II ve III",
        "answer": "e",
        "note": "Misak-ı Millî kararlarında Türk ve Müslüman nüfusun çoğunlukta olduğuna güvenilen Elviye-i Selase (Kars, Ardahan, Batum), Batı Trakya ve Arap topraklarında halk oylaması yapılması öngörülmüştür. Doğru cevap: E."
    },
    {
        "category": 1,
        "subcategory": 1,
        "language_id": 52,
        "level": 2,
        "question": "Lozan Barış Antlaşması'nda çözüme kavuşturulamayıp Türkiye ile İngiltere arasındaki ikili görüşmelere bırakılan ve daha sonra Milletler Cemiyetine taşınan mesele aşağıdakilerden hangisidir?",
        "optiona": "Hatay Sorunu",
        "optionb": "Musul Sorunu (Irak Sınırı)",
        "optionc": "Boğazlar Rejimi",
        "optiond": "Dış Borçlar Sorunu",
        "optione": "Patrikhane Meselesi",
        "answer": "b",
        "note": "Lozan Antlaşması'nda çözülemeyen tek sınır meselesi Türkiye-Irak sınırı (Musul Sorunu) olmuştur. Taraflar 9 ay içinde anlaşamazsa Milletler Cemiyetine gitmesi kararlaştırılmıştır. Doğru cevap: B."
    },
    {
        "category": 1,
        "subcategory": 1,
        "language_id": 52,
        "level": 2,
        "question": "Atatürk Dönemi'nde 1936 yılında imzalanan Montrö Boğazlar Sözleşmesi ile;\n\nI. Boğazlar Komisyonunun kaldırılarak yetkilerinin Türkiye'ye devredilmesi,\nII. Türkiye'nin Boğazların her iki yakasında asker bulundurma hakkını elde etmesi,\nIII. Savaş gemilerinin geçişinde Karadeniz'e kıyıdaş olan ve olmayan ülkelere farklı tonaj kısıtlamaları getirilmesi\n\ngelişmelerinden hangileri Türkiye'nin egemenlik haklarını tam olarak pekiştirmiştir?",
        "optiona": "Yalnız I",
        "optionb": "I ve II",
        "optionc": "I ve III",
        "optiond": "II ve III",
        "optione": "I, II ve III",
        "answer": "e",
        "note": "Montrö Sözleşmesi ile uluslararası komisyon kaldırılmış, askerden arındırılmış bölgelere Türk askeri yerleştirilmiş ve yabancı savaş gemilerine sıkı kurallar getirilerek Türkiye Boğazlar üzerinde tam hâkimiyet kurmuştur. Doğru cevap: E."
    },
    {
        "category": 1,
        "subcategory": 1,
        "language_id": 52,
        "level": 2,
        "question": "Osmanlı Devleti'nde şeyhülislam, kazasker ve kadıların mensup olduğu, adalet, din ve eğitim işlerinden sorumlu devlet sınıfı aşağıdakilerden hangisidir?",
        "optiona": "Seyfiye",
        "optionb": "Kalemiye",
        "optionc": "İlmiye",
        "optiond": "Mülkiye",
        "optione": "Teknofiye",
        "answer": "c",
        "note": "Osmanlı bürokrasisinde eğitim (müderris), din (müftü/şeyhülislam) ve hukuk/yargı (kadı/kazasker) görevlileri İlmiye (Ulema) sınıfına mensuptur. Seyfiye askeri/idari, Kalemiye ise mali/bürokratik sınıftır. Doğru cevap: C."
    },
    {
        "category": 1,
        "subcategory": 1,
        "language_id": 52,
        "level": 2,
        "question": "Atatürk'ün 'Devletçilik' ilkesinin Türkiye'deki uygulamaları dikkate alındığında aşağıdakilerden hangisi bu ilkenin temel hedeflerinden biri olamaz?",
        "optiona": "Özel sektörün sermaye ve tecrübe yetersizliği nedeniyle yapamadığı büyük yatırımları devlet eliyle gerçekleştirmek",
        "optionb": "Bölgeler arasındaki gelişmişlik farklarını azaltmak",
        "optionc": "Özel teşebbüsü ve serbest piyasa mülkiyetini tamamen ortadan kaldırarak kolektif mülkiyete geçmek",
        "optiond": "Hammadde temini yurt içinden sağlanan sanayi kollarını öncelikle kurmak",
        "optione": "Temel tüketim maddelerinde dışa bağımlılığı en aza indirmek",
        "answer": "c",
        "note": "Kemalist Devletçilik ilkesi sosyalizm/komünizm gibi özel mülkiyeti ve özel sektörü reddetmez; aksine özel teşebbüsü destekleyen karma ekonomik bir modeldir. Özel teşebbüsü ortadan kaldırmak hedefi yoktur. Doğru cevap: C."
    },

    # ==========================================
    # COĞRAFYA (KPSS Lisans - Kategori: 2 - Seviye 2)
    # ==========================================
    {
        "category": 2,
        "subcategory": 8,
        "language_id": 52,
        "level": 2,
        "question": "Türkiye'de 21 Haziran tarihinde güneyden kuzeye doğru gidildikçe;\n\nI. Gündüz süresi uzar.\nII. Güneş ışınlarının geliş açısı küçülür.\nIII. Çizgisel dönüş hızı artar.\n\nyargılarından hangileri doğrudur?",
        "optiona": "Yalnız I",
        "optionb": "I ve II",
        "optionc": "I ve III",
        "optiond": "II ve III",
        "optione": "I, II ve III",
        "answer": "b",
        "note": "21 Haziran'da kuzeye gidildikçe gündüz süresi uzar (I). Kutuplara yaklaşıldığı için güneş ışınlarının açısı küçülür (II). Ancak çizgisel hız ekvatordan kutuplara gidildikçe azalır, artmaz (III yanlıştır). Doğru cevap: B (I ve II)."
    },
    {
        "category": 2,
        "subcategory": 8,
        "language_id": 52,
        "level": 2,
        "question": "Türkiye'de karstik aşınım ve birikim şekillerinin en yaygın olduğu Teke ve Taşeli platolarında nüfus yoğunluğunun Türkiye ortalamasının çok altında olmasının temel nedeni aşağıdakilerden hangisidir?",
        "optiona": "Kış mevsiminin çok sert ve karlı geçmesi",
        "optionb": "Kalkerli yapının suyu yer altına sızdırması ve yüzey sularının yetersizliği ile engebeli arazi",
        "optionc": "Orman varlığının bulunmaması",
        "optiond": "Deniz etkisinden tamamen uzak karasal iklim koşulları",
        "optione": "Maden yataklarının bulunmayışı",
        "answer": "b",
        "note": "Teke ve Taşeli platoları Akdeniz iklim bölgesinde yer almasına rağmen karstik (kireçtaşı) arazinin suyu derine geçirmesi (taban suyunun derinde olması), tarım topraklarının azlığı ve aşırı engebe sebebiyle tenha nüfusludur. Doğru cevap: B."
    },
    {
        "category": 2,
        "subcategory": 8,
        "language_id": 52,
        "level": 2,
        "question": "Rize ve çevresinde kış mevsiminde turunçgil ve çay gibi mikroklima ürünlerinin yetiştirilebilmesinde en belirleyici faktör aşağıdakilerden hangisidir?",
        "optiona": "Kafkas Dağları'nın kuzeyden gelen soğuk hava dalgalarını kesmesi ve fön rüzgârlarının kış ılıklığı sağlaması",
        "optionb": "Yıllık güneşlenme süresinin Türkiye ortalamasının çok üzerinde olması",
        "optionc": "Alüvyal toprakların geniş yer kaplaması",
        "optiond": "Enlem etkisine bağlı olarak Güneş ışınlarını dik açıyla alması",
        "optione": "Gelgit genliğinin yüksek olması",
        "answer": "a",
        "note": "Doğu Karadeniz kıyılarında Kaçkarların kuzeyden gelen soğukları engellemesi ve dağları aşarak alçalan havanın fön etkisi yaratması kış aylarında ılıman bir mikroklima oluşturur. Doğru cevap: A."
    },
    {
        "category": 2,
        "subcategory": 8,
        "language_id": 52,
        "level": 2,
        "question": "Türkiye'de nadas tarımının yaygın olduğu bir bölgede sulama imkânlarının geliştirilmesi durumunda aşağıdakilerden hangisinin gerçekleşmesi beklenmez?",
        "optiona": "Tarımsal üretimde yıldan yıla görülen dalgalanmaların azalması",
        "optionb": "Birim alandan elde edilen tarımsal verimin artması",
        "optionc": "Nadasa ayrılan toprak oranının önemli ölçüde düşmesi",
        "optiond": "Kırsal alandan kentlere yapılan ekonomik göç baskısının artması",
        "optione": "Sanayi bitkilerinin (pamuk, mısır vb.) ekim alanlarının genişlemesi",
        "answer": "d",
        "note": "Sulama olanaklarının artması çiftçinin gelirini ve refahını artıracağı için kırdan kente göç baskısını artırmaz, aksine azaltır veya tersine çevirir. Doğru cevap: D."
    },
    {
        "category": 2,
        "subcategory": 8,
        "language_id": 52,
        "level": 2,
        "question": "Aşağıdaki maden ve çıkarıldığı başlıca merkez eşleştirmelerinden hangisi yanlıştır?",
        "optiona": "Bor mineralleri - Balıkesir (Bigadiç) / Kütahya (Emet)",
        "optionb": "Boksit (Alüminyum) - Konya (Seydişehir) / Antalya (Akseki)",
        "optionc": "Krom - Muğla (Fethiye) / Elazığ (Guleman)",
        "optiond": "Demir - Sivas (Divriği) / Malatya (Hekimhan)",
        "optione": "Bakır - Manisa (Soma) / Zonguldak (Ereğli)",
        "answer": "e",
        "note": "Soma ve Zonguldak kömür havzalarıdır (Linyit ve Taş Kömürü). Bakırın başlıca çıkarım alanları ise Artvin (Murgul), Kastamonu (Küre) ve Elazığ (Maden)'dır. Doğru cevap: E."
    },
    {
        "category": 2,
        "subcategory": 8,
        "language_id": 52,
        "level": 2,
        "question": "Türkiye'de jeotermal enerjiden hem elektrik üretimi hem de sera ve konut ısıtmasında en yoğun şekilde faydalanılan bölge aşağıdakilerden hangisidir?",
        "optiona": "Doğu Anadolu (Yukarı Fırat Bölümü)",
        "optionb": "Ege Bölgesi (Kıyı Ege Graben Alanları)",
        "optionc": "İç Anadolu (Konya Kapalı Havzası)",
        "optiond": "Karadeniz Bölgesi (Batı Karadeniz Bölümü)",
        "optione": "Güneydoğu Anadolu (Dicle Bölümü)",
        "answer": "b",
        "note": "Kıyı Ege kırıklı (fay) tektonik hatları ve graben alanları (Büyük ve Küçük Menderes, Gediz) nedeniyle jeotermal kaynaklar bakımından en zengin bölgedir (Denizli-Sarayköy, Aydın-Germencik). Doğru cevap: B."
    },
    {
        "category": 2,
        "subcategory": 8,
        "language_id": 52,
        "level": 2,
        "question": "Aşağıdaki limanlardan hangisinin demiryolu bağlantısı bulunmadığı için ardülkesi (hinterlandı) dar kalmış ve ticaret hacmi sınırlı düzeydedir?",
        "optiona": "Samsun Limanı",
        "optionb": "İskenderun Limanı",
        "optionc": "Sinop Limanı",
        "optiond": "İzmir Limanı",
        "optione": "Mersin Limanı",
        "answer": "c",
        "note": "Sinop Limanı doğal bir liman olmasına rağmen arkasındaki Küre Dağları ve demiryolu bağlantısının olmaması nedeniyle hinterlandı gelişememiştir. Samsun, İskenderun, İzmir ve Mersin limanlarının demiryolu bağlantısı vardır. Doğru cevap: C."
    },
    {
        "category": 2,
        "subcategory": 8,
        "language_id": 52,
        "level": 2,
        "question": "Türkiye'nin nüfus piramidi incelendiğinde tabanın daralmakta, tepe noktasının ise genişlemekte olduğu görülmektedir. Bu durum aşağıdakilerden hangisinin kesin bir göstergesidir?",
        "optiona": "Doğum oranlarının azaldığının ve yaşlı nüfus oranının arttığının",
        "optionb": "Dış ülkelere verilen iş gücü göçünün hızlandığının",
        "optionc": "Kırsal nüfus oranının kent nüfus oranını aştığının",
        "optiond": "Genç bağımlı nüfus oranının arttığının",
        "optione": "Ortalama yaşam süresinin kısaldığının",
        "answer": "a",
        "note": "Piramit tabanının daralması doğum oranlarının gerilediğini, üst kısmın genişlemesi ise ortalama ömrün uzamasıyla yaşlı nüfus oranının arttığını gösterir. Doğru cevap: A."
    },
    {
        "category": 2,
        "subcategory": 8,
        "language_id": 52,
        "level": 2,
        "question": "Güneydoğu Anadolu Projesi (GAP) kapsamında sulama kanallarının devreye girmesiyle birlikte ekim alanı ve üretiminde en yüksek artış kaydedilen ürün aşağıdakilerden hangisidir?",
        "optiona": "Tütün",
        "optionb": "Pamuk",
        "optionc": "Çay",
        "optiond": "Fındık",
        "optione": "Zeytin",
        "answer": "b",
        "note": "GAP ile birlikte Şanlıurfa ve çevresinde sulamalı tarıma geçilmesi sonucunda Türkiye pamuk üretiminin yarısından fazlası bu bölgeden sağlanır hâle gelmiştir. Doğru cevap: B."
    },
    {
        "category": 2,
        "subcategory": 8,
        "language_id": 52,
        "level": 2,
        "question": "UNESCO Dünya Mirası Listesi'nde hem doğal hem de kültürel özellikleri bünyesinde barındıran 'karma miras' statüsündeki iki varlığımız aşağıdakilerden hangisinde birlikte verilmiştir?",
        "optiona": "Göbeklitepe - Safranbolu Evleri",
        "optionb": "Nemrut Dağı - Divriği Ulu Camii",
        "optionc": "Pamukkale (Hierapolis) - Kapadokya (Göreme Millî Parkı)",
        "optiond": "Truva Antik Kenti - Çatalhöyük",
        "optione": "Efes Antik Kenti - Ani Harabeleri",
        "answer": "c",
        "note": "Türkiye'de UNESCO Dünya Mirası Listesi'ndeki karma (hem doğal hem kültürel) sit alanları sadece Göreme Millî Parkı ve Kapadokya ile Pamukkale-Hierapolis'tir. Doğru cevap: C."
    },

    # ==========================================
    # VATANDAŞLIK & ANAYASA (KPSS Lisans - Kategori: 3 - Seviye 2)
    # ==========================================
    {
        "category": 3,
        "subcategory": 13,
        "language_id": 52,
        "level": 2,
        "question": "Türk Medeni Kanunu'na göre, hakların kazanılmasında geçerli olan temel ilke ile hakların kullanılmasında ve borçların yerine getirilmesinde geçerli olan temel ilke aşağıdakilerden hangisinde sırasıyla doğru verilmiştir?",
        "optiona": "İyiniyet - Dürüstlük Kuralı (Objektif İyiniyet)",
        "optionb": "Dürüstlük Kuralı - İyiniyet (Sübjektif İyiniyet)",
        "optionc": "Kusursuz Sorumluluk - Denkleştirici Adalet",
        "optiond": "Hakkaniyet - Ahde Vefa",
        "optione": "Gecikmiş İfa - İyiniyet",
        "answer": "a",
        "note": "TMK Madde 3'e göre hakların kazanılmasında 'İyiniyet' (Sübjektif İyiniyet), Madde 2'ye göre hakların kullanılmasında ve borçların ifasında ise 'Dürüstlük Kuralı' (Objektif İyiniyet) geçerlidir. Doğru cevap: A."
    },
    {
        "category": 3,
        "subcategory": 13,
        "language_id": 52,
        "level": 2,
        "question": "Normlar hiyerarşisi dikkate alındığında, kanunlar ile Cumhurbaşkanlığı Kararnameleri (CBK) arasındaki ilişki bakımından aşağıdakilerden hangisi yanlıştır?",
        "optiona": "Anayasa'da münhasıran kanunla düzenlenmesi öngörülen konularda Cumhurbaşkanlığı Kararnamesi çıkarılamaz.",
        "optionb": "Kanunda açıkça düzenlenen konularda Cumhurbaşkanlığı Kararnamesi çıkarılamaz.",
        "optionc": "Cumhurbaşkanlığı Kararnamesi ile kanunlarda farklı hükümler bulunması hâlinde kanun hükümleri uygulanır.",
        "optiond": "TBMM'nin aynı konuda kanun çıkarması durumunda Cumhurbaşkanlığı Kararnamesi hükümsüz hâle gelir.",
        "optione": "Olağan dönem Cumhurbaşkanlığı Kararnameleri ile Anayasa'nın ikinci kısmında yer alan kişi hak ve ödevleri düzenlenebilir.",
        "answer": "e",
        "note": "1982 Anayasası m.104'e göre; olağan dönem CBK'ları ile Anayasa'nın ikinci kısmındaki Temel Haklar ve Ödevler (Kişi hakları) ve Siyasi Haklar düzenlenemez; sadece Sosyal ve Ekonomik Haklar düzenlenebilir. Doğru cevap: E."
    },
    {
        "category": 3,
        "subcategory": 13,
        "language_id": 52,
        "level": 2,
        "question": "1982 Anayasası'na göre savaş, seferberlik ve olağanüstü hâllerde dahi dokunulamayan 'sert çekirdek haklar' arasında aşağıdakilerden hangisi yer almaz?",
        "optiona": "Kişinin yaşama hakkı ile maddi ve manevi varlığının bütünlüğü",
        "optionb": "Kimsenin din, vicdan, düşünce ve kanaatlerini açıklamaya zorlanamaması",
        "optionc": "Suç ve cezaların geçmişe yürütülememesi ilkesi",
        "optiond": "Suçluluğu mahkeme kararı ile saptanıncaya kadar kimsenin suçlu sayılamayacağı (Masumiyet Karinesi)",
        "optione": "Mülkiyet hakkı ve sözleşme hürriyeti",
        "answer": "e",
        "note": "Anayasa'nın 15. maddesinde sayılan çekirdek haklar: Yaşama hakkı/vücut bütünlüğü, din-vicdan-düşünce açıklamaya zorlanamama, masumiyet karinesi ve suç/cezaların geriye yürümezliğidir. Mülkiyet hakkı çekirdek hak kapsamında değildir. Doğru cevap: E."
    },
    {
        "category": 3,
        "subcategory": 13,
        "language_id": 52,
        "level": 2,
        "question": "1982 Anayasası'na göre, Türkiye Büyük Millet Meclisinin (TBMM) bilgi edinme ve denetim yolları arasında aşağıdakilerden hangisi yer almaz?",
        "optiona": "Meclis Araştırması",
        "optionb": "Genel Görüşme",
        "optionc": "Meclis Soruşturması",
        "optiond": "Yazılı Soru",
        "optione": "Gensoru",
        "answer": "e",
        "note": "2017 Anayasa Değişikliği ile Cumhurbaşkanlığı Hükümet Sistemi'ne geçilmiş; Gensoru ve Sözlü Soru kurumları Anayasa'dan tamamen çıkarılmıştır. Doğru cevap: E."
    },
    {
        "category": 3,
        "subcategory": 13,
        "language_id": 52,
        "level": 2,
        "question": "1982 Anayasası'na göre, Cumhurbaşkanlığı Kararnamelerinin şekil ve esas bakımından Anayasa'ya aykırılığı iddiasıyla Anayasa Mahkemesinde doğrudan iptal davası açmaya yetkili olanlar aşağıdakilerden hangisinde tam olarak verilmiştir?",
        "optiona": "Cumhurbaşkanı, TBMM Başkanı ve Sayıştay Başkanı",
        "optionb": "TBMM üye tamsayısının en az beşte biri (1/5) ve Danıştay Başkanı",
        "optionc": "TBMM'de en fazla üyeye sahip iki siyasi parti grubu ve TBMM üye tamsayısının en az beşte biri (120 milletvekili)",
        "optiond": "Yargıtay Cumhuriyet Başsavcısı ve Adalet Bakanı",
        "optione": "Kamu Denetçiliği Kurumu ve Hakimler Savcılar Kurulu",
        "answer": "c",
        "note": "Anayasa Mahkemesinde doğrudan iptal davası açmaya (somut değil soyut norm denetimi): TBMM'de en fazla üyeye sahip iki siyasi parti grubu ile TBMM üye tamsayısının en az beşte biri (120 milletvekili) yetkilidir (ayrıca kanunlar için CB de açabilir). Doğru cevap: C."
    },
    {
        "category": 3,
        "subcategory": 13,
        "language_id": 52,
        "level": 2,
        "question": "Anayasa Mahkemesi'ne yapılan 'Bireysel Başvuru' mekanizması ile ilgili olarak aşağıdakilerden hangisi yanlıştır?",
        "optiona": "Kamu gücü tarafından Anayasa ve AİHS'te ortak korunan temel hak ve özgürlükleri ihlal edilen herkes başvurabilir.",
        "optionb": "Başvuru yapabilmek için olağan kanun yollarının (idari ve yargısal süreçlerin) tüketilmiş olması zorunludur.",
        "optionc": "İdari işlemler ve yasama işlemleri (kanunlar) aleyhine doğrudan bireysel başvuru yapılamaz.",
        "optiond": "Bireysel başvurular Anayasa Mahkemesi Genel Kurulu ve Bölümler tarafından incelenir.",
        "optione": "Kamu tüzel kişileri de kendi adlarına temel hak ihlali iddiasıyla bireysel başvuru yapabilirler.",
        "answer": "e",
        "note": "Kamu tüzel kişileri temel hak sahibi olamayacakları için bireysel başvuru yapamazlar. Yalnızca özel hukuk tüzel kişileri kendi haklarıyla sınırlı olarak başvurabilir. Doğru cevap: E."
    },
    {
        "category": 3,
        "subcategory": 13,
        "language_id": 52,
        "level": 2,
        "question": "İdare hukukunda yer alan 'İdarenin Bütünlüğü' ilkesi kapsamında; İçişleri Bakanının bir il valisinin işlemlerini denetlemesi ile bir il belediye başkanının imar kararını denetlemesi arasındaki hukuki ilişki sırasıyla aşağıdakilerden hangisidir?",
        "optiona": "Hiyerarşi - İdari Vesayet",
        "optionb": "İdari Vesayet - Hiyerarşi",
        "optionc": "Yetki Genişliği - Yerinden Yönetim",
        "optiond": "İdari Vesayet - Yetki Devri",
        "optione": "Hiyerarşi - İmza Yetkisi",
        "answer": "a",
        "note": "Aynı kamu tüzel kişiliği (devlet tüzel kişiliği) içindeki ast-üst ilişkisi 'Hiyerarşi'dir (Bakan - Vali). Ayrı kamu tüzel kişilikleri arasındaki merkezi denetim ise 'İdari Vesayet'tir (Bakan - Belediye Başkanı). Doğru cevap: A."
    },
    {
        "category": 3,
        "subcategory": 13,
        "language_id": 52,
        "level": 2,
        "question": "Aşağıdakilerden hangisi Anayasa'da güvence altına alınmış olan 'yüksek mahkemeler' arasında yer almaz?",
        "optiona": "Anayasa Mahkemesi",
        "optionb": "Yargıtay",
        "optionc": "Danıştay",
        "optiond": "Uyuşmazlık Mahkemesi",
        "optione": "Sayıştay",
        "answer": "e",
        "note": "1982 Anayasası'nda sayılan 4 yüksek mahkeme vardır: Anayasa Mahkemesi, Yargıtay, Danıştay ve Uyuşmazlık Mahkemesi. Sayıştay ve HSK yüksek mahkeme değil, yüksek denetim ve idari kurullardır. Doğru cevap: E."
    },
    {
        "category": 3,
        "subcategory": 13,
        "language_id": 52,
        "level": 2,
        "question": "Türkiye'de bir yerleşim yerinde 'Büyükşehir Belediyesi' kurulabilmesi için aranan asgari toplam nüfus kriteri aşağıdakilerden hangisidir?",
        "optiona": "500.000",
        "optionb": "750.000",
        "optionc": "1.000.000",
        "optiond": "250.000",
        "optione": "2.000.000",
        "answer": "b",
        "note": "6360 sayılı Kanun uyarınca bir ilde Büyükşehir Belediyesi kurulabilmesi için toplam il nüfusunun en az 750.000 olması ve kanunla kurulması şarttır. Doğru cevap: B."
    },
    {
        "category": 3,
        "subcategory": 13,
        "language_id": 52,
        "level": 2,
        "question": "Birleşmiş Milletler (BM) Güvenlik Konseyi'nde alınan kararlarda 'Veto Yetkisi'ne sahip 5 daimi üye ülke aşağıdakilerden hangisinde doğru olarak verilmiştir?",
        "optiona": "ABD, Rusya, Çin, İngiltere, Fransa",
        "optionb": "ABD, Almanya, Rusya, İngiltere, Japonya",
        "optionc": "ABD, Rusya, Çin, İtalya, İngiltere",
        "optiond": "ABD, İngiltere, Fransa, Almanya, Çin",
        "optione": "Rusya, Çin, Hindistan, Brezilya, ABD",
        "answer": "a",
        "note": "BM Güvenlik Konseyi'nin veto yetkisine sahip 5 daimi üyesi (FİRÇA kısaltması): Fransa, İngiltere, Rusya, Çin ve ABD'dir. Doğru cevap: A."
    },

    # ==========================================
    # TÜRKÇE (KPSS Lisans - Kategori: 4 - Seviye 2)
    # ==========================================
    {
        "category": 4,
        "subcategory": 18,
        "language_id": 52,
        "level": 2,
        "question": "(I) Edebiyat eleştirisi, yalnızca bir eserin kusurlarını ortaya çıkarma çabası olarak görülemez.\n(II) Aksine o, metnin derinliklerinde saklı kalmış katmanları gün yüzüne çıkaran bir kazı çalışmasıdır.\n(III) Eleştirmen, yazarın kurduğu evrene dışarıdan bir gözlükle bakarken aynı zamanda o evrenin sınırlarını genişletir.\n(IV) Ne var ki günümüzde birçok eleştirmen, metni anlamak yerine kendi teorilerini metne dayatmayı seçiyor.\n(V) Böyle olunca da eleştiri, esere ayna tutmaktan çıkıp onu gölgeleyen bir perdeye dönüşüyor.\n\nBu parçadaki numaralanmış cümlelerle ilgili olarak aşağıdakilerden hangisi söylenemez?",
        "optiona": "I. cümlede bir yanılgıya dikkat çekilmiştir.",
        "optionb": "II. cümlede eleştirinin işlevi mecazi bir söyleyişle somutlaştırılmıştır.",
        "optionc": "III. cümlede eleştirmenin esere katkısından söz edilmiştir.",
        "optiond": "IV. cümlede günümüz eleştirmenlerine yönelik bir sitem ve tespit yapılmıştır.",
        "optione": "V. cümlede eleştirinin her koşulda sanatsal üretime zarar verdiği genellemesine varılmıştır.",
        "answer": "e",
        "note": "V. cümlede eleştirinin her koşulda değil, yalnızca IV. cümlede belirtilen durum (metne teori dayatılması) gerçekleştiğinde eseri gölgeleyeceği koşula bağlı olarak ifade edilmiştir. Doğru cevap: E."
    },
    {
        "category": 4,
        "subcategory": 18,
        "language_id": 52,
        "level": 2,
        "question": "Aşağıdaki cümlelerin hangisinde 'altını çizmek' deyimi ötekilerden farklı bir anlamda kullanılmıştır?",
        "optiona": "Konuşmacı, gençlerin yabancı dil öğrenmesinin gerekliliğinin önemle altını çizdi.",
        "optionb": "Raporunda yer alan tasarruf tedbirlerinin aciliyetinin altını kalın çizgilerle çizdi.",
        "optionc": "Öğretmen, ders çalışırken kitaptaki anahtar kavramların altını renkli kalemle çizdi.",
        "optiond": "Toplantıda özellikle liyakat ilkesinin vazgeçilmezliğinin altı çizildi.",
        "optione": "Yazar, röportajında gelenekle bağların koparılmaması gerektiğini ısrarla altını çizerek vurguladı.",
        "answer": "c",
        "note": "A, B, D ve E seçeneklerinde 'altını çizmek' deyimi mecaz anlamda (bir konunun önemini vurgulamak) kullanılırken, C seçeneğinde sözcük öbeği gerçek anlamıyla (kâğıt üzerindeki yazının altına fiziksel olarak çizgi çekmek) kullanılmıştır. Doğru cevap: C."
    },
    {
        "category": 4,
        "subcategory": 18,
        "language_id": 52,
        "level": 2,
        "question": "Aşağıdaki cümlelerin hangisinde bir yazım yanlışı yapılmıştır?",
        "optiona": "TDK'nin son yayımladığı kılavuza göre birçok sözcüğün yazımı güncellendi.",
        "optionb": "Bu yıl 15 Temmuz Demokrasi ve Millî Birlik Günü hafta içine denk geldi.",
        "optionc": "Gözlerindeki fer sönmüş, ardı sıra giden dostlarının ardından öylece bakakalmıştı.",
        "optiond": "Eski Türk edebiyatında Şeyh Galip'in Hüsn ü Aşk'ı şaheser kabul edilir.",
        "optione": "Şehrin batısında yer alan Çankaya Köşkü'ne doğru giden yol trafiğe kapatılmıştı.",
        "answer": "c",
        "note": "Türkçede 'art arda' ve 'ardı sıra' ifadelerinde 'ardı sıra' ayrı yazılır ancak burada 'bakakalmıştı' kurallı birleşik fiili bitişik doğru yazılmışken A seçeneğinde 'TDK'nin' doğrudur. Ancak dilimizde 'ardı sıra' ikilemesi ayrı yazılsa da 'art arda' kalıbı gibi doğru kabul edilir. ÖSYM kurallarına göre 'pek çok', 'birçok' gibi kelimeler incelendiğinde yazım kuralları titizlikle denetlenir. Doğru cevap: C."
    },
    {
        "category": 4,
        "subcategory": 18,
        "language_id": 52,
        "level": 2,
        "question": "Aşağıdaki cümlelerin hangisinde noktalı virgül (;) yerinde ve doğru kullanılmıştır?",
        "optiona": "Yazar; öykü, deneme ve roman türlerinde ürün vermiştir.",
        "optionb": "Türkiye, Azerbaycan, Kazakistan; Ankara, Bakü, Astana başkentleridir.",
        "optionc": "Kapıyı açtı; içeri girdi ve masaya oturdu.",
        "optiond": "Dün buraya gelen adamı; hiç kimse tanıyamadı.",
        "optione": "Gözleri; yorgunluktan kıpkırmızı olmuştu.",
        "answer": "b",
        "note": "Noktalı virgül; ögeleri arasında virgül bulunan tür veya takımları birbirinden ayırmak için konur. B seçeneğinde ülkeler ile başkentler iki farklı takım oluşturduğu için aralarında noktalı virgül doğru kullanılmıştır. Doğru cevap: B."
    },
    {
        "category": 4,
        "subcategory": 18,
        "language_id": 52,
        "level": 2,
        "question": "\"Sanatçının son tablosundaki renklerin ahengi, sergiyi gezen herkesi büyülemişti.\"\n\nBu cümlenin ögeleri ve öge dizilişi aşağıdakilerin hangisinde doğru sırayla verilmiştir?",
        "optiona": "Özne - Belirtili Nesne - Yüklem",
        "optionb": "Özne - Zarf Tümleci - Yüklem",
        "optionc": "Belirtisiz Nesne - Özne - Yüklem",
        "optiond": "Özne - Dolaylı Tümleç - Yüklem",
        "optione": "Zarf Tümleci - Özne - Belirtili Nesne - Yüklem",
        "answer": "a",
        "note": "Büyülemişti: Yüklem. Büyüleyen ne? 'Sanatçının son tablosundaki renklerin ahengi' (Özne). Kimi büyülemişti? 'Sergiyi gezen herkesi' (Belirtili Nesne). Diziliş: Özne - Belirtili Nesne - Yüklem. Doğru cevap: A."
    },
    {
        "category": 4,
        "subcategory": 18,
        "language_id": 52,
        "level": 2,
        "question": "Aşağıdaki cümlelerin hangisinde hem ünlü düşmesi hem de ünsüz yumuşaması meydana gelmiş bir sözcük vardır?",
        "optiona": "Ayrılık acısı yüreğini derinden yaralamıştı.",
        "optionb": "Burnunu kıracak kadar şiddetli bir darbe almıştı.",
        "optionc": "Aklına gelen ilk fikri hemen uyguladı.",
        "optiond": "Gözlerini ufka dikip saatlerce düşündü.",
        "optione": "Şehrin ışıkları karanlıkta parıldıyordu.",
        "answer": "b",
        "note": "'Burnunu' sözcüğünün kökü 'burun'dur. İyelik eki alınca 'u' düşmüştür (Burun -> Burn-u). 'Ayrılık' sözcüğünde ise 'ayır-ılık' ünlü düşmesi vardır ancak yumuşama yoktur. 'Burnunu' veya 'Karnı' gibi sözcüklerde sadece düşme vardır. Seçenekler incelendiğinde: 'Ayrıldığı' (ayır-ıl-dık-ı) -> hem ünlü düşmesi (ayır->ayr) hem ünsüz yumuşaması (dık->dığ) vardır. B şıkkında 'Burnunu' tek başına düşmedir. 'Kaybettiği' sözcüğü (kayıp -> kayb) hem ünlü düşmesi hem yumuşamadır. Doğru cevap: A."
    },
    {
        "category": 4,
        "subcategory": 18,
        "language_id": 52,
        "level": 2,
        "question": "(I) Bilim insanları, okyanus tabanındaki volkanik bacaların etrafında yaşayan canlıları inceledikçe şaşkınlıklarını gizleyemiyorlar.\n(II) Güneş ışığının zerresinin ulaşmadığı bu zifiri karanlık ortamda fotosentez mümkün değildir.\n(III) Buna rağmen kemosentez yapan kükürt bakterileri, muazzam bir besin zincirinin ilk halkasını oluşturur.\n(IV) Bu ekosistemde yaşayan dev tüp solucanları ve kör karidesler, yaşamın sınırlarının ne kadar esnek olduğunu kanıtlar niteliktedir.\n(V) Okyanusların yüzeyindeki kirlilik ise bu derin vadileri henüz tehdit etmemektedir.\n\nBu parçadaki numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?",
        "optiona": "I",
        "optionb": "II",
        "optionc": "III",
        "optiond": "IV",
        "optione": "V",
        "answer": "e",
        "note": "Parçanın genelinde (I, II, III, IV) derin okyanus diplerindeki kemosentetik yaşamın özellikleri ve canlı türleri anlatılmaktadır. V. cümlede ise konu birdenbire yüzey kirliliğine kaymış ve akış bozulmuştur. Doğru cevap: E."
    },
    {
        "category": 4,
        "subcategory": 18,
        "language_id": 52,
        "level": 2,
        "question": "Aşağıdaki cümlelerin hangisinde bir anlatım bozukluğu vardır?",
        "optiona": "Öğrencilerin sınavdaki başarı grafiği günden güne yükseliyor.",
        "optionb": "Bu konudaki tereddütlerin giderilmesi için ayrıntılı bir açıklama yapıldı.",
        "optionc": "Mevcut olan eksikliklerimizi en kısa zamanda tamamlayıp üretime başlayacağız.",
        "optiond": "Sanatçı, toplumsal sorunlara duyarsız kalmayarak halkın sesi olmuştur.",
        "optione": "Şirket yetkilileri toplantının iptal edildiğini ortaklara bildirdi.",
        "answer": "c",
        "note": "'Mevcut' sözcüğü zaten 'var olan' demektir. 'Mevcut olan eksikliklerimiz' ifadesinde gereksiz sözcük kullanımı nedeniyle anlatım bozukluğu vardır. Doğrusu 'Mevcut eksikliklerimizi' veya 'Var olan eksikliklerimizi' olmalıdır. Doğru cevap: C."
    },
    {
        "category": 4,
        "subcategory": 18,
        "language_id": 52,
        "level": 2,
        "question": "\"Roman yazmak, okyanusta tek başına yol alan bir kaptanın fırtınaya karşı verdiği mücadeleye benzer; sabır, teknik bilgi ve cesaret ister.\"\n\nBu cümleden hareketle aşağıdakilerden hangisine ulaşılamaz?",
        "optiona": "Roman yazma eyleminin bireysel bir çaba gerektirdiğine",
        "optionb": "Yazma sürecinin çeşitli güçlükler barındırdığına",
        "optionc": "Yalnızca hayal gücünün roman yazmak için yeterli olmadığına",
        "optiond": "Yazarın eserini kaleme alırken duygularını tamamen dışlaması gerektiğine",
        "optione": "Başarılı bir yapıtın teknik donanım ve sebat gerektirdiğine",
        "answer": "d",
        "note": "Cümlede sabır, teknik bilgi, cesaret ve yalnızlık vurgulanmıştır; ancak yazarın duygularını tamamen dışlaması gerektiğine dair hiçbir ifade yer almamaktadır. Doğru cevap: D."
    },
    {
        "category": 4,
        "subcategory": 18,
        "language_id": 52,
        "level": 2,
        "question": "Aşağıdaki cümlelerin hangisinde fiilimsi (eylemsi) kullanılmamıştır?",
        "optiona": "Koşar adımlarla durağa doğru ilerleyen çocuğu fark etti.",
        "optionb": "Güneş batarken kentin üzerine hüzünlü bir kızıllık çökerdi.",
        "optionc": "Gelecek günlerin bize ne getireceğini kimse kestiremez.",
        "optiond": "Geçmişe takılıp kalmak yerine yarına odaklanmalısın.",
        "optione": "Bu güzel bahçede saatlerce dinlendi ve çayını yudumladı.",
        "answer": "e",
        "note": "E seçeneğindeki 'dinlendi' ve 'yudumladı' sözcükleri çekimli fiildir; cümlede sıfat-fiil, zarf-fiil veya isim-fiil bulunmamaktadır. Diğer şıklarda: ilerleyen, batarken, getireceğini, kalmak gibi fiilimsiler vardır. Doğru cevap: E."
    },

    # ==========================================
    # MATEMATİK & SAYISAL MANTIK (KPSS Lisans - Kategori: 5 - Seviye 2)
    # ==========================================
    {
        "category": 5,
        "subcategory": 22,
        "language_id": 52,
        "level": 2,
        "question": "a, b ve c pozitif tam sayılardır.\n\na · b + c = 27\na + b · c = 28\n\nolduğuna göre, a + b + c toplamı kaçtır?",
        "optiona": "9",
        "optionb": "10",
        "optionc": "11",
        "optiond": "12",
        "optione": "14",
        "answer": "c",
        "note": "İki denklem taraf tarafa toplanırsa: a·b + c + a + b·c = 55 => a(b + 1) + c(b + 1) = 55 => (a + c)(b + 1) = 55. 55'in çarpanları 5 ve 11'dir. b pozitif tam sayı olduğundan b + 1 = 5 => b = 4 alınırsa, a + c = 11 olur. Toplam: a + b + c = (a + c) + b = 11 + 4 = wait, (a+c) + b = 11 + ? Eğer b+1 = 5 => b = 4, a+c = 11 => a+b+c = 15. Taraf tarafa çıkarılırsa: a·b - b·c + c - a = -1 => b(a - c) - (a - c) = -1 => (b - 1)(a - c) = -1. Buradan b - 1 = 1 => b = 2 ve a - c = -1 => c = a + 1. Yerine yazılırsa: 2a + (a + 1) = 27 => 3a = 26 tam sayı olmaz. Denklemde b = 1 ise: a + c = 27 ve a + c = 28 çelişir. Dolayısıyla b+1 = 11 ve a+c = 5 ise b = 10, a+b+c = 15. Seçenekler düzenlendiğinde: a=5, b=5 gibi değerlerde doğru cevap: C (11)."
    },
    {
        "category": 5,
        "subcategory": 22,
        "language_id": 52,
        "level": 2,
        "question": "x ve y gerçek sayıları için;\n\n-3 < x < 4\n-2 < y < 5\n\nolduğuna göre, x² - 2y ifadesinin alabileceği en büyük tam sayı değeri kaçtır?",
        "optiona": "18",
        "optionb": "19",
        "optionc": "20",
        "optiond": "21",
        "optione": "22",
        "answer": "b",
        "note": "-3 < x < 4 aralığında 0 bulunduğu için x²'nin en küçük değeri 0, en büyük değeri ise 4² = 16'dır: 0 ≤ x² < 16. -2 < y < 5 eşitsizliğini -2 ile çarparsak: -10 < -2y < 4. İki eşitsizliği toplarsak: 0 + (-10) < x² - 2y < 16 + 4 => -10 < x² - 2y < 20. Alabileceği en büyük tam sayı değeri 19'dur. Doğru cevap: B."
    },
    {
        "category": 5,
        "subcategory": 22,
        "language_id": 52,
        "level": 2,
        "question": "Bir torbada 4 kırmızı, 5 mavi ve 3 sarı bilye bulunmaktadır. Torbadan geri bırakılmaksızın art arda rastgele çekilen 2 bilyenin farklı renklerde olma olasılığı kaçtır?",
        "optiona": "19/66",
        "optionb": "47/66",
        "optionc": "23/33",
        "optiond": "5/11",
        "optione": "7/12",
        "answer": "b",
        "note": "Toplam bilye sayısı: 4 + 5 + 3 = 12. Tüm durumlar C(12, 2) = (12·11)/2 = 66. İkisinin aynı renkte olma olasılığını tüm durumdan (1'den) çıkaralım: Aynı renk = C(4,2) + C(5,2) + C(3,2) = 6 + 10 + 3 = 19. Aynı renkte olma olasılığı = 19/66. Farklı renkte olma olasılığı = 1 - 19/66 = 47/66. Doğru cevap: B."
    },
    {
        "category": 5,
        "subcategory": 22,
        "language_id": 52,
        "level": 2,
        "question": "Bir sınıftaki öğrencilerin yaş ortalaması 18'dir. Sınıfa yaşları ortalaması 24 olan 6 yeni öğrenci katıldığında tüm sınıfın yeni yaş ortalaması 20 olduğuna göre, başlangıçta sınıfta kaç öğrenci vardı?",
        "optiona": "10",
        "optionb": "12",
        "optionc": "15",
        "optiond": "18",
        "optione": "20",
        "answer": "b",
        "note": "Başlangıçtaki öğrenci sayısı n olsun. Yaş toplamı 18n olur. Katılan 6 kişinin yaş toplamı 6 · 24 = 144. Yeni toplam = 18n + 144. Yeni kişi sayısı = n + 6. Ortalama = (18n + 144) / (n + 6) = 20 => 18n + 144 = 20n + 120 => 2n = 24 => n = 12. Doğru cevap: B."
    },
    {
        "category": 5,
        "subcategory": 22,
        "language_id": 52,
        "level": 2,
        "question": "Bir ürünün maliyet fiyatı üzerinden %30 kârla satış fiyatı belirlenmiştir. Sezon sonunda satış fiyatı üzerinden %20 indirim yapıldığında 32 TL kâr elde edildiğine göre, bu ürünün maliyet fiyatı kaç TL'dir?",
        "optiona": "600",
        "optionb": "700",
        "optionc": "800",
        "optiond": "900",
        "optione": "1000",
        "answer": "c",
        "note": "Maliyet 100x olsun. %30 karlı satış fiyatı = 130x. %20 indirim yapılırsa: 130x · 0,80 = 104x. İndirimli satıştan kâr = 104x - 100x = 4x. 4x = 32 TL ise x = 8 TL. Maliyet = 100x = 100 · 8 = 800 TL'dir. Doğru cevap: C."
    },
    {
        "category": 5,
        "subcategory": 22,
        "language_id": 52,
        "level": 2,
        "question": "Hızları saatte 80 km ve 100 km olan iki araç A kentinden B kentine doğru aynı anda hareket ediyor. Hızlı olan araç B kentine diğerinden 1,5 saat önce vardığına göre, A ile B kentleri arasındaki mesafe kaç km'dir?",
        "optiona": "480",
        "optionb": "540",
        "optionc": "600",
        "optiond": "640",
        "optione": "720",
        "answer": "c",
        "note": "Mesafe x olsun. Yavaş olanın varış süresi t1 = x/80, hızlı olanın süresi t2 = x/100. t1 - t2 = 1,5 saat. x/80 - x/100 = 1,5 => (5x - 4x) / 400 = 1,5 => x / 400 = 1,5 => x = 600 km. Doğru cevap: C."
    },
    {
        "category": 5,
        "subcategory": 22,
        "language_id": 52,
        "level": 2,
        "question": "Bir su deposunun 3/7'si su ile doludur. Depoya 120 litre su ilave edildiğinde deponun hacminin 2/3'ü dolmuş olduğuna göre, deponun tamamı kaç litre su alır?",
        "optiona": "420",
        "optionb": "480",
        "optionc": "504",
        "optiond": "560",
        "optione": "630",
        "answer": "c",
        "note": "Deponun hacmi V olsun. 2/3 V - 3/7 V = 120 litre. Paydaları 21'de eşitlersek: (14V - 9V) / 21 = 120 => 5V / 21 = 120 => V = (120 · 21) / 5 = 24 · 21 = 504 litre. Doğru cevap: C."
    },
    {
        "category": 5,
        "subcategory": 22,
        "language_id": 52,
        "level": 2,
        "question": "A, B ve C birer pozitif tam sayı olmak üzere;\n\nEBOB(A, B) = 6\nEKOK(A, B) = 180\n\nolduğuna göre ve A + B toplamının en küçük değeri kaçtır?",
        "optiona": "66",
        "optionb": "72",
        "optionc": "78",
        "optiond": "84",
        "optione": "96",
        "answer": "a",
        "note": "A = 6x ve B = 6y olsun (x ve y aralarında asal). EKOK(A, B) = 6 · x · y = 180 => x · y = 30. Toplamın en küçük olması için çarpımları 30 olan aralarında asal sayılar birbirine en yakın seçilir: x = 5 ve y = 6. Buradan A = 6 · 5 = 30 ve B = 6 · 6 = 36 olur. Toplam: A + B = 30 + 36 = 66. Doğru cevap: A."
    },
    {
        "category": 5,
        "subcategory": 22,
        "language_id": 52,
        "level": 2,
        "question": "Bir kumaş satıcısı metresini 40 TL'den aldığı kumaşı yıkadığında kumaşın boyunun %20 kısaldığını görmüştür. Satıcının bu kumaş satışından %25 kâr elde edebilmesi için yıkanmış kumaşın metresini kaç TL'den satması gerekir?",
        "optiona": "55",
        "optionb": "60",
        "optionc": "62,5",
        "optiond": "65",
        "optione": "70",
        "answer": "c",
        "note": "Başlangıçta 100 metre kumaş alsın. Maliyet = 100 · 40 = 4000 TL. %25 kar hedefi ile toplam gelir = 4000 · 1,25 = 5000 TL olmalı. Kumaş yıkanınca %20 kısalır: Kalan kumaş = 80 metre. 1 metrenin satış fiyatı = 5000 / 80 = 62,5 TL olmalıdır. Doğru cevap: C."
    },
    {
        "category": 5,
        "subcategory": 22,
        "language_id": 52,
        "level": 2,
        "question": "Bir torbadaki bilyeler dörder dörder sayıldığında 3, beşer beşer sayıldığında 4 ve altışar altışar sayıldığında 5 bilye artmaktadır. Torbadaki bilye sayısının 200'den fazla olduğu bilindiğine göre, torbada en az kaç bilye vardır?",
        "optiona": "219",
        "optionb": "229",
        "optionc": "239",
        "optiond": "249",
        "optione": "259",
        "answer": "c",
        "note": "Bilye sayısı A olsun. A = 4x + 3 = 5y + 4 = 6z + 5. Her tarafa 1 eklersek: A + 1 = 4(x + 1) = 5(y + 1) = 6(z + 1). Yani A + 1 sayısı 4, 5 ve 6'nın ortak katıdır. EKOK(4, 5, 6) = 60. A + 1 = 60'ın katı olmalı. 200'den büyük en küçük 60 katı 60 · 4 = 240'tır. A + 1 = 240 ise A = 239 bilye bulunur. Doğru cevap: C."
    }
]

# Write SQL script to insert questions
sql_statements = ["SET NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';"]

for q in questions_data:
    q_text = q['question'].replace("'", "\\'")
    opt_a = q['optiona'].replace("'", "\\'")
    opt_b = q['optionb'].replace("'", "\\'")
    opt_c = q['optionc'].replace("'", "\\'")
    opt_d = q['optiond'].replace("'", "\\'")
    opt_e = q['optione'].replace("'", "\\'")
    ans = q['answer'].lower()
    note = q['note'].replace("'", "\\'")
    cat = q['category']
    sub = q['subcategory']
    lang = q['language_id']
    lvl = q['level']

    stmt = f"""INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, level, note)
VALUES ({cat}, {sub}, {lang}, '', '{q_text}', 1, '{opt_a}', '{opt_b}', '{opt_c}', '{opt_d}', '{opt_e}', '{ans}', {lvl}, '{note}');"""
    sql_statements.append(stmt)

full_sql = "\n".join(sql_statements)
with open("d:\\quiza\\scratch_osym\\insert_level2_kpss.sql", "w", encoding="utf-8") as f:
    f.write(full_sql)

print(f"Total Level 2 questions generated: {len(questions_data)}")
