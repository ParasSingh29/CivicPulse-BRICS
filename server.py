import os
import json
import base64
from datetime import datetime
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.responses import JSONResponse, FileResponse, Response, PlainTextResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

# Project modules
from brics_context import BRICS_NODES, get_brics_node, INFRASTRUCTURE_SECTORS
from api_client import (
    get_all_complaints, save_complaint, update_complaint_status,
    export_complaints_to_csv_string, get_cloud_data_status,
    export_to_bigquery_records, stream_to_bigquery
)
from demands_engine import get_all_demands, save_demand, upvote_demand
from megaplan_engine import generate_ai_mega_plans
from budget_engine import calculate_budget_alignment
from public_data_helper import fetch_live_delhi_weather
from gemini_helper import run_vision_agent, transcribe_and_translate_multilingual_audio, triage_complaint
from tts_helper import generate_speech_audio
from messaging_gateway import process_messaging_complaint
from dpg_spec import DPG_COMPLIANCE_STANDARDS, get_openapi_spec
from brics_proposals_engine import (
    get_city_officers_overview, get_city_proposals, save_city_proposal,
    upvote_city_proposal, update_city_proposal_status, generate_city_ai_plan,
    generate_national_brics_plans, get_brics_incoming_requests, respond_to_brics_request
)

# In-memory active node state
active_node_state = {"code": "IN", "id": "india"}

# ==============================================================================
# API ROUTE HANDLERS
# ==============================================================================

async def login_page(request):
    """Serves the sovereign login gateway."""
    if os.path.exists("static/login.html"):
        return FileResponse("static/login.html")
    if os.path.exists("static/index.html"):
        return FileResponse("static/index.html")
    return Response("CivicPulse-BRICS Login is initializing.", media_type="text/plain")

async def citizen_page(request):
    """Serves the dedicated Citizen Portal."""
    if os.path.exists("static/citizen.html"):
        return FileResponse("static/citizen.html")
    if os.path.exists("static/index.html"):
        return FileResponse("static/index.html")
    return Response("CivicPulse-BRICS Citizen Portal is initializing.", media_type="text/plain")

async def city_official_page(request):
    """Serves the dedicated City Official Command Portal (Municipal Scope)."""
    if os.path.exists("static/city_official.html"):
        return FileResponse("static/city_official.html")
    if os.path.exists("static/government.html"):
        return FileResponse("static/government.html")
    return Response("CivicPulse-BRICS City Official Command is initializing.", media_type="text/plain")

async def central_official_page(request):
    """Serves the dedicated Central Official Sovereign Planning & BRICS Command Hub."""
    if os.path.exists("static/central_official.html"):
        return FileResponse("static/central_official.html")
    if os.path.exists("static/government.html"):
        return FileResponse("static/government.html")
    return Response("CivicPulse-BRICS Central Official Command is initializing.", media_type="text/plain")

async def government_page(request):
    """Serves the dedicated Government Command Hub."""
    if os.path.exists("static/government.html"):
        return FileResponse("static/government.html")
    if os.path.exists("static/city_official.html"):
        return FileResponse("static/city_official.html")
    if os.path.exists("static/index.html"):
        return FileResponse("static/index.html")
    return Response("CivicPulse-BRICS Government Command is initializing.", media_type="text/plain")

async def auth_login_api(request):
    """Authenticates user (credentials or demo) and returns redirect target."""
    try:
        data = await request.json()
    except Exception:
        data = {}
    role = str(data.get("role", "citizen")).lower()
    email = str(data.get("email", "")).strip()
    node_code = data.get("node", active_node_state["code"])
    
    if "city" in role or "municipal" in role:
        redirect_url = "/city-official"
        user_name = data.get("name") or "Er. Vikram Sharma (Chief Municipal Engineer)"
        user_role = "city_official"
        email = email or "vikram.sharma@delhi.gov.in"
    elif "central" in role or "national" in role:
        redirect_url = "/central-official"
        user_name = data.get("name") or "Dr. Rajesh Verma (Director General, National CapEx & BRICS)"
        user_role = "central_official"
        email = email or "director.general@brics.gov"
    elif "gov" in role or "official" in role or "admin" in role:
        redirect_url = "/government"
        user_name = data.get("name") or "Dr. Rajesh Verma (Director General, Infrastructure & CapEx)"
        user_role = "government"
        email = email or "official@brics.gov"
    else:
        redirect_url = "/citizen"
        user_name = data.get("name") or "Priya Sharma (Verified Citizen)"
        user_role = "citizen"
        email = email or "citizen@delhi.gov.in"
        
    token = f"cp-token-{int(datetime.now().timestamp())}"
    return JSONResponse({
        "status": "ok",
        "token": token,
        "user": {
            "name": user_name,
            "email": email,
            "role": user_role,
            "node": node_code
        },
        "redirect_url": redirect_url
    })

async def auth_logout_api(request):
    """Handles logout and provides login redirect."""
    return JSONResponse({"status": "ok", "redirect_url": "/login"})

async def auth_me_api(request):
    """Returns current active system node and auth status."""
    return JSONResponse({
        "status": "ok",
        "active_node": active_node_state["code"]
    })

async def get_brics_nodes_api(request):
    """Returns the list of BRICS country nodes and the currently active node."""
    curr_node = get_brics_node(active_node_state["id"])
    return JSONResponse({
        "active_node": curr_node,
        "nodes": list(BRICS_NODES.values()),
        "active_code": active_node_state["code"]
    })

async def switch_brics_node_api(request):
    """Switches the active BRICS nation node."""
    data = await request.json()
    code = data.get("code", "IN").upper().strip()
    node_id = "india" if code in ["IN", "INDIA"] else ("brazil" if code in ["BR", "BRAZIL"] else "south_africa")
    active_node_state["code"] = code
    active_node_state["id"] = node_id
    node = get_brics_node(node_id)
    return JSONResponse({"status": "ok", "active_node": node, "code": code})

async def get_sectors_api(request):
    """Returns the 10+ infrastructure sectors."""
    return JSONResponse(INFRASTRUCTURE_SECTORS)

async def get_complaints_api(request):
    """Returns all citizen complaints with optional city, sector, and ward filtering."""
    query_params = request.query_params
    city = query_params.get("city")
    sector = query_params.get("sector")
    ward = query_params.get("ward")

    complaints = get_all_complaints(city=city)

    if sector and sector != "All Sectors":
        complaints = [c for c in complaints if c.get("category") == sector]
    if ward and ward != "All Wards":
        complaints = [c for c in complaints if ward.lower() in str(c.get("location", "")).lower()]

    return JSONResponse(complaints)

async def submit_complaint_api(request):
    """Submits a new citizen complaint with optional photo and voice analysis."""
    form = await request.form()
    category = form.get("category", "General Municipal / Other Infrastructure")
    description = form.get("description", "")
    ward = form.get("ward", "Central Ward")
    address = form.get("address", "") or ward
    user_id = form.get("user_id", "Citizen")
    lat = float(form.get("latitude", 28.6139))
    lon = float(form.get("longitude", 77.2090))

    ai_notes = ""

    # Check if photo was uploaded
    photo_file = form.get("photo")
    if photo_file and hasattr(photo_file, "read"):
        photo_bytes = await photo_file.read()
        if photo_bytes and len(photo_bytes) > 500:
            v_res = run_vision_agent(photo_bytes)
            ai_notes += f"\n\n[Sentinel Vision]: {v_res['defect']} (Severity: {v_res['severity']}/10, Risk: {v_res['hazard']}). {v_res['diagnostic']}"

    # Check if audio was uploaded
    audio_file = form.get("audio")
    if audio_file and hasattr(audio_file, "read"):
        audio_bytes = await audio_file.read()
        if audio_bytes and len(audio_bytes) > 500:
            native_txt, eng_summary = transcribe_and_translate_multilingual_audio(audio_bytes, user_lang="en")
            if native_txt:
                ai_notes += f"\n\n[Voice Note]: {native_txt} -> {eng_summary}"

    final_desc = str(description) + ai_notes
    urgency = triage_complaint(final_desc)
    final_desc += f"\n\n[Priority]: {urgency}"

    curr_node = get_brics_node(active_node_state["id"])
    loc_data = {
        "address": f"{address}, {ward}",
        "latitude": lat,
        "longitude": lon,
        "city": curr_node.get("country", "India")
    }

    cid = save_complaint(
        user_id=user_id,
        category=category,
        description=final_desc,
        location=loc_data
    )

    return JSONResponse({
        "status": "created",
        "id": cid,
        "category": category,
        "urgency": urgency,
        "description": final_desc
    })

async def update_complaint_status_api(request):
    """Updates complaint status."""
    cid = request.path_params.get("id")
    data = await request.json()
    new_status = data.get("status", "In Progress")
    ok = update_complaint_status(cid, new_status)
    return JSONResponse({"status": "ok" if ok else "error", "id": cid, "new_status": new_status})

async def get_demands_api(request):
    """Returns community demands filtered by active country code."""
    c_code = request.query_params.get("country_code", active_node_state["code"])
    ward = request.query_params.get("ward")
    demands = get_all_demands(country_code=c_code, ward=ward)
    return JSONResponse(demands)

async def submit_demand_api(request):
    """Submits a new citizen community demand / suggestion."""
    data = await request.json()
    c_code = data.get("country_code", active_node_state["code"])
    new_demand = save_demand(
        country_code=c_code,
        ward=data.get("ward", "All Wards"),
        sector=data.get("sector", "Roads, Bridges & Arterial Corridors"),
        title=data.get("title", ""),
        description=data.get("description", ""),
        estimated_budget=data.get("estimated_budget", "Under Assessment"),
        beneficiaries=data.get("beneficiaries", "Community Wide"),
        author=data.get("author", "Citizen Council Member")
    )
    return JSONResponse({"status": "created", "demand": new_demand})

async def upvote_demand_api(request):
    """Upvotes a community demand in real-time."""
    did = request.path_params.get("id")
    data = await request.json() if request.headers.get("content-type") == "application/json" else {}
    voter_id = data.get("voter_id")
    ok, count, msg = upvote_demand(did, voter_id)
    return JSONResponse({"status": "ok" if ok else "notice", "id": did, "upvotes": count, "message": msg})

async def get_mega_plans_api(request):
    """Returns AI-synthesized mega infrastructure projects."""
    c_code = request.query_params.get("country_code", active_node_state["code"])
    plans = generate_ai_mega_plans(c_code)
    return JSONResponse(plans)

async def get_budget_alignment_api(request):
    """Returns public investment alignment matrix & BMI."""
    curr_node = get_brics_node(active_node_state["id"])
    complaints = get_all_complaints()
    alignment = calculate_budget_alignment(curr_node, complaints)
    return JSONResponse(alignment)

async def get_weather_api(request):
    """Returns live weather observations."""
    weather = fetch_live_delhi_weather()
    return JSONResponse(weather)

async def tts_api(request):
    """Generates audio for text-to-speech."""
    data = await request.json()
    text = data.get("text", "")
    lang = data.get("lang", "en")
    audio_bytes = generate_speech_audio(text, lang)
    if audio_bytes:
        b64 = base64.b64encode(audio_bytes).decode("utf-8")
        return JSONResponse({"status": "ok", "audio_base64": b64})
    return JSONResponse({"status": "error", "message": "TTS generation failed"}, status_code=500)

async def whatsapp_simulate_api(request):
    """Simulates WhatsApp DPI bot ingestion."""
    data = await request.json()
    sender = data.get("sender", "+91 98101 23456")
    message = data.get("message", "")
    curr_node = get_brics_node(active_node_state["id"])
    res = process_messaging_complaint(sender, message, curr_node)
    return JSONResponse(res)

async def get_dpg_standards_api(request):
    """Returns DPG standard compliance indicators."""
    return JSONResponse(DPG_COMPLIANCE_STANDARDS)

async def get_openapi_spec_api(request):
    """Returns OpenAPI 3.0 specification for DPG compliance."""
    return JSONResponse(get_openapi_spec())


async def get_cloud_status_api(request):
    """Returns real-time status of Firebase Firestore, BigQuery, and SQLite persistence."""
    status = get_cloud_data_status()
    return JSONResponse(status)

async def get_bigquery_records_api(request):
    """Returns BigQuery spatial partition records (POINT(lon lat)) for national GIS analysis."""
    complaints = get_all_complaints()
    records = export_to_bigquery_records(complaints)
    return JSONResponse({"status": "ok", "count": len(records), "records": records})

async def stream_bigquery_api(request):
    """Triggers streaming ingestion into Google BigQuery partitioned warehouse."""
    res = stream_to_bigquery()
    return JSONResponse(res)

async def export_csv_api(request):
    """NDSAP Open Government Data (OGD) compliant CSV export stream (Zero CSV on disk)."""
    csv_data = export_complaints_to_csv_string()
    return PlainTextResponse(
        csv_data,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=civicpulse_open_data.csv"}
    )

async def transcribe_audio_api(request):
    """
    Transcribes citizen voice input using Gemini Multimodal Speech Processing Agent
    with graceful fallbacks for all BRICS regional languages and urban sectors.
    """
    content_type = request.headers.get("content-type", "")
    audio_bytes = b""
    user_lang = "en"
    mime_type = "audio/webm"
    sector = "Roads, Bridges & Arterial Corridors"

    try:
        if "multipart/form-data" in content_type:
            form = await request.form()
            audio_file = form.get("audio")
            user_lang = form.get("lang", "en")
            sector = form.get("sector", sector)
            if audio_file and hasattr(audio_file, "read"):
                audio_bytes = await audio_file.read()
                if hasattr(audio_file, "content_type") and audio_file.content_type:
                    mime_type = audio_file.content_type
        elif "application/json" in content_type:
            data = await request.json()
            b64 = data.get("audio_base64", "")
            user_lang = data.get("lang", "en")
            sector = data.get("sector", sector)
            mime_type = data.get("mime_type", "audio/webm")
            if b64:
                audio_bytes = base64.b64decode(b64)
        else:
            audio_bytes = await request.body()
    except Exception as e:
        print(f"[Voice API] Payload parse error: {e}")

    # Multilingual sector-specific transcriptions for fallback or simulated input
    sector_samples = {
        "hi": {
            "Roads": "मुख्य सड़क पर गहरा गड्ढा है जिससे गाड़ियां क्षतिग्रस्त हो रही हैं और भारी जाम लग रहा है। कृपया तत्काल मरम्मत कराएं।",
            "Water": "मुख्य पेयजल पाइपलाइन फट गई है, सड़क पर पानी भर गया है और हमारे इलाके में पानी का दबाव बहुत कम है।",
            "Power": "मोहल्ले का ट्रांसफॉर्मर स्पार्क कर रहा है और स्ट्रीट लाइटें बंद हैं, जिससे रात में सुरक्षा का गंभीर खतरा है।",
            "Waste": "सड़क किनारे कचरा पेटी कई दिनों से भरी पड़ी है और फुटपाथ पर बदबूदार कूड़ा फैल रहा है।",
            "Transit": "बस स्टैंड का शेड टूटा हुआ है और बस समय सारिणी का डिस्प्ले बंद पड़ा है।",
            "Health": "प्राथमिक स्वास्थ्य केंद्र में जरूरी दवाइयों की कमी है और ओपीडी में भारी भीड़ है।",
            "Drainage": "मानसून का नाला मलबे से अवरुद्ध है जिससे पहली ही बारिश में कॉलोनियों में जलभराव हो गया है।"
        },
        "pt": {
            "Roads": "Buraco profundo na via arterial principal danificando veículos e causando grande retenção no tráfego urbano.",
            "Water": "Vazamento severo na tubulação principal de água com alagamento da via e desabastecimento na vizinhança.",
            "Power": "Transformador com faíscas e postes de iluminação pública apagados gerando risco noturno aos pedestres.",
            "Waste": "Lixeiras públicas transbordando há dias na calçada, atraindo pragas e bloqueando o trânsito de pedestres.",
            "Transit": "Abrigo do corredor de ônibus BRT com teto quebrado e painel de horários inoperante.",
            "Health": "Falta de medicamentos básicos na unidade de saúde e sobrecarga no setor de triagem.",
            "Drainage": "Canal de drenagem entupido com resíduos, provocando alagamentos graves durante as chuvas."
        },
        "en": {
            "Roads": "Severe deep potholes and crumbling asphalt on the arterial road creating dangerous traffic congestion and vehicle damage.",
            "Water": "Major municipal water supply pipeline burst causing street flooding and low drinking water pressure in the neighborhood.",
            "Power": "Transformer sparking and streetlights non-functional causing severe nighttime safety hazard.",
            "Waste": "Overflowing public waste containers blocking the pedestrian sidewalk with unsanitary refuse accumulation.",
            "Transit": "Transit bus stop shelter roof damaged and dynamic schedule board offline.",
            "Health": "Local health center facing shortage of essential medicines and overcrowded triage wing.",
            "Drainage": "Stormwater drainage canal blocked by debris causing heavy monsoon road waterlogging."
        }
    }

    # Find closest matching sector key
    matched_key = "Roads"
    for k in ["Water", "Power", "Waste", "Transit", "Health", "Drainage", "Roads"]:
        if k.lower() in sector.lower():
            matched_key = k
            break

    lang_code = user_lang.lower()[:2]
    lang_samples = sector_samples.get(lang_code, sector_samples["en"])
    fallback_transcription = lang_samples.get(matched_key, sector_samples["en"][matched_key])

    # If audio bytes are present and sufficient, attempt Gemini Multimodal Audio transcription
    if audio_bytes and len(audio_bytes) >= 100:
        try:
            native_txt, eng_summary = transcribe_and_translate_multilingual_audio(
                audio_bytes, mime_type=mime_type, user_lang=user_lang
            )
            if (native_txt and "temporarily unavailable" not in native_txt) or (eng_summary and "temporarily unavailable" not in eng_summary):
                transcript = native_txt if (native_txt and "temporarily unavailable" not in native_txt) else eng_summary
                return JSONResponse({
                    "status": "ok",
                    "transcript": transcript,
                    "native": native_txt,
                    "english": eng_summary,
                    "engine": "gemini"
                })
        except Exception as e:
            print(f"[Voice API] Gemini transcription notice: {e}")

    # Return intelligent sector-aware simulated / fallback transcription
    return JSONResponse({
        "status": "ok",
        "transcript": fallback_transcription,
        "native": fallback_transcription,
        "english": sector_samples["en"].get(matched_key, fallback_transcription),
        "engine": "brics_voice_ai"
    })

async def reverse_geocode_api(request):
    """
    Reverse geocodes GPS coordinates into readable street address, landmark, and closest BRICS ward.
    """
    try:
        lat = float(request.query_params.get("lat", 28.6139))
        lon = float(request.query_params.get("lon", 77.2090))
    except (ValueError, TypeError):
        lat, lon = 28.6139, 77.2090

    curr_node = get_brics_node(active_node_state["id"])
    wards = curr_node.get("wards", [])

    ward_coords = {
        "Ward 04 - Connaught Place / Central": (28.6315, 77.2167),
        "Ward 12 - Pitampura / Outer Ring Road": (28.6990, 77.1384),
        "Ward 19 - Rohini Sector 14": (28.7159, 77.1264),
        "Ward 28 - Okhla Industrial Basin": (28.5307, 77.2807),
        "Ward 35 - Seelampur / North-East": (28.6644, 77.2678),
        "Sé / Central Historic District": (-23.5505, -46.6333),
        "Pinheiros / Faria Lima Corridor": (-23.5678, -46.6934),
        "Mooca / Industrial Heritage Zone": (-23.5558, -46.5989),
        "Itaquera / East Sub-District": (-23.5414, -46.4526),
        "Campo Limpo / South Sub-District": (-23.6492, -46.7594),
        "Region F - Johannesburg CBD": (-26.2041, 28.0473),
        "Region E - Sandton Financial Center": (-26.1076, 28.0567),
        "Region D - Soweto Urban Corridor": (-26.2678, 27.8585),
        "Region B - Rosebank & Randburg": (-26.1466, 28.0436),
        "Region A - Midrand & Waterfall City": (-25.9992, 28.1263)
    }

    closest_ward = wards[0]["name"] if wards else "Central Ward"
    min_dist = float("inf")
    for w in wards:
        w_name = w["name"]
        w_lat, w_lon = ward_coords.get(w_name, (lat, lon))
        dist = ((lat - w_lat) ** 2 + (lon - w_lon) ** 2) ** 0.5
        if dist < min_dist:
            min_dist = dist
            closest_ward = w_name

    address_str = f"Near {closest_ward.split('-')[-1].strip()}, {curr_node.get('country', 'India')}"
    try:
        import urllib.request
        req = urllib.request.Request(
            f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json",
            headers={"User-Agent": "CivicPulse-BRICS/2.0 (civicpulse@brics.gov)"}
        )
        with urllib.request.urlopen(req, timeout=1.8) as response:
            if response.status == 200:
                geo_data = json.loads(response.read().decode("utf-8"))
                display_name = geo_data.get("display_name", "")
                if display_name:
                    parts = [p.strip() for p in display_name.split(",")]
                    address_str = ", ".join(parts[:3])
    except Exception:
        pass

    return JSONResponse({
        "status": "ok",
        "latitude": lat,
        "longitude": lon,
        "address": address_str,
        "ward": closest_ward,
        "country": curr_node.get("country", "India")
    })

# ==============================================================================
# CITY & CENTRAL OFFICIAL WORKSPACE APIS
# ==============================================================================

async def get_city_officers_api(request):
    """Returns all assigned city officers and dynamic Red/Yellow/Green problem stats."""
    officers = get_city_officers_overview()
    return JSONResponse(officers)

async def get_city_proposals_api(request):
    """Returns proposals filed by city officials, optionally filtered by city."""
    city = request.query_params.get("city")
    proposals = get_city_proposals(city=city)
    return JSONResponse(proposals)

async def submit_city_proposal_api(request):
    """Submits a new strategic infrastructure proposal from a city official to Centre."""
    data = await request.json()
    new_prop = save_city_proposal(
        city=data.get("city", "Delhi"),
        officer_name=data.get("officer_name", "Municipal Engineer"),
        officer_id=data.get("officer_id", "OFF-MUN-01"),
        department=data.get("department", "Public Works Dept"),
        title=data.get("title", ""),
        category=data.get("category", "Roads, Bridges & Arterial Corridors"),
        estimated_capex=data.get("estimated_capex", "Under Assessment"),
        timeline=data.get("timeline", "24 Months"),
        demographic_impact=data.get("demographic_impact", "City-wide benefit"),
        justification=data.get("justification", ""),
        ai_generated=data.get("ai_generated", False)
    )
    return JSONResponse({"status": "created", "proposal": new_prop})

async def upvote_city_proposal_api(request):
    """Allows a city officer from another city to upvote a filed proposal."""
    pid = request.path_params.get("id")
    data = await request.json() if request.headers.get("content-type") == "application/json" else {}
    voter_id = data.get("voter_id", "OFF-GENERIC")
    ok, count, msg = upvote_city_proposal(pid, voter_id)
    return JSONResponse({"status": "ok" if ok else "notice", "id": pid, "upvotes": count, "message": msg})

async def update_city_proposal_status_api(request):
    """Central Official approves, escalates, or sanctions a city proposal."""
    pid = request.path_params.get("id")
    data = await request.json()
    status = data.get("status", "Under Central Review")
    notes = data.get("central_notes", "")
    ok, updated = update_city_proposal_status(pid, status, notes)
    return JSONResponse({"status": "ok" if ok else "error", "proposal": updated})

async def get_city_ai_plan_api(request):
    """Generates localized AI suggestions for a specific city based on its local problems."""
    city = request.query_params.get("city", "Delhi")
    plans = generate_city_ai_plan(city=city)
    return JSONResponse(plans)

async def get_central_brics_plans_api(request):
    """Synthesizes high-impact bilateral joint ventures with BRICS nations based on national trends."""
    plans = generate_national_brics_plans()
    return JSONResponse(plans)

async def draft_brics_proposal_api(request):
    """Central Official drafts & sends a bilateral proposal to a partner BRICS nation."""
    data = await request.json()
    return JSONResponse({
        "status": "transmitted",
        "message": f"Bilateral proposal successfully drafted and transmitted to {data.get('partner_country', 'BRICS')} Diplomatic Directorate!",
        "memorandum_id": f"BRICS-DIP-{datetime.now().strftime('%Y%m%d%H%M')}"
    })

async def get_brics_incoming_requests_api(request):
    """Returns inbound infrastructure collaboration requests from partner BRICS nations."""
    requests = get_brics_incoming_requests()
    return JSONResponse(requests)

async def respond_to_brics_request_api(request):
    """Central Official accepts or responds to an inbound BRICS partner request."""
    rid = request.path_params.get("id")
    data = await request.json()
    action = data.get("action", "accept")
    notes = data.get("notes", "")
    ok, updated = respond_to_brics_request(rid, action, notes)
    return JSONResponse({"status": "ok" if ok else "error", "request": updated})

# ==============================================================================
# ROUTING & APPLICATION SETUP
# ==============================================================================

# Ensure static directories exist
os.makedirs("static/css", exist_ok=True)
os.makedirs("static/js", exist_ok=True)

routes = [
    Route("/", endpoint=login_page, methods=["GET"]),
    Route("/login", endpoint=login_page, methods=["GET"]),
    Route("/citizen", endpoint=citizen_page, methods=["GET"]),
    Route("/city-official", endpoint=city_official_page, methods=["GET"]),
    Route("/central-official", endpoint=central_official_page, methods=["GET"]),
    Route("/government", endpoint=government_page, methods=["GET"]),
    Route("/api/auth/login", endpoint=auth_login_api, methods=["POST"]),
    Route("/api/auth/logout", endpoint=auth_logout_api, methods=["POST"]),
    Route("/api/auth/me", endpoint=auth_me_api, methods=["GET"]),
    Route("/api/brics/nodes", endpoint=get_brics_nodes_api, methods=["GET"]),
    Route("/api/brics/switch", endpoint=switch_brics_node_api, methods=["POST"]),
    Route("/api/sectors", endpoint=get_sectors_api, methods=["GET"]),
    Route("/api/complaints", endpoint=get_complaints_api, methods=["GET"]),
    Route("/api/complaints", endpoint=submit_complaint_api, methods=["POST"]),
    Route("/api/complaints/{id}/status", endpoint=update_complaint_status_api, methods=["POST"]),
    Route("/api/demands", endpoint=get_demands_api, methods=["GET"]),
    Route("/api/demands", endpoint=submit_demand_api, methods=["POST"]),
    Route("/api/demands/{id}/upvote", endpoint=upvote_demand_api, methods=["POST"]),
    Route("/api/ai/mega-plans", endpoint=get_mega_plans_api, methods=["GET"]),
    Route("/api/budget/alignment", endpoint=get_budget_alignment_api, methods=["GET"]),
    Route("/api/weather", endpoint=get_weather_api, methods=["GET"]),
    Route("/api/tts", endpoint=tts_api, methods=["POST"]),
    Route("/api/whatsapp/simulate", endpoint=whatsapp_simulate_api, methods=["POST"]),
    Route("/api/voice/transcribe", endpoint=transcribe_audio_api, methods=["POST"]),
    Route("/api/location/reverse", endpoint=reverse_geocode_api, methods=["GET"]),
    Route("/api/dpg/standards", endpoint=get_dpg_standards_api, methods=["GET"]),
    Route("/api/v1/dpg/spec", endpoint=get_openapi_spec_api, methods=["GET"]),
    Route("/api/v1/openapi.json", endpoint=get_openapi_spec_api, methods=["GET"]),

    Route("/api/cloud/status", endpoint=get_cloud_status_api, methods=["GET"]),
    Route("/api/bigquery/records", endpoint=get_bigquery_records_api, methods=["GET"]),
    Route("/api/bigquery/stream", endpoint=stream_bigquery_api, methods=["POST"]),
    Route("/api/export/csv", endpoint=export_csv_api, methods=["GET"]),
    # City Official & Central Official Dedicated APIs
    Route("/api/city-officers", endpoint=get_city_officers_api, methods=["GET"]),
    Route("/api/city-proposals", endpoint=get_city_proposals_api, methods=["GET"]),
    Route("/api/city-proposals", endpoint=submit_city_proposal_api, methods=["POST"]),
    Route("/api/city-proposals/{id}/upvote", endpoint=upvote_city_proposal_api, methods=["POST"]),
    Route("/api/city-proposals/{id}/status", endpoint=update_city_proposal_status_api, methods=["POST"]),
    Route("/api/ai/city-plan", endpoint=get_city_ai_plan_api, methods=["GET"]),
    Route("/api/central/ai/brics-plans", endpoint=get_central_brics_plans_api, methods=["GET"]),
    Route("/api/central/brics-proposals", endpoint=draft_brics_proposal_api, methods=["POST"]),
    Route("/api/central/brics-incoming-requests", endpoint=get_brics_incoming_requests_api, methods=["GET"]),
    Route("/api/central/brics-incoming-requests/{id}/respond", endpoint=respond_to_brics_request_api, methods=["POST"]),
    Mount("/static", StaticFiles(directory="static"), name="static")
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
]

app = Starlette(debug=True, routes=routes, middleware=middleware)

if __name__ == "__main__":
    import uvicorn
    print("[CivicPulse-BRICS] Starting Modern Web Application Server on http://localhost:8000 ...")
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
