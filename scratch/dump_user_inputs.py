import json

with open('scratch_user_inputs.txt', 'w', encoding='utf-8') as out:
    with open(r'C:\Users\SAAV166\.gemini\antigravity-ide\brain\eb6f2ecc-e154-4018-9c8a-24824ad3e36c\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
        for line in f:
            d = json.loads(line)
            idx = d.get('step_index')
            if d.get('type') == 'USER_INPUT':
                out.write(f"=== STEP {idx} USER_INPUT ===\n")
                out.write(str(d.get('content')) + "\n\n")

print("Dump complete")
