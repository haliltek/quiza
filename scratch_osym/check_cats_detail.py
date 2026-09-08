import subprocess

cmd = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT id, category_name, language_id, row_order FROM tbl_category WHERE language_id = 52 ORDER BY id ASC;"']
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stdout)
