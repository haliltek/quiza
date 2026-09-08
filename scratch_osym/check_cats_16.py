import subprocess

cmd = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT category, count(*) FROM tbl_question WHERE category >= 16 GROUP BY category;"']
res = subprocess.run(cmd, capture_output=True, text=True)
print("Questions in categories >= 16:")
print(res.stdout)
