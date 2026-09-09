import json

with open('d:/quiza/scratch_osym/cleaned_hmgs_book.json', 'r', encoding='utf-8') as f:
    hmgs = json.load(f)

print("HMGS sample solutions:")
for q in hmgs[:5]:
    print(f"Q: {q['question'][:80]}")
    print(f"Sol: {q['solution'][:100]}\n")

with open('d:/quiza/scratch_osym/extracted_anayasa_book.json', 'r', encoding='utf-8') as f:
    ay = json.load(f)

print("Anayasa sample questions:")
for q in ay[:5]:
    print(f"Q: {q['question'][:80]}")
    print(f"Sol: {q.get('solution', '')[:100]}\n")
