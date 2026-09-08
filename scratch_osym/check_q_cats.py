import subprocess

cmd = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT q.category, c.category_name, q.subcategory, s.subcategory_name, COUNT(*) as cnt FROM tbl_question q LEFT JOIN tbl_category c ON q.category = c.id LEFT JOIN tbl_subcategory s ON q.subcategory = s.id WHERE q.language_id = 52 GROUP BY q.category, q.subcategory;"']
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stdout)
