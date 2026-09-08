import subprocess

# Copy seed_study.sql to remote and import with utf8mb4
subprocess.run(['scp', '-o', 'StrictHostKeyChecking=no', r'd:\quiza\scratch_osym\seed_study.sql', 'root@142.93.104.78:/tmp/seed_study.sql'], check=True)

remote_cmd = (
    "docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db --default-character-set=utf8mb4 -e 'TRUNCATE TABLE tbl_study_notes;' && "
    "docker exec -i elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db --default-character-set=utf8mb4 < /tmp/seed_study.sql && "
    "docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db --default-character-set=utf8mb4 -e 'SELECT id, note_type, topic_title, LEFT(content, 60) FROM tbl_study_notes WHERE id=63;'"
)

res = subprocess.run(['ssh', '-o', 'StrictHostKeyChecking=no', 'root@142.93.104.78', remote_cmd], capture_output=True)
print("STDOUT:", res.stdout.decode('utf-8', errors='replace'))
print("STDERR:", res.stderr.decode('utf-8', errors='replace'))
