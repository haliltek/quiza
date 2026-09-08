import subprocess
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def run_mysql_query(sql):
    cmd = [
        "ssh", "root@142.93.104.78",
        f"docker exec -i elitequiz_db mysql -u elite_user -pelite_user_pass_2026 elite_quiz_db"
    ]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='replace')
    out, err = p.communicate(sql)
    return out, err

setup_sql = """
-- 1. Insert subcategories for Category 5 (Matematik & Sayısal Mantık) if not already present
INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, row_order)
SELECT 52, 5, 'Temel Kavramlar & Dört İşlem', 'kpss-mat-temel-kavramlar', 1, 1
WHERE NOT EXISTS (SELECT 1 FROM tbl_subcategory WHERE maincat_id = 5 AND slug = 'kpss-mat-temel-kavramlar');

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, row_order)
SELECT 52, 5, 'Sayı Basamakları & Bölünebilme', 'kpss-mat-sayi-basamaklari', 1, 2
WHERE NOT EXISTS (SELECT 1 FROM tbl_subcategory WHERE maincat_id = 5 AND slug = 'kpss-mat-sayi-basamaklari');

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, row_order)
SELECT 52, 5, 'Rasyonel & Ondalık Sayılar', 'kpss-mat-rasyonel-sayilar', 1, 3
WHERE NOT EXISTS (SELECT 1 FROM tbl_subcategory WHERE maincat_id = 5 AND slug = 'kpss-mat-rasyonel-sayilar');

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, row_order)
SELECT 52, 5, 'Üslü & Köklü Sayılar', 'kpss-mat-uslu-koklu-sayilar', 1, 4
WHERE NOT EXISTS (SELECT 1 FROM tbl_subcategory WHERE maincat_id = 5 AND slug = 'kpss-mat-uslu-koklu-sayilar');

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, row_order)
SELECT 52, 5, 'Problemler (Yaş, Hız, Kar-Zarar)', 'kpss-mat-problemler', 1, 5
WHERE NOT EXISTS (SELECT 1 FROM tbl_subcategory WHERE maincat_id = 5 AND slug = 'kpss-mat-problemler');

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, row_order)
SELECT 52, 5, 'Kümeler, Mantık & Olasılık', 'kpss-mat-kumeler-olasilik', 1, 6
WHERE NOT EXISTS (SELECT 1 FROM tbl_subcategory WHERE maincat_id = 5 AND slug = 'kpss-mat-kumeler-olasilik');

INSERT INTO tbl_subcategory (language_id, maincat_id, subcategory_name, slug, status, row_order)
SELECT 52, 5, 'Geometri & Sayısal Mantık', 'kpss-mat-geometri-sayisal-mantik', 1, 7
WHERE NOT EXISTS (SELECT 1 FROM tbl_subcategory WHERE maincat_id = 5 AND slug = 'kpss-mat-geometri-sayisal-mantik');
"""

print("Inserting subcategories for Category 5...")
out, err = run_mysql_query(setup_sql)
print(out, err)

# Get the subcategory IDs for each category
get_subcats_sql = """
SELECT id, maincat_id, subcategory_name FROM tbl_subcategory WHERE maincat_id IN (1, 2, 3, 4, 5) AND language_id = 52 ORDER BY maincat_id, row_order;
"""
out, err = run_mysql_query(get_subcats_sql)
print("Subcategories:")
print(out)

subcats_by_cat = {}
for line in out.strip().split('\n'):
    if not line or line.startswith('id') or 'Warning' in line:
        continue
    parts = line.split('\t')
    if len(parts) >= 2:
        sub_id = int(parts[0])
        cat_id = int(parts[1])
        subcats_by_cat.setdefault(cat_id, []).append(sub_id)

print("Subcategories map:", subcats_by_cat)

# Now distribute questions in each category across its subcategories
distribute_sqls = []

for cat_id, sub_ids in subcats_by_cat.items():
    if not sub_ids:
        continue
    num_subs = len(sub_ids)
    # Get question IDs for this category
    q_sql = f"SELECT id FROM tbl_question WHERE category = {cat_id} AND language_id = 52 ORDER BY id;"
    q_out, _ = run_mysql_query(q_sql)
    q_ids = [int(line) for line in q_out.strip().split('\n') if line.isdigit()]
    print(f"Category {cat_id}: {len(q_ids)} questions distributed across {num_subs} subcategories {sub_ids}")
    
    # Assign each question to a subcategory round-robin
    for i, q_id in enumerate(q_ids):
        target_sub = sub_ids[i % num_subs]
        distribute_sqls.append(f"UPDATE tbl_question SET subcategory = {target_sub} WHERE id = {q_id};")

print(f"Total question update statements: {len(distribute_sqls)}")
batch_size = 500
for i in range(0, len(distribute_sqls), batch_size):
    batch = "\n".join(distribute_sqls[i:i+batch_size])
    run_mysql_query(batch)
print("Questions distribution complete!")

# Verification query
verify_sql = """
SELECT c.id, c.category_name, s.id as sub_id, s.subcategory_name, count(q.id) as q_count
FROM tbl_category c
JOIN tbl_subcategory s ON s.maincat_id = c.id
LEFT JOIN tbl_question q ON q.subcategory = s.id
WHERE c.language_id = 52
GROUP BY c.id, c.category_name, s.id, s.subcategory_name
ORDER BY c.id, s.row_order;
"""
v_out, _ = run_mysql_query(verify_sql)
print("Verification:\n", v_out)

# Update Halil's score in tbl_leaderboard_monthly and tbl_leaderboard_daily so his rank is #1
rank_sql = """
UPDATE tbl_leaderboard_monthly SET score = 450, last_updated = NOW() WHERE user_id = 1;
UPDATE tbl_leaderboard_daily SET score = 150, date_created = NOW() WHERE user_id = 1;
"""
run_mysql_query(rank_sql)
print("Halil's rank updated to top score.")
