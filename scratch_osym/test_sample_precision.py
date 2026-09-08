import pymupdf, re

def parse_sample_page(page, pno, year):
    # Find DOĞRU CEVAP
    blocks = page.get_text('blocks')
    ans_block = None
    for b in blocks:
        m = re.search(r'DOĞRU CEVAP\s*:\s*([A-E])', b[4], re.IGNORECASE)
        if m:
            ans_block = (b, m.group(1).lower())
            break
            
    if not ans_block:
        return None
        
    b_ans, ans = ans_block
    ans_x0, ans_y0 = b_ans[0], b_ans[1]
    
    # Determine column: left if ans_x0 < page.rect.width / 2 else right
    col_x_min = 0 if ans_x0 < page.rect.width / 2 else page.rect.width / 2
    col_x_max = page.rect.width / 2 if ans_x0 < page.rect.width / 2 else page.rect.width
    
    # Collect words belonging to this question:
    # 1. in same column (col_x_min <= x <= col_x_max)
    # 2. above ans_y0 (y1 <= ans_y0 + 5)
    # 3. not in watermark
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
                
    # Sort into lines
    q_words = sorted(q_words, key=lambda item: (item[1], item[0]))
    lines = []
    cur_line = []
    cur_y = None
    for w in q_words:
        if cur_y is None:
            cur_y = w[1]
            cur_line.append(w)
        elif abs(w[1] - cur_y) < 4.5:
            cur_line.append(w)
        else:
            cur_line.sort(key=lambda item: item[0])
            lines.append(' '.join(item[4] for item in cur_line))
            cur_line = [w]
            cur_y = w[1]
    if cur_line:
        cur_line.sort(key=lambda item: item[0])
        lines.append(' '.join(item[4] for item in cur_line))
        
    # Strip standalone numbers at the top of the column (e.g. '51.', '52.', etc.)
    real_lines = []
    started = False
    for l in lines:
        if re.match(r'^\s*\d{1,2}\.\s*$', l):
            continue # standalone placeholder number
        if any(k in l.lower() for k in ['bu testte', 'cevaplarınız', 'ayrılan kısmına', 'diğer sayfaya']):
            continue
        real_lines.append(l)
        
    full_q_text = '\n'.join(real_lines).strip()
    
    # Split into question text and options A, B, C, D, E
    opt_pattern = re.compile(r'(?:^|\s+)([A-E])\)\s*')
    opt_splits = list(opt_pattern.finditer(full_q_text))
    
    if len(opt_splits) < 5:
        return None
        
    a_idx = -1
    for idx, sm in enumerate(opt_splits):
        if sm.group(1) == 'A':
            a_idx = idx
            break
    if a_idx == -1 or len(opt_splits) < a_idx + 5:
        return None
        
    q_body = full_q_text[:opt_splits[a_idx].start()].strip()
    q_body = re.sub(r'^\s*\d{1,2}\.\s*', '', q_body).strip()
    
    opt_dict = {}
    for k in range(5):
        curr_m = opt_splits[a_idx + k]
        letter = curr_m.group(1).lower()
        if k < 4:
            next_m = opt_splits[a_idx + k + 1]
            val = full_q_text[curr_m.end():next_m.start()].strip()
        else:
            val = full_q_text[curr_m.end():].strip()
        # Clean trailing
        val = re.split(r'\n\s*(?:\d{1,2}\.|Diğer|DOĞRU|ÖSYM|Bu soruların)', val, flags=re.IGNORECASE)[0].strip()
        opt_dict[f'option{letter}'] = val
        
    # Test type from page
    test_type = 'GY' if 'YETENEK' in page.get_text().upper() else 'GK'
    
    return {
        'year': year,
        'page': pno + 1,
        'test': test_type,
        'question': q_body,
        'optiona': opt_dict.get('optiona', ''),
        'optionb': opt_dict.get('optionb', ''),
        'optionc': opt_dict.get('optionc', ''),
        'optiond': opt_dict.get('optiond', ''),
        'optione': opt_dict.get('optione', ''),
        'answer': ans
    }

for y in [2024, 2023, 2022, 2018]:
    doc = pymupdf.open(f'd:/quiza/scratch_osym/{y}.pdf')
    results = []
    for pno in range(len(doc)):
        res = parse_sample_page(doc[pno], pno, y)
        if res:
            results.append(res)
    print(f"=== Year {y}: {len(results)} sample questions successfully parsed ===")
    for r in results[:2]:
        print(f"  P.{r['page']} [{r['test']}] Ans: {r['answer'].upper()} | {r['question'][:60]}... | A: {r['optiona']} | E: {r['optione']}")
