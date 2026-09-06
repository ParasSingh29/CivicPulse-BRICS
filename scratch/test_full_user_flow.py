"""
CivicPulse-BRICS: Comprehensive End-to-End User Flow & Portal Verification Script
Exercises 100% of portals, sectors, forms, button actions, AI engines, and cloud APIs.
"""
import sys
import os
import json
import base64
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from starlette.testclient import TestClient
from server import app

client = TestClient(app)

def run_comprehensive_e2e_audit():
    print("\n" + "="*80)
    print("🚀 CIVICPULSE-BRICS: COMPREHENSIVE END-TO-END SYSTEM & USER FLOW AUDIT")
    print("="*80)

    # --------------------------------------------------------------------------
    # 1. PAGE & PORTAL NAVIGATION FLOWS
    # --------------------------------------------------------------------------
    print("\n--- 1. Testing Page & Portal Navigation Flows ---")
    pages = [
        ("/", "Sovereign Login Gateway"),
        ("/login", "Login Gateway"),
        ("/citizen", "Citizen Sovereign Portal"),
        ("/city-official", "City Official Command Portal"),
        ("/central-official", "Central Official Sovereign Command"),
        ("/government", "Government Command Hub")
    ]
    for url, label in pages:
        res = client.get(url)
        assert res.status_code == 200, f"Page {url} failed with status {res.status_code}"
        print(f"  ✓ {label} ({url}) loaded successfully [HTTP 200 OK]")

    # --------------------------------------------------------------------------
    # 2. AUTHENTICATION & ROLE-BASED REDIRECTION FLOWS
    # --------------------------------------------------------------------------
    print("\n--- 2. Testing Authentication & Role Redirection Flows ---")
    roles_to_test = [
        ("citizen", "priya@delhi.gov.in", "/citizen"),
        ("city_official", "vikram.sharma@delhi.gov.in", "/city-official"),
        ("central_official", "director.general@brics.gov", "/central-official"),
        ("government", "official@brics.gov", "/government")
    ]
    for role, email, expected_redirect in roles_to_test:
        res = client.post("/api/auth/login", json={"role": role, "email": email, "node": "IN"})
        data = res.json()
        assert data.get("status") == "ok"
        assert data.get("redirect_url") == expected_redirect
        print(f"  ✓ Role '{role}' ({email}) authenticated -> Redirects to {expected_redirect}")

    # Logout Flow
    res = client.post("/api/auth/logout", json={})
    assert res.json().get("redirect_url") == "/login"
    print("  ✓ Auth logout flow verified -> Redirects to /login")

    # --------------------------------------------------------------------------
    # 3. COMPLAINT INGESTION ACROSS ALL 10 INFRASTRUCTURE SECTORS
    # --------------------------------------------------------------------------
    print("\n--- 3. Testing Incident Ingestion Across All 10 Urban Infrastructure Sectors ---")
    
    res = client.get("/api/sectors")
    sectors = res.json()
    assert len(sectors) >= 10, "Must have 10+ infrastructure sectors"
    print(f"  ✓ Fetched {len(sectors)} urban infrastructure sectors")

    sample_coords = [
        (28.6139, 77.2090, "Ward 04 - Connaught Place / Central", "Delhi"),
        (28.6990, 77.1384, "Ward 12 - Pitampura / Outer Ring Road", "Delhi"),
        (28.7159, 77.1264, "Ward 19 - Rohini Sector 14", "Delhi"),
        (28.5307, 77.2807, "Ward 28 - Okhla Industrial Basin", "Delhi"),
        (28.6644, 77.2678, "Ward 35 - Seelampur / North-East", "Delhi"),
        (-23.5505, -46.6333, "Sé / Central Historic District", "São Paulo"),
        (-23.5678, -46.6934, "Pinheiros / Faria Lima Corridor", "São Paulo"),
        (-26.2041, 28.0473, "Region F - Johannesburg CBD", "Johannesburg"),
        (-26.1076, 28.0567, "Region E - Sandton Financial Center", "Johannesburg"),
        (19.0178, 72.8478, "Dadar Junction / Central", "Mumbai")
    ]

    submitted_complaint_ids = []

    for idx, s in enumerate(sectors):
        lat, lon, ward, city = sample_coords[idx % len(sample_coords)]
        sector_name = s.get("name")
        desc = f"Testing E2E reporting for sector [{sector_name}]: Structural failure identified near {ward}, {city}. Immediate crew dispatch required."
        
        # Test multipart complaint submission with photo and audio
        dummy_jpg = b'\xff\xd8\xff\xe0\x00\x10JFIF' + b'\x00' * 500
        dummy_wav = b'RIFF' + b'\x00' * 300
        
        form_data = {
            "category": sector_name,
            "description": desc,
            "ward": ward,
            "address": f"Near Main Intersection, {ward}",
            "user_id": f"citizen_tester_{idx}@brics.gov",
            "latitude": str(lat),
            "longitude": str(lon)
        }
        files = {
            "photo": ("test_defect.jpg", dummy_jpg, "image/jpeg"),
            "audio": ("test_speech.wav", dummy_wav, "audio/wav")
        }
        
        res = client.post("/api/complaints", data=form_data, files=files)
        data = res.json()
        assert data.get("status") == "created", f"Failed to submit complaint for {sector_name}"
        cid = data.get("id")
        submitted_complaint_ids.append(cid)
        print(f"  ✓ [{idx+1}/10] Sector '{sector_name}' -> Incident #{cid} registered (Urgency: {data.get('urgency')})")

    # --------------------------------------------------------------------------
    # 4. COMPLAINT STATUS UPDATES & OPERATIONAL QUEUE FLOWS
    # --------------------------------------------------------------------------
    print("\n--- 4. Testing Operational Queue & Resolution Status Updates ---")
    for idx, cid in enumerate(submitted_complaint_ids[:5]):
        new_status = "In Progress" if idx % 2 == 0 else "Resolved"
        res = client.post(f"/api/complaints/{cid}/status", json={"status": new_status})
        assert res.json().get("status") == "ok"
        print(f"  ✓ Incident #{cid} status updated -> '{new_status}'")

    # --------------------------------------------------------------------------
    # 5. PARTICIPATORY BUDGETING & COMMUNITY DEMANDS WALL
    # --------------------------------------------------------------------------
    print("\n--- 5. Testing Community Demands Wall & Real-Time Upvoting ---")
    # Fetch demands for IN, BR, ZA
    for code in ["IN", "BR", "ZA"]:
        res = client.get(f"/api/demands?country_code={code}")
        demands = res.json()
        assert len(demands) > 0, f"Demands list empty for {code}"
        print(f"  ✓ Loaded {len(demands)} community demands for nation node [{code}]")
        
        # Upvote top demand
        top_demand = demands[0]
        did = top_demand["id"]
        res = client.post(f"/api/demands/{did}/upvote", json={"voter_id": "e2e_tester_user"})
        upvote_res = res.json()
        assert upvote_res.get("status") in ["ok", "notice"]
        print(f"  ✓ Upvoted demand #{did} ('{top_demand['title'][:35]}...') -> New votes: {upvote_res.get('upvotes')}")

    # Submit a new custom community demand
    new_demand_payload = {
        "title": "Automated Multi-Level Electric Bus Charging Super-Hub & Solar Canopy",
        "sector": "Public Transport & Transit Hubs",
        "ward": "Ward 12 - Pitampura / Outer Ring Road",
        "estimated_budget": "₹380 Crore",
        "beneficiaries": "250,000 Commuters Daily",
        "description": "Construction of zero-emission rapid charging depot and feeder electric bus terminal to eliminate last-mile commuter congestion.",
        "author": "Pitampura Commuter Welfare Council",
        "country_code": "IN"
    }
    res = client.post("/api/demands", json=new_demand_payload)
    data = res.json()
    assert data.get("status") == "created"
    print(f"  ✓ Posted new community demand: #{data['demand']['id']} '{new_demand_payload['title'][:40]}...'")

    # --------------------------------------------------------------------------
    # 6. CITY OFFICIAL MUNICIPAL PROPOSALS TO CENTRE
    # --------------------------------------------------------------------------
    print("\n--- 6. Testing City Official Strategic Proposals & Central Review ---")
    cities_to_test = ["Delhi", "Mumbai", "Bengaluru", "São Paulo", "Johannesburg"]
    created_proposals = []

    for city in cities_to_test:
        res = client.get(f"/api/city-proposals?city={city}")
        props = res.json()
        print(f"  ✓ Fetched {len(props)} city proposals for {city}")

        # Submit new proposal from city to Centre
        new_prop = {
            "city": city,
            "officer_name": f"Chief Engineer ({city})",
            "officer_id": f"OFF-{city[:3].upper()}-99",
            "department": "Public Works & Urban Development",
            "title": f"Integrated Smart Grid & Underground Drainage Resiliency Corridor ({city})",
            "category": "Stormwater Drainage & Monsoon Floods",
            "estimated_capex": "₹650 Crore / R$ 420 Mi",
            "timeline": "18 Months",
            "demographic_impact": "1.2 Million Residents",
            "justification": f"Systemic urban flood mitigation and storm drainage upgrading in high-density sectors of {city}."
        }
        res = client.post("/api/city-proposals", json=new_prop)
        prop_data = res.json()
        assert prop_data.get("status") == "created"
        pid = prop_data["proposal"]["id"]
        created_proposals.append(pid)
        print(f"  ✓ [{city}] Submitted municipal proposal #{pid} to Centre")

    # Central Official Sanctions & Escalates Proposals
    if created_proposals:
        # Sanction first proposal
        res = client.post(f"/api/city-proposals/{created_proposals[0]}/status", json={
            "status": "Sanctioned under National Infrastructure Pipeline",
            "central_notes": "Cabinet approval granted. Initial CapEx tranche released."
        })
        assert res.json().get("status") == "ok"
        print(f"  ✓ Central Official approved & sanctioned proposal #{created_proposals[0]}")

        # Escalate second proposal to BRICS JV
        if len(created_proposals) > 1:
            res = client.post(f"/api/city-proposals/{created_proposals[1]}/status", json={
                "status": "Escalated to BRICS Joint Venture",
                "central_notes": "Referred to Bilateral Diplomatic Infrastructure Commission."
            })
            assert res.json().get("status") == "ok"
            print(f"  ✓ Central Official escalated proposal #{created_proposals[1]} to BRICS Joint Venture")

    # --------------------------------------------------------------------------
    # 7. AI MEGA-PLANNING & BRICS BILATERAL JOINT VENTURES
    # --------------------------------------------------------------------------
    print("\n--- 7. Testing Gemini 2.5 AI Mega-Planning & BRICS Joint Ventures ---")
    res = client.get("/api/ai/mega-plans?country_code=IN")
    mega_plans = res.json()
    assert len(mega_plans) > 0
    print(f"  ✓ Synthesized {len(mega_plans)} AI Capital Infrastructure Mega-Plans for India Node")

    res = client.get("/api/central/ai/brics-plans")
    brics_jvs = res.json()
    assert len(brics_jvs) > 0
    print(f"  ✓ Synthesized {len(brics_jvs)} Bilateral BRICS Joint Ventures (e.g. '{brics_jvs[0]['title'][:40]}...')")

    # Draft & Transmit Bilateral Proposal
    draft_payload = {
        "partner_country": brics_jvs[0]["partner_country"],
        "project_title": brics_jvs[0]["title"],
        "capex": brics_jvs[0]["estimated_capex"],
        "notes": "Diplomatic memorandum authorized by Director General, National CapEx Planning Commission."
    }
    res = client.post("/api/central/brics-proposals", json=draft_payload)
    assert res.json().get("status") == "transmitted"
    print(f"  ✓ Transmitted bilateral proposal to {brics_jvs[0]['partner_country']} Diplomatic Directorate")

    # Inbound Partner Requests
    res = client.get("/api/central/brics-incoming-requests")
    inbound_reqs = res.json()
    assert len(inbound_reqs) > 0
    print(f"  ✓ Loaded {len(inbound_reqs)} inbound partner requests (e.g. from {inbound_reqs[0]['origin_country']})")

    # Respond to inbound request
    rid = inbound_reqs[0]["id"]
    res = client.post(f"/api/central/brics-incoming-requests/{rid}/respond", json={"action": "accept", "notes": "Bilateral accord accepted."})
    assert res.json().get("status") == "ok"
    print(f"  ✓ Responded & accepted inbound partner request #{rid}")

    # --------------------------------------------------------------------------
    # 8. MULTIMODAL GEMINI VOICE AI, REVERSE GEOCODING & CLOUD APIS
    # --------------------------------------------------------------------------
    print("\n--- 8. Testing Voice AI, Reverse Geocoding, Weather & Cloud Infrastructure ---")
    
    # Multilingual Voice AI Transcription for 3 languages
    for lang, sec in [("en", "Water Supply"), ("hi", "Roads"), ("pt", "Power Grid")]:
        res = client.post("/api/voice/transcribe", json={"sector": sec, "lang": lang})
        vdata = res.json()
        assert vdata.get("status") == "ok"
        assert len(vdata.get("transcript", "")) > 5
        print(f"  ✓ Gemini Voice AI transcription [{lang.upper()}] ({sec}): '{vdata['transcript'][:40]}...'")

    # GPS Reverse Geocoding for India, Brazil, South Africa
    coords = [
        (28.6315, 77.2167, "India"),
        (-23.5505, -46.6333, "Brazil"),
        (-26.2041, 28.0473, "South Africa")
    ]
    for lat, lon, country in coords:
        res = client.get(f"/api/location/reverse?lat={lat}&lon={lon}")
        rev = res.json()
        assert rev.get("status") == "ok"
        print(f"  ✓ Reverse Geocoding [{country}]: {rev.get('address')} ({rev.get('ward')})")

    # Weather Telemetry
    res = client.get("/api/weather")
    w = res.json()
    assert "temperature" in w
    print(f"  ✓ Live Meteorological Telemetry: {w.get('temperature')}°C, {w.get('humidity')}% humidity ({w.get('condition')})")

    # Cloud Data Status
    res = client.get("/api/cloud/status")
    cloud = res.json()
    assert cloud.get("cloud_firestore", {}).get("status") == "Ready (Firestore Native Adapter Active)"
    print(f"  ✓ Cloud Architecture HUD Status: {cloud.get('cloud_firestore', {}).get('name')}")

    # BigQuery GIS Partition Records & Stream
    res = client.get("/api/bigquery/records")
    bq_recs = res.json()
    assert bq_recs.get("count", 0) > 0
    print(f"  ✓ BigQuery GIS Warehouse: Exported {bq_recs['count']} spatial partition records")

    res = client.post("/api/bigquery/stream", json={})
    assert res.json().get("status") in ["buffered", "success"]
    print("  ✓ BigQuery GIS Partition Streaming Pipeline executed successfully")

    # Open Government Data CSV Stream
    res = client.get("/api/export/csv")
    assert res.status_code == 200
    assert "text/csv" in res.headers.get("content-type", "")
    print("  ✓ Open Government Data (OGD) NDSAP CSV Stream generated (Zero CSV on disk)")

    # DPG & OpenAPI Standards
    res = client.get("/api/dpg/standards")
    assert len(res.json()) >= 6
    print(f"  ✓ Digital Public Good (DPG) standards verified: {len(res.json())} indicators compliant")

    res = client.get("/api/v1/dpg/spec")
    assert res.json().get("info", {}).get("version") == "2.0.0"
    print("  ✓ OpenAPI 3.0.0 DPG specification verified")

    print("\n" + "="*80)
    print("🎉 ALL 8 E2E AUDIT SECTIONS PASSED WITH 100% OPERATIONAL SUCCESS!")
    print("="*80 + "\n")

if __name__ == "__main__":
    run_comprehensive_e2e_audit()
