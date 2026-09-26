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
            "title": "100MW Solar PhotovoltaIC & Battery Energy Storage (BESS) Sovereign Power Plant",
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
    ],
    "china": [
        {
            "id": "MEGA-CN-01",
            "title": "Shanghai Deep Stormwater Interceptor Tunnel & Sponge City Ecological Network",
            "category": "Stormwater Drainage & Monsoon Floods",
            "ward": "Yangpu District - Wujiaochang / Riverside Tech Belt",
            "svg_key": "drainage",
            "color": "#0284c7",
            "estimated_capex": "¥ 2.8 Billion",
            "funding_framework": "14th Five-Year Urban Resilience & Sponge City Plan",
            "timeline": "24 Months",
            "citizen_backing": "6,240 Tech Worker Votes & 1,180 Drainage Petitions",
            "demographic_impact": "Protects 1.8M residents and key tech parks from typhoons",
            "justification": "Typhoon storm surges inundate low-lying arterial corridors, impeding high-tech manufacturing and commercial logistics.",
            "policy_directive": "Municipal Decree: Authorize deep sub-surface boring machines and connect to Yangtze hydrological SCADA."
        },
        {
            "id": "MEGA-CN-02",
            "title": "Lujiazui to Pudong Airport Magnetic Levitation & Autonomous Sky-Pod Feeder",
            "category": "Public Transport & Transit Hubs",
            "ward": "Pudong New Area - Lujiazui / Zhangjiang Hi-Tech",
            "svg_key": "transit",
            "color": "#6366f1",
            "estimated_capex": "¥ 4.5 Billion",
            "funding_framework": "National Smart Megacity Mobility Initiative",
            "timeline": "30 Months",
            "citizen_backing": "5,890 Commuter Votes & 840 Transit Proposals",
            "demographic_impact": "Serves 400,000 daily passengers reducing airport transit to 18 mins",
            "justification": "Current highway corridors operate at 190% design capacity during peak trade hours, causing multi-hour congestion.",
            "policy_directive": "Cabinet Directive: Expedite right-of-way clearance and approve high-speed automated feeder spurs."
        },
        {
            "id": "MEGA-CN-03",
            "title": "500kV Ultra-High-Voltage Smart Substation & Distributed Hydrogen Storage",
            "category": "Electricity, Streetlights & Grid",
            "ward": "Huangpu District - East Nanjing Road / Bund",
            "svg_key": "electricity",
            "color": "#eab308",
            "estimated_capex": "¥ 3.2 Billion",
            "funding_framework": "State Grid Urban Decarbonization Scheme",
            "timeline": "18 Months",
            "citizen_backing": "4,120 Commercial Votes & 620 Grid Alerts",
            "demographic_impact": "Guarantees 99.999% power reliability for financial core & 2.5M regional citizens",
            "justification": "Extreme summer peak loads threaten financial server centers and urban mass transit grids.",
            "policy_directive": "State Council Directive: Deploy solid-state battery buffers and underground gas-insulated substation."
        }
    ],
    "egypt": [
        {
            "id": "MEGA-EG-01",
            "title": "Cairo Ring Road Multi-Tier Elevated Expressway & Monorail Intermodal Feeder",
            "category": "Roads, Bridges & Arterial Corridors",
            "ward": "Nasr City - Abbas El Akkad / Smart Transit Corridor",
            "svg_key": "roads",
            "color": "#f59e0b",
            "estimated_capex": "E£ 1.8 Billion",
            "funding_framework": "Egypt Vision 2030 & Ministry of Transport Infrastructure Fund",
            "timeline": "20 Months",
            "citizen_backing": "5,410 Citizen Upvotes & 980 Pothole Grievances",
            "demographic_impact": "3.2 Million daily commuters; halves transit time across Cairo spine",
            "justification": "Critical bottleneck connecting East Cairo and Giza causes massive fuel wastage and severe particulate air pollution.",
            "policy_directive": "Presidential Decree: Allocate priority funding from National Arterial Corridor Grant."
        },
        {
            "id": "MEGA-EG-02",
            "title": "Giza Basin Desalinated Water Booster Pipeline & Smart Telemetry Network",
            "category": "Water Supply & Pipeline Leakage",
            "ward": "Giza - Al Haram / Faisal Residential Basin",
            "svg_key": "water",
            "color": "#06b6d4",
            "estimated_capex": "E£ 1.4 Billion",
            "funding_framework": "Decent Life (Haya Karima) National Infrastructure Initiative",
            "timeline": "16 Months",
            "citizen_backing": "6,120 Resident Petitions & 1,450 Water Pressure Alerts",
            "demographic_impact": "4.1 Million residents guaranteed potable drinking water pressure",
            "justification": "Aged cast-iron mains suffer 35% non-revenue water loss and acute low pressure during summer peak heatwaves.",
            "policy_directive": "Cabinet Sanction: Replace trunk pipelines with ductile iron mains with real-time acoustic leak detection."
        },
        {
            "id": "MEGA-EG-03",
            "title": "Greater Cairo 200MW Desert Solar Microgrid & Substation Undergrounding",
            "category": "Electricity, Streetlights & Grid",
            "ward": "Qasr El Nil - Tahrir Square / Downtown",
            "svg_key": "electricity",
            "color": "#eab308",
            "estimated_capex": "E£ 1.2 Billion",
            "funding_framework": "Ministry of Electricity Renewable Transition Program",
            "timeline": "14 Months",
            "citizen_backing": "4,340 Downtown Merchant Votes & 790 Outage Grievances",
            "demographic_impact": "Stabilizes historic core and protects 820,000 residents from rolling cuts",
            "justification": "Historic architectural cabling experiences thermal overloads during 45°C summer peaks.",
            "policy_directive": "Ministerial Directive: Transfer municipal desert land parcel and fast-track grid interconnection."
        }
    ],
    "ethiopia": [
        {
            "id": "MEGA-ET-01",
            "title": "Addis Ababa Corridor Arterial Transit Overhaul & Pedestrian Skyway Network",
            "category": "Roads, Bridges & Arterial Corridors",
            "ward": "Bole Sub-City - Airport Corridor / Rwanda Bridge",
            "svg_key": "roads",
            "color": "#f59e0b",
            "estimated_capex": "Br 850 Million",
            "funding_framework": "Addis Ababa Corridor Development Project",
            "timeline": "12 Months",
            "citizen_backing": "4,780 Citizen Votes & 890 Road Safety Petitions",
            "demographic_impact": "890,000 residents; safe pedestrian crossings and asphalt resurfacing",
            "justification": "Rapid urbanization has overwhelmed arterial road capacity, creating dangerous pedestrian conditions and commuter delays.",
            "policy_directive": "Mayoral Decree: Implement modern protected pedestrian walkways, bicycle lanes, and resurfaced asphalt."
        },
        {
            "id": "MEGA-ET-02",
            "title": "Legedadi-Dire Municipal Water Reticulation & Clean Pressure Booster Network",
            "category": "Water Supply & Pipeline Leakage",
            "ward": "Arada Sub-City - Piazza / Heritage Civic Sector",
            "svg_key": "water",
            "color": "#06b6d4",
            "estimated_capex": "Br 620 Million",
            "funding_framework": "Ethiopian Water Sector Modernization Program",
            "timeline": "18 Months",
            "citizen_backing": "5,340 Resident Petitions & 1,120 Scarcity Grievances",
            "demographic_impact": "560,000 citizens guaranteed safe daily potable piped water",
            "justification": "Informal settlement growth and aged reservoir conduits leave central neighborhoods reliant on costly water tankers.",
            "policy_directive": "Cabinet Directive: Deploy modern booster pumps and digital pressure regulation valves across Piazza."
        },
        {
            "id": "MEGA-ET-03",
            "title": "Meskel Square High-Capacity Substation Modernization & LED Streetlight Grid",
            "category": "Electricity, Streetlights & Grid",
            "ward": "Kirkos Sub-City - Meskel Square / Kazanchis",
            "svg_key": "electricity",
            "color": "#eab308",
            "estimated_capex": "Br 480 Million",
            "funding_framework": "Ethiopian Electric Utility (EEU) Urban Grid Renewal",
            "timeline": "14 Months",
            "citizen_backing": "3,890 Business Votes & 670 Power Failure Reports",
            "demographic_impact": "480,000 residents; illuminates key civic gathering spaces and transit hubs",
            "justification": "Recurrent transformer blowouts and unlit arterial corridors cause commercial paralysis and safety hazards at night.",
            "policy_directive": "Ministerial Directive: Sanction turnkey GIS substation replacement and smart LED street lighting."
        }
    ],
    "indonesia": [
        {
            "id": "MEGA-ID-01",
            "title": "Jakarta Coastal Sea Dike (NCICD) & Automated Retention Pumping Station",
            "category": "Stormwater Drainage & Monsoon Floods",
            "ward": "North Jakarta - Pluit / Tanjung Priok Port",
            "svg_key": "drainage",
            "color": "#0284c7",
            "estimated_capex": "Rp 1.8 Trillion",
            "funding_framework": "National Strategic Project (PSN) Coastal Defense Plan",
            "timeline": "24 Months",
            "citizen_backing": "6,780 Community Votes & 1,540 Flood Disaster Warnings",
            "demographic_impact": "1.8 Million residents shielded from tidal flooding and sea level rise",
            "justification": "Pluit and coastal neighborhoods face chronic land subsidence, with monsoon king tides submerging residential homes up to 1.5m.",
            "policy_directive": "Governor Decree: Fast-track sea wall height enhancement and deploy four 50 m³/s automated electric pumps."
        },
        {
            "id": "MEGA-ID-02",
            "title": "TransJakarta Elevated Busway Extension & MRT Intermodal Feeder Viaduct",
            "category": "Roads, Bridges & Arterial Corridors",
            "ward": "East Jakarta - Jatinegara / Cawang Interchange",
            "svg_key": "roads",
            "color": "#f59e0b",
            "estimated_capex": "Rp 1.4 Trillion",
            "funding_framework": "DKI Jakarta Regional Infrastructure Budget (APBD)",
            "timeline": "18 Months",
            "citizen_backing": "5,120 Commuter Votes & 920 Pothole/Traffic Petitions",
            "demographic_impact": "600,000 daily transit users; cuts bottleneck transit time by 40 minutes",
            "justification": "Cawang intersection is the most congested transit choke-point in Southeast Asia, with pavement shearing from heavy freight.",
            "policy_directive": "Executive Action: Commission elevated dual-lane dedicated busway with grade-separated pedestrian skywalks."
        },
        {
            "id": "MEGA-ID-03",
            "title": "150kV Gas-Insulated Substation & Micro-Solar Industrial Resilience Hub",
            "category": "Electricity, Streetlights & Grid",
            "ward": "Central Jakarta - Gambir / Thamrin CBD",
            "svg_key": "electricity",
            "color": "#eab308",
            "estimated_capex": "Rp 950 Billion",
            "funding_framework": "PLN Green Energy Transition & Urban Grid Scheme",
            "timeline": "16 Months",
            "citizen_backing": "4,210 Enterprise Votes & 680 Power Fluctuations",
            "demographic_impact": "920,000 residents and key national government ministries",
            "justification": "Underground power distribution in flood-prone central wards requires watertight gas-insulated transformation.",
            "policy_directive": "Ministerial Directive: Sanction flood-proof compact GIS substation with automated SCADA isolation."
        }
    ],
    "iran": [
        {
            "id": "MEGA-IR-01",
            "title": "Tehran Metro Line 7 Linkages & Zero-Emission Electric Trolleybus Fleet",
            "category": "Public Transport & Transit Hubs",
            "ward": "District 2 - Sadeghiyeh / Shahrak-e Gharb",
            "svg_key": "transit",
            "color": "#6366f1",
            "estimated_capex": "﷼ 1.6 Trillion",
            "funding_framework": "Tehran Municipality Urban Transport Modernization Fund",
            "timeline": "22 Months",
            "citizen_backing": "5,320 Commuter Votes & 950 Smog / Air Quality Petitions",
            "demographic_impact": "450,000 daily passengers; takes 80,000 private vehicles off the road",
            "justification": "Tehran basin suffers severe seasonal temperature inversions, trapping heavy vehicle emissions against the Alborz mountains.",
            "policy_directive": "Mayoral Decree: Authorize 200 high-capacity electric articulated buses and dedicated right-of-way spurs."
        },
        {
            "id": "MEGA-IR-02",
            "title": "Latyan-to-Rey Deep Aqueduct Pipeline & Potable Water Filtration Overhaul",
            "category": "Water Supply & Pipeline Leakage",
            "ward": "District 20 - Shahr-e Rey Southern Basin",
            "svg_key": "water",
            "color": "#06b6d4",
            "estimated_capex": "﷼ 1.2 Trillion",
            "funding_framework": "National Water & Wastewater Engineering Company Plan",
            "timeline": "18 Months",
            "citizen_backing": "4,890 Resident Petitions & 1,140 Salinity Grievances",
            "demographic_impact": "1.45 Million southern residents guaranteed high-quality drinking water",
            "justification": "Groundwater depletion in southern Tehran has degraded drinking water quality, requiring mountain aqueduct interconnections.",
            "policy_directive": "Ministry of Energy Directive: Expedite 32 km pipeline construction with advanced multi-stage reverse osmosis."
        },
        {
            "id": "MEGA-IR-03",
            "title": "Historic Bazaar Underground Cable Fire-Safety & Smart SCADA Substation",
            "category": "Electricity, Streetlights & Grid",
            "ward": "District 12 - Grand Bazaar / Baharestan",
            "svg_key": "electricity",
            "color": "#eab308",
            "estimated_capex": "﷼ 890 Billion",
            "funding_framework": "National Cultural Heritage & Power Infrastructure Program",
            "timeline": "14 Months",
            "citizen_backing": "4,450 Merchant Votes & 780 Electrical Hazard Alerts",
            "demographic_impact": "Protects 680,000 citizens and irreplaceable historic cultural landmark",
            "justification": "Aged overhead wiring in the covered bazaar poses acute short-circuit fire risks and causes frequent blackouts.",
            "policy_directive": "Government Decree: Complete subterranean fireproof cable conduit system with smart circuit breaker telemetry."
        }
    ],
    "russia": [
        {
            "id": "MEGA-RU-01",
            "title": "Moscow Central Diameters (MCD-5) Underground Rail Transit Cross-City Tunnel",
            "category": "Public Transport & Transit Hubs",
            "ward": "Central Administrative Okrug - Tverskoy / Arbat",
            "svg_key": "transit",
            "color": "#6366f1",
            "estimated_capex": "₽ 3.8 Billion",
            "funding_framework": "Moscow Transport Master Plan & RZD Sovereign Rail Partnership",
            "timeline": "28 Months",
            "citizen_backing": "6,890 Commuter Votes & 1,120 Metro Overcrowding Reports",
            "demographic_impact": "1.2 Million daily passengers; connects north and south radial rail lines",
            "justification": "Surface passenger transfers bottleneck existing Ring and Circle lines, causing severe platform overcrowding at peak hours.",
            "policy_directive": "Government Sanction: Authorize deep tunnel boring under central Moscow with high-speed automated trains."
        },
        {
            "id": "MEGA-RU-02",
            "title": "Moskva River Watershed Flood Protection & Ecological Wastewater Mega-Plant",
            "category": "Stormwater Drainage & Monsoon Floods",
            "ward": "South-Eastern Okrug - Lyublino / Maryino",
            "svg_key": "drainage",
            "color": "#0284c7",
            "estimated_capex": "₽ 2.6 Billion",
            "funding_framework": "Mosvodokanal Clean Watershed National Project",
            "timeline": "20 Months",
            "citizen_backing": "5,120 Citizen Petitions & 870 River Odor Grievances",
            "demographic_impact": "Protects 1.5M residents from heavy snowmelt flooding and river contamination",
            "justification": "Spring snowmelt runoff overwhelms legacy stormwater drains, discharging untreated street effluent into the river.",
            "policy_directive": "Mayor Decree: Commission automated membrane filtration plant with deep gravity interceptor sewers."
        },
        {
            "id": "MEGA-RU-03",
            "title": "Subterranean Cryogenic District Heating Overhaul & 220kV Smart Substation",
            "category": "Electricity, Streetlights & Grid",
            "ward": "Northern Administrative Okrug - Sokol / Aeroport",
            "svg_key": "electricity",
            "color": "#eab308",
            "estimated_capex": "₽ 2.1 Billion",
            "funding_framework": "Mosenergo Winter Resilience & Modernization Scheme",
            "timeline": "16 Months",
            "citizen_backing": "4,780 Resident Votes & 640 Heating Pipe Defect Alerts",
            "demographic_impact": "Guarantees uninterrupted sub-zero heating and power for 1.18M citizens",
            "justification": "Extreme winter temperatures (-25°C) cause pipe stress ruptures, risking catastrophic heat loss in high-density residential towers.",
            "policy_directive": "Executive Directive: Install pre-insulated telemetry pipelines with automated pressure sensor relays."
        }
    ],
    "saudi_arabia": [
        {
            "id": "MEGA-SA-01",
            "title": "Riyadh Ring Road Deep Underground Expressway & Autonomous Transit Viaduct",
            "category": "Roads, Bridges & Arterial Corridors",
            "ward": "Al Malaz - University & Government Ministries District",
            "svg_key": "roads",
            "color": "#f59e0b",
            "estimated_capex": "﷼ 4.2 Billion",
            "funding_framework": "Saudi Vision 2030 & Royal Commission for Riyadh City (RCRC)",
            "timeline": "26 Months",
            "citizen_backing": "5,980 Citizen Votes & 940 Pothole / Traffic Alerts",
            "demographic_impact": "1.4 Million daily commuters; eliminates central Riyadh 50-min bottlenecks",
            "justification": "Extreme summer asphalt thermal fatigue and vehicular density cause chronic delays across university and ministry corridors.",
            "policy_directive": "Royal Decree: Fast-track construction of climate-controlled subterranean transit bypass with heat-resistant asphalt."
        },
        {
            "id": "MEGA-SA-02",
            "title": "Wadi Hanifah Storm Runoff Retention & Strategic Desalinated Water Reservoirs",
            "category": "Water Supply & Pipeline Leakage",
            "ward": "Al Batha - Old Commercial & High-Density Center",
            "svg_key": "water",
            "color": "#06b6d4",
            "estimated_capex": "﷼ 3.5 Billion",
            "funding_framework": "Green Riyadh Initiative & National Water Company (NWC)",
            "timeline": "20 Months",
            "citizen_backing": "6,340 Merchant & Resident Votes & 1,210 Flash Flood Alerts",
            "demographic_impact": "1.85 Million citizens shielded from desert flash floods and water outages",
            "justification": "Desert convective flash storms flood low-lying commercial basins, while potable water reserves require 7-day emergency buffering.",
            "policy_directive": "Ministerial Directive: Construct 3 underground megawatt-pump reservoirs and interconnect with Ras Al Khair desal pipelines."
        },
        {
            "id": "MEGA-SA-03",
            "title": "Al Olaya District Cooling Smart Microgrid & 380kV Substation Modernization",
            "category": "Electricity, Streetlights & Grid",
            "ward": "Al Olaya - King Fahd Corridor / Central Financial Hub",
            "svg_key": "electricity",
            "color": "#eab308",
            "estimated_capex": "﷼ 2.9 Billion",
            "funding_framework": "Saudi Electricity Company (SEC) Sustainability Transition",
            "timeline": "18 Months",
            "citizen_backing": "4,620 Enterprise Votes & 680 Peak Cooling Alerts",
            "demographic_impact": "Guarantees 100% cooling and power continuity for 950,000 residents and businesses",
            "justification": "Air conditioning accounts for 70% of peak electricity demand in 50°C summer conditions, placing severe stress on legacy transformers.",
            "policy_directive": "Cabinet Sanction: Deploy centralized chilled-water district cooling networks and automated SCADA substations."
        }
    ],
    "united_arab_emirates": [
        {
            "id": "MEGA-AE-01",
            "title": "Deep Rain Stormwater Gravity Tunnel (Tasreef System) & Marine Outfall",
            "category": "Stormwater Drainage & Monsoon Floods",
            "ward": "Deira & Dubai Creek - Historic Maritime Commercial Hub",
            "svg_key": "drainage",
            "color": "#0284c7",
            "estimated_capex": "AED 3.9 Billion",
            "funding_framework": "Dubai Strategic Infrastructure Plan & Municipality Tasreef Project",
            "timeline": "24 Months",
            "citizen_backing": "7,120 Community Votes & 1,680 Flood Warnings",
            "demographic_impact": "1.45 Million residents and Dubai International Airport access corridor protected",
            "justification": "Unprecedented record rainfall events cause severe waterlogging, shutting down arterial trade and grounding aviation.",
            "policy_directive": "Executive Council Sanction: Deploy high-capacity deep gravity storm tunnel draining 20 million m³ water daily directly into the sea."
        },
        {
            "id": "MEGA-AE-02",
            "title": "Dubai Metro Blue Line Extension & Autonomous Sky-Pod Feeder Interchange",
            "category": "Public Transport & Transit Hubs",
            "ward": "Dubai South - Al Maktoum International & Logistics City",
            "svg_key": "transit",
            "color": "#6366f1",
            "estimated_capex": "AED 4.8 Billion",
            "funding_framework": "Dubai 2040 Urban Master Plan & RTA",
            "timeline": "30 Months",
            "citizen_backing": "5,840 Commuter Petitions & 820 Transit Upgrades",
            "demographic_impact": "320,000 daily passengers; connects aviation hub to Dubai Creek Harbour and Downtown",
            "justification": "Al Maktoum International expansion requires high-capacity rapid transit to handle projected 120M annual passenger throughput.",
            "policy_directive": "Crown Prince Directive: Fast-track construction of 30 km driverless track with 14 smart stations."
        },
        {
            "id": "MEGA-AE-03",
            "title": "300MW Solar Microgrid & Ultra-Fast Commercial EV Charging Super-Hubs",
            "category": "Electricity, Streetlights & Grid",
            "ward": "Downtown Dubai - Sheikh Zayed Road / DIFC Corridor",
            "svg_key": "electricity",
            "color": "#eab308",
            "estimated_capex": "AED 2.4 Billion",
            "funding_framework": "Dubai Clean Energy Strategy 2050 & DEWA",
            "timeline": "16 Months",
            "citizen_backing": "4,590 Enterprise Votes & 610 EV Charger Requests",
            "demographic_impact": "Supplies 100% clean power for Downtown municipal lighting and 620,000 citizens",
            "justification": "Rapid adoption of commercial electric delivery fleets and private EVs demands ultra-fast megawatt-charging stations.",
            "policy_directive": "DEWA Sanction: Deploy grid-tied battery storage and 50 liquid-cooled 400kW public fast-chargers."
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
    node = get_brics_node(c_code)
    node_key = node.get("id", "india")
    
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
