import subprocess

questions = [
    {
        'q': '[Yargı KPSS Deneme 15]\n\nKişilerin haysiyet ve şereflerine dokunulması veya kendileriyle ilgili gerçeğe aykırı yayınlar yapılması hallerinde tanınan hakka ne ad verilir?',
        'a': 'Düzeltme ve cevap hakkı',
        'b': 'Süreli ve süresiz yayın hakkı',
        'c': 'Hak arama hürriyeti',
        'd': 'Basın hürriyeti',
        'e': 'İspat hakkı',
        'ans': 'a',
        'note': 'Anayasa m.32: Düzeltme ve cevap hakkı, ancak kişilerin haysiyet ve şereflerine dokunulması veya kendileriyle ilgili gerçeğe aykırı yayınlar yapılması hallerinde tanınır ve kanunla düzenlenir.'
    },
    {
        'q': '[Yargı KPSS Deneme 15]\n\nAşağıdakilerden hangisi 1982 Anayasası\'nın 2. maddesinde sayılan Cumhuriyetin niteliklerinden biri değildir?',
        'a': 'Sosyal Devlet',
        'b': 'İnsan Haklarına Saygılı Devlet',
        'c': 'Demokratik Devlet',
        'd': 'Türk Milliyetçiliğine Bağlı Devlet',
        'e': 'Hukuk Devleti',
        'ans': 'd',
        'note': '1982 Anayasası m.2\'ye göre Türkiye Cumhuriyeti, toplumun huzuru, millî dayanışma ve adalet anlayışı içinde, insan haklarına saygılı, Atatürk milliyetçiliğine bağlı, demokratik, lâik ve sosyal bir hukuk devletidir.'
    },
    {
        'q': '[Yargı KPSS Deneme 15]\n\nCumhurbaşkanı tarafından meclise iade edilen anayasa değişikliğine ilişkin kanunların, anayasa değişikliği sürecinin devam edebilmesi için meclis tarafından en az ne kadar çoğunluk ile kabul edilmesi gerekir?',
        'a': '1/3',
        'b': '2/3',
        'c': '3/5',
        'd': '2/4',
        'e': '1/5',
        'ans': 'c',
        'note': 'Anayasa değişikliği kanunları Cumhurbaşkanı tarafından geri gönderilirse meclis en az beşte üç (3/5) çoğunlukla aynen kabul edebilir.'
    },
    {
        'q': '[Yargı KPSS Deneme 15]\n\n1982 Anayasası\'na göre TBMM\'nin toplantı yeter sayısı ile ilgili aşağıdaki bilgilerden hangisi doğrudur?',
        'a': 'TBMM yapacağı seçimler dâhil bütün işlerinde üye tamsayısının en az 1/3\'ü ile toplanır',
        'b': 'TBMM, üye tamsayısının salt çoğunluğu ile toplanır',
        'c': 'TBMM\'nin toplantı yeter sayısı üye tamsayısının 1/4\'ünün bir fazlasıdır',
        'd': 'TBMM, üye tamsayısının 2/3\'ü ile toplanır',
        'e': 'Meclisin toplantı yeter sayısı 139\'dur',
        'ans': 'a',
        'note': 'Anayasa m.96: TBMM, yapacağı seçimler dahil bütün işlerinde üye tamsayısının en az üçte biri (1/3) ile toplanır.'
    },
    {
        'q': '[Yargı KPSS Deneme 15]\n\nTüzükler ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        'a': 'Bakanlıklar ve kamu tüzel kişilerinin tüzük çıkarma yetkisi yoktur',
        'b': 'Danıştay incelemesinden geçirilmemiş olan bir tüzük hiç yapılmamış sayılır',
        'c': 'Tüzüğün daha önce yürürlüğe girmiş bulunan bir kanuna dayanması zorunludur',
        'd': 'Tüzükler bir idari işlemdir',
        'e': 'Tüzüklerin yargısal denetimi Anayasa Mahkemesi\'nce yapılmaktadır',
        'ans': 'e',
        'note': 'Tüzüklerin yargısal denetimi Anayasa Mahkemesi değil, Danıştay (idari yargı) tarafından yapılmaktaydı.'
    },
    {
        'q': '[Yargı KPSS Deneme 15]\n\nDevlet veya kamu tüzel kişilerinin, kamu yararının gerektirdiği durumlarda, karşılığının peşin ödenmesi koşuluyla, özel mülkiyette bulunan taşınmaz malların tamamına veya bir kısmına el koymasına ne ad verilir?',
        'a': 'İstimval',
        'b': 'Geçici işgal',
        'c': 'Kamulaştırma',
        'd': 'İstikraz',
        'e': 'Devletleştirme',
        'ans': 'c',
        'note': 'Anayasa m.46: Kamulaştırma, kamu yararının gerektirdiği hallerde özel mülkiyetteki taşınmazlara bedeli peşin ödenmek şartıyla el konulmasıdır. Taşınırlar için yapılan ise istimvaldir.'
    },
    {
        'q': '[Yargı KPSS Deneme 15]\n\nAşağıdakilerden hangisi yasama yetkisinin asliliği (ilk-el olması) ilkesini ifade eder?',
        'a': 'Yasama organının dilediği konuda ve istediği kadar ayrıntıya girerek düzenleme yapabilmesi',
        'b': 'Yasama organının bir konuyu araya başka bir işlem girmeksizin doğrudan doğruya düzenleyebilmesi',
        'c': 'Yasama organının parlamento kararları alma yetkisi',
        'd': 'Yasama yetkisinin Türk milleti adına TBMM\'ye ait olması',
        'e': 'Yasama organının hükümeti denetleme yetkisinin bulunması',
        'ans': 'b',
        'note': 'Yasama yetkisinin asliliği (ilk-el oluşu), TBMM\'nin bir konuyu araya başka bir organın işlemi veya yetkilendirmesi girmeksizin doğrudan doğruya Anayasa\'ya dayanarak düzenleyebilmesidir.'
    },
    {
        'q': '[Yargı KPSS Deneme 15]\n\nTBMM, savaş nedeni ile seçimlerin yapılmasına olanak bulunmaması halinde seçimlerin kaç yıl ertelenmesine karar verebilir?',
        'a': '1 yıl',
        'b': '2 yıl',
        'c': '3 yıl',
        'd': '4 yıl',
        'e': '5 yıl',
        'ans': 'a',
        'note': 'Anayasa m.78: Savaş sebebiyle yeni seçimlerin yapılmasına imkân görülmezse, TBMM, seçimlerin bir yıl geriye bırakılmasına karar verebilir.'
    },
    {
        'q': '[Yargı KPSS Deneme 15]\n\n2007 yılını Mevlana, 2008 yılını Kaşgarlı Mahmut yılı olarak ilan eden uluslararası kuruluş aşağıdakilerden hangisidir?',
        'a': 'Avrupa Birliği',
        'b': 'UNESCO',
        'c': 'Avrupa Konseyi',
        'd': 'İslam Konferansı Örgütü',
        'e': 'OECD',
        'ans': 'b',
        'note': 'UNESCO, 2007 yılını Mevlana Celaleddin Rumi, 2008 yılını ise Kaşgarlı Mahmut yılı ilan etmiştir.'
    },
    {
        'q': '[Yargı KPSS Deneme 15]\n\nAlmanya\'nın önde gelen müzik festivalleri arasında yer alan Bremen Müzik Festivali 2008 Ödülünü alan dünyaca ünlü Türk piyanist ve besteci aşağıdakilerden hangisidir?',
        'a': 'Fahir Atakoğlu',
        'b': 'Fazıl Say',
        'c': 'Tolga Özdemiroğlu',
        'd': 'Çetin Işıközlü',
        'e': 'İpek Mine Altınel',
        'ans': 'b',
        'note': 'Dünyaca ünlü piyanistimiz Fazıl Say, Bremen Müzik Festivali 2008 Müzik Ödülü\'ne layık görülmüştür.'
    }
]

sql_lines = []
for item in questions:
    q_esc = item['q'].replace("'", "\\'")
    a_esc = item['a'].replace("'", "\\'")
    b_esc = item['b'].replace("'", "\\'")
    c_esc = item['c'].replace("'", "\\'")
    d_esc = item['d'].replace("'", "\\'")
    e_esc = item['e'].replace("'", "\\'")
    note_esc = item['note'].replace("'", "\\'")
    ans = item['ans']
    
    sql = f"INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, level, note) VALUES (32, 0, 52, '', '{q_esc}', 1, '{a_esc}', '{b_esc}', '{c_esc}', '{d_esc}', '{e_esc}', '{ans}', 1, '{note_esc}');"
    sql_lines.append(sql)

full_sql = '\n'.join(sql_lines)
with open('d:/quiza/scratch_osym/insert_yargi_kpss.sql', 'w', encoding='utf-8') as f:
    f.write(full_sql)

print(f"Created SQL file with {len(questions)} questions.")

# Upload and execute on remote DB
cmd_scp = ['scp', '-o', 'StrictHostKeyChecking=no', 'd:/quiza/scratch_osym/insert_yargi_kpss.sql', 'root@142.93.104.78:/tmp/insert_yargi_kpss.sql']
subprocess.run(cmd_scp, check=True)

cmd_sql = ['ssh', '-o', 'StrictHostKeyChecking=no', 'root@142.93.104.78', 'docker exec -i elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db < /tmp/insert_yargi_kpss.sql']
res = subprocess.run(cmd_sql, capture_output=True, text=True)
print("MySQL execution:", res.stdout, res.stderr)
