"""
CIVICPULSE-BRICS: Realistic Seed Data Script
Adds 40 diverse, realistic complaints across BRICS cities and all sectors.
"""
import sqlite3
import json
import uuid
from datetime import datetime, timedelta
import random

DB_PATH = 'data/civicpulse.db'

# ─── Realistic Complaints Dataset ───────────────────────────────────────────
COMPLAINTS = [
    # ── INDIA (Delhi NCR) ───────────────────────────────────────────────────
    {
        "category": "Roads, Bridges & Arterial Corridors",
        "description": "Large pothole on NH-48 near Dhaula Kuan flyover causing accidents. Two-wheelers have already skidded. Road surface completely degraded after monsoon. | Priority: High - Active road hazard on national highway causing accidents. | Severity: 8/10",
        "location": {"address": "NH-48, Dhaula Kuan, New Delhi", "latitude": 28.5918, "longitude": 77.1696, "city": "New Delhi"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 3,
        "user": "resident.delhi@gmail.com"
    },
    {
        "category": "Water Supply",
        "description": "No water supply for 5 days in Sector 14, Rohini. Tanker is not arriving on scheduled days. Families with elderly and children severely affected. | Priority: High - Essential service failure for 5+ days. | Severity: 9/10",
        "location": {"address": "Sector 14, Rohini, New Delhi", "latitude": 28.7196, "longitude": 77.1138, "city": "New Delhi"},
        "status": "In Progress",
        "photo_url": None,
        "days_ago": 5,
        "user": "mohit.kumar@delhi.in"
    },
    {
        "category": "Electricity & Power Grid",
        "description": "Transformer exploded near B-Block, Lajpat Nagar last night. Power outage across 3 colonies. Live wires hanging on the street near the transformer pole. | Priority: Critical - Live exposed wires are immediate safety hazard. | Severity: 10/10",
        "location": {"address": "B-Block, Lajpat Nagar, New Delhi", "latitude": 28.5686, "longitude": 77.2437, "city": "New Delhi"},
        "status": "In Progress",
        "photo_url": None,
        "days_ago": 1,
        "user": "lajpat.resident@ndmc.gov"
    },
    {
        "category": "Drainage & Flood Management",
        "description": "Storm drain completely blocked on Ring Road near ITO. Even light rain causes 4-foot flooding on the main road, blocking traffic for hours. | Priority: High - Regular flooding on arterial road. | Severity: 7/10",
        "location": {"address": "Ring Road near ITO, New Delhi", "latitude": 28.6274, "longitude": 77.2413, "city": "New Delhi"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 8,
        "user": "citizen@delhi.gov.in"
    },
    {
        "category": "Waste Management & Sanitation",
        "description": "Garbage not collected for 12 days in Mayur Vihar Phase 2. Garbage pile near E-4 park has become a health hazard. Stray animals spreading waste across the street. | Priority: High - Public health risk. | Severity: 8/10",
        "location": {"address": "Mayur Vihar Phase 2, E-4 Block, New Delhi", "latitude": 28.6075, "longitude": 77.2920, "city": "New Delhi"},
        "status": "Resolved",
        "photo_url": None,
        "days_ago": 10,
        "user": "mayurvihar.citi@gmail.com"
    },
    {
        "category": "Public Transit & Metro",
        "description": "Footover bridge at Kashmere Gate Metro station has broken steps — 4 steps cracked and dangerous. Senior citizens and children are falling. MCD has not responded to 3 prior complaints. | Priority: High - Safety hazard at public transit hub. | Severity: 8/10",
        "location": {"address": "Kashmere Gate Metro Station, New Delhi", "latitude": 28.6676, "longitude": 77.2283, "city": "New Delhi"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 6,
        "user": "transit.user@gmail.com"
    },
    {
        "category": "Parks, Green Spaces & Urban Forestry",
        "description": "100-year-old banyan tree fallen on Lodhi Garden path after storm, blocking the main walkway entirely. Heavy branches across path. No maintenance crew visible. | Priority: Medium - Tourist area obstruction. | Severity: 5/10",
        "location": {"address": "Lodhi Garden, New Delhi", "latitude": 28.5916, "longitude": 77.2207, "city": "New Delhi"},
        "status": "Resolved",
        "photo_url": None,
        "days_ago": 2,
        "user": "parkuser.delhi@gmail.com"
    },
    {
        "category": "Schools & Educational Infrastructure",
        "description": "MCD Primary School, Shahdara: Roof of classroom 4B leaking heavily during rain, exposing 40 children to water. Ceiling fans have started sparking. No repairs done despite 3 prior complaints. | Priority: Critical - Children's safety at risk. | Severity: 9/10",
        "location": {"address": "MCD Primary School, Shahdara, New Delhi", "latitude": 28.6742, "longitude": 77.2880, "city": "New Delhi"},
        "status": "In Progress",
        "photo_url": None,
        "days_ago": 14,
        "user": "shahdara.school@mcd.gov.in"
    },

    # ── BRAZIL (São Paulo) ──────────────────────────────────────────────────
    {
        "category": "Roads, Bridges & Arterial Corridors",
        "description": "Avenida Paulista, near MASP museum: Large sinkhole opened due to underground water leak. Road partially collapsed, blocking 2 of 4 lanes. Risk of further collapse. | Priority: Critical - Sinkhole on major boulevard. | Severity: 9/10",
        "location": {"address": "Avenida Paulista, near MASP, São Paulo, Brazil", "latitude": -23.5614, "longitude": -46.6561, "city": "São Paulo"},
        "status": "In Progress",
        "photo_url": None,
        "days_ago": 2,
        "user": "paulista.resident@sp.gov.br"
    },
    {
        "category": "Water Supply",
        "description": "Sabesp has cut water supply to Jardins district for 3 days without prior notice. No alternative water provision made. Heat wave currently 38°C. | Priority: High - Water crisis during heat wave. | Severity: 9/10",
        "location": {"address": "Jardins, São Paulo, Brazil", "latitude": -23.5710, "longitude": -46.6566, "city": "São Paulo"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 3,
        "user": "jardins.morador@gmail.com"
    },
    {
        "category": "Public Safety & Street Lighting",
        "description": "12 streetlights on Rua Augusta are broken for 2 months. After dark, the street becomes dangerous — multiple muggings have been reported in the unlit stretch. | Priority: High - Public safety emergency. | Severity: 8/10",
        "location": {"address": "Rua Augusta, São Paulo, Brazil", "latitude": -23.5559, "longitude": -46.6520, "city": "São Paulo"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 60,
        "user": "rua.augusta.seg@gmail.com"
    },
    {
        "category": "Waste Management & Sanitation",
        "description": "Illegal dumping ground has formed near Parque do Ibirapuera east entrance. Household waste, electronic waste, and construction debris piled 2 meters high. | Priority: Medium - Environmental hazard near major park. | Severity: 7/10",
        "location": {"address": "Parque do Ibirapuera East Entrance, São Paulo, Brazil", "latitude": -23.5874, "longitude": -46.6576, "city": "São Paulo"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 30,
        "user": "ibirapuera.verde@sp.br"
    },

    # ── CHINA (Shanghai) ────────────────────────────────────────────────────
    {
        "category": "Roads, Bridges & Arterial Corridors",
        "description": "Bridge guardrail on Waibaidu Bridge is severely corroded and broken in 3 sections. Pedestrians risk falling into the Suzhou Creek below. | Priority: Critical - Structural safety failure on heritage bridge. | Severity: 9/10",
        "location": {"address": "Waibaidu Bridge, Huangpu District, Shanghai, China", "latitude": 31.2432, "longitude": 121.4882, "city": "Shanghai"},
        "status": "In Progress",
        "photo_url": None,
        "days_ago": 7,
        "user": "shanghai.resident@sh.gov.cn"
    },
    {
        "category": "Electricity & Power Grid",
        "description": "Repeated power fluctuations in Pudong New Area, Lujiazui district — 6 incidents this week. Electronics getting damaged. Small businesses reporting losses. | Priority: High - Repeated power quality issues in financial district. | Severity: 7/10",
        "location": {"address": "Lujiazui, Pudong, Shanghai, China", "latitude": 31.2397, "longitude": 121.4993, "city": "Shanghai"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 7,
        "user": "lujiazui.biz@pudong.gov.cn"
    },
    {
        "category": "Drainage & Flood Management",
        "description": "Xujiahui area flooded during yesterday's typhoon. Storm drains completely overwhelmed. Basement carparks flooded. City needs comprehensive drainage upgrade here. | Priority: High - Typhoon-related infrastructure failure. | Severity: 8/10",
        "location": {"address": "Xujiahui, Xuhui District, Shanghai, China", "latitude": 31.1986, "longitude": 121.4344, "city": "Shanghai"},
        "status": "Resolved",
        "photo_url": None,
        "days_ago": 4,
        "user": "xuhui.district@sh.gov.cn"
    },

    # ── RUSSIA (Moscow) ─────────────────────────────────────────────────────
    {
        "category": "Roads, Bridges & Arterial Corridors",
        "description": "Kutuzovsky Prospekt: Road surface crumbling after harsh winter. Potholes every 50 meters making driving hazardous. Bus 157 route delayed by 40+ minutes daily due to road condition. | Priority: High - Major boulevard deteriorating. | Severity: 7/10",
        "location": {"address": "Kutuzovsky Prospekt, Moscow, Russia", "latitude": 55.7390, "longitude": 37.5480, "city": "Moscow"},
        "status": "In Progress",
        "photo_url": None,
        "days_ago": 20,
        "user": "moscow.resident@mos.ru"
    },
    {
        "category": "Public Transit & Metro",
        "description": "Escalator at Komsomolskaya Metro Station (Sokolnicheskaya Line) broken for 3 weeks. No repair team assigned. Thousands of passengers use this station daily, including elderly. | Priority: High - Key metro infrastructure failure. | Severity: 7/10",
        "location": {"address": "Komsomolskaya Metro Station, Moscow, Russia", "latitude": 55.7756, "longitude": 37.6555, "city": "Moscow"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 21,
        "user": "metro.user.msk@gmail.com"
    },
    {
        "category": "Electricity & Power Grid",
        "description": "Heating system failure in apartment block at Ulitsa Tverskaya 18. In -15°C winter temperatures, 140 apartments without heating for 36 hours. City must send emergency response immediately. | Priority: Critical - Life-threatening cold exposure. | Severity: 10/10",
        "location": {"address": "Ulitsa Tverskaya 18, Moscow, Russia", "latitude": 55.7636, "longitude": 37.6012, "city": "Moscow"},
        "status": "Resolved",
        "photo_url": None,
        "days_ago": 15,
        "user": "tverskaya18.residents@mos.ru"
    },

    # ── SOUTH AFRICA (Johannesburg / Gauteng) ───────────────────────────────
    {
        "category": "Water Supply",
        "description": "Soweto, Zone 6: No running water for 8 days. Johannesburg Water not responding. Residents are buying expensive bottled water. Area is a densely populated township. | Priority: Critical - Essential service failure in high-density area. | Severity: 9/10",
        "location": {"address": "Soweto Zone 6, Johannesburg, South Africa", "latitude": -26.2674, "longitude": 27.8579, "city": "Johannesburg"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 8,
        "user": "soweto.residents@gauteng.gov.za"
    },
    {
        "category": "Electricity & Power Grid",
        "description": "Sandton CBD: Loadshedding schedule not matching Eskom published schedule. Businesses losing an extra 4-6 hours of power daily beyond planned outages. Refrigerated goods destroyed. | Priority: High - Irregular load shedding causing business losses. | Severity: 8/10",
        "location": {"address": "Sandton CBD, Johannesburg, South Africa", "latitude": -26.1076, "longitude": 28.0567, "city": "Johannesburg"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 5,
        "user": "sandton.biz@gcc.gov.za"
    },
    {
        "category": "Public Safety & Street Lighting",
        "description": "Alexandra Township: No working streetlights for 2 months on 3rd Avenue and 4th Avenue. Crime has increased significantly after dark. Residents afraid to walk at night. | Priority: Critical - Public safety emergency in high-crime area. | Severity: 9/10",
        "location": {"address": "Alexandra Township, 3rd Avenue, Johannesburg, South Africa", "latitude": -26.1033, "longitude": 28.0835, "city": "Johannesburg"},
        "status": "In Progress",
        "photo_url": None,
        "days_ago": 60,
        "user": "alex.township@community.za"
    },

    # ── EGYPT (Cairo) ───────────────────────────────────────────────────────
    {
        "category": "Roads, Bridges & Arterial Corridors",
        "description": "Corniche El Nil near Zamalek: Guardrail on Nile-side walkway broken for 1 month. Pedestrians, especially children, at risk of falling into the Nile. | Priority: Critical - Safety hazard at riverside walkway. | Severity: 9/10",
        "location": {"address": "Corniche El Nil, Zamalek, Cairo, Egypt", "latitude": 30.0626, "longitude": 31.2232, "city": "Cairo"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 30,
        "user": "zamalek.resident@cairo.gov.eg"
    },
    {
        "category": "Waste Management & Sanitation",
        "description": "Khan El-Khalili tourist area: Garbage bins overflowing for 4 days during Eid holiday surge. Waste on streets affecting tourism and causing smell complaints from hotels. | Priority: High - Tourist district sanitation emergency. | Severity: 7/10",
        "location": {"address": "Khan El-Khalili Market, Cairo, Egypt", "latitude": 30.0476, "longitude": 31.2621, "city": "Cairo"},
        "status": "Resolved",
        "photo_url": None,
        "days_ago": 12,
        "user": "cairo.tourism@ministry.eg"
    },

    # ── INDIA — More cities ──────────────────────────────────────────────────
    {
        "category": "Healthcare & Medical Infrastructure",
        "description": "AIIMS Delhi Emergency Wing: 3 of 6 ambulance bays blocked by illegally parked vehicles for weeks. Emergency ambulances taking 8+ extra minutes to unload patients. Lives at risk. | Priority: Critical - Emergency medical response compromised. | Severity: 10/10",
        "location": {"address": "AIIMS Emergency Gate, Ansari Nagar, New Delhi", "latitude": 28.5670, "longitude": 77.2090, "city": "New Delhi"},
        "status": "In Progress",
        "photo_url": None,
        "days_ago": 10,
        "user": "aiims.ambulance@aiims.edu"
    },
    {
        "category": "Drainage & Flood Management",
        "description": "Gurugram sector 29: Waterlogging after every rain event, even moderate ones. Water enters ground-floor apartments. Existing drainage pipes completely choked with construction debris. | Priority: High - Repeated flooding in residential area. | Severity: 8/10",
        "location": {"address": "Sector 29, Gurugram, Haryana", "latitude": 28.4744, "longitude": 77.0857, "city": "Gurugram"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 11,
        "user": "sec29.gurugram@gmail.com"
    },
    {
        "category": "Public Safety & Street Lighting",
        "description": "CP Outer Circle: 20+ streetlights broken for 6 weeks. This iconic area sees thousands of tourists nightly. Incidents of theft and harassment increasing after 9 PM. | Priority: High - Safety in major tourist area. | Severity: 7/10",
        "location": {"address": "Connaught Place Outer Circle, New Delhi", "latitude": 28.6315, "longitude": 77.2167, "city": "New Delhi"},
        "status": "In Progress",
        "photo_url": None,
        "days_ago": 42,
        "user": "cp.tourist@ndmc.gov.in"
    },
    {
        "category": "Roads, Bridges & Arterial Corridors",
        "description": "Flyover ramp at Ashram Chowk has developed visible cracks in the concrete pillar. Structural integrity concerning. PWD inspection requested urgently. Traffic should be diverted as precaution. | Priority: Critical - Structural integrity of flyover in question. | Severity: 9/10",
        "location": {"address": "Ashram Chowk Flyover, New Delhi", "latitude": 28.5706, "longitude": 77.2503, "city": "New Delhi"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 4,
        "user": "ashram.safety@pwd.delhi.gov.in"
    },
    {
        "category": "Water Supply",
        "description": "Chandni Chowk heritage zone: Ancient water pipeline in Khari Baoli market area is leaking since 6 months. Water wastage massive and market lanes remain wet and slippery causing falls. | Priority: Medium - Long-standing leak causing civic hazard. | Severity: 6/10",
        "location": {"address": "Khari Baoli, Chandni Chowk, Old Delhi", "latitude": 28.6571, "longitude": 77.2267, "city": "New Delhi"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 180,
        "user": "kharibuyer@gmail.com"
    },

    # ── INDONESIA (Jakarta) ──────────────────────────────────────────────────
    {
        "category": "Drainage & Flood Management",
        "description": "Pluit area: Repeated flooding due to clogged drainage canals. Last flood reached 1.2m depth, displacing 400 families. Canal desilting overdue by 3 years. | Priority: Critical - Mass displacement from recurrent flooding. | Severity: 9/10",
        "location": {"address": "Pluit, North Jakarta, Indonesia", "latitude": -6.1273, "longitude": 106.7964, "city": "Jakarta"},
        "status": "In Progress",
        "photo_url": None,
        "days_ago": 7,
        "user": "pluit.warga@jakarta.go.id"
    },
    {
        "category": "Roads, Bridges & Arterial Corridors",
        "description": "Jl. Sudirman: Bus lane markings completely faded. Private vehicles occupying bus lanes causing Transjakarta delays of 25-40 minutes at peak hours. Re-marking overdue by 8 months. | Priority: Medium - Transit efficiency impacted by road marking failure. | Severity: 6/10",
        "location": {"address": "Jalan Sudirman, Jakarta Pusat, Indonesia", "latitude": -6.2146, "longitude": 106.8229, "city": "Jakarta"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 240,
        "user": "transjakarta.user@gmail.com"
    },

    # ── UAE (Dubai) ──────────────────────────────────────────────────────────
    {
        "category": "Roads, Bridges & Arterial Corridors",
        "description": "Sheikh Zayed Road underpass at Mall of the Emirates: Ceiling water seepage after heavy rain. Dark stains and dripping water creating slip hazard in high-traffic tunnel. | Priority: High - Safety risk in busy underpass. | Severity: 7/10",
        "location": {"address": "Sheikh Zayed Road Underpass, Mall of the Emirates, Dubai, UAE", "latitude": 25.1173, "longitude": 55.1993, "city": "Dubai"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 5,
        "user": "dubai.resident@dm.gov.ae"
    },
    {
        "category": "Parks, Green Spaces & Urban Forestry",
        "description": "Safa Park: Automated irrigation system malfunctioning — overwatering in 3 sections creating muddy unusable areas. Lawn completely destroyed. System needs recalibration. | Priority: Low - Park maintenance issue. | Severity: 4/10",
        "location": {"address": "Safa Park, Al Wasl Road, Dubai, UAE", "latitude": 25.1879, "longitude": 55.2365, "city": "Dubai"},
        "status": "Resolved",
        "photo_url": None,
        "days_ago": 8,
        "user": "safapark.user@dm.gov.ae"
    },

    # ── SAUDI ARABIA (Riyadh) ────────────────────────────────────────────────
    {
        "category": "Electricity & Power Grid",
        "description": "Al Olaya district: Voltage fluctuations causing air conditioning units to trip repeatedly during peak summer hours (45°C+). 3 AC units in commercial buildings burned out this week. | Priority: High - Power quality emergency in summer heat. | Severity: 8/10",
        "location": {"address": "Al Olaya District, Riyadh, Saudi Arabia", "latitude": 24.6942, "longitude": 46.6820, "city": "Riyadh"},
        "status": "In Progress",
        "photo_url": None,
        "days_ago": 6,
        "user": "olaya.biz@amanatriyadh.gov.sa"
    },
    {
        "category": "Waste Management & Sanitation",
        "description": "Al-Bat'ha market: Street cleaning schedule not followed for 2 weeks during Hajj season influx. Market lanes overflowing with waste. Health inspection risk. | Priority: High - Hygiene emergency during major religious season. | Severity: 8/10",
        "location": {"address": "Al-Bat'ha Market, Riyadh, Saudi Arabia", "latitude": 24.6862, "longitude": 46.7155, "city": "Riyadh"},
        "status": "Resolved",
        "photo_url": None,
        "days_ago": 20,
        "user": "bathamarket@riyadh.gov.sa"
    },

    # ── ETHIOPIA (Addis Ababa) ───────────────────────────────────────────────
    {
        "category": "Water Supply",
        "description": "Bole Sub-city: Water supply available only 2 hours per day (5–7 AM). Residents unable to collect enough water. Schools and health centres also affected. | Priority: High - Severe water rationing in dense urban area. | Severity: 8/10",
        "location": {"address": "Bole Sub-city, Addis Ababa, Ethiopia", "latitude": 8.9981, "longitude": 38.8020, "city": "Addis Ababa"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 30,
        "user": "bole.resident@addisababa.gov.et"
    },
    {
        "category": "Roads, Bridges & Arterial Corridors",
        "description": "Meskel Square approach road: Cobblestone surface deteriorating badly. Sharp stones causing tyre punctures and injuries to pedestrians walking barefoot. | Priority: Medium - Road surface deterioration in city centre. | Severity: 6/10",
        "location": {"address": "Meskel Square, Addis Ababa, Ethiopia", "latitude": 9.0113, "longitude": 38.7632, "city": "Addis Ababa"},
        "status": "Pending",
        "photo_url": None,
        "days_ago": 45,
        "user": "meskel.area@aaca.gov.et"
    },
]

def generate_id():
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    suffix = str(random.randint(100000, 999999))
    return f"CP-{now}{suffix}"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

inserted = 0
for c in COMPLAINTS:
    cid = generate_id()
    days = c.get("days_ago", 1)
    ts = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
    loc_json = json.dumps(c["location"])
    cur.execute(
        "INSERT INTO complaints (id, user_id, category, description, location_json, status, timestamp, photo_url, resolution_photo, resolution_notes) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (cid, c.get("user","citizen@civicpulse.brics"), c["category"], c["description"], loc_json, c["status"], ts, c.get("photo_url"), None, None)
    )
    inserted += 1

conn.commit()
conn.close()

print(f"[OK] Inserted {inserted} new complaints successfully.")

# Verify total
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM complaints")
total = cur.fetchone()[0]
cur.execute("SELECT status, COUNT(*) FROM complaints GROUP BY status")
by_status = cur.fetchall()
conn.close()
print(f"[DB] Total complaints in DB: {total}")
print(f"[DB] By status: {dict(by_status)}")
