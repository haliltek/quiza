import subprocess

def query(sql):
    cmd = ['ssh', 'root@142.93.104.78', f'docker exec elitequiz_db mysql --default-character-set=utf8mb4 -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "{sql}"']
    res = subprocess.run(cmd, capture_output=True)
    return res.stdout.decode('utf-8', errors='replace')

print("=== DESCRIBE tbl_category ===")
print(query("DESCRIBE tbl_category;"))

print("=== DESCRIBE tbl_subcategory ===")
print(query("DESCRIBE tbl_subcategory;"))

print("=== SAMPLE SUBCATEGORIES ===")
print(query("SELECT * FROM tbl_subcategory LIMIT 20;"))

print("=== QUESTION COUNT PER LANGUAGE ===")
print(query("SELECT l.id as lang_id, l.language, l.code, COUNT(q.id) as question_count FROM tbl_languages l LEFT JOIN tbl_category c ON l.id = c.language_id LEFT JOIN tbl_question q ON c.id = q.category WHERE l.status = 1 GROUP BY l.id, l.language, l.code ORDER BY l.id;"))
