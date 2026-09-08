import sys, os, re, json
import pymupdf

def clean_text(txt):
    txt = re.sub(r'Diğer sayfaya geçiniz.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Bu testte \d+ soru vardır.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Cevaplarınızı,.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Bu soruların telif hakları.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Ö S Y M.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'TEST BİTTİ.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'CEVAPLARINIZI KONTROL.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'\s+', ' ', txt).strip()
    return txt

def fix_hyphenation(txt):
    # Join hyphenated words across linebreaks e.g. 'ko- nuşmak' -> 'konuşmak'
    txt = re.sub(r'(\w+)-\s+(\w+)', r'\1\2', txt)
    return txt

def parse_kpss_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)

    # 1. Parse Answer Keys from last pages
    answer_keys = {"GY": {}, "GK": {}}
    ans_page_idx = -1

    for pno in range(total_pages - 1, max(-1, total_pages - 4), -1):
        txt = doc[pno].get_text()
        if "GENEL YETENEK" in txt.upper() and "GENEL KÜLTÜR" in txt.upper():
            lines = txt.split('\n')
            # Look for lines with question answers
            for l in lines:
                # e.g. "1. A   2. B"
                matches = re.findall(r'(\d{1,2})\.\s*([A-Ea-e])\b', l)
                for qnum_str, ans in matches:
                    qn = int(qnum_str)
                    # We will match based on page layout
            # Try blocks
            w = doc[pno].rect.width
            blocks = doc[pno].get_text("blocks")
            found = 0
            for b in blocks:
                b_txt = b[4]
                test = "GY" if b[0] < w / 2 else "GK"
                if "GENEL KÜLTÜR" in b_txt.upper():
                    test = "GK"
                elif "GENEL YETENEK" in b_txt.upper():
                    test = "GY"
                m = re.findall(r'(\d{1,2})\.\s*([A-Ea-e])\b', b_txt)
                for qnum_str, ans in m:
                    qn = int(qnum_str)
                    if qn <= 60:
                        answer_keys[test][qn] = ans.lower()
                        found += 1
            if found > 20:
                ans_page_idx = pno
                break

    # 2. Parse Questions Page by Page
    questions = []
    current_test = "GY"

    for pno in range(total_pages):
        if pno == ans_page_idx:
            continue
        page = doc[pno]
        w, h = page.rect.width, page.rect.height

        # Determine if page switches to GK
        p_raw = page.get_text()
        if re.search(r'GENEL\s+KÜLTÜR\s+TESTİ', p_raw, re.IGNORECASE) and not re.search(r'GENEL\s+KÜLTÜR.*GEÇİNİZ', p_raw, re.IGNORECASE):
            current_test = "GK"
        elif re.search(r'GENEL\s+YETENEK\s+TESTİ', p_raw, re.IGNORECASE) and not re.search(r'GENEL\s+YETENEK.*GEÇİNİZ', p_raw, re.IGNORECASE):
            current_test = "GY"

        # Discard headers (y < 60) and footers (y > h - 45)
        words = [wrd for wrd in page.get_text("words") if 55 <= wrd[1] <= h - 45]
        if not words:
            continue

        # Split into left and right columns by page middle
        mid_x = w / 2
        left_words = [wrd for wrd in words if wrd[0] < mid_x]
        right_words = [wrd for wrd in words if wrd[0] >= mid_x]

        def words_to_lines(wlist):
            if not wlist: return []
            wlist = sorted(wlist, key=lambda it: (it[1], it[0]))
            lines = []
            cur = [wlist[0]]
            cur_y = wlist[0][1]
            for it in wlist[1:]:
                if abs(it[1] - cur_y) < 4.5:
                    cur.append(it)
                else:
                    cur.sort(key=lambda x: x[0])
                    lines.append(" ".join(x[4] for x in cur))
                    cur = [it]
                    cur_y = it[1]
            if cur:
                cur.sort(key=lambda x: x[0])
                lines.append(" ".join(x[4] for x in cur))
            return lines

        col_lines = words_to_lines(left_words) + words_to_lines(right_words)

        cur_q = None
        for line in col_lines:
            line_str = line.strip()
            if not line_str:
                continue

            # Ignore stray headers/footers
            if line_str in ['A', 'B', 'C', 'D'] and len(line_str) == 1:
                continue
            if re.match(r'^(?:20\d{2}\s*-\s*KPSS|Diğer sayfaya|Sayfa\s+\d+|\d+$)', line_str, re.I):
                continue

            # Check question start: "1. ", "2. ", "60. "
            qm = re.match(r'^(\d{1,2})\.\s*(.*)', line_str)
            if qm and int(qm.group(1)) <= 60:
                qn = int(qm.group(1))
                if cur_q and cur_q['optiona']:
                    questions.append(cur_q)

                ans = answer_keys[current_test].get(qn, 'a')

                # Category & Subcategory mapping
                if current_test == "GY":
                    if qn <= 30:
                        cat_id = 4 # Türkçe
                        sub_id = 18
                        subject = "Türkçe"
                    else:
                        cat_id = 5 # Matematik
                        sub_id = 22
                        subject = "Matematik"
                else: # GK
                    if qn <= 27:
                        cat_id = 1 # Tarih
                        sub_id = 1
                        subject = "Tarih"
                    elif qn <= 45:
                        cat_id = 2 # Coğrafya
                        sub_id = 8
                        subject = "Coğrafya"
                    elif qn <= 54:
                        cat_id = 3 # Vatandaşlık
                        sub_id = 13
                        subject = "Vatandaşlık"
                    else:
                        cat_id = 3 # Güncel
                        sub_id = 17
                        subject = "Güncel Bilgiler"

                sec_name = "Genel Yetenek" if current_test == "GY" else "Genel Kültür"
                cur_q = {
                    "qnum": qn,
                    "test": current_test,
                    "subject": subject,
                    "category": cat_id,
                    "subcategory": sub_id,
                    "question": qm.group(2).strip(),
                    "optiona": "",
                    "optionb": "",
                    "optionc": "",
                    "optiond": "",
                    "optione": "",
                    "answer": ans,
                    "solution": f"ÖSYM KPSS {sec_name} ({subject}) {qn}. Soru. Resmi Doğru Cevap: {ans.upper()}"
                }
                continue

            if not cur_q:
                continue

            # Check options on this line: matches A) ... B) ... etc.
            opt_matches = list(re.finditer(r'([A-E])\)\s*', line_str))
            if opt_matches:
                for idx, m in enumerate(opt_matches):
                    let = m.group(1).lower()
                    v_start = m.end()
                    v_end = opt_matches[idx + 1].start() if idx + 1 < len(opt_matches) else len(line_str)
                    val = line_str[v_start:v_end].strip()
                    cur_q['option' + let] = val
                continue

            # Continuation line
            # If options haven't started, append to question text
            if not cur_q['optiona']:
                cur_q['question'] += " " + line_str
            else:
                # It belongs to the last option read, BUT check if it's junk/header
                if cur_q['optione']:
                    # Don't append if it's stray single letter or header
                    if len(line_str) > 1 and not re.match(r'^(?:ÖSYM|KPSS|GENEL)', line_str, re.I):
                        cur_q['optione'] += " " + line_str
                elif cur_q['optiond']:
                    cur_q['optiond'] += " " + line_str
                elif cur_q['optionc']:
                    cur_q['optionc'] += " " + line_str
                elif cur_q['optionb']:
                    cur_q['optionb'] += " " + line_str
                elif cur_q['optiona']:
                    cur_q['optiona'] += " " + line_str

        if cur_q and cur_q['optiona']:
            questions.append(cur_q)

    # Post-clean all questions
    for q in questions:
        q['question'] = fix_hyphenation(clean_text(q['question']))
        for let in ['a', 'b', 'c', 'd', 'e']:
            q['option' + let] = fix_hyphenation(clean_text(q['option' + let]))

    return questions

if __name__ == '__main__':
    qs = parse_kpss_pdf('d:/quiza/scratch_osym/2009.pdf')
    print(f"Total extracted questions: {len(qs)}")
    
    # Check questions 1, 2 of GK
    gk_qs = [q for q in qs if q['test'] == 'GK']
    print(f"GK questions count: {len(gk_qs)}")
    if gk_qs:
        for q in gk_qs[:3]:
            print(f"\n--- GK Soru {q['qnum']} ({q['subject']}) ---")
            print("Soru:", q['question'])
            print("A:", q['optiona'])
            print("B:", q['optionb'])
            print("C:", q['optionc'])
            print("D:", q['optiond'])
            print("E:", q['optione'])
            print("Cevap:", q['answer'])

    # Check question 28 of GY (User's question)
    gy_qs = [q for q in qs if q['test'] == 'GY' and q['qnum'] == 28]
    if gy_qs:
        q = gy_qs[0]
        print(f"\n--- GY Soru 28 ({q['subject']}) ---")
        print("Soru:", q['question'])
        print("A:", q['optiona'])
        print("B:", q['optionb'])
        print("C:", q['optionc'])
        print("D:", q['optiond'])
        print("E:", q['optione'])
        print("Cevap:", q['answer'])
