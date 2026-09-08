import subprocess

cmd = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT id, category, question FROM tbl_question WHERE question LIKE \'%HMGS%\' OR question LIKE \'%Hakimlik%\' LIMIT 10;"']
res = subprocess.run(cmd, capture_output=True, text=True)
print("Samples:")
print(res.stdout)

cmd_count = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT category, COUNT(*) as cnt FROM tbl_question WHERE question LIKE \'%HMGS%\' OR question LIKE \'%Hakimlik%\' GROUP BY category;"']
res_count = subprocess.run(cmd_count, capture_output=True, text=True)
print("Counts by category:")
print(res_count.stdout)

# Check tbl_category name for those categories
cmd_cat = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT id, category_name FROM tbl_category;"']
res_cat = subprocess.run(cmd_cat, capture_output=True, text=True)
print("Categories:")
print(res_cat.stdout)
