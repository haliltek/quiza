import sys; sys.path.append(r'd:\quiza\scratch_osym')
from extract_all_candidates import parse_sample_booklet, parse_full_booklet, full_ranges
from parse_answer_keys import parse_answer_keys

keys = parse_answer_keys()

all_qs = []
for y in [2024, 2023, 2022, 2018]:
    all_qs.extend(parse_sample_booklet(y))
for y, (gy_r, gk_r) in full_ranges.items():
    all_qs.extend(parse_full_booklet(y, gy_r, gk_r, keys))

by_cat = {}
for q in all_qs:
    by_cat.setdefault(q['category'], []).append(q)

cat_names = {1: "Tarih", 2: "Coğrafya", 3: "Vatandaşlık & Güncel", 4: "Türkçe", 5: "Matematik"}

for cid in sorted(by_cat.keys()):
    print(f"\n==================== KATEGORİ {cid}: {cat_names[cid]} (Toplam: {len(by_cat[cid])}) ====================")
    samples = [by_cat[cid][0], by_cat[cid][len(by_cat[cid])//2], by_cat[cid][-1]]
    for q in samples:
        print(f"\n[{q['year']} - {q['test']} Soru {q['qnum']} | Subcat: {q['subcategory']} | Doğru Cevap: {q['answer'].upper()}]")
        print("Soru:")
        print(q['question'])
        print(f"A) {q['optiona']}")
        print(f"B) {q['optionb']}")
        print(f"C) {q['optionc']}")
        print(f"D) {q['optiond']}")
        print(f"E) {q['optione']}")
        print("Note:", q['note'])
