import subprocess

cmd_del = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "DELETE FROM tbl_question WHERE id >= 1480 AND id <= 1909;"']
res_del = subprocess.run(cmd_del, capture_output=True, text=True)
print("Delete result:", res_del.stdout, res_del.stderr)

cmd_check = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT COUNT(*) as remaining_hmgs FROM tbl_question WHERE question LIKE \'%HMGS%\' OR question LIKE \'%Hakimlik%\';"']
res_check = subprocess.run(cmd_check, capture_output=True, text=True)
print("Remaining HMGS questions:", res_check.stdout)

cmd_total = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT COUNT(*) as total_questions FROM tbl_question;"']
res_total = subprocess.run(cmd_total, capture_output=True, text=True)
print("Total questions in DB:", res_total.stdout)
