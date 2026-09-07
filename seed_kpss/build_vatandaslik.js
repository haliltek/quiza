const fs = require('fs');

const p1Path = 'C:/Users/Halil/.gemini/antigravity-ide/brain/4ea7509a-a32e-412e-8838-11397c0a91c7/scratch/kpss_vatandaslik_part1.js';
const p2Path = 'C:/Users/Halil/.gemini/antigravity-ide/brain/4ea7509a-a32e-412e-8838-11397c0a91c7/scratch/kpss_vatandaslik_part2.js';

let p1 = fs.readFileSync(p1Path, 'utf8');
let p2 = fs.readFileSync(p2Path, 'utf8');

const extra13 = `
    addQ(3, 13, 3, 'Haksız fiilin unsurlarından biri olan illiyet bağını (nedensellik bağı) kesen durumlar aşağıdakilerin hangisinde tam olarak verilmiştir?', 'Mücbir sebep, zarar görenin ağır kusuru, üçüncü kişinin ağır kusuru', 'Haksız fiil, rıza, meşru müdafaa', 'Zarar, kusur, hukuka aykırılık', 'Gaiplik, ölüm karinesi, zamanaşımı', 'Defi, itiraz, temerrüt', 'A', 'İlliyet bağı; mücbir sebep, zarar görenin veya üçüncü kişinin kusuru ile kesilir ve sorumluluk kalkar.');
    addQ(3, 13, 3, 'Hukuk düzeninin gerçekleşmesini bir kimsenin iradesine bağladığı ve hukuki sonuç doğuran fiillere ne denir?', 'Hukuki İşlem', 'Hukuki Olay', 'Maddi Fiil', 'Haksız Fiil', 'Gabin', 'A', 'Kişinin iradesiyle hukuki sonuç doğurması hukuki işlemdir (sözleşme, vasiyetname vb.).');
    addQ(3, 13, 3, 'Bir hukuki işlemin kurucu unsurları tam olmasına rağmen kanunun emredici hükümlerine aykırı yapılması sebebiyle baştan itibaren hükümsüz olmasına ne ad verilir?', 'Mutlak Butlan', 'Yokluk', 'Nisbi Butlan', 'Askıda Hükümsüzlük', 'Fesih', 'A', 'Mutlak butlanda işlem ölü doğmuştur; kamu düzenini ilgilendirdiği için hakim re\\\'sen gözetir.');
    addQ(3, 13, 3, 'Tarafların gerçek iradelerini gizleyerek üçüncü kişileri aldatmak amacıyla görünüşte başka bir işlem yapmaları durumuna ne denir?', 'Muvazaa', 'Hata', 'Hile', 'İkrah (Korkutma)', 'Gabin', 'A', 'Muvazaada taraflar üçüncü kişileri aldatma kastıyla gizli bir anlaşma yaparlar; görünürdeki işlem butlanla sakattır.');
    addQ(3, 13, 3, 'Türk Medeni Kanunu\\\'na göre bir hakkın kazanılmasında iyi niyet aranırken, bir hakkın kullanılmasında ve borçların ifasında hangi ilke geçerlidir?', 'Dürüstlük Kuralı (Objektif İyiniyet)', 'Sübjektif İyiniyet', 'Ahde Vefa İlkesi', 'Hakkaniyet İlkesi', 'Kusursuz Sorumluluk', 'A', 'TMK m. 2 uyarınca herkes haklarını kullanırken ve borçlarını ifa ederken dürüstlük kuralına uymak zorundadır.');
`;

const extra14 = `
    addQ(3, 14, 3, '1982 Anayasası\\\'na göre siyasi partilerin kapatılması davası kim tarafından ve nerede açılır?', 'Yargıtay Cumhuriyet Başsavcısı tarafından Anayasa Mahkemesi\\\'nde açılır', 'Adalet Bakanı tarafından Danıştay\\\'da', 'İçişleri Bakanı tarafından İdare Mahkemesi\\\'nde', 'TBMM Başkanı tarafından Yargıtay\\\'da', 'Cumhurbaşkanı tarafından AYM\\\'de', 'A', 'Siyasi partilerin kapatılması davasını Yargıtay Cumhuriyet Başsavcısı açar; kararı AYM üye tamsayısının 2/3 çoğunluğuyla verir.');
    addQ(3, 14, 3, '1982 Anayasası\\\'nda \\\'Sosyal ve Ekonomik Haklar\\\'ın yerine getirilmesinde devletin sorumluluğunun sınırı Anayasa\\\'da nasıl belirlenmiştir?', 'Mali kaynaklarının yeterliliği ölçüsünde', 'Sınırsız ve mutlak olarak', 'Yalnızca uluslararası yardımlarla', 'Mahkeme kararları doğrultusunda', 'Seçim dönemlerine bağlı olarak', 'A', 'Anayasa m. 65: Devlet, sosyal ve ekonomik ödevlerini mali kaynaklarının yeterliliği ölçüsünde yerine getirir.');
    addQ(3, 14, 3, '1982 Anayasası\\\'na göre Cumhurbaşkanlığı Kararnameleri (CBK) kanun ile çatıştığında hangi kural geçerlidir?', 'Kanun hükümleri uygulanır', 'CBK hükümleri uygulanır', 'AYM\\'ye başvuruluncaya kadar ikisi de durur', 'Cumhurbaşkanının tercihi geçerli olur', 'Son tarihli olan uygulanır', 'A', 'Anayasa m. 104 uyarınca kanun ile CBK aynı konuda farklı hükümler içerirse kanun hükümleri uygulanır.');
    addQ(3, 14, 3, 'Temel hak ve hürriyetlerin yabancılar için sınırlandırılması Anayasa\\\'nın 16. maddesine göre neye uygun olarak yapılabilir?', 'Milletlerarası hukuka uygun olarak ancak kanunla', 'Valilik genelgesiyle', 'Yalnızca Dışişleri Bakanı kararıyla', 'Sınırlandırılamaz', 'Yönetmelikle', 'A', 'Anayasa m. 16: Temel hak ve hürriyetler, yabancılar için, milletlerarası hukuka uygun olarak kanunla sınırlanabilir.');
    addQ(3, 14, 3, '1982 Anayasası\\\'na göre vatandaşlıktan çıkarma ile ilgili karar ve işlemlere karşı hangi kanun yolu kesinlikle kapatılamaz?', 'Yargı yolu (Danıştay denetimi)', 'İdari başvuru', 'TBMM dilekçe komisyonu', 'Sayıştay incelemesi', 'Ombudsman incelemesi', 'A', 'Anayasa m. 66: Vatandaşlıktan çıkarma ile ilgili karar ve işlemlere karşı yargı yolu kapatılamaz.');
`;

const extra15 = `
    addQ(3, 15, 3, 'TBMM seçimleri hangi gerekçeyle ve en fazla ne kadar süreyle geriye bırakılabilir (ertelenebilir)?', 'Savaş sebebiyle TBMM kararıyla en fazla 1 yıl süreyle', 'Doğal afet sebebiyle Cumhurbaşkanı kararıyla 6 ay', 'Ekonomik kriz sebebiyle 2 yıl', 'Seçim komisyonu kararıyla 3 ay', 'OHAL sebebiyle 1 yıl', 'A', 'Anayasa m. 78: Savaş sebebiyle yeni seçimlerin yapılmasına imkân görülmezse TBMM seçimlerin 1 yıl geriye bırakılmasına karar verebilir.');
    addQ(3, 15, 3, 'Anayasa Mahkemesi kaç üyeden oluşur ve üyelerin görev süresi kaç yıldır?', '15 üyeden oluşur - Görev süresi 12 yıldır (bir kimse iki defa üye seçilemez)', '11 üye - Ömür boyu', '17 üye - 5 yıl', '12 üye - 10 yıl', '20 üye - 6 yıl', 'A', 'AYM 15 üyeden oluşur (3 üyeyi TBMM, 12 üyeyi CB seçer). Üyeler 12 yıl için seçilir, 65 yaşında emekli olurlar.');
    addQ(3, 15, 3, 'Danıştay üyelerinin seçim dağılımı aşağıdakilerin hangisinde doğru verilmiştir?', 'Üçte üçünü HSK, dörtte birini Cumhurbaşkanı seçer', 'Tamamını HSK seçer', 'Yarısını TBMM, yarısını CB seçer', 'Tamamını Cumhurbaşkanı seçer', 'Dörtte üçünü TBMM seçer', 'A', 'Danıştay üyelerinin 3/4\\\'ünü Hakimler ve Savcılar Kurulu (HSK), 1/4\\\'ünü ise Cumhurbaşkanı doğrudan seçer.');
    addQ(3, 15, 3, 'Anayasa Mahkemesi\\\'ne Bireysel Başvuru için iç hukuk yollarının tüketildiği tarihten itibaren kaç gün içinde başvuru yapılmalıdır?', '30 gün içinde', '60 gün içinde', '15 gün içinde', '90 gün içinde', '6 ay içinde', 'A', 'Temel hak ve özgürlükleri ihlal edilen herkes nihai kararın öğrenilmesinden itibaren 30 gün içinde AYM\\\'ye bireysel başvuruda bulunabilir.');
    addQ(3, 15, 3, 'Cumhurbaşkanının Yüce Divan\\\'da yargılanması süreci TBMM\\\'de en az kaç milletvekilinin teklifiyle başlatılabilir?', 'Üye tamsayısının salt çoğunluğunun (301 vekil) önergesiyle', '150 vekil', '200 vekil', '360 vekil', '400 vekil', 'A', 'Teklif: 301 vekil, Soruşturma açılması kararı: 360 vekil (3/5), Yüce Divan\\\'a sevk kararı: 400 vekil (2/3) ile alınır.');
`;

const extra16 = `
    addQ(3, 16, 3, 'Merkezi idarenin taşra teşkilatında yalnızca il idaresine (vali) tanınan, merkeze danışmadan devlet adına karar alabilme yetkisine ne ad verilir?', 'Yetki Genişliği (Tevsi-i Mezuniyet)', 'Yetki Devri', 'İmza Devri', 'İdari Vesayet', 'Hiyerarşik Yetki', 'A', 'Yetki genişliği sadece İl İdaresinde Valiye tanınmıştır. Vali harcama yapamaz, gelir toplayamaz ama kamu düzeni kararlarını merkez adına re\\\'sen alır.');
    addQ(3, 16, 3, 'Devlet veya kamu tüzel kişilerinin kamu yararı amacıyla özel mülkiyette bulunan taşınmaz mallara bedelini peşin ödemek kaydıyla el koymasına ne ad verilir?', 'Kamulaştırma (İstimlak)', 'İstimval', 'Devletleştirme', 'Müsadere', 'Kamulaştırmasız El Atma', 'A', 'Kamulaştırma taşınmazlara peşin bedelle el koymadır. Taşınır mallara el koymaya ise istimval denir.');
    addQ(3, 16, 3, 'İdarenin hukuki sorumluluğunda idarenin hiçbir kusuru bulunmasa dahi ortaya çıkan zararı tazmin etmesini gerektiren ilkelere ne ad verilir?', 'Kusursuz Sorumluluk (Risk ve Fedakarlığın Denkleştirilmesi)', 'Hizmet Kusuru', 'Kişisel Kusur', 'Ağır İhmal', 'Görev Kusuru', 'A', 'İdarenin tehlike yaratan faaliyetlerinde (risk) veya kamu yararına fedakarlık durumunda kusuru olmasa da zarar tazmin edilir.');
    addQ(3, 16, 3, 'İdari yargıda kural olarak genel iptal ve tam yargı davası açma süresi İdare Mahkemelerinde ve Danıştay\\\'da kaç gündür?', '60 gün', '30 gün', '15 gün', '90 gün', '1 yıl', 'A', 'İYUK m. 7 uyarınca dava açma süresi Danıştay ve İdare Mahkemelerinde 60 gün, Vergi Mahkemelerinde ise 30 gündür.');
    addQ(3, 16, 3, 'Kamu Denetçiliği Kurumu (Ombudsmanlık) kime bağlı olarak çalışır ve Başdenetçiyi kim seçer?', 'TBMM Başkanlığına bağlıdır - Başdenetçiyi TBMM seçer', 'Cumhurbaşkanlığına bağlıdır - CB seçer', 'Adalet Bakanlığına bağlıdır - HSK seçer', 'Danıştay\\\'a bağlıdır - Danıştay seçer', 'İçişleri Bakanlığına bağlıdır', 'A', 'Kamu Denetçiliği TBMM Başkanlığına bağlı olup idarenin her türlü eylem ve işlemini insan hakları yönünden inceler.');
`;

const extra17 = `
    addQ(3, 17, 3, 'Birleşmiş Milletler (BM) Güvenlik Konseyi\\\'nde veto yetkisine sahip 5 daimi üye ülke (FÇİRA) aşağıdakilerin hangisinde tam olarak verilmiştir?', 'Fransa, Çin, İngiltere, Rusya, ABD', 'Almanya, Çin, Rusya, ABD, Japonya', 'Türkiye, ABD, Rusya, İngiltere, Fransa', 'Fransa, İtalya, İngiltere, Çin, ABD', 'Kanada, ABD, Rusya, İngiltere, Çin', 'A', 'BM Güvenlik Konseyi\\\'nin veto hakkı bulunan 5 daimi üyesi FÇİRA kısaltmasıyla bilinen Fransa, Çin, İngiltere, Rusya ve ABD\\\'dir.');
    addQ(3, 17, 3, 'Kuzey Atlantik Antlaşması Örgütü (NATO) genel merkezi nerede bulunmaktadır ve Türkiye hangi yıl örgüte üye olmuştur?', 'Brüksel (Belçika) - 1952 yılında', 'Cenevre - 1949 yılında', 'New York - 1950 yılında', 'Londra - 1955 yılında', 'Paris - 1960 yılında', 'A', 'NATO 1949\\\'da kurulmuş, genel merkezi Brüksel\\\'dedir. Türkiye Kore Savaşı\\\'ndaki başarısının ardından 1952 yılında Yunanistan ile birlikte üye olmuştur.');
    addQ(3, 17, 3, 'Avrupa İnsan Hakları Mahkemesi (AİHM) hangi uluslararası kuruluşun bünyesinde faaliyet gösterir ve merkezi neresidir?', 'Avrupa Konseyi bünyesindedir - Strazburg (Fransa)', 'Avrupa Birliği bünyesinde - Brüksel', 'Birleşmiş Milletler bünyesinde - Cenevre', 'Lahey Adalet Divanı - Hollanda', 'UNESCO - Paris', 'A', 'AİHM, 1949\\\'da kurulan Avrupa Konseyi\\\'nin yargı organıdır ve Strazburg\\\'da bulunur.');
    addQ(3, 17, 3, 'Türkiye\\\'nin ev sahipliğinde İstanbul\\\'da kurulan ve 8 gelişmekte olan Müslüman ülkenin oluşturduğu ekonomik işbirliği örgütü hangisidir?', 'D-8 (Gelişen Sekiz Ülke)', 'G-20', 'OPEC', 'Şanghay İşbirliği Örgütü', 'Arap Birliği', 'A', 'D-8, 1997 yılında Necmettin Erbakan öncülüğünde İstanbul\\\'da kurulmuştur (Türkiye, İran, Pakistan, Bangladeş, Malezya, Endonezya, Mısır, Nijerya).');
    addQ(3, 17, 3, 'UNESCO Dünya Kültür Mirası Listesi\\\'nde yer alan ve \\\'Tarihin Sıfır Noktası\\\' olarak adlandırılan dünyanın en eski tapınak kompleksi Göbeklitepe hangi ilimizdedir?', 'Şanlıurfa', 'Gaziantep', 'Mardin', 'Diyarbakır', 'Adıyaman', 'A', 'Göbeklitepe MÖ 10.000\\\'e dayanan ve Klaus Schmidt tarafından kazılan Şanlıurfa ilimizdeki neolitik tapınak kompleksidir.');
`;

// Insert subcat 13
p1 = p1.replace(/(addQ\(3, 13, 3, 'Kişiye sıkı sıkıya bağlı haklar[\s\S]*?\);)/, '$1\n' + extra13);

// Insert subcat 14
p1 = p1.replace(/(addQ\(3, 14, 3, 'Bireysel Başvuru hakkı[\s\S]*?\);)/, '$1\n' + extra14);

// Insert subcat 15
p1 = p1.replace(/(addQ\(3, 15, 3, 'Cumhurbaşkanlığı Kararnameleri \(CBK\)[\s\S]*?\);)/, '$1\n' + extra15);

// Insert subcat 16
p2 = p2.replace(/(addQ\(3, 16, 3, 'Türkiye Radyo ve Televizyon Üst Kurulu[\s\S]*?\);)/, '$1\n' + extra16);

// Insert subcat 17
p2 = p2.replace(/(addQ\(3, 17, 3, 'Şanghay[\s\S]*?\);)/, '$1\n' + extra17);

const body1 = p1.replace(/module\.exports\s*=\s*function\s*\(addQ\)\s*\{/, '').replace(/\};\s*$/, '');
const body2 = p2.replace(/module\.exports\s*=\s*function\s*\(addQ\)\s*\{/, '').replace(/\};\s*$/, '');

const combined = '// KPSS Vatandaşlık Complete Bank (150 Questions - 5 Subcategories, 3 Levels, 10 Q per level)\nmodule.exports = function (addQ) {\n' + body1 + '\n' + body2 + '\n};\n';
fs.writeFileSync('d:/quiza/seed_kpss/kpss_vatandaslik.js', combined, 'utf8');
console.log('kpss_vatandaslik.js created successfully.');
