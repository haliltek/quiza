import subprocess

sql = """
SELECT language_id, COUNT(*) as question_cnt 
FROM tbl_question 
WHERE language_id IN (52, 57, 58, 66, 67, 68) 
GROUP BY language_id;
"""
cmd = ['ssh', 'root@142.93.104.78', f'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db --default-character-set=utf8mb4 -e "{sql}"']
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
print(res.stdout)
