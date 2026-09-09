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

sql_subcats = """
SET NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';

-- ==========================================================
-- 1. HMGS (Language ID: 60) Subcategories
-- ==========================================================
INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, is_premium, coins, has_level, row_order)
VALUES
-- Anayasa (66)
(60, 66, 'Temel Hak ve Hürriyetler Rejimi', 'hmgs-ay-haklar', 1, 0, 0, 1, 1),
(60, 66, 'Yasama, Yürütme ve Yargı Organları', 'hmgs-ay-organlar', 1, 0, 0, 1, 2),
(60, 66, 'Anayasa Yargısı & Bireysel Başvuru', 'hmgs-ay-yargisi', 1, 0, 0, 1, 3),

-- İdare & İYUK (67)
(60, 67, 'Türkiye İdari Teşkilatı ve Yetki İlkeleri', 'hmgs-idare-teskilat', 1, 0, 0, 1, 1),
(60, 67, 'İdari İşlemler, İdari Sözleşmeler ve Kamu Malları', 'hmgs-idare-islemler', 1, 0, 0, 1, 2),
(60, 67, 'İYUK: İptal ve Tam Yargı Davaları, Süreler', 'hmgs-iyuk-davalar', 1, 0, 0, 1, 3),

-- HMK (68)
(60, 68, 'Görev, Yetki ve Yargı Yolu', 'hmgs-hmk-gorev-yetki', 1, 0, 0, 1, 1),
(60, 68, 'Dava Şartları, İlk İtirazlar ve Dilekçeler', 'hmgs-hmk-dava-sartlari', 1, 0, 0, 1, 2),
(60, 68, 'İspat Hukuku, Deliller ve Hüküm', 'hmgs-hmk-deliller', 1, 0, 0, 1, 3),
(60, 68, 'Kanun Yolları: İstinaf ve Temyiz Süreçleri', 'hmgs-hmk-kanun-yollari', 1, 0, 0, 1, 4),

-- Ceza Genel & Özel (69)
(60, 69, 'Suçun Unsurları, Hukuka Uygunluk & Kusurluluk', 'hmgs-tck-genel', 1, 0, 0, 1, 1),
(60, 69, 'Teşebbüs, İştirak ve İçtima Hükümleri', 'hmgs-tck-tesebbus-istirak', 1, 0, 0, 1, 2),
(60, 69, 'Kişilere ve Malvarlığına Karşı Suçlar', 'hmgs-tck-ozel', 1, 0, 0, 1, 3),

-- CMK (70)
(60, 70, 'Soruşturma Evresi, İfade ve Sorgu', 'hmgs-cmk-sorusturma', 1, 0, 0, 1, 1),
(60, 70, 'Koruma Tedbirleri (Yakalama, Tutuklama, Arama)', 'hmgs-cmk-koruma', 1, 0, 0, 1, 2),
(60, 70, 'Kovuşturma Evresi, Duruşma ve Kanun Yolları', 'hmgs-cmk-kovusturma', 1, 0, 0, 1, 3),

-- Medeni & Borçlar (71)
(60, 71, 'Kişiler, Aile ve Miras Hukuku', 'hmgs-medeni-kisiler-aile', 1, 0, 0, 1, 1),
(60, 71, 'Eşya Hukuku, Zilyetlik ve Tapu Sicili', 'hmgs-medeni-esya', 1, 0, 0, 1, 2),
(60, 71, 'Borçlar Hukuku: Sözleşmeler, Haksız Fiil ve İfa', 'hmgs-borclar-genel', 1, 0, 0, 1, 3),

-- Ticaret Hukuku (72)
(60, 72, 'Ticari İşletme, Tacir ve Ticaret Sicili', 'hmgs-ticaret-isletme', 1, 0, 0, 1, 1),
(60, 72, 'Şirketler Hukuku (Anonim ve Limited)', 'hmgs-ticaret-sirketler', 1, 0, 0, 1, 2),
(60, 72, 'Kıymetli Evrak (Bono, Poliçe, Çek)', 'hmgs-ticaret-kiymetli-evrak', 1, 0, 0, 1, 3),

-- İcra İflas (73)
(60, 73, 'İlamsız İcra ve Ödeme Emrine İtiraz', 'hmgs-iik-ilamsiz-icra', 1, 0, 0, 1, 1),
(60, 73, 'Haciz, Satış ve Paraların Paylaştırılması', 'hmgs-iik-haciz-satis', 1, 0, 0, 1, 2),
(60, 73, 'İlamlı İcra, İhtiyati Haciz ve İflas Yolu', 'hmgs-iik-ilamli-iflas', 1, 0, 0, 1, 3),

-- Avukatlık & Felsefe (74)
(60, 74, '1136 Sayılı Avukatlık Kanunu ve Disiplin', 'hmgs-avukatlik-kanunu', 1, 0, 0, 1, 1),
(60, 74, 'Hukuk Felsefesi, Sosyolojisi ve Hukuk Tarihi', 'hmgs-hukuk-felsefesi', 1, 0, 0, 1, 2)
ON DUPLICATE KEY UPDATE subcategory_name = VALUES(subcategory_name);

-- ==========================================================
-- 2. Hakimlik & Savcılık (Language ID: 59) Subcategories
-- ==========================================================
INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, is_premium, coins, has_level, row_order)
VALUES
-- Anayasa & İdare (11)
(59, 11, 'Anayasa Hukuku & Bireysel Başvuru', 'hakimlik-anayasa', 1, 0, 0, 1, 1),
(59, 11, 'İdare Hukuku ve İdari Teşkilat', 'hakimlik-idare-hukuku', 1, 0, 0, 1, 2),

-- Ceza Genel & Özel (12)
(59, 12, 'Ceza Hukuku Genel Hükümler', 'hakimlik-ceza-genel', 1, 0, 0, 1, 1),
(59, 12, 'Ceza Hukuku Özel Hükümler', 'hakimlik-ceza-ozel', 1, 0, 0, 1, 2),

-- CMK (13)
(59, 13, 'Soruşturma & Koruma Tedbirleri', 'hakimlik-cmk-koruma', 1, 0, 0, 1, 1),
(59, 13, 'Kovuşturma, Deliller ve İtiraz/İstinaf/Temyiz', 'hakimlik-cmk-kovusturma', 1, 0, 0, 1, 2),

-- Medeni & Borçlar (14)
(59, 14, 'Medeni Hukuk (Kişiler, Eşya, Miras)', 'hakimlik-medeni', 1, 0, 0, 1, 1),
(59, 14, 'Borçlar Hukuku Genel & Özel Hükümler', 'hakimlik-borclar', 1, 0, 0, 1, 2),

-- İYUK (15)
(59, 15, 'İdari Yargılama Usulü, Dava Açma ve Süreler', 'hakimlik-iyuk-sureler', 1, 0, 0, 1, 1),
(59, 15, 'Yürütmenin Durdurulması ve Kanun Yolları', 'hakimlik-iyuk-kanun-yollari', 1, 0, 0, 1, 2)
ON DUPLICATE KEY UPDATE subcategory_name = VALUES(subcategory_name);

-- ==========================================================
-- 3. İcra Müdürlüğü (Language ID: 61) Subcategories
-- ==========================================================
INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, is_premium, coins, has_level, row_order)
VALUES
-- İcra ve İflas (6)
(61, 6, 'İlamsız Takip, Ödeme Emri & İtiraz', 'icra-ilamsiz-takip', 1, 0, 0, 1, 1),
(61, 6, 'Haciz, Satış ve Paylaştırma Aşamaları', 'icra-haciz-satis', 1, 0, 0, 1, 2),
(61, 6, 'Kambiyo Senetlerine Özgü Haciz Yolu', 'icra-kambiyo-takibi', 1, 0, 0, 1, 3),
(61, 6, 'İlamlı İcra, Tahliye ve İflas Tasfiyesi', 'icra-ilamli-iflas', 1, 0, 0, 1, 4),

-- Ticaret Hukuku (7)
(61, 7, 'Kıymetli Evrak: Bono, Poliçe, Çek Şekil Şartları', 'icra-kiymetli-evrak', 1, 0, 0, 1, 1),
(61, 7, 'Ticaret Şirketleri ve Temsil Yetkisi', 'icra-ticaret-sirketler', 1, 0, 0, 1, 2),

-- Borçlar Hukuku (8)
(61, 8, 'Borcun İfası, Temerrüt ve Faiz Türleri', 'icra-borclar-ifa-faiz', 1, 0, 0, 1, 1),
(61, 8, 'Sözleşmenin Sona Ermesi ve Takas', 'icra-borclar-sona-erme', 1, 0, 0, 1, 2),

-- HMK (9)
(61, 9, 'Tebligat ve Yargılama Süreleri', 'icra-hmk-tebligat-sureler', 1, 0, 0, 1, 1),
(61, 9, 'İhtiyati Haciz, İhtiyati Tedbir ve Deliller', 'icra-hmk-tedbirler', 1, 0, 0, 1, 2),

-- Harçlar & Damga (10)
(61, 10, 'Yargı ve İcra Harçları (Peşin, Başvurma, Tahsil)', 'icra-harclar-tarifesi', 1, 0, 0, 1, 1),
(61, 10, 'Damga Vergisi ve Cezaevi Harcı Uygulamaları', 'icra-damga-vergisi', 1, 0, 0, 1, 2),

-- Anayasa (38)
(61, 38, 'Temel Haklar ve Anayasal İlkeler', 'icra-anayasa-ilkeler', 1, 0, 0, 1, 1)
ON DUPLICATE KEY UPDATE subcategory_name = VALUES(subcategory_name);

-- ==========================================================
-- 4. Adalet Bakanlığı GYS (Language ID: 63) Subcategories
-- ==========================================================
INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, is_premium, coins, has_level, row_order)
VALUES
-- Anayasa (75)
(63, 75, 'T.C. Anayasası Temel İlkeler ve Yargı Organları', 'gys-ay-yargi', 1, 0, 0, 1, 1),

-- 657 DMK (76)
(63, 76, 'Memurların Hakları, Ödevleri ve Yasaklar', 'gys-dmk-haklar-odevler', 1, 0, 0, 1, 1),
(63, 76, 'Disiplin Cezaları ve Soruşturma Usulü', 'gys-dmk-disiplin', 1, 0, 0, 1, 2),
(63, 76, 'Adaylık, Kademe İlerlemesi ve Görevden Uzaklaştırma', 'gys-dmk-ilerleme', 1, 0, 0, 1, 3),

-- 7201 Tebligat (77)
(63, 77, 'Tebligat Usulleri ve Bilinen Adreste Tebligat', 'gys-tebligat-usul', 1, 0, 0, 1, 1),
(63, 77, 'Madde 21 ve 35 Göre Tebligat, Gece ve Tatil', 'gys-tebligat-madde21-35', 1, 0, 0, 1, 2),
(63, 77, 'Elektronik Tebligat (UETS) ve Memur Vasıtasıyla Tebliğ', 'gys-tebligat-uets', 1, 0, 0, 1, 3),

-- Yazı İşleri (78)
(63, 78, 'Dava Açılışı, Tevzi ve Tensip İşlemleri', 'gys-yazi-tevzi-tensip', 1, 0, 0, 1, 1),
(63, 78, 'Duruşma Tutanağı, Gerekçeli Karar ve Kesinleşme', 'gys-yazi-tutanak-kesinlesme', 1, 0, 0, 1, 2),
(63, 78, 'Adli Emanet, Suç Eşyası ve Arşiv İşlemleri', 'gys-yazi-emanet-arsiv', 1, 0, 0, 1, 3),

-- Harçlar & Giderler (79)
(63, 79, 'Yargı Harçları (Peşin, Nispi, Maktu Harçlar)', 'gys-harclar-yargi', 1, 0, 0, 1, 1),
(63, 79, 'Gider Avansı, Delil Avansı ve İade İşlemleri', 'gys-gider-avansi', 1, 0, 0, 1, 2),

-- HMK & CMK İlkeleri (80)
(63, 80, 'HMK Temel İlkeler ve Yargılama Süreleri', 'gys-hmk-sureler', 1, 0, 0, 1, 1),
(63, 80, 'CMK Soruşturma, İfade, Tutuklama ve Karar Türleri', 'gys-cmk-kararlar', 1, 0, 0, 1, 2),

-- UYAP ve Büro (81)
(63, 81, 'UYAP Ekranları, Elektronik İmza ve Veri Girişi', 'gys-uyap-e-imza', 1, 0, 0, 1, 1),
(63, 81, 'Resmi Yazışma Kuralları ve Tebellüğ Belgeleri', 'gys-resmi-yazisma', 1, 0, 0, 1, 2)
ON DUPLICATE KEY UPDATE subcategory_name = VALUES(subcategory_name);

-- ==========================================================
-- 5. KPSS A Grubu (Language ID: 58) Subcategories
-- ==========================================================
INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, is_premium, coins, has_level, row_order)
VALUES
-- Kamu Yönetimi (52)
(58, 52, 'Siyaset Bilimi ve Yönetim Bilimi', 'a-kamu-siyaset-yonetim', 1, 0, 0, 1, 1),
(58, 52, 'Türkiye İdare Tarihi ve Yerel Yönetimler', 'a-kamu-idare-tarihi', 1, 0, 0, 1, 2),

-- Muhasebe (53)
(58, 53, 'Genel Muhasebe & Finansal Tablolar', 'a-muhasebe-genel', 1, 0, 0, 1, 1),
(58, 53, 'Maliyet Muhasebesi ve Şirketler Muhasebesi', 'a-muhasebe-maliyet', 1, 0, 0, 1, 2)
ON DUPLICATE KEY UPDATE subcategory_name = VALUES(subcategory_name);

-- Check inserted subcategory counts
SELECT language_id, COUNT(*) as subcategory_count FROM tbl_subcategory WHERE language_id IN (58, 59, 60, 61, 63) GROUP BY language_id;
"""

print(run_sql(sql_subcats))
