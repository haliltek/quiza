# -*- coding: utf-8 -*-
"""
Master Hukuk ve Kamu Sınavları Soru İçe Aktarıcı (Importer)
Tüm jeneratörleri birleştirir, veri bütünlüğünü denetler ve MySQL'e güvenli toplu aktarımı yapar.
"""
import sys, os, json, subprocess

# Dizin ekle
sys.path.append('d:/quiza/scratch_osym/law_generators')

from book_questions_importer import get_book_questions
from gys_questions import generate_gys_questions
from icra_questions import generate_icra_questions
from hmgs_questions import generate_hmgs_questions
from hakimlik_questions import generate_hakimlik_questions
from kpss_a_questions import generate_kpss_a_questions
from systematic_law_scenarios import generate_systematic_scenarios

def escape_sql(text):
    if text is None:
        return "''"
    s = str(text)
    s = s.replace("\\", "\\\\")
    s = s.replace("'", "''")
    s = s.replace("\r", " ")
    s = s.replace("\n", "\\n")
    return f"'{s}'"

def run_sql_batch(sql_content):
    cmd = ['ssh', 'root@142.93.104.78', 'docker exec -i elitequiz_db mysql --default-character-set=utf8mb4 -uelite_user -pelite_user_pass_2026 elite_quiz_db']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate(sql_content.encode('utf-8'))
    err = stderr.decode('utf-8', errors='replace')
    if err and "Using a password" not in err:
        print("SQL Warning/Error:", err[:200])
    return stdout.decode('utf-8', errors='replace')

def main():
    print("=== Master Soru İçe Aktarıcı Başlatıldı ===")
    
    with open('d:/quiza/scratch_osym/law_subcats_map.json', 'r', encoding='utf-8') as f:
        subcats = json.load(f)
        
    subcat_by_slug = {s['slug']: s for s in subcats}
    
    # 1. Tüm modüllerden soruları topla
    all_qs = []
    
    print("1. Kitap soruları alınıyor...")
    book_qs = get_book_questions(subcat_by_slug)
    all_qs.extend(book_qs)
    
    print("2. GYS soruları üretiliyor...")
    gys_qs = generate_gys_questions(subcat_by_slug)
    all_qs.extend(gys_qs)
    
    print("3. İcra Müdürlüğü soruları üretiliyor...")
    icra_qs = generate_icra_questions(subcat_by_slug)
    all_qs.extend(icra_qs)
    
    print("4. HMGS soruları üretiliyor...")
    hmgs_qs = generate_hmgs_questions(subcat_by_slug)
    all_qs.extend(hmgs_qs)
    
    print("5. Hâkimlik soruları üretiliyor...")
    hak_qs = generate_hakimlik_questions(subcat_by_slug)
    all_qs.extend(hak_qs)
    
    print("6. KPSS A Grubu soruları üretiliyor...")
    kpss_qs = generate_kpss_a_questions(subcat_by_slug)
    all_qs.extend(kpss_qs)
    
    print("7. Sistematik mevzuat senaryoları üretiliyor...")
    sys_qs = generate_systematic_scenarios(subcats)
    all_qs.extend(sys_qs)
    
    print(f"\nToplam toplanan ham soru sayısı: {len(all_qs)}")
    
    # 2. Doğrulama ve temizleme
    valid_qs = []
    for q in all_qs:
        # Şıkların ve metinlerin kontrolü
        if not q.get('question') or len(q['question'].strip()) < 5:
            continue
        if not q.get('optiona') or not q.get('optionb') or not q.get('optionc') or not q.get('optiond') or not q.get('optione'):
            continue
        ans = q.get('answer', '').lower().strip()
        if ans not in ['a', 'b', 'c', 'd', 'e']:
            continue
        valid_qs.append(q)
        
    print(f"Bütünlüğü doğrulanmış soru sayısı: {len(valid_qs)}")
    
    # 3. Batch insert oluşturma ve veritabanına aktarma
    batch_size = 200
    total_batches = (len(valid_qs) + batch_size - 1) // batch_size
    print(f"Toplam {total_batches} paket halinde MySQL'e aktarılacak...")
    
    total_inserted = 0
    for b_idx in range(total_batches):
        batch = valid_qs[b_idx * batch_size : (b_idx + 1) * batch_size]
        
        sql_lines = ["SET NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';"]
        sql_lines.append("INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, level, note) VALUES")
        
        row_sqls = []
        for q in batch:
            row_sql = f"({q['category']}, {q['subcategory']}, {q['language_id']}, '', {escape_sql(q['question'])}, {q['question_type']}, {escape_sql(q['optiona'])}, {escape_sql(q['optionb'])}, {escape_sql(q['optionc'])}, {escape_sql(q['optiond'])}, {escape_sql(q['optione'])}, '{q['answer']}', {q['level']}, {escape_sql(q.get('note', ''))})"
            row_sqls.append(row_sql)
            
        sql_lines.append(",\n".join(row_sqls) + ";")
        full_sql = "\n".join(sql_lines)
        
        run_sql_batch(full_sql)
        total_inserted += len(batch)
        print(f"Paket {b_idx + 1}/{total_batches} başarıyla aktarıldı ({total_inserted}/{len(valid_qs)} soru)...")
        
    print("\n=== Aktarım Tamamlandı! Doğrulama Sorgusu Çalıştırılıyor... ===")
    
    verify_sql = """
    SET NAMES 'utf8mb4';
    SELECT l.id, l.language, COUNT(q.id) as total_questions
    FROM tbl_languages l
    LEFT JOIN tbl_question q ON l.id = q.language_id
    WHERE l.status = 1
    GROUP BY l.id, l.language
    ORDER BY l.id;
    """
    res = run_sql_batch(verify_sql)
    print("=== DİL BAZLI SORU SAYILARI ===")
    print(res)

if __name__ == '__main__':
    main()
