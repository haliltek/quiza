import subprocess

sql = """
SET NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';

-- Subcategories for Önlisans (57)
-- Get category IDs for 57
SET @cat_tr_57 = (SELECT id FROM tbl_category WHERE language_id = 57 AND category_name LIKE 'Türkçe%' LIMIT 1);
SET @cat_mat_57 = (SELECT id FROM tbl_category WHERE language_id = 57 AND category_name LIKE 'Matematik%' LIMIT 1);
SET @cat_tar_57 = (SELECT id FROM tbl_category WHERE language_id = 57 AND category_name LIKE 'Tarih%' LIMIT 1);
SET @cat_cog_57 = (SELECT id FROM tbl_category WHERE language_id = 57 AND category_name LIKE 'Coğrafya%' LIMIT 1);
SET @cat_vat_57 = (SELECT id FROM tbl_category WHERE language_id = 57 AND category_name LIKE 'Vatandaşlık%' LIMIT 1);

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, is_premium, coins, has_level, row_order)
VALUES
(57, @cat_tr_57, 'Sözcük ve Cümlede Anlam', 'onlisans-tr-1', 1, 0, 0, 1, 1),
(57, @cat_tr_57, 'Paragraf & Anlatım Teknikleri', 'onlisans-tr-2', 1, 0, 0, 1, 2),
(57, @cat_tr_57, 'Dil Bilgisi & Yazım Kuralları', 'onlisans-tr-3', 1, 0, 0, 1, 3),
(57, @cat_tar_57, 'İlk Türk Devletleri', 'onlisans-tar-1', 1, 0, 0, 1, 1),
(57, @cat_tar_57, 'Osmanlı Tarihi', 'onlisans-tar-2', 1, 0, 0, 1, 2),
(57, @cat_tar_57, 'Kurtuluş Savaşı ve İnkılap Tarihi', 'onlisans-tar-3', 1, 0, 0, 1, 3),
(57, @cat_tar_57, 'Çağdaş Türk ve Dünya Tarihi', 'onlisans-tar-4', 1, 0, 0, 1, 4),
(57, @cat_cog_57, 'Türkiye Fiziki Coğrafyası', 'onlisans-cog-1', 1, 0, 0, 1, 1),
(57, @cat_cog_57, 'Türkiye Beşeri ve Ekonomik Coğrafyası', 'onlisans-cog-2', 1, 0, 0, 1, 2),
(57, @cat_vat_57, 'Temel Hukuk Kavramları', 'onlisans-vat-1', 1, 0, 0, 1, 1),
(57, @cat_vat_57, '1982 Anayasası & Devlet Organları', 'onlisans-vat-2', 1, 0, 0, 1, 2),
(57, @cat_vat_57, 'İdare Hukuku & Güncel Bilgiler', 'onlisans-vat-3', 1, 0, 0, 1, 3)
ON DUPLICATE KEY UPDATE subcategory_name = VALUES(subcategory_name);

-- Subcategories for Ortaöğretim (66)
SET @cat_tr_66 = (SELECT id FROM tbl_category WHERE language_id = 66 AND category_name LIKE 'Türkçe%' LIMIT 1);
SET @cat_tar_66 = (SELECT id FROM tbl_category WHERE language_id = 66 AND category_name LIKE 'Tarih%' LIMIT 1);
SET @cat_cog_66 = (SELECT id FROM tbl_category WHERE language_id = 66 AND category_name LIKE 'Coğrafya%' LIMIT 1);
SET @cat_vat_66 = (SELECT id FROM tbl_category WHERE language_id = 66 AND category_name LIKE 'Vatandaşlık%' LIMIT 1);

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, is_premium, coins, has_level, row_order)
VALUES
(66, @cat_tr_66, 'Sözcük ve Paragrafta Anlam', 'ortaogretim-tr-1', 1, 0, 0, 1, 1),
(66, @cat_tr_66, 'Temel Dil Bilgisi & Noktalama', 'ortaogretim-tr-2', 1, 0, 0, 1, 2),
(66, @cat_tar_66, 'İlk Türk Devletleri ve İslamiyet', 'ortaogretim-tar-1', 1, 0, 0, 1, 1),
(66, @cat_tar_66, 'Osmanlı Devleti & Kültür Medeniyet', 'ortaogretim-tar-2', 1, 0, 0, 1, 2),
(66, @cat_tar_66, 'Milli Mücadele ve Atatürk İlkeleri', 'ortaogretim-tar-3', 1, 0, 0, 1, 3),
(66, @cat_cog_66, 'Türkiye Coğrafyası & Bölgeler', 'ortaogretim-cog-1', 1, 0, 0, 1, 1),
(66, @cat_cog_66, 'Ekonomik Faaliyetler ve Nüfus', 'ortaogretim-cog-2', 1, 0, 0, 1, 2),
(66, @cat_vat_66, 'Temel Hukuk Bilgisi & Anayasa', 'ortaogretim-vat-1', 1, 0, 0, 1, 1),
(66, @cat_vat_66, 'Güncel Olaylar ve Genel Kültür', 'ortaogretim-vat-2', 1, 0, 0, 1, 2)
ON DUPLICATE KEY UPDATE subcategory_name = VALUES(subcategory_name);

-- Subcategories for A Grubu (58)
SET @cat_huk_58 = (SELECT id FROM tbl_category WHERE language_id = 58 AND category_name LIKE 'Hukuk%' LIMIT 1);
SET @cat_ikt_58 = (SELECT id FROM tbl_category WHERE language_id = 58 AND category_name LIKE 'İktisat%' LIMIT 1);
SET @cat_mal_58 = (SELECT id FROM tbl_category WHERE language_id = 58 AND category_name LIKE 'Maliye%' LIMIT 1);

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, is_premium, coins, has_level, row_order)
VALUES
(58, @cat_huk_58, 'Anayasa ve İdare Hukuku', 'a-hukuk-1', 1, 0, 0, 1, 1),
(58, @cat_huk_58, 'Ceza ve Ceza Muhakemesi Hukuku', 'a-hukuk-2', 1, 0, 0, 1, 2),
(58, @cat_huk_58, 'Medeni ve Borçlar Hukuku', 'a-hukuk-3', 1, 0, 0, 1, 3),
(58, @cat_ikt_58, 'Mikro ve Makro İktisat', 'a-iktisat-1', 1, 0, 0, 1, 1),
(58, @cat_ikt_58, 'Para, Banka ve Türkiye Ekonomisi', 'a-iktisat-2', 1, 0, 0, 1, 2),
(58, @cat_mal_58, 'Kamu Maliyesi ve Bütçe', 'a-maliye-1', 1, 0, 0, 1, 1),
(58, @cat_mal_58, 'Vergi Hukuku ve Türk Vergi Sistemi', 'a-maliye-2', 1, 0, 0, 1, 2)
ON DUPLICATE KEY UPDATE subcategory_name = VALUES(subcategory_name);
"""

cmd = ['ssh', 'root@142.93.104.78', 'docker exec -i elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db --default-character-set=utf8mb4']
res = subprocess.run(cmd, input=sql.encode('utf-8'), capture_output=True)
print("STDOUT:", res.stdout.decode('utf-8', errors='replace'))
print("STDERR:", res.stderr.decode('utf-8', errors='replace'))
print("EXIT CODE:", res.returncode)
