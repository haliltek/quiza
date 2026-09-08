import json, re, os, sys

json_path = 'd:/quiza/scratch_osym/extracted_anayasa_book.json'
if not os.path.exists(json_path):
    print("Waiting for JSON...")
    sys.exit(0)

with open(json_path, 'r', encoding='utf-8') as f:
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

    full_body = f"A) {opt_a} B) {opt_b} C) {opt_c} D) {opt_d} E) {opt_e}"
    
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
        rem_e = full_body[indices['E'][1]:].strip()
        
        sol_m = re.search(r'\s*(?:ÇÖZÜM|DİKKAT)\s*[:\-]?\s*', rem_e, re.IGNORECASE)
        roman_m = re.match(r'^((?:Yalnız\s+[I|V|X]+|(?:[I|V|X]+(?:\s*,\s*|\s+ve\s+))+[I|V|X]+))\s+(.*)', rem_e, re.IGNORECASE)
        
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

    q_text = re.sub(r'^\s*\\n\s*', '', q_text)
    q_text = re.sub(r'^\s*\d{1,3}\.\s*', '', q_text)
    q_text = re.sub(r'[\r\n\t]+', ' ', q_text)
    q_text = re.sub(r'\s+', ' ', q_text).strip()

    for o in [opt_a, opt_b, opt_c, opt_d, opt_e]:
        o = re.sub(r'[\r\n\t]+', ' ', o)
        o = re.sub(r'\s+', ' ', o).strip()

    sol = re.sub(r'^(?:\\n)+', '', sol)
    sol = re.sub(r'[\r\n\t]+', ' ', sol)
    sol = re.sub(r'\s*(?:Hakimlik|Hukuk Meslekleri|Akademisi)\s*.*$', '', sol, flags=re.IGNORECASE)
    sol = re.sub(r'\s+', ' ', sol).strip()

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

print(f"Total valid cleaned questions for Anayasa: {len(cleaned_questions)}")

# Generate SQL
# Category 11 = Anayasa & İdare Hukuku (Hakimlik)
category_id = 11
subcategory_id = 0
language_id = 52
badge = "[HMGS Anayasa Hukuku Soru Bankası]"

sql_statements = []
for q in cleaned_questions:
    q_text = f"{badge}\n\n{q['question'].strip()}"
    opt_a = q['optiona'].strip()
    opt_b = q['optionb'].strip()
    opt_c = q['optionc'].strip()
    opt_d = q['optiond'].strip()
    opt_e = q['optione'].strip()
    ans = q['answer'].strip().lower()
    sol = q['solution'].strip()

    def esc(s):
        return s.replace('\\', '\\\\').replace("'", "''")

    sql = f"""INSERT INTO `tbl_question` (`category`, `subcategory`, `language_id`, `image`, `question`, `question_type`, `optiona`, `optionb`, `optionc`, `optiond`, `optione`, `answer`, `level`, `note`)
VALUES ({category_id}, {subcategory_id}, {language_id}, '', '{esc(q_text)}', 1, '{esc(opt_a)}', '{esc(opt_b)}', '{esc(opt_c)}', '{esc(opt_d)}', '{esc(opt_e)}', '{esc(ans)}', 1, '{esc(sol)}');"""
    sql_statements.append(sql)

out_sql = 'd:/quiza/scratch_osym/insert_anayasa_book.sql'
with open(out_sql, 'w', encoding='utf-8') as f:
    f.write("SET NAMES utf8mb4;\n")
    f.write("START TRANSACTION;\n")
    for s in sql_statements:
        f.write(s + "\n")
    f.write("COMMIT;\n")

print(f"Generated {len(sql_statements)} INSERT statements in {out_sql}")
