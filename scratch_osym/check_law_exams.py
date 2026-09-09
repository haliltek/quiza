import subprocess

cmd = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql --default-character-set=utf8mb4 -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT id, category_name, language_id FROM tbl_category WHERE language_id IN (59, 60, 61, 62, 63); SELECT language_id, count(*) FROM tbl_question WHERE language_id IN (59, 60, 61, 62, 63) GROUP BY language_id;"']
res = subprocess.run(cmd, capture_output=True)
print(res.stdout.decode('utf-8', errors='replace'))
