# ⚡ CivicPulse-BRICS
### AI for Digital Public Infrastructure (DPI) & Governance
> **BRICS Innovation Theme • Track 1 Official Submission**  
> *A scalable, multilingual Digital Public Good (DPG) connecting citizen voices across messaging apps to national public investment priorities and capital expenditure allocation.*

---

## 🌍 The Problem (Track 1 Challenge)
Governments across BRICS nations often struggle to consolidate citizen development feedback and align it with national infrastructure spending. Development requests remain trapped in fragmented departmental silos, resulting in:
1. **Misaligned Public Spending:** Millions in capital expenditure (CapEx) allocated to low-demand areas while critical hotspots remain neglected.
2. **Unaddressed Infrastructure Gaps:** Water supply pipelines, failing power grids, and collapsed transit culverts unaddressed until emergencies occur.
3. **No Cross-Analysis with Demographics:** Lack of integration between citizen voice, population density census data, and vulnerability indices.

---

## 💡 The Solution: CivicPulse-BRICS
CivicPulse-BRICS is an open, federated **Digital Public Good (DPG)** that:
- **Aggregates Citizen Demand** via native voice notes, photos, and an automated **WhatsApp / Telegram DPI Gateway**.
- **Cross-Analyzes with Demographics:** Weights citizen feedback by population density and socio-economic vulnerability.
- **Identifies Public Budget Misalignment:** Compares actual citizen demand hotspots against planned government CapEx budgets, flagging severe deficits.
- **Generates National Policy Directives:** Uses **Google Gemini 2.5** to recommend multi-million capital budget reallocations to national policymakers and ministers.
- **Rule 04 Cross-Border Scalability:** Pre-configured with multi-nation jurisdiction nodes:
  - 🇮🇳 **India Node (Delhi NCR):** Integrated with PM Gati Shakti & data.gov.in.
  - 🇧🇷 **Brazil Node (São Paulo):** Integrated with PAC & Brazilian Open Data (dados.gov.br).
  - 🇿🇦 **South Africa Node (Johannesburg):** Integrated with Municipal Infrastructure Grants (MIG).

---

## 🏆 Google AI Hackathon Technology Stack Integration

| Hackathon Category | Recommended Google Technologies | CivicPulse-BRICS Implementation |
| :--- | :--- | :--- |
| **1. Generative AI & Agents** | Gemini API, Google AI Studio, Vertex AI | **Gemini 2.5 Pro & Flash** multi-agent autonomous triage & Smart City executive directives (`gemini_helper.py`). |
| **2. Vision & Multimodal** | Gemini Multimodal, Vertex AI Vision | **Gemini Vision Agent** analyzes uploaded photos for defect type, severity (1-10), hazard rating, and structural integrity diagnostics. |
| **3. Language & Voice** | Cloud Speech-to-Text, Translation, TTS | **Google Text-to-Speech (`gTTS`)** with `🔊 Listen / सुनें` audio reader in Hindi & English + Multilingual speech translation for 5 languages. |
| **4. Predictive Modelling** | Vertex AI (AutoML, model serving) | Dynamic infrastructure failure forecaster correlating citizen density with **live IMD weather risk vectors** (`public_data_helper.py`). |
| **5. Geospatial** | Google Maps Platform, Earth Engine | Interactive pinpointing + **1-tap "📍 Navigate with Google Maps"** turn-by-turn routing for field repair teams. |
| **6. Data & Backend** | BigQuery, Firebase, Cloud Run | **Firebase Cloud Firestore Engine** (`api_client.py`) + **Google BigQuery GIS Spatial Warehouse** (`POINT(lon lat)`) + **Pure JavaScript SPA** (Zero Streamlit, Zero CSV). |
| **7. Public Data** | data.gov.in, IMD, ISRO/Bhuvan | **Live IMD Meteorological Weather Station HUD** + **`data.gov.in` Public Civic Grievance Dataset Explorer**. |

---

## 🏛️ Digital Public Good (DPG) Alignment
CivicPulse-BRICS adheres strictly to the **Digital Public Goods Alliance (DPGA)** standard:
- **UN SDG Relevance:** SDG 9 (Industry, Innovation & Infrastructure), SDG 11 (Sustainable Cities), SDG 16 (Inclusive Governance).
- **Open Standards:** OpenAPI 3.0 specification (`POST /api/v1/dpg/messaging-webhook`).
- **Privacy by Design:** Anonymized citizen telemetry and salted PBKDF2-HMAC-SHA256 password security.
- **Interoperability:** JSON-LD schema compliant with national open government data platforms.

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10+ installed
- Google Gemini API Key (`GEMINI_API_KEY`)

### Local Installation
```bash
# 1. Clone the repository
git clone https://github.com/your-username/CivicPulse-BRICS.git
cd CivicPulse-BRICS

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your Google Gemini API Key
export GEMINI_API_KEY="your_api_key_here"  # On Windows: set GEMINI_API_KEY="your_key"

# 4. Launch the application
python app.py
```
Open **`http://localhost:8000`** in your browser.

---

## ☁️ Google Cloud Run Deployment

CivicPulse-BRICS is containerized and ready for 1-click deployment on **Google Cloud Run**:

```bash
# Build and deploy directly to Google Cloud Run
gcloud builds submit --config cloudbuild.yaml

# Or deploy via gcloud CLI
gcloud run deploy civicpulse-brics \
    --source . \
    --platform managed \
    --region asia-south1 \
    --allow-unauthenticated \
    --port 8080
```

---

## 👥 Contributors & License
Built for the **Google AI Hackathon — BRICS Track 1 (AI for Digital Public Infrastructure & Governance)**.  
Licensed under the **Apache 2.0 License** — Open Source Digital Public Good.
