import subprocess

cmd = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "DESCRIBE tbl_languages;"']
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stdout)

cmd_row = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT * FROM tbl_languages WHERE id = 52;"']
res_row = subprocess.run(cmd_row, capture_output=True, text=True)
print("ID 52 row:", res_row.stdout)
