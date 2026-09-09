# -*- coding: utf-8 -*-
"""
Hukuk ve Kamu Sınavları Kapsamlı Soru Üretici ve Aktarıcı Motoru
Quiza Platformu - 2025/2026 Güncel Mevzuat (8. ve 9. Yargı Paketleri Dahil)
"""
import json, random, re, subprocess

# Alt kategori haritasını oku
with open('d:/quiza/scratch_osym/law_subcats_map.json', 'r', encoding='utf-8') as f:
    subcats = json.load(f)

print(f"Toplam {len(subcats)} alt kategori için soru üretimi başlatılıyor...")

# Subcategory map by ID and by slug
subcat_by_id = {s['subcat_id']: s for s in subcats}
subcat_by_slug = {s['slug']: s for s in subcats}

all_questions = []

def add_q(subcat, q_text, opt_a, opt_b, opt_c, opt_d, opt_e, correct_opt, solution, level=1):
    all_questions.append({
        'category': subcat['category_id'],
        'subcategory': subcat['subcat_id'],
        'language_id': subcat['language_id'],
        'question': q_text.strip(),
        'question_type': 1,
        'optiona': opt_a.strip(),
        'optionb': opt_b.strip(),
        'optionc': opt_c.strip(),
        'optiond': opt_d.strip(),
        'optione': opt_e.strip(),
        'answer': correct_opt.lower(),
        'level': level,
        'note': solution.strip()
    })

print("Kütüphaneler yüklendi.")
