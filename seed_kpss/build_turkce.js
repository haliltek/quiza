const fs = require('fs');

const pPath = 'C:/Users/Halil/.gemini/antigravity-ide/brain/4ea7509a-a32e-412e-8838-11397c0a91c7/scratch/kpss_turkce_all.js';
let p = fs.readFileSync(pPath, 'utf8');

const extra18 = `
    addQ(4, 18, 3, '"Gözden çıkarmak" deyiminin anlamı aşağıdakilerden hangisidir?', 'Bir şeyin elden çıkmasına veya feda edilmesine razı olmak', 'Bir şeyi çok beğenmek', 'Göz sağlığını kaybetmek', 'Birinden intikam almak', 'Herkesin dikkatini çekmek', 'A', 'Gözden çıkarmak; bir amaç uğruna bir varlıktan veya kazançtan vazgeçmeyi kabullenmektir.');
    addQ(4, 18, 3, '"Sanatçı eserinde hayatın acı gerçeklerini bir ayna gibi yansıtmıştır." cümlesindeki anlam olayı aşağıdakilerden hangisidir?', 'Teşbih (Benzetme)', 'Mecazımürsel (Ad Aktarması)', 'Tezat (Zıtlık)', 'Kinaye', 'Teşhis (Kişileştirme)', 'A', '"Bir ayna gibi yansıtmak" ifadesinde gibi edatıyla benzetme (teşbih) yapılmıştır.');
    addQ(4, 18, 3, 'Aşağıdaki cümlelerin hangisinde "dolaylama" yapılmıştır?', 'Bacada tüten dumanlar köye beyaz bir gelinlik giydirmişti.', 'Kara kıta açlıkla boğuşurken dünya izlemeye devam ediyor.', 'Takım dün akşam sahada var gücüyle savaştı.', 'Ormanın kralı sessizce avına yaklaşıyordu.', 'İzmir, Ege\\'nin incisi olarak turistleri büyülüyor.', 'E', '"Ege\\'nin incisi" İzmir için, "Kara kıta" Afrika için, "Ormanın kralı" aslan için dolaylamadır.');
    addQ(4, 18, 3, 'Aşağıdaki cümlelerin hangisinde kinayeli bir anlatım vardır?', 'Çok çalışkan olduğu karnesindeki zayıflardan belli.', 'Sınavı kazanmak için gecesini gündüzüne kattı.', 'Yağmur dünden beri aralıksız yağıyor.', 'Güneş dağların ardından usulca battı.', 'Kitap fuarı bu yıl çok kalabalıktı.', 'A', 'Sözün tersini kastederek alay etme veya hem gerçek hem mecaz anlamı düşündürüp mecazı kastetme kinayedir.');
    addQ(4, 18, 3, '"Ahşap konağın tahtaları soğuk kış gecelerinde acıyla inlerdi." cümlesinde hangi söz sanatı vardır?', 'Teşhis (Kişileştirme)', 'Tezat', 'Mübalağa', 'İntak', 'Tariz', 'A', 'İnsana özgü "inlemek" fiilinin ahşap konağa aktarılması kişileştirmedir.');
`;

const extra19 = `
    addQ(4, 19, 3, 'Bir paragrafta düşünceyi geliştirme yollarından "tanık gösterme"nin temel amacı nedir?', 'Yazarın savunduğu düşünceyi alanında uzman bir kişinin sözüyle destekleyip inandırıcılığı artırmak', 'Olayları kronolojik sıraya koymak', 'Karakterlerin iç dünyasını betimlemek', 'Paragrafı gereksiz yere uzatmak', 'Farklı görüşleri çürütmek', 'A', 'Tanık göstermede yazar kendi tezini güçlendirmek için tanınan bir otoritenin doğrudan sözünü alıntılar.');
    addQ(4, 19, 3, 'Paragrafta "akışı bozan cümle"yi bulurken en çok neye dikkat edilmelidir?', 'Konunun farklı bir yönüne geçen veya anlam zincirinden kopan yabancı düşünceye', 'Cümlenin uzunluğuna', 'Yüklemin sonda olup olmamasına', 'Cümledeki noktalama işaretlerine', 'Yazım kurallarına', 'A', 'Akışı bozan cümle paragrafın ana temasından saparak farklı bir bakış açısı sunan cümledir.');
    addQ(4, 19, 3, 'Bir eleştirmenin "Bu romanda ne anlatıldığı kadar nasıl anlatıldığı da beni büyüledi." sözü eserin hangi yönlerini vurgulamaktadır?', 'İçerik (Konu) ve Üslup (Biçem)', 'Sadece hacim ve sayfa sayısı', 'Fiyat ve kapak tasarımı', 'Yazarın biyografisi', 'Yayınlandığı dönemin siyaseti', 'A', '"Ne anlatıldığı" içerik/konu; "nasıl anlatıldığı" ise yazarın dili kullanış biçimi olan üsluptur.');
    addQ(4, 19, 3, '"Yazar, olayları kendi merceğinden geçirmeden olduğu gibi, kamera tarafsızlığıyla aktarmıştır." cümlesinde yazarın hangi niteliği övülmektedir?', 'Nesnellik (Objektiflik)', 'Öznellik', 'Ağdalı dil kullanımı', 'Özgünlük', 'Süslü anlatım', 'A', 'Olayları kamera gibi tarafsız aktarmak nesnelliğin (objektifliğin) göstergesidir.');
    addQ(4, 19, 3, '"Bir yazarın özgün olabilmesi, başkalarının ayak izlerine basmadan kendi patikasını açmasıyla mümkündür." sözüyle vurgulanan temel ilke nedir?', 'Taklitten uzak durmak ve kendine has olmak', 'Çok sayıda eser vermek', 'Yabancı dillerden çeviri yapmak', 'Geleneksel konuları işlemek', 'Halkın dilinden uzaklaşmak', 'A', 'Kendi patikasını açmak, kimseyi taklit etmeden özgün bir tarz oluşturmaktır.');
`;

const extra20 = `
    addQ(4, 20, 3, '"Yıllardır hayalini kurduğu o eski yalıyı nihayet dün satın aldı." cümlesinin ögeleri sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?', 'Belirtili Nesne - Zarf Tümleci - Zarf Tümleci - Yüklem', 'Özne - Belirtili Nesne - Yüklem', 'Zarf Tümleci - Özne - Yüklem', 'Belirtisiz Nesne - Zarf Tümleci - Yüklem', 'Dolaylı Tümleç - Özne - Nesne - Yüklem', 'A', 'Satın aldı (Yüklem), Kim? O (Gizli özne), Neyi? Yıllardır hayalini kurduğu o eski yalıyı (Belirtili Nesne), Ne zaman? Nihayet (Zarf T.), Ne zaman? Dün (Zarf T.).');
    addQ(4, 20, 3, 'Aşağıdaki cümlelerin hangisinde "çatı özelliği" ARANMAZ?', 'Dışarıdaki soğuk hava hepimizi tir tir titretiyordu.', 'Okulun bahçesindeki ulu çınar asırlara meydan okuyan bir abideydi.', 'Bahçedeki sararmış yaprakları büyük bir titizlikle topladı.', 'Kuşlar akşam karanlığı çökünce yuvalarına doğru kanat çırptı.', 'Yolculuk boyunca pencereden dışarıyı seyretti.', 'B', 'İsim cümlelerinde (yüklemi ek-eylem almış isim veya isim soylu sözcük olan cümlelerde) fiil çatısı aranmaz.');
    addQ(4, 20, 3, '"Ders çalışırken müzik dinlemek bazılarının odaklanmasını güçleştirir." cümlesindeki fiilimsilerin (eylemsilerin) türleri sırasıyla hangileridir?', 'Zarf-fiil - İsim-fiil - İsim-fiil', 'Sıfat-fiil - İsim-fiil - Zarf-fiil', 'Zarf-fiil - Sıfat-fiil - Zarf-fiil', 'İsim-fiil - İsim-fiil - Sıfat-fiil', 'Sıfat-fiil - Sıfat-fiil - İsim-fiil', 'A', 'çalış-ırken (Zarf-fiil), dinle-mek (İsim-fiil), odaklan-ma-sı (İsim-fiil).');
    addQ(4, 20, 3, 'Aşağıdaki cümlelerin hangisinde bir anlatım bozukluğu vardır?', 'Bu zorlu sınavı kazanmak için kuşkusuz çok emek vermiş olmalı.', 'Öğrenciler ders zili çalınca sessizce sınıflarına girdiler.', 'Yağmur dindikten sonra gökyüzünde bir gökkuşağı belirdi.', 'Yeni aldığı arabayla ilk kez uzun yola çıktı.', 'Her sabah düzenli olarak yarım saat koşar.', 'A', '"Kuşkusuz" (kesinlik) ile "olmalı" (ihtimal) sözcüklerinin bir arada kullanılması çelişen sözcüklerden kaynaklanan anlatım bozukluğudur.');
    addQ(4, 20, 3, '"Yarışmada birinci olan öğrenciye plaketini okul müdürü verdi." cümlesinde vurgulanan öge hangisidir?', 'Özne (Okul müdürü)', 'Belirtili Nesne', 'Dolaylı Tümleç', 'Zarf Tümleci', 'Yüklem', 'A', 'Fiil cümlelerinde vurgu yüklemden hemen önceki ögededir. Yüklemden hemen önce "okul müdürü" (özne) yer almaktadır.');
`;

const extra21 = `
    addQ(4, 21, 3, 'Aşağıdaki cümlelerin hangisinde büyük harflerin yazımıyla ilgili bir YANLIŞLIK yapılmıştır?', 'Güneydoğu Anadolu Bölgesi\\'nde pamuk üretimi yaygındır.', 'Bu akşam Boğaz\\'dan geçen gemileri Van kedimiz Pamuk ile izledik.', 'Tarih öğretmeni bize Kurtuluş Savaşı Dönemi\\'ni detaylı anlattı.', 'Fırat nehri üzerinde kurulan barajlar ülke ekonomisine büyük katkı sağlar.', 'Her yıl 29 Ekim Cumhuriyet Bayramı coşkuyla kutlanır.', 'D', 'Nehir, göl, dağ, deniz adları büyük harfle başlar: "Fırat Nehri" şeklinde yazılmalıdır.');
    addQ(4, 41, 3, 'Aşağıdaki cümlelerin hangisinde "ki"nin yazımı YANLIŞTIR?', 'Evdeki hesap çarşıya uymadı.', 'Seninki yine derse geç kaldı.', 'Mademki gelmeyecektin neden haber vermedin?', 'Duydumki unutmuşsun gözlerimin rengini.', 'Oysaki her şey çok güzel başlamıştı.', 'D', '"Duydum ki" cümlesindeki ki bağlaçtır ve ayrı yazılmalıdır (SOMBAHÇEMİ formülü dışındakiler ayrı yazılır).');
    addQ(4, 21, 3, 'Aşağıdaki cümlelerin hangisinde kesme işareti (\\') YANLIŞ kullanılmıştır?', 'Türk Dil Kurumu\\'na yapılan başvurular incelendi.', 'Ahmet\\'in kardeşi bu yıl liseye başladı.', 'Ankara\\'dan dün akşam yola çıktılar.', '1923\\'te Cumhuriyet ilan edildi.', 'TBMM\\'nin aldığı tarihi kararlar açıklandı.', 'A', 'Kurum, kuruluş, kurul, birleşim ve iş yeri adlarına gelen ekler kesmeyle AYRILMAZ: "Türk Dil Kurumuna" olmalıdır.');
    addQ(4, 21, 3, 'Aşağıdaki cümlelerin hangisinde noktalı virgül (;) yerinde kullanılmıştır?', 'Sevinçten, heyecandan içim içime sığmıyor; bağırmak, kahkahalar atmak istiyorum.', 'Bahçede elmalar; armutlar ve kirazlar toplanmıştı.', 'Pazardan; domates, biber ve patlıcan aldım.', 'Yarın akşam bize gel; birlikte çalışalım.', 'Ders zili çaldı; herkes sınıfa girdi.', 'A', 'Ögeleri arasında virgül bulunan sıralı cümleleri birbirinden ayırmak için noktalı virgül (;) kullanılır.');
    addQ(4, 21, 3, 'Aşağıdaki sözcüklerden hangisinin yazımı DOĞRUDUR?', 'Hristiyan', 'Kıravat', 'Kirbit', 'Traş', 'Yalnız', 'E', '"Yalnız" (yalın-ız) doğrudur. Hristiyan -> Hristiyan (i yok), Kravat (ı yok), Kibrit, Tıraş (ı var).');
`;

const extra22L2 = `
    addQ(4, 22, 2, 'Ahmet, Burak, Cem ve Deniz bir koşu yarışına katılmıştır. Ahmet yarışı Burak\\'tan önce, Cem ise Deniz\\'den sonra tamamlamıştır. Burak yarışı Cem\\'den önce bitirdiğine göre yarışı sonuncu bitiren kimdir?', 'Deniz', 'Cem', 'Burak', 'Ahmet', 'Belirlenemez', 'A', 'Sıralama: Ahmet > Burak > Cem > Deniz. Dolayısıyla yarışı sonuncu bitiren Deniz\\'dir.');
    addQ(4, 22, 2, 'Beş katlı bir apartmanın her katında bir daire vardır ve Ali, Banu, Can, Derya, Emre oturmaktadır. Ali 3. katta oturmaktadır. Can, Banu\\'nun hemen üstündeki kattadır. Derya en üst katta (5. kat) oturduğuna göre 1. katta kim oturmaktadır?', 'Emre veya Banu (Banu 2. katta ise Emre 1. kattadır)', 'Sadece Can', 'Sadece Ali', 'Derya', 'Banu 4. kattadır', 'A', 'Derya 5\\'te, Ali 3\\'te. Can ve Banu ardışık olmalı: Can 2\\'de ise Banu 1\\'dedir; ya da Can 4\\'te Banu 2\\'de olamaz. Dolayısıyla yerleşim tek türlü netleşir.');
    addQ(4, 22, 2, 'Pazartesi, Salı ve Çarşamba günleri nöbet tutan doktorlar Ayşe, Berk ve Ceren\\'dir. Berk Salı günü nöbet tutmamıştır. Ceren nöbetini Ayşe\\'den hemen sonraki gün tutmuştur. Buna göre Salı günü kim nöbetçidir?', 'Ceren', 'Ayşe', 'Berk', 'Ayşe veya Berk', 'Ceren nöbet tutmamıştır', 'A', 'Ceren Ayşe\\'den hemen sonra ise: Pazartesi Ayşe, Salı Ceren, Çarşamba Berk olur (Berk Salı tutmamıştır şartı sağlanır).');
    addQ(4, 22, 2, 'Bir kütüphanede A, B, C, D kitapları soldan sağa dizilmiştir. B kitabı en solda değildir. C kitabı A ile D arasındadır. A kitabı en solda olduğuna göre sağdan ikinci kitap hangisidir?', 'C kitabı', 'A kitabı', 'B kitabı', 'D kitabı', 'Belirlenemez', 'A', 'A en solda (1. sıra). C, A ile D arasında ise D 3. veya 4. sıradadır. Dizi: A - C - D - B veya A - C - B - D. Dolayısıyla C her halükarda A\\'nın yanındadır.');
    addQ(4, 22, 2, 'Bir manavda elma, armut, muz ve portakal satılmaktadır. Muz portakaldan daha pahalı, elma armuttan daha ucuzdur. Armut portakaldan daha pahalı olduğuna göre en ucuz meyve hangisi OLABİLİR?', 'Elma', 'Muz', 'Armut', 'Portakal', 'Muz veya Armut', 'A', 'Muz > Portakal, Armut > Elma, Armut > Portakal. Sıralamada Elma Portakal\\'dan da ucuz olabilir, dolayısıyla en ucuz elma olabilir.');
`;

const extra22L3 = `
    addQ(4, 22, 3, 'Bir şirkette müdür, müdür yardımcısı, şef ve uzman pozisyonları vardır. K, L, M, N kişileri bu pozisyonlardadır. K uzman değildir. L şef veya müdür yardımcısıdır. M en üst makamdadır (müdür). Buna göre uzman pozisyonunda kim bulunmaktadır?', 'N kişisi', 'K kişisi', 'L kişisi', 'M kişisi', 'Belirlenemez', 'A', 'M müdür. L şef veya müdür yardımcısı. K uzman değilse şef veya müdür yardımcısıdır. Geriye kalan N uzman olmak zorundadır.');
    addQ(4, 22, 3, 'A, B, C, D, E adlı 5 öğrenci bir yuvarlak masa etrafında oturmaktadır. A ile B yan yanadır. C, D\\'nin hemen sağındadır. E, A\\'nın hemen solundadır. Buna göre C\\'nin karşısında oturan kimdir?', 'A veya B', 'Yalnızca E', 'Yalnızca D', 'Masa kare olduğundan oturamazlar', 'Belirlenemez', 'A', 'Döngüsel yerleşimde E-A-B bloğu ve D-C bloğu masayı tam 5 kişiye tamamlar.');
    addQ(4, 22, 3, 'Bir lokantada çorba, kebap ve tatlı siparişi veren 3 müşteri (Ali, Veli, Selami) vardır. Herkes farklı bir yemek türü seçmiştir. Ali tatlı yememiştir. Veli kebap yememiştir. Selami\\'nin çorba içtiği bilindiğine göre Ali hangi yemeği sipariş etmiştir?', 'Kebap', 'Tatlı', 'Çorba', 'Salata', 'Belirlenemez', 'A', 'Selami çorba içti. Ali tatlı yemediğine göre geriye sadece Kebap kalır.');
    addQ(4, 22, 3, 'Bir turnuvada 4 takım (T1, T2, T3, T4) lig usulü tek maç yapmıştır. T1 hiçbir maçını kaybetmemiştir. T4 tüm maçlarını kaybetmiştir. T2, T3\\'ü mağlup ettiğine göre şampiyon takım hangisidir?', 'T1 takımı', 'T2 takımı', 'T3 takımı', 'T4 takımı', 'T2 ve T3 berabere kalmıştır', 'A', 'Hiç maç kaybetmeyen takım T1\\'dir ve en yüksek puanı toplayarak şampiyon olmuştur.');
    addQ(4, 22, 3, 'Bir sinema salonunda yan yana 5 koltuk (1\\'den 5\\'e) numaralandırılmıştır. Can 3 numarada oturmaktadır. Aslı tek numaralı bir koltukta oturmaktadır ancak Can ile yan yana değildir. Buna göre Aslı kaç numaralı koltuktadır?', '1 veya 5 numaralı koltukta', '2 numaralı koltukta', '4 numaralı koltukta', 'Yalnızca 3 numarada', 'Koltuk numarası çifttir', 'A', 'Tek sayılar 1, 3, 5. Can 3\\'te. Can ile yan yana değilse (2 ve 4 olamaz), Aslı 1 veya 5 numaralı koltukta oturabilir.');
`;

// Insert subcat 18
p = p.replace(/(addQ\(4, 18, 3, 'Aşağıdaki atasözlerinden hangisi[\s\S]*?\);)/, '$1\n' + extra18);

// Insert subcat 19
p = p.replace(/(addQ\(4, 19, 3, 'Paragraf sorularında \'çıkarılamaz\'[\s\S]*?\);)/, '$1\n' + extra19);

// Insert subcat 20
p = p.replace(/(addQ\(4, 20, 3, '\'Gözlerinin içine baktıkça çocukluğumu hatırlıyorum\'[\s\S]*?\);)/, '$1\n' + extra20);

// Insert subcat 21
p = p.replace(/(addQ\(4, 21, 3, 'Aşağıdaki cümlelerin hangisinde bir yazım yanlışı[\s\S]*?\);)/, '$1\n' + extra21);

// Insert subcat 22 Level 2
p = p.replace(/(addQ\(4, 22, 2, 'K, L, M, N, P adlı 5 kişi bir bankta[\s\S]*?\);)/, '$1\n' + extra22L2);

// Insert subcat 22 Level 3
p = p.replace(/(addQ\(4, 22, 3, 'Bir otoparkta 5 araçlık yan yana park[\s\S]*?\);)/, '$1\n' + extra22L3);

fs.writeFileSync('d:/quiza/seed_kpss/kpss_turkce.js', p, 'utf8');
console.log('kpss_turkce.js created.');
