import json, re

with open('d:/quiza/scratch_osym/extracted_hmgs_book.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

cleaned_questions = []

for q in questions:
    qnum = q.get('qnum')
    page = q.get('page')
    q_text = q['question']
    opt_a = q['optiona']
    opt_b = q['optionb']
    opt_c = q['optionc']
    opt_d = q['optiond']
    opt_e = q['optione']
    ans = q['answer']
    sol = q['solution']

    # Combine all options and solution to re-parse if they were collapsed
    full_body = f"A) {opt_a} B) {opt_b} C) {opt_c} D) {opt_d} E) {opt_e}"
    
    # Split by \b([A-E])\)\s*
    matches = list(re.finditer(r'(?:^|\s+)([A-E])\)\s*', full_body))
    # We want unique sequence A, B, C, D, E
    opt_map = {'a': opt_a, 'b': opt_b, 'c': opt_c, 'd': opt_d, 'e': opt_e}
    
    # Check if A, B, C, D, E exist in sequence in full_body
    indices = {}
    last_idx = -1
    valid_seq = True
    for letter in ['A', 'B', 'C', 'D', 'E']:
        m = re.search(r'(?:^|\s+)' + letter + r'\)\s*', full_body[last_idx+1:])
        if m:
            abs_start = last_idx + 1 + m.start()
            abs_end = last_idx + 1 + m.end()
            indices[letter] = (abs_start, abs_end)
            last_idx = abs_end
        else:
            valid_seq = False
            break
            
    if valid_seq:
        opt_a = full_body[indices['A'][1]:indices['B'][0]].strip()
        opt_b = full_body[indices['B'][1]:indices['C'][0]].strip()
        opt_c = full_body[indices['C'][1]:indices['D'][0]].strip()
        opt_d = full_body[indices['D'][1]:indices['E'][0]].strip()
        # Option E goes until solution or end
        rem_e = full_body[indices['E'][1]:].strip()
        # Does rem_e contain solution text?
        # Check if "ÇÖZÜM" or sentence is in rem_e
        sol_m = re.search(r'\s*(?:ÇÖZÜM|DİKKAT)\s*[:\-]?\s*', rem_e, re.IGNORECASE)
        # Check if option E has Roman numeral choice followed by explanation:
        # e.g. "I, II ve III 1982 Anayasasının..." or "II ve III Anayasanın..."
        roman_m = re.match(r'^((?:Yalnız\s+[I|V|X]+|(?:[I|V|X]+(?:\s*,\s*|\s+ve\s+))+[I|V|X]+))\s+(.*)', opt_e, re.IGNORECASE)
        if roman_m:
            opt_e = roman_m.group(1).strip()
            extra_sol = roman_m.group(2).strip()
            if extra_sol:
                sol = extra_sol + (" " + sol if sol else "")
        elif sol_m:
            opt_e = rem_e[:sol_m.start()].strip()
            extra_sol = rem_e[sol_m.end():].strip()
            if extra_sol:
                sol = extra_sol + (" " + sol if sol else "")
        else:
            opt_e = rem_e

    # Clean question text
    q_text = re.sub(r'^\s*\\n\s*', '', q_text)
    q_text = re.sub(r'^\s*\d{1,3}\.\s*', '', q_text)
    q_text = re.sub(r'[\r\n\t]+', ' ', q_text)
    q_text = re.sub(r'\s+', ' ', q_text).strip()

    # Clean options
    for o in [opt_a, opt_b, opt_c, opt_d, opt_e]:
        o = re.sub(r'[\r\n\t]+', ' ', o)
        o = re.sub(r'\s+', ' ', o).strip()

    # Clean solution text
    sol = re.sub(r'^(?:\\n)+', '', sol)
    sol = re.sub(r'[\r\n\t]+', ' ', sol)
    sol = re.sub(r'\s*(?:Hakimlik|Hukuk Meslekleri|Akademisi)\s*.*$', '', sol, flags=re.IGNORECASE)
    sol = re.sub(r'\s+', ' ', sol).strip()

    # Only include valid questions with all 5 options and answer
    if opt_a and opt_b and opt_c and opt_d and opt_e and ans:
        cleaned_questions.append({
            'qnum': qnum,
            'page': page,
            'question': q_text,
            'optiona': opt_a,
            'optionb': opt_b,
            'optionc': opt_c,
            'optiond': opt_d,
            'optione': opt_e,
            'answer': ans.lower(),
            'solution': sol
        })

print(f"Total valid cleaned questions: {len(cleaned_questions)}")

# Inspect sample Q5 and Q6
for q in cleaned_questions[:8]:
    print(f"[Q{q['qnum']} - P{q['page']}] Ans: {q['answer'].upper()}")
    print(f"  Q: {q['question'][:70]}...")
    print(f"  A: {q['optiona'][:30]} | B: {q['optionb'][:30]} | C: {q['optionc'][:30]}")
    print(f"  D: {q['optiond'][:30]} | E: {q['optione'][:30]}")
    print(f"  Sol: {q['solution'][:70]}...\n")

with open('d:/quiza/scratch_osym/cleaned_hmgs_book.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_questions, f, ensure_ascii=False, indent=2)
