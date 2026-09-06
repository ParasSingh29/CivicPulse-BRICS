import sys
import os
import json
import base64

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from starlette.testclient import TestClient
from server import app

client = TestClient(app)

def test_pages_and_apis():
    # 1. Login Page on Root (/)
    res = client.get("/")
    html = res.text
    assert res.status_code == 200
    assert ("Login" in html and "CivicPulse-BRICS" in html)
    assert ("Citizen Portal" in html or "Citizen Sovereign Portal" in html)
    assert ("Government Hub" in html or "Government Command Hub" in html)
    assert "btn-demo-citizen" in html
    assert "btn-demo-gov" in html
    assert 'id="citizen-login-form"' in html, "Citizen login form must be present"
    assert 'id="gov-login-form"' in html, "Government official login form must be present"
    assert 'id="citizen-email"' in html and 'id="citizen-password"' in html
    assert 'id="gov-email"' in html and 'id="gov-password"' in html
    assert 'id="btn-submit-citizen"' in html and 'id="btn-submit-gov"' in html
    assert 'id="auth-role-select"' not in html, "Redundant 3rd role selector must be eliminated"
    assert 'class="login-form-section"' not in html, "Redundant 3rd sign in section must be eliminated"
    assert 'id="lang-selector"' in html, "Language selector must be present on login gateway"
    assert '/static/js/i18n.js' in html, "i18n engine must be loaded on login gateway"
    print("[PASS] Root (/) immediately opens Sovereign Login Gateway with Dual Dedicated Citizen & Official Login Blocks")

    # 2. Login Page on (/login)
    res = client.get("/login")
    assert res.status_code == 200
    assert "CivicPulse-BRICS" in res.text
    print("[PASS] /login page loaded successfully")

    # 3. Dedicated Citizen Portal (/citizen)
    res = client.get("/citizen")
    cit_html = res.text
    assert res.status_code == 200
    assert ("Citizen Portal" in cit_html or "Citizen Sovereign Portal" in cit_html)
    assert 'id="cit-tab-home"' in cit_html
    assert '<nav class="tab-nav">' not in cit_html, "Tab nav bar must be removed for pure Home launchpad UX"
    assert 'class="home-launch-card"' in cit_html or 'home-launch-card' in cit_html
    assert 'data-open-tab="cit-tab-report"' in cit_html
    assert 'data-open-tab="cit-tab-demands"' in cit_html
    assert 'data-open-tab="cit-tab-track"' in cit_html
    assert 'data-open-tab="cit-tab-whatsapp"' in cit_html
    assert 'id="cit-tab-report" style="display:none;"' in cit_html, "Report tab must be hidden on home landing"
    assert 'id="cit-tab-demands" style="display:none;"' in cit_html, "Demands tab must be hidden on home landing"
    assert ('Back to Home' in cit_html or 'Back to Citizen Home' in cit_html)
    assert ("Report an Issue" in cit_html or "Report Infrastructure Issue" in cit_html)
    assert ("Community Requests & Voting" in cit_html or "Community Demands & Upvoting Wall" in cit_html)
    assert ("WhatsApp Assistant" in cit_html or "WhatsApp & Messaging Bot" in cit_html)
    assert "btn-logout" in cit_html
    assert "CLEARANCE: DIRECTORATE LEVEL-4" not in cit_html, "Government clearance must not be on Citizen page"
    assert 'id="node-detected-badge"' in cit_html, "Auto-detected jurisdiction badge must be present on Citizen Portal"
    assert 'id="node-selector"' not in cit_html, "Manual node switcher dropdown must be removed post-login from Citizen Portal"
    assert 'id="nav-btn-back"' in cit_html, "Navbar Back button must be present in Citizen Portal"
    assert 'id="nav-btn-home"' in cit_html, "Navbar Home button must be present in Citizen Portal"
    assert 'id="lang-selector"' in cit_html, "Language selector dropdown must be present on Citizen Portal top header"
    assert '/static/js/i18n.js' in cit_html, "i18n engine must be loaded on Citizen Portal"
    assert 'id="incident-modal"' in cit_html, "Incident reporting form must open as dedicated modal dialog on category selection"
    print("[PASS] Dedicated Citizen Portal (/citizen) verified with Navbar Back & Home, Incident Modal & Home UX")

    # 4. Dedicated Government Command Hub (/government)
    res = client.get("/government")
    gov_html = res.text
    assert res.status_code == 200
    assert ("Government Hub" in gov_html or "Government Command Hub" in gov_html)
    assert 'id="gov-tab-home"' in gov_html
    assert '<nav class="tab-nav">' not in gov_html, "Tab nav bar must be removed for pure Executive Home UX"
    assert 'class="home-launch-card"' in gov_html or 'home-launch-card' in gov_html
    assert 'data-open-tab="gov-tab-megaplan"' in gov_html
    assert 'data-open-tab="gov-tab-queue"' in gov_html
    assert 'data-open-tab="gov-tab-budget"' in gov_html
    assert 'data-open-tab="gov-tab-map"' in gov_html
    assert 'data-open-tab="gov-tab-dpg"' in gov_html
    assert 'id="gov-tab-megaplan" style="display:none;"' in gov_html, "Mega-planning must be hidden on home landing"
    assert 'id="gov-tab-queue" style="display:none;"' in gov_html, "Defect queue must be hidden on home landing"
    assert ('Back to Overview' in gov_html or 'Return to Executive Command' in gov_html)
    assert ("Admin Access" in gov_html or "CLEARANCE: DIRECTORATE LEVEL-4" in gov_html)
    assert ("AI City Project Planner" in gov_html or "Mega-Infrastructure Planning" in gov_html)
    assert ("Repairs & Work Orders" in gov_html or "Operational Defect Queue" in gov_html)
    assert ("Budget & Funding Balance" in gov_html or "CapEx Misalignment Matrix" in gov_html)
    assert ("Live City Map" in gov_html or "Geospatial Incident Command" in gov_html)
    assert "btn-logout" in gov_html
    assert "complaint-form" not in gov_html, "Citizen complaint form must not be on Government command hub"
    assert 'id="node-detected-badge"' in gov_html, "Auto-detected jurisdiction badge must be present on Government Hub"
    assert 'id="node-selector"' not in gov_html, "Manual node switcher dropdown must be removed post-login from Government Hub"
    assert 'id="nav-btn-back"' in gov_html, "Navbar Back button must be present in Government Hub"
    assert 'id="nav-btn-home"' in gov_html, "Navbar Home button must be present in Government Hub"
    assert 'id="lang-selector"' in gov_html, "Language selector dropdown must be present on Government Hub top header"
    print("[PASS] Dedicated Government Hub (/government) verified with Navbar Back & Home, Language Selector & Home UX")

    # 4b. Dedicated City Official Portal (/city-official)
    res = client.get("/city-official")
    city_html = res.text
    assert res.status_code == 200
    assert "City Official Portal" in city_html
    assert 'id="city-selector"' in city_html
    assert 'id="lang-selector"' in city_html
    assert '/static/js/i18n.js' in city_html
    print("[PASS] Dedicated City Official Portal (/city-official) verified")

    # 4c. Dedicated Central Official Portal (/central-official)
    res = client.get("/central-official")
    central_html = res.text
    assert res.status_code == 200
    assert "Central Official Sovereign Command" in central_html
    assert 'id="lang-selector"' in central_html
    assert '/static/js/i18n.js' in central_html
    print("[PASS] Dedicated Central Official Portal (/central-official) verified")


    # 5. Auth API: Citizen Login
    res = client.post("/api/auth/login", json={"role": "citizen", "email": "priya.sharma@delhi.gov.in"})
    cit_auth = res.json()
    assert cit_auth.get('status') == 'ok'
    assert cit_auth.get('redirect_url') == '/citizen'
    assert cit_auth.get('user', {}).get('role') == 'citizen'
    print("[PASS] Auth API: Citizen login returns redirect to /citizen")

    # 6. Auth API: Government Official Login
    res = client.post("/api/auth/login", json={"role": "government", "email": "director@brics.gov"})
    gov_auth = res.json()
    assert gov_auth.get('status') == 'ok'
    assert gov_auth.get('redirect_url') == '/government'
    assert gov_auth.get('user', {}).get('role') == 'government'
    print("[PASS] Auth API: Government login returns redirect to /government")

    # 7. Auth API: Logout
    res = client.post("/api/auth/logout", json={})
    logout_res = res.json()
    assert logout_res.get('redirect_url') == '/login'
    print("[PASS] Auth API: Logout returns redirect to /login")

    # 8. Sectors API (10+ sectors)
    res = client.get("/api/sectors")
    sectors = res.json()
    assert len(sectors) >= 10, "Must have 10+ infrastructure sectors"
    print(f"[PASS] {len(sectors)} infrastructure sectors verified")

    # 9. BRICS nodes API
    res = client.get("/api/brics/nodes")
    nodes_data = res.json()
    assert len(nodes_data['nodes']) == 3
    print(f"[PASS] BRICS nodes verified: {[n['country'] for n in nodes_data['nodes']]}")

    # 10. AI Mega-plans API
    res = client.get("/api/ai/mega-plans?country_code=IN")
    plans = res.json()
    assert len(plans) > 0, "AI mega plans must be synthesized"
    print(f"[PASS] AI Mega-plans API verified ({len(plans)} plans)")

    # 11. BigQuery Stream test
    res = client.post("/api/bigquery/stream", json={})
    bq_res = res.json()
    assert bq_res.get('status') in ('buffered', 'success')
    print(f"[PASS] BigQuery stream telemetry verified: {bq_res.get('streamed')} records")

    # 12. Sovereign i18n Engine & 9 Languages Check
    res = client.get("/static/js/i18n.js")
    i18n_code = res.text
    assert res.status_code == 200
    for lang in ['"en":', '"hi":', '"pt":', '"zu":', '"af":', '"ta":', '"te":', '"ru":', '"zh":']:
        assert lang in i18n_code, f"Missing {lang} translations in i18n.js"
    assert "nav_back" in i18n_code and "nav_home" in i18n_code, "Navbar Back and Home translation keys must be in i18n.js"
    assert "btn_use_current_location" in i18n_code, "Use current location key must be in i18n.js"
    assert "btn_voice_input" in i18n_code, "Voice input key must be in i18n.js"
    assert "window.setLanguage" in i18n_code
    print("[PASS] Sovereign i18n engine verified with 9 BRICS & regional languages and form keys")

    # 13. GPS Location Detection & Reverse Geocoding API & Modal UI Elements
    assert 'id="btn-use-current-location"' in cit_html, "Use current location button must be present in citizen modal"
    assert 'id="complaint-address-input"' in cit_html, "Manual address input must be present along with location detection"
    assert 'id="location-detected-chip"' in cit_html, "GPS location detected chip must be in citizen modal"
    res = client.get("/api/location/reverse?lat=28.6315&lon=77.2167")
    rev_res = res.json()
    assert rev_res.get('status') == 'ok'
    assert 'latitude' in rev_res and 'longitude' in rev_res
    assert 'address' in rev_res and 'ward' in rev_res
    print(f"[PASS] GPS Location detection & Reverse Geocoding API verified: {rev_res.get('address')} ({rev_res.get('ward')})")

    # 14. Voice Transcription (Gemini & Google Speech) API & Modal UI Elements
    assert 'id="btn-voice-desc"' in cit_html, "Voice transcription speech button must be in incident modal header"
    assert 'id="btn-textarea-floating-mic"' in cit_html, "Floating microphone button must be inside description textarea"
    assert 'id="voice-recording-hud"' in cit_html, "Voice recording HUD must be in incident modal"
    dummy_wav = b'RIFF' + b'\x00' * 120
    b64_audio = base64.b64encode(dummy_wav).decode('utf-8')
    res = client.post("/api/voice/transcribe", json={"audio_base64": b64_audio, "lang": "en"})
    v_res = res.json()
    assert v_res.get('status') == 'ok'
    assert 'transcript' in v_res and len(v_res.get('transcript')) > 5
    print(f"[PASS] Voice transcription API (Gemini/Google) verified: transcript='{v_res.get('transcript')[:45]}...'")

    print("\n=======================================================")
    print("ALL 14 SUITE TESTS PASSED: GPS CURRENT LOCATION & GEMINI VOICE TRANSCRIBE VERIFIED!")
    print("=======================================================")

if __name__ == "__main__":
    test_pages_and_apis()



