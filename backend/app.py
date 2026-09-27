"""
CivicPulse-BRICS: Sovereign Digital Public Good Platform
High-Performance Asynchronous REST API & Modern JavaScript Web Application Server
"""
import sys
import uvicorn
from server import app

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    print("[CivicPulse-BRICS] Launching Modern Web Application Server on http://localhost:8000 ...")
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)