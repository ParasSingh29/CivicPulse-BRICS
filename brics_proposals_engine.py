"""
CivicPulse-BRICS: City Proposals, Municipal Officer Analytics, and BRICS Joint Ventures Engine
Provides:
1. Dynamic Municipal Officer Health & Red/Yellow/Green Complaint Tracking
2. City-to-Centre Strategic Proposals Registry & Inter-City Peer Upvoting
3. Local Area AI Infrastructure Planning (City-Scoped Gemini 2.5 Synthesizer)
4. Central AI National Interest Strategic Engine (BRICS Sovereign Joint Ventures)
5. Inbound BRICS Partner Requests Ingestion & Bilateral Working Group Protocols
"""

import os
import json
from datetime import datetime
from api_client import get_all_complaints
from brics_context import get_brics_node, INFRASTRUCTURE_SECTORS
from gemini_helper import call_gemini_with_fallback

CITY_PROPOSALS_FILE = "city_proposals.json"
BRICS_INCOMING_FILE = "brics_incoming_requests.json"

# ==============================================================================
# 1. CITY OFFICERS REGISTRY & MUNICIPAL STATUS (RED, YELLOW, GREEN)
# ==============================================================================

OFFICERS_REGISTRY = [
    {
        "id": "OFF-DEL-01",
        "name": "Er. Vikram Sharma",
        "city": "Delhi",
        "jurisdiction": "National Capital Region (Delhi NCR)",
        "country": "India",
        "country_code": "IN",
        "flag": "🇮🇳",
        "department": "Public Works & Urban Mobility Dept",
        "designation": "Chief Executive Engineer",
        "email": "vikram.sharma@delhi.gov.in",
        "phone": "+91 98101 11223"
    },
    {
        "id": "OFF-MUM-02",
        "name": "Er. Rajesh Kulkarni",
        "city": "Mumbai",
        "jurisdiction": "Mumbai Metropolitan Region (MMRDA)",
        "country": "India",
        "country_code": "IN",
        "flag": "🇮🇳",
        "department": "Metropolitan Rail & Highway Authority",
        "designation": "Superintending Transit Engineer",
        "email": "rajesh.kulkarni@mmrda.gov.in",
        "phone": "+91 98200 44556"
    },
    {
        "id": "OFF-BLR-03",
        "name": "Dr. Sunita Rao",
        "city": "Bengaluru",
        "jurisdiction": "Greater Bengaluru Urban Area (BBMP)",
        "country": "India",
        "country_code": "IN",
        "flag": "🇮🇳",
        "department": "Smart Mobility & Municipal Water Board",
        "designation": "Executive Director (Urban Planning)",
        "email": "sunita.rao@bbmp.gov.in",
        "phone": "+91 98450 77889"
    },
    {
        "id": "OFF-SP-04",
        "name": "Eng. Carlos Mendes",
        "city": "São Paulo",
        "jurisdiction": "São Paulo Metropolitan Area (RMSP)",
        "country": "Brazil",
        "country_code": "BR",
        "flag": "🇧🇷",
        "department": "Secretaria Municipal de Infraestrutura Urbana",
        "designation": "Diretor Geral de Obras Públicas",
        "email": "carlos.mendes@sp.gov.br",
        "phone": "+55 11 98101 5566"
    },
    {
        "id": "OFF-JHB-05",
        "name": "Dir. Sipho Nkosi",
        "city": "Johannesburg",
        "jurisdiction": "City of Johannesburg Metropolitan (Gauteng)",
        "country": "South Africa",
        "country_code": "ZA",
        "flag": "🇿🇦",
        "department": "Johannesburg Roads Agency & City Power",
        "designation": "Executive Infrastructure Director",
        "email": "sipho.nkosi@joburg.gov.za",
        "phone": "+27 11 981 7788"
    }
]

def normalize_city_name(val):
    """Normalizes city string from address or location data."""
    if not val:
        return "Delhi"
    v = str(val).lower()
    if "delhi" in v or "pitampura" in v or "rohini" in v or "connaught" in v or "janakpuri" in v or "okhla" in v:
        return "Delhi"
    if "mumbai" in v or "bandra" in v or "andheri" in v or "dadar" in v or "kurla" in v:
        return "Mumbai"
    if "bengaluru" in v or "bangalore" in v or "koramangala" in v or "whitefield" in v or "silk board" in v:
        return "Bengaluru"
    if "são paulo" in v or "sao paulo" in v or "itaquera" in v or "pinheiros" in v or "brazil" in v:
        return "São Paulo"
    if "johannesburg" in v or "joburg" in v or "soweto" in v or "sandton" in v or "south africa" in v:
        return "Johannesburg"
    return "Delhi"

def get_city_officers_overview():
    """
    Returns all assigned city officers along with their live complaint statistics:
    - Red (Critical / High / Pending)
    - Yellow (In Progress / Dispatched)
    - Green (Resolved / Closed)
    - Total Complaints & Health Index
    """
    all_complaints = get_all_complaints()
    officers = []

    for off in OFFICERS_REGISTRY:
        city = off["city"]
        city_complaints = []
        for c in all_complaints:
            loc = c.get("location", {}) if isinstance(c.get("location"), dict) else {}
            addr = str(loc.get("address", "")) + " " + str(loc.get("city", "")) + " " + str(c.get("description", ""))
            if normalize_city_name(addr).lower() == city.lower():
                city_complaints.append(c)

        red_count = 0
        yellow_count = 0
        green_count = 0

        for c in city_complaints:
            status = str(c.get("status", "")).lower()
            if "resolved" in status or "closed" in status or "fixed" in status:
                green_count += 1
            elif "progress" in status or "dispatch" in status:
                yellow_count += 1
            else:
                red_count += 1

        total = len(city_complaints)
        if total > 0:
            health_index = int(round(((green_count * 1.0) + (yellow_count * 0.5)) / total * 100))
        else:
            health_index = 95

        officers.append({
            **off,
            "total_problems": total,
            "red_problems": red_count,
            "yellow_problems": yellow_count,
            "green_problems": green_count,
            "health_index": health_index,
            "status_summary": f"{red_count} Critical • {yellow_count} In Progress • {green_count} Resolved"
        })

    return officers

# ==============================================================================
# 2. CITY PROPOSALS TO CENTRE & INTER-CITY PEER UPVOTING
# ==============================================================================

DEFAULT_CITY_PROPOSALS = [
    {
        "id": "PROP-DEL-2026-01",
        "city": "Delhi",
        "country": "India",
        "country_code": "IN",
        "officer_name": "Er. Vikram Sharma",
        "officer_id": "OFF-DEL-01",
        "department": "Public Works & Urban Mobility Dept",
        "title": "Outer Ring Road Phase-IV Elevated Metro Feeder & 6-Lane Expressway Bypass",
        "category": "Roads, Bridges & Arterial Corridors",
        "estimated_capex": "₹1,450 Crore",
        "timeline": "28 Months",
        "demographic_impact": "Relieves gridlock for 1.8 Million commuters; cuts arterial peak delay by 48 mins",
        "justification": "Surface telemetry registers 240% vehicular saturation and severe pavement shearing along Outer Ring Road choke points. Local repairs cannot resolve structural bottlenecks without grade-separated elevated transit.",
        "ai_generated": True,
        "upvotes": 14,
        "upvoted_by": ["OFF-MUM-02", "OFF-BLR-03", "OFF-SP-04", "OFF-JHB-05"],
        "status": "Under Central Review",
        "central_notes": "Planning Commission reviewing inclusion in PM Gati Shakti FY 2026-27 tranche.",
        "date": "2026-08-25"
    },
    {
        "id": "PROP-MUM-2026-02",
        "city": "Mumbai",
        "country": "India",
        "country_code": "IN",
        "officer_name": "Er. Rajesh Kulkarni",
        "officer_id": "OFF-MUM-02",
        "department": "Metropolitan Rail & Highway Authority",
        "title": "Western Railway Corridor High-Capacity Quadrupling & Multi-Modal Interchange",
        "category": "Public Transport & Transit Hubs",
        "estimated_capex": "₹3,200 Crore",
        "timeline": "36 Months",
        "demographic_impact": "3.5 Million daily suburban railway passengers; eliminates life-threatening super-dense crushing",
        "justification": "Suburban trains operate at 16 commuters per sq meter during peak hours with average 28 km/h crawl speeds. Urgent national corridor intervention required.",
        "ai_generated": True,
        "upvotes": 19,
        "upvoted_by": ["OFF-DEL-01", "OFF-BLR-03", "OFF-SP-04"],
        "status": "Escalated to BRICS JV",
        "central_notes": "Central Command prioritizing for Sino-Indian High-Speed Rail consortium assessment.",
        "date": "2026-08-28"
    },
    {
        "id": "PROP-BLR-2026-03",
        "city": "Bengaluru",
        "country": "India",
        "country_code": "IN",
        "officer_name": "Dr. Sunita Rao",
        "officer_id": "OFF-BLR-03",
        "department": "Smart Mobility & Municipal Water Board",
        "title": "Silk Board to Electronic City Driverless Elevated Pod-Transit & Drainage Canal Overhaul",
        "category": "Public Transport & Transit Hubs",
        "estimated_capex": "₹1,850 Crore",
        "timeline": "24 Months",
        "demographic_impact": "Protects IT corridor transit for 850,000 tech employees and ends Bellandur basin flooding",
        "justification": "Peak traffic delays at Central Silk Board junction cost ₹1,050 Cr annually in lost productivity and vehicle emissions.",
        "ai_generated": False,
        "upvotes": 11,
        "upvoted_by": ["OFF-DEL-01", "OFF-MUM-02"],
        "status": "Submitted to Centre",
        "central_notes": "Feasibility report requested from state urban development directorate.",
        "date": "2026-09-02"
    },
    {
        "id": "PROP-SP-2026-04",
        "city": "São Paulo",
        "country": "Brazil",
        "country_code": "BR",
        "officer_name": "Eng. Carlos Mendes",
        "officer_id": "OFF-SP-04",
        "department": "Secretaria Municipal de Infraestrutura Urbana",
        "title": "Marginal Tietê Deep Gravity Inundation Bypass & Bio-Drainage Canal",
        "category": "Stormwater Drainage & Monsoon Floods",
        "estimated_capex": "R$ 1.150 Milhões",
        "timeline": "22 Meses",
        "demographic_impact": "Protects 2.4 Million residents and main freight connection to Santos Port",
        "justification": "Seasonal flood events paralyze logistics between interior industrial belt and seaport.",
        "ai_generated": True,
        "upvotes": 8,
        "upvoted_by": ["OFF-DEL-01", "OFF-JHB-05"],
        "status": "Under Central Review",
        "central_notes": "Federal PAC matching grant under technical consideration.",
        "date": "2026-08-30"
    },
    {
        "id": "PROP-JHB-2026-05",
        "city": "Johannesburg",
        "country": "South Africa",
        "country_code": "ZA",
        "officer_name": "Dir. Sipho Nkosi",
        "officer_id": "OFF-JHB-05",
        "department": "Johannesburg Roads Agency & City Power",
        "title": "Soweto 150MW Sovereign Solar & Decentralized Battery Storage Microgrid",
        "category": "Electricity, Streetlights & Grid",
        "estimated_capex": "R 1.250 Million",
        "timeline": "18 Months",
        "demographic_impact": "Guarantees 24/7 uninterrupted power for 650,000 township households, clinics & water pumps",
        "justification": "Recurrent transformer blowouts and Stage 6 loadshedding disable drinking water booster stations.",
        "ai_generated": True,
        "upvotes": 16,
        "upvoted_by": ["OFF-DEL-01", "OFF-MUM-02", "OFF-SP-04"],
        "status": "Approved for National Budget",
        "central_notes": "National Treasury approved 60% grant under Just Energy Transition Investment Plan.",
        "date": "2026-09-01"
    }
]

def init_city_proposals():
    """Initializes proposals store if absent."""
    if not os.path.exists(CITY_PROPOSALS_FILE):
        with open(CITY_PROPOSALS_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CITY_PROPOSALS, f, indent=2, ensure_ascii=False)

init_city_proposals()

def get_city_proposals(city=None):
    """Retrieves city proposals, optionally filtered by city."""
    init_city_proposals()
    try:
        with open(CITY_PROPOSALS_FILE, "r", encoding="utf-8") as f:
            proposals = json.load(f)
    except Exception:
        proposals = list(DEFAULT_CITY_PROPOSALS)

    if city and city != "All Cities":
        c_clean = city.strip().lower()
        proposals = [p for p in proposals if p.get("city", "").lower() == c_clean]

    proposals.sort(key=lambda x: x.get("upvotes", 0), reverse=True)
    return proposals

def save_city_proposal(city, officer_name, officer_id, department, title, category,
                       estimated_capex, timeline, demographic_impact, justification, ai_generated=False):
    """Saves a new strategic report/proposal from a city official to Central Command."""
    proposals = get_city_proposals()
    pid = f"PROP-{city[:3].upper()}-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    matched_officer = next((o for o in OFFICERS_REGISTRY if o["city"].lower() == city.lower()), None)
    country = matched_officer["country"] if matched_officer else "India"
    country_code = matched_officer["country_code"] if matched_officer else "IN"

    new_prop = {
        "id": pid,
        "city": city,
        "country": country,
        "country_code": country_code,
        "officer_name": officer_name or "Municipal Executive Officer",
        "officer_id": officer_id or "OFF-MUN-01",
        "department": department or "Public Works & Urban Affairs",
        "title": title,
        "category": category,
        "estimated_capex": estimated_capex or "Under Evaluation",
        "timeline": timeline or "24 Months",
        "demographic_impact": demographic_impact or "Community-wide benefit",
        "justification": justification,
        "ai_generated": bool(ai_generated),
        "upvotes": 1,
        "upvoted_by": [officer_id] if officer_id else [],
        "status": "Submitted to Centre",
        "central_notes": "Awaiting review by Central Planning Commission.",
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    proposals.insert(0, new_prop)
    with open(CITY_PROPOSALS_FILE, "w", encoding="utf-8") as f:
        json.dump(proposals, f, indent=2, ensure_ascii=False)

    return new_prop

def upvote_city_proposal(proposal_id, voter_id):
    """Registers an inter-city peer upvote from another city officer."""
    proposals = get_city_proposals()
    target = None

    for p in proposals:
        if p.get("id") == proposal_id:
            upvoters = p.setdefault("upvoted_by", [])
            if voter_id and voter_id in upvoters:
                return False, p.get("upvotes", 0), "You have already upvoted this proposal from your municipal node!"
            if voter_id:
                upvoters.append(voter_id)
            p["upvotes"] = p.get("upvotes", 0) + 1
            target = p
            break

    if target:
        with open(CITY_PROPOSALS_FILE, "w", encoding="utf-8") as f:
            json.dump(proposals, f, indent=2, ensure_ascii=False)
        return True, target["upvotes"], "Proposal upvoted successfully! Regional solidarity score updated."

    return False, 0, "Proposal not found."

def update_city_proposal_status(proposal_id, new_status, central_notes=None):
    """Allows Central Official to sanction, escalate, or update status of a city proposal."""
    proposals = get_city_proposals()
    target = None

    for p in proposals:
        if p.get("id") == proposal_id:
            p["status"] = new_status
            if central_notes:
                p["central_notes"] = central_notes
            target = p
            break

    if target:
        with open(CITY_PROPOSALS_FILE, "w", encoding="utf-8") as f:
            json.dump(proposals, f, indent=2, ensure_ascii=False)
        return True, target

    return False, None

# ==============================================================================
# 3. LOCAL AREA AI STRATEGIC PLANNER (CITY-LEVEL)
# ==============================================================================

def generate_city_ai_plan(city="Delhi"):
    """
    Synthesizes larger strategic infrastructure plans specifically for one city
    by analyzing local complaint frequency, categories, and hotspots.
    Example: Heavy traffic complaints -> Suggests elevated Metro corridor.
    """
    clean_city = city.strip()
    all_complaints = get_all_complaints()

    city_complaints = []
    category_counts = {}
    for c in all_complaints:
        loc = c.get("location", {}) if isinstance(c.get("location"), dict) else {}
        addr = str(loc.get("address", "")) + " " + str(loc.get("city", "")) + " " + str(c.get("description", ""))
        if normalize_city_name(addr).lower() == clean_city.lower():
            city_complaints.append(c)
            cat = c.get("category", "General")
            category_counts[cat] = category_counts.get(cat, 0) + 1

    prompt = f"""
You are the Municipal Infrastructure AI Chief Architect for the City of {clean_city}.
Analyze the following active citizen complaints and problems registered in {clean_city}:
- Total Active City Problems: {len(city_complaints)}
- Top Issue Categories: {json.dumps(category_counts)}
- Sample Complaint Descriptions:
"""
    for c in city_complaints[:6]:
        prompt += f"  * [{c.get('category')}] {c.get('description', '')[:100]}...\n"

    prompt += f"""
Suggest 2-3 High-Impact Strategic Infrastructure Plans for {clean_city} to resolve root-cause systemic problems.
For example, if there is chronic traffic or road complaints, suggest an Elevated Metro Transit Corridor or Multi-Level Arterial Bypass.
If there are flood/drainage complaints, suggest an Enclosed Stormwater Trunk Canal.

Return ONLY a valid JSON array of objects with keys:
"title", "category", "estimated_capex", "timeline", "demographic_impact", "justification", "policy_recommendation"
"""
    try:
        gemini_resp = call_gemini_with_fallback(prompt)
        if gemini_resp and "{" in gemini_resp:
            clean_json = gemini_resp.strip()
            if "```json" in clean_json:
                clean_json = clean_json.split("```json")[1].split("```")[0].strip()
            elif "```" in clean_json:
                clean_json = clean_json.split("```")[1].split("```")[0].strip()
            parsed = json.loads(clean_json)
            if isinstance(parsed, list) and len(parsed) > 0:
                for p in parsed:
                    p["city"] = clean_city
                    p["ai_generated"] = True
                return parsed
    except Exception as e:
        print(f"[City AI Planner] Gemini notice: {e}")

    fallback_plans = {
        "Delhi": [
            {
                "title": "Outer Ring Road Metro Phase-IV Feeder & High-Speed Transit Bypass",
                "category": "Roads, Bridges & Arterial Corridors",
                "city": "Delhi",
                "estimated_capex": "₹1,450 Crore",
                "timeline": "28 Months",
                "demographic_impact": "1.8 Million commuters daily across North-West & Central corridors",
                "justification": "Analysis of road and transit complaints confirms that surface pavement patching cannot withstand 240% vehicular saturation. Elevated automated metro loops will absorb 42% of private vehicle trips.",
                "policy_recommendation": "File formal proposal to Ministry of Housing and Urban Affairs (MOHUA) under National Transit Scheme.",
                "ai_generated": True
            },
            {
                "title": "Seelampur 50 MGD Deep Gravity Stormwater Canal & Automated Siphon Station",
                "category": "Stormwater Drainage & Monsoon Floods",
                "city": "Delhi",
                "estimated_capex": "₹920 Crore",
                "timeline": "22 Months",
                "demographic_impact": "Protects 3.9 Million residents from catastrophic seasonal monsoon submergence",
                "justification": "Repeated citizen alerts regarding basement inundation and waterlogging on Yamuna floodplains require enclosed high-capacity gravity drainage.",
                "policy_recommendation": "Escalate to Central Command for PM Gati Shakti National Flood Mitigation grant.",
                "ai_generated": True
            }
        ],
        "Mumbai": [
            {
                "title": "Western Railway Quadrupling & Automated CBTC Fast-Train Corridor",
                "category": "Public Transport & Transit Hubs",
                "city": "Mumbai",
                "estimated_capex": "₹3,200 Crore",
                "timeline": "36 Months",
                "demographic_impact": "3.5 Million daily suburban commuters; cuts transit times by 50%",
                "justification": "Suburban railway network handles over 7.5 million daily commuters with extreme overcapacity. Quadrupling lines with computer-based train control slashes headway from 4 mins to 90 seconds.",
                "policy_recommendation": "Recommend Central Government escalate to BRICS High-Speed Rail Technology Joint Venture.",
                "ai_generated": True
            },
            {
                "title": "Mithi River Basin Deep Subsurface Flood Diversion Tunnel",
                "category": "Stormwater Drainage & Monsoon Floods",
                "city": "Mumbai",
                "estimated_capex": "₹2,100 Crore",
                "timeline": "30 Months",
                "demographic_impact": "Protects 2.8 Million residents from high-tide monsoon flooding",
                "justification": "High tide backflow combined with torrential monsoon precipitation routinely submerges railway tracks and airport access roads.",
                "policy_recommendation": "File proposal to Central Disaster Management Authority.",
                "ai_generated": True
            }
        ],
        "Bengaluru": [
            {
                "title": "Silk Board - Whitefield Autonomous Elevated Monorail & Pod Transit",
                "category": "Public Transport & Transit Hubs",
                "city": "Bengaluru",
                "estimated_capex": "₹1,850 Crore",
                "timeline": "24 Months",
                "demographic_impact": "850,000 tech employees and outer corridor residents",
                "justification": "Chronic junction paralysis causes ₹1,050 Cr in lost economic hours annually. Elevated grade separation is the sole viable physical solution.",
                "policy_recommendation": "Submit report to Central Smart Cities Directorate for 50% viability gap funding.",
                "ai_generated": True
            },
            {
                "title": "Bellandur & Varthur Catchment Automated Sewage Interceptor Network",
                "category": "Water Supply & Pipeline Leakage",
                "city": "Bengaluru",
                "estimated_capex": "₹780 Crore",
                "timeline": "18 Months",
                "demographic_impact": "Restores water table for 1.2 Million south-east zone residents",
                "justification": "Untreated domestic effluent discharge triggers foam fires and groundwater chemical contamination.",
                "policy_recommendation": "File proposal under National Clean Ganga & River Conservation Mission.",
                "ai_generated": True
            }
        ],
        "São Paulo": [
            {
                "title": "Marginal Tietê Deep Gravity Inundation Bypass & Bio-Retention Reservoir",
                "category": "Stormwater Drainage & Monsoon Floods",
                "city": "São Paulo",
                "estimated_capex": "R$ 1.150 Milhões",
                "timeline": "22 Meses",
                "demographic_impact": "2.4 Million commuters & vital freight route to Santos Port",
                "justification": "Seasonal flash floods inundate highway lanes, interrupting national import/export supply chains.",
                "policy_recommendation": "Sanction executive submission to National Ministry of Cities.",
                "ai_generated": True
            }
        ],
        "Johannesburg": [
            {
                "title": "Soweto 150MW Sovereign Solar & Decentralized Battery Storage Microgrid",
                "category": "Electricity, Streetlights & Grid",
                "city": "Johannesburg",
                "estimated_capex": "R 1.250 Million",
                "timeline": "18 Months",
                "demographic_impact": "650,000 households shielded from rolling loadshedding",
                "justification": "Severe transformer burnout reports indicate distribution collapse during rolling blackouts. Solar microgrids provide essential baseload.",
                "policy_recommendation": "Submit for National Treasury Just Energy Transition Grant.",
                "ai_generated": True
            }
        ]
    }

    return fallback_plans.get(clean_city, fallback_plans["Delhi"])

# ==============================================================================
# 4. CENTRAL AI NATIONAL INTEREST ENGINE (BRICS SOVEREIGN JOINT VENTURES)
# ==============================================================================

DEFAULT_BRICS_JV_PLANS = [
    {
        "id": "JV-CHINA-RAIL-01",
        "partner_country": "China",
        "partner_flag": "🇨🇳",
        "partner_entity": "China State Railway Group (CRRC) & China Railway Engineering (CREC)",
        "domestic_counterpart": "Indian Railways & National High-Speed Rail Corp (NHSRCL)",
        "sector": "High-Speed Rail & Rapid Passenger Transit",
        "title": "National High-Speed Bullet Train Joint Venture Corridor (Delhi-Mumbai-Bengaluru Spine)",
        "estimated_capex": "₹48,000 Crore ($5.8 Billion USD)",
        "financing_structure": "40% New Development Bank (NDB) Sovereign Loan + 30% Bilateral EPC Equity + 30% Central CapEx",
        "national_interest_analysis": "Cross-city analysis across Delhi, Mumbai, and Bengaluru reveals acute transit friction: passenger trains average under 58 km/h, causing immense freight congestion and multi-hour delays. China operates the world's largest 45,000 km high-speed network. A 50:50 joint venture transfers magnetic levitation & 350 km/h rolling stock manufacturing to domestic factories while slashing transit times from 16h to 4.5h.",
        "synergy_benefits": [
            "100% domestic rolling-stock assembly under technology transfer",
            "Eliminates 12.4 Million tons of road freight CO2 emissions annually",
            "Direct inter-city transit linking all 3 major economic growth engines"
        ],
        "status": "Ready to Propose to Partner Nation",
        "date_formulated": "2026-09-01"
    },
    {
        "id": "JV-RUSSIA-NUCLEAR-02",
        "partner_country": "Russia",
        "partner_flag": "🇷🇺",
        "partner_entity": "State Atomic Energy Corporation Rosatom & Inter RAO",
        "domestic_counterpart": "Nuclear Power Corporation of India (NPCIL) & Power Grid Corp",
        "sector": "Modular Clean Nuclear & Supergrid Baseload",
        "title": "Small Modular Reactor (SMR) 300MW Fleet & High-Voltage Supergrid Joint Venture",
        "estimated_capex": "₹34,000 Crore ($4.1 Billion USD)",
        "financing_structure": "50% Rupee-Ruble Bilateral Trade Mechanism + 50% Sovereign Green Bonds",
        "national_interest_analysis": "Industrial corridors across Delhi NCR, Okhla, and Mumbai face recurrent transformer surges and thermal plant curtailments. Russia is the global leader in compact modular nuclear tech (RITM-200 series). This JV installs 8 factory-fabricated SMR units providing continuous zero-carbon industrial power without land acquisition delays.",
        "synergy_benefits": [
            "Zero carbon footprint with 99.4% base-load capacity factor",
            "Immune to coal supply disruption or monsoon rail logistics cuts",
            "Settlement via local currency sovereign clearing mechanism"
        ],
        "status": "Under Bilateral Technical Review",
        "date_formulated": "2026-08-28"
    },
    {
        "id": "JV-BRAZIL-BIOFUEL-03",
        "partner_country": "Brazil",
        "partner_flag": "🇧🇷",
        "partner_entity": "Petrobras & Embraer Sustainable Aviation Division",
        "domestic_counterpart": "Indian Oil Corporation (IOCL) & Hindustan Petroleum",
        "sector": "Biofuels & Sustainable Aviation Fuel (SAF)",
        "title": "Bioethanol-to-Jet Fuel & Flex-Fuel Municipal Transit Fleet Joint Venture",
        "estimated_capex": "₹16,500 Crore ($2.0 Billion USD)",
        "financing_structure": "NDB Sustainable Infrastructure Facility + Joint Public-Private Partnership",
        "national_interest_analysis": "Air quality telemetry in Delhi NCR and São Paulo demonstrates massive pollution from diesel commercial fleets. Brazil leads the world in sugarcane bioethanol blending and flex-fuel aviation. This JV builds 6 mega-refineries to produce 100% domestic SAF and convert municipal bus fleets to 85% ethanol blend.",
        "synergy_benefits": [
            "Saves ₹28,000 Cr in annual crude oil foreign exchange outflow",
            "Reduces urban PM2.5 emissions by 38% in metropolitan corridors",
            "Creates direct farmer procurement mechanism for agricultural residue"
        ],
        "status": "Ready to Propose to Partner Nation",
        "date_formulated": "2026-09-03"
    },
    {
        "id": "JV-SA-MINERALS-04",
        "partner_country": "South Africa",
        "partner_flag": "🇿🇦",
        "partner_entity": "Mintek & South African National Energy Development Institute (SANEDI)",
        "domestic_counterpart": "Khanij Bidesh India Ltd (KABIL) & BHEL",
        "sector": "Critical Minerals & Deep Battery Energy Storage",
        "title": "Platinum Group Metals (PGM) Hydrogen Fuel-Cell & Vanadium Redox Battery JV",
        "estimated_capex": "₹21,000 Crore ($2.5 Billion USD)",
        "financing_structure": "BRICS Multilateral Development Bank Equity Guarantee + Bilateral Consortium",
        "national_interest_analysis": "Both South Africa (Gauteng loadshedding) and India (peak solar generation curtailment) require massive stationary battery storage. South Africa holds 75% of global platinum reserves and 26% of vanadium. This JV establishes dual-hub battery manufacturing plants in Durban and Chennai.",
        "synergy_benefits": [
            "Secures long-term sovereign supply of critical battery minerals",
            "Prevents multi-day grid blackouts across dense urban settlements",
            "Powers electric mass transit without foreign supply chain chokepoints"
        ],
        "status": "Ready to Propose to Partner Nation",
        "date_formulated": "2026-09-04"
    }
]

def generate_national_brics_plans():
    """
    Synthesizes national-scale infrastructure joint ventures with BRICS nations
    based on aggregated cross-city problem trends.
    """
    all_complaints = get_all_complaints()
    total_complaints = len(all_complaints)
    
    prompt = f"""
You are the Chief International Strategy Architect for the BRICS Infrastructure Council.
National telemetry across Indian and partner cities indicates:
- Total complaints logged: {total_complaints}
- Chronic issues reported: Slow inter-city train speeds, urban traffic congestion, power grid transformer trips, stormwater inundation.

Synthesize 4 high-impact Bilateral Joint Venture proposals partnering with BRICS member nations:
1. High-Speed Bullet Train Transit Joint Venture with China (CRRC)
2. Modular Clean Nuclear / Supergrid baseload Joint Venture with Russia (Rosatom)
3. Biofuels & Sustainable Aviation Fuel Joint Venture with Brazil (Petrobras)
4. Critical Mineral & Battery Storage (PGM/Vanadium) Joint Venture with South Africa

Return ONLY a valid JSON array of objects with keys:
"id", "partner_country", "partner_flag", "partner_entity", "domestic_counterpart", "sector", "title", "estimated_capex", "financing_structure", "national_interest_analysis", "synergy_benefits", "status"
"""
    try:
        gemini_resp = call_gemini_with_fallback(prompt)
        if gemini_resp and "{" in gemini_resp:
            clean_json = gemini_resp.strip()
            if "```json" in clean_json:
                clean_json = clean_json.split("```json")[1].split("```")[0].strip()
            elif "```" in clean_json:
                clean_json = clean_json.split("```")[1].split("```")[0].strip()
            parsed = json.loads(clean_json)
            if isinstance(parsed, list) and len(parsed) > 0:
                return parsed
    except Exception as e:
        print(f"[Central BRICS AI Planner] Gemini notice: {e}")

    return DEFAULT_BRICS_JV_PLANS

# ==============================================================================
# 5. INCOMING COLLABORATIVE REQUESTS FROM OTHER BRICS COUNTRIES
# ==============================================================================

DEFAULT_INCOMING_REQUESTS = [
    {
        "id": "INBOUND-CN-2026-01",
        "origin_country": "China",
        "origin_flag": "🇨🇳",
        "origin_ministry": "Ministry of Transport & National Development and Reform Commission (NDRC)",
        "contact_liaison": "Vice Minister Chen Wei (Dept of International Cooperation)",
        "project_title": "Maritime Silk Road Automated Deep-Sea Container Terminal & Smart Logistics Hub",
        "target_location": "Gujarat / Mumbai Maritime Corridor",
        "proposed_capex": "₹8,400 Crore ($1.0 Billion USD)",
        "cooperation_model": "50:50 Sovereign Equity Joint Venture with automated 5G crane telemetry",
        "summary": "China proposes to co-finance and build a fully automated 4.2M TEU smart container terminal with robotic logistics cranes to cut vessel turnaround time from 38 hours to 11 hours.",
        "status": "Pending Central Government Decision",
        "date_received": "2026-09-02",
        "diplomatic_priority": "High / Tier-1"
    },
    {
        "id": "INBOUND-BR-2026-02",
        "origin_country": "Brazil",
        "origin_flag": "🇧🇷",
        "origin_ministry": "Ministério de Minas e Energia (MME) & Agência Espacial Brasileira (AEB)",
        "contact_liaison": "Secretary Luciana Guimarães (Energy Transition Directorate)",
        "project_title": "Amazonian-Deccan Satellite Hydrological Telemetry & Floating Solar Grid",
        "target_location": "Narmada & Yamuna River Basins (India) / Tietê Basin (Brazil)",
        "proposed_capex": "₹4,600 Crore ($550 Million USD)",
        "cooperation_model": "Cross-hemisphere climate satellite data exchange & 500MW floating solar EPC",
        "summary": "Brazil proposes a reciprocal joint space-earth sensor network to predict flash floods 48 hours in advance and deploy floating solar arrays on municipal reservoir surfaces.",
        "status": "Under Bilateral Assessment",
        "date_received": "2026-08-29",
        "diplomatic_priority": "Strategic / Environmental"
    },
    {
        "id": "INBOUND-ZA-2026-03",
        "origin_country": "South Africa",
        "origin_flag": "🇿🇦",
        "origin_ministry": "Department of Mineral Resources and Energy (DMRE)",
        "contact_liaison": "Director-General Jacob Dlamini (Clean Mineral Supply Chains)",
        "project_title": "Sovereign Green Hydrogen Electrolyzer Manufacturing Corridor",
        "target_location": "Coega Special Economic Zone / Kochi Port SEZ",
        "proposed_capex": "₹6,200 Crore ($750 Million USD)",
        "cooperation_model": "Shared intellectual property & joint NDB concessionary debt financing",
        "summary": "South Africa requests partnership to establish dual giga-factories for proton exchange membrane (PEM) electrolyzers utilizing South African iridium and Indian engineering talent.",
        "status": "Accepted for Working Group Review",
        "date_received": "2026-08-22",
        "diplomatic_priority": "Priority Energy Transition"
    },
    {
        "id": "INBOUND-RU-2026-04",
        "origin_country": "Russia",
        "origin_flag": "🇷🇺",
        "origin_ministry": "Ministry of Transport & Russian Railways (RZD)",
        "contact_liaison": "Deputy Minister Alexander Popov (INSTC Working Group)",
        "project_title": "International North-South Transport Corridor (INSTC) Cryogenic Rail Terminal",
        "target_location": "Bandar Abbas - Mumbai - Delhi Freight Spine",
        "proposed_capex": "₹9,800 Crore ($1.2 Billion USD)",
        "cooperation_model": "Multi-modal transit consortium with guaranteed 14-day delivery timeframe",
        "summary": "Russia requests formal bilateral sanction to construct specialized temperature-controlled intermodal rail freight terminals to expedite fertilizer and pharmaceutical cargo.",
        "status": "Under Diplomatic Review",
        "date_received": "2026-09-04",
        "diplomatic_priority": "Tier-1 Trade & Logistics"
    },
    {
        "id": "INBOUND-UAE-2026-05",
        "origin_country": "United Arab Emirates",
        "origin_flag": "🇦🇪",
        "origin_ministry": "Ministry of Energy and Infrastructure & Masdar Clean Energy",
        "contact_liaison": "Undersecretary H.E. Sharif Al Olama",
        "project_title": "Solar-Powered High-Recovery Seawater Desalination Master Plant",
        "target_location": "Coastal Gujarat & Tamil Nadu Municipalities",
        "proposed_capex": "₹7,200 Crore ($870 Million USD)",
        "cooperation_model": "Build-Own-Operate-Transfer (BOOT) with Masdar 60% equity backing",
        "summary": "UAE proposes to build a 200 MLD energy-neutral sea desalination plant using high-efficiency reverse osmosis powered by a dedicated 300MW coastal solar park.",
        "status": "Pending Central Government Decision",
        "date_received": "2026-09-05",
        "diplomatic_priority": "High / Water Security"
    }
]

def init_brics_incoming_requests():
    """Initializes incoming requests store if absent."""
    if not os.path.exists(BRICS_INCOMING_FILE):
        with open(BRICS_INCOMING_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_INCOMING_REQUESTS, f, indent=2, ensure_ascii=False)

init_brics_incoming_requests()

def get_brics_incoming_requests():
    """Retrieves incoming requests from partner BRICS nations."""
    init_brics_incoming_requests()
    try:
        with open(BRICS_INCOMING_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return list(DEFAULT_INCOMING_REQUESTS)

def respond_to_brics_request(request_id, response_action, notes=""):
    """
    Central Official responds to an inbound BRICS request:
    - 'accept': Sanction and move to Bilateral Working Group
    - 'negotiate': Request Bilateral Dialogue & Terms Revision Scheduled
    - 'review': Mark under Formal Inter-Ministerial Review
    """
    requests = get_brics_incoming_requests()
    target = None

    for r in requests:
        if r.get("id") == request_id:
            if response_action == "accept":
                r["status"] = "Sanctioned for Bilateral Working Group"
            elif response_action == "negotiate":
                r["status"] = "Bilateral Dialogue & Terms Revision Scheduled"
            else:
                r["status"] = "Under Formal Inter-Ministerial Review"
            if notes:
                r["central_response_notes"] = notes
            r["response_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            target = r
            break

    if target:
        with open(BRICS_INCOMING_FILE, "w", encoding="utf-8") as f:
            json.dump(requests, f, indent=2, ensure_ascii=False)
        return True, target

    return False, None
