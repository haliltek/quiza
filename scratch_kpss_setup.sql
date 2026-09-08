SET NAMES utf8mb4;

-- 1. Update & Insert into tbl_languages
UPDATE tbl_languages SET language = 'KPSS Lisans (B Grubu - GY-GK)', code = 'kpss_lis', status = 1 WHERE id = 52;
UPDATE tbl_languages SET language = 'KPSS Önlisans (B Grubu)', code = 'kpss_onl', status = 1 WHERE id = 57;
UPDATE tbl_languages SET language = 'KPSS A Grubu (Alan Bilgisi)', code = 'kpss_aln', status = 1 WHERE id = 58;

INSERT INTO tbl_languages (id, language, code, status, type, default_active) 
VALUES 
(66, 'KPSS Ortaöğretim (Lise)', 'kpss_ort', 1, 1, 0),
(67, 'KPSS ÖABT (Öğretmenlik)', 'kpss_oabt', 1, 1, 0),
(68, 'KPSS DHBT (Din Hizmetleri)', 'kpss_dhbt', 1, 1, 0)
ON DUPLICATE KEY UPDATE language = VALUES(language), code = VALUES(code), status = 1;

-- 2. Ensure Categories for KPSS Önlisans (language_id = 57)
INSERT INTO tbl_category (language_id, category_name, slug, type, is_premium, coins, has_level, image, row_order)
VALUES
(57, 'Türkçe (KPSS Önlisans)', 'turkce-kpss-onlisans', 1, 0, 0, 1, '', 1),
(57, 'Matematik & Mantık (KPSS Önlisans)', 'matematik-kpss-onlisans', 1, 0, 0, 1, '', 2),
(57, 'Tarih (KPSS Önlisans)', 'tarih-kpss-onlisans', 1, 0, 0, 1, '', 3),
(57, 'Coğrafya (KPSS Önlisans)', 'cografya-kpss-onlisans', 1, 0, 0, 1, '', 4),
(57, 'Vatandaşlık & Anayasa (KPSS Önlisans)', 'vatandaslik-kpss-onlisans', 1, 0, 0, 1, '', 5)
ON DUPLICATE KEY UPDATE category_name = VALUES(category_name);

-- 3. Ensure Categories for KPSS Ortaöğretim (language_id = 66)
INSERT INTO tbl_category (language_id, category_name, slug, type, is_premium, coins, has_level, image, row_order)
VALUES
(66, 'Türkçe (KPSS Ortaöğretim)', 'turkce-kpss-ortaogretim', 1, 0, 0, 1, '', 1),
(66, 'Matematik (KPSS Ortaöğretim)', 'matematik-kpss-ortaogretim', 1, 0, 0, 1, '', 2),
(66, 'Tarih (KPSS Ortaöğretim)', 'tarih-kpss-ortaogretim', 1, 0, 0, 1, '', 3),
(66, 'Coğrafya (KPSS Ortaöğretim)', 'cografya-kpss-ortaogretim', 1, 0, 0, 1, '', 4),
(66, 'Vatandaşlık & Güncel (KPSS Ortaöğretim)', 'vatandaslik-kpss-ortaogretim', 1, 0, 0, 1, '', 5)
ON DUPLICATE KEY UPDATE category_name = VALUES(category_name);

-- 4. Ensure Categories for KPSS A Grubu (language_id = 58)
INSERT INTO tbl_category (language_id, category_name, slug, type, is_premium, coins, has_level, image, row_order)
VALUES
(58, 'Hukuk (KPSS A Grubu)', 'hukuk-kpss-a', 1, 0, 0, 1, '', 1),
(58, 'İktisat (KPSS A Grubu)', 'iktisat-kpss-a', 1, 0, 0, 1, '', 2),
(58, 'Maliye (KPSS A Grubu)', 'maliye-kpss-a', 1, 0, 0, 1, '', 3),
(58, 'Kamu Yönetimi (KPSS A Grubu)', 'kamu-yonetimi-kpss-a', 1, 0, 0, 1, '', 4),
(58, 'Muhasebe (KPSS A Grubu)', 'muhasebe-kpss-a', 1, 0, 0, 1, '', 5)
ON DUPLICATE KEY UPDATE category_name = VALUES(category_name);

-- 5. Ensure Categories for KPSS ÖABT Öğretmenlik (language_id = 67)
INSERT INTO tbl_category (language_id, category_name, slug, type, is_premium, coins, has_level, image, row_order)
VALUES
(67, 'Eğitim Bilimleri (Ortak Oturum)', 'egitim-bilimleri-ortak', 1, 0, 0, 1, '', 1),
(67, 'Türkçe & Edebiyat Öğretmenliği ÖABT', 'turkce-edebiyat-oabt', 1, 0, 0, 1, '', 2),
(67, 'İlköğretim & Lise Matematik ÖABT', 'matematik-oabt', 1, 0, 0, 1, '', 3),
(67, 'Tarih Öğretmenliği ÖABT', 'tarih-oabt', 1, 0, 0, 1, '', 4),
(67, 'Sınıf Öğretmenliği ÖABT', 'sinif-ogretmenligi-oabt', 1, 0, 0, 1, '', 5),
(67, 'Din Kültürü & İHL Meslek ÖABT', 'dikab-ihl-oabt', 1, 0, 0, 1, '', 6)
ON DUPLICATE KEY UPDATE category_name = VALUES(category_name);

-- 6. Ensure Categories for KPSS DHBT Din Hizmetleri (language_id = 68)
INSERT INTO tbl_category (language_id, category_name, slug, type, is_premium, coins, has_level, image, row_order)
VALUES
(68, 'DHBT-1 Temel İslam Bilimleri', 'dhbt-1-temel-islam', 1, 0, 0, 1, '', 1),
(68, 'İslam İnanç Esasları & Akaid', 'islam-inanc-akaid', 1, 0, 0, 1, '', 2),
(68, 'Fıkıh ve İslam Hukuku', 'fikih-islam-hukuku', 1, 0, 0, 1, '', 3),
(68, 'Tefsir ve Kur’an İlimleri', 'tefsir-kuran-ilimleri', 1, 0, 0, 1, '', 4),
(68, 'Hadis ve Sünnet', 'hadis-sunnet', 1, 0, 0, 1, '', 5),
(68, 'Siyer ve İslam Tarihi', 'siyer-islam-tarihi', 1, 0, 0, 1, '', 6)
ON DUPLICATE KEY UPDATE category_name = VALUES(category_name);
