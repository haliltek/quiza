import subprocess

with open('d:/quiza/scratch_kpss_setup.sql', 'r', encoding='utf-8') as f:
    sql = f.read()

# Prepend connection character set directives
full_sql = "SET NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';\n" + sql

cmd = ['ssh', 'root@142.93.104.78', 'docker exec -i elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db --default-character-set=utf8mb4']
res = subprocess.run(cmd, input=full_sql.encode('utf-8'), capture_output=True)
print("STDOUT:", res.stdout.decode('utf-8', errors='replace'))
print("STDERR:", res.stderr.decode('utf-8', errors='replace'))
print("EXIT CODE:", res.returncode)
