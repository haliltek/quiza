import subprocess, json

cmd = ['ssh', 'root@142.93.104.78', 'curl -s -X POST -d "access_key=6808&get_categories_by_language=1&language_id=60" http://localhost:8088/api-v2.php']
res = subprocess.run(cmd, capture_output=True)
out = res.stdout.decode('utf-8', errors='replace')
print("=== HMGS CATEGORIES API RESPONSE (first 500 chars) ===")
print(out[:500])

cmd2 = ['ssh', 'root@142.93.104.78', 'curl -s -X POST -d "access_key=6808&get_categories_by_language=1&language_id=63" http://localhost:8088/api-v2.php']
res2 = subprocess.run(cmd2, capture_output=True)
out2 = res2.stdout.decode('utf-8', errors='replace')
print("\n=== GYS CATEGORIES API RESPONSE (first 500 chars) ===")
print(out2[:500])
