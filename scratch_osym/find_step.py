import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/Halil/.gemini/antigravity-ide/brain/4ea7509a-a32e-412e-8838-11397c0a91c7/.system_generated/logs/transcript.jsonl', 'r', encoding='utf-8', errors='ignore') as fp:
    for line in fp:
        if 'halil@quiza.com' in line:
            obj = json.loads(line)
            if obj.get('source') == 'MODEL' and obj.get('type') == 'PLANNER_RESPONSE' and not obj.get('tool_calls'):
                print(f"=== Step {obj.get('step_index')} ===")
                print(obj.get('content'))
