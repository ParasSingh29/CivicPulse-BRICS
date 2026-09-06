# ==============================================================================
# EXPANDED 10+ MUNICIPAL & PUBLIC WORKS SECTORS
# ==============================================================================

INFRASTRUCTURE_SECTORS = [
    {
        "id": "roads_transit",
        "name": "Roads, Bridges & Arterial Corridors",
        "icon": "🛣️",
        "svg_key": "roads",
        "color": "#f59e0b",
        "badge": "Transit Backbone",
        "description": "Expressways, flyovers, arterial road resurfacing, structural bridges & pedestrian skywalks"
    },
    {
        "id": "water_supply",
        "name": "Water Supply & Pipeline Leakage",
        "icon": "💧",
        "svg_key": "water",
        "color": "#06b6d4",
        "badge": "Potable Water",
        "description": "Clean drinking water distribution, high-pressure trunk mains, smart leak telemetry & pumping stations"
    },
    {
        "id": "electricity_grid",
        "name": "Electricity, Streetlights & Grid",
        "icon": "⚡",
        "svg_key": "electricity",
        "color": "#eab308",
        "badge": "Energy Infrastructure",
        "description": "High-voltage transmission substations, underground cabling, smart LED lighting & grid blackout prevention"
    },
    {
        "id": "waste_sanitation",
        "name": "Waste Management & Sanitation",
        "icon": "♻️",
        "svg_key": "waste",
        "color": "#10b981",
        "badge": "Circular Cleanliness",
        "description": "Automated material recovery, bio-methanation plants, toxic landfill remediation & daily door-to-door collection"
    },
    {
        "id": "public_transport",
        "name": "Public Transport & Transit Hubs",
        "icon": "🚌",
        "svg_key": "transit",
        "color": "#6366f1",
        "badge": "Mobility Corridors",
        "description": "Metro rail feeder routes, electric bus fleets, multi-modal passenger terminals & commuter shelters"
    },
    {
        "id": "stormwater_flood",
        "name": "Stormwater Drainage & Monsoon Floods",
        "icon": "🌊",
        "svg_key": "drainage",
        "color": "#0284c7",
        "badge": "Hydrological Defense",
        "description": "Deep gravity drainage canals, river embankments, retention reservoirs & floodgate automated telemetry"
    },
    {
        "id": "health_clinics",
        "name": "Public Health, Clinics & Vector Control",
        "icon": "🏥",
        "svg_key": "health",
        "color": "#f43f5e",
        "badge": "Community Health",
        "description": "Secondary trauma hospitals, maternal healthcare centers, medicine stock telemetry & anti-dengue fogging"
    },
    {
        "id": "schools_facilities",
        "name": "Government Schools & Public Facilities",
        "icon": "🏫",
        "svg_key": "schools",
        "color": "#8b5cf6",
        "badge": "Social Infrastructure",
        "description": "Public school building safety, polytechnic skill centers, civic libraries & digital learning labs"
    },
    {
        "id": "parks_environment",
        "name": "Public Parks, Green Belts & Air Quality",
        "icon": "🌳",
        "svg_key": "parks",
        "color": "#16a34a",
        "badge": "Eco Restoration",
        "description": "Urban afforestation, anti-smog water misting towers, public park solar lighting & biodiversity corridors"
    },
    {
        "id": "public_safety",
        "name": "Public Safety & Emergency Infrastructure",
        "icon": "🚨",
        "svg_key": "safety",
        "color": "#ea580c",
        "badge": "Emergency Defense",
        "description": "Pressurized fire hydrants, municipal disaster evacuation routes, CCTV optical feeds & emergency sirens"
    }
]

# ==============================================================================
# BRICS MULTI-NATION JURISDICTION REGISTRY (RULE 04 COMPLIANCE)
# ==============================================================================

BRICS_NODES = {
    "india": {
        "id": "india",
        "country": "India",
        "jurisdiction": "National Capital Region (Delhi NCR)",
        "flag": "🇮🇳",
        "currency": "₹ INR (Crores)",
        "currency_symbol": "₹",
        "unit": "Cr",
        "framework": "PM Gati Shakti National Master Plan & Smart Cities Mission",
        "open_data_portal": "data.gov.in (NDSAP Standards)",
        "total_population": "33.2 Million",
        "avg_density": "11,320 / km²",
        "vulnerability_index": 0.42,
        "total_capex_budget": 18400, # ₹18,400 Cr
        "wards": [
            {
                "name": "Ward 04 - Connaught Place / Central",
                "population": 1200000,
                "density": 14500,
                "vulnerability": 0.22,
                "allocated_capex": 4800, # Cr
                "primary_demand": "Stormwater Drainage & Basements",
                "sector": "Water Supply"
            },
            {
                "name": "Ward 12 - Pitampura / Outer Ring Road",
                "population": 2800000,
                "density": 18200,
                "vulnerability": 0.45,
                "allocated_capex": 2100,
                "primary_demand": "Asphalt Resurfacing & Heavy Potholes",
                "sector": "Roads & Potholes"
            },
            {
                "name": "Ward 19 - Rohini Sector 14",
                "population": 2100000,
                "density": 12800,
                "vulnerability": 0.34,
                "allocated_capex": 1900,
                "primary_demand": "Power Distribution Grid Upgrades",
                "sector": "Electricity & Grid"
            },
            {
                "name": "Ward 28 - Okhla Industrial Basin",
                "population": 3400000,
                "density": 21000,
                "vulnerability": 0.58,
                "allocated_capex": 1400,
                "primary_demand": "Industrial Effluent & Solid Waste Dumps",
                "sector": "Waste & Sanitation"
            },
            {
                "name": "Ward 35 - Seelampur / North-East",
                "population": 3900000,
                "density": 29000,
                "vulnerability": 0.68,
                "allocated_capex": 850,
                "primary_demand": "Piped Clean Drinking Water Network",
                "sector": "Water Supply"
            }
        ]
    },
    "brazil": {
        "id": "brazil",
        "country": "Brazil",
        "jurisdiction": "São Paulo Metropolitan Area (RMSP)",
        "flag": "🇧🇷",
        "currency": "R$ BRL (Milhões)",
        "currency_symbol": "R$",
        "unit": "Mi",
        "framework": "PAC (Programa de Aceleração do Crescimento) & Marco do Saneamento",
        "open_data_portal": "dados.gov.br (Portal Brasileiro de Dados Abertos)",
        "total_population": "22.4 Million",
        "avg_density": "7,500 / km²",
        "vulnerability_index": 0.46,
        "total_capex_budget": 14200, # R$ 14,200 Mi
        "wards": [
            {
                "name": "Distrito Central - Sé / República",
                "population": 950000,
                "density": 9800,
                "vulnerability": 0.28,
                "allocated_capex": 3900, # Mi
                "primary_demand": "Rede Elétrica e Iluminação Pública",
                "sector": "Electricity & Grid"
            },
            {
                "name": "Zona Leste - Itaquera / São Mateus",
                "population": 3800000,
                "density": 16500,
                "vulnerability": 0.55,
                "allocated_capex": 2400,
                "primary_demand": "Drenagem Pluvial e Pavimentação Asfáltica",
                "sector": "Roads & Potholes"
            },
            {
                "name": "Zona Sul - Capão Redondo / Campo Limpo",
                "population": 3200000,
                "density": 15200,
                "vulnerability": 0.62,
                "allocated_capex": 1800,
                "primary_demand": "Abastecimento de Água Tratada (Sabesp)",
                "sector": "Water Supply"
            },
            {
                "name": "Zona Norte - Brasilândia / Freguesia",
                "population": 2600000,
                "density": 14000,
                "vulnerability": 0.59,
                "allocated_capex": 1600,
                "primary_demand": "Contenção de Encostas e Drenagem",
                "sector": "Waste & Sanitation"
            },
            {
                "name": "Região ABC - Santo André / Mauá",
                "population": 2100000,
                "density": 8200,
                "vulnerability": 0.38,
                "allocated_capex": 2200,
                "primary_demand": "Corredores de Transporte Metropolitano",
                "sector": "Public Transport"
            }
        ]
    },
    "south_africa": {
        "id": "south_africa",
        "country": "South Africa",
        "jurisdiction": "Johannesburg / Gauteng Province",
        "flag": "🇿🇦",
        "currency": "R ZAR (Millions)",
        "currency_symbol": "R",
        "unit": "M",
        "framework": "Municipal Infrastructure Grant (MIG) & NDP 2030",
        "open_data_portal": "data.gov.za (National Treasury Portal)",
        "total_population": "15.8 Million",
        "avg_density": "3,400 / km²",
        "vulnerability_index": 0.51,
        "total_capex_budget": 9800, # R 9,800 M
        "wards": [
            {
                "name": "Region F - Inner City / Joburg Central",
                "population": 850000,
                "density": 6200,
                "vulnerability": 0.35,
                "allocated_capex": 3100, # M
                "primary_demand": "Substation Electrification & Cable Protection",
                "sector": "Electricity & Grid"
            },
            {
                "name": "Region D - Soweto / Diepkloof",
                "population": 1900000,
                "density": 8900,
                "vulnerability": 0.59,
                "allocated_capex": 2200,
                "primary_demand": "Bulk Water Pipe Replacement (Joburg Water)",
                "sector": "Water Supply"
            },
            {
                "name": "Region A - Diepsloot / Midrand Corridor",
                "population": 1400000,
                "density": 7400,
                "vulnerability": 0.65,
                "allocated_capex": 1100,
                "primary_demand": "Stormwater Culverts & Access Roads",
                "sector": "Roads & Potholes"
            },
            {
                "name": "Region G - Orange Farm / Ennerdale",
                "population": 1100000,
                "density": 5600,
                "vulnerability": 0.71,
                "allocated_capex": 950,
                "primary_demand": "Sanitation Reticulation & Wastewater",
                "sector": "Waste & Sanitation"
            },
            {
                "name": "Region C - Roodepoort / West Rand",
                "population": 920000,
                "density": 4100,
                "vulnerability": 0.32,
                "allocated_capex": 1600,
                "primary_demand": "Pothole Resurfacing & Traffic Lights",
                "sector": "Roads & Potholes"
            }
        ]
    }
}

def get_brics_node(node_key="india"):
    """Returns a specific BRICS country node by id or country code."""
    key = str(node_key).lower().strip()
    if key in ["in", "india"]:
        return BRICS_NODES["india"]
    elif key in ["br", "brazil"]:
        return BRICS_NODES["brazil"]
    elif key in ["za", "south_africa", "south africa", "southafrica"]:
        return BRICS_NODES["south_africa"]
    return BRICS_NODES.get(key, BRICS_NODES["india"])

def get_active_brics_node(node_key="india"):
    """Returns the currently active BRICS country jurisdiction node."""
    return get_brics_node(node_key)
