import sys
import os
import json
import uuid

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starlette.testclient import TestClient
from server import app

client = TestClient(app)

def test_reverse_geocoding():
    coords = [
        (28.6139, 77.2090, "India / Delhi"),
        (-23.5505, -46.6333, "Brazil / Sao Paulo"),
        (-26.2041, 28.0473, "South Africa / Joburg")
    ]
    for lat, lon, label in coords:
        url = f"/api/location/reverse?lat={lat}&lon={lon}"
        resp = client.get(url)
        assert resp.status_code == 200
        data = resp.json()
        assert data.get('status') == 'ok', f"Failed for {label}: {data}"
        assert 'address' in data, f"Missing address for {label}"
        assert 'ward' in data, f"Missing ward for {label}"
        print(f"[PASS] Geocoding for {label}: Address='{data['address']}', Ward='{data['ward']}'")

def test_voice_transcribe_json():
    sectors = [
        ("Water Distribution & Pipeline Integrity", "en"),
        ("Roads, Bridges & Arterial Corridors", "hi"),
        ("Power Grid & High-Voltage Transmission", "pt"),
        ("Solid Waste Management & Sanitation", "ta")
    ]
    for sector, lang in sectors:
        url = "/api/voice/transcribe"
        payload = {"sector": sector, "lang": lang}
        resp = client.post(url, json=payload)
        assert resp.status_code == 200
        data = resp.json()
        assert data.get('status') == 'ok', f"Failed for {sector}: {data}"
        assert 'transcript' in data and len(data['transcript']) > 10, f"Transcript empty for {sector}"
        print(f"[PASS] Voice transcription for '{sector}' [{lang}] via {data.get('engine')}: length={len(data['transcript'])} chars")

def test_voice_transcribe_multipart():
    url = "/api/voice/transcribe"
    files = {"audio": ("report.webm", b"\x1a\x45\xdf\xa3\x9f\x42\x86\x81\x01\x42\xf7\x81\x01", "audio/webm")}
    data = {"sector": "Emergency Healthcare", "lang": "en"}
    resp = client.post(url, data=data, files=files)
    assert resp.status_code == 200
    res_data = resp.json()
    assert res_data.get('status') == 'ok', f"Failed multipart: {res_data}"
    assert 'transcript' in res_data and len(res_data['transcript']) > 5, "Multipart transcript empty"
    print(f"[PASS] Voice multipart transcription: length={len(res_data['transcript'])} chars, status={res_data['status']}")

if __name__ == "__main__":
    print("Running voice & location API integration tests...")
    test_reverse_geocoding()
    test_voice_transcribe_json()
    test_voice_transcribe_multipart()
    print("ALL TESTS PASSED SUCCESSFULLY!")

