import subprocess

sql = """
SELECT c.id as cat_id, c.category_name, COUNT(s.id) as sub_cnt 
FROM tbl_category c 
LEFT JOIN tbl_subcategory s ON s.maincat_id = c.id 
WHERE c.language_id = 52 AND c.type = 1 
GROUP BY c.id;
"""
cmd = ['ssh', 'root@142.93.104.78', f'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db --default-character-set=utf8mb4 -e "{sql}"']
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
print(res.stdout)
