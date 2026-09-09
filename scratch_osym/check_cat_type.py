import subprocess

def query(sql):
    cmd = ['ssh', 'root@142.93.104.78', f'docker exec elitequiz_db mysql --default-character-set=utf8mb4 -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "{sql}"']
    res = subprocess.run(cmd, capture_output=True)
    return res.stdout.decode('utf-8', errors='replace')

print(query("SELECT type, count(*) FROM tbl_category GROUP BY type;"))
