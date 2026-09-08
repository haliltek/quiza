import json, os, sys

json_path = 'd:/quiza/scratch_osym/cleaned_hmgs_book.json'
if not os.path.exists(json_path):
    print("JSON file not ready yet.")
    sys.exit(0)

with open(json_path, 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions from JSON.")

sql_statements = []
# Category 11 = Anayasa & İdare Hukuku (Hakimlik)
# Category 3 = Vatandaşlık & Anayasa (KPSS Lisans)
category_id = 11
subcategory_id = 0
language_id = 52 # Turkish
badge = "[HMGS İdare Hukuku Soru Bankası]"

for idx, q in enumerate(questions):
    q_text = f"{badge}\n\n{q['question'].strip()}"
    opt_a = q['optiona'].strip()
    opt_b = q['optionb'].strip()
    opt_c = q['optionc'].strip()
    opt_d = q['optiond'].strip()
    opt_e = q['optione'].strip()
    ans = q['answer'].strip().lower()
    sol = q['solution'].strip()

    # Escape strings for SQL
    def esc(s):
        return s.replace('\\', '\\\\').replace("'", "''")

    sql = f"""INSERT INTO `tbl_question` (`category`, `subcategory`, `language_id`, `image`, `question`, `question_type`, `optiona`, `optionb`, `optionc`, `optiond`, `optione`, `answer`, `level`, `note`)
VALUES ({category_id}, {subcategory_id}, {language_id}, '', '{esc(q_text)}', 1, '{esc(opt_a)}', '{esc(opt_b)}', '{esc(opt_c)}', '{esc(opt_d)}', '{esc(opt_e)}', '{esc(ans)}', 1, '{esc(sol)}');"""
    sql_statements.append(sql)

out_sql = 'd:/quiza/scratch_osym/insert_hmgs_book.sql'
with open(out_sql, 'w', encoding='utf-8') as f:
    f.write("SET NAMES utf8mb4;\n")
    f.write("START TRANSACTION;\n")
    for s in sql_statements:
        f.write(s + "\n")
    f.write("COMMIT;\n")

print(f"Generated {len(sql_statements)} INSERT statements in {out_sql}")
