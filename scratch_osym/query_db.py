import subprocess

cmd = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT category, COUNT(*) as total, COUNT(CASE WHEN note != \'\' THEN 1 END) as with_solution FROM tbl_question WHERE category = 11 GROUP BY category;"']
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stdout)
