import subprocess, json

def query(sql):
    cmd = ['ssh', 'root@142.93.104.78', f'docker exec elitequiz_db mysql --default-character-set=utf8mb4 -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "{sql}"']
    res = subprocess.run(cmd, capture_output=True)
    return res.stdout.decode('utf-8', errors='replace')

out = query("SELECT s.id, s.language_id, s.maincat_id, c.category_name, s.subcategory_name, s.slug FROM tbl_subcategory s JOIN tbl_category c ON s.maincat_id = c.id WHERE s.language_id IN (58, 59, 60, 61, 63) ORDER BY s.language_id, c.id, s.id;")

lines = out.strip().split('\n')
header = lines[0].split('\t')
subcats = []
for line in lines[1:]:
    parts = line.split('\t')
    if len(parts) >= 6:
        subcats.append({
            'subcat_id': int(parts[0]),
            'language_id': int(parts[1]),
            'category_id': int(parts[2]),
            'category_name': parts[3],
            'subcategory_name': parts[4],
            'slug': parts[5]
        })

print(f"Total subcategories mapped: {len(subcats)}")
with open('d:/quiza/scratch_osym/law_subcats_map.json', 'w', encoding='utf-8') as f:
    json.dump(subcats, f, ensure_ascii=False, indent=2)

print("Saved to d:/quiza/scratch_osym/law_subcats_map.json")
