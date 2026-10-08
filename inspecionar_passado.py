import json

with open(r'C:\Users\SAAV166\.gemini\antigravity-ide\brain\eb6f2ecc-e154-4018-9c8a-24824ad3e36c\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        d = json.loads(line)
        idx = d.get('step_index')
        if idx is not None and idx >= 270:
            print(f"=== STEP {idx} : {d.get('type')} ===")
            if d.get('tool_calls'):
                for tc in d['tool_calls']:
                    print("CALL:", tc.get('name') or tc.get('tool_name'), tc.get('arguments') or tc.get('args'))
            if d.get('content'):
                print("CONTENT:", str(d.get('content'))[:500].encode('ascii', errors='replace').decode('ascii'))
