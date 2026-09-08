import sys, os, re, subprocess
sys.path.append(r'd:\quiza\scratch_osym')
import pymupdf
from parse_answer_keys import parse_answer_keys
from kpss_extractor import extract_lines_from_words, get_subcategory_mapping

WATERMARK_WORDS = set([
    'ösym', 'ösym’ye', 'ösym\'ye', 'ösymnin', 'ösym’nin', 'ösym\'nin',
    'telif', 'hakları', 'haklar', 'haklari', 'aittir', 'yazılı', 'yazl',
    'izni', 'olmaksızın', 'olmakszn', 'hiçbir', 'hibir', 'kişi', 'kisi',
    'kurum', 'kuruluş', 'kurulua', 'kurulus', 'tarafından', 'tarafndan',
    'kullanılamaz', 'kullanlamaz', 'soruların', 'sorularn', 'sorular'
])

def clean_watermark(text):
    text = re.sub(r'Bu soruların telif hakları.*?(?:kullanılamaz\.?)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Bu testlerin her hakkı saklıdır.*?(?:sayılır\.?)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Diğer sayfaya geçiniz\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'TEST BİTTİ\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'CEVAPLARINIZI KONTROL EDİNİZ\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'GENEL KÜLTÜR TESTİ BİTTİ\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'GENEL YETENEK TESTİ BİTTİ\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'GENEL KÜLTÜR TESTİNE GEÇİNİZ\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'GENEL YETENEK TESTİNE GEÇİNİZ\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'kısmına işaretleyiniz\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'ayrılan kısmına\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Bu testte \d+ soru vardır\.?', '', text, flags=re.IGNORECASE)
    
    # Filter individual scattered tokens
    words = text.split()
    clean = []
    for w in words:
        clean_w = re.sub(r'[^\w]', '', w).lower()
        if clean_w in WATERMARK_WORDS:
            continue
        if len(w) == 1 and w.upper() in ['Ö', 'S', 'Y', 'M']:
            continue
        clean.append(w)
    res = ' '.join(clean)
    res = re.sub(r'^\s*[:\-\.]\s*', '', res)
    res = re.sub(r'\s+', ' ', res).strip()
    return res

def clean_option(txt):
    txt = re.split(r'\n\s*(?:\d{1,2}\.|Diğer|DOĞRU|ÖSYM|Bu soruların|TEST BİTTİ|CEVAPLARINIZI)', txt, flags=re.IGNORECASE)[0].strip()
    txt = clean_watermark(txt)
    # Remove trailing page or question numbers
    txt = re.sub(r'\s+\d{1,2}\s*$', '', txt)
    return txt.strip()

def clean_question(txt):
    txt = clean_watermark(txt)
    # Remove leading numbers like "12."
    txt = re.sub(r'^\s*\d{1,2}\.\s*', '', txt).strip()
    return txt.strip()

def is_math_problematic(q_text):
    # Check if a math question requires missing visual drawing or geometry figure
    q_low = q_text.lower()
    skip_keywords = [
        'üçgen', 'dörtgen', 'çember', 'daire grafiği', 'grafikte', 'şekildeki',
        'koordinat düzlemi', 'doğrusu üzerinde', 'alanı kaç birimkaredir',
        'kaç derecedir', 'şekil 1', 'şekil 2', 'şekilde verilen', 'boyalı bölge',
        'taranmış alan', 'yamuk', 'paralelkenar', 'kare dik prizma', 'dik koordinat'
    ]
    return any(k in q_low for k in skip_keywords)

def is_geography_problematic(q_text):
    q_low = q_text.lower()
    skip_keywords = [
        'haritada numaralandırılmış', 'haritada taranarak', 'haritadaki alanlar',
        'haritaya göre', 'grafiğe göre', 'tabloya göre', 'haritada gösterilen'
    ]
    return any(k in q_low for k in skip_keywords)

def parse_full_booklet(year, gy_range, gk_range, answer_keys):
    pdf_path = f'd:/quiza/scratch_osym/{year}.pdf'
    if not os.path.exists(pdf_path): return []
    doc = pymupdf.open(pdf_path)
    extracted = []
    
    for test_type, p_range in [('GY', gy_range), ('GK', gk_range)]:
        start_p, end_p = p_range
        stream = []
        for pno in range(start_p - 1, end_p):
            page = doc[pno]
            w, h = page.rect.width, page.rect.height
            words = [wrd for wrd in page.get_text('words') if 70 <= wrd[1] <= h - 45]
            left_words = [wrd for wrd in words if wrd[0] < w / 2]
            right_words = [wrd for wrd in words if wrd[0] >= w / 2]
            lines_l = extract_lines_from_words(left_words)
            lines_r = extract_lines_from_words(right_words)
            for l in lines_l + lines_r:
                l_clean = re.sub(r'^\s*ÖSYM\s*', '', l, flags=re.IGNORECASE)
                l_low = l_clean.lower()
                if any(k in l_low for k in ['bu testte', 'cevaplarınız', 'cevaplarnz', 'ayrılan kısmına', 'ayrlan ksmna']):
                    continue
                stream.append(l_clean)
                
        full_text = '\n'.join(stream)
        pattern = re.compile(r'(?:^|\n)\s*(\d{1,2})\.\s+', re.MULTILINE)
        matches = list(pattern.finditer(full_text))
        
        valid_q_matches = []
        expected = 1
        for m in matches:
            num = int(m.group(1))
            if num == expected:
                valid_q_matches.append((num, m.start()))
                expected += 1
            elif num == expected + 1 and expected > 1:
                valid_q_matches.append((num, m.start()))
                expected = num + 1
                
        for i, (qnum, start_idx) in enumerate(valid_q_matches):
            end_idx = valid_q_matches[i+1][1] if i + 1 < len(valid_q_matches) else len(full_text)
            block = full_text[start_idx:end_idx].strip()
            block = re.sub(r'^\s*\d{1,2}\.\s*', '', block).strip()
            
            opt_pattern = re.compile(r'(?:^|\s+)([A-E])\)\s*')
            opt_splits = list(opt_pattern.finditer(block))
            
            opt_dict = {}
            q_text = block
            if len(opt_splits) >= 5:
                a_idx = -1
                for idx, sm in enumerate(opt_splits):
                    if sm.group(1) == 'A':
                        a_idx = idx
                        break
                if a_idx != -1 and len(opt_splits) >= a_idx + 5:
                    q_text = block[:opt_splits[a_idx].start()].strip()
                    for k in range(5):
                        curr_m = opt_splits[a_idx + k]
                        letter = curr_m.group(1).lower()
                        if k < 4:
                            next_m = opt_splits[a_idx + k + 1]
                            val = block[curr_m.end():next_m.start()].strip()
                        else:
                            val = block[curr_m.end():].strip()
                        opt_dict[f'option{letter}'] = clean_option(val)
                        
            q_text = clean_question(q_text)
            ans = answer_keys.get((year, test_type, qnum), '')
            
            if not all(opt_dict.get(f'option{c}') for c in ['a', 'b', 'c', 'd', 'e']):
                continue
            if ans not in ['a', 'b', 'c', 'd', 'e']:
                continue
            if len(q_text) < 15:
                continue
                
            cat = 0
            if test_type == 'GK':
                if qnum <= 27:
                    cat = 1 # Tarih
                elif qnum <= 45:
                    cat = 2 # Coğrafya
                else:
                    cat = 3 # Vatandaşlık & Güncel
            elif test_type == 'GY':
                if qnum <= 30:
                    cat = 4 # Türkçe
                else:
                    cat = 5 # Matematik
                    
            if cat == 2 and is_geography_problematic(q_text):
                continue
            if cat == 5 and is_math_problematic(q_text):
                continue
                
            subcat = get_subcategory_mapping(cat, qnum, q_text)
            test_title = "Genel Kültür" if test_type == 'GK' else "Genel Yetenek"
            
            extracted.append({
                'year': year,
                'test': test_type,
                'qnum': qnum,
                'category': cat,
                'subcategory': subcat,
                'question': f"[{year} KPSS Çıkmış Soru]\n\n{q_text}",
                'optiona': opt_dict['optiona'],
                'optionb': opt_dict['optionb'],
                'optionc': opt_dict['optionc'],
                'optiond': opt_dict['optiond'],
                'optione': opt_dict['optione'],
                'answer': ans,
                'note': f"{year} KPSS Lisans {test_title} oturumunda ÖSYM tarafından sorulmuş orijinal çıkmış sınav sorusudur."
            })
            
    return extracted

def parse_sample_booklet(year):
    pdf_path = f'd:/quiza/scratch_osym/{year}.pdf'
    if not os.path.exists(pdf_path): return []
    doc = pymupdf.open(pdf_path)
    extracted = []
    
    for pno in range(len(doc)):
        page = doc[pno]
        raw_text = page.get_text()
        ans_match = re.search(r'DOĞRU CEVAP\s*:\s*([A-E])', raw_text, re.IGNORECASE)
        if not ans_match:
            continue
        ans = ans_match.group(1).lower()
        
        # Test type: check if GY or GK in header
        first_line = raw_text.split('\n')[0].upper()
        if 'GY' in first_line or 'YETENEK' in raw_text.upper()[:100]:
            test_type = 'GY'
        else:
            test_type = 'GK'
            
        ans_y0 = page.rect.height
        for b in page.get_text('blocks'):
            if 'DOĞRU CEVAP' in b[4].upper():
                ans_y0 = b[1]
                ans_x0 = b[0]
                break
                
        col_x_min = 0 if ans_x0 < page.rect.width / 2 else page.rect.width / 2
        col_x_max = page.rect.width / 2 if ans_x0 < page.rect.width / 2 else page.rect.width
        
        words = page.get_text('words')
        q_words = []
        for w in words:
            if 'telif' in w[4].lower() or 'haklar' in w[4].lower() or 'ösym' in w[4].lower():
                continue
            if len(w[4]) == 1 and w[4].upper() in ['Ö', 'S', 'Y', 'M']:
                continue
            if col_x_min <= w[0] and w[2] <= col_x_max + 10:
                if 70 <= w[1] and w[3] <= ans_y0 + 5:
                    q_words.append(w)
                    
        lines = extract_lines_from_words(q_words)
        real_lines = []
        for l in lines:
            if re.match(r'^\s*\d{1,2}\.\s*$', l):
                continue
            if any(k in l.lower() for k in ['bu testte', 'cevaplarınız', 'ayrılan kısmına', 'diğer sayfaya']):
                continue
            real_lines.append(l)
            
        full_q_text = '\n'.join(real_lines).strip()
        opt_pattern = re.compile(r'(?:^|\s+)([A-E])\)\s*')
        opt_splits = list(opt_pattern.finditer(full_q_text))
        
        if len(opt_splits) < 5:
            continue
        a_idx = -1
        for idx, sm in enumerate(opt_splits):
            if sm.group(1) == 'A':
                a_idx = idx
                break
        if a_idx == -1 or len(opt_splits) < a_idx + 5:
            continue
            
        q_body = full_q_text[:opt_splits[a_idx].start()].strip()
        q_body = clean_question(q_body)
        
        opt_dict = {}
        for k in range(5):
            curr_m = opt_splits[a_idx + k]
            letter = curr_m.group(1).lower()
            if k < 4:
                next_m = opt_splits[a_idx + k + 1]
                val = full_q_text[curr_m.end():next_m.start()].strip()
            else:
                val = full_q_text[curr_m.end():].strip()
            opt_dict[f'option{letter}'] = clean_option(val)
            
        if len(q_body) < 15 or not all(opt_dict.get(f'option{c}') for c in ['a', 'b', 'c', 'd', 'e']):
            continue
            
        qnum_m = re.search(r'\b(\d{1,2})\.\s+', raw_text)
        qnum = int(qnum_m.group(1)) if qnum_m else 1
        
        cat = 0
        if test_type == 'GK':
            if qnum <= 27: cat = 1
            elif qnum <= 45: cat = 2
            else: cat = 3
        else:
            if qnum <= 30: cat = 4
            else: cat = 5
            
        if cat == 2 and is_geography_problematic(q_body):
            continue
        if cat == 5 and is_math_problematic(q_body):
            continue
            
        subcat = get_subcategory_mapping(cat, qnum, q_body)
        test_title = "Genel Kültür" if test_type == 'GK' else "Genel Yetenek"
        
        extracted.append({
            'year': year,
            'test': test_type,
            'qnum': qnum,
            'category': cat,
            'subcategory': subcat,
            'question': f"[{year} KPSS Çıkmış Soru]\n\n{q_body}",
            'optiona': opt_dict['optiona'],
            'optionb': opt_dict['optionb'],
            'optionc': opt_dict['optionc'],
            'optiond': opt_dict['optiond'],
            'optione': opt_dict['optione'],
            'answer': ans,
            'note': f"{year} KPSS Lisans {test_title} oturumunda ÖSYM tarafından sorulmuş orijinal çıkmış sınav sorusudur."
        })
        
    return extracted

def sql_escape(s):
    if s is None:
        return "''"
    s = str(s).replace('\\', '\\\\').replace("'", "\\'")
    return f"'{s}'"

def main():
    keys = parse_answer_keys()
    
    full_ranges = {
        2021: ((3, 20), (21, 33)),
        2020: ((3, 20), (21, 33)),
        2019: ((3, 20), (21, 32)),
        2017: ((3, 21), (22, 34)),
        2016: ((3, 17), (18, 28)),
        2015: ((3, 17), (18, 27)),
        2014: ((3, 18), (19, 29)),
        2013: ((3, 21), (22, 32)),
        2012: ((3, 19), (20, 30)),
        2010: ((2, 15), (16, 29)),
        2009: ((2, 15), (16, 29)),
    }
    
    all_questions = []
    
    # 1. Samples
    for y in [2024, 2023, 2022, 2018]:
        qs = parse_sample_booklet(y)
        print(f"Sample {y}: {len(qs)} questions extracted")
        all_questions.extend(qs)
        
    # 2. Full booklets
    for y, (gy_r, gk_r) in full_ranges.items():
        qs = parse_full_booklet(y, gy_r, gk_r, keys)
        print(f"Full {y}: {len(qs)} questions extracted")
        all_questions.extend(qs)
        
    print(f"\nTotal extracted before deduplication: {len(all_questions)}")
    
    # Deduplicate by normalized question body
    seen = set()
    unique_questions = []
    for q in all_questions:
        norm = re.sub(r'[^\w]', '', q['question']).lower()
        if norm in seen:
            continue
        seen.add(norm)
        unique_questions.append(q)
        
    print(f"Total unique questions to insert: {len(unique_questions)}")
    
    # Print summary by Category
    cat_names = {1: "Tarih", 2: "Coğrafya", 3: "Vatandaşlık & Güncel", 4: "Türkçe", 5: "Matematik"}
    cat_counts = {}
    for q in unique_questions:
        cat_counts[q['category']] = cat_counts.get(q['category'], 0) + 1
    for cid, cnt in sorted(cat_counts.items()):
        print(f"  Category {cid} ({cat_names.get(cid, 'Unknown')}): {cnt} questions")
        
    # Generate SQL file
    sql_path = 'd:/quiza/scratch_osym/insert_kpss.sql'
    with open(sql_path, 'w', encoding='utf-8') as f:
        f.write("SET NAMES utf8mb4;\n")
        f.write("START TRANSACTION;\n\n")
        
        for q in unique_questions:
            vals = [
                str(q['category']),
                str(q['subcategory']),
                "52", # language_id
                "''", # image
                sql_escape(q['question']),
                "1",  # question_type (multiple choice)
                sql_escape(q['optiona']),
                sql_escape(q['optionb']),
                sql_escape(q['optionc']),
                sql_escape(q['optiond']),
                sql_escape(q['optione']),
                sql_escape(q['answer']),
                "1",  # level
                sql_escape(q['note'])
            ]
            f.write(f"INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, level, note) VALUES ({', '.join(vals)});\n")
            
        f.write("\nCOMMIT;\n")
        
    print(f"\nSQL script written to {sql_path} ({os.path.getsize(sql_path)} bytes)")
    
    # Pipe SQL into live MySQL container via SSH
    print("Executing SQL on live database root@142.93.104.78...")
    with open(sql_path, 'rb') as sql_file:
        proc = subprocess.run(
            ['ssh', 'root@142.93.104.78', 'docker exec -i elitequiz_db mysql --default-character-set=utf8mb4 -uelite_user -pelite_user_pass_2026 elite_quiz_db'],
            stdin=sql_file,
            capture_output=True,
            text=True
        )
    print("MySQL Return Code:", proc.returncode)
    if proc.stdout:
        print("MySQL STDOUT:", proc.stdout)
    if proc.stderr:
        print("MySQL STDERR:", proc.stderr)
        
if __name__ == '__main__':
    main()
