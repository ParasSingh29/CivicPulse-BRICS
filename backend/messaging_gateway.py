import os
import json
import urllib.request
from datetime import datetime
from api_client import save_complaint
from gemini_helper import triage_complaint
from brics_context import get_active_brics_node

# ==============================================================================
# MESSAGING APP DPI GATEWAY (WHATSAPP / TELEGRAM REAL WEBHOOKS & SIMULATOR)
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

def process_messaging_complaint(sender_id, message_text, brics_node, channel="WhatsApp DPI Gateway", category=None, address=None, photo_bytes=None):
    """
    Parses incoming messaging app text (WhatsApp/Telegram/SMS) using AI,
    geotags to local ward, triages urgency, and saves to national DPI stream.
    Supports explicit category, exact user address, and photo bytes.
    """
    node_name = brics_node.get("country", "India")
    curr_wards = [w["name"] for w in brics_node.get("wards", [])]

    # Category selection: explicit or heuristic
    if category and str(category).strip():
        cat = str(category).strip()
    else:
        text_lower = message_text.lower()
        if any(k in text_lower for k in ["água", "water", "पानी", "pipe", "adutora", "drain", "waterlogging", "leak"]):
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

    # Address determination: preserve EXACT user-supplied detailed address!
    final_address = str(address).strip() if (address and str(address).strip()) else f"{curr_wards[0] if curr_wards else 'Central Ward'}, {brics_node.get('jurisdiction', 'Metropolitan Node')}"

    # Assign ward based on address/text matching or default
    matched_ward = curr_wards[0] if curr_wards else "Central Ward"
    comb_txt = (final_address + " " + message_text).lower()
    for w in curr_wards:
        parts = [p for p in w.split(" ") if len(p) > 2 and p.lower() not in ["ward", "region", "district", "zone"]]
        if any(p.lower() in comb_txt for p in parts):
            matched_ward = w
            break

    # Analyze optional defect photo if uploaded
    ai_vision_note = ""
    if photo_bytes and len(photo_bytes) > 500:
        try:
            from gemini_helper import run_vision_agent
            v_res = run_vision_agent(photo_bytes, description=message_text, category=cat)
            sev_val = v_res.get('severity') or 6.5
            ai_vision_note = f"\n\n[Sentinel Vision AI]: {v_res.get('defect', 'Infrastructure Defect')} (Severity: {sev_val}/10, Risk: {v_res.get('hazard', 'High')}). {v_res.get('diagnostic', '')}"
        except Exception as ve:
            print(f"[Chatbot Vision Error] {ve}")

    if not ai_vision_note:
        from gemini_helper import evaluate_dynamic_severity
        dyn_sev = evaluate_dynamic_severity(message_text, cat)
        ai_vision_note = f"\n\n[Sentinel Severity]: Severity: {dyn_sev}/10"

    full_triage_text = f"Problem: {cat} | Address: {final_address} | Details: {message_text}{ai_vision_note}"
    urgency = triage_complaint(full_triage_text, cat)

    # Save to persistent database with exact location address
    node_coords = brics_node.get("coordinates", {})
    base_lat = node_coords.get("lat", 28.6139)
    base_lon = node_coords.get("lon", 77.2090)

    location_data = {
        "address": final_address,
        "ward": matched_ward,
        "latitude": base_lat,
        "longitude": base_lon,
        "city": node_name,
        "channel": channel
    }

    desc_to_save = f"[{channel}] Category: {cat} | Address: {final_address} | Notes: {message_text}{ai_vision_note} | Priority: {urgency}"

    complaint_id = save_complaint(
        user_id=f"{channel}: {sender_id}",
        category=cat,
        description=desc_to_save,
        location=location_data
    )

    formatted_bot_reply = (
        f"🏛️ *CivicPulse-BRICS Official Bot*\n"
        f"✅ *Grievance Registered Successfully*\n\n"
        f"🆔 *Complaint ID:* `{complaint_id}`\n"
        f"🏗️ *Problem Type:* {cat}\n"
        f"📍 *Accurate Address:* {final_address}\n"
        f"⚡ *AI Urgency:* {urgency} (Gemini AI Triaged)\n"
        f"📷 *Photo Attached:* {'Yes (Analyzed by Sentinel AI)' if ai_vision_note else 'None'}\n"
        f"⏰ *Timestamp:* {datetime.now().strftime('%I:%M %p')}\n\n"
        f"📋 *Status:* Transmitted to Municipal Chief Engineer & BRICS CapEx Planning Matrix.\n"
        f"🌐 *Track online:* http://localhost:8000/citizen"
    )

    return {
        "id": complaint_id,
        "category": cat,
        "address": final_address,
        "ward": matched_ward,
        "urgency": urgency,
        "has_photo": bool(ai_vision_note),
        "timestamp": datetime.now().strftime("%I:%M %p"),
        "channel": channel,
        "reply": formatted_bot_reply
    }


def send_telegram_message_http(chat_id, text):
    """Optionally dispatches real HTTP message back to Telegram API if bot token is provided."""
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token or not chat_id:
        return False
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = json.dumps({
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "Markdown"
        }).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"[Telegram Bot HTTP Error] {e}")
        return False


def process_telegram_webhook_payload(payload, brics_node):
    """
    Parses native Telegram Bot API webhook updates:
    https://core.telegram.org/bots/api#update
    """
    try:
        msg = payload.get("message") or payload.get("edited_message") or {}
        chat = msg.get("chat", {})
        chat_id = chat.get("id")
        from_user = msg.get("from", {})
        sender_name = from_user.get("first_name", "Citizen")
        sender_username = from_user.get("username", str(chat_id))
        text = msg.get("text") or msg.get("caption") or ""

        if not text:
            # Handle voice note or photo caption if text empty
            if msg.get("voice") or msg.get("audio"):
                text = "[Voice Note Received] Infrastructure damage reported via Telegram audio."
            elif msg.get("photo"):
                text = "[Photo Uploaded] Hazardous infrastructure defect captured via Telegram camera."
            else:
                text = "Citizen infrastructure query submitted via Telegram."

        res = process_messaging_complaint(
            sender_id=f"@{sender_username}" if sender_username else f"ID_{chat_id}",
            message_text=text,
            brics_node=brics_node,
            channel="Telegram Bot DPI Gateway"
        )

        if chat_id:
            send_telegram_message_http(chat_id, res["reply"])

        return {
            "status": "success",
            "channel": "Telegram",
            "chat_id": chat_id,
            "grievance": res
        }
    except Exception as e:
        print(f"[Telegram Webhook Parser Error] {e}")
        return {"status": "error", "message": str(e)}


def process_whatsapp_webhook_payload(payload, brics_node):
    """
    Parses both Meta WhatsApp Cloud API payloads and Twilio WhatsApp webhook payloads:
    - Meta Cloud API: payload['entry'][0]['changes'][0]['value']['messages'][0]
    - Twilio API: form fields (From, Body)
    """
    sender_id = "+91 98101 00000"
    message_text = ""

    try:
        # Check if Meta WhatsApp Cloud API format
        if isinstance(payload, dict) and "entry" in payload:
            entry = payload.get("entry", [])[0]
            changes = entry.get("changes", [])[0]
            value = changes.get("value", {})
            messages = value.get("messages", [])
            if messages:
                msg = messages[0]
                sender_id = msg.get("from", sender_id)
                if msg.get("type") == "text":
                    message_text = msg.get("text", {}).get("body", "")
                elif msg.get("type") == "audio":
                    message_text = "[WhatsApp Voice Note] Citizen audio report received."
                elif msg.get("type") == "image":
                    message_text = msg.get("image", {}).get("caption", "[WhatsApp Photo] Defect uploaded.")

        # Check if Twilio / Form Data format
        elif isinstance(payload, dict) and ("Body" in payload or "From" in payload):
            sender_id = payload.get("From", sender_id).replace("whatsapp:", "")
            message_text = payload.get("Body", "")

        # Fallback dictionary payload
        elif isinstance(payload, dict):
            sender_id = payload.get("sender", payload.get("from", sender_id))
            message_text = payload.get("message", payload.get("text", payload.get("body", "")))

        if not message_text:
            message_text = "Water supply leakage and damaged road near neighborhood."

        res = process_messaging_complaint(
            sender_id=sender_id,
            message_text=message_text,
            brics_node=brics_node,
            channel="WhatsApp DPI Gateway"
        )

        return {
            "status": "success",
            "channel": "WhatsApp",
            "sender": sender_id,
            "grievance": res
        }
    except Exception as e:
        print(f"[WhatsApp Webhook Parser Error] {e}")
        return {"status": "error", "message": str(e)}

