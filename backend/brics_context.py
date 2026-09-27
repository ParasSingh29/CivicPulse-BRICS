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
        "description": "Potholes, damaged flyovers, road resurfacing & pedestrian skywalk safety",
        "image": "/static/img/sectors/roads_transit.jpg"
    },
    {
        "id": "water_supply",
        "name": "Water Supply & Pipeline Leakage",
        "icon": "💧",
        "svg_key": "water",
        "color": "#06b6d4",
        "badge": "Potable Water",
        "description": "Dirty drinking water, leaking water pipes, pressure issues & pump failures",
        "image": "/static/img/sectors/water_supply.jpg"
    },
    {
        "id": "electricity_grid",
        "name": "Electricity, Streetlights & Grid",
        "icon": "⚡",
        "svg_key": "electricity",
        "color": "#eab308",
        "badge": "Energy Infrastructure",
        "description": "Power outages, non-working streetlights, loose wiring & faulty transformers",
        "image": "/static/img/sectors/electricity_grid.jpg"
    },
    {
        "id": "waste_sanitation",
        "name": "Waste Management & Sanitation",
        "icon": "♻️",
        "svg_key": "waste",
        "color": "#10b981",
        "badge": "Circular Cleanliness",
        "description": "Overflowing trash, uncollected house waste, bad odors & illegal dumping",
        "image": "/static/img/sectors/waste_sanitation.jpg"
    },
    {
        "id": "public_transport",
        "name": "Public Transport & Transit Hubs",
        "icon": "🚌",
        "svg_key": "transit",
        "color": "#6366f1",
        "badge": "Mobility Corridors",
        "description": "Bus/Metro delays, damaged bus stops, broken ticket counters & overcrowding",
        "image": "/static/img/sectors/public_transport.jpg"
    },
    {
        "id": "stormwater_flood",
        "name": "Stormwater Drainage & Monsoon Floods",
        "icon": "🌊",
        "svg_key": "drainage",
        "color": "#0284c7",
        "badge": "Hydrological Defense",
        "description": "Waterlogged roads, clogged drains, open gutters & canal flooding",
        "image": "/static/img/sectors/stormwater_flood.jpg"
    },
    {
        "id": "health_clinics",
        "name": "Public Health, Clinics & Vector Control",
        "icon": "🏥",
        "svg_key": "health",
        "color": "#f43f5e",
        "badge": "Community Health",
        "description": "Mosquito breeding, clinic medicine shortages, dengue fogging & hospital hygiene",
        "image": "/static/img/sectors/health_clinics.jpg"
    },
    {
        "id": "schools_facilities",
        "name": "Government Schools & Public Facilities",
        "icon": "🏫",
        "svg_key": "schools",
        "color": "#8b5cf6",
        "badge": "Social Infrastructure",
        "description": "Damaged school rooms, broken toilets, missing desks & library maintenance",
        "image": "/static/img/sectors/schools_facilities.jpg"
    },
    {
        "id": "parks_environment",
        "name": "Public Parks, Green Belts & Air Quality",
        "icon": "🌳",
        "svg_key": "parks",
        "color": "#16a34a",
        "badge": "Eco Restoration",
        "description": "Unlit parks, broken park benches, overgrown trees & heavy dust pollution",
        "image": "/static/img/sectors/parks_environment.jpg"
    },
    {
        "id": "public_safety",
        "name": "Public Safety & Emergency Infrastructure",
        "icon": "🚨",
        "svg_key": "safety",
        "color": "#ea580c",
        "badge": "Emergency Defense",
        "description": "Broken CCTV cameras, unlit streets, damaged fire hydrants & emergency sirens",
        "image": "/static/img/sectors/public_safety.jpg"
    }
]

# ==============================================================================
# BRICS MULTI-NATION JURISDICTION REGISTRY (RULE 04 COMPLIANCE)
# ==============================================================================

BRICS_NODES = {
    "brazil": {
        "id": "brazil",
        "code": "BR",
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
        "coordinates": {"lat": -23.5505, "lon": -46.6333},
        "wards": [
            {
                "name": "Distrito Central - Sé / República",
                "population": 950000,
                "density": 9800,
                "vulnerability": 0.28,
                "allocated_capex": 3900,
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
    "china": {
        "id": "china",
        "code": "CN",
        "country": "China",
        "jurisdiction": "Shanghai Municipality / Yangtze River Delta",
        "flag": "🇨🇳",
        "currency": "¥ CNY (Billion)",
        "currency_symbol": "¥",
        "unit": "B",
        "framework": "14th Five-Year Urban Renewal Plan & Smart Megacity Initiative",
        "open_data_portal": "data.sh.gov.cn (Shanghai Open Data Portal)",
        "total_population": "24.9 Million",
        "avg_density": "3,920 / km²",
        "vulnerability_index": 0.28,
        "total_capex_budget": 28600,
        "coordinates": {"lat": 31.2304, "lon": 121.4737},
        "wards": [
            {
                "name": "Huangpu District - East Nanjing Road / Bund",
                "population": 660000,
                "density": 32000,
                "vulnerability": 0.18,
                "allocated_capex": 6200,
                "primary_demand": "Smart Grid Micro-Substations & Underground Utilities",
                "sector": "Electricity & Grid"
            },
            {
                "name": "Pudong New Area - Lujiazui / Zhangjiang Hi-Tech",
                "population": 5680000,
                "density": 4700,
                "vulnerability": 0.22,
                "allocated_capex": 9400,
                "primary_demand": "Automated Maglev & Autonomous Bus Transit Arterials",
                "sector": "Public Transport"
            },
            {
                "name": "Minhang District - Qibao / Hongqiao Transport Hub",
                "population": 2650000,
                "density": 7100,
                "vulnerability": 0.32,
                "allocated_capex": 4800,
                "primary_demand": "Intermodal Arterial Flyover & Pavement Resurfacing",
                "sector": "Roads & Potholes"
            },
            {
                "name": "Yangpu District - Wujiaochang / Riverside Tech Belt",
                "population": 1240000,
                "density": 20400,
                "vulnerability": 0.29,
                "allocated_capex": 4500,
                "primary_demand": "Deep Flood Interceptor & Sponge City Permeable Pavement",
                "sector": "Water Supply"
            },
            {
                "name": "Jing'an District - West Nanjing Road Commercial Core",
                "population": 980000,
                "density": 26500,
                "vulnerability": 0.24,
                "allocated_capex": 3700,
                "primary_demand": "Intelligent Circular Solid Waste Robotic Sorting",
                "sector": "Waste & Sanitation"
            }
        ]
    },
    "egypt": {
        "id": "egypt",
        "code": "EG",
        "country": "Egypt",
        "jurisdiction": "Greater Cairo Metropolitan Area",
        "flag": "🇪🇬",
        "currency": "E£ EGP (Billion)",
        "currency_symbol": "E£",
        "unit": "B",
        "framework": "Egypt Vision 2030 & Decent Life (Haya Karima) National Initiative",
        "open_data_portal": "egypt.gov.eg (National Open Data Initiative)",
        "total_population": "21.3 Million",
        "avg_density": "19,376 / km²",
        "vulnerability_index": 0.54,
        "total_capex_budget": 11500,
        "coordinates": {"lat": 30.0444, "lon": 31.2357},
        "wards": [
            {
                "name": "Qasr El Nil - Tahrir Square / Downtown",
                "population": 820000,
                "density": 24500,
                "vulnerability": 0.34,
                "allocated_capex": 3100,
                "primary_demand": "Heritage District Cable Undergrounding & Grid Resilience",
                "sector": "Electricity & Grid"
            },
            {
                "name": "Nasr City - Abbas El Akkad / Smart Transit Corridor",
                "population": 2900000,
                "density": 16800,
                "vulnerability": 0.42,
                "allocated_capex": 2800,
                "primary_demand": "Cairo Monorail Feeder Roads & Asphalt Modernization",
                "sector": "Roads & Potholes"
            },
            {
                "name": "Giza - Al Haram / Faisal Residential Basin",
                "population": 4100000,
                "density": 28000,
                "vulnerability": 0.62,
                "allocated_capex": 2200,
                "primary_demand": "Potable Water Pipeline Pressure & Desalination Booster",
                "sector": "Water Supply"
            },
            {
                "name": "Shubra El Kheima - Industrial & Transit Gateway",
                "population": 3200000,
                "density": 31000,
                "vulnerability": 0.67,
                "allocated_capex": 1800,
                "primary_demand": "Industrial Solid Waste & Wastewater Canal Remediation",
                "sector": "Waste & Sanitation"
            },
            {
                "name": "New Administrative Capital - R5 Garden City Feeder",
                "population": 750000,
                "density": 4500,
                "vulnerability": 0.20,
                "allocated_capex": 1600,
                "primary_demand": "Automated Electric Bus Fast-Charging Depots",
                "sector": "Public Transport"
            }
        ]
    },
    "ethiopia": {
        "id": "ethiopia",
        "code": "ET",
        "country": "Ethiopia",
        "jurisdiction": "Addis Ababa City Administration",
        "flag": "🇪🇹",
        "currency": "Br ETB (Billion)",
        "currency_symbol": "Br",
        "unit": "B",
        "framework": "Homegrown Economic Reform Agenda & Addis Ababa Corridor Development",
        "open_data_portal": "data.gov.et (Ethiopia National Data Hub)",
        "total_population": "5.4 Million",
        "avg_density": "10,200 / km²",
        "vulnerability_index": 0.63,
        "total_capex_budget": 4800,
        "coordinates": {"lat": 9.0320, "lon": 38.7483},
        "wards": [
            {
                "name": "Kirkos Sub-City - Meskel Square / Kazanchis",
                "population": 480000,
                "density": 14500,
                "vulnerability": 0.45,
                "allocated_capex": 1400,
                "primary_demand": "Corridor Street Lighting & Smart Traffic Intersections",
                "sector": "Electricity & Grid"
            },
            {
                "name": "Bole Sub-City - Airport Corridor / Rwanda Bridge",
                "population": 890000,
                "density": 7200,
                "vulnerability": 0.38,
                "allocated_capex": 1100,
                "primary_demand": "Arterial Highway Drainage & Pothole Asphalt Resurfacing",
                "sector": "Roads & Potholes"
            },
            {
                "name": "Arada Sub-City - Piazza / Heritage Civic Sector",
                "population": 560000,
                "density": 21000,
                "vulnerability": 0.68,
                "allocated_capex": 850,
                "primary_demand": "Clean Municipal Water Reticulation & Tanker Hubs",
                "sector": "Water Supply"
            },
            {
                "name": "Yeka Sub-City - Kotebe / Megenagna Transit Hub",
                "population": 720000,
                "density": 11400,
                "vulnerability": 0.58,
                "allocated_capex": 750,
                "primary_demand": "Solid Waste Transfer Stations & Drainage Embankments",
                "sector": "Waste & Sanitation"
            },
            {
                "name": "Akaki Kality - Industrial Free Zone / Freight Line",
                "population": 640000,
                "density": 5300,
                "vulnerability": 0.64,
                "allocated_capex": 700,
                "primary_demand": "Commuter Rail Feeder Roads & Heavy Freight Bypass",
                "sector": "Public Transport"
            }
        ]
    },
    "india": {
        "id": "india",
        "code": "IN",
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
        "coordinates": {"lat": 28.6139, "lon": 77.2090},
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
    "indonesia": {
        "id": "indonesia",
        "code": "ID",
        "country": "Indonesia",
        "jurisdiction": "Special Capital Region of Jakarta (DKI Jakarta)",
        "flag": "🇮🇩",
        "currency": "Rp IDR (Trillion)",
        "currency_symbol": "Rp",
        "unit": "T",
        "framework": "National Strategic Projects (PSN) & Jakarta Flood Resilient Megacity Plan",
        "open_data_portal": "data.jakarta.go.id (Satu Data Indonesia)",
        "total_population": "10.6 Million",
        "avg_density": "15,900 / km²",
        "vulnerability_index": 0.58,
        "total_capex_budget": 9200,
        "coordinates": {"lat": -6.2088, "lon": 106.8456},
        "wards": [
            {
                "name": "Central Jakarta - Gambir / Thamrin CBD",
                "population": 920000,
                "density": 19200,
                "vulnerability": 0.32,
                "allocated_capex": 2700,
                "primary_demand": "Underground Substation & Smart Public Streetlights",
                "sector": "Electricity & Grid"
            },
            {
                "name": "North Jakarta - Pluit / Tanjung Priok Port",
                "population": 1800000,
                "density": 12500,
                "vulnerability": 0.72,
                "allocated_capex": 2300,
                "primary_demand": "Giant Sea Wall Sea Dikes & Pumping Stations",
                "sector": "Water Supply"
            },
            {
                "name": "East Jakarta - Jatinegara / Cawang Interchange",
                "population": 3100000,
                "density": 16800,
                "vulnerability": 0.59,
                "allocated_capex": 1800,
                "primary_demand": "TransJakarta Bus Rapid Transit Flyovers & Resurfacing",
                "sector": "Roads & Potholes"
            },
            {
                "name": "South Jakarta - Kebayoran Baru / Blok M Hub",
                "population": 2300000,
                "density": 15900,
                "vulnerability": 0.41,
                "allocated_capex": 1400,
                "primary_demand": "MRT Jakarta Feeder Line Expansion & Pedestrian Bridges",
                "sector": "Public Transport"
            },
            {
                "name": "West Jakarta - Cengkareng / Kalideres Lowland",
                "population": 2480000,
                "density": 19100,
                "vulnerability": 0.65,
                "allocated_capex": 1000,
                "primary_demand": "River Dredging & Modern Waste Compactor Hubs",
                "sector": "Waste & Sanitation"
            }
        ]
    },
    "iran": {
        "id": "iran",
        "code": "IR",
        "country": "Iran",
        "jurisdiction": "Tehran Metropolitan Area",
        "flag": "🇮🇷",
        "currency": "Toman / Rial (Trillion)",
        "currency_symbol": "﷼",
        "unit": "T",
        "framework": "Tehran Master Development Plan & National Urban Transport Modernization",
        "open_data_portal": "data.tehran.ir (Tehran Open Data Portal)",
        "total_population": "9.5 Million",
        "avg_density": "12,900 / km²",
        "vulnerability_index": 0.49,
        "total_capex_budget": 8100,
        "coordinates": {"lat": 35.6892, "lon": 51.3890},
        "wards": [
            {
                "name": "District 12 - Grand Bazaar / Baharestan",
                "population": 680000,
                "density": 18200,
                "vulnerability": 0.48,
                "allocated_capex": 2200,
                "primary_demand": "Historic Bazaar Fire Protection & Electrical Upgrades",
                "sector": "Electricity & Grid"
            },
            {
                "name": "District 6 - Vali Asr / Enghelab Academic Hub",
                "population": 820000,
                "density": 15400,
                "vulnerability": 0.35,
                "allocated_capex": 1900,
                "primary_demand": "BRT Vali Asr Corridor Modernization & Pothole Repair",
                "sector": "Roads & Potholes"
            },
            {
                "name": "District 20 - Shahr-e Rey Southern Basin",
                "population": 1450000,
                "density": 11200,
                "vulnerability": 0.66,
                "allocated_capex": 1600,
                "primary_demand": "Deep Aquifer Potable Water & Pipe Network Renovation",
                "sector": "Water Supply"
            },
            {
                "name": "District 2 - Sadeghiyeh / Shahrak-e Gharb",
                "population": 1200000,
                "density": 9800,
                "vulnerability": 0.28,
                "allocated_capex": 1400,
                "primary_demand": "Tehran Metro Line 7 Linkages & Clean Electric Buses",
                "sector": "Public Transport"
            },
            {
                "name": "District 4 - Tehranpars / Eastern Foothills",
                "population": 1950000,
                "density": 13600,
                "vulnerability": 0.52,
                "allocated_capex": 1000,
                "primary_demand": "Seasonal Stormwater Runoff Culverts & Waste Processing",
                "sector": "Waste & Sanitation"
            }
        ]
    },
    "russia": {
        "id": "russia",
        "code": "RU",
        "country": "Russia",
        "jurisdiction": "Moscow Federal City & Central Federal District",
        "flag": "🇷🇺",
        "currency": "₽ RUB (Billion)",
        "currency_symbol": "₽",
        "unit": "B",
        "framework": "National Project 'Safe & Quality Roads' & Smart City Moscow",
        "open_data_portal": "data.mos.ru (Moscow Open Data Portal)",
        "total_population": "13.1 Million",
        "avg_density": "5,100 / km²",
        "vulnerability_index": 0.31,
        "total_capex_budget": 22400,
        "coordinates": {"lat": 55.7558, "lon": 37.6173},
        "wards": [
            {
                "name": "Central Administrative Okrug - Tverskoy / Arbat",
                "population": 780000,
                "density": 11800,
                "vulnerability": 0.19,
                "allocated_capex": 5800,
                "primary_demand": "District Heating Pipeline Telemetry & Smart Substations",
                "sector": "Electricity & Grid"
            },
            {
                "name": "Northern Administrative Okrug - Sokol / Aeroport",
                "population": 1180000,
                "density": 10400,
                "vulnerability": 0.27,
                "allocated_capex": 4600,
                "primary_demand": "Leningradsky Prospekt Asphalt & Bridge Resurfacing",
                "sector": "Roads & Potholes"
            },
            {
                "name": "South-Eastern Okrug - Lyublino / Maryino",
                "population": 1520000,
                "density": 12800,
                "vulnerability": 0.42,
                "allocated_capex": 4200,
                "primary_demand": "Moskva River Watershed Drainage & Wastewater Treatment",
                "sector": "Water Supply"
            },
            {
                "name": "Western Administrative Okrug - Ramenki / Dorogomilovo",
                "population": 1390000,
                "density": 9100,
                "vulnerability": 0.24,
                "allocated_capex": 4100,
                "primary_demand": "Electric Bus (Electrobus) Terminals & Charging Hubs",
                "sector": "Public Transport"
            },
            {
                "name": "Troitsky & Novomoskovsky Okrug - New Moscow",
                "population": 650000,
                "density": 1200,
                "vulnerability": 0.36,
                "allocated_capex": 3700,
                "primary_demand": "Automated Waste Sorting & High-Tech Landfill Gas Recovery",
                "sector": "Waste & Sanitation"
            }
        ]
    },
    "saudi_arabia": {
        "id": "saudi_arabia",
        "code": "SA",
        "country": "Saudi Arabia",
        "jurisdiction": "Riyadh Metropolitan Area",
        "flag": "🇸🇦",
        "currency": "﷼ SAR (Billion)",
        "currency_symbol": "﷼",
        "unit": "B",
        "framework": "Saudi Vision 2030 & Riyadh Green Infrastructure Sustainability Project",
        "open_data_portal": "data.gov.sa (Saudi Open Data Portal)",
        "total_population": "7.7 Million",
        "avg_density": "4,200 / km²",
        "vulnerability_index": 0.33,
        "total_capex_budget": 26500,
        "coordinates": {"lat": 24.7136, "lon": 46.6753},
        "wards": [
            {
                "name": "Al Olaya - King Fahd Corridor / Central Financial Hub",
                "population": 950000,
                "density": 8500,
                "vulnerability": 0.21,
                "allocated_capex": 7200,
                "primary_demand": "District Cooling Microgrids & Smart SCADA Sensors",
                "sector": "Electricity & Grid"
            },
            {
                "name": "King Abdullah Financial District (KAFD) - Northern Spine",
                "population": 450000,
                "density": 12000,
                "vulnerability": 0.16,
                "allocated_capex": 6400,
                "primary_demand": "Riyadh Metro Line 4 Feeder Links & Autonomous Transit",
                "sector": "Public Transport"
            },
            {
                "name": "Al Malaz - University & Government Ministries District",
                "population": 1400000,
                "density": 9200,
                "vulnerability": 0.35,
                "allocated_capex": 4800,
                "primary_demand": "Arterial Ring Road Pothole Resurfacing & Heat-Proof Asphalt",
                "sector": "Roads & Potholes"
            },
            {
                "name": "Al Batha - Old Commercial & High-Density Center",
                "population": 1850000,
                "density": 14800,
                "vulnerability": 0.52,
                "allocated_capex": 4500,
                "primary_demand": "Wadi Hanifah Storm Runoff Drainage & Desalinated Water",
                "sector": "Water Supply"
            },
            {
                "name": "Al Shifa - Southern Residential & Industrial Zone",
                "population": 1250000,
                "density": 6800,
                "vulnerability": 0.44,
                "allocated_capex": 3600,
                "primary_demand": "Circular Waste Processing & Eco-Recycling Complex",
                "sector": "Waste & Sanitation"
            }
        ]
    },
    "south_africa": {
        "id": "south_africa",
        "code": "ZA",
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
        "coordinates": {"lat": -26.2041, "lon": 28.0473},
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
    },
    "united_arab_emirates": {
        "id": "united_arab_emirates",
        "code": "AE",
        "country": "United Arab Emirates",
        "jurisdiction": "Dubai / Abu Dhabi Metropolitan Federal Hub",
        "flag": "🇦🇪",
        "currency": "AED (Billion)",
        "currency_symbol": "AED",
        "unit": "B",
        "framework": "UAE Centenary 2071 & Dubai 2040 Urban Master Plan",
        "open_data_portal": "bayanat.ae (UAE Federal Open Data Portal)",
        "total_population": "9.9 Million",
        "avg_density": "3,200 / km²",
        "vulnerability_index": 0.24,
        "total_capex_budget": 24800,
        "coordinates": {"lat": 25.2048, "lon": 55.2708},
        "wards": [
            {
                "name": "Downtown Dubai - Sheikh Zayed Road / DIFC Corridor",
                "population": 620000,
                "density": 11500,
                "vulnerability": 0.15,
                "allocated_capex": 6800,
                "primary_demand": "Smart Grid EV Ultra-Fast Depots & Substation Upgrades",
                "sector": "Electricity & Grid"
            },
            {
                "name": "Deira & Dubai Creek - Historic Maritime Commercial Hub",
                "population": 1450000,
                "density": 19800,
                "vulnerability": 0.38,
                "allocated_capex": 5200,
                "primary_demand": "Deep Rain Stormwater Canals & Underground Retention",
                "sector": "Water Supply"
            },
            {
                "name": "Dubai South - Al Maktoum International & Logistics City",
                "population": 580000,
                "density": 2400,
                "vulnerability": 0.22,
                "allocated_capex": 4900,
                "primary_demand": "Autonomous Freight Corridors & Heavy Highway Resurfacing",
                "sector": "Roads & Potholes"
            },
            {
                "name": "Jumeirah & Al Sufouh - Coastal Smart Urban District",
                "population": 780000,
                "density": 5600,
                "vulnerability": 0.18,
                "allocated_capex": 4300,
                "primary_demand": "Dubai Tram Feeder Lines & Solar Pod Shuttles",
                "sector": "Public Transport"
            },
            {
                "name": "Abu Dhabi Central - Corniche / Al Reem Island Corridor",
                "population": 1100000,
                "density": 8200,
                "vulnerability": 0.22,
                "allocated_capex": 3600,
                "primary_demand": "Circular Zero-Waste Waste-to-Energy Master Plant",
                "sector": "Waste & Sanitation"
            }
        ]
    }
}

NODE_KEY_ALIAS_MAP = {
    "in": "india", "india": "india",
    "br": "brazil", "brazil": "brazil",
    "za": "south_africa", "south_africa": "south_africa", "south africa": "south_africa", "southafrica": "south_africa",
    "cn": "china", "china": "china",
    "ru": "russia", "russia": "russia", "russian federation": "russia",
    "eg": "egypt", "egypt": "egypt",
    "et": "ethiopia", "ethiopia": "ethiopia",
    "id": "indonesia", "indonesia": "indonesia",
    "ir": "iran", "iran": "iran",
    "sa": "saudi_arabia", "saudi_arabia": "saudi_arabia", "saudi arabia": "saudi_arabia", "saudi": "saudi_arabia",
    "ae": "united_arab_emirates", "united_arab_emirates": "united_arab_emirates", "uae": "united_arab_emirates", "united arab emirates": "united_arab_emirates"
}

def get_brics_node(node_key="india"):
    """Returns a specific BRICS country node by id, country code, or country name."""
    key = str(node_key).lower().strip()
    node_id = NODE_KEY_ALIAS_MAP.get(key, key)
    return BRICS_NODES.get(node_id, BRICS_NODES["india"])

def get_active_brics_node(node_key="india"):
    """Returns the currently active BRICS country jurisdiction node."""
    return get_brics_node(node_key)
