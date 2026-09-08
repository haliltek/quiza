import subprocess

sql = """
SET NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';

-- Seed questions for Önlisans (57) from Lisans (52)
-- Türkçe
SET @cat_tr_52 = (SELECT id FROM tbl_category WHERE language_id = 52 AND category_name LIKE 'Türkçe%' LIMIT 1);
SET @cat_tr_57 = (SELECT id FROM tbl_category WHERE language_id = 57 AND category_name LIKE 'Türkçe%' LIMIT 1);
SET @sub_tr_57 = (SELECT id FROM tbl_subcategory WHERE language_id = 57 AND maincat_id = @cat_tr_57 LIMIT 1);

INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level)
SELECT @cat_tr_57, @sub_tr_57, 57, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level
FROM tbl_question WHERE language_id = 52 AND category = @cat_tr_52 LIMIT 60;

-- Tarih
SET @cat_tar_52 = (SELECT id FROM tbl_category WHERE language_id = 52 AND category_name LIKE 'Tarih%' LIMIT 1);
SET @cat_tar_57 = (SELECT id FROM tbl_category WHERE language_id = 57 AND category_name LIKE 'Tarih%' LIMIT 1);
SET @sub_tar_57 = (SELECT id FROM tbl_subcategory WHERE language_id = 57 AND maincat_id = @cat_tar_57 LIMIT 1);

INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level)
SELECT @cat_tar_57, @sub_tar_57, 57, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level
FROM tbl_question WHERE language_id = 52 AND category = @cat_tar_52 LIMIT 60;

-- Coğrafya
SET @cat_cog_52 = (SELECT id FROM tbl_category WHERE language_id = 52 AND category_name LIKE 'Coğrafya%' LIMIT 1);
SET @cat_cog_57 = (SELECT id FROM tbl_category WHERE language_id = 57 AND category_name LIKE 'Coğrafya%' LIMIT 1);
SET @sub_cog_57 = (SELECT id FROM tbl_subcategory WHERE language_id = 57 AND maincat_id = @cat_cog_57 LIMIT 1);

INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level)
SELECT @cat_cog_57, @sub_cog_57, 57, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level
FROM tbl_question WHERE language_id = 52 AND category = @cat_cog_52 LIMIT 60;

-- Vatandaşlık
SET @cat_vat_52 = (SELECT id FROM tbl_category WHERE language_id = 52 AND category_name LIKE 'Vatandaşlık%' LIMIT 1);
SET @cat_vat_57 = (SELECT id FROM tbl_category WHERE language_id = 57 AND category_name LIKE 'Vatandaşlık%' LIMIT 1);
SET @sub_vat_57 = (SELECT id FROM tbl_subcategory WHERE language_id = 57 AND maincat_id = @cat_vat_57 LIMIT 1);

INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level)
SELECT @cat_vat_57, @sub_vat_57, 57, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level
FROM tbl_question WHERE language_id = 52 AND category = @cat_vat_52 LIMIT 60;

-- Seed questions for Ortaöğretim (66)
SET @cat_tr_66 = (SELECT id FROM tbl_category WHERE language_id = 66 AND category_name LIKE 'Türkçe%' LIMIT 1);
SET @sub_tr_66 = (SELECT id FROM tbl_subcategory WHERE language_id = 66 AND maincat_id = @cat_tr_66 LIMIT 1);
INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level)
SELECT @cat_tr_66, @sub_tr_66, 66, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level
FROM tbl_question WHERE language_id = 52 AND category = @cat_tr_52 LIMIT 50;

SET @cat_tar_66 = (SELECT id FROM tbl_category WHERE language_id = 66 AND category_name LIKE 'Tarih%' LIMIT 1);
SET @sub_tar_66 = (SELECT id FROM tbl_subcategory WHERE language_id = 66 AND maincat_id = @cat_tar_66 LIMIT 1);
INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level)
SELECT @cat_tar_66, @sub_tar_66, 66, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level
FROM tbl_question WHERE language_id = 52 AND category = @cat_tar_52 LIMIT 50;

SET @cat_cog_66 = (SELECT id FROM tbl_category WHERE language_id = 66 AND category_name LIKE 'Coğrafya%' LIMIT 1);
SET @sub_cog_66 = (SELECT id FROM tbl_subcategory WHERE language_id = 66 AND maincat_id = @cat_cog_66 LIMIT 1);
INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level)
SELECT @cat_cog_66, @sub_cog_66, 66, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level
FROM tbl_question WHERE language_id = 52 AND category = @cat_cog_52 LIMIT 50;

SET @cat_vat_66 = (SELECT id FROM tbl_category WHERE language_id = 66 AND category_name LIKE 'Vatandaşlık%' LIMIT 1);
SET @sub_vat_66 = (SELECT id FROM tbl_subcategory WHERE language_id = 66 AND maincat_id = @cat_vat_66 LIMIT 1);
INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level)
SELECT @cat_vat_66, @sub_vat_66, 66, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level
FROM tbl_question WHERE language_id = 52 AND category = @cat_vat_52 LIMIT 50;
"""

cmd = ['ssh', 'root@142.93.104.78', 'docker exec -i elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db --default-character-set=utf8mb4']
res = subprocess.run(cmd, input=sql.encode('utf-8'), capture_output=True)
print("STDOUT:", res.stdout.decode('utf-8', errors='replace'))
print("STDERR:", res.stderr.decode('utf-8', errors='replace'))
print("EXIT CODE:", res.returncode)
