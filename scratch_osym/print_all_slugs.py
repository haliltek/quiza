import json

with open('d:/quiza/scratch_osym/law_subcats_map.json', 'r', encoding='utf-8') as f:
    subcats = json.load(f)

for s in subcats:
    print(f"[{s['language_id']}] Cat {s['category_id']}: {s['category_name'][:25]} -> Sub {s['subcat_id']} ({s['slug']}): {s['subcategory_name']}")
