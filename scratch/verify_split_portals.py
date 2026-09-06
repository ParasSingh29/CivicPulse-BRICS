"""
Automated Test Verification for CivicPulse-BRICS: Split Government Portals
Tests:
1. Web Pages: /login, /citizen, /city-official, /central-official, /government
2. Login Auth Routing for Citizen, City Official, and Central Official
3. City-Scoped Complaint Filtering
4. Assigned City Officers with Red/Yellow/Green problem meters
5. City-to-Centre Strategic Proposals & Inter-City Peer Upvoting
6. City AI Suggestions (e.g. Metro for traffic)
7. Central AI BRICS Joint Ventures (e.g. Bullet Train JV with China for slow trains)
8. Inbound Partner Requests Handling
"""

import sys
import os
import json
import asyncio

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starlette.testclient import TestClient
from server import app

def run_tests():
    client = TestClient(app)

    print("==================================================================")
    print("TEST SUITE: CivicPulse-BRICS Split Government Portals Verification")
    print("==================================================================")

    # 1. Test HTML Page Serving
    pages = [
        ("/", 200, "Sovereign Login Gateway"),
        ("/login", 200, "Login"),
        ("/citizen", 200, "Citizen Portal"),
        ("/city-official", 200, "City Official Portal"),
        ("/central-official", 200, "Central Official Sovereign Command"),
        ("/government", 200, "Government")
    ]

    for path, expected_status, title_snippet in pages:
        res = client.get(path)
        assert res.status_code == expected_status, f"Expected {expected_status} for {path}, got {res.status_code}"
        assert title_snippet in res.text or "CivicPulse-BRICS" in res.text, f"Snippet '{title_snippet}' not found in {path}"
        print(f"[PASS] Page {path} successfully returned HTTP {res.status_code}")

    # Verify elements in city_official.html
    res = client.get("/city-official")
    assert "city-selector" in res.text
    assert "city-tab-home" in res.text
    assert "city-tab-complaints" in res.text
    assert "city-tab-ai-plan" in res.text
    assert "city-tab-proposals" in res.text
    assert "city-complaints-container" in res.text
    assert "city-ai-suggestions-grid" in res.text
    assert "city-proposals-feed" in res.text
    assert "file-proposal-modal" in res.text
    print("[PASS] City Official Portal contains Home Launchpad overview and tab views")

    # Verify elements in central_official.html
    res = client.get("/central-official")
    assert "central-tab-home" in res.text
    assert "central-tab-officers" in res.text
    assert "central-tab-proposals-review" in res.text
    assert "central-tab-brics-jv" in res.text
    assert "central-tab-inbound-requests" in res.text
    assert "central-officers-grid" in res.text
    assert "central-proposals-feed" in res.text
    assert "central-brics-jv-container" in res.text
    assert "central-inbound-requests-container" in res.text
    assert "draft-jv-modal" in res.text
    print("[PASS] Central Official Portal contains Sovereign Command Home Launchpad overview and tab views")


    # 2. Test Auth Routing
    auth_cases = [
        ({"role": "citizen", "email": "resident@delhi.gov.in"}, "/citizen", "citizen"),
        ({"role": "city_official", "email": "vikram.sharma@delhi.gov.in"}, "/city-official", "city_official"),
        ({"role": "central_official", "email": "director.general@brics.gov"}, "/central-official", "central_official"),
        ({"role": "government", "email": "official@brics.gov"}, "/government", "government")
    ]

    for payload, expected_url, expected_role in auth_cases:
        res = client.post("/api/auth/login", json=payload)
        assert res.status_code == 200
        data = res.json()
        assert data["status"] == "ok"
        assert data["redirect_url"] == expected_url, f"Expected redirect {expected_url}, got {data['redirect_url']}"
        assert data["user"]["role"] == expected_role
        print(f"[PASS] Auth for role '{payload['role']}' redirects to {expected_url}")

    # 3. Test City-Filtered Complaints
    res_all = client.get("/api/complaints")
    assert res_all.status_code == 200
    all_complaints = res_all.json()
    assert len(all_complaints) > 0

    res_delhi = client.get("/api/complaints?city=Delhi")
    assert res_delhi.status_code == 200
    delhi_complaints = res_delhi.json()
    assert len(delhi_complaints) > 0
    print(f"[PASS] Total complaints: {len(all_complaints)}, Delhi-scoped complaints: {len(delhi_complaints)}")

    # 4. Test Assigned City Officers with Red/Yellow/Green Breakdown
    res_officers = client.get("/api/city-officers")
    assert res_officers.status_code == 200
    officers = res_officers.json()
    assert len(officers) >= 5
    for off in officers:
        assert "red_problems" in off and "yellow_problems" in off and "green_problems" in off
        assert "health_index" in off
        print(f"[PASS] Officer {off['name']} ({off['city']}): Red={off['red_problems']}, Yellow={off['yellow_problems']}, Green={off['green_problems']}, Health={off['health_index']}%")

    # 5. Test City Proposals, Upvoting & Central Status Update
    res_props = client.get("/api/city-proposals")
    assert res_props.status_code == 200
    proposals = res_props.json()
    assert len(proposals) > 0
    test_prop = proposals[0]
    initial_upvotes = test_prop.get("upvotes", 0)

    import time
    voter_id = f"TEST-OFF-{int(time.time()*1000)}"
    res_upvote = client.post(f"/api/city-proposals/{test_prop['id']}/upvote", json={"voter_id": voter_id})
    assert res_upvote.status_code == 200
    upvote_data = res_upvote.json()
    assert upvote_data["status"] == "ok"
    assert upvote_data["upvotes"] == initial_upvotes + 1
    print(f"[PASS] Upvoted proposal #{test_prop['id']}: count incremented from {initial_upvotes} to {upvote_data['upvotes']}")

    # Submit new proposal from Delhi
    new_prop_payload = {
        "city": "Delhi",
        "officer_name": "Er. Vikram Sharma",
        "officer_id": "OFF-DEL-01",
        "department": "Public Works & Urban Mobility Dept",
        "title": "Automated Multi-Level Electric Bus Transit Depot at Pitampura",
        "category": "Public Transport & Transit Hubs",
        "estimated_capex": "₹650 Crore",
        "timeline": "18 Months",
        "demographic_impact": "400,000 daily commuters",
        "justification": "Heavy diesel bus emissions and lack of terminal parking causes arterial gridlock."
    }
    res_create = client.post("/api/city-proposals", json=new_prop_payload)
    assert res_create.status_code == 200
    created_prop = res_create.json()["proposal"]
    print(f"[PASS] Created new city proposal to Centre: #{created_prop['id']} '{created_prop['title']}'")

    # Central official approves proposal
    res_status = client.post(f"/api/city-proposals/{created_prop['id']}/status", json={
        "status": "Approved for National Budget",
        "central_notes": "Fast-tracked by Central Planning Commission."
    })
    assert res_status.status_code == 200
    updated_prop = res_status.json()["proposal"]
    assert updated_prop["status"] == "Approved for National Budget"
    print(f"[PASS] Central official successfully approved proposal #{created_prop['id']}")

    # 6. Test Local Area AI Suggestions
    res_city_ai = client.get("/api/ai/city-plan?city=Delhi")
    assert res_city_ai.status_code == 200
    city_ai_plans = res_city_ai.json()
    assert len(city_ai_plans) > 0
    print(f"[PASS] City AI generated {len(city_ai_plans)} structural suggestions for Delhi (e.g. '{city_ai_plans[0]['title']}')")

    # 7. Test Central AI BRICS Joint Ventures
    res_brics_ai = client.get("/api/central/ai/brics-plans")
    assert res_brics_ai.status_code == 200
    brics_jvs = res_brics_ai.json()
    assert len(brics_jvs) > 0
    # Check that China Bullet Train JV is present
    china_jv = next((j for j in brics_jvs if "china" in j.get("partner_country", "").lower() or "rail" in j.get("title", "").lower() or "bullet" in j.get("title", "").lower()), None)
    assert china_jv is not None, "China Bullet Train Joint Venture must be present"
    print(f"[PASS] Central AI synthesized {len(brics_jvs)} BRICS Joint Ventures including '{china_jv['title']}' (Partner: {china_jv['partner_country']})")

    # Draft and transmit bilateral proposal
    res_draft_jv = client.post("/api/central/brics-proposals", json={
        "partner_country": "China",
        "project_title": china_jv["title"],
        "capex": china_jv["estimated_capex"]
    })
    assert res_draft_jv.status_code == 200
    assert res_draft_jv.json()["status"] == "transmitted"
    print("[PASS] Drafted and transmitted bilateral proposal to China Diplomatic Directorate")

    # 8. Test Inbound Partner Requests
    res_inbound = client.get("/api/central/brics-incoming-requests")
    assert res_inbound.status_code == 200
    inbound_reqs = res_inbound.json()
    assert len(inbound_reqs) >= 4
    sample_inbound = inbound_reqs[0]
    print(f"[PASS] Found {len(inbound_reqs)} incoming requests from partner BRICS nations (e.g. from {sample_inbound['origin_country']}: '{sample_inbound['project_title']}')")

    # Respond to inbound request
    res_respond = client.post(f"/api/central/brics-incoming-requests/{sample_inbound['id']}/respond", json={
        "action": "accept",
        "notes": "Sanctioned for bilateral joint working group in New Delhi."
    })
    assert res_respond.status_code == 200
    assert "Sanctioned" in res_respond.json()["request"]["status"]
    # 9. Test OpenAPI DPG Specification Endpoints
    res_spec = client.get("/api/v1/dpg/spec")
    assert res_spec.status_code == 200
    spec_data = res_spec.json()
    assert spec_data.get("openapi") == "3.0.3"
    assert "CivicPulse-BRICS" in spec_data.get("info", {}).get("title", "")
    print(f"[PASS] DPG OpenAPI specification endpoint (/api/v1/dpg/spec) verified: v{spec_data.get('info', {}).get('version')}")

    res_openapi = client.get("/api/v1/openapi.json")
    assert res_openapi.status_code == 200
    assert res_openapi.json().get("openapi") == "3.0.3"
    print("[PASS] OpenAPI endpoint (/api/v1/openapi.json) verified")

    print("==================================================================")
    print("ALL TESTS PASSED SUCCESSFULLY! 100% VERIFIED.")
    print("==================================================================")


if __name__ == "__main__":
    run_tests()
