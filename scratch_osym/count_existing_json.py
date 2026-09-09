import json

with open('d:/quiza/scratch_osym/cleaned_hmgs_book.json', 'r', encoding='utf-8') as f:
    hmgs = json.load(f)

print(f"Total questions in cleaned_hmgs_book.json: {len(hmgs)}")

with open('d:/quiza/scratch_osym/extracted_anayasa_book.json', 'r', encoding='utf-8') as f:
    anayasa = json.load(f)

print(f"Total questions in extracted_anayasa_book.json: {len(anayasa)}")
