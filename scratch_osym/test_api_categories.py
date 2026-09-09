import subprocess, json

cmd = ['ssh', 'root@142.93.104.78', 'curl -s -X POST -d "type=1&language_id=60" http://localhost:8088/Api/get_categories']
res = subprocess.run(cmd, capture_output=True)
out = res.stdout.decode('utf-8', errors='replace')
print("=== HMGS CATEGORIES API RESPONSE ===")
try:
    data = json.loads(out)
    print(f"Error: {data.get('error')}")
    cats = data.get('data', [])
    print(f"Returned {len(cats)} categories for HMGS:")
    for c in cats:
        print(f"  ID: {c.get('id')} - {c.get('category_name')}")
except Exception as e:
    print("Raw output:", out[:300])

cmd2 = ['ssh', 'root@142.93.104.78', 'curl -s -X POST -d "type=1&language_id=63" http://localhost:8088/Api/get_categories']
res2 = subprocess.run(cmd2, capture_output=True)
out2 = res2.stdout.decode('utf-8', errors='replace')
print("\n=== GYS CATEGORIES API RESPONSE ===")
try:
    data2 = json.loads(out2)
    print(f"Error: {data2.get('error')}")
    cats2 = data2.get('data', [])
    print(f"Returned {len(cats2)} categories for GYS:")
    for c in cats2:
        print(f"  ID: {c.get('id')} - {c.get('category_name')}")
except Exception as e:
    print("Raw output:", out2[:300])
