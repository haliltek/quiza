import re, urllib.request, gzip, sys
sys.stdout.reconfigure(encoding='utf-8')

# Load embed HTML to get all page URLs
with open('d:/quiza/scratch_osym/scribd_embed.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

matches = re.findall(r'pageNum:\s*(\d+).*?contentUrl:\s*"([^"]+)"', html, re.DOTALL)
page_urls = {int(p): url for p, url in matches}
print(f"Total available page URLs: {len(page_urls)}")

def fetch_page_raw(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=5) as resp:
        raw = resp.read()
        if raw[:2] == b'\x1f\x8b':
            return gzip.decompress(raw).decode('utf-8', errors='ignore')
        return raw.decode('utf-8', errors='ignore')

def parse_page_questions(pnum, data):
    # Extract plain text
    # In Scribd JSONP: window.pageN_callback(["...HTML..."]);
    # Clean HTML tags
    text = re.sub(r'<[^>]+>', ' ', data)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Check if page has question pattern e.g. "1. Aşağıdakilerden..." or "1.\n"
    # Find all question numbers: \b(\d{1,3})\.\s+
    # In this book, each page typically has 2 questions, e.g. 1 & 2, or 3 & 4.
    # And after each question there is options A..E, then explanation, then CEVAP: X
    # Let's inspect the regex:
    q_matches = list(re.finditer(r'(?:^|\s)(\d{1,3})\.\s+', text))
    if not q_matches:
        return []
        
    page_questions = []
    for idx, qm in enumerate(q_matches):
        qnum = int(qm.group(1))
        start_pos = qm.start()
        end_pos = q_matches[idx+1].start() if idx + 1 < len(q_matches) else len(text)
        chunk = text[start_pos:end_pos].strip()
        
        # Check if CEVAP: [A-E] exists in chunk
        ans_m = re.search(r'CEVAP\s*:\s*([A-E])', chunk, re.IGNORECASE)
        if not ans_m:
            continue
        ans = ans_m.group(1).lower()
        
        # Everything before CEVAP is question + options + solution
        before_ans = chunk[:ans_m.start()].strip()
        
        # Options A) B) C) D) E)
        opt_pattern = re.compile(r'(?:^|\s+)([A-E])\)\s*')
        opt_splits = list(opt_pattern.finditer(before_ans))
        
        if len(opt_splits) < 5:
            continue
            
        a_idx = -1
        for s_i, sm in enumerate(opt_splits):
            if sm.group(1) == 'A':
                a_idx = s_i
                break
        if a_idx == -1 or len(opt_splits) < a_idx + 5:
            continue
            
        # Question text is before A)
        q_text = before_ans[:opt_splits[a_idx].start()].strip()
        # Remove leading "N. "
        q_text = re.sub(r'^\s*\d{1,3}\.\s*', '', q_text).strip()
        
        # Options
        opt_dict = {}
        for k in range(5):
            curr_m = opt_splits[a_idx + k]
            letter = curr_m.group(1).lower()
            if k < 4:
                next_m = opt_splits[a_idx + k + 1]
                val = before_ans[curr_m.end():next_m.start()].strip()
            else:
                # Option E ends where solution / ÇÖZÜM or sentence begins
                rem = before_ans[curr_m.end():].strip()
                # Usually after option E there is solution text:
                # e.g. "İç düzen - öz yönetim faaliyetleri İdarenin ekonomik faaliyetleri sosyal devlet..."
                # Or marked with "ÇÖZÜM" or sentence
                val = rem
            opt_dict[f'option{letter}'] = val
            
        # Option E and Solution separation:
        # In this book, option E text is followed by the solution text.
        # Let's inspect how option E and solution are separated!
        page_questions.append({
            'page': pnum,
            'qnum': qnum,
            'question': q_text,
            'optiona': opt_dict['optiona'],
            'optionb': opt_dict['optionb'],
            'optionc': opt_dict['optionc'],
            'optiond': opt_dict['optiond'],
            'optione_raw': opt_dict['optione'],
            'answer': ans,
            'chunk': chunk
        })
    return page_questions

# Test on pages 5, 6, 7
for p in [5, 6, 7]:
    if p in page_urls:
        raw = fetch_page_raw(page_urls[p])
        qs = parse_page_questions(p, raw)
        print(f"Page {p} extracted {len(qs)} questions:")
        for q in qs:
            print(f"  Q{q['qnum']} | Ans: {q['answer'].upper()} | Text: {q['question'][:60]}...")
            print(f"    A: {q['optiona'][:30]} | D: {q['optiond'][:30]}")
            print(f"    E_raw: {q['optione_raw'][:80]}...")
