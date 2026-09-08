import subprocess

for tbl, col in [('tbl_exam_module_question', 'question_id'), ('tbl_bookmark', 'question_id'), ('tbl_question_reports', 'question_id'), ('tbl_daily_quiz', 'questions_id')]:
    cmd = ['ssh', 'root@142.93.104.78', f'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT count(*) FROM {tbl} WHERE {col} >= 1480 AND {col} <= 1909;"']
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(tbl, res.stdout.strip())
