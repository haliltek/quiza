import sys, os, re, json
import fitz # PyMuPDF

def extract_pdf_questions(pdf_path, badge=""):
    if not os.path.exists(pdf_path):
        return {"error": True, "message": f"Dosya bulunamadı: {pdf_path}"}

    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    if total_pages == 0:
        return {"error": True, "message": "PDF boş."}

    # 1. Parse Answer Key from last 1-3 pages
    answer_keys = {"GY": {}, "GK": {}, "GENEL": {}}
    # Scan from last page backwards
    for pno in range(total_pages - 1, max(-1, total_pages - 3), -1):
        page = doc[pno]
        w, h = page.rect.width, page.rect.height
        txt = page.get_text()
        
        # Check if this page contains answer key
        if re.search(r'CEVAP\s+ANAHTARI|GENEL\s+YETENEK|GENEL\s+KÜLTÜR', txt, re.IGNORECASE):
            # Check layout using words or blocks
            blocks = page.get_text("blocks")
            for b in blocks:
                b_txt = b[4]
                # Determine section based on heading or x-position
                # In ÖSYM layout:
                # Left side is GY, right side is GK
                test_type = "GY" if b[0] < w / 2 else "GK"
                if "GENEL KÜLTÜR" in b_txt.upper():
                    test_type = "GK"
                elif "GENEL YETENEK" in b_txt.upper():
                    test_type = "GY"

                matches = re.findall(r'(\d{1,3})\s*[\.\-:]\s*([A-Ea-e])\b', b_txt)
                for qnum_str, ans in matches:
                    qnum = int(qnum_str)
                    if qnum <= 60:
                        answer_keys[test_type][qnum] = ans.lower()
                    answer_keys["GENEL"][qnum] = ans.lower()

    # 2. Extract Questions Page by Page (Column by Column)
    questions = []
    current_test = "GY" # Start with Genel Yetenek
    
    # We scan question pages (exclude last answer key page)
    end_page = total_pages - 1 if (len(answer_keys["GY"]) > 10 or len(answer_keys["GK"]) > 10) else total_pages

    all_lines = []
    for pno in range(end_page):
        page = doc[pno]
        w, h = page.rect.width, page.rect.height
        
        # Exclude headers (y < 60) and footers (y > h - 40)
        words = [wrd for wrd in page.get_text("words") if 50 <= wrd[1] <= h - 35]
        left_words = [wrd for wrd in words if wrd[0] < w / 2]
        right_words = [wrd for wrd in words if wrd[0] >= w / 2]

        def get_lines(wlist):
            wlist = sorted(wlist, key=lambda it: (it[1], it[0]))
            lines = []
            cur_line = []
            cur_y = None
            for wrd in wlist:
                if cur_y is None:
                    cur_y = wrd[1]
                    cur_line.append(wrd)
                elif abs(wrd[1] - cur_y) < 4.5:
                    cur_line.append(wrd)
                else:
                    cur_line.sort(key=lambda it: it[0])
                    lines.append(" ".join(it[4] for it in cur_line))
                    cur_line = [wrd]
                    cur_y = wrd[1]
            if cur_line:
                cur_line.sort(key=lambda it: it[0])
                lines.append(" ".join(it[4] for it in cur_line))
            return lines

        for l in get_lines(left_words) + get_lines(right_words):
            l_clean = l.strip()
            # Check test section switch
            if re.search(r'GENEL\s+KÜLTÜR\s+TESTİ|GENEL\s+KÜLTÜR', l_clean, re.IGNORECASE) and not re.search(r'GENEL\s+KÜLTÜR.*GEÇİNİZ', l_clean, re.IGNORECASE):
                if pno >= 10: # GK usually starts around page 14-18
                    current_test = "GK"
            all_lines.append((current_test, pno + 1, l_clean))

    # 3. Parse Question Bodies and Options
    current_q = None
    
    for test_type, pnum, line in all_lines:
        # Skip watermarks
        if re.search(r'Bu testte \d+ soru vardır|Cevaplarınızı, cevap|Diğer sayfaya geçiniz|Bu soruların telif|Ö S Y M|ÖSYM|TEST BİTTİ|CEVAPLARINIZI KONTROL', line, re.IGNORECASE):
            continue

        # Match question start: "1. ", "2. ", "1 - "
        qm = re.match(r'^(\d{1,2})\.\s+(.*)', line)
        if qm and int(qm.group(1)) <= 60:
            qnum = int(qm.group(1))
            
            # Save previous question if it has option A
            if current_q and current_q.get("optiona"):
                questions.append(current_q)

            # Lookup answer
            ans = answer_keys[test_type].get(qnum, answer_keys["GENEL"].get(qnum, "a"))

            # Determine category & subcategory based on KPSS standard
            if test_type == "GY":
                if qnum <= 30:
                    cat_name = "Türkçe (KPSS Lisans)"
                    cat_id = 4
                    subcat_id = 18 # Türkçe
                else:
                    cat_name = "Matematik & Sayısal Mantık"
                    cat_id = 5
                    subcat_id = 22 # Matematik
            else: # GK
                if qnum <= 27:
                    cat_name = "Tarih (KPSS Lisans)"
                    cat_id = 1
                    subcat_id = 1 # Tarih
                elif qnum <= 45:
                    cat_name = "Coğrafya (KPSS Lisans)"
                    cat_id = 2
                    subcat_id = 8 # Coğrafya
                elif qnum <= 54:
                    cat_name = "Vatandaşlık & Anayasa (KPSS Lisans)"
                    cat_id = 3
                    subcat_id = 13 # Vatandaşlık
                else:
                    cat_name = "Vatandaşlık & Anayasa (KPSS Lisans)"
                    cat_id = 3
                    subcat_id = 17 # Güncel Bilgiler

            current_q = {
                "qnum": qnum,
                "test": test_type,
                "page": pnum,
                "category": cat_id,
                "subcategory": subcat_id,
                "category_name": cat_name,
                "question": qm.group(2),
                "optiona": "",
                "optionb": "",
                "optionc": "",
                "optiond": "",
                "optione": "",
                "answer": ans,
                "solution": f"KPSS {test_type} {qnum}. Soru. Resmi Cevap: {ans.upper()}"
            }
            continue

        if not current_q:
            continue

        # Match options A) .. E)
        if re.match(r'^[A-E]\)\s*(.*)', line):
            if line.startswith("A)"):
                current_q["optiona"] = line[2:].strip()
            elif line.startswith("B)"):
                current_q["optionb"] = line[2:].strip()
            elif line.startswith("C)"):
                current_q["optionc"] = line[2:].strip()
            elif line.startswith("D)"):
                current_q["optiond"] = line[2:].strip()
            elif line.startswith("E)"):
                current_q["optione"] = line[2:].strip()
            continue

        # Append to question or current option
        if not current_q["optiona"]:
            current_q["question"] += " " + line
        elif current_q["optione"]:
            current_q["optione"] += " " + line
        elif current_q["optiond"]:
            current_q["optiond"] += " " + line
        elif current_q["optionc"]:
            current_q["optionc"] += " " + line
        elif current_q["optionb"]:
            current_q["optionb"] += " " + line
        elif current_q["optiona"]:
            current_q["optiona"] += " " + line

    if current_q and current_q.get("optiona"):
        questions.append(current_q)

    # Clean up formatting
    cleaned_questions = []
    for q in questions:
        q["question"] = re.sub(r'\s+', ' ', q["question"]).strip()
        q["optiona"] = re.sub(r'\s+', ' ', q["optiona"]).strip()
        q["optionb"] = re.sub(r'\s+', ' ', q["optionb"]).strip()
        q["optionc"] = re.sub(r'\s+', ' ', q["optionc"]).strip()
        q["optiond"] = re.sub(r'\s+', ' ', q["optiond"]).strip()
        q["optione"] = re.sub(r'\s+', ' ', q["optione"]).strip()
        
        # Only keep questions with at least 4 options
        if q["optiona"] and q["optionb"] and q["optionc"] and q["optiond"] and len(q["question"]) > 10:
            cleaned_questions.append(q)

    return {
        "error": False,
        "title": os.path.basename(pdf_path),
        "total": len(cleaned_questions),
        "gy_count": sum(1 for q in cleaned_questions if q["test"] == "GY"),
        "gk_count": sum(1 for q in cleaned_questions if q["test"] == "GK"),
        "questions": cleaned_questions
    }

if __name__ == "__main__":
    test_pdf = sys.argv[1] if len(sys.argv) > 1 else 'd:/quiza/scratch_osym/2019.pdf'
    res = extract_pdf_questions(test_pdf)
    print(f"Total extracted: {res.get('total')}")
    print(f"GY count: {res.get('gy_count')}, GK count: {res.get('gk_count')}")
    if res.get("questions"):
        print("Sample Q1 (GY):", res["questions"][0]["question"][:60], "Ans:", res["questions"][0]["answer"])
        gk_sample = [q for q in res["questions"] if q["test"] == "GK"]
        if gk_sample:
            print("Sample Q1 (GK):", gk_sample[0]["question"][:60], "Ans:", gk_sample[0]["answer"])
