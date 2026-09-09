import subprocess

def run_sql(sql):
    cmd = ['ssh', 'root@142.93.104.78', 'docker exec -i elitequiz_db mysql --default-character-set=utf8mb4 -uelite_user -pelite_user_pass_2026 elite_quiz_db']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate(sql.encode('utf-8'))
    out = stdout.decode('utf-8', errors='replace')
    err = stderr.decode('utf-8', errors='replace')
    if err and "Using a password" not in err:
        print("SQL ERROR:", err)
    return out

sql_setup_cats = """
SET NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';

-- ==========================================================
-- 1. HMGS (Language ID: 60) Categories
-- ==========================================================
INSERT INTO tbl_category (language_id, category_name, slug, type, is_premium, coins, has_level, image, row_order)
VALUES
(60, 'Anayasa Hukuku (HMGS)', 'hmgs-anayasa-hukuku', 1, 0, 0, 1, '', 1),
(60, 'İdare Hukuku & İYUK (HMGS)', 'hmgs-idare-hukuku-iyuk', 1, 0, 0, 1, '', 2),
(60, 'Hukuk Muhakemeleri Kanunu - HMK (HMGS)', 'hmgs-hmk', 1, 0, 0, 1, '', 3),
(60, 'Ceza Hukuku Genel & Özel (HMGS)', 'hmgs-ceza-hukuku', 1, 0, 0, 1, '', 4),
(60, 'Ceza Muhakemesi Hukuku - CMK (HMGS)', 'hmgs-cmk', 1, 0, 0, 1, '', 5),
(60, 'Medeni Hukuk & Borçlar Hukuku (HMGS)', 'hmgs-medeni-borclar', 1, 0, 0, 1, '', 6),
(60, 'Ticaret Hukuku (HMGS)', 'hmgs-ticaret-hukuku', 1, 0, 0, 1, '', 7),
(60, 'İcra ve İflas Hukuku (HMGS)', 'hmgs-icra-iflas', 1, 0, 0, 1, '', 8),
(60, 'Avukatlık Hukuku & Hukuk Felsefesi (HMGS)', 'hmgs-avukatlik-felsefe', 1, 0, 0, 1, '', 9)
ON DUPLICATE KEY UPDATE category_name = VALUES(category_name);

-- ==========================================================
-- 2. Adalet Bakanlığı GYS (Language ID: 63) Categories
-- ==========================================================
INSERT INTO tbl_category (language_id, category_name, slug, type, is_premium, coins, has_level, image, row_order)
VALUES
(63, '1982 Anayasası & Devlet Teşkilatı (GYS)', 'gys-anayasa-teskilat', 1, 0, 0, 1, '', 1),
(63, '657 Sayılı Devlet Memurları Kanunu (GYS)', 'gys-657-dmk', 1, 0, 0, 1, '', 2),
(63, '7201 Sayılı Tebligat Kanunu (GYS)', 'gys-tebligat-kanunu', 1, 0, 0, 1, '', 3),
(63, 'Yazı İşleri ve Mahkeme Büro Yönetimi (GYS)', 'gys-yazi-isleri-yonetimi', 1, 0, 0, 1, '', 4),
(63, 'Harçlar Kanunu ve Yargılama Giderleri (GYS)', 'gys-harclar-kanunu', 1, 0, 0, 1, '', 5),
(63, 'HMK & CMK Temel Yargılama İlkeleri (GYS)', 'gys-hmk-cmk-ilkeler', 1, 0, 0, 1, '', 6),
(63, 'UYAP Bilişim Sistemi ve Büro Mevzuatı (GYS)', 'gys-uyap-mevzuati', 1, 0, 0, 1, '', 7)
ON DUPLICATE KEY UPDATE category_name = VALUES(category_name);

-- Check inserted categories
SELECT id, language_id, category_name FROM tbl_category WHERE language_id IN (58, 59, 60, 61, 63) ORDER BY language_id, row_order;
"""

print(run_sql(sql_setup_cats))
