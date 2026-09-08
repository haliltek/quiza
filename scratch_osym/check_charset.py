import subprocess

cmd = [
    'ssh', '-o', 'StrictHostKeyChecking=no', 'root@142.93.104.78',
    'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db --default-character-set=utf8mb4 -e "SHOW CREATE TABLE tbl_study_notes; SELECT id, note_type, topic_title, LEFT(content, 60) FROM tbl_study_notes WHERE note_type=\'flashcard\' LIMIT 3;"'
]

res = subprocess.run(cmd, capture_output=True)
print("STDOUT:")
print(res.stdout.decode('utf-8', errors='replace'))
print("STDERR:")
print(res.stderr.decode('utf-8', errors='replace'))
