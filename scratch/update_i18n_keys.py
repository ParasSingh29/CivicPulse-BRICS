import json
import re

extra_keys = {
    "en": {
        "badge_underfunding": "SEVERE UNDERFUNDING",
        "badge_surplus": "SURPLUS ALLOCATION",
        "badge_balanced": "OPTIMAL BALANCE",
        "btn_reopen": "Re-open Incident",
    },
    "hi": {
        "badge_underfunding": "गंभीर कम फंडिंग",
        "badge_surplus": "अधिशेष आवंटन",
        "badge_balanced": "संतुलित आवंटन",
        "btn_reopen": "शिकायत दोबारा खोलें",
    },
    "pt": {
        "badge_underfunding": "SUBFINANCIAMENTO SEVERO",
        "badge_surplus": "ALOCAÇÃO COM SUPERÁVIT",
        "badge_balanced": "EQUILÍBRIO ÓTIMO",
        "btn_reopen": "Reabrir Incidente",
    },
    "ru": {
        "badge_underfunding": "ОСТРЫЙ ДЕФИЦИТ СРЕДСТВ",
        "badge_surplus": "ПРОФИЦИТНОЕ ВЫДЕЛЕНИЕ",
        "badge_balanced": "ОПТИМАЛЬНЫЙ БАЛАНС",
        "btn_reopen": "Возобновить заявку",
    },
    "zh": {
        "badge_underfunding": "严重资金不足",
        "badge_surplus": "预算盈余分配",
        "badge_balanced": "最佳预算平衡",
        "btn_reopen": "重新打开事件",
    },
    "ta": {
        "badge_underfunding": "கடுமையான நிதி பற்றாக்குறை",
        "badge_surplus": "உபரி நிதி ஒதுக்கீடு",
        "badge_balanced": "உகந்த சமநிலை",
        "btn_reopen": "புகாரை மீண்டும் திறக்க",
    },
    "te": {
        "badge_underfunding": "తీవ్రమైన నిధుల కొరత",
        "badge_surplus": "మిగులు నిధుల కేటాయింపు",
        "badge_balanced": "సరైన బడ్జెట్ సమతుల్యత",
        "btn_reopen": "ఫిర్యాదును మళ్లీ తెరవండి",
    },
    "zu": {
        "badge_underfunding": "UKUSWELEKA KWEZIMALI OKUKHULU",
        "badge_surplus": "UKWABIWA KWENZALO ETHE XAXA",
        "badge_balanced": "UKULINGANA OKUFANELEKILE",
        "btn_reopen": "Vula Kabusha Isikhalazo",
    },
    "af": {
        "badge_underfunding": "ERNSTIGE ONDERBEFONDSING",
        "badge_surplus": "SURPLUS TOEWYSING",
        "badge_balanced": "OPTIMALE BALANS",
        "btn_reopen": "Heropen Klagte",
    }
}

with open("scratch/build_comprehensive_i18n.py", "r", encoding="utf-8") as f:
    code = f.read()

# Append extra keys injection before js_content formatting
injection = """
# Inject extra keys across all languages
for lang, kvs in """ + repr(extra_keys) + """.items():
    if lang in ALL_TRANSLATIONS:
        ALL_TRANSLATIONS[lang].update(kvs)
"""

if "# Inject extra keys across all languages" not in code:
    code = code.replace('js_content = f"""/**', injection + '\njs_content = f"""/**')

# Add window.i18n alias and auto-init to the template
if "window.i18n = window.getTranslation;" not in code:
    code = code.replace(
        "window.getTranslation = function(key, fallback = '') {{",
        "window.getTranslation = function(key, fallback = '') {{\n};\nwindow.i18n = window.getTranslation;\nwindow.getTranslation = function(key, fallback = '') {{"
    )

auto_init_snippet = """
  // Setup change event listeners on all language dropdowns
  document.querySelectorAll('#lang-selector, #login-lang-select, .lang-select').forEach(sel => {{
    sel.addEventListener('change', (e) => {{
      window.setLanguage(e.target.value);
    }});
  }});
}};

// Auto-initialize language engine upon page readiness
if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', window.initLanguage);
}} else {{
  window.initLanguage();
}}
"""

code = re.sub(
    r"  // Setup change event listeners on all language dropdowns.*?document\.querySelectorAll\(.*?\}\);\s*\}\};",
    auto_init_snippet.strip(),
    code,
    flags=re.DOTALL
)

with open("scratch/build_comprehensive_i18n.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated scratch/build_comprehensive_i18n.py successfully.")
