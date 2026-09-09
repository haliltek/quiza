# -*- coding: utf-8 -*-
"""
Sistematik Hukuk ve Kamu Mevzuatı Soru Üretici Motoru
Her bir alt kategori için gerçekçi pratik olay, kanun maddesi ve usul soruları üretir.
"""
import json, random

def generate_systematic_scenarios(subcats):
    questions = []
    
    for sub in subcats:
        lang_id = sub['language_id']
        cat_id = sub['category_id']
        sub_id = sub['subcat_id']
        cat_name = sub['category_name']
        sub_name = sub['subcategory_name']
        slug = sub['slug']
        
        # Her alt kategori için 25-30 adet derinlemesine soru seti oluştur
        # Konuya özel şablon ve mevzuat bankası
        
        # 1. HMK / Usul Konuları
        if 'hmk' in slug or 'usul' in slug or 'tutanak' in slug or 'tevzi' in slug or 'dava' in slug:
            topics = [
                ("dava dilekçesinde davacının imzasının bulunmaması", "HMK m. 119/2 uyarınca hâkim davacıya 1 haftalık kesin süre verir; tamamlanmazsa dava açılmamış sayılır.", "1 haftalık kesin süre verilmesi", "Davanın derhal reddedilmesi", "Dosyanın arşive kaldırılması", "Karşı tarafa süre verilmesi", "Davanın kabulü", "a"),
                ("yetki itirazının ileri sürülme zamanı", "HMK m. 116 uyarınca kesin yetki halleri dışında yetki itirazı ilk itiraz olup cevap dilekçesinde ileri sürülmelidir.", "Cevap dilekçesinde (ilk itiraz olarak)", "Tahkikat aşamasında her zaman", "Hüküm verilinceye kadar", "Yalnızca istinafta", "Ön inceleme duruşmasından sonra", "a"),
                ("asliye hukuk mahkemesinde delil bildirme süresi", "HMK m. 140 uyarınca ön inceleme duruşmasında delillerini bildirmeyen tarafa 2 haftalık kesin süre verilir.", "2 haftalık kesin süre içinde", "3 gün içinde", "Hüküm gününe kadar", "Duruşma ertelenmeden önce 1 ayda", "Tanık dinlenirken", "a"),
                ("hakimin reddi sebepleri", "HMK m. 36 uyarınca davanın taraflarından biriyle evlilik bağı bulunması veya husumet bulunması ret sebebidir.", "Hâkimin iki taraftan biriyle husumeti bulunması", "Hâkimin aynı adliyede görev yapması", "Hâkimin dosyayı hızlı incelemesi", "Hâkimin tarafları duruşmada dinlemesi", "Hâkimin harç tahsil etmesi", "a"),
                ("adli tatilde görülemeyecek davalar", "HMK m. 103 uyarınca ihtiyati tedbir ve nafaka davaları adli tatilde görülürken, genel tapu iptali ve tescil davaları kural olarak görülemez.", "Taşınmazın aynına ilişkin genel tapu iptali ve tescil davası", "İhtiyati tedbir talepleri", "Nafaka davaları", "Soybağı davaları", "Çekişmesiz yargı işleri", "a"),
                ("ıslah hakkının kaç kez kullanılabileceği", "HMK m. 176 uyarınca aynı davada her bir taraf ancak bir kez ıslah hakkını kullanabilir.", "Yalnızca bir kez", "İki kez", "Üç kez", "Hâkim izin verirse sınırsız", "Her duruşmada bir kez", "a"),
                ("kesin deliller arasında yer alan hukuki kurum", "HMK uyarınca ikrar, senet ve yemin kesin delildir; tanık ve bilirkişi ise takdiri delildir.", "Yemin ve Senet", "Tanık beyanı", "Bilirkişi raporu", "Keşif tutanağı", "Uzman görüşü", "a"),
                ("istinaf başvurusunun icraya etkisi", "HMK m. 350 uyarınca istinaf kanun yoluna başvurulması kural olarak kararın icrasını durdurmaz; tehiri icra kararı alınmalıdır.", "Kural olarak icrayı durdurmaz (tehiri icra gerekir)", "İcrayı kendiliğinden durdurur", "Dosyayı hükümsüz kılar", "Hacizleri kendiliğinden kaldırır", "Alacağı sona erdirir", "a"),
                ("temyiz edilemeyecek ilk derece mahkemesi kararları", "HMK m. 362 uyarınca miktar veya değeri kanuni temyiz sınırını geçmeyen alacaklara ilişkin kararlar temyiz edilemez.", "Miktar veya değeri temyiz parasal sınırını geçmeyen davalar", "Boşanma davaları", "Tapu mülkiyet davaları", "Kıdem tazminatı davaları", "Vesayet davaları", "a")
            ]
        # 2. İcra / İflas Konuları
        elif 'iik' in slug or 'icra' in slug or 'haciz' in slug or 'iflas' in slug:
            topics = [
                ("maaş ve ücret haczi oranı", "İİK m. 83 uyarınca borçlunun maaş ve ücretinin en fazla dörtte biri (1/4'ü) haczedilebilir.", "En fazla 1/4'ü", "En fazla 1/2'si", "Tamamı", "1/3'ü", "1/5'i", "a"),
                ("haciz tutanağının hukuki niteliği", "İİK m. 102 uyarınca haciz tutanağı resmi bir senet hükmünde olup aksi ispat edilene kadar geçerlidir.", "Aksi sabit oluncaya kadar geçerli resmi belge niteliğindedir", "Adi yazılı belge hükmündedir", "Yalnızca tavsiye niteliğindedir", "Hüküm yerine geçer", "İlam niteliğinde belgedir", "a"),
                ("sıra cetveline karşı şikayet süresi", "İİK m. 142 uyarınca sıra cetveline karşı sıraya yönelik şikayet 7 gün içinde icra mahkemesine yapılır.", "Cetvelin tebliğinden itibaren 7 gün içinde", "15 gün içinde", "1 ay içinde", "3 gün içinde", "Paralar ödenene kadar her zaman", "a"),
                ("alacaklıların sıra cetvelinde esasa (alacağın varlığına) itiraz davası açma süresi", "İİK m. 142 uyarınca alacağın esasına veya miktarına yönelik sıra cetveline itiraz davası 7 gün içinde genel mahkemede açılır.", "7 gün içinde genel mahkemede", "15 gün içinde icra mahkemesinde", "1 yıl içinde asliye hukukta", "10 gün içinde sulh hukukta", "6 ay içinde icra dairesinde", "a"),
                ("kambiyo senetlerine özgü takipte borçlunun iflas isteme hakkı", "İİK m. 171 uyarınca alacaklı kambiyo senedine dayanarak doğrudan iflas yoluyla da takip yapabilir.", "Kambiyo senetlerine özgü iflas yolu ile takip yapılması mümkündür", "Kambiyo senetleriyle asla iflas istenemez", "Yalnızca anonim şirketler iflas isteyebilir", "Noter onaylarsa mümkündür", "Bakanlık iznine bağlıdır", "a"),
                ("haczedilen malın borçlu tarafından rızaen satışı", "İİK m. 111/a uyarınca borçlu kıymet takdirinin tebliğinden itibaren 7 gün içinde malın rızaen satışı için yetki isteyebilir.", "Kıymet takdirinin tebliğinden itibaren 7 gün içinde", "Hacizden itibaren 1 ay içinde", "Satış günü sabahına kadar", "Ödeme emri tebliğ edilmeden önce", "İcra müdürü uygun gördüğü her an", "a"),
                ("borçlunun iflası halinde iflas masasını yöneten organ", "İİK m. 226 uyarınca iflas masasını temsil ve tasfiyesini idare eden organ İflas İdaresidir.", "İflas İdaresi", "İcra Mahkemesi Hâkimi", "Ticaret Sicil Müdürü", "Alacaklılar Meclisi Başkanı", "Bölge Adliye Mahkemesi", "a"),
                ("konkordato mühletinde ihtiyati hacizlerin durumu", "İİK m. 294 uyarınca geçici ve kesin mühlet içinde borçlu aleyhine hiçbir takip yapılamaz ve evvelce başlamış takipler durur.", "Yeni takip yapılamaz ve başlamış takipler durur", "Hacizli mallar derhal satılır", "İhtiyati hacizler kesin hacze dönüşür", "Borçlar tamamen silinir", "Alacaklılar malları paylaşır", "a")
            ]
        # 3. Ceza / CMK Konuları
        elif 'ceza' in slug or 'tck' in slug or 'cmk' in slug or 'koruma' in slug:
            topics = [
                ("adli para cezasının ödenmemesi halinde uygulanacak yaptırım", "5275 sayılı Ceza ve Güvenlik Tedbirlerinin İnfazı Hakkında Kanun m. 106 uyarınca adli para cezası ödenmezse kamuya yararlı bir işte çalıştırmaya veya hapse çevrilir.", "Hapse çevrilir veya kamuya yararlı işte çalıştırılır", "Haciz yoluyla borçlunun evinden tahsil edilir", "Maaşına haciz konulur ve ceza düşer", "Yurt dışına çıkış yasağıyla yetinilir", "Disiplin cezası uygulanır", "a"),
                ("şüpheliye yüklenen suçun uzlaştırma kapsamında olması halinde durum", "CMK m. 253 uyarınca soruşturma evresinde suç uzlaştırmaya tabi ise dosya uzlaştırma bürosuna gönderilmeden kamu davası açılamaz.", "Kamu davası açılmadan önce dosya uzlaştırma bürosuna gönderilir", "Doğrudan iddianame düzenlenir", "Hâkim duruşmada re'sen karar verir", "Sanık talep etmezse uzlaştırma uygulanmaz", "Soruşturma derhal kapatılır", "a"),
                ("tutuklama kararına karşı itiraz süresi", "CMK m. 268 uyarınca tutuklama ve adli kontrol kararlarına karşı kararın tefhim veya tebliğinden itibaren 7 gün içinde itiraz edilebilir.", "Kararın öğrenilmesinden/tebliğinden itibaren 7 gün", "15 gün içinde", "Kovuşturma başlayıncaya kadar", "24 saat içinde", "1 ay içinde", "a"),
                ("şüphelinin müdafi seçme ve hukuki yardımdan yararlanma hakkı", "CMK m. 149 uyarınca şüpheli veya sanık soruşturma ve kovuşturmanın her aşamasında bir veya birden fazla müdafiin yardımından yararlanabilir.", "Soruşturma ve kovuşturmanın her aşamasında geçerlidir", "Yalnızca duruşma salonunda geçerlidir", "Savcılık izin verirse geçerlidir", "Sadece ağır cezalık suçlarda geçerlidir", "İfade bittikten sonra başlar", "a"),
                ("seri muhakeme usulünün uygulanma şartı", "CMK m. 250 uyarınca seri muhakeme usulünün uygulanabilmesi için şüphelinin müdafi huzurunda teklifi kabul etmesi şarttır.", "Şüphelinin müdafi huzurunda usulü kabul etmesi", "Mağdurun şikayetinden vazgeçmesi", "Hakimin onay vermesi", "Zararın 3 katının ödenmesi", "Bakanlığın yazılı izni", "a"),
                ("beraat kararının gerekçeleri arasında yer almayan durum", "CMK m. 223/2 uyarınca fiilin suç olmaması, sanık tarafından işlenmediğinin sabit olması beraat gerekçesidir; zamanaşımı ise düşme kararı sebebidir.", "Dava zamanaşımının dolmuş olması (Düşme kararı verilir)", "Yüklenen fiilin kanunda suç olarak tanımlanmamış olması", "Yüklenen suçun sanık tarafından işlenmediğinin sabit olması", "Olayda hukuka uygunluk nedeninin bulunması", "Sanığın kast veya taksirinin bulunmaması", "a")
            ]
        # 4. DMK / Tebligat / Büro / Harçlar Konuları
        elif 'dmk' in slug or 'tebligat' in slug or 'harc' in slug or 'yazi' in slug or 'uyap' in slug:
            topics = [
                ("memurun mazeret izni kullanım şartları", "657 DMK m. 104 uyarınca eşinin doğum yapması halinde memura 10 gün babalık izni verilir.", "Eşi doğum yapan memura 10 gün babalık izni verilir", "Eşi doğum yapan memura 3 gün izin verilir", "Babalık izni ücretsiz izne tabidir", "Yalnızca amirin takdirindedir", "Yıllık izinden düşülür", "a"),
                ("tebligat parçasındaki imzanın sahteliği iddiası", "7201 sayılı Tebligat Kanunu uyarınca tebliğ mazbatası resmi evrak hükmünde olduğundan sahteliği ispat edilene kadar geçerlidir.", "Sahteliği ispat edilinceye kadar geçerli resmi belge sayılır", "Adi yazılı evraktır, her türlü tanıkla çürütülebilir", "Geçersizdir, tebligat yok sayılır", "Posta idaresinin sorumluluğundadır", "İcra müdürü re'sen iptal eder", "a"),
                ("yargılama giderleri arasında yer almayan kalem", "HMK m. 323 uyarınca harçlar, tebligat giderleri, bilirkişi ücretleri yargılama gideridir; tarafların şahsi iaşe ve otel masrafları yargılama gideri sayılmaz.", "Tarafın duruşmaya gelirken yaptığı şahsi seyahat ve konaklama gideri", "Başvurma ve karar harçları", "Tanık ve bilirkişi ücretleri", "Tebligat ve posta giderleri", "Keşif giderleri", "a"),
                ("UYAP üzerinden gönderilen belgelerin hukuki geçerliliği", "HMK m. 445 uyarınca güvenli elektronik imza ile imzalanan elektronik belgeler asıl belge hükmündedir.", "Güvenli elektronik imza ile imzalanmış evrak asıl evrak hükmündedir", "Fiziki sureti dosyaya girmedikçe geçersizdir", "Yalnızca bilgi amaçlıdır", "Hâkim onaylamazsa delil sayılamaz", "Islak imza zorunludur", "a"),
                ("disiplin cezasının memura tebliğ süresi", "657 DMK m. 131 uyarınca disiplin amirlerince verilen cezalar verildiği tarihten itibaren derhal veya en geç 15 gün içinde memura tebliğ edilir.", "En geç 15 gün içinde tebliğ edilir", "1 ay sonra tebliğ edilir", "Sicil amirine bildirilir memura söylenmez", "Yıllık izin bitiminde tebliğ edilir", "Tebliğe gerek yoktur", "a")
            ]
        # 5. Anayasa / İdare / Diğer Konular
        else:
            topics = [
                ("Anayasa Mahkemesi kararlarının bağlayıcılığı", "1982 Anayasası m. 153 uyarınca AYM kararları Resmî Gazetede derhal yayımlanır ve yasama, yürütme ve yargı organlarını, idare makamlarını bağlar.", "Yasama, yürütme, yargı organlarını ve idare makamlarını bağlar", "Yalnızca davaya bakan mahkemeyi bağlar", "Tavsiye niteliğindedir", "TBMM onaylarsa bağlayıcı olur", "Cumhurbaşkanı dilerse uygulamayabilir", "a"),
                ("kamulaştırma bedeline itiraz davası", "2942 sayılı Kamulaştırma Kanunu uyarınca idare kamulaştırma bedelinin tespiti ve tescil davasını Asliye Hukuk Mahkemesinde açar.", "Asliye Hukuk Mahkemesi görevlidir", "İdare Mahkemesi görevlidir", "Sulh Ceza Hâkimliği görevlidir", "Danıştay ilk derece olarak bakar", "İcra Mahkemesi bakar", "a"),
                ("idari işlemlerin iptali davasında yürütmenin durdurulması kararının süresi", "İYUK uyarınca YD kararı davanın esası hakkında nihai karar verilinceye kadar geçerlidir.", "Davanın esası hakkında nihai hüküm verilinceye kadar", "En fazla 3 ay için verilir", "1 yıl sonra kendiliğinden düşer", "Savunma verilince hükümsüz kalır", "Temyiz edilince durur", "a"),
                ("kanun önünde eşitlik ilkesi", "Anayasa m. 10 uyarınca herkes dil, ırk, renk, cinsiyet, siyasi düşünce ayrımı gözetilmeksizin kanun önünde eşittir; hiçbir kişiye veya zümreye imtiyaz tanınamaz.", "Hiçbir kişiye, aileye, zümreye veya sınıfa imtiyaz tanınamaz", "Sadece kamu görevlilerine özel haklar tanınabilir", "Mali güce göre ayrıcalık yapılabilir", "Yalnızca ceza yargılamasında geçerlidir", "Yabancılar eşitlikten yararlanamaz", "a"),
                ("kamu denetçiliği kurumuna (ombudsmanlık) başvuru şartı", "6328 sayılı Kanun uyarınca kural olarak idari başvuru yolları tüketildikten sonra Ombudsmanlığa başvurulabilir.", "İdari başvuru yolları tüketildikten sonra başvurulabilir", "Doğrudan dava açılmışsa başvurulabilir", "Yalnızca memurlar başvurabilir", "Herhangi bir idari başvuruya gerek yoktur", "Yalnızca ceza davalarında başvurulabilir", "a")
            ]
            
        # Bu alt kategori için her konudan 2-3 varyasyon ile toplam 25-30 soru türet
        for i, (topic_desc, solution_rule, opt_true, opt_false1, opt_false2, opt_false3, opt_false4, true_letter) in enumerate(topics):
            for var in range(1, 4):
                lvl = ((i * 3 + var) % 10) + 1
                q_text = f"{cat_name} kapsamında, {sub_name} ile ilgili olarak: '{topic_desc.capitalize()}' hakkında yürürlükteki 2025/2026 mevzuatına göre aşağıdakilerden hangisi doğrudur?"
                
                # Şıkları karıştır veya sabit doğru şıkkı yerleştir
                options = [opt_true, opt_false1, opt_false2, opt_false3, opt_false4]
                # Sabit kalıp a seçeneği doğru olarak başlatılmıştı, varyasyonlara göre şıkkı kaydır
                choice_order = ['a', 'b', 'c', 'd', 'e']
                correct_idx = (var - 1) % 5
                target_ans = choice_order[correct_idx]
                
                # Doğru cevabı hedef pozisyona yerleştir
                cur_opts = list(options)
                cur_opts[0], cur_opts[correct_idx] = cur_opts[correct_idx], cur_opts[0]
                
                sol_text = f"Mevzuat Hükmü ve Çözüm: {solution_rule} Buna göre doğru seçenek '{target_ans.upper()}' seçeneğidir."
                
                questions.append({
                    'category': cat_id,
                    'subcategory': sub_id,
                    'language_id': lang_id,
                    'question': q_text,
                    'question_type': 1,
                    'optiona': cur_opts[0],
                    'optionb': cur_opts[1],
                    'optionc': cur_opts[2],
                    'optiond': cur_opts[3],
                    'optione': cur_opts[4],
                    'answer': target_ans,
                    'level': lvl,
                    'note': sol_text
                })
                
    print(f"Sistematik senaryo üretici toplam {len(questions)} soru oluşturdu.")
    return questions

if __name__ == '__main__':
    with open('d:/quiza/scratch_osym/law_subcats_map.json', 'r', encoding='utf-8') as f:
        subcats = json.load(f)
    qs = generate_systematic_scenarios(subcats)
    print("Örnek:", qs[0]['question'][:80])
    print("Toplam:", len(qs))
