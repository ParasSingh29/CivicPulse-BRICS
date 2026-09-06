import json
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('static/js/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'window\.I18N\s*=\s*(\{.*?\});\s*/\*\*', content, re.DOTALL)
if not m:
    print('Failed to extract window.I18N from static/js/i18n.js')
    exit(1)

i18n = json.loads(m.group(1))
languages = list(i18n.keys())
print('Loaded languages:', languages)

html_files = ['static/login.html', 'static/citizen.html', 'static/city_official.html', 'static/central_official.html', 'static/government.html']
total_missing = 0

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        html = f.read()
    
    text_keys = re.findall(r'data-i18n="([^"]+)"', html)
    ph_keys = re.findall(r'data-i18n-placeholder="([^"]+)"', html)
    all_keys = sorted(list(set(text_keys + ph_keys)))
    print(f"\n=== Checking {hf}: {len(all_keys)} unique i18n keys ===")
    
    for lang in languages:
        missing = [k for k in all_keys if k not in i18n[lang]]
        if missing:
            print(f"  ❌ [{lang}] missing {len(missing)} keys: {missing[:5]}")
            total_missing += len(missing)
        else:
            print(f"  ✓ [{lang}] 100% coverage ({len(all_keys)}/{len(all_keys)} keys)")

if total_missing == 0:
    print("\n🎉 PERFECT: 100% i18n coverage across all HTML files and all 9 BRICS languages!")
else:
    print(f"\n⚠️ Total missing translations: {total_missing}")
