import re

translations = {
    "en": {
        "btn_use_current_location": "Use Current Location",
        "btn_voice_input": "Speak with AI",
        "lbl_problem": "What is the problem? *",
        "lbl_neighborhood_ward": "Neighborhood / Ward *",
        "lbl_street_address": "Street Address or Landmark"
    },
    "hi": {
        "btn_use_current_location": "वर्तमान स्थान का उपयोग करें",
        "btn_voice_input": "एआई से बोलकर दर्ज करें",
        "lbl_problem": "समस्या क्या है? *",
        "lbl_neighborhood_ward": "पड़ोस / वार्ड *",
        "lbl_street_address": "सड़क का पता या लैंडमार्क"
    },
    "pt": {
        "btn_use_current_location": "Usar Localização Atual",
        "btn_voice_input": "Falar com IA",
        "lbl_problem": "Qual é o problema? *",
        "lbl_neighborhood_ward": "Bairro / Zona *",
        "lbl_street_address": "Endereço ou Ponto de Referência"
    },
    "ru": {
        "btn_use_current_location": "Использовать текущее местоположение",
        "btn_voice_input": "Голосовой ввод ИИ",
        "lbl_problem": "В чем проблема? *",
        "lbl_neighborhood_ward": "Район / Округ *",
        "lbl_street_address": "Улица или ориентир"
    },
    "zh": {
        "btn_use_current_location": "使用当前位置",
        "btn_voice_input": "语音AI输入",
        "lbl_problem": "具体问题是什么？*",
        "lbl_neighborhood_ward": "社区 / 街道 *",
        "lbl_street_address": "街道地址或地标"
    },
    "ta": {
        "btn_use_current_location": "தற்போதைய இருப்பிடத்தைப் பயன்படுத்து",
        "btn_voice_input": "குரல் மூலம் பேசுங்கள் (AI)",
        "lbl_problem": "பிரச்சினை என்ன? *",
        "lbl_neighborhood_ward": "பகுதி / வார்டு *",
        "lbl_street_address": "தெரு முகவரி அல்லது அடையாளம்"
    },
    "te": {
        "btn_use_current_location": "ప్రస్తుత స్థానాన్ని ఉపయోగించండి",
        "btn_voice_input": "వాయిస్ ద్వారా మాట్లాడండి (AI)",
        "lbl_problem": "సమస్య ఏమిటి? *",
        "lbl_neighborhood_ward": "ప్రాంతం / వార్డు *",
        "lbl_street_address": "వీధి చిరునామా లేదా ల్యాండ్‌మార్క్"
    },
    "zu": {
        "btn_use_current_location": "Sebenzisa Indawo Yamanje",
        "btn_voice_input": "Khuluma nge-AI",
        "lbl_problem": "Yini inkinga? *",
        "lbl_neighborhood_ward": "Indawo / Iwadi *",
        "lbl_street_address": "Ikheli Lomgwaqo noma Indawo Eyaziwayo"
    },
    "af": {
        "btn_use_current_location": "Gebruik Huidige Ligging",
        "btn_voice_input": "Praat met AI",
        "lbl_problem": "Wat is die probleem? *",
        "lbl_neighborhood_ward": "Buurt / Wyk *",
        "lbl_street_address": "Straatadres of Baken"
    }
}

path = r"c:\Users\pbabu\OneDrive\Desktop\CivicPulse-BRICS\static\js\i18n.js"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

for lang, keys in translations.items():
    # Find pattern like `lang: {\n`
    pattern = rf"(\b{lang}\s*:\s*\{{)"
    replacement_lines = "\n" + "\n".join([f'    {k}: "{v}",' for k, v in keys.items()])
    content = re.sub(pattern, rf"\1{replacement_lines}", content, count=1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully injected form i18n keys!")
