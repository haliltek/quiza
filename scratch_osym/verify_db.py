import subprocess

def run_query(sql):
    cmd = ['ssh', 'root@142.93.104.78', f'docker exec elitequiz_db mysql --default-character-set=utf8mb4 -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "{sql}"']
    res = subprocess.run(cmd, capture_output=True)
    out = res.stdout.decode('utf-8', errors='replace')
    print(out)
    err = res.stderr.decode('utf-8', errors='replace')
    if err and "Using a password" not in err:
        print("ERR:", err)

print("=== TOTAL QUESTIONS BY CATEGORY ===")
run_query("SELECT c.id, c.category_name, COUNT(q.id) as question_count FROM tbl_category c LEFT JOIN tbl_question q ON c.id = q.category GROUP BY c.id, c.category_name ORDER BY c.id;")

print("\n=== KPSS QUESTIONS COUNT ===")
run_query("SELECT COUNT(*) as kpss_question_count FROM tbl_question WHERE question LIKE '%KPSS Çıkmış Soru%';")

print("\n=== SAMPLE KPSS QUESTIONS FROM DATABASE ===")
run_query("SELECT id, category, subcategory, LEFT(question, 100) as question_preview, answer, note FROM tbl_question WHERE question LIKE '%KPSS Çıkmış Soru%' ORDER BY id DESC LIMIT 5;")
