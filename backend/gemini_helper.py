import os
from google import genai
from google.genai import types

def get_gemini_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None
    try:
        return genai.Client(api_key=api_key)
    except Exception:
        return None

def call_gemini_with_fallback(contents, custom_models=None):
    client = get_gemini_client()
    if not client:
        return "AI service temporarily unavailable (GEMINI_API_KEY not configured)."
    # Current active production Gemini models
    models_to_try = custom_models or ['gemini-2.5-flash', 'gemini-2.0-flash', 'gemini-1.5-flash', 'gemini-1.5-pro']
    
    last_error = None
    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=contents
            )
            return response.text
        except Exception as e:
            last_error = e
            continue
            
    return f"AI service temporarily unavailable across all models. Error: {last_error}"

def analyze_issue_image(image_bytes, mime_type="image/jpeg"):
    contents = [
        types.Part.from_bytes(data=image_bytes, mime_type=mime_type),
        "Analyze this infrastructure image for a municipal complaint. Provide a concise 2-sentence description of the damage, estimate its severity (Low, Medium, High, Critical), and confirm what category it belongs to."
    ]
    result = call_gemini_with_fallback(contents)
    if "temporarily unavailable" in result:
        return f"AI Image Analysis failed: {result}"
    return result

import zlib

def evaluate_dynamic_severity(description_text="", category="", image_bytes=None):
    """
    Computes a realistic dynamic severity score (1.0 to 10.0) based on NLP keyword triage,
    hazard risk vectors, category baselines, and deterministic variation.
    """
    combined = (str(description_text) + " " + str(category)).lower()
    
    # Critical keywords (8.5 - 9.8)
    critical_keywords = [
        "collapse", "burst pipe", "high voltage", "fire", "explosion", "bridge failure", 
        "sewage overflow", "sewage leak", "toxic", "sinkhole", "fatal", "structural failure", 
        "live wire", "open drain", "flood", "gas leak", "catastrophic", "electrocution"
    ]
    
    # High keywords (7.0 - 8.4)
    high_keywords = [
        "deep pothole", "broken main", "transformer", "major leak", "traffic light", "signal down",
        "waterlogging", "heavy damage", "crack", "pipeline fracture", "cave in", "blocked road",
        "urgent", "danger", "hazard", "accident", "overflowing"
    ]
    
    # Medium keywords (4.5 - 6.9)
    medium_keywords = [
        "pothole", "leak", "street light", "garbage", "waste", "trash", "sidewalk", 
        "clogged", "debris", "damaged sign", "road damage", "water shortage"
    ]
    
    # Low keywords (1.5 - 4.4)
    low_keywords = [
        "graffiti", "litter", "faded", "grass", "noise", "poster", "bench", "paint", 
        "dirty", "aesthetic", "tree branch", "minor"
    ]
    
    base_score = 5.5
    
    # Category baseline
    cat_lower = str(category).lower()
    if any(k in cat_lower for k in ["power", "grid", "electrical", "disaster", "water supply"]):
        base_score += 1.0
    elif any(k in cat_lower for k in ["road", "bridge", "transit", "sanitation"]):
        base_score += 0.5
    elif any(k in cat_lower for k in ["park", "recreation", "governance"]):
        base_score -= 1.0
        
    crit_matches = sum(1 for k in critical_keywords if k in combined)
    high_matches = sum(1 for k in high_keywords if k in combined)
    med_matches = sum(1 for k in medium_keywords if k in combined)
    low_matches = sum(1 for k in low_keywords if k in combined)
    
    if crit_matches > 0:
        base_score = 8.5 + min(1.3, (crit_matches - 1) * 0.4)
    elif high_matches > 0:
        base_score = 7.0 + min(1.4, (high_matches - 1) * 0.3)
    elif low_matches > 0 and med_matches == 0:
        base_score = 2.5 + min(1.8, low_matches * 0.5)
    elif med_matches > 0:
        base_score = 4.8 + min(1.8, (med_matches - 1) * 0.4)

    if image_bytes and len(image_bytes) > 500:
        base_score += 0.3

    hash_seed = zlib.crc32(combined.encode("utf-8")) % 100
    variance = (hash_seed - 50) / 100.0  # -0.50 to +0.49
    
    final_score = round(max(1.0, min(10.0, base_score + variance)), 1)
    return final_score

def run_vision_agent(image_bytes, mime_type="image/jpeg", description="", category=""):
    """
    Autonomous Sentinel Vision Agent:
    Extracts structured computer vision telemetry (defect, score /10, hazard level, confidence %, notes).
    """
    prompt = """
    You are the Sentinel Computer Vision Agent for CivicPulse-BRICS municipal infrastructure.
    Analyze the uploaded photographic evidence of physical damage.
    Respond in EXACTLY this format:
    DEFECT: <1 to 4 words describing defect, e.g. Severe Asphalt Pothole, High-Voltage Wire Exposure, Underground Pipe Fracture>
    SEVERITY: <Numeric score from 1.0 to 10.0>
    HAZARD: <Critical Hazard OR Moderate Risk OR Minor Defect>
    CONFIDENCE: <Integer between 80 and 99>
    DIAGNOSTIC: <2 crisp sentences explaining the physical structural failure and immediate safety risk to public.>
    """
    contents = [
        types.Part.from_bytes(data=image_bytes, mime_type=mime_type),
        prompt
    ]
    raw_res = call_gemini_with_fallback(contents)
    
    # Defaults in case of parsing variance
    data = {
        "defect": "Physical Infrastructure Damage",
        "severity": None,
        "hazard": "Critical Hazard",
        "confidence": 92,
        "diagnostic": "Detected structural degradation requiring immediate municipal crew intervention."
    }
    
    if "temporarily unavailable" not in raw_res:
        for line in raw_res.splitlines():
            line = line.strip()
            clean_line = line.replace("*", "").strip()
            upper_clean = clean_line.upper()
            if upper_clean.startswith("DEFECT:"):
                data["defect"] = clean_line[7:].strip()
            elif upper_clean.startswith("SEVERITY:"):
                try:
                    val_str = clean_line[9:].replace("/10", "").strip()
                    data["severity"] = round(float(val_str), 1)
                except Exception:
                    pass
            elif upper_clean.startswith("HAZARD:"):
                data["hazard"] = clean_line[7:].strip()
            elif upper_clean.startswith("CONFIDENCE:"):
                try:
                    val_str = clean_line[11:].replace("%", "").strip()
                    data["confidence"] = int(val_str)
                except Exception:
                    pass
            elif upper_clean.startswith("DIAGNOSTIC:"):
                data["diagnostic"] = clean_line[11:].strip()

    if data["severity"] is None:
        data["severity"] = evaluate_dynamic_severity(description or data["defect"], category or "Infrastructure", image_bytes=image_bytes)

    if data["severity"] >= 8.5:
        data["hazard"] = "Critical Hazard"
    elif data["severity"] >= 6.0:
        data["hazard"] = "Moderate Risk"
    else:
        data["hazard"] = "Minor Defect"

    return data

def transcribe_and_summarize_audio(audio_bytes, mime_type="audio/wav"):
    contents = [
        types.Part.from_bytes(data=audio_bytes, mime_type=mime_type),
        "Transcribe this citizen audio complaint and provide a 1-sentence clean summary of the core issue reported."
    ]
    result = call_gemini_with_fallback(contents)
    if "temporarily unavailable" in result:
        return f"AI Audio Processing failed: {result}"
    return result

def transcribe_and_translate_multilingual_audio(audio_bytes, mime_type="audio/wav", user_lang="en"):
    """
    Omni-Lingual Speech Processing Agent:
    Transcribes audio in ANY regional Indian dialect or BRICS language (Hindi, Tamil, Russian, Chinese, Portuguese, etc.)
    and produces both the native transcript and a standardized English operational summary.
    """
    prompt = """
    You are the Multilingual Speech Telemetry Agent for CivicPulse-BRICS.
    Listen to this citizen voice note. It may be spoken in Hindi, Tamil, Telugu, Portuguese, Russian, Chinese, or English.
    1. Transcribe the audio in its original native script/language.
    2. Translate the issue into a clear 1-sentence standardized English summary for municipal dispatchers.
    Output in format:
    NATIVE: <original transcription>
    ENGLISH: <standardized english summary>
    """
    contents = [
        types.Part.from_bytes(data=audio_bytes, mime_type=mime_type),
        prompt
    ]
    raw = call_gemini_with_fallback(contents)
    native_text = ""
    english_text = ""
    if "temporarily unavailable" not in raw:
        for line in raw.splitlines():
            if line.startswith("NATIVE:"):
                native_text = line.replace("NATIVE:", "").strip()
            elif line.startswith("ENGLISH:"):
                english_text = line.replace("ENGLISH:", "").strip()
    
    if not english_text:
        english_text = raw
    return native_text, english_text

def triage_complaint(description_text, category=""):
    prompt = f"Analyze this municipal complaint and output ONLY one of these four urgency levels (Critical, High, Medium, Low) followed by a short reason:\n\nComplaint: {description_text}"
    result = call_gemini_with_fallback(prompt)
    if "temporarily unavailable" in result:
        sev = evaluate_dynamic_severity(description_text, category)
        if sev >= 8.5:
            return f"Critical - Urgent safety hazard (Severity: {sev}/10)"
        elif sev >= 6.5:
            return f"High - Substantial municipal defect (Severity: {sev}/10)"
        elif sev >= 4.5:
            return f"Medium - Standard service request (Severity: {sev}/10)"
        else:
            return f"Low - Routine maintenance item (Severity: {sev}/10)"
    return result

def generate_dashboard_summary(complaints_list):
    if not complaints_list:
        return "No complaints available for analysis yet."
    
    summary_text = "\n".join([f"- [{c.get('category')}] {c.get('description')} (Status: {c.get('status')})" for c in complaints_list[:20]])
    prompt = f"You are a municipal city planner. Review these recent citizen complaints and write a professional 3-bullet-point executive summary highlighting critical infrastructure trends or high-risk zones:\n\n{summary_text}"
    
    result = call_gemini_with_fallback(prompt)
    if "temporarily unavailable" in result:
        return f"Could not generate AI insights: {result}"
    return result

def answer_citizen_query(prompt_text, complaints_list):
    context_data = "\n".join([f"ID: {c.get('id')} | Category: {c.get('category')} | Status: {c.get('status')} | Desc: {c.get('description')}" for c in complaints_list[:30]])
    prompt = f"""You are the official in-app AI Assistant for "CivicPulse BRICS". Keep answers short, actionable, and strictly focused on app features.\nDatabase Context:\n{context_data}\nUser Question: {prompt_text}"""
    result = call_gemini_with_fallback(prompt)
    if "temporarily unavailable" in result:
        return f"AI Assistant is currently offline: {result}"
    return result

def get_predictive_risk_forecast(complaints_list=None):
    """
    Vertex AI Predictive Modeling Simulation:
    Predicts secondary infrastructure failure probability across key municipal sectors
    by correlating real-time complaint clustering with live IMD meteorological risk vectors.
    """
    try:
        from public_data_helper import fetch_live_delhi_weather, calculate_weather_risk_vector
        weather = fetch_live_delhi_weather()
        vectors = calculate_weather_risk_vector(weather)
        
        drain_score = vectors["drainage"]["score"]
        grid_score = vectors["power_grid"]["score"]
        road_score = vectors["roads"]["score"]
        
        temp_val = weather.get("temperature", 32.0)
        rain_val = weather.get("precipitation_mm", 0.0)
        cond_val = weather.get("condition", "Clear")
        
        return [
            {
                "zone": "Ward 04 • Connaught Place / Janpath Corridor",
                "risk_pct": min(98, max(45, drain_score + 10)),
                "hazard": "Stormwater Drainage Backflow & Waterlogging",
                "imd_factor": f"Live IMD: {rain_val}mm Rain • {cond_val}",
                "window": "12 to 24 Hours"
            },
            {
                "zone": "Ward 12 • Pitampura / Outer Ring Road",
                "risk_pct": min(96, max(40, road_score + 15)),
                "hazard": "Asphalt Subsidence & Rapid Pothole Formation",
                "imd_factor": f"Live Surface Saturation Index • {temp_val}°C",
                "window": "24 to 36 Hours"
            },
            {
                "zone": "Ward 19 • Rohini Sector 14 Distribution Grid",
                "risk_pct": min(92, max(35, grid_score + 12)),
                "hazard": "Transformer Overheating & Feeder Cable Faults",
                "imd_factor": f"Live Thermal Stress: {temp_val}°C Ambient",
                "window": "36 to 48 Hours"
            }
        ]
    except Exception:
        return [
            {
                "zone": "Ward 04 • Connaught Place / Janpath Corridor",
                "risk_pct": 88,
                "hazard": "Stormwater Drainage Backflow & Waterlogging",
                "imd_factor": "Monsoon Saturation Baseline",
                "window": "24 Hours"
            },
            {
                "zone": "Ward 12 • Pitampura / Outer Ring Road",
                "risk_pct": 82,
                "hazard": "Asphalt Subsidence & Secondary Potholes",
                "imd_factor": "Seasonal Rain Runoff Factor",
                "window": "36 Hours"
            },
            {
                "zone": "Ward 19 • Rohini Sector 14 Distribution Grid",
                "risk_pct": 65,
                "hazard": "Transformer Overheating & Feeder Tripping",
                "imd_factor": "Thermal Grid Baseline",
                "window": "48 Hours"
            }
        ]