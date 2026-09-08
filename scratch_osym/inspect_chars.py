import fitz, json

doc = fitz.open('d:/quiza/scratch_osym/2013.pdf')
raw = json.loads(doc[31].get_text('rawjson'))
found = 0
for b in raw['blocks']:
    if 'lines' in b:
        for l in b['lines']:
            for s in l['spans']:
                if 'chars' in s:
                    for c in s['chars']:
                        if c['c'] == '\ufffd':
                            print(f"Char: {c}")
                            found += 1
                            if found > 5:
                                break
                    if found > 5: break
            if found > 5: break
    if found > 5: break
