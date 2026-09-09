import subprocess

cmd = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql --default-character-set=utf8mb4 -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT * FROM tbl_languages;"']
res = subprocess.run(cmd, capture_output=True)
print("=== TBL_LANGUAGES ===")
print(res.stdout.decode('utf-8', errors='replace'))
if res.stderr:
    print("STDERR:", res.stderr.decode('utf-8', errors='replace'))

cmd2 = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql --default-character-set=utf8mb4 -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT id, category_name, language_id FROM tbl_category;"']
res2 = subprocess.run(cmd2, capture_output=True)
print("=== TBL_CATEGORY ===")
print(res2.stdout.decode('utf-8', errors='replace'))
