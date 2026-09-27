import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    blank_layout = prs.slide_layouts[6]
    
    # Colors
    BG_DARK = RGBColor(10, 13, 20)       # #0A0D14
    CARD_BG = RGBColor(18, 24, 38)       # #121826
    CARD_BORDER = RGBColor(30, 41, 59)   # #1E293B
    CYAN = RGBColor(6, 182, 212)         # #06B6D4
    BLUE = RGBColor(59, 130, 246)        # #3B82F6
    GOLD = RGBColor(245, 158, 11)        # #F59E0B
    RED = RGBColor(239, 68, 68)          # #EF4444
    GREEN = RGBColor(16, 185, 129)       # #10B981
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_LIGHT = RGBColor(243, 244, 246) # #F3F4F6
    TEXT_MUTED = RGBColor(156, 163, 175) # #9CA3AF
    
    def set_slide_background(slide):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = BG_DARK

    def add_header(slide, title_text, subtitle_text, slide_num_str):
        # Header text box
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(10.5), Inches(1.1))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = 'Segoe UI'
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        
        p2 = tf.add_paragraph()
        p2.text = subtitle_text
        p2.font.name = 'Segoe UI'
        p2.font.size = Pt(13)
        p2.font.color.rgb = CYAN
        p2.space_before = Pt(4)
        
        # Slide number tag
        tb_num = slide.shapes.add_textbox(Inches(11.5), Inches(0.4), Inches(1.0), Inches(0.5))
        tf_num = tb_num.text_frame
        p_num = tf_num.paragraphs[0]
        p_num.text = slide_num_str
        p_num.font.name = 'Consolas'
        p_num.font.size = Pt(12)
        p_num.font.color.rgb = TEXT_MUTED
        p_num.alignment = PP_ALIGN.RIGHT

    def add_footer(slide, category_str):
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.7), Inches(0.4))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        p.text = f"CivicPulse-BRICS • Track 1 Official Pitch Deck  |  {category_str}"
        p.font.name = 'Segoe UI'
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title, body, icon="", accent_color=CYAN):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = CARD_BG
        shape.line.color.rgb = CARD_BORDER
        shape.line.width = Pt(1)
        
        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        p.text = f"{icon} {title}".strip()
        p.font.name = 'Segoe UI'
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = accent_color
        
        p2 = tf.add_paragraph()
        p2.text = body
        p2.font.name = 'Segoe UI'
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(8)

    def add_screenshot_placeholder(slide, left, top, width, height, title_str, url_str, bullet_notes):
        # Dashed Border Box
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor(12, 17, 28)
        shape.line.color.rgb = CYAN
        shape.line.width = Pt(2)
        
        tb = slide.shapes.add_textbox(left + Inches(0.3), top + Inches(0.3), width - Inches(0.6), height - Inches(0.6))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        # Icon & Title
        p_head = tf.paragraphs[0]
        p_head.text = f"📸  {title_str}"
        p_head.font.name = 'Segoe UI'
        p_head.font.size = Pt(15)
        p_head.font.bold = True
        p_head.font.color.rgb = CYAN
        p_head.alignment = PP_ALIGN.CENTER
        
        # URL Label
        p_url = tf.add_paragraph()
        p_url.text = f"URL: {url_str}"
        p_url.font.name = 'Consolas'
        p_url.font.size = Pt(11)
        p_url.font.color.rgb = GOLD
        p_url.space_before = Pt(6)
        p_url.alignment = PP_ALIGN.CENTER
        
        # Note header
        p_note_hdr = tf.add_paragraph()
        p_note_hdr.text = "Capture & Insert Instructions:"
        p_note_hdr.font.name = 'Segoe UI'
        p_note_hdr.font.size = Pt(11)
        p_note_hdr.font.bold = True
        p_note_hdr.font.color.rgb = TEXT_WHITE
        p_note_hdr.space_before = Pt(14)
        
        for note in bullet_notes:
            p_b = tf.add_paragraph()
            p_b.text = f"• {note}"
            p_b.font.name = 'Segoe UI'
            p_b.font.size = Pt(10.5)
            p_b.font.color.rgb = TEXT_MUTED
            p_b.space_before = Pt(4)

    # =========================================================================
    # SLIDE 1: COVER
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)
    
    # Translucent Watermark Logo in background
    logo_wm_path = os.path.join(os.path.dirname(__file__), "static", "img", "brics_logo_watermark.png")
    if os.path.exists(logo_wm_path):
        wm_width = Inches(5.6)
        wm_height = Inches(6.15)
        wm_left = (prs.slide_width - wm_width) / 2
        wm_top = (prs.slide_height - wm_height) / 2
        slide1.shapes.add_picture(logo_wm_path, wm_left, wm_top, wm_width, wm_height)
    
    # Hero Title Box
    tb_c = slide1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(4.5))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True
    
    p = tf_c.paragraphs[0]
    p.text = "BRICS INNOVATION THEME • TRACK 1 OFFICIAL SUBMISSION"
    p.font.name = 'Segoe UI'
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = GOLD
    p.alignment = PP_ALIGN.CENTER
    
    p2 = tf_c.add_paragraph()
    p2.text = "⚡ CivicPulse-BRICS"
    p2.font.name = 'Segoe UI'
    p2.font.size = Pt(44)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    p2.space_before = Pt(10)
    p2.alignment = PP_ALIGN.CENTER
    
    p_by = tf_c.add_paragraph()
    p_by.text = "by Syntax Error"
    p_by.font.name = 'Segoe UI'
    p_by.font.size = Pt(14)
    p_by.font.bold = True
    p_by.font.color.rgb = CYAN
    p_by.space_before = Pt(4)
    p_by.alignment = PP_ALIGN.CENTER
    
    p3 = tf_c.add_paragraph()
    p3.text = "AI for Digital Public Infrastructure (DPI) & Governance: A Sovereign Multilingual AI Platform for Multichannel Citizen Petition Aggregation and CapEx Infrastructure Budget Realignment."
    p3.font.name = 'Segoe UI'
    p3.font.size = Pt(16)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(16)
    p3.alignment = PP_ALIGN.CENTER
    
    p4 = tf_c.add_paragraph()
    p4.text = "🇮🇳 India Node (Delhi NCR)   •   🇧🇷 Brazil Node (São Paulo)   •   🇿🇦 South Africa Node (Gauteng)"
    p4.font.name = 'Segoe UI'
    p4.font.size = Pt(13)
    p4.font.bold = True
    p4.font.color.rgb = CYAN
    p4.space_before = Pt(28)
    p4.alignment = PP_ALIGN.CENTER
    
    add_footer(slide1, "Cover & Executive Summary")

    # =========================================================================
    # SLIDE 2: THE PROBLEM
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, "The Problem: Governance & CapEx Friction", "Track 1 Challenge — Fragmented feedback & misaligned capital investments", "02 / 12")
    
    # 2x2 Grid of cards
    add_card(slide2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.2), "Fragmented Citizen Feedback", "Citizen petitions & development requests live in disconnected departmental channels, voice messages, and paper files with zero unified aggregation engine.", icon="🔴", accent_color=RED)
    add_card(slide2, Inches(6.9), Inches(1.8), Inches(5.6), Inches(2.2), "Misaligned CapEx Spending", "Millions in capital expenditure (CapEx) are allocated to low-demand projects while critical citizen infrastructure hotspots remain severely neglected.", icon="🔴", accent_color=RED)
    add_card(slide2, Inches(0.8), Inches(4.3), Inches(5.6), Inches(2.2), "Unaddressed Infrastructure Failures", "Stormwater pipelines, failing power grids, and transit culverts remain unmonitored until catastrophic climate or urban emergencies strike.", icon="🔴", accent_color=RED)
    add_card(slide2, Inches(6.9), Inches(4.3), Inches(5.6), Inches(2.2), "Missing Demographic & Risk Data", "Lack of cross-analysis combining citizen petitions with population density census data, vulnerability indices, and live IMD meteorological risk vectors.", icon="🔴", accent_color=RED)
    
    add_footer(slide2, "The Problem Statement")

    # =========================================================================
    # SLIDE 3: THE SOLUTION
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, "The Solution: CivicPulse-BRICS Platform", "A Sovereign Multilingual AI Platform & Federated Digital Public Good", "03 / 12")
    
    add_card(slide3, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.7), "01. Multichannel Gateway", "Native voice notes, photo defect scans, and an automated WhatsApp & Telegram bot webhook aggregating citizen petitions across diverse languages without requiring app installs.", icon="💬", accent_color=CYAN)
    add_card(slide3, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.7), "02. AI Budget Deficit Engine", "Cross-analyzes weighted citizen demand against actual government CapEx budgets in real-time, surfacing severe spending deficits and misallocations instantly.", icon="📊", accent_color=GOLD)
    add_card(slide3, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.7), "03. Gemini Policy Directives", "Generates multi-crore capital budget reallocation directives and strategic national infrastructure megaplans for policymakers and ministers.", icon="🤖", accent_color=GREEN)
    
    add_footer(slide3, "Core Solution Pillars")

    # =========================================================================
    # SLIDE 4: WHO IT SERVES
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, "Who It Serves: Core Stakeholders", "Empowering citizens, municipal field crews, central ministers, and BRICS nations", "04 / 12")
    
    add_card(slide4, Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.2), "1. Citizens & Community Voice", "File petitions in native languages via WhatsApp, Telegram, or Web. Voice-to-text translation and real-time status tracking.", icon="🗣️", accent_color=CYAN)
    add_card(slide4, Inches(6.9), Inches(1.8), Inches(5.6), Inches(2.2), "2. City Municipal Repair Crews", "Automated task queue prioritized by AI severity ratings (1-10) + 1-tap Google Maps turn-by-turn route dispatch for field trucks.", icon="🏙️", accent_color=BLUE)
    add_card(slide4, Inches(0.8), Inches(4.3), Inches(5.6), Inches(2.2), "3. Central Ministries & Policymakers", "GIS Demand Hotspot Heatmaps, CapEx misalignment alerts, IMD weather risk vectors, and Gemini executive policy directives.", icon="🏛️", accent_color=GOLD)
    add_card(slide4, Inches(6.9), Inches(4.3), Inches(5.6), Inches(2.2), "4. BRICS Sovereign Nations", "Federated node architecture (India Delhi, Brazil São Paulo, South Africa Gauteng) with cross-border Digital Public Good asset sharing.", icon="🌐", accent_color=GREEN)
    
    add_footer(slide4, "Stakeholders & Governance")

    # =========================================================================
    # SLIDE 5: AI APPROACH & ARCHITECTURE
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, "AI Approach & Multi-Agent Architecture", "Powered by Google Gemini 2.5 Pro & Flash multi-agent intelligence", "05 / 12")
    
    add_card(slide5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.2), "Gemini Vision Defect Agent", "Analyzes uploaded infrastructure photos, automatically classifying defect type, severity score (1-10), structural hazard rating, and priority code.", icon="📸", accent_color=CYAN)
    add_card(slide5, Inches(6.9), Inches(1.8), Inches(5.6), Inches(2.2), "Multilingual Speech & Translation", "Converts native voice notes in Hindi, Portuguese, or Zulu to text, translates to English, and generates audio synthesis with Google TTS.", icon="🎙️", accent_color=BLUE)
    add_card(slide5, Inches(0.8), Inches(4.3), Inches(5.6), Inches(2.2), "CapEx Budget Alignment Engine", "Correlates citizen petition density with census demographics, weather risk vectors, and public investment plans to calculate budget misalignment.", icon="📊", accent_color=GOLD)
    add_card(slide5, Inches(6.9), Inches(4.3), Inches(5.6), Inches(2.2), "Gemini Policy Directive Agent", "Synthesizes executive policy recommendations and multi-million dollar CapEx budget reallocation proposals for national ministers.", icon="🤖", accent_color=GREEN)
    
    add_footer(slide5, "AI Architecture & Models")

    # =========================================================================
    # SLIDE 6: PROTOTYPE DEMO 1 - CITIZEN PORTAL
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, "Live Prototype Demo: Citizen Voice & DPI Gateway", "Multilingual voice recorder, multimodal vision defect scanner & weather HUD", "06 / 12")
    
    # Left Feature Summary Box
    add_card(slide6, Inches(0.8), Inches(1.8), Inches(4.8), Inches(4.7), "Citizen Gateway Features", "• Multimodal AI Vision Scanner: Photo defect classification & 8.7/10 severity rating.\n\n• Multilingual Voice Petitions: Speech recorder with Hindi/English translation toggle.\n\n• WhatsApp & Telegram Webhook: Instant bot petition filing without downloading apps.\n\n• Live IMD Weather Risk HUD: Real-time monsoon and flood risk vectors.", icon="🚀", accent_color=CYAN)
    
    # Right Placeholder Box
    add_screenshot_placeholder(
        slide6, Inches(5.9), Inches(1.8), Inches(6.6), Inches(4.7),
        "SCREENSHOT DEMO: CITIZEN PORTAL & DPI GATEWAY",
        "http://localhost:8000/citizen",
        [
            "Voice Grievance Recorder with active wave audio visualizer & Hindi/English toggle.",
            "AI Multimodal Defect Scanner with uploaded road pothole image & severity score (8.7/10).",
            "WhatsApp & Telegram bot webhook messaging simulator panel.",
            "Live IMD Weather Risk HUD with monsoon/rainfall alert banners."
        ]
    )
    add_footer(slide6, "Prototype Screenshot — Citizen Portal")

    # =========================================================================
    # SLIDE 7: PROTOTYPE DEMO 2 - CITY OPERATIONS
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, "Live Prototype Demo: City Operations & Field Triage", "Real-time repair queue, priority scoring & Google Maps navigation", "07 / 12")
    
    add_card(slide7, Inches(0.8), Inches(1.8), Inches(4.8), Inches(4.7), "City Operations Features", "• Real-Time Repair Queue: Dynamic ranking by AI severity score (Critical 9.2/10).\n\n• Automated Crew Dispatch: Real-time status tracking for repair trucks (Truck-01 En Route).\n\n• Google Maps Field Routing: 1-Tap turn-by-turn route dispatch for municipal vehicles.\n\n• Operational Efficiency: Zero manual sorting overhead for field engineers.", icon="🏙️", accent_color=BLUE)
    
    add_screenshot_placeholder(
        slide7, Inches(5.9), Inches(1.8), Inches(6.6), Inches(4.7),
        "SCREENSHOT DEMO: CITY OPERATIONS & FIELD TRIAGE",
        "http://localhost:8000/city-official",
        [
            "Live City Repair Queue with prioritized task cards & CRITICAL (9.2/10) badges.",
            "Automated Field Crew Dispatch table showing repair truck status (Truck-01 En Route).",
            "Interactive Google Maps Field Route preview with turn-by-turn navigation overlay."
        ]
    )
    add_footer(slide7, "Prototype Screenshot — City Official Portal")

    # =========================================================================
    # SLIDE 8: PROTOTYPE DEMO 3 - GOVERNMENT COMMAND
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(slide8, "Live Prototype Demo: National Ministry Command", "GIS demand heatmap, CapEx misalignment matrix & Gemini directives", "08 / 12")
    
    add_card(slide8, Inches(0.8), Inches(1.8), Inches(4.8), Inches(4.7), "National Command Features", "• Spatial Demand Hotspots: Interactive Leaflet GIS map visualizing high citizen demand zones.\n\n• CapEx Misalignment Matrix: Flags severe budget deficits (88% demand vs 24% budget).\n\n• Gemini Policy Directives: Automated multi-crore capital budget reallocation proposals.\n\n• Public Investment Integration: Connects directly with national capital budgets.", icon="🏛️", accent_color=GOLD)
    
    add_screenshot_placeholder(
        slide8, Inches(5.9), Inches(1.8), Inches(6.6), Inches(4.7),
        "SCREENSHOT DEMO: NATIONAL MINISTRY COMMAND & CAPEX MATRIX",
        "http://localhost:8000/government",
        [
            "Interactive GIS Spatial Demand Heatmap over Delhi NCR coordinates.",
            "CapEx Budget Misalignment Matrix comparing citizen demand index (88%) vs allocated budget (24%).",
            "Google Gemini 2.5 Executive Directives detailing recommended budget shifts."
        ]
    )
    add_footer(slide8, "Prototype Screenshot — Government Command")

    # =========================================================================
    # SLIDE 9: PROTOTYPE DEMO 4 - BRICS SOVEREIGN HUB
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9)
    add_header(slide9, "Live Prototype Demo: BRICS Sovereign Minister Hub", "Multi-nation federation nodes, Gemini megaplans & UN SDG telemetry", "09 / 12")
    
    add_card(slide9, Inches(0.8), Inches(1.8), Inches(4.8), Inches(4.7), "BRICS Hub Features", "• Multi-Country Jurisdiction: Switch between India (Delhi), Brazil (São Paulo), and South Africa (Gauteng).\n\n• Strategic Megaplans: Automated generation of multi-million infrastructure overhauls ($45M CapEx).\n\n• UN SDG Telemetry: Live progress tracking against UN SDGs 9, 11, and 16.\n\n• Cross-Border Exchange: Federated DPG data sharing between BRICS nations.", icon="🌐", accent_color=GREEN)
    
    add_screenshot_placeholder(
        slide9, Inches(5.9), Inches(1.8), Inches(6.6), Inches(4.7),
        "SCREENSHOT DEMO: BRICS SOVEREIGN MINISTER HUB",
        "http://localhost:8000/central-official",
        [
            "Multi-nation jurisdiction node selector (India Delhi, Brazil São Paulo, South Africa Gauteng).",
            "Google Gemini 2.5 Strategic Megaplans ($45M Drainage Infrastructure Overhaul).",
            "UN SDG Alignment Telemetry (SDG 9, 11, 16 metrics) & DPG Exchange status."
        ]
    )
    add_footer(slide9, "Prototype Screenshot — BRICS Sovereign Hub")

    # =========================================================================
    # SLIDE 10: DPG ALIGNMENT & OPEN STANDARDS
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide10)
    add_header(slide10, "Digital Public Good (DPG) & Open Standards", "Built for open governance, interoperability, and privacy", "10 / 12")
    
    add_card(slide10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.2), "OpenAPI 3.0 Webhook Specification", "Fully compliant standard webhook endpoint (POST /api/v1/dpg/messaging-webhook) for instant integration with national messaging platforms.", icon="📜", accent_color=CYAN)
    add_card(slide10, Inches(6.9), Inches(1.8), Inches(5.6), Inches(2.2), "Privacy & Security by Design", "Anonymized citizen telemetry and salted PBKDF2-HMAC-SHA256 password hashing. Zero persistent tracking of sensitive personal identities.", icon="🔒", accent_color=BLUE)
    add_card(slide10, Inches(0.8), Inches(4.3), Inches(5.6), Inches(2.2), "UN SDG Strategic Alignment", "Directly contributes to UN SDG 9 (Industry & Infrastructure), SDG 11 (Sustainable Cities), and SDG 16 (Peace, Justice & Strong Institutions).", icon="🌐", accent_color=GREEN)
    add_card(slide10, Inches(6.9), Inches(4.3), Inches(5.6), Inches(2.2), "Open Data & Interoperability", "Exports structured JSON-LD schemas and GIS records compatible with open government portals like data.gov.in and dados.gov.br.", icon="🔓", accent_color=GOLD)
    
    add_footer(slide10, "DPG Alliance Standards")

    # =========================================================================
    # SLIDE 11: DEPLOYABILITY, BRICS SCALE & GOOGLE TECH STACK
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide11)
    add_header(slide11, "Deployability, BRICS Scale & Google Tech Stack", "Cloud Run containerization, federated jurisdiction nodes & Google Cloud AI architecture", "11 / 12")
    
    # Left: Federated Sovereign Nodes
    add_card(slide11, Inches(0.8), Inches(1.8), Inches(5.6), Inches(1.5), "🇮🇳 India Node (Delhi NCR)", "• PM Gati Shakti spatial portal & data.gov.in integration\n• Live IMD meteorological weather telemetry HUD\n• CapEx alignment with national ministry priorities", accent_color=CYAN)
    add_card(slide11, Inches(0.8), Inches(3.45), Inches(5.6), Inches(1.5), "🇧🇷 Brazil Node (São Paulo)", "• PAC (Programa de Aceleração do Crescimento) integration\n• Brazilian Open Data (dados.gov.br) & Portuguese triage\n• Amazonian watershed flood & vulnerability indices", accent_color=GREEN)
    add_card(slide11, Inches(0.8), Inches(5.1), Inches(5.6), Inches(1.5), "🇿🇦 South Africa Node (Gauteng)", "• Municipal Infrastructure Grants (MIG) registry integration\n• Multilingual Zulu & English speech triage agent\n• Township power grid & water resilience tracking", accent_color=GOLD)
    
    # Right: Google Cloud Hackathon Tech Stack (2x2 grid)
    add_card(slide11, Inches(6.8), Inches(1.8), Inches(2.8), Inches(2.35), "Gemini 2.5 AI", "Google Gemini 2.5 Pro & Flash multi-agent defect triage, voice translation, and strategic policy directives.", icon="🤖", accent_color=CYAN)
    add_card(slide11, Inches(9.8), Inches(1.8), Inches(2.8), Inches(2.35), "Google Maps", "Interactive spatial pinpointing & 1-tap turn-by-turn routing for municipal repair trucks.", icon="🗺️", accent_color=BLUE)
    add_card(slide11, Inches(6.8), Inches(4.25), Inches(2.8), Inches(2.35), "Cloud Run", "Serverless containerized microservices running high-performance asynchronous Python ASGI core.", icon="☁️", accent_color=GOLD)
    add_card(slide11, Inches(9.8), Inches(4.25), Inches(2.8), Inches(2.35), "BigQuery GIS", "Spatial warehouse (POINT coordinates) for macro analysis + Firebase Cloud Firestore realtime sync.", icon="⚡", accent_color=GREEN)
    
    add_footer(slide11, "BRICS Federation & Google Tech Stack")

    # =========================================================================
    # SLIDE 12: THANK YOU & TEAM MEMBERS
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide12)
    
    # Big THANK YOU & by Syntax Error Header
    tb_ty = slide12.shapes.add_textbox(Inches(1.0), Inches(0.35), Inches(11.333), Inches(1.75))
    tf_ty = tb_ty.text_frame
    tf_ty.word_wrap = True
    
    p_ty = tf_ty.paragraphs[0]
    p_ty.text = "THANK YOU"
    p_ty.font.name = 'Segoe UI'
    p_ty.font.size = Pt(42)
    p_ty.font.bold = True
    p_ty.font.color.rgb = TEXT_WHITE
    p_ty.alignment = PP_ALIGN.CENTER
    
    p_by = tf_ty.add_paragraph()
    p_by.text = "by Syntax Error"
    p_by.font.name = 'Segoe UI'
    p_by.font.size = Pt(16)
    p_by.font.bold = True
    p_by.font.color.rgb = CYAN
    p_by.space_before = Pt(2)
    p_by.alignment = PP_ALIGN.CENTER
    
    p_sub = tf_ty.add_paragraph()
    p_sub.text = "AI for Digital Public Infrastructure (DPI) & Governance  •  Track 1 Official Submission"
    p_sub.font.name = 'Segoe UI'
    p_sub.font.size = Pt(11)
    p_sub.font.color.rgb = TEXT_MUTED
    p_sub.space_before = Pt(4)
    p_sub.alignment = PP_ALIGN.CENTER
    
    # 4 Simple Team Member Cards (Name, Contribution, LinkedIn)
    team_members = [
        (
            "Paras Singh",
            "Team Lead & Full-Stack. Project concept & AI system design. Built core platform & connected all portals.",
            "linkedin.com/in/paras-singh",
            CYAN
        ),
        (
            "Aradhara Pal",
            "Frontend & UI/UX Designer. Designed website layouts & mobile screens. Created dashboards for citizens & officials.",
            "linkedin.com/in/",
            GREEN
        ),
        (
            "Anshika Anand",
            "Backend Developer. Set up server, database & Render hosting.",
            "linkedin.com/in/",
            GOLD
        ),
        (
            "Himanshi",
            "Product Research & Testing. Researched city budget data & guidelines. Tested user workflows & documentation.",
            "linkedin.com/in/",
            BLUE
        ),
    ]
    
    card_w = Inches(2.8)
    card_h = Inches(4.0)
    spacing = Inches(0.18)
    start_left = Inches(0.8)
    
    for i, (name, contrib, linkedin, color) in enumerate(team_members):
        left_pos = start_left + i * (card_w + spacing)
        
        # Card Background
        card_shape = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, Inches(2.25), card_w, card_h)
        card_shape.fill.solid()
        card_shape.fill.fore_color.rgb = CARD_BG
        card_shape.line.color.rgb = CARD_BORDER
        card_shape.line.width = Pt(1)
        
        tb = slide12.shapes.add_textbox(left_pos + Inches(0.2), Inches(2.35), card_w - Inches(0.4), card_h - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        
        # Member Name
        p_name = tf.paragraphs[0]
        p_name.text = name
        p_name.font.name = 'Segoe UI'
        p_name.font.size = Pt(14)
        p_name.font.bold = True
        p_name.font.color.rgb = TEXT_WHITE
        p_name.alignment = PP_ALIGN.CENTER
        
        # Contribution Header
        p_ch = tf.add_paragraph()
        p_ch.text = "CONTRIBUTION"
        p_ch.font.name = 'Segoe UI'
        p_ch.font.size = Pt(9.5)
        p_ch.font.bold = True
        p_ch.font.color.rgb = GOLD
        p_ch.space_before = Pt(8)
        
        # Contribution Text
        p_cb = tf.add_paragraph()
        p_cb.text = contrib
        p_cb.font.name = 'Segoe UI'
        p_cb.font.size = Pt(10)
        p_cb.font.color.rgb = TEXT_MUTED
        p_cb.space_before = Pt(3)
        
        # LinkedIn Header
        p_lh = tf.add_paragraph()
        p_lh.text = "LINKEDIN"
        p_lh.font.name = 'Segoe UI'
        p_lh.font.size = Pt(9.5)
        p_lh.font.bold = True
        p_lh.font.color.rgb = color
        p_lh.space_before = Pt(10)
        
        # LinkedIn Link
        p_lb = tf.add_paragraph()
        p_lb.text = f"🔗 {linkedin}"
        p_lb.font.name = 'Segoe UI'
        p_lb.font.size = Pt(9.5)
        p_lb.font.color.rgb = TEXT_LIGHT
        p_lb.space_before = Pt(2)
    
    # Project Footer Box
    shape_ft = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.45), Inches(11.8), Inches(0.4))
    shape_ft.fill.solid()
    shape_ft.fill.fore_color.rgb = CARD_BG
    shape_ft.line.color.rgb = CARD_BORDER
    shape_ft.line.width = Pt(1)
    
    tb_ft = slide12.shapes.add_textbox(Inches(1.0), Inches(6.48), Inches(11.4), Inches(0.35))
    tf_ft = tb_ft.text_frame
    p_ft = tf_ft.paragraphs[0]
    p_ft.text = "🌐 Live Demo: http://localhost:8000   •   💻 GitHub: https://github.com/ParasSingh29/CivicPulse-BRICS   •   📜 Apache 2.0 Open Source DPG"
    p_ft.font.name = 'Segoe UI'
    p_ft.font.size = Pt(9.5)
    p_ft.font.color.rgb = TEXT_MUTED
    p_ft.alignment = PP_ALIGN.CENTER
    
    add_footer(slide12, "Thank You • Team Syntax Error • Q&A")

    output_candidates = [
        "CivicPulse-BRICS_Pitch_Deck.pptx",
        "CivicPulse-BRICS_Pitch_Deck_Updated.pptx",
        "CivicPulse-BRICS_Pitch_Deck_Final.pptx",
        "CivicPulse-BRICS_Pitch_Deck_SyntaxError.pptx"
    ]
    saved_path = None
    for path in output_candidates:
        try:
            prs.save(path)
            saved_path = path
            print(f"Successfully generated PowerPoint presentation at: {os.path.abspath(path)}")
            break
        except PermissionError:
            continue
            
    if not saved_path:
        import time
        fallback = f"CivicPulse-BRICS_Pitch_Deck_{int(time.time())}.pptx"
        prs.save(fallback)
        print(f"Successfully generated presentation at: {os.path.abspath(fallback)}")

if __name__ == "__main__":
    create_deck()
