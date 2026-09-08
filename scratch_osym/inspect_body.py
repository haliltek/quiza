import sys, re
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\Halil\.gemini\antigravity-ide\brain\c6d98a08-2e4f-4268-9dc3-134a590c7dc4\.system_generated\steps\1052\content.md'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

print("Total length:", len(content))
# Find <body>
m = re.search(r'<body', content, re.IGNORECASE)
print("<body found:", bool(m))
if m:
    body_idx = m.start()
    body_text = content[body_idx:body_idx+2000]
    print("Body snippet:\n", body_text)
