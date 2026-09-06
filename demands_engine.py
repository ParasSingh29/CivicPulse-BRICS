import os
import json
from datetime import datetime

DEMANDS_FILE = "demands.json"

def get_all_demands(country_code=None, ward=None):
    """Retrieves all community demands from demands.json, optionally filtered by country and ward."""
    if not os.path.exists(DEMANDS_FILE):
        return []
    try:
        with open(DEMANDS_FILE, "r", encoding="utf-8") as f:
            demands = json.load(f)
    except Exception:
        demands = []

    if country_code:
        c_clean = str(country_code).upper().strip()
        demands = [d for d in demands if d.get("country_code", "").upper() == c_clean]

    if ward and ward != "All Wards":
        w_clean = str(ward).strip().lower()
        demands = [d for d in demands if w_clean in d.get("ward", "").lower()]

    # Default sort by upvotes descending
    demands.sort(key=lambda x: x.get("upvotes", 0), reverse=True)
    return demands

def save_demand(country_code, ward, sector, title, description, estimated_budget="", beneficiaries="", author="Citizen Council"):
    """Saves a new community demand proposal and replicates to Firebase Firestore."""
    demands = get_all_demands()
    new_id = f"DEM-{country_code.upper()}-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    new_demand = {
        "id": new_id,
        "country_code": str(country_code).upper(),
        "ward": str(ward),
        "sector": str(sector),
        "title": str(title),
        "description": str(description),
        "estimated_budget": str(estimated_budget) or "Under Assessment",
        "beneficiaries": str(beneficiaries) or "Community Wide",
        "upvotes": 1,
        "status": "Under Citizen Voting",
        "author": str(author) or "Local Community Member",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "upvoted_by": []
    }

    demands.insert(0, new_demand)
    with open(DEMANDS_FILE, "w", encoding="utf-8") as f:
        json.dump(demands, f, indent=2, ensure_ascii=False)

    try:
        from api_client import sync_demand_to_firestore
        sync_demand_to_firestore(new_demand)
    except Exception:
        pass

    return new_demand

def upvote_demand(demand_id, voter_id=None):
    """Increments the upvote counter for a community demand and updates Firebase."""
    demands = get_all_demands()
    target = None
    for d in demands:
        if d.get("id") == demand_id:
            # Check if voter already voted if voter_id provided
            if voter_id:
                if voter_id in d.get("upvoted_by", []):
                    return False, d.get("upvotes", 0), "You have already upvoted this proposal!"
                d.setdefault("upvoted_by", []).append(voter_id)

            d["upvotes"] = d.get("upvotes", 0) + 1
            target = d
            break

    if target is not None:
        with open(DEMANDS_FILE, "w", encoding="utf-8") as f:
            json.dump(demands, f, indent=2, ensure_ascii=False)

        try:
            from api_client import sync_demand_to_firestore
            sync_demand_to_firestore(target)
        except Exception:
            pass

        return True, target["upvotes"], "Upvote registered successfully!"

    return False, 0, "Demand proposal not found."
