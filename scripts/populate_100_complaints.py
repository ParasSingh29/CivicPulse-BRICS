import sqlite3
import json
import random
from datetime import datetime, timedelta

DB_FILE = "data/civicpulse.db"

def generate_100_complaints():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Ensure tables exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY,
        name TEXT,
        phone TEXT,
        password_hash TEXT,
        salt TEXT,
        address TEXT,
        city TEXT,
        pincode TEXT,
        state TEXT,
        country TEXT,
        role TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        id TEXT PRIMARY KEY,
        user_id TEXT,
        category TEXT,
        description TEXT,
        location_json TEXT,
        status TEXT,
        timestamp TEXT,
        photo_url TEXT,
        resolution_photo TEXT,
        resolution_notes TEXT
    )
    """)

    first_names_in = ["Aarav", "Ananya", "Rajesh", "Priya", "Karthik", "Sunita", "Arjun", "Neha", "Vikram", "Meera", "Rohan", "Kavita", "Sanjay", "Deepika", "Aditya", "Pooja", "Rahul", "Swati", "Nikhil", "Divya"]
    last_names_in = ["Sharma", "Kumar", "Patel", "Verma", "Mehta", "Singh", "Joshi", "Gowda", "Nair", "Rao", "Deshmukh", "Chawla", "Gupta", "Reddy", "Banerjee", "Kapoor", "Bhat", "Dhar", "Chatterjee", "Mishra"]

    first_names_br = ["Lucas", "Mateo", "Gabriel", "Sophia", "Isabella", "Rodrigo", "Thiago", "Camila", "Mariana", "Felipe", "Beatriz", "Carlos", "Fernanda", "Rafael", "Letícia", "Bruno"]
    last_names_br = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Ribeiro", "Carvalho", "Mendes", "Martins"]

    first_names_za = ["Sipho", "Kagiso", "Thabo", "Njabulo", "Zinhle", "Nomvula", "Bongani", "Tebogo", "Lungile", "Khaya", "Ayanda", "Bandile", "Lerato", "Sibusiso"]
    last_names_za = ["Nkosi", "Ndlovu", "Dlamini", "Mokoena", "Sithole", "Khumalo", "Mthembu", "Zulu", "Malaika", "Botha", "Van Der Merwe", "Naidoo"]

    first_names_ru = ["Dmitry", "Elena", "Alexander", "Olga", "Sergei", "Tatyana", "Ivan", "Natalia", "Maxim", "Anna", "Vladimir", "Yulia"]
    last_names_ru = ["Smirnov", "Ivanov", "Kuznetsov", "Popov", "Vasiliev", "Petrov", "Sokolov", "Mikhailov", "Morozov", "Volkov"]

    first_names_cn = ["Wei", "Li", "Zhang", "Chen", "Wang", "Liu", "Yang", "Huang", "Zhao", "Wu", "Zhou", "Xu"]
    last_names_cn = ["Wei", "Na", "Ming", "Qiang", "Jie", "Lei", "Xiu", "Fang", "Yan", "Hao", "Jun", "Lin"]

    sectors = [
        "Roads, Bridges & Arterial Corridors",
        "Water Supply & Pipeline Leakage",
        "Public Transport & Transit Hubs",
        "Stormwater Drainage & Monsoon Floods",
        "Electricity, Streetlights & Grid",
        "Solid Waste, Garbage & Sanitation",
        "Public Health, Clinics & Vector Control",
        "Parks, Green Spaces & Environment",
        "School Infrastructure & Education",
        "Street Safety, Lighting & CCTV"
    ]

    locations_data = [
        # Delhi
        {"city": "Delhi", "country": "India", "address": "Outer Ring Road, Pitampura, North West Delhi", "lat": 28.6987, "lon": 77.1385},
        {"city": "Delhi", "country": "India", "address": "Janakpuri Block B, West Delhi", "lat": 28.6219, "lon": 77.0878},
        {"city": "Delhi", "country": "India", "address": "Seelampur Main Market, North-East Delhi", "lat": 28.6644, "lon": 77.2678},
        {"city": "Delhi", "country": "India", "address": "Rohini Sector 14, North West Delhi", "lat": 28.7159, "lon": 77.1264},
        {"city": "Delhi", "country": "India", "address": "Connaught Place Inner Circle, Central Delhi", "lat": 28.6315, "lon": 77.2167},
        {"city": "Delhi", "country": "India", "address": "Lajpat Nagar Central Market, South Delhi", "lat": 28.5677, "lon": 77.2433},
        {"city": "Delhi", "country": "India", "address": "Dwarka Sector 10 Metro Corridor, South West Delhi", "lat": 28.5815, "lon": 77.0588},
        {"city": "Delhi", "country": "India", "address": "Chandni Chowk Main Road, Old Delhi", "lat": 28.6506, "lon": 77.2303},
        {"city": "Delhi", "country": "India", "address": "Okhla Industrial Area Phase 3, South East Delhi", "lat": 28.5445, "lon": 77.2731},
        {"city": "Delhi", "country": "India", "address": "Karol Bagh Metro Station Area, Central Delhi", "lat": 28.6517, "lon": 77.1906},
        {"city": "Delhi", "country": "India", "address": "Saket District Centre, South Delhi", "lat": 28.5246, "lon": 77.2066},
        {"city": "Delhi", "country": "India", "address": "Mayur Vihar Phase 1, East Delhi", "lat": 28.6083, "lon": 77.2950},
        
        # Mumbai
        {"city": "Mumbai", "country": "India", "address": "Dadar Junction Railway Station, West Dadar", "lat": 19.0178, "lon": 72.8478},
        {"city": "Mumbai", "country": "India", "address": "Kurla Freight Yard Terminus, Kurla East", "lat": 19.0657, "lon": 72.8797},
        {"city": "Mumbai", "country": "India", "address": "JVLR East-West Link Road, Jogeshwari", "lat": 19.1254, "lon": 72.8741},
        {"city": "Mumbai", "country": "India", "address": "Andheri East Western Express Highway, Andheri", "lat": 19.1136, "lon": 72.8697},
        {"city": "Mumbai", "country": "India", "address": "Bandra Hill Road, Bandra West", "lat": 19.0596, "lon": 72.8295},
        {"city": "Mumbai", "country": "India", "address": "Colaba Causeway Market Corridor, South Mumbai", "lat": 18.9067, "lon": 72.8147},
        {"city": "Mumbai", "country": "India", "address": "Thane Station West Flyover, Thane Corridor", "lat": 19.1860, "lon": 72.9759},
        {"city": "Mumbai", "country": "India", "address": "Vashi Sector 17 Commercial Hub, Navi Mumbai", "lat": 19.0771, "lon": 73.0033},
        {"city": "Mumbai", "country": "India", "address": "Powai Lake Promenade Road, Powai", "lat": 19.1232, "lon": 72.9054},
        {"city": "Mumbai", "country": "India", "address": "Worli Sea Face Promenade, South Mumbai", "lat": 19.0110, "lon": 72.8170},

        # Bengaluru
        {"city": "Bengaluru", "country": "India", "address": "Central Silk Board Junction, Hosur Road", "lat": 12.9172, "lon": 77.6228},
        {"city": "Bengaluru", "country": "India", "address": "Bellandur Lake Spillway Road, South-East Bengaluru", "lat": 12.9345, "lon": 77.6657},
        {"city": "Bengaluru", "country": "India", "address": "Whitefield ITPL Main Road, East Bengaluru", "lat": 12.9870, "lon": 77.7370},
        {"city": "Bengaluru", "country": "India", "address": "Indiranagar 100ft Road Corridor, East Bengaluru", "lat": 12.9784, "lon": 77.6408},
        {"city": "Bengaluru", "country": "India", "address": "Koramangala 5th Block Junction, South Bengaluru", "lat": 12.9352, "lon": 77.6245},
        {"city": "Bengaluru", "country": "India", "address": "Hebbal Flyover Bottleneck, North Bengaluru", "lat": 13.0358, "lon": 77.5970},
        {"city": "Bengaluru", "country": "India", "address": "Electronic City Phase 1 Gate 3, South Bengaluru", "lat": 12.8452, "lon": 77.6602},
        {"city": "Bengaluru", "country": "India", "address": "Jayanagar 4th Block Shopping Complex, South Bengaluru", "lat": 12.9250, "lon": 77.5840},
        {"city": "Bengaluru", "country": "India", "address": "Marathahalli Bridge Underpass, Outer Ring Road", "lat": 12.9562, "lon": 77.7019},

        # São Paulo
        {"city": "São Paulo", "country": "Brazil", "address": "Marginal Pinheiros / Ponte Estaiada Expressway", "lat": -23.6134, "lon": -46.6985},
        {"city": "São Paulo", "country": "Brazil", "address": "Avenida dos Estados Tamanduateí River Basin", "lat": -23.5505, "lon": -46.6333},
        {"city": "São Paulo", "country": "Brazil", "address": "Avenida Paulista Financial Corridor, Centro", "lat": -23.5615, "lon": -46.6559},
        {"city": "São Paulo", "country": "Brazil", "address": "Moema Residential Perimeter, Zona Sul", "lat": -23.6025, "lon": -46.6617},
        {"city": "São Paulo", "country": "Brazil", "address": "Tatuapé Metro Transit Hub, Zona Leste", "lat": -23.5412, "lon": -46.5744},
        {"city": "São Paulo", "country": "Brazil", "address": "Vila Madalena Cultural District, Zona Oeste", "lat": -23.5542, "lon": -46.6908},
        {"city": "São Paulo", "country": "Brazil", "address": "Santo Amaro Industrial Zone, South SP", "lat": -23.6534, "lon": -46.7088},
        {"city": "São Paulo", "country": "Brazil", "address": "Liberdade Square District, Central SP", "lat": -23.5587, "lon": -46.6358},

        # Johannesburg
        {"city": "Johannesburg", "country": "South Africa", "address": "Soweto West Industrial Grid Perimeter", "lat": -26.2485, "lon": 27.8540},
        {"city": "Johannesburg", "country": "South Africa", "address": "Diepsloot West Bulk Pump Infrastructure, Region A", "lat": -25.9333, "lon": 28.0167},
        {"city": "Johannesburg", "country": "South Africa", "address": "Sandton City Commercial Hub, Region E", "lat": -26.1076, "lon": 28.0567},
        {"city": "Johannesburg", "country": "South Africa", "address": "Braamfontein Civic Theatre Zone, Central JHB", "lat": -26.1925, "lon": 28.0345},
        {"city": "Johannesburg", "country": "South Africa", "address": "Midrand Logistics & Tech Corridor, Northern JHB", "lat": -25.9981, "lon": 28.1264},
        {"city": "Johannesburg", "country": "South Africa", "address": "Rosebank Gautrain Station Hub, Region B", "lat": -26.1458, "lon": 28.0441},
        {"city": "Johannesburg", "country": "South Africa", "address": "Alexandra Township Main Arterial Road", "lat": -26.1034, "lon": 28.0954},

        # Moscow
        {"city": "Moscow", "country": "Russia", "address": "Tverskaya Street Boulevard, Central Moscow", "lat": 55.7601, "lon": 37.6083},
        {"city": "Moscow", "country": "Russia", "address": "Arbat Pedestrian Corridor, Western Okrug", "lat": 55.7494, "lon": 37.5913},
        {"city": "Moscow", "country": "Russia", "address": "Sokolniki Metro & Park Zone, Eastern Okrug", "lat": 55.7925, "lon": 37.6784},
        {"city": "Moscow", "country": "Russia", "address": "Tagansky District Hub, South-Eastern Okrug", "lat": 55.7415, "lon": 37.6538},
        {"city": "Moscow", "country": "Russia", "address": "Izmailovo District Boulevard, East Moscow", "lat": 55.7877, "lon": 37.7782},

        # Beijing
        {"city": "Beijing", "country": "China", "address": "Chaoyang District International Zone", "lat": 39.9219, "lon": 116.4431},
        {"city": "Beijing", "country": "China", "address": "Haidian Tech Corridor & Zhongguancun", "lat": 39.9593, "lon": 116.2985},
        {"city": "Beijing", "country": "China", "address": "Dongcheng Historic District, Central Beijing", "lat": 39.9289, "lon": 116.4164},
        {"city": "Beijing", "country": "China", "address": "Xicheng Financial Avenue Corridor", "lat": 39.9123, "lon": 116.3658}
    ]

    problem_templates = [
        ("Roads, Bridges & Arterial Corridors", "Severe asphalt subsidence and deep crater pothole chain creating massive traffic hazard during peak commute hours.", "Critical"),
        ("Roads, Bridges & Arterial Corridors", "Damaged expansion joint on elevated flyover bridge causing structural vibration and tire blowouts.", "High"),
        ("Water Supply & Pipeline Leakage", "Main feeder pipeline burst resulting in heavy road flooding and water pressure loss to 12,000 households.", "Critical"),
        ("Water Supply & Pipeline Leakage", "Contaminated municipal drinking water supply flowing with brown rust silt from aging iron distribution lines.", "High"),
        ("Public Transport & Transit Hubs", "Suburban transit signaling failure causing 50-minute train delays and severe platform overcrowding.", "Critical"),
        ("Public Transport & Transit Hubs", "Broken ticketing barriers and out-of-service escalators causing commuter crushes at main metro gate.", "Medium"),
        ("Stormwater Drainage & Monsoon Floods", "Stormwater nullah completely clogged with plastic debris, flooding adjacent residential streets under 2ft of water.", "Critical"),
        ("Stormwater Drainage & Monsoon Floods", "Blocked street catch basins causing flash puddle accumulation and waterlogging near school gate.", "Medium"),
        ("Electricity, Streetlights & Grid", "Substation transformer explosion causing widespread blackout across 8 residential blocks for over 18 hours.", "Critical"),
        ("Electricity, Streetlights & Grid", "Continuous string of 14 non-functional streetlights leaving key arterial underpass pitch dark at night.", "High"),
        ("Solid Waste, Garbage & Sanitation", "Unattended municipal dump site overflowing into main roadway, attracting stray animals and generating stench.", "High"),
        ("Solid Waste, Garbage & Sanitation", "Secondary waste collection bins damaged and unemptied for 5 days, spilling onto pedestrian pavement.", "Medium"),
        ("Public Health, Clinics & Vector Control", "Stagnant rainwater pool fostering mosquito breeding ground near public primary healthcare center.", "High"),
        ("Public Health, Clinics & Vector Control", "Local dispensary lacks critical emergency trauma first-aid supplies and functioning cold-chain refrigeration.", "Medium"),
        ("Parks, Green Spaces & Environment", "Fallen heavy oak branch blocking public park walking trail and posing danger to children.", "Low"),
        ("Parks, Green Spaces & Environment", "Uncontrolled industrial effluent dumping into community wetland pond causing fish die-off.", "High"),
        ("School Infrastructure & Education", "Primary school perimeter wall collapse after heavy downpour, leaving campus unsecured.", "High"),
        ("School Infrastructure & Education", "Leaking roof tiles in municipal school science laboratory damaging educational computers.", "Medium"),
        ("Street Safety, Lighting & CCTV", "Public surveillance CCTV camera damaged by vandalism at high-crime intersection.", "Medium"),
        ("Street Safety, Lighting & CCTV", "Dark unlit pedestrian crosswalk on 4-lane avenue posing severe danger to night commuters.", "High")
    ]

    statuses = ["Pending", "In Progress", "Resolved"]
    status_weights = [0.45, 0.35, 0.20]

    base_time = datetime.now()

    inserted_users = set()

    for i in range(1, 101):
        loc_item = locations_data[(i - 1) % len(locations_data)]
        country = loc_item["country"]

        if country == "India":
            fn = random.choice(first_names_in)
            ln = random.choice(last_names_in)
            domain = random.choice(["gmail.com", "yahoo.co.in", "civicpulse.org", "outlook.com"])
            phone = f"+91 {random.randint(98000, 98999)} {random.randint(10000, 99999)}"
        elif country == "Brazil":
            fn = random.choice(first_names_br)
            ln = random.choice(last_names_br)
            domain = random.choice(["uol.com.br", "gmail.com", "sp.gov.br", "hotmail.com"])
            phone = f"+55 11 {random.randint(98000, 98999)}-{random.randint(1000, 9999)}"
        elif country == "South Africa":
            fn = random.choice(first_names_za)
            ln = random.choice(last_names_za)
            domain = random.choice(["gmail.com", "yahoo.co.za", "jhb.gov.za", "webmail.co.za"])
            phone = f"+27 11 {random.randint(980, 999)} {random.randint(1000, 9999)}"
        elif country == "Russia":
            fn = random.choice(first_names_ru)
            ln = random.choice(last_names_ru)
            domain = random.choice(["yandex.ru", "mail.ru", "gmail.com", "rambler.ru"])
            phone = f"+7 495 {random.randint(900, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}"
        else: # China
            fn = random.choice(first_names_cn)
            ln = random.choice(last_names_cn)
            domain = random.choice(["qq.com", "163.com", "sina.com", "gmail.com"])
            phone = f"+86 10 {random.randint(8000, 8999)} {random.randint(1000, 9999)}"

        full_name = f"{fn} {ln}"
        email = f"{fn.lower()}.{ln.lower()}{random.randint(1, 99)}@{domain}"

        if email not in inserted_users:
            cursor.execute("""
            INSERT OR IGNORE INTO users (email, name, phone, password_hash, salt, address, city, country, role)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (email, full_name, phone, "hash", "salt", loc_item["address"], loc_item["city"], country, "citizen"))
            inserted_users.add(email)

        template = problem_templates[(i - 1) % len(problem_templates)]
        category = template[0]
        base_desc = template[1]
        priority = template[2]

        full_description = f"{base_desc}\n\n[Priority]: {priority}"

        comp_id = f"CP-{loc_item['city'][:3].upper()}-{(i):03d}"
        
        status = random.choices(statuses, weights=status_weights)[0]
        
        # Random timestamp in the last 14 days
        hours_ago = random.randint(1, 336)
        ts_dt = base_time - timedelta(hours=hours_ago)
        ts_str = ts_dt.strftime("%Y-%m-%d %H:%M:%S")

        loc_json = json.dumps({
            "address": loc_item["address"],
            "latitude": loc_item["lat"],
            "longitude": loc_item["lon"],
            "city": loc_item["city"],
            "country": country
        })

        cursor.execute("""
        INSERT OR REPLACE INTO complaints (id, user_id, category, description, location_json, status, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (comp_id, email, category, full_description, loc_json, status, ts_str))

    conn.commit()
    conn.close()
    print("Successfully generated 100 complaints across BRICS cities!")

if __name__ == "__main__":
    generate_100_complaints()
