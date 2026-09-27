import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from starlette.testclient import TestClient
from server import app
from sms_gateway import send_sms_notification, get_sms_logs
from api_client import save_complaint, update_complaint_status

client = TestClient(app)

def test_sms_gateway_direct_dispatch():
    """Test direct SMS formatting and logging for all status milestones."""
    from datetime import datetime
    phone = "+91 98101 23456"
    test_cid = f"CP-SMS-TEST-{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

    # 1. Registered
    res1 = send_sms_notification(phone, test_cid, "REGISTERED", "Water Supply & Pipeline Leakage")
    assert res1["status"] == "success"
    assert "REGISTERED" in res1["message"]
    assert test_cid in res1["message"]

    # 2. Team Assigned
    res2 = send_sms_notification(phone, test_cid, "In Progress", "Water Supply & Pipeline Leakage", {
        "department": "Municipal Water Board",
        "engineer": "Er. Ananya Verma"
    })
    assert res2["status"] == "success"
    assert "TEAM ASSIGNED" in res2["message"]
    assert "Er. Ananya Verma" in res2["message"]

    # 3. Solved
    res3 = send_sms_notification(phone, test_cid, "Resolved", "Water Supply & Pipeline Leakage")
    assert res3["status"] == "success"
    assert "SOLVED" in res3["message"]

    # 4. Verify logs
    logs = get_sms_logs(complaint_id=test_cid)
    assert len(logs) == 3
    print("[PASS] Direct SMS Gateway Dispatch & Audit Log verified for all 3 status milestones!")


def test_sms_integration_via_complaint_lifecycle():
    """Test end-to-end complaint creation and status updates triggering SMS dispatches."""
    # 1. Register Complaint via API Client -> triggers REGISTERED SMS
    cid = save_complaint(
        user_id="paras@civicpulse.org",
        category="Roads, Bridges & Arterial Corridors",
        description="Large pothole near ring road flyover",
        location={"address": "Pitampura, New Delhi", "latitude": 28.69, "longitude": 77.13}
    )
    assert cid.startswith("CP-")

    logs1 = get_sms_logs(complaint_id=cid)
    assert len(logs1) >= 1
    assert "REGISTERED" in logs1[0]["event_type"].upper()

    # 2. Assign Team (In Progress) -> triggers TEAM ASSIGNED SMS
    ok_prog = update_complaint_status(
        cid,
        new_status="In Progress",
        department="Delhi Public Works Department",
        engineer="Er. Vikram Sharma"
    )
    assert ok_prog is True

    logs2 = get_sms_logs(complaint_id=cid)
    assert len(logs2) >= 2
    assert any("TEAM" in l["message"] or "ASSIGNED" in l["message"] or "PROGRESS" in l["event_type"].upper() for l in logs2)

    # 3. Solve Problem (Resolved) -> triggers SOLVED SMS
    ok_solv = update_complaint_status(cid, new_status="Resolved")
    assert ok_solv is True

    logs3 = get_sms_logs(complaint_id=cid)
    assert len(logs3) >= 3
    assert any("SOLVED" in l["message"] or "RESOLVED" in l["event_type"].upper() for l in logs3)

    print(f"[PASS] End-to-end complaint lifecycle for #{cid} successfully dispatched SMS alerts for Registered, Team Assigned, and Solved!")


def test_sms_api_endpoints():
    """Test HTTP API endpoints /api/sms/logs and /api/sms/send."""
    # 1. Test /api/sms/send
    res = client.post("/api/sms/send", json={
        "phone": "+91 98101 99999",
        "complaint_id": "CP-API-SMS-1",
        "event_type": "SOLVED",
        "category": "Waste Management & Sanitation"
    })
    assert res.status_code == 200
    body = res.json()
    assert body["status"] == "success"
    assert "CP-API-SMS-1" in body["message"]

    # 2. Test /api/sms/logs
    res_logs = client.get("/api/sms/logs?complaint_id=CP-API-SMS-1")
    assert res_logs.status_code == 200
    logs_data = res_logs.json()
    assert len(logs_data) >= 1
    assert logs_data[0]["complaint_id"] == "CP-API-SMS-1"

    print("[PASS] /api/sms/send and /api/sms/logs API endpoints verified successfully!")


if __name__ == "__main__":
    test_sms_gateway_direct_dispatch()
    test_sms_integration_via_complaint_lifecycle()
    test_sms_api_endpoints()
    print("\n[SUCCESS] ALL SMS REAL-TIME UPDATE TESTS PASSED CLEANLY!")
