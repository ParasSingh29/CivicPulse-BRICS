# ==============================================================================
# DIGITAL PUBLIC GOOD (DPG) SPECIFICATION & OPEN API COMPLIANCE
# ==============================================================================

DPG_INDICATORS = [
    {
        "standard": "1. SDG Alignment",
        "status": "✅ Compliant",
        "description": "Aligns with UN Sustainable Development Goals: SDG 9 (Infrastructure), SDG 11 (Sustainable Cities & Communities), and SDG 16 (Inclusive Governance)."
    },
    {
        "standard": "2. Open Source Licensing",
        "status": "✅ Apache 2.0 / MIT",
        "description": "All core code, models, and UI components are fully open-sourced with unrestricted public usage."
    },
    {
        "standard": "3. Open Data & Interoperability",
        "status": "✅ NDSAP & OGD Ready",
        "description": "Exposes standard RESTful endpoints and newline-delimited JSON for national data hubs (data.gov.in, dados.gov.br, data.gov.za)."
    },
    {
        "standard": "4. Privacy & Consent (DPDP / LGPD)",
        "status": "✅ Privacy-by-Design",
        "description": "Fully anonymized citizen telemetry. Passwords hashed using PBKDF2-HMAC-SHA256. Optional guest and anonymous whistleblowing mode."
    },
    {
        "standard": "5. Multilingual & Inclusion",
        "status": "✅ Voice & 5+ Dialects",
        "description": "Empowers low-literacy citizens via voice recording, Google Text-to-Speech audio playback, and vernacular language translation."
    },
    {
        "standard": "6. Cross-Border Portability",
        "status": "✅ BRICS Compatible",
        "description": "Architected with multi-nation jurisdiction adapters easily deployable across India, Brazil, South Africa, and emerging economies."
    }
]

DPG_COMPLIANCE_STANDARDS = DPG_INDICATORS

OPENAPI_SPEC = {
    "openapi": "3.0.3",
    "info": {
        "title": "CivicPulse-BRICS Digital Public Good (DPG) API",
        "description": "Standardized RESTful API for citizen demand aggregation, CapEx budget realignment, Gemini multimodal AI defect triage, and BRICS sovereign cross-border infrastructure collaboration.",
        "version": "2.0.0",
        "license": {
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
        }
    },
    "servers": [
        {"url": "http://localhost:8000", "description": "Local Sovereign Node"},
        {"url": "https://civicpulse.brics.gov", "description": "BRICS Federated Production Mesh"}
    ],
    "paths": {
        "/api/complaints": {
            "get": {
                "summary": "Retrieve citizen complaints with optional city, sector, and ward filtering.",
                "parameters": [
                    {"name": "city", "in": "query", "required": False, "schema": {"type": "string"}},
                    {"name": "sector", "in": "query", "required": False, "schema": {"type": "string"}},
                    {"name": "ward", "in": "query", "required": False, "schema": {"type": "string"}}
                ],
                "responses": {
                    "200": {"description": "Array of citizen infrastructure complaints."}
                }
            },
            "post": {
                "summary": "Submit a citizen complaint with optional photo vision diagnosis and voice note transcription.",
                "responses": {
                    "201": {"description": "Complaint registered successfully."}
                }
            }
        },
        "/api/city-proposals": {
            "get": {
                "summary": "Retrieve proposals filed by city officials for central government review.",
                "responses": {
                    "200": {"description": "List of municipal strategic infrastructure proposals."}
                }
            },
            "post": {
                "summary": "File a new municipal infrastructure proposal for central CapEx funding.",
                "responses": {
                    "201": {"description": "Proposal transmitted to central planning commission."}
                }
            }
        },
        "/api/central/ai/brics-plans": {
            "get": {
                "summary": "Synthesize AI-driven bilateral Joint Venture proposals across BRICS nations.",
                "responses": {
                    "200": {"description": "BRICS bilateral infrastructure project recommendations."}
                }
            }
        },
        "/api/voice/transcribe": {
            "post": {
                "summary": "Transcribe citizen audio using Gemini Multimodal Speech Processing Agent.",
                "responses": {
                    "200": {"description": "Transcript in native language and English translation."}
                }
            }
        },
        "/api/dpg/standards": {
            "get": {
                "summary": "Retrieve Digital Public Good Alliance (DPGA) standard compliance indicators.",
                "responses": {
                    "200": {"description": "Compliance status against DPGA criteria."}
                }
            }
        }
    }
}

def get_openapi_spec():
    """Returns standard OpenAPI 3.0 specification dictionary."""
    return OPENAPI_SPEC

