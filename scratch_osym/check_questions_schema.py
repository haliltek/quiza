import subprocess

cmd = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql --default-character-set=utf8mb4 -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "DESCRIBE tbl_question; SELECT q.category, c.category_name, c.language_id, count(*) FROM tbl_question q JOIN tbl_category c ON q.category = c.id GROUP BY q.category, c.category_name, c.language_id;"']
res = subprocess.run(cmd, capture_output=True)
print(res.stdout.decode('utf-8', errors='replace'))
