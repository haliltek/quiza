import subprocess

cmd = [
    'ssh', '-o', 'StrictHostKeyChecking=no', 'root@142.93.104.78',
    'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db --default-character-set=utf8mb4 -e "SELECT id, HEX(topic_title), HEX(LEFT(content, 40)) FROM tbl_study_notes WHERE id=63;"'
]
res = subprocess.run(cmd, capture_output=True)
print(res.stdout.decode('utf-8'))
