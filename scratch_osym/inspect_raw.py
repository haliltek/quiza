import fitz

doc = fitz.open('d:/quiza/scratch_osym/2013.pdf')
page = doc[31]
text_instances = page.get_text("blocks")
for b in text_instances:
    # b is (x0, y0, x1, y1, text, block_no, block_type)
    if "Orhan" in b[4]:
        print("Block:", repr(b[4]))
        for ch in b[4]:
            print(f"{ch} (U+{ord(ch):04X})", end=" ")
        print()
