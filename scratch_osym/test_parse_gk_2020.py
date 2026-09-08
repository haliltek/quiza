import sys; sys.path.append(r'd:\quiza\scratch_osym')
import pymupdf, re
from parse_answer_keys import parse_answer_keys

def extract_lines(words):
    lines = []
    words = sorted(words, key=lambda item: (item[1], item[0]))
    cur_line = []
    cur_y = None
    for word in words:
        if cur_y is None:
            cur_y = word[1]
            cur_line.append(word)
        elif abs(word[1] - cur_y) < 4.5:
            cur_line.append(word)
        else:
            cur_line.sort(key=lambda item: item[0])
            lines.append(' '.join(item[4] for item in cur_line))
            cur_line = [word]
            cur_y = word[1]
    if cur_line:
        cur_line.sort(key=lambda item: item[0])
        lines.append(' '.join(item[4] for item in cur_line))
    return lines

def parse_booklet_section(doc, start_pno, end_pno):
    # Returns raw text stream of the section
    stream = []
    for pno in range(start_pno, end_pno):
        page = doc[pno]
        w, h = page.rect.width, page.rect.height
        # filter header and footer
        words = [wrd for wrd in page.get_text('words') if 70 <= wrd[1] <= h - 45]
        left_words = [wrd for wrd in words if wrd[0] < w / 2]
        right_words = [wrd for wrd in words if wrd[0] >= w / 2]
        lines_l = extract_lines(left_words)
        lines_r = extract_lines(right_words)
        for l in lines_l + lines_r:
            l_low = l.lower()
            if any(k in l_low for k in ['bu testte', 'cevaplarınız', 'cevaplarnz', 'ayrılan kısmına', 'ayrlan ksmna']):
                continue
            stream.append(l)
    return stream

def parse_questions_from_stream(stream, year, test_type, answer_keys):
    questions = []
    # Join into a single text with newlines
    full_text = '\n'.join(stream)
    
    # We want to split text by question numbers: ^\s*(\d{1,2})\.\s+
    # Note: within a question, Roman numerals like I., II., III. might appear at start of line,
    # so we must only split on numeric numbers 1..60 that match the expected next question number!
    pattern = re.compile(r'(?:^|\n)\s*(\d{1,2})\.\s+', re.MULTILINE)
    matches = list(pattern.finditer(full_text))
    
    # Filter matches to ensure they form a strictly increasing sequence of question numbers
    valid_q_matches = []
    expected = 1
    for m in matches:
        num = int(m.group(1))
        if num == expected:
            valid_q_matches.append((num, m.start()))
            expected += 1
        elif num == expected + 1 and expected > 1: # maybe 1 skipped
            valid_q_matches.append((num, m.start()))
            expected = num + 1
            
    print(f"Found {len(valid_q_matches)} sequential questions in {test_type} (expected ~60)")
    
    for i, (qnum, start_idx) in enumerate(valid_q_matches):
        end_idx = valid_q_matches[i+1][1] if i + 1 < len(valid_q_matches) else len(full_text)
        block = full_text[start_idx:end_idx].strip()
        
        # Strip the leading 'N. '
        block = re.sub(r'^\s*\d{1,2}\.\s*', '', block).strip()
        
        # Now find options A), B), C), D), E)
        # Options could be vertical or horizontal
        # Regex to split out options:
        opt_pattern = re.compile(r'(?:^|\s+)([A-E])\)\s*')
        opt_splits = list(opt_pattern.finditer(block))
        
        # We need options A, B, C, D, E in order
        opt_dict = {}
        q_text = block
        
        if len(opt_splits) >= 5:
            # First match should be 'A'
            a_idx = -1
            for idx, sm in enumerate(opt_splits):
                if sm.group(1) == 'A':
                    a_idx = idx
                    break
            if a_idx != -1 and len(opt_splits) >= a_idx + 5:
                q_text = block[:opt_splits[a_idx].start()].strip()
                for k in range(5):
                    curr_m = opt_splits[a_idx + k]
                    letter = curr_m.group(1).lower()
                    if k < 4:
                        next_m = opt_splits[a_idx + k + 1]
                        val = block[curr_m.end():next_m.start()].strip()
                    else:
                        val = block[curr_m.end():].strip()
                    # Clean any trailing garbage or "Diğer sayfaya geçiniz"
                    val = re.sub(r'Diğer sayfaya geçiniz.*', '', val, flags=re.IGNORECASE).strip()
                    opt_dict[f'option{letter}'] = val
                    
        # Remove any footer / test header text from q_text
        q_text = re.sub(r'Diğer sayfaya geçiniz.*', '', q_text, flags=re.IGNORECASE).strip()
        q_text = re.sub(r'GENEL KÜLTÜR.*', '', q_text, flags=re.IGNORECASE).strip()
        q_text = re.sub(r'GENEL YETENEK.*', '', q_text, flags=re.IGNORECASE).strip()
        
        ans = answer_keys.get((year, test_type, qnum), '')
        
        questions.append({
            'year': year,
            'test': test_type,
            'qnum': qnum,
            'question': q_text,
            'optiona': opt_dict.get('optiona', ''),
            'optionb': opt_dict.get('optionb', ''),
            'optionc': opt_dict.get('optionc', ''),
            'optiond': opt_dict.get('optiond', ''),
            'optione': opt_dict.get('optione', ''),
            'answer': ans
        })
        
    return questions

if __name__ == '__main__':
    keys = parse_answer_keys()
    doc = pymupdf.open('d:/quiza/scratch_osym/2020.pdf')
    # 2020 GK is page 21 to 33 (0-indexed 20 to 33)
    stream = parse_booklet_section(doc, 20, 33)
    gk_questions = parse_questions_from_stream(stream, 2020, 'GK', keys)
    print(f"Total parsed GK questions: {len(gk_questions)}")
    for q in gk_questions[:5]:
        print(f"\n--- Soru {q['qnum']} (Cevap: {q['answer'].upper()}) ---")
        print("Soru:", q['question'][:120] + "...")
        print("A:", q['optiona'])
        print("B:", q['optionb'])
        print("C:", q['optionc'])
        print("D:", q['optiond'])
        print("E:", q['optione'])
