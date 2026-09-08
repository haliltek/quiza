import pymupdf, re

def parse_answer_keys():
    keys = {} # (year, test, qnum) -> ans_lower
    
    # 1. 2016 hardcoded from official Page 30 answer sheet
    gy_2016 = "A B E D D D B A E D A B E D A B B C B C A D B D E E D B B E A B B C C D C B A E C B B C E A D E B D B C C D A C C D E A".split()
    gk_2016 = "A A E A C D A A B A D A A D E A A B B A A E A A C C A A D C E B C B A C A A D B E E A E D C A C B A C A A B D D A B B C".split()
    for i, a in enumerate(gy_2016, 1):
        keys[(2016, 'GY', i)] = a.lower()
    for i, a in enumerate(gk_2016, 1):
        keys[(2016, 'GK', i)] = a.lower()
        
    # 2. 2021: Page 35 (blocks with x < 300 is GY, x >= 300 is GK)
    doc_2021 = pymupdf.open('d:/quiza/scratch_osym/2021.pdf')
    for b in doc_2021[34].get_text('blocks'):
        txt = b[4]
        matches = re.findall(r'(\d+)\.\s+([A-E])\b', txt)
        if matches:
            test = 'GY' if b[0] < 300 else 'GK'
            for qstr, ans in matches:
                keys[(2021, test, int(qstr))] = ans.lower()

    # 3. 2020: Page 35 (GY then GK)
    doc_2020 = pymupdf.open('d:/quiza/scratch_osym/2020.pdf')
    txt_2020 = doc_2020[34].get_text()
    # Split by GENEL KÜLTÜR
    pos_gk = txt_2020.find('GENEL K', txt_2020.find('GENEL K') + 10)
    gy_part = txt_2020[:pos_gk]
    gk_part = txt_2020[pos_gk:]
    for qstr, ans in re.findall(r'(\d+)\.\s+([A-E])\b', gy_part):
        keys[(2020, 'GY', int(qstr))] = ans.lower()
    for qstr, ans in re.findall(r'(\d+)\.\s+([A-E])\b', gk_part):
        keys[(2020, 'GK', int(qstr))] = ans.lower()

    # 4. 2019: Page 34 (GY then GK)
    doc_2019 = pymupdf.open('d:/quiza/scratch_osym/2019.pdf')
    txt_2019 = doc_2019[33].get_text()
    pos_gk = txt_2019.find('GENEL KÜLTÜR')
    gy_part = txt_2019[:pos_gk]
    gk_part = txt_2019[pos_gk:]
    for qstr, ans in re.findall(r'(\d+)\.\s+([A-E])\b', gy_part):
        keys[(2019, 'GY', int(qstr))] = ans.lower()
    for qstr, ans in re.findall(r'(\d+)\.\s+([A-E])\b', gk_part):
        keys[(2019, 'GK', int(qstr))] = ans.lower()

    # 5. 2017: Page 36 (GY then GK)
    doc_2017 = pymupdf.open('d:/quiza/scratch_osym/2017.pdf')
    txt_2017 = doc_2017[35].get_text()
    pos_gk = txt_2017.find('GENEL KÜLTÜR')
    gy_part = txt_2017[:pos_gk]
    gk_part = txt_2017[pos_gk:]
    for qstr, ans in re.findall(r'(\d+)\.\s+([A-E])\b', gy_part):
        keys[(2017, 'GY', int(qstr))] = ans.lower()
    for qstr, ans in re.findall(r'(\d+)\.\s+([A-E])\b', gk_part):
        keys[(2017, 'GK', int(qstr))] = ans.lower()

    # 6. 2015: Page 29 (GY), Page 30 (GK)
    doc_2015 = pymupdf.open('d:/quiza/scratch_osym/2015.pdf')
    for qstr, ans in re.findall(r'(\d+)\.\s*\n?\s*([A-E])\b', doc_2015[28].get_text()):
        keys[(2015, 'GY', int(qstr))] = ans.lower()
    for qstr, ans in re.findall(r'(\d+)\.\s*\n?\s*([A-E])\b', doc_2015[29].get_text()):
        keys[(2015, 'GK', int(qstr))] = ans.lower()

    # 7. 2014: Page 31 (GY), Page 32 (GK)
    doc_2014 = pymupdf.open('d:/quiza/scratch_osym/2014.pdf')
    for qstr, ans in re.findall(r'(\d+)\.\s*\n?\s*([A-E])\b', doc_2014[30].get_text()):
        keys[(2014, 'GY', int(qstr))] = ans.lower()
    for qstr, ans in re.findall(r'(\d+)\.\s*\n?\s*([A-E])\b', doc_2014[31].get_text()):
        keys[(2014, 'GK', int(qstr))] = ans.lower()

    # 8. 2013: Page 34 (GY on left, GK on right)
    doc_2013 = pymupdf.open('d:/quiza/scratch_osym/2013.pdf')
    p34 = doc_2013[33]
    w = p34.rect.width
    gy_txt = p34.get_text(clip=pymupdf.Rect(0, 0, w/2, p34.rect.height))
    gk_txt = p34.get_text(clip=pymupdf.Rect(w/2, 0, w, p34.rect.height))
    for qstr, ans in re.findall(r'(\d+)\.\s+([A-E])\b', gy_txt):
        keys[(2013, 'GY', int(qstr))] = ans.lower()
    for qstr, ans in re.findall(r'(\d+)\.\s+([A-E])\b', gk_txt):
        keys[(2013, 'GK', int(qstr))] = ans.lower()

    # 9. 2012: Page 32 (GY on left, GK on right)
    doc_2012 = pymupdf.open('d:/quiza/scratch_osym/2012.pdf')
    p32 = doc_2012[31]
    w = p32.rect.width
    gy_txt = p32.get_text(clip=pymupdf.Rect(0, 0, w/2, p32.rect.height))
    gk_txt = p32.get_text(clip=pymupdf.Rect(w/2, 0, w, p32.rect.height))
    for qstr, ans in re.findall(r'(\d+)\.\s*\n?\s*([A-E])\b', gy_txt):
        keys[(2012, 'GY', int(qstr))] = ans.lower()
    for qstr, ans in re.findall(r'(\d+)\.\s*\n?\s*([A-E])\b', gk_txt):
        keys[(2012, 'GK', int(qstr))] = ans.lower()

    # 10. 2010: Page 31 (GY), Page 32 (GK)
    doc_2010 = pymupdf.open('d:/quiza/scratch_osym/2010.pdf')
    for qstr, ans in re.findall(r'(\d+)\.\s+([A-E])\b', doc_2010[30].get_text()):
        keys[(2010, 'GY', int(qstr))] = ans.lower()
    for qstr, ans in re.findall(r'(\d+)\.\s+([A-E])\b', doc_2010[31].get_text()):
        keys[(2010, 'GK', int(qstr))] = ans.lower()

    # 11. 2009: Page 31 (GY), Page 32 (GK)
    doc_2009 = pymupdf.open('d:/quiza/scratch_osym/2009.pdf')
    for qstr, ans in re.findall(r'(\d+)\.\s+([A-E])\b', doc_2009[30].get_text()):
        keys[(2009, 'GY', int(qstr))] = ans.lower()
    for qstr, ans in re.findall(r'(\d+)\.\s+([A-E])\b', doc_2009[31].get_text()):
        keys[(2009, 'GK', int(qstr))] = ans.lower()

    return keys

if __name__ == '__main__':
    all_keys = parse_answer_keys()
    print(f"Total parsed key entries: {len(all_keys)}")
    for y in [2021, 2020, 2019, 2017, 2016, 2015, 2014, 2013, 2012, 2010, 2009]:
        gy_count = sum(1 for (yy, t, q) in all_keys if yy == y and t == 'GY')
        gk_count = sum(1 for (yy, t, q) in all_keys if yy == y and t == 'GK')
        print(f"Year {y}: GY={gy_count}, GK={gk_count}")
