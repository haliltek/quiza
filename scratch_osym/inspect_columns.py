import subprocess
import sys

def run_sql(sql):
    cmd = ['ssh', 'root@142.93.104.78', 'docker exec -i elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db --default-character-set=utf8mb4']
    res = subprocess.run(cmd, input=sql, text=True, capture_output=True, encoding='utf-8')
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    return res.returncode

if __name__ == '__main__':
    sql = """
    SHOW FULL COLUMNS FROM tbl_languages;
    """
    run_sql(sql)
