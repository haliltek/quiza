import os, glob, json

pattern = 'C:/Users/Halil/.gemini/antigravity-ide/brain/*/.system_generated/logs/transcript.jsonl'
files = glob.glob(pattern)
print(f"Found {len(files)} transcript files.")

for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        for i, line in enumerate(fp):
            if 'halil@quiza.com' in line or 'UCSfhMkMwIgE6NObaPEByjfxH7j1' in line:
                try:
                    obj = json.loads(line)
                    content = str(obj.get('content', ''))
                    if any(k in content for k in ['şifre', 'sifre', 'password', 'login', 'giriş', 'giris', 'admin']):
                        print(f"File: {f}")
                        print(f"Step {obj.get('step_index')}: {content[:300]}\n")
                except:
                    pass
