# -*- coding: utf-8 -*-
"""
Hazır Kitap Sorularını (cleaned_hmgs_book.json ve extracted_anayasa_book.json)
İlgili Alt Kategorilere Eşleme ve Yükleme Modülü
"""
import json, re

def get_book_questions(subcat_by_slug):
    questions = []
    
    # 1. cleaned_hmgs_book.json (237 Soru - İdare ve İYUK Ağırlıklı)
    try:
        with open('d:/quiza/scratch_osym/cleaned_hmgs_book.json', 'r', encoding='utf-8') as f:
            hmgs_data = json.load(f)
            
        for i, q in enumerate(hmgs_data):
            q_text = q['question'].strip()
            sol = q.get('solution', '').strip()
            ans = q['answer'].lower().strip()
            
            # Konu tespitine göre HMGS alt kategorisi belirleme
            # 97: hmgs-idare-teskilat
            # 98: hmgs-idare-islemler
            # 99: hmgs-iyuk-davalar
            lower_q = q_text.lower() + " " + sol.lower()
            if 'dava' in lower_q or 'iptal' in lower_q or 'yürütme' in lower_q or 'danıştay' in lower_q or 'süre' in lower_q:
                sub = subcat_by_slug.get('hmgs-iyuk-davalar')
            elif 'kamu mal' in lower_q or 'kamulaştırma' in lower_q or 'idari işlem' in lower_q or 'sözleşme' in lower_q:
                sub = subcat_by_slug.get('hmgs-idare-islemler')
            else:
                sub = subcat_by_slug.get('hmgs-idare-teskilat')
                
            if not sub:
                continue
                
            level = (i % 10) + 1
            note = f"HMGS & Hâkimlik Akademisi Açıklamalı Çözümü: {sol}" if sol else "2577 sayılı İYUK ve İdare Hukuku mevzuat hükümleri uyarınca doğru şık belirlenmiştir."
            
            questions.append({
                'category': sub['category_id'],
                'subcategory': sub['subcat_id'],
                'language_id': sub['language_id'],
                'question': q_text,
                'question_type': 1,
                'optiona': q['optiona'].strip(),
                'optionb': q['optionb'].strip(),
                'optionc': q['optionc'].strip(),
                'optiond': q['optiond'].strip(),
                'optione': q['optione'].strip(),
                'answer': ans,
                'level': level,
                'note': note
            })
    except Exception as e:
        print("HMGS kitap import hatası:", e)

    # 2. extracted_anayasa_book.json (195 Soru - Anayasa Hukuku)
    try:
        with open('d:/quiza/scratch_osym/extracted_anayasa_book.json', 'r', encoding='utf-8') as f:
            ay_data = json.load(f)
            
        for i, q in enumerate(ay_data):
            q_text = q['question'].strip()
            sol = q.get('solution', '').strip()
            ans = q['answer'].lower().strip()
            
            lower_q = q_text.lower() + " " + sol.lower()
            # 94: hmgs-ay-haklar
            # 95: hmgs-ay-organlar
            # 96: hmgs-ay-yargisi
            if 'anayasa mahkemesi' in lower_q or 'iptal' in lower_q or 'bireysel başvuru' in lower_q or 'itiraz' in lower_q:
                sub = subcat_by_slug.get('hmgs-ay-yargisi')
            elif 'tbmm' in lower_q or 'cumhurbaşkanı' in lower_q or 'bakan' in lower_q or 'seçim' in lower_q or 'kanun' in lower_q:
                sub = subcat_by_slug.get('hmgs-ay-organlar')
            else:
                sub = subcat_by_slug.get('hmgs-ay-haklar')
                
            if not sub:
                continue
                
            level = (i % 10) + 1
            note = f"1982 T.C. Anayasası İncelemesi ve Çözümü: {sol}" if sol else "1982 Anayasası ilgili maddeleri doğrultusunda çözülmüştür."
            
            questions.append({
                'category': sub['category_id'],
                'subcategory': sub['subcat_id'],
                'language_id': sub['language_id'],
                'question': q_text,
                'question_type': 1,
                'optiona': q['optiona'].strip(),
                'optionb': q['optionb'].strip(),
                'optionc': q['optionc'].strip(),
                'optiond': q['optiond'].strip(),
                'optione': q['optione'].strip(),
                'answer': ans,
                'level': level,
                'note': note
            })
    except Exception as e:
        print("Anayasa kitap import hatası:", e)
        
    print(f"Kitaplardan aktarılan toplam kaliteli soru sayısı: {len(questions)}")
    return questions

if __name__ == '__main__':
    with open('d:/quiza/scratch_osym/law_subcats_map.json', 'r', encoding='utf-8') as f:
        subcats = json.load(f)
    subcat_by_slug = {s['slug']: s for s in subcats}
    qs = get_book_questions(subcat_by_slug)
    print("Örnek:", qs[0]['question'][:60], "Alt Kategori ID:", qs[0]['subcategory'])
