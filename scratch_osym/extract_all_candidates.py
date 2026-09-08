import sys, os, re
sys.path.append(r'd:\quiza\scratch_osym')
import pymupdf
from parse_answer_keys import parse_answer_keys
from kpss_extractor import extract_lines_from_words, get_subcategory_mapping, clean_question_text, clean_option_text

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
        
        # Match question start numbers
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
            
            # Options
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
                        opt_dict[f'option{letter}'] = clean_option_text(val)
                        
            q_text = clean_question_text(q_text)
            
            # Answer
            ans = answer_keys.get((year, test_type, qnum), '')
            
            # Filter checks
            # 1. Must have all 5 options
            if not all(opt_dict.get(f'option{c}') for c in ['a', 'b', 'c', 'd', 'e']):
                continue
            # 2. Must have valid answer
            if ans not in ['a', 'b', 'c', 'd', 'e']:
                continue
            # 3. Question text length
            if len(q_text) < 15:
                continue
            # 4. Skip questions requiring missing maps / visual graphs
            q_low = q_text.lower()
            if any(k in q_low for k in ['haritada numaralandırılmış', 'haritada taranarak', 'haritadaki alanlar', 'haritaya göre', 'grafiğe göre', 'tabloya göre']):
                continue
                
            # Determine category & subcategory
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
                    
            subcat = get_subcategory_mapping(cat, qnum, q_text)
            
            # Test name for note
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
    # For 2024, 2023, 2022, 2018
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
        
        # Test type
        test_type = 'GY' if 'YETENEK' in raw_text.upper() else 'GK'
        
        # Text above DOĞRU CEVAP
        above_txt = raw_text[:ans_match.start()]
        
        # Let's extract lines using words to maintain proper column order if 2 columns
        w, h = page.rect.width, page.rect.height
        words = [wrd for wrd in page.get_text('words') if 70 <= wrd[1] <= h - 45]
        left_words = [wrd for wrd in words if wrd[0] < w / 2]
        right_words = [wrd for wrd in words if wrd[0] >= w / 2]
        lines = extract_lines_from_words(left_words) + extract_lines_from_words(right_words)
        
        # Clean lines
        cleaned_lines = []
        for l in lines:
            if any(k in l.lower() for k in ['bu testte', 'cevaplarınız', 'cevaplarnz', 'doğru cevap', 'dogru cevap', 'telif hakları', 'ö s y m']):
                continue
            cleaned_lines.append(l)
            
        block = '\n'.join(cleaned_lines).strip()
        
        # Options
        opt_pattern = re.compile(r'(?:^|\s+)([A-E])\)\s*')
        opt_splits = list(opt_pattern.finditer(block))
        
        if len(opt_splits) < 5:
            continue
            
        a_idx = -1
        for idx, sm in enumerate(opt_splits):
            if sm.group(1) == 'A':
                a_idx = idx
                break
        if a_idx == -1 or len(opt_splits) < a_idx + 5:
            continue
            
        q_text = block[:opt_splits[a_idx].start()].strip()
        opt_dict = {}
        for k in range(5):
            curr_m = opt_splits[a_idx + k]
            letter = curr_m.group(1).lower()
            if k < 4:
                next_m = opt_splits[a_idx + k + 1]
                val = block[curr_m.end():next_m.start()].strip()
            else:
                val = block[curr_m.end():].strip()
            opt_dict[f'option{letter}'] = clean_option_text(val)
            
        # Clean question text: strip leading question number
        q_text = re.sub(r'^\s*\d{1,2}\.\s*', '', q_text).strip()
        # Remove trailing single standalone numbers
        q_text = re.sub(r'\n\s*\d{1,2}\s*$', '', q_text).strip()
        q_text = clean_question_text(q_text)
        
        if len(q_text) < 15 or not all(opt_dict.get(f'option{c}') for c in ['a', 'b', 'c', 'd', 'e']):
            continue
            
        # Guess question number from block
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

if __name__ == '__main__':
    keys = parse_answer_keys()
    
    all_extracted = []
    
    # 1. Samples
    for y in [2024, 2023, 2022, 2018]:
        qs = parse_sample_booklet(y)
        print(f"Sample {y}: extracted {len(qs)} questions")
        all_extracted.extend(qs)
        
    # 2. Full booklets
    for y, (gy_r, gk_r) in full_ranges.items():
        qs = parse_full_booklet(y, gy_r, gk_r, keys)
        print(f"Full {y}: extracted {len(qs)} questions")
        all_extracted.extend(qs)
        
    print(f"\n==========================================")
    print(f"TOTAL EXTRACTED QUESTIONS: {len(all_extracted)}")
    
    # Summary by Category
    cat_counts = {}
    for q in all_extracted:
        cat_counts[q['category']] = cat_counts.get(q['category'], 0) + 1
    cat_names = {1: "Tarih", 2: "Coğrafya", 3: "Vatandaşlık & Güncel", 4: "Türkçe", 5: "Matematik"}
    for cid, cnt in sorted(cat_counts.items()):
        print(f"  Category {cid} ({cat_names.get(cid, 'Other')}): {cnt} questions")
