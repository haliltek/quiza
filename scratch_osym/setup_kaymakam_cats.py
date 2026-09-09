import subprocess

def run_sql(sql):
    cmd = ['ssh', 'root@142.93.104.78', 'docker exec -i elitequiz_db mysql --default-character-set=utf8mb4 -uelite_user -pelite_user_pass_2026 elite_quiz_db']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate(sql.encode('utf-8'))
    return stdout.decode('utf-8', errors='replace')

sql = """
SET NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';

INSERT INTO tbl_category (language_id, category_name, slug, type, is_premium, coins, has_level, image, row_order)
VALUES
(62, 'Anayasa Hukuku (Kaymakamlık)', 'kaymakam-anayasa', 1, 0, 0, 1, '', 1),
(62, 'İdare Hukuku & Teşkilat (Kaymakamlık)', 'kaymakam-idare', 1, 0, 0, 1, '', 2),
(62, 'Türkiye İdari Yapısı & Yerel Yönetimler (Kaymakamlık)', 'kaymakam-mahalli-idareler', 1, 0, 0, 1, '', 3),
(62, 'Türkiye Ekonomisi & İktisat (Kaymakamlık)', 'kaymakam-ekonomi', 1, 0, 0, 1, '', 4),
(62, 'Atatürk İlkeleri & İnkılap Tarihi (Kaymakamlık)', 'kaymakam-tarih', 1, 0, 0, 1, '', 5)
ON DUPLICATE KEY UPDATE category_name = VALUES(category_name);

-- Subcategories
SET @cat_ay_62 = (SELECT id FROM tbl_category WHERE language_id = 62 AND slug = 'kaymakam-anayasa' LIMIT 1);
SET @cat_id_62 = (SELECT id FROM tbl_category WHERE language_id = 62 AND slug = 'kaymakam-idare' LIMIT 1);
SET @cat_mh_62 = (SELECT id FROM tbl_category WHERE language_id = 62 AND slug = 'kaymakam-mahalli-idareler' LIMIT 1);
SET @cat_ek_62 = (SELECT id FROM tbl_category WHERE language_id = 62 AND slug = 'kaymakam-ekonomi' LIMIT 1);
SET @cat_tr_62 = (SELECT id FROM tbl_category WHERE language_id = 62 AND slug = 'kaymakam-tarih' LIMIT 1);

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, is_premium, coins, has_level, row_order)
VALUES
(62, @cat_ay_62, 'T.C. Anayasası Temel İlkeler ve Hükümet Sistemi', 'kaym-ay-ilkeler', 1, 0, 0, 1, 1),
(62, @cat_ay_62, 'Yasama, Yürütme ve Anayasa Yargısı', 'kaym-ay-organlar', 1, 0, 0, 1, 2),
(62, @cat_id_62, 'İdare Hukuku Genel İlkeler ve İşlemler', 'kaym-idare-genel', 1, 0, 0, 1, 1),
(62, @cat_id_62, 'Kamu Hizmetleri, Kolluk ve Sorumluluk', 'kaym-idare-kolluk', 1, 0, 0, 1, 2),
(62, @cat_mh_62, 'İl İdaresi Kanunu, Vali ve Kaymakam Yetkileri', 'kaym-il-idaresi-vali', 1, 0, 0, 1, 1),
(62, @cat_mh_62, 'Belediye, Büyükşehir ve Köy Kanunu', 'kaym-belediye-koy', 1, 0, 0, 1, 2),
(62, @cat_ek_62, 'Türkiye Ekonomisi ve Mali Politikalar', 'kaym-ekonomi-maliye', 1, 0, 0, 1, 1),
(62, @cat_tr_62, 'Milli Mücadele ve Cumhuriyet Dönemi Reformları', 'kaym-tarih-reformlar', 1, 0, 0, 1, 1)
ON DUPLICATE KEY UPDATE subcategory_name = VALUES(subcategory_name);

SELECT c.id, c.category_name, COUNT(s.id) as sub_count
FROM tbl_category c
LEFT JOIN tbl_subcategory s ON c.id = s.maincat_id
WHERE c.language_id = 62
GROUP BY c.id, c.category_name;
"""

print(run_sql(sql))
