import sys, os, re, json
import pymupdf

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def clean_text(txt):
    txt = re.sub(r'Diğer sayfaya geçiniz.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Bu testte \d+ soru vardır.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Cevaplarınızı,.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Bu soruların telif hakları.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'Ö S Y M.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'TEST BİTTİ.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'CEVAPLARINIZI KONTROL.*', '', txt, flags=re.IGNORECASE)
    txt = re.sub(r'\bTEST[İI]?\b', '', txt)
    txt = re.sub(r'\s+', ' ', txt).strip()
    return txt

def fix_hyphenation(txt):
    # Join hyphenated words across lines e.g. 'ko- nuşmak' -> 'konuşmak'
    txt = re.sub(r'(\w+)-\s+(\w+)', r'\1\2', txt)
    return txt

EXAM_CONFIGS = {
    "auto_kpss_lisans": {
        "name": "KPSS Lisans (B Grubu - GY-GK)",
        "lang_id": 52,
        "gy_turkce": {"cat": 4, "sub": 18, "subject": "Türkçe"},
        "gy_mat": {"cat": 5, "sub": 22, "subject": "Matematik & Mantık"},
        "gk_tarih": {"cat": 1, "sub": 1, "subject": "Tarih"},
        "gk_cografya": {"cat": 2, "sub": 8, "subject": "Coğrafya"},
        "gk_vatandaslik": {"cat": 3, "sub": 13, "subject": "Vatandaşlık & Anayasa"},
        "gk_guncel": {"cat": 3, "sub": 17, "subject": "Güncel Bilgiler"}
    },
    "auto_kpss_onlisans": {
        "name": "KPSS Önlisans (B Grubu)",
        "lang_id": 57,
        "gy_turkce": {"cat": 39, "sub": 55, "subject": "Türkçe"},
        "gy_mat": {"cat": 40, "sub": 83, "subject": "Matematik & Mantık"},
        "gk_tarih": {"cat": 41, "sub": 58, "subject": "Tarih"},
        "gk_cografya": {"cat": 42, "sub": 62, "subject": "Coğrafya"},
        "gk_vatandaslik": {"cat": 43, "sub": 64, "subject": "Vatandaşlık & Anayasa"},
        "gk_guncel": {"cat": 43, "sub": 66, "subject": "Güncel Bilgiler"}
    },
    "auto_kpss_ortaogretim": {
        "name": "KPSS Ortaöğretim (Lise)",
        "lang_id": 66,
        "gy_turkce": {"cat": 44, "sub": 67, "subject": "Türkçe"},
        "gy_mat": {"cat": 45, "sub": 85, "subject": "Matematik"},
        "gk_tarih": {"cat": 46, "sub": 69, "subject": "Tarih"},
        "gk_cografya": {"cat": 47, "sub": 72, "subject": "Coğrafya"},
        "gk_vatandaslik": {"cat": 48, "sub": 74, "subject": "Vatandaşlık & Anayasa"},
        "gk_guncel": {"cat": 48, "sub": 75, "subject": "Güncel Olaylar"}
    },
    "auto_kpss_alan": {
        "name": "KPSS A Grubu (Alan Bilgisi)",
        "lang_id": 58,
        "default": {"cat": 49, "sub": 56, "subject": "Hukuk (A Grubu)"}
    },
    "auto_hakimlik": {
        "name": "Hakimlik & Savcılık",
        "lang_id": 59,
        "default": {"cat": 11, "sub": 0, "subject": "Anayasa & İdare (Hakimlik)"}
    }
}

def detect_exam_type(pdf_path, doc):
    total_pages = len(doc)
    sample_text = (os.path.basename(pdf_path) + " " + " ".join(doc[p].get_text() for p in range(min(4, total_pages)))).upper()

    if "ÖN LİSANS" in sample_text or "ÖNLİSANS" in sample_text or "ONLISANS" in sample_text or "ON LISANS" in sample_text:
        return "auto_kpss_onlisans"
    elif "ORTAÖĞRETİM" in sample_text or "ORTAOGRETIM" in sample_text or "LİSE" in sample_text:
        return "auto_kpss_ortaogretim"
    elif "HAKİMLİK" in sample_text or "HAKIMLIK" in sample_text or "ADLİ YARGI" in sample_text or "İDARİ YARGI" in sample_text:
        return "auto_hakimlik"
    elif "ALAN BİLGİSİ" in sample_text or "A GRUBU" in sample_text or ("İKTİSAT" in sample_text and "MALİYE" in sample_text):
        return "auto_kpss_alan"
    else:
        return "auto_kpss_lisans"

def parse_kpss_pdf(pdf_path, target_mode="auto_detect"):
    if not os.path.exists(pdf_path):
        return {"error": True, "message": f"Dosya bulunamadı: {pdf_path}"}

    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    if total_pages == 0:
        return {"error": True, "message": "PDF boş."}

    # Auto detect if requested
    if not target_mode or target_mode in ["auto_detect", "auto", "0"]:
        target_mode = detect_exam_type(pdf_path, doc)
    elif target_mode not in EXAM_CONFIGS:
        target_mode = "auto_kpss_lisans"

    cfg = EXAM_CONFIGS[target_mode]

    # Extract Year from first page if present
    first_page_text = doc[0].get_text() + " " + (doc[1].get_text() if total_pages > 1 else "")
    year_match = re.search(r'(20\d{2})[-\s]*(?:KPSS|Kamu)', first_page_text, re.I)
    year_str = year_match.group(1) if year_match else ""

    # 1. Parse Answer Keys from last 1-6 pages (supports split pages for GY and GK)
    answer_keys = {"GY": {}, "GK": {}}
    ans_page_indices = set()

    for pno in range(total_pages - 1, max(-1, total_pages - 6), -1):
        txt = doc[pno].get_text()
        has_gy = "GENEL YETENEK" in txt.upper()
        has_gk = "GENEL KÜLTÜR" in txt.upper()
        has_key_format = bool(re.search(r'\b1\.\s*[A-Ea-e]\b', txt))

        if (has_gy or has_gk) and has_key_format:
            ans_page_indices.add(pno)
            w = doc[pno].rect.width
            blocks = doc[pno].get_text("blocks")

            if has_gy and has_gk:
                # Both on same page in two columns
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
            elif has_gk:
                m = re.findall(r'(\d{1,2})\.\s*([A-Ea-e])\b', txt)
                for qnum_str, ans in m:
                    qn = int(qnum_str)
                    if qn <= 60:
                        answer_keys["GK"][qn] = ans.lower()
            elif has_gy:
                m = re.findall(r'(\d{1,2})\.\s*([A-Ea-e])\b', txt)
                for qnum_str, ans in m:
                    qn = int(qnum_str)
                    if qn <= 60:
                        answer_keys["GY"][qn] = ans.lower()

    # 2. Parse Questions Page by Page
    questions = []
    current_test = "GY"
    subject_counts = {}

    for pno in range(total_pages):
        if pno in ans_page_indices:
            continue
        page = doc[pno]
        w, h = page.rect.width, page.rect.height

        # Determine section switch
        p_raw = page.get_text()
        if re.search(r'GENEL\s+KÜLTÜR\s+TESTİ', p_raw, re.IGNORECASE) and not re.search(r'GENEL\s+KÜLTÜR.*GEÇİNİZ', p_raw, re.IGNORECASE):
            current_test = "GK"
        elif re.search(r'GENEL\s+YETENEK\s+TESTİ', p_raw, re.IGNORECASE) and not re.search(r'GENEL\s+YETENEK.*GEÇİNİZ', p_raw, re.IGNORECASE):
            current_test = "GY"

        # Discard headers (y < 55) and footers (y > h - 45)
        words = [wrd for wrd in page.get_text("words") if 55 <= wrd[1] <= h - 45]
        if not words:
            continue

        # Split into left and right columns
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

            # Ignore standalone booklet codes, page numbers, instructions
            if line_str in ['A', 'B', 'C', 'D', 'E'] and len(line_str) == 1:
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

                # Determine category, subcategory and subject
                if "gy_turkce" in cfg:
                    if current_test == "GY":
                        if qn <= 30:
                            branch = cfg["gy_turkce"]
                        else:
                            branch = cfg["gy_mat"]
                    else: # GK
                        if qn <= 27:
                            branch = cfg["gk_tarih"]
                        elif qn <= 45:
                            branch = cfg["gk_cografya"]
                        elif qn <= 54:
                            branch = cfg["gk_vatandaslik"]
                        else:
                            branch = cfg["gk_guncel"]
                else:
                    branch = cfg.get("default", {"cat": 1, "sub": 0, "subject": "Genel"})

                cat_id = branch["cat"]
                sub_id = branch["sub"]
                subject = branch["subject"]
                subject_counts[subject] = subject_counts.get(subject, 0) + 1

                sec_name = "Genel Yetenek" if current_test == "GY" else "Genel Kültür"
                year_prefix = f"ÖSYM {year_str} " if year_str else "ÖSYM "
                cur_q = {
                    "qnum": qn,
                    "test": current_test,
                    "subject": subject,
                    "category": cat_id,
                    "subcategory": sub_id,
                    "language_id": cfg["lang_id"],
                    "question": qm.group(2).strip(),
                    "optiona": "",
                    "optionb": "",
                    "optionc": "",
                    "optiond": "",
                    "optione": "",
                    "answer": ans,
                    "solution": f"{year_prefix}{cfg['name']} {sec_name} ({subject}) {qn}. Soru. Resmi Doğru Cevap: {ans.upper()}"
                }
                continue

            if not cur_q:
                continue

            # Check for multiple options on same line e.g. "A) 12  B) 14  C) 16"
            matches = list(re.finditer(r'([A-Ea-e])\)\s*(.*?)(?=(?:[A-Ea-e]\)|$))', line_str))
            if matches and any(m.group(1).upper() in ['A', 'B', 'C', 'D', 'E'] for m in matches):
                has_opt = False
                for m in matches:
                    opt_letter = m.group(1).lower()
                    opt_val = m.group(2).strip()
                    if opt_letter in ['a', 'b', 'c', 'd', 'e']:
                        cur_q[f'option{opt_letter}'] = opt_val
                        has_opt = True
                if has_opt:
                    continue

            # If no options filled yet, append to question text
            if not cur_q['optiona']:
                cur_q['question'] += " " + line_str
            else:
                # Find last filled option
                last_opt = None
                for ltr in ['e', 'd', 'c', 'b', 'a']:
                    if cur_q[f'option{ltr}']:
                        last_opt = ltr
                        break
                if last_opt:
                    clean_line = re.sub(r'\s+[A-E]$', '', line_str) # Strip trailing booklet letters
                    clean_line = re.sub(r'\s+\d+$', '', clean_line) # Strip trailing page numbers
                    if clean_line:
                        cur_q[f'option{last_opt}'] += " " + clean_line

        if cur_q and cur_q['optiona']:
            questions.append(cur_q)

    # 3. Post-process clean up
    for q in questions:
        q['question'] = fix_hyphenation(clean_text(q['question']))
        for ltr in ['a', 'b', 'c', 'd', 'e']:
            q[f'option{ltr}'] = fix_hyphenation(clean_text(q[f'option{ltr}']))
            # Clean trailing booklet codes
            q[f'option{ltr}'] = re.sub(r'\s+[A-E]$', '', q[f'option{ltr}'])
            q[f'option{ltr}'] = re.sub(r'\s+\d+$', '', q[f'option{ltr}'])

    summary_parts = [f"{subj}: {cnt}" for subj, cnt in subject_counts.items()]
    summary_text = ", ".join(summary_parts) if summary_parts else f"{len(questions)} Soru"

    return {
        "error": False,
        "title": os.path.basename(pdf_path),
        "year": year_str,
        "exam_target": target_mode,
        "exam_name": cfg["name"],
        "language_id": cfg["lang_id"],
        "summary": summary_text,
        "total": len(questions),
        "questions": questions
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": True, "message": "Kullanım: python3 kpss_pdf_parser.py <pdf_path> [badge] [target_exam]"}))
        sys.exit(1)

    pdf_file = sys.argv[1]
    badge = sys.argv[2] if len(sys.argv) > 2 else ""
    target_mode = sys.argv[3] if len(sys.argv) > 3 else "auto_detect"

    res = parse_kpss_pdf(pdf_file, target_mode)
    print(json.dumps(res, ensure_ascii=False, indent=2))
