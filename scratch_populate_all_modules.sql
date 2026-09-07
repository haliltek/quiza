
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- Ensure categories for all 6 types exist for KPSS Lisans (language_id = 52)

-- =========================================================================
-- TYPE 2: FUN 'N' LEARN CATEGORIES & SUBCATEGORIES
-- =========================================================================
INSERT INTO tbl_category (language_id, category_name, slug, type, is_premium, coins, has_level, image, row_order)
VALUES 
(52, 'KPSS Tarih Hap Bilgiler', 'kpss-tarih-hap-bilgiler', 2, 0, 0, 1, '', 1),
(52, 'KPSS Coğrafya Şifreleri', 'kpss-cografya-sifreleri', 2, 0, 0, 1, '', 2),
(52, 'KPSS Vatandaşlık Notları', 'kpss-vatandaslik-notlari', 2, 0, 0, 1, '', 3)
ON DUPLICATE KEY UPDATE category_name = VALUES(category_name);

SET @fnl_cat1 = (SELECT id FROM tbl_category WHERE language_id = 52 AND type = 2 AND slug = 'kpss-tarih-hap-bilgiler' LIMIT 1);
SET @fnl_cat2 = (SELECT id FROM tbl_category WHERE language_id = 52 AND type = 2 AND slug = 'kpss-cografya-sifreleri' LIMIT 1);
SET @fnl_cat3 = (SELECT id FROM tbl_category WHERE language_id = 52 AND type = 2 AND slug = 'kpss-vatandaslik-notlari' LIMIT 1);

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, is_premium, coins, has_level, row_order)
VALUES
(52, @fnl_cat1, 'İlk Türk Devletleri ve Teşkilat', 'fnl-ilk-turk-devletleri', 1, 0, 0, 1, 1),
(52, @fnl_cat1, 'Osmanlı Önemli Antlaşmalar', 'fnl-osmanli-antlasmalar', 1, 0, 0, 1, 2),
(52, @fnl_cat2, 'Türkiye Dağları ve Gölleri', 'fnl-turkiye-daglari', 1, 0, 0, 1, 1),
(52, @fnl_cat3, '1982 Anayasası Temel Maddeler', 'fnl-1982-anayasa', 1, 0, 0, 1, 1)
ON DUPLICATE KEY UPDATE subcategory_name = VALUES(subcategory_name);

-- =========================================================================
-- TYPE 3: GUESS THE WORD (KELİME TAHMİNİ) CATEGORIES & SUBCATEGORIES
-- =========================================================================
INSERT INTO tbl_category (language_id, category_name, slug, type, is_premium, coins, has_level, image, row_order)
VALUES 
(52, 'KPSS Tarih Kavramları', 'kpss-tarih-kavramlari', 3, 0, 0, 1, '', 1),
(52, 'KPSS Coğrafya Terimleri', 'kpss-cografya-terimleri', 3, 0, 0, 1, '', 2),
(52, 'KPSS Hukuk ve Anayasa Terimleri', 'kpss-hukuk-terimleri', 3, 0, 0, 1, '', 3)
ON DUPLICATE KEY UPDATE category_name = VALUES(category_name);

SET @gtw_cat1 = (SELECT id FROM tbl_category WHERE language_id = 52 AND type = 3 AND slug = 'kpss-tarih-kavramlari' LIMIT 1);
SET @gtw_cat2 = (SELECT id FROM tbl_category WHERE language_id = 52 AND type = 3 AND slug = 'kpss-cografya-terimleri' LIMIT 1);
SET @gtw_cat3 = (SELECT id FROM tbl_category WHERE language_id = 52 AND type = 3 AND slug = 'kpss-hukuk-terimleri' LIMIT 1);

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, is_premium, coins, has_level, row_order)
VALUES
(52, @gtw_cat1, 'Eski Türk ve Osmanlı Terimleri', 'gtw-eski-turk-osmanli', 1, 0, 0, 1, 1),
(52, @gtw_cat2, 'Yeryüzü Şekilleri ve İklim Terimleri', 'gtw-yeryuzu-sekilleri', 1, 0, 0, 1, 1),
(52, @gtw_cat3, 'Temel Hukuk ve Anayasa Kavramları', 'gtw-temel-hukuk', 1, 0, 0, 1, 1)
ON DUPLICATE KEY UPDATE subcategory_name = VALUES(subcategory_name);

-- =========================================================================
-- TYPE 5: MATHS QUESTION CATEGORIES & SUBCATEGORIES
-- =========================================================================
INSERT INTO tbl_category (language_id, category_name, slug, type, is_premium, coins, has_level, image, row_order)
VALUES 
(52, 'KPSS Temel Matematik', 'kpss-temel-matematik', 5, 0, 0, 1, '', 1),
(52, 'KPSS Sayısal Mantık & Problemler', 'kpss-sayisal-mantik-problemler', 5, 0, 0, 1, '', 2)
ON DUPLICATE KEY UPDATE category_name = VALUES(category_name);

SET @mq_cat1 = (SELECT id FROM tbl_category WHERE language_id = 52 AND type = 5 AND slug = 'kpss-temel-matematik' LIMIT 1);
SET @mq_cat2 = (SELECT id FROM tbl_category WHERE language_id = 52 AND type = 5 AND slug = 'kpss-sayisal-mantik-problemler' LIMIT 1);

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, is_premium, coins, has_level, row_order)
VALUES
(52, @mq_cat1, 'Sayılar ve Dört İşlem', 'mq-sayilar-dort-islem', 1, 0, 0, 1, 1),
(52, @mq_cat1, 'Rasyonel ve Ondalık Sayılar', 'mq-rasyonel-sayilar', 1, 0, 0, 1, 2),
(52, @mq_cat2, 'Yaş ve Yüzde Problemleri', 'mq-yas-yuzde-problemleri', 1, 0, 0, 1, 1),
(52, @mq_cat2, 'Hız ve Kar-Zarar Problemleri', 'mq-hiz-kar-zarar', 1, 0, 0, 1, 2)
ON DUPLICATE KEY UPDATE subcategory_name = VALUES(subcategory_name);

-- =========================================================================
-- TYPE 6: MULTI MATCH (KARMA EŞLEŞTİRME) CATEGORIES & SUBCATEGORIES
-- =========================================================================
INSERT INTO tbl_category (language_id, category_name, slug, type, is_premium, coins, has_level, image, row_order)
VALUES 
(52, 'KPSS Tarih Eşleştirmeleri', 'kpss-tarih-eslestirmeleri', 6, 0, 0, 1, '', 1),
(52, 'KPSS Coğrafya Eşleştirmeleri', 'kpss-cografya-eslestirmeleri', 6, 0, 0, 1, '', 2),
(52, 'KPSS Genel Kültür Eşleştirmeleri', 'kpss-genel-kultur-eslestirmeleri', 6, 0, 0, 1, '', 3)
ON DUPLICATE KEY UPDATE category_name = VALUES(category_name);

SET @mm_cat1 = (SELECT id FROM tbl_category WHERE language_id = 52 AND type = 6 AND slug = 'kpss-tarih-eslestirmeleri' LIMIT 1);
SET @mm_cat2 = (SELECT id FROM tbl_category WHERE language_id = 52 AND type = 6 AND slug = 'kpss-cografya-eslestirmeleri' LIMIT 1);
SET @mm_cat3 = (SELECT id FROM tbl_category WHERE language_id = 52 AND type = 6 AND slug = 'kpss-genel-kultur-eslestirmeleri' LIMIT 1);

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, is_premium, coins, has_level, row_order)
VALUES
(52, @mm_cat1, 'Savaşlar ve Tarihleri', 'mm-savaslar-tarihleri', 1, 0, 0, 1, 1),
(52, @mm_cat1, 'Hükümdarlar ve Olaylar', 'mm-hukumdar-olaylar', 1, 0, 0, 1, 2),
(52, @mm_cat2, 'Dağlar ve Bulunduğu Bölgeler', 'mm-daglar-bolgeler', 1, 0, 0, 1, 1),
(52, @mm_cat3, 'Uluslararası Örgütler ve Merkezleri', 'mm-orgutler-merkezleri', 1, 0, 0, 1, 1)
ON DUPLICATE KEY UPDATE subcategory_name = VALUES(subcategory_name);

-- =========================================================================
-- INSERT MATHS QUESTIONS (tbl_maths_question)
-- =========================================================================
SET @mq_sub1 = (SELECT id FROM tbl_subcategory WHERE language_id = 52 AND maincat_id = @mq_cat1 LIMIT 1);

INSERT INTO tbl_maths_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note)
VALUES
(@mq_cat1, @mq_sub1, 52, '', 'Ardışık 5 tek sayının toplamı 85 olduğuna göre bu sayıların en büyüğü kaçtır?', 1, '21', '19', '17', '23', '25', 'a', 'Ortanca sayı 85 / 5 = 17. Sayılar: 13, 15, 17, 19, 21.'),
(@mq_cat1, @mq_sub1, 52, '', 'Bir sayının 3 katının 5 eksiği 40 olduğuna göre bu sayı kaçtır?', 1, '15', '12', '18', '20', '14', 'a', '3x - 5 = 40 => 3x = 45 => x = 15.'),
(@mq_cat1, @mq_sub1, 52, '', 'Bir sınıftaki öğrencilerin %60ı erkektir. 12 kız olduğuna göre sınıf mevcudu kaçtır?', 1, '30', '25', '35', '40', '50', 'a', 'Kızlar %40. 0.40 * x = 12 => x = 30.'),
(@mq_cat1, @mq_sub1, 52, '', 'Bir babanın yaşı oğlunun yaşının 4 katıdır. 5 yıl sonra 3 katı olacağına göre çocuk bugün kaç yaşındadır?', 1, '10', '8', '12', '14', '15', 'a', '4x + 5 = 3(x + 5) => x = 10.'),
(@mq_cat1, @mq_sub1, 52, '', '200 TL maliyetli bir ürün %30 kârla kaç TLye satılır?', 1, '260 TL', '230 TL', '250 TL', '270 TL', '280 TL', 'a', '200 * 1.30 = 260 TL.');

-- =========================================================================
-- INSERT FUN 'N' LEARN (tbl_fun_n_learn & tbl_fun_n_learn_question)
-- =========================================================================
SET @fnl_sub1 = (SELECT id FROM tbl_subcategory WHERE language_id = 52 AND maincat_id = @fnl_cat1 LIMIT 1);

INSERT INTO tbl_fun_n_learn (language_id, category, subcategory, title, detail, status, content_type, content_data)
VALUES
(52, @fnl_cat1, @fnl_sub1, 'İslamiyet Öncesi Türk Devlet Teşkilatı', 'İslamiyet öncesi Türk devletlerinde devlet hükümdar ve ailesinin ortak malı sayılırdı (Kut Anlayışı). Hükümdarın erkek çocuklarına Tigin denirdi. Devlet işleri Kurultay (Toy) adı verilen mecliste görüşülürdü. Kurultaya boy beyleri ve Hatun da katılırdı. Ordu onluk sisteme göre teşkilatlanmıştı.', 1, 0, '');

SET @fnl_id = LAST_INSERT_ID();

INSERT INTO tbl_fun_n_learn_question (fun_n_learn_id, question, question_type, optiona, optionb, optionc, optiond, optione, answer, image)
VALUES
(@fnl_id, 'Türk devletlerinde hükümdarın erkek çocuklarına verilen unvan nedir?', 1, 'Tigin', 'Şad', 'Yabgu', 'Atabey', 'Melik', 'a', ''),
(@fnl_id, 'Devlet işlerinin görüşülüp karara bağlandığı meclise ne ad verilir?', 1, 'Kurultay (Toy)', 'Divan', 'Pankuş', 'Senato', 'Meclis-i Mebusan', 'a', '');

-- =========================================================================
-- INSERT GUESS THE WORD (tbl_guess_the_word)
-- =========================================================================
SET @gtw_sub1 = (SELECT id FROM tbl_subcategory WHERE language_id = 52 AND maincat_id = @gtw_cat1 LIMIT 1);
SET @gtw_sub2 = (SELECT id FROM tbl_subcategory WHERE language_id = 52 AND maincat_id = @gtw_cat2 LIMIT 1);
SET @gtw_sub3 = (SELECT id FROM tbl_subcategory WHERE language_id = 52 AND maincat_id = @gtw_cat3 LIMIT 1);

INSERT INTO tbl_guess_the_word (language_id, category, subcategory, image, question, answer)
VALUES
(52, @gtw_cat1, @gtw_sub1, '', 'İslamiyet öncesi Türklerde devlet işlerinin görüşüldüğü meclis', 'KURULTAY'),
(52, @gtw_cat1, @gtw_sub1, '', 'Osmanlı Devleti\'nde toprağa ve üretime bağlı askeri sistem', 'TIMAR'),
(52, @gtw_cat1, @gtw_sub1, '', 'Gök Tanrı tarafından hükümdara verilen kutsal yönetim yetkisi', 'KUT'),
(52, @gtw_cat1, @gtw_sub1, '', 'Milli Mücadele\'de vatanın sınırlarını çizen tarihi antlaşma kararları', 'MISAKIMILLI'),
(52, @gtw_cat2, @gtw_sub2, '', 'Bir adanın kıyı oku ile karaya bağlanmasıyla oluşan saplı ada', 'TOMBOLO'),
(52, @gtw_cat2, @gtw_sub2, '', 'Akdeniz bölgesinde kalkerli arazide suların eritmesiyle oluşan şekil', 'KARSTIK'),
(52, @gtw_cat2, @gtw_sub2, '', 'Akarsuyun denize döküldüğü yerde biriktirdiği alüvyon ovası', 'DELTA'),
(52, @gtw_cat3, @gtw_sub3, '', 'Toplum düzenini sağlayan ve devlet gücüyle desteklenen kurallar bütünü', 'HUKUK'),
(52, @gtw_cat3, @gtw_sub3, '', 'Devletin en üstün ve bağlayıcı temel yazılı kanunu', 'ANAYASA'),
(52, @gtw_cat3, @gtw_sub3, '', 'İdarede halkın şikayetlerini inceleyen Kamu Denetçiliği makamı', 'OMBUDSMAN');

SET FOREIGN_KEY_CHECKS = 1;
