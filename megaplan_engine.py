import os
import json
from brics_context import get_active_brics_node, get_brics_node, INFRASTRUCTURE_SECTORS
from demands_engine import get_all_demands
from api_client import get_all_complaints
from gemini_helper import call_gemini_with_fallback

# ==============================================================================
# GOVERNMENT AI MEGA-PLANNING & MASTER INFRASTRUCTURE SYNTHESIZER
# ==============================================================================

DEFAULT_MEGA_PLANS = {
    "india": [
        {
            "id": "MEGA-IN-01",
            "title": "North-East Delhi 50 MGD Deep Stormwater Drainage Canal & Waste Treatment Mega-Plant",
            "category": "Stormwater Drainage & Monsoon Floods",
            "ward": "Ward 35 - Seelampur / North-East",
            "svg_key": "drainage",
            "color": "#0284c7",
            "estimated_capex": "₹920 Crore",
            "funding_framework": "PM Gati Shakti National Master Plan",
            "timeline": "24 Months",
            "citizen_backing": "6,540 Community Upvotes & 1,420 Geo-Complaints",
            "demographic_impact": "Protects 3.9 Million residents across high-density flood basin",
            "justification": "Aggregated telemetry demonstrates chronic monsoon submergence. Existing municipal pumps waste ₹14 Cr annually in reactive diesel pumping without solving root-cause runoff capacity.",
            "policy_directive": "Cabinet Sanction: Reallocate ₹450 Cr from surplus Central Commercial beautification budget + ₹470 Cr from Gati Shakti Urban Flood Mitigation Grant."
        },
        {
            "id": "MEGA-IN-02",
            "title": "Outer Ring Road 6-Lane Elevated Arterial Bypass & Phase-IV Metro Feeder Interchange",
            "category": "Roads, Bridges & Arterial Corridors",
            "ward": "Ward 12 - Pitampura / Outer Ring Road",
            "svg_key": "roads",
            "color": "#f59e0b",
            "estimated_capex": "₹1,450 Crore",
            "funding_framework": "National Highways Authority & DMRC Partnership",
            "timeline": "30 Months",
            "citizen_backing": "4,821 Community Upvotes & 890 Commuter Petitions",
            "demographic_impact": "180,000 daily commuters; eliminates 45-min bottleneck",
            "justification": "Surface corridor operates at 240% design vehicular capacity. Pothole and road defect volume reflects pavement shearing from heavy freight and gridlocked transit.",
            "policy_directive": "Cabinet Sanction: Accelerate Phase-IV elevated viaduct construction with multi-modal electric feeder bus loops at Pitampura hub."
        },
        {
            "id": "MEGA-IN-03",
            "title": "220kV Gas-Insulated High-Voltage Substation & 150MW Industrial Solar Microgrid",
            "category": "Electricity, Streetlights & Grid",
            "ward": "Ward 28 - Okhla Industrial Basin",
            "svg_key": "electricity",
            "color": "#eab308",
            "estimated_capex": "₹780 Crore",
            "funding_framework": "National Power Grid Resilience Scheme",
            "timeline": "18 Months",
            "citizen_backing": "3,190 Industrial Upvotes & 620 Grid Failure Alerts",
            "demographic_impact": "1,200 industrial units & 3.4M regional population",
            "justification": "Legacy distribution infrastructure suffers 18% technical line losses and recurrent transformer explosions. Industrial manufacturing loses ₹120 Cr annually in idle generator diesel costs.",
            "policy_directive": "Cabinet Sanction: Commission turnkey EPC contract for compact 220kV GIS substation with automated SCADA fault isolation."
        },
        {
            "id": "MEGA-IN-04",
            "title": "300-Bed Secondary Multi-Specialty Government Hospital & Emergency Trauma Center",
            "category": "Public Health, Clinics & Vector Control",
            "ward": "Ward 19 - Rohini Sector 14",
            "svg_key": "health",
            "color": "#f43f5e",
            "estimated_capex": "₹480 Crore",
            "funding_framework": "Pradhan Mantri Ayushman Bharat Health Infrastructure Mission",
            "timeline": "20 Months",
            "citizen_backing": "5,210 Community Upvotes & 410 Health Petitions",
            "demographic_impact": "650,000 residents within 15-min emergency response radius",
            "justification": "Currently zero government tertiary trauma facilities within 20 km radius. Citizen petitions indicate fatal delays during critical golden-hour medical emergencies.",
            "policy_directive": "Cabinet Sanction: Approve land parcel transfer and fast-track capital expenditure allocation under National Health Mission."
        }
    ],
    "brazil": [
        {
            "id": "MEGA-BR-01",
            "title": "Extensão do Corredor BRT Metropolitano e Interligação Metroferroviária Linha 15",
            "category": "Roads, Bridges & Arterial Corridors",
            "ward": "Zona Leste - Itaquera / São Mateus",
            "svg_key": "roads",
            "color": "#f59e0b",
            "estimated_capex": "R$ 1.150 Milhões",
            "funding_framework": "PAC Mobilidade Urbana & Governo do Estado de SP",
            "timeline": "28 Meses",
            "citizen_backing": "5.120 Votos da Comunidade e 940 Demandas Populares",
            "demographic_impact": "250.000 passageiros/dia reduzindo tempo de trânsito em 50%",
            "justification": "A Zona Leste possui a maior taxa de viagens pendulares da América Latina, sobrecarregando o sistema radial e isolando trabalhadores periféricos.",
            "policy_directive": "Diretiva Executiva: Sanção de financiamento via BNDES e priorização imediata no PAC."
        },
        {
            "id": "MEGA-BR-02",
            "title": "Construção de Mega-Piscinão de Contenção de Cheias e Drenagem da Bacia do Rio Pinheiros",
            "category": "Stormwater Drainage & Monsoon Floods",
            "ward": "Zona Sul - Santo Amaro / Grajaú",
            "svg_key": "drainage",
            "color": "#0284c7",
            "estimated_capex": "R$ 840 Milhões",
            "funding_framework": "Marco Legal do Saneamento Básico & Sabesp",
            "timeline": "22 Meses",
            "citizen_backing": "4.310 Votos Populares e 1.120 Alertas de Alagamento",
            "demographic_impact": "Proteção direta para 400.000 moradores de áreas de risco",
            "justification": "Inundações sazonais causam prejuízos de mais de R$ 60 milhões ao comércio e habitações populares a cada tempestade de verão.",
            "policy_directive": "Diretiva Executiva: Licitação urgente de reservatório subterrâneo com capacidade de 500.000 m³."
        },
        {
            "id": "MEGA-BR-03",
            "title": "Usina Solar Fotovoltaica Metropolitana e Subestação de Alta Tensão de 200MW",
            "category": "Electricity, Streetlights & Grid",
            "ward": "Zona Leste - São Mateus / Polo Industrial",
            "svg_key": "electricity",
            "color": "#eab308",
            "estimated_capex": "R$ 980 Milhões",
            "funding_framework": "Plano de Transição Energética & Eletrobras",
            "timeline": "18 Meses",
            "citizen_backing": "3.840 Votos Comunitários & 730 Alertas de Apagão",
            "demographic_impact": "Abastecimento limpo e ininterrupto para 600.000 habitantes",
            "justification": "A rede elétrica periférica sofre com sobrecargas crônicas e oscilações severas que paralisam serviços essenciais e postos de saúde.",
            "policy_directive": "Diretiva Executiva: Sanção de projeto prioritário pelo Ministério de Minas e Energia com isenção tarifária."
        },
        {
            "id": "MEGA-BR-04",
            "title": "Hospital Geral Regional de Urgência e Centro de Atenção à Saúde Materna",
            "category": "Public Health, Clinics & Vector Control",
            "ward": "Zona Sul - Grajaú / Parelheiros",
            "svg_key": "health",
            "color": "#f43f5e",
            "estimated_capex": "R$ 620 Milhões",
            "funding_framework": "SUS & Ministério da Saúde Brasil",
            "timeline": "24 Meses",
            "citizen_backing": "4.890 Votos Populares e 610 Petições de Saúde",
            "demographic_impact": "Atendimento direto para 500.000 moradores do extremo sul",
            "justification": "A distância média até um pronto-socorro com UTI neonatal ultrapassa 18 km na zona sul, gerando riscos críticos de mortalidade evitável.",
            "policy_directive": "Diretiva Executiva: Liberação de emenda parlamentar e início imediato das obras estruturais."
        }
    ],
    "south_africa": [
        {
            "id": "MEGA-ZA-01",
            "title": "Dual-Carriageway Arterial Bridge & Elevated Stormwater Viaduct over Jukskei River",
            "category": "Roads, Bridges & Arterial Corridors",
            "ward": "Region A - Diepsloot / Midrand Corridor",
            "svg_key": "roads",
            "color": "#f59e0b",
            "estimated_capex": "R 420 Million",
            "funding_framework": "Municipal Infrastructure Grant (MIG) & Gauteng DRPW",
            "timeline": "16 Months",
            "citizen_backing": "3,890 Citizen Upvotes & 780 Emergency Petitions",
            "demographic_impact": "140,000 residents; safe permanent corridor for ambulances & buses",
            "justification": "Low-level informal culvert is completely submerged in summer flash floods, cutting off emergency medical response and school transit.",
            "policy_directive": "Ministerial Directive: Fast-track capital grant allocation from Provincial Infrastructure Fund."
        },
        {
            "id": "MEGA-ZA-02",
            "title": "Soweto Bulk Reticulation Overhaul & 40 MVA Electrical Substation Reinforcement",
            "category": "Electricity, Streetlights & Grid",
            "ward": "Region D - Soweto / Diepkloof",
            "svg_key": "electricity",
            "color": "#eab308",
            "estimated_capex": "R 750 Million",
            "funding_framework": "Eskom & City Power Infrastructure Modernization",
            "timeline": "20 Months",
            "citizen_backing": "4,670 Community Votes & 1,350 Blackout Reports",
            "demographic_impact": "850,000 residents guaranteed reliable power and water security",
            "justification": "Systemic transformer overloads trigger rolling multi-day blackouts and water pumping failures across dense settlements.",
            "policy_directive": "Ministerial Directive: Sanction priority equipment procurement and dedicated feeder line ring fencing."
        },
        {
            "id": "MEGA-ZA-03",
            "title": "100MW Solar Photovoltaic & Battery Energy Storage (BESS) Sovereign Power Plant",
            "category": "Electricity, Streetlights & Grid",
            "ward": "Region G - Ennerdale / Orange Farm",
            "svg_key": "electricity",
            "color": "#eab308",
            "estimated_capex": "R 920 Million",
            "funding_framework": "Just Energy Transition Investment Plan (JET-IP)",
            "timeline": "18 Months",
            "citizen_backing": "5,140 Community Votes & 920 Grid Failure Alerts",
            "demographic_impact": "Shields 450,000 township residents from national loadshedding stages",
            "justification": "Severe loadshedding cripples township micro-enterprises and basic municipal water booster pumps for up to 10 hours daily.",
            "policy_directive": "Cabinet Sanction: Designate as Strategic Integrated Project (SIP) with immediate environmental clearance."
        },
        {
            "id": "MEGA-ZA-04",
            "title": "Diepsloot Regional Trauma Hospital & Maternal Emergency Healthcare Complex",
            "category": "Public Health, Clinics & Vector Control",
            "ward": "Region A - Diepsloot West",
            "svg_key": "health",
            "color": "#f43f5e",
            "estimated_capex": "R 480 Million",
            "funding_framework": "National Health Insurance (NHI) Capital Grant",
            "timeline": "22 Months",
            "citizen_backing": "4,950 Community Petitions & 810 Health Grievances",
            "demographic_impact": "Serves 320,000 citizens eliminating 25km transit barrier",
            "justification": "Existing local clinics lack emergency overnight surgical beds, forcing severe trauma and maternal cases to travel to Helen Joseph Hospital.",
            "policy_directive": "Ministerial Directive: Sanction fast-track site transfer and phased modular construction under NHI infrastructure branch."
        }
    ]
}

def enrich_plan_metadata(plan):
    """Enriches an AI-generated plan with sector visual metadata (color & svg_key)."""
    cat = (plan.get("category") or "").lower()
    matched = None
    for s in INFRASTRUCTURE_SECTORS:
        s_name = s["name"].lower()
        if s_name in cat or cat in s_name or any(w in cat for w in s["id"].split("_")):
            matched = s
            break

    if matched:
        plan["svg_key"] = matched.get("svg_key", "road")
        plan["color"] = matched.get("color", "#f59e0b")
    else:
        # Defaults based on keyword
        if "water" in cat or "drain" in cat or "flood" in cat:
            plan["svg_key"] = "drainage"
            plan["color"] = "#0284c7"
        elif "power" in cat or "solar" in cat or "electr" in cat:
            plan["svg_key"] = "electricity"
            plan["color"] = "#eab308"
        elif "health" in cat or "hospital" in cat or "clinic" in cat:
            plan["svg_key"] = "health"
            plan["color"] = "#f43f5e"
        elif "transit" in cat or "bus" in cat or "metro" in cat:
            plan["svg_key"] = "transit"
            plan["color"] = "#6366f1"
        else:
            plan["svg_key"] = "roads"
            plan["color"] = "#f59e0b"

    return plan

def generate_ai_mega_plans(country_code="IN"):
    """
    Synthesizes big infrastructure plans by combining citizen complaints,
    top-upvoted community demands, and demographic census data using Gemini 2.5.
    """
    c_code = str(country_code).upper().strip()
    node_key = "india" if c_code in ["IN", "INDIA"] else ("brazil" if c_code in ["BR", "BRAZIL"] else "south_africa")
    node = get_brics_node(node_key)
    
    complaints = get_all_complaints()
    demands = get_all_demands(country_code=c_code)
    top_demands = demands[:5]

    prompt = f"""
You are the Chief AI Infrastructure Planner for {node.get('country')} ({node.get('jurisdiction')}).
Analyze the following citizen inputs and national parameters:
- Total National CapEx Budget: {node.get('currency')} {node.get('total_capex_budget')}
- Total Population: {node.get('total_population')} (Avg Density: {node.get('avg_density')})
- Active Citizen Complaints: {len(complaints)} records
- Top Community Demands with Citizen Upvotes:
"""
    for d in top_demands:
        prompt += f"\n  * [{d.get('sector')}] '{d.get('title')}' in {d.get('ward')} (Upvotes: {d.get('upvotes')}, Est. Budget: {d.get('estimated_budget')})"

    prompt += f"""
Synthesize 3-4 High-Impact Capital Infrastructure Mega-Projects (e.g. Highways/Expressways, Power Plants/Substations, Deep Drainage Canals, Hospitals) that national policymakers should sanction immediately.
Return ONLY valid JSON formatted as a list of objects with keys:
"id", "title", "category", "ward", "estimated_capex", "funding_framework", "timeline", "citizen_backing", "demographic_impact", "justification", "policy_directive"
Do NOT include emoji icons.
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
                return [enrich_plan_metadata(p) for p in parsed]
    except Exception:
        pass

    defaults = DEFAULT_MEGA_PLANS.get(node_key, DEFAULT_MEGA_PLANS["india"])
    return [enrich_plan_metadata(dict(p)) for p in defaults]
