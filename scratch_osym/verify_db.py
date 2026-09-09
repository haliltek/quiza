import subprocess

def run_query(sql):
    cmd = ['ssh', 'root@142.93.104.78', f'docker exec elitequiz_db mysql --default-character-set=utf8mb4 -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "{sql}"']
    res = subprocess.run(cmd, capture_output=True)
    out = res.stdout.decode('utf-8', errors='replace')
    print(out)
    return out

print("=== 1. DİL / HEDEF SINAV BAZLI SORU SAYILARI ===")
run_query("""
SELECT l.id, l.language, l.code, COUNT(q.id) as question_count
FROM tbl_languages l
LEFT JOIN tbl_question q ON l.id = q.language_id
WHERE l.status = 1
GROUP BY l.id, l.language, l.code
ORDER BY l.id;
""")

print("=== 2. HUKUK & KAMU KATEGORİ BAZLI SORU DAĞILIMI ===")
run_query("""
SELECT c.id, c.language_id, c.category_name, COUNT(DISTINCT s.id) as subcat_count, COUNT(q.id) as q_count
FROM tbl_category c
LEFT JOIN tbl_subcategory s ON c.id = s.maincat_id
LEFT JOIN tbl_question q ON c.id = q.category
WHERE c.language_id IN (58, 59, 60, 61, 63)
GROUP BY c.id, c.language_id, c.category_name
ORDER BY c.language_id, c.id;
""")

print("=== 3. VERİ BÜTÜNLÜĞÜ KONTROLÜ ===")
run_query("""
SELECT 
    COUNT(*) as total_questions,
    SUM(CASE WHEN optiona IS NULL OR optiona = '' THEN 1 ELSE 0 END) as empty_opt_a,
    SUM(CASE WHEN optionb IS NULL OR optionb = '' THEN 1 ELSE 0 END) as empty_opt_b,
    SUM(CASE WHEN optionc IS NULL OR optionc = '' THEN 1 ELSE 0 END) as empty_opt_c,
    SUM(CASE WHEN optiond IS NULL OR optiond = '' THEN 1 ELSE 0 END) as empty_opt_d,
    SUM(CASE WHEN optione IS NULL OR optione = '' THEN 1 ELSE 0 END) as empty_opt_e,
    SUM(CASE WHEN answer NOT IN ('a', 'b', 'c', 'd', 'e') THEN 1 ELSE 0 END) as invalid_answer
FROM tbl_question;
""")

print("=== 4. ÖRNEK GYS & HMGS SORULARI ===")
run_query("""
SELECT id, language_id, category, subcategory, LEFT(question, 70) as question_preview, answer, LEFT(note, 80) as solution_preview
FROM tbl_question 
WHERE language_id IN (60, 63)
ORDER BY id DESC
LIMIT 5;
""")
