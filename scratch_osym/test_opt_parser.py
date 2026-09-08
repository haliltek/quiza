import re

lines = [
    "A) Hat                              B) Maden işçiliği",
    "C) Heykel                           D) Oyma",
    "                    E) Dokuma",
    "A) Yalnız I                B) Yalnız II            C) I ve II",
    "              D) II ve III          E) I, II ve III"
]

def parse_line_options(line):
    # Match all options like A) ... B) ...
    matches = list(re.finditer(r'([A-E])\)\s*', line))
    if not matches:
        return None
    opts = {}
    for i, m in enumerate(matches):
        letter = m.group(1).lower()
        val_start = m.end()
        val_end = matches[i + 1].start() if i + 1 < len(matches) else len(line)
        val = line[val_start:val_end].strip()
        opts[letter] = val
    return opts

for l in lines:
    print(f"Line: {l}")
    print(f"Parsed: {parse_line_options(l)}")
    print("-" * 40)
