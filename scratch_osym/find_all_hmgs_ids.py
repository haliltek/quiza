import subprocess

cmd = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT id, category, language_id, question FROM tbl_question WHERE question LIKE \'%HMGS%\' OR question LIKE \'%Hakimlik%\' ORDER BY id ASC;"']
res = subprocess.run(cmd, capture_output=True, text=True)
lines = res.stdout.strip().split('\n')
print(f"Total HMGS/Hakimlik questions found: {len(lines) - 1}")
if len(lines) > 1:
    print(f"First ID: {lines[1].split()[0]}")
    print(f"Last ID: {lines[-1].split()[0]}")

# Also check if any exam_module_question entries exist for them
cmd_exam = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT count(*) FROM tbl_exam_module_question WHERE question_id >= 1480;"']
res_exam = subprocess.run(cmd_exam, capture_output=True, text=True)
print("tbl_exam_module_question count:", res_exam.stdout)
