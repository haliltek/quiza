import subprocess, re, sys, os
sys.stdout.reconfigure(encoding='utf-8')

# We run pdftotext -layout on the server or local if pdftotext is available
# Or we do it via ssh
cmd = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_api pdftotext -layout /tmp/2019.pdf /tmp/2019_layout.txt && docker cp elitequiz_api:/tmp/2019_layout.txt /tmp/2019_layout.txt']
subprocess.run(cmd, check=True)

# Copy 2019_layout.txt to local
subprocess.run(['scp', '-o', 'StrictHostKeyChecking=no', 'root@142.93.104.78:/tmp/2019_layout.txt', 'd:/quiza/scratch_osym/2019_layout.txt'], check=True)

with open('d:/quiza/scratch_osym/2019_layout.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

pages = content.split('\x0c')
print(f"Total pages in layout text: {len(pages)}")

# 1. Parse Answer Key from page 34 (pages[33])
ans_page = pages[33] if len(pages) >= 34 else pages[-1]
# Find GY and GK answer keys
ans_keys = {'GY': {}, 'GK': {}}

# On page 34:
# GENEL YETENEK          GENEL YETENEK               GENEL KÜLTÜR           GENEL KÜLTÜR
#     1.   D                  48.   E                    1.   E                 48.   C
lines = ans_page.split('\n')
for l in lines:
    # Match patterns like: (\d+)\.\s+([A-E])
    m = list(re.finditer(r'(\d{1,2})\.\s+([A-E])\b', l))
    for match in m:
        qnum = int(match.group(1))
        ans = match.group(2).lower()
        # Column position: match.start()
        # Col 0..70 is GY, Col >= 70 is GK
        if match.start() < 70:
            ans_keys['GY'][qnum] = ans
        else:
            ans_keys['GK'][qnum] = ans

print("GY Answer Key count:", len(ans_keys['GY']))
print("GK Answer Key count:", len(ans_keys['GK']))
print("GY Sample 1-5:", {k: ans_keys['GY'].get(k) for k in range(1, 6)})
print("GK Sample 1-5:", {k: ans_keys['GK'].get(k) for k in range(1, 6)})

# 2. Extract Questions Column by Column from Pages 2 to 33
gy_questions = {}
gk_questions = {}
current_test = 'GY'

for pno in range(1, len(pages) - 1):
    p_text = pages[pno]
    if 'GENEL KÜLTÜR TESTİ' in p_text or 'GENEL KÜLTÜR' in p_text and pno >= 12:
        current_test = 'GK'

    # Split lines into left column and right column
    p_lines = p_text.split('\n')
    left_col = []
    right_col = []
    
    for line in p_lines:
        # Determine split position (around 65-75 chars)
        if len(line) > 65:
            # Look for a gap of spaces between 60 and 80
            gap = re.search(r'\s{4,}', line[55:85])
            if gap:
                split_pos = 55 + gap.start() + len(gap.group()) // 2
            else:
                split_pos = 70
            left_col.append(line[:split_pos].rstrip())
            right_col.append(line[split_pos:].rstrip())
        else:
            left_col.append(line.rstrip())
            right_col.append('')

    # Process left column then right column
    stream = left_col + right_col
    cur_q = None
    
    for l in stream:
        trim = l.strip()
        if not trim: continue
        if any(k in trim for k in ['2019-KPSS', 'GENEL YETENEK', 'GENEL KÜLTÜR', 'Diğer sayfaya', 'TEST BİTTİ', 'Bu testte', 'Cevaplarınızı']):
            continue

        # Question start: "1. ", "2. ", "13. "
        qm = re.match(r'^(\d{1,2})\.\s+(.*)', trim)
        if qm and int(qm.group(1)) <= 60:
            qnum = int(qm.group(1))
            if cur_q:
                target_dict = gy_questions if cur_q['test'] == 'GY' else gk_questions
                target_dict[cur_q['qnum']] = cur_q

            ans = ans_keys[current_test].get(qnum, 'a')
            cur_q = {
                'qnum': qnum,
                'test': current_test,
                'question': qm.group(2),
                'optiona': '',
                'optionb': '',
                'optionc': '',
                'optiond': '',
                'optione': '',
                'answer': ans,
                'solution': f"ÖSYM 2019 KPSS {current_test} {qnum}. Soru. Resmi Cevap: {ans.upper()}"
            }
            continue

        if not cur_q: continue

        # Options A) .. E)
        # In layout text, options can be on one line: A) II B) III C) IV D) V E) VI
        # Or each option on its own line: A) ...
        opt_matches = list(re.finditer(r'([A-E])\)\s*', trim))
        if opt_matches:
            for i, om in enumerate(opt_matches):
                letter = om.group(1).lower()
                start_txt = om.end()
                end_txt = opt_matches[i+1].start() if i + 1 < len(opt_matches) else len(trim)
                val = trim[start_txt:end_txt].strip()
                cur_q[f'option{letter}'] = val
            continue

        # Append to question or option
        if not cur_q['optiona']:
            cur_q['question'] += ' ' + trim
        elif cur_q['optione']:
            cur_q['optione'] += ' ' + trim
        elif cur_q['optiond']:
            cur_q['optiond'] += ' ' + trim
        elif cur_q['optionc']:
            cur_q['optionc'] += ' ' + trim
        elif cur_q['optionb']:
            cur_q['optionb'] += ' ' + trim
        elif cur_q['optiona']:
            cur_q['optiona'] += ' ' + trim

    if cur_q:
        target_dict = gy_questions if cur_q['test'] == 'GY' else gk_questions
        target_dict[cur_q['qnum']] = cur_q

print(f"\nFinal Extracted GY Questions: {len(gy_questions)} / 60")
print(f"Final Extracted GK Questions: {len(gk_questions)} / 60")
print(f"TOTAL Extracted Questions: {len(gy_questions) + len(gk_questions)} / 120")
