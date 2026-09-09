import subprocess, json

cmd = ['ssh', 'root@142.93.104.78', 'curl -s -X POST -d "category=66" http://localhost:8088/Api/get_subcategory_by_maincategory']
res = subprocess.run(cmd, capture_output=True)
print(res.stdout.decode('utf-8', errors='replace'))
