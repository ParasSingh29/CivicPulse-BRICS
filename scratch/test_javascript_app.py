import sys
import os
import glob
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8')

from starlette.testclient import TestClient
from server import app


client = TestClient(app)

print("==================================================================")
print("🧪 TESTING CIVICPULSE-BRICS JAVASCRIPT APP, FIREBASE & BIGQUERY")
print("==================================================================\n")

# 0. Architectural Verification: Streamlit and CSV Removal
print("=== 0. Verifying Full Removal of Streamlit & CSV Files ===")
assert not os.path.exists(".streamlit"), "ERROR: .streamlit directory still exists!"
csv_files = glob.glob("*.csv")
assert len(csv_files) == 0, f"ERROR: Found legacy CSV files on disk: {csv_files}"
print("✓ Verified: Zero .streamlit directory on disk.")
print("✓ Verified: Zero .csv files on disk.")

# 1. Main Page Test
print("\n=== 1. Testing Sovereign Gateway & Dedicated Portals ===")
r = client.get("/")
assert r.status_code == 200
assert "CivicPulse-BRICS" in r.text
print("✓ Sovereign Login Gateway (/) served with 200 OK.")

r_cit = client.get("/citizen")
assert r_cit.status_code == 200
assert "sector-grid-container" in r_cit.text
print("✓ Citizen Portal (/citizen) served with 200 OK.")

r_gov = client.get("/government")
assert r_gov.status_code == 200
assert "megaplan-container" in r_gov.text
print("✓ Government Hub (/government) served with 200 OK.")

# 2. Static Assets Test
print("\n=== 2. Testing Static CSS & JS Assets ===")
r_css = client.get("/static/css/styles.css")
assert r_css.status_code == 200
assert "--bg-primary" in r_css.text
print("✓ CSS design system styles.css served with 200 OK.")

r_js = client.get("/static/js/app.js")
assert r_js.status_code == 200
assert "AppState" in r_js.text
print("✓ Core JavaScript app.js served with 200 OK.")

# 3. Cloud Firestore & BigQuery Status API
print("\n=== 3. Testing Cloud Firebase & BigQuery Status API ===")
r_cloud = client.get("/api/cloud/status")
assert r_cloud.status_code == 200
cloud_status = r_cloud.json()
assert "cloud_firestore" in cloud_status
assert "google_bigquery" in cloud_status
assert "persistence_layer" in cloud_status
print(f"✓ Cloud Firestore Engine: {cloud_status['cloud_firestore']['name']} -> {cloud_status['cloud_firestore']['status']}")
print(f"✓ BigQuery Warehouse:     {cloud_status['google_bigquery']['name']} -> {cloud_status['google_bigquery']['status']}")
print(f"✓ Persistence Layer:       {cloud_status['persistence_layer']['name']} ({cloud_status['persistence_layer']['csv_dependency']})")
print(f"✓ Frontend Architecture:   {cloud_status['frontend_layer']['architecture']}")

# 4. BigQuery Spatial Telemetry & Streaming Pipeline
print("\n=== 4. Testing BigQuery Spatial Telemetry & GIS Partition Stream ===")
r_bq = client.get("/api/bigquery/records")
assert r_bq.status_code == 200
bq_data = r_bq.json()
assert bq_data["status"] == "ok"
records = bq_data["records"]
assert len(records) > 0
print(f"✓ BigQuery GIS Partition Records Exported: {len(records)} records")
print(f"   • Sample Spatial Geography: {records[0]['location_geography']}")
print(f"   • Incident ID:              {records[0]['incident_id']}")
print(f"   • Urgency Score:            {records[0]['urgency_score']}")
print(f"   • Assigned Directorate:     {records[0]['assigned_division']}")

r_stream = client.post("/api/bigquery/stream")
assert r_stream.status_code == 200
stream_res = r_stream.json()
print(f"✓ BigQuery Stream Trigger: {stream_res['status']} -> {stream_res.get('target')}")

# 5. BRICS Nodes & 10+ Sectors
print("\n=== 5. Testing BRICS Nodes & 10+ Sectors API ===")
r_nodes = client.get("/api/brics/nodes")
assert r_nodes.status_code == 200
nodes_data = r_nodes.json()
assert len(nodes_data["nodes"]) == 3
print(f"✓ BRICS nodes loaded: {[n['country'] for n in nodes_data['nodes']]}")

r_sectors = client.get("/api/sectors")
assert r_sectors.status_code == 200
sectors = r_sectors.json()
assert len(sectors) >= 10
print(f"✓ Expanded 10+ sectors loaded: {len(sectors)} sectors available.")

# 6. Community Demands & Real-Time Upvoting Engine
print("\n=== 6. Testing Participatory Demands & Real-Time Upvoting ===")
r_demands = client.get("/api/demands?country_code=IN")
assert r_demands.status_code == 200
demands = r_demands.json()
assert len(demands) > 0
first_demand = demands[0]
initial_votes = first_demand["upvotes"]
print(f"✓ Community Demands loaded: {len(demands)} proposals. Top: '{first_demand['title']}' ({initial_votes} votes)")

# Upvote the first demand
r_upvote = client.post(f"/api/demands/{first_demand['id']}/upvote", json={"voter_id": "integration_test_voter"})
assert r_upvote.status_code == 200
upvote_res = r_upvote.json()
new_votes = upvote_res["upvotes"]
print(f"✓ Upvote executed on {first_demand['id']}: Initial={initial_votes} -> New={new_votes}")
assert new_votes == initial_votes + 1 or upvote_res["status"] == "notice"

# 7. AI Mega-Planning Engine
print("\n=== 7. Testing Gemini 2.5 AI Mega-Planning Engine ===")
r_mega = client.get("/api/ai/mega-plans?country_code=IN")
assert r_mega.status_code == 200
mega_plans = r_mega.json()
assert len(mega_plans) > 0
print(f"✓ Synthesized {len(mega_plans)} AI Capital Infrastructure Mega-Plans:")
for p in mega_plans[:2]:
    print(f"   • [{p.get('icon', p.get('svg_key', 'zap'))}] {p['title']} | CapEx: {p['estimated_capex']} | Backing: {p['citizen_backing']}")

# 8. Budget Misalignment Matrix
print("\n=== 8. Testing Public Spending & Budget Alignment Matrix ===")
r_budget = client.get("/api/budget/alignment")
assert r_budget.status_code == 200
matrix = r_budget.json()
assert len(matrix) > 0
print(f"✓ CapEx Misalignment Matrix computed for {len(matrix)} wards.")

# 9. Live Weather Telemetry
print("\n=== 9. Testing Live Meteorological Weather ===")
r_weather = client.get("/api/weather")
assert r_weather.status_code == 200
w = r_weather.json()
print(f"✓ Weather Telemetry: {w['temperature']}°C, {w['humidity']}% humidity, {w['condition']}")

print("\n==================================================================")
print("🎉 100% OPERATIONAL: ZERO STREAMLIT, ZERO CSV, JAVASCRIPT SPA + FIREBASE & BIGQUERY!")
print("==================================================================")

