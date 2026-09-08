import pymupdf, re

def extract_column_lines(words):
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

doc = pymupdf.open('d:/quiza/scratch_osym/2020.pdf')
# Let's inspect pages 21 to 24 (start of GK in 2020)
for pno in range(20, 25):
    page = doc[pno]
    w, h = page.rect.width, page.rect.height
    words = [wrd for wrd in page.get_text('words') if 120 <= wrd[1] <= h - 40]
    left_words = [wrd for wrd in words if wrd[0] < w / 2]
    right_words = [wrd for wrd in words if wrd[0] >= w / 2]
    
    print(f"=== PAGE {pno+1} LEFT ===")
    lines_l = extract_column_lines(left_words)
    print("\n".join(lines_l[:15]))
    
    print(f"=== PAGE {pno+1} RIGHT ===")
    lines_r = extract_column_lines(right_words)
    print("\n".join(lines_r[:15]))
