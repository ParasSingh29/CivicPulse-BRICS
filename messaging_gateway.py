from datetime import datetime
from api_client import save_complaint
from gemini_helper import triage_complaint
from brics_context import get_active_brics_node

# ==============================================================================
# MESSAGING APP DPI GATEWAY (WHATSAPP / TELEGRAM SIMULATOR & WEBHOOKS)
# ==============================================================================

SAMPLE_WHATSAPP_PROMPTS = [
    {
        "lang": "🇮🇳 Hindi (Delhi)",
        "sender": "+91 98101 23456",
        "text": "नमस्ते, पीतमपुरा मेन आउटर रिंग रोड पर 4 दिन से पीने का पानी नहीं आ रहा है, टैंकर वाले मनमाना पैसा मांग रहे हैं। कृपया पाइपलाइन ठीक करवाएं।",
        "ward": "Ward 12 - Pitampura",
        "category": "Water Supply & Pipeline Leakage"
    },
    {
        "lang": "🇧🇷 Portuguese (São Paulo)",
        "sender": "+55 11 98765 4321",
        "text": "Olá, temos um rompimento grave de adutora de água na Zona Leste, Itaquera. A rua está alagada e sem água nas casas há 3 dias.",
        "ward": "Zona Leste - Itaquera",
        "category": "Water Supply & Pipeline Leakage"
    },
    {
        "lang": "🇿🇦 English (Johannesburg)",
        "sender": "+27 82 123 4567",
        "text": "Hello, Diepsloot main gravel access culvert has completely collapsed after storm runoff. School buses and ambulances cannot enter.",
        "ward": "Region A - Diepsloot",
        "category": "Roads, Bridges & Arterial Corridors"
    }
]

def process_messaging_complaint(sender_id, message_text, brics_node):
    """
    Parses incoming messaging app text (WhatsApp/Telegram/SMS) using AI,
    geotags to local ward, triages urgency, and saves to national DPI stream.
    """
    node_name = brics_node.get("country", "India")
    curr_wards = [w["name"] for w in brics_node.get("wards", [])]

    # Heuristic / AI categorization across 10 sectors
    text_lower = message_text.lower()
    if any(k in text_lower for k in ["água", "water", "पानी", "pipe", "adutora", "drain"]):
        cat = "Water Supply & Pipeline Leakage"
    elif any(k in text_lower for k in ["road", "rua", "pothole", "culvert", "asfalto", "सड़क", "bridge", "flyover"]):
        cat = "Roads, Bridges & Arterial Corridors"
    elif any(k in text_lower for k in ["luz", "power", "wire", "elétr", "बिजली", "cable", "transformer"]):
        cat = "Electricity, Streetlights & Grid"
    elif any(k in text_lower for k in ["flood", "alagamento", "inundação", "बाढ़", "stormwater", "नाला"]):
        cat = "Stormwater Drainage & Monsoon Floods"
    elif any(k in text_lower for k in ["lixo", "waste", "trash", "कचरा", "garbage", "sewer"]):
        cat = "Waste Management & Sanitation"
    elif any(k in text_lower for k in ["hospital", "clinic", "dengue", "doctor", "दवा", "स्वास्थ्य"]):
        cat = "Public Health, Clinics & Vector Control"
    elif any(k in text_lower for k in ["bus", "metro", "ônibus", "transit", "बस"]):
        cat = "Public Transport & Transit Hubs"
    else:
        cat = "General Municipal / Other Infrastructure"

    # Assign to first matching ward or default
    matched_ward = curr_wards[1] if len(curr_wards) > 1 else "Central Ward"
    for w in curr_wards:
        if any(part.lower() in text_lower for part in w.split(" ")):
            matched_ward = w
            break

    urgency = triage_complaint(message_text)

    # Save to persistent database
    location_data = {
        "address": f"{matched_ward}, {brics_node.get('jurisdiction')}",
        "latitude": 28.6139 if "India" in node_name else (-23.5505 if "Brazil" in node_name else -26.2041),
        "longitude": 77.2090 if "India" in node_name else (-46.6333 if "Brazil" in node_name else 28.0473),
        "city": node_name,
        "channel": "WhatsApp DPI Gateway"
    }

    complaint_id = save_complaint(
        user_id=f"WhatsApp: {sender_id}",
        category=cat,
        description=f"[WhatsApp Voice/Text Ingestion] {message_text} | Priority: {urgency} | Geotag: {matched_ward}",
        location=location_data
    )

    return {
        "id": complaint_id,
        "category": cat,
        "ward": matched_ward,
        "urgency": urgency,
        "timestamp": datetime.now().strftime("%I:%M %p")
    }
