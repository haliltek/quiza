import sys
sys.path.append(r'd:\quiza\scratch_osym')
from extract_pdf_questions import extract_pdf_questions

res = extract_pdf_questions('d:/quiza/scratch_osym/2019.pdf')
qs = res['questions']
gy_nums = [q['qnum'] for q in qs if q['test'] == 'GY']
gk_nums = [q['qnum'] for q in qs if q['test'] == 'GK']
print(f"Extracted GY ({len(gy_nums)}):", gy_nums)
print(f"Extracted GK ({len(gk_nums)}):", gk_nums)

# What GY numbers are missing from 1-60?
missing_gy = [i for i in range(1, 61) if i not in gy_nums]
print("Missing GY:", missing_gy)

# What GK numbers are missing from 1-60?
missing_gk = [i for i in range(1, 61) if i not in gk_nums]
print("Missing GK:", missing_gk)
