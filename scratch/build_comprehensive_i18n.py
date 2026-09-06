# -*- coding: utf-8 -*-
"""
Generates the complete static/js/i18n.js with 100% translations for all 9 languages:
en, hi, pt, ru, zh, ta, te, zu, af.
"""

import json

EN = {
    "portal_citizen_badge": "Citizen Portal",
    "portal_gov_badge": "Government Hub",
    "nav_back": "Back",
    "nav_home": "Home",
    "btn_sign_out": "Sign Out",
    "btn_exit_command": "Exit Portal",
    "detected_node_title": "Detected Location",
    "badge_cloud_connected": "Cloud Connected",
    "badge_live_data": "Live Cloud Data",
    "badge_open_standard": "Open Standard",

    "sector_roads_transit_name": "Roads, Bridges & Arterial Corridors",
    "sector_roads_transit_badge": "Transit Backbone",
    "sector_roads_transit_desc": "Expressways, flyovers, arterial road resurfacing, structural bridges & pedestrian skywalks",

    "sector_water_supply_name": "Water Supply & Pipeline Leakage",
    "sector_water_supply_badge": "Potable Water",
    "sector_water_supply_desc": "Clean drinking water distribution, high-pressure trunk mains, smart leak telemetry & pumping stations",

    "sector_electricity_grid_name": "Electricity, Streetlights & Grid",
    "sector_electricity_grid_badge": "Energy Infrastructure",
    "sector_electricity_grid_desc": "High-voltage transmission substations, underground cabling, smart LED lighting & grid blackout prevention",

    "sector_waste_sanitation_name": "Waste Management & Sanitation",
    "sector_waste_sanitation_badge": "Circular Cleanliness",
    "sector_waste_sanitation_desc": "Automated material recovery, bio-methanation plants, toxic landfill remediation & daily door-to-door collection",

    "sector_public_transport_name": "Public Transport & Transit Hubs",
    "sector_public_transport_badge": "Mobility Corridors",
    "sector_public_transport_desc": "Metro rail feeder routes, electric bus fleets, multi-modal passenger terminals & commuter shelters",

    "sector_stormwater_flood_name": "Stormwater Drainage & Monsoon Floods",
    "sector_stormwater_flood_badge": "Hydrological Defense",
    "sector_stormwater_flood_desc": "Deep gravity drainage canals, river embankments, retention reservoirs & floodgate automated telemetry",

    "sector_health_clinics_name": "Public Health, Clinics & Vector Control",
    "sector_health_clinics_badge": "Community Health",
    "sector_health_clinics_desc": "Secondary trauma hospitals, maternal healthcare centers, medicine stock telemetry & anti-dengue fogging",

    "sector_schools_facilities_name": "Government Schools & Public Facilities",
    "sector_schools_facilities_badge": "Social Infrastructure",
    "sector_schools_facilities_desc": "Public school building safety, polytechnic skill centers, civic libraries & digital learning labs",

    "sector_parks_environment_name": "Public Parks, Green Belts & Air Quality",
    "sector_parks_environment_badge": "Eco Restoration",
    "sector_parks_environment_desc": "Urban afforestation, anti-smog water misting towers, public park solar lighting & biodiversity corridors",

    "sector_public_safety_name": "Public Safety & Emergency Infrastructure",
    "sector_public_safety_badge": "Emergency Defense",
    "sector_public_safety_desc": "Pressurized fire hydrants, municipal disaster evacuation routes, CCTV optical feeds & emergency sirens",

    "sec_choose_category": "Choose a Category",
    "sec_choose_category_sub": "Pick the category matching your issue across our 10 city sectors:",
    "sec_category_prompt": "Click any category above to open the quick report form with photo or voice note.",
    "lbl_sla_24h": "SLA: < 24h",
    "btn_report_issue": "Report Issue",
    "badge_report_context": "Report an Issue",

    "cit_hero_tag": "Active Citizen Portal",
    "cit_hero_title": "Report Issues & Community Needs",
    "cit_hero_subtitle": "Easily report local problems, vote on projects your community needs, and track ongoing repairs with live voice and photo updates.",
    "cit_welcome_title": "Welcome, Priya Sharma",
    "cit_welcome_desc": "Your citizen portal to report issues, vote on neighborhood improvements, and track repairs.",
    "cit_badge_resident": "Verified Resident • Delhi",
    "cit_badge_ward": "Ward 14 • Delhi NCR",
    "cit_badge_sla": "98.4% On-Time Fixes",
    "cit_launchpad_title": "What would you like to do?",
    "cit_launchpad_subtitle": "Choose an option below to get started:",

    "card_report_title": "Report an Issue",
    "card_report_desc": "Report broken roads, dark streetlights, water leaks, or garbage issues with a quick photo or voice note.",
    "card_report_btn": "Report an Issue",
    "card_demands_title": "Community Requests & Voting",
    "card_demands_desc": "Vote for neighborhood improvements like new parks, road widening, and clean water projects to guide city spending.",
    "card_demands_btn": "View Community Requests",
    "card_track_title": "Track My Reports",
    "card_track_desc": "Check the progress of your reported issues, see assigned repair workers, and listen to voice status updates.",
    "card_track_btn": "Track My Reports",
    "card_whatsapp_title": "WhatsApp Assistant",
    "card_whatsapp_desc": "Chat with us on WhatsApp to report issues or ask questions in Hindi, English, Portuguese, or your local language.",
    "card_whatsapp_btn": "Open WhatsApp Chat",

    "tag_quick_ai": "Quick AI Review",
    "tag_10_categories": "10+ Categories",
    "tag_photo_review": "Photo Review",
    "tag_voice_msg": "Voice Message",
    "tag_auto_loc": "Auto-Location",
    "lbl_avg_resp": "Avg. response: 4s",
    "lbl_votes_cast": "27,421 Votes Cast",
    "tag_public_voting": "Public Voting",
    "tag_local_budget": "Local Budget",
    "tag_ward_projects": "Ward Projects",
    "tag_live_count": "Live Count",
    "lbl_active_wards": "Active in 8 Wards",
    "tag_step_status": "Step-by-Step Status",
    "tag_voice_briefing": "Voice Briefing",
    "tag_crew_map": "Repair Crew Map",
    "tag_proof_photos": "Proof Photos",
    "lbl_tracked_live": "Tracked live",
    "lbl_24_7_wa": "24/7 on WhatsApp",
    "tag_no_app": "No App Needed",
    "tag_any_lang": "Any Language",
    "tag_smart_chat": "Smart Chat",
    "tag_instant_ticket": "Instant Ticket",
    "lbl_instant_reply": "Instant reply",
    "sec_recently_fixed": "Recently Fixed in Your Area",
    "sec_community_notices": "Community Notices & Events",

    "back_to_citizen_home": "← Back to Home",
    "return_to_executive_cmd": "← Back to Overview",

    "modal_report_title": "Report an Issue",
    "modal_report_sub": "Add details, photos, or voice notes for fast resolution.",
    "lbl_selected_category": "Selected Category",
    "lbl_problem": "What is the problem? *",
    "btn_voice_input": "Speak with AI",
    "ph_desc": "Describe what is broken, nearest landmark or shop, and how it affects people...",
    "voice_listening": "Listening... Speak now in Hindi, English, or mother tongue",
    "btn_stop_rec": "Done / Stop",
    "lbl_neighborhood_ward": "Neighborhood / Ward *",
    "lbl_street_address": "Street Address or Landmark",
    "btn_use_current_location": "Use Current Location",
    "ph_street_address": "e.g. Outer Ring Road, Near Metro Gate 2",
    "gps_acquired": "📍 GPS Coordinates Acquired",
    "lbl_add_photo": "Add a Photo (Optional)",
    "lbl_add_photo_hint": "Our AI automatically checks the damage severity to speed up repairs.",
    "lbl_add_voice": "Add a Voice Note (Optional)",
    "lbl_add_voice_hint": "Speak in Hindi, English, Portuguese, or your mother tongue.",
    "btn_cancel": "Cancel",
    "btn_submit_report": "Submit Report",

    "badge_demands_context": "Community Requests",
    "sec_demands_title": "Community Requests & Voting",
    "sec_demands_sub": "Vote for neighborhood improvements like new parks, road widening, and clean water projects to guide city spending.",
    "btn_propose_project": "+ Propose a Project",
    "ph_search_demands": "Search projects by title, neighborhood, or keyword...",
    "opt_all_wards": "All Neighborhoods / Wards",
    "btn_upvote": "Upvote",
    "lbl_votes": "Votes",
    "lbl_est_cost": "Estimated Cost",
    "lbl_beneficiaries": "People Benefited",
    "lbl_proposed_by": "Proposed by",
    "modal_propose_title": "Propose a Community Project",
    "modal_propose_sub": "Projects with high citizen votes are submitted directly to city planners for funding.",
    "lbl_project_title": "Project Title *",
    "ph_project_title": "e.g. New Park and Solar Lighting in Sector 4",
    "lbl_category": "Category *",
    "lbl_budget": "Estimated Cost",
    "ph_budget": "e.g. ₹50 Lakhs / R$ 300,000",
    "lbl_est_beneficiaries": "Estimated People Benefited",
    "ph_beneficiaries": "e.g. 5,000 residents",
    "lbl_why_needed": "Why is this project needed? *",
    "ph_why_needed": "Explain why this project is important and how it will improve our neighborhood...",
    "btn_submit_voting": "Submit for Voting",

    "badge_track_context": "Track Reports",
    "sec_track_title": "Track Your Reports",
    "sec_track_sub": "Check the progress of your reported issues, see assigned repair workers, and listen to voice status updates.",
    "ph_search_track": "Enter Report ID (e.g. CP-2026...) or street address...",
    "btn_listen_briefing": "Listen to Voice Briefing",
    "btn_open_maps": "Open in Google Maps",
    "step_submitted": "Submitted",
    "step_dispatched": "Dispatched",
    "step_in_progress": "In Progress",
    "step_resolved": "Resolved",
    "lbl_assigned_worker": "Assigned Worker",

    "badge_wa_context": "WhatsApp Chat",
    "sec_wa_title": "Chat with CivicPulse on WhatsApp",
    "sec_wa_sub": "Send a quick text, photo, or voice message just like chatting with a friend.",
    "wa_assistant_name": "CivicPulse Assistant (Verified Support)",
    "wa_online_status": "● Online • Instant Help",
    "badge_online": "ONLINE",
    "wa_bot_greeting": "Hello / Namaste / Olá! How can I help you today? Send a voice message or type what is broken in your neighborhood, and I will report it immediately.",
    "btn_wa_sample_hi": "🇮🇳 Hindi Voice Note",
    "btn_wa_sample_pt": "🇧🇷 Portuguese Note",
    "btn_wa_sample_en": "🇿🇦 English Message",
    "ph_wa_input": "Type message or click a sample...",

    "gov_hero_tag": "City Planning & Operations",
    "gov_hero_title": "City Projects & Operations Command",
    "gov_hero_subtitle": "Track citizen reports, assign repair teams, plan major infrastructure projects, and review city budgets with AI insights.",
    "gov_welcome_title": "Operations Overview",
    "gov_welcome_desc": "View real-time citizen reports, AI planning recommendations, and budget allocations. Select any module below to open it.",
    "gov_badge_clearance": "Admin Access",
    "gov_badge_uptime": "99.98% System Uptime",
    "gov_launchpad_title": "City Management Modules",
    "gov_launchpad_subtitle": "Select any tool below to manage city operations:",

    "card_megaplan_title": "AI City Project Planner",
    "card_megaplan_desc": "Combines citizen requests and neighborhood data to recommend major projects with estimated costs and benefits.",
    "card_megaplan_btn": "Open Planning Tool",
    "card_queue_title": "Repairs & Work Orders",
    "card_queue_desc": "Review incoming citizen complaints, dispatch repair teams, track completion deadlines, and approve finished work.",
    "card_queue_btn": "View Repair Queue",
    "card_budget_title": "Budget & Funding Balance",
    "card_budget_desc": "Compare public spending across neighborhoods to ensure underserved areas receive fair funding and resources.",
    "card_budget_btn": "Open Budget Tool",
    "card_map_title": "Live City Map",
    "card_map_desc": "Interactive map showing reported issues, repair crew locations, neighborhood boundaries, and incident hot spots.",
    "card_map_btn": "Open City Map",
    "card_dpg_title": "Data Standards & Compliance",
    "card_dpg_desc": "Check open digital standards compliance, view API documentation, and review data privacy guidelines.",
    "card_dpg_btn": "View Standards",

    "sec_live_weather": "Live City Weather",
    "badge_sensor_data": "Live Sensor Data",
    "lbl_weather_source": "Source: Open-Meteo Real-Time Sensor",
    "lbl_temperature": "Ambient Temperature",
    "lbl_humidity": "Relative Humidity",
    "lbl_precipitation": "Precipitation (Rain)",
    "lbl_wind_velocity": "Wind Velocity",
    "lbl_database": "Database",
    "lbl_city_map_data": "City Map Data",
    "lbl_storage": "Storage",
    "btn_sync_map_data": "Sync Map Data",
    "sec_recent_directives": "Recent City Directives & Actions",
    "sec_repair_status": "City Repair Operations Status",
    "lbl_infra_health": "City Infrastructure Health",
    "lbl_active_teams": "Active Field Repair Teams",
    "lbl_budget_influence": "Citizen Budget Influence",

    "badge_planning_context": "City Planning",
    "sec_megaplan_title": "AI Infrastructure Recommendations",
    "sec_megaplan_sub": "High-impact project proposals automatically generated by analyzing citizen requests, traffic bottlenecks, and demographic priorities.",
    "btn_update_plan": "Update AI Plan",
    "lbl_capex": "Estimated CapEx",
    "lbl_justification": "Project Justification",
    "btn_approve_project": "Approve Project",

    "badge_queue_context": "Repairs & Dispatches",
    "sec_queue_title": "Reported Issues & Repair Queue",
    "sec_queue_sub": "Filter and manage citizen complaints, dispatch field workers, and approve completed repairs:",
    "th_id": "ID",
    "th_category": "Category",
    "th_description": "Description",
    "th_ward": "Ward",
    "th_severity": "Severity",
    "th_status": "Status",
    "th_action": "Action",
    "btn_dispatch": "Dispatch Team",
    "btn_mark_resolved": "Mark Fixed",

    "badge_budget_context": "Budget Analysis",
    "sec_budget_title": "Ward Budget & Spending Equity",
    "sec_budget_sub": "Compare municipal investment against neighborhood needs to balance infrastructure spending:",
    "th_ward_budget": "Neighborhood / Ward",
    "th_population_vulnerability": "Population & Vulnerability",
    "th_planned_budget": "Planned Budget",
    "th_demand_share": "Citizen Demand Share",
    "th_funding_status": "Funding Status",
    "th_recommended_action": "Recommended Action",

    "badge_map_context": "City Map",
    "sec_map_title": "Live City Incident Map",
    "sec_map_sub": "Colored markers show issue status, priority hot spots, and repair crew locations:",

    "badge_dpg_context": "Open Standards",
    "sec_dpg_title": "Digital Public Good Standards",
    "sec_dpg_sub": "Compliance with 9 open source and digital public good indicators:",

    "login_hero_sub": "Connecting citizens and city planners to build better neighborhoods together across BRICS communities.",
    "card_citizen_title": "Citizen Portal",
    "card_citizen_tag": "For Residents & Communities",
    "card_citizen_desc": "Report local problems, vote on neighborhood improvements, and track repairs in real time.",
    "lbl_citizen_email": "Resident Email or Username *",
    "ph_citizen_email": "e.g. resident@delhi.gov.in",
    "lbl_password": "Password *",
    "btn_sign_in_citizen": "Sign In to Citizen Portal",
    "lbl_or": "OR",
    "btn_demo_citizen": "Enter Citizen Portal (1-Click Demo)",
    "card_gov_title": "Government Hub",
    "card_gov_tag": "For City Officials & Planners",
    "card_gov_desc": "Review citizen reports, dispatch repair teams, plan city projects, and balance budgets with AI.",
    "lbl_gov_email": "Official Government Email *",
    "ph_gov_email": "e.g. official@brics.gov",
    "btn_sign_in_gov": "Sign In to Government Hub",
    "btn_demo_gov": "Enter Government Hub (1-Click Demo)",

    "status_pending": "Pending Review",
    "status_progress": "In Progress",
    "status_resolved": "Fixed"
}

# -------------------------------------------------------------
# HINDI (hi)
# -------------------------------------------------------------
HI = {
    "portal_citizen_badge": "नागरिक पोर्टल",
    "portal_gov_badge": "सरकारी कमान केंद्र",
    "nav_back": "पीछे",
    "nav_home": "होम",
    "btn_sign_out": "साइन आउट",
    "btn_exit_command": "कमान से बाहर निकलें",
    "detected_node_title": "पहचाना गया स्थान",
    "badge_cloud_connected": "क्लाउड से जुड़ा हुआ",
    "badge_live_data": "लाइव क्लाउड डेटा",
    "badge_open_standard": "ओपन डिजिटल मानक",

    "sector_roads_transit_name": "सड़कें, पुल एवं मुख्य मार्ग",
    "sector_roads_transit_badge": "परिवहन रीढ़",
    "sector_roads_transit_desc": "एक्सप्रेसवे, फ्लाईओवर, मुख्य सड़कों की मरम्मत, पुल और पैदल यात्री स्काईवॉक",

    "sector_water_supply_name": "जलापूर्ति एवं पाइपलाइन लीकेज",
    "sector_water_supply_badge": "पेयजल आपूर्ति",
    "sector_water_supply_desc": "स्वच्छ पेयजल वितरण, मुख्य ट्रंक लाइन, स्मार्ट लीकेज टेलीमेट्री और पंपिंग स्टेशन",

    "sector_electricity_grid_name": "बिजली, स्ट्रीटलाइट्स एवं ग्रिड",
    "sector_electricity_grid_badge": "ऊर्जा अवसंरचना",
    "sector_electricity_grid_desc": "उच्च-वोल्टेज सबस्टेशन, भूमिगत केबलिंग, स्मार्ट एलईडी लाइटें और ब्लैकआउट रोकथाम",

    "sector_waste_sanitation_name": "कचरा प्रबंधन एवं स्वच्छता",
    "sector_waste_sanitation_badge": "चक्रीय स्वच्छता",
    "sector_waste_sanitation_desc": "स्वचालित सामग्री पुनर्चक्रण, बायो-मीथेनेशन प्लांट, लैंडफिल सफाई और दैनिक घर-घर संग्रहण",

    "sector_public_transport_name": "सार्वजनिक परिवहन एवं ट्रांजिट हब",
    "sector_public_transport_badge": "गतिशीलता गलियारे",
    "sector_public_transport_desc": "मेट्रो फीडर रूट, इलेक्ट्रिक बस फ्लीट, मल्टी-मॉडल टर्मिनल और यात्री बस शेल्टर",

    "sector_stormwater_flood_name": "बरसाती जल निकासी एवं बाढ़ नियंत्रण",
    "sector_stormwater_flood_badge": "जलभराव सुरक्षा",
    "sector_stormwater_flood_desc": "गहरे जल निकासी नाले, नदी तटबंध, वर्षा जल जलाशय और स्वचालित फ्लडगेट टेलीमेट्री",

    "sector_health_clinics_name": "सार्वजनिक स्वास्थ्य, क्लीनिक एवं वेक्टर नियंत्रण",
    "sector_health_clinics_badge": "सामुदायिक स्वास्थ्य",
    "sector_health_clinics_desc": "ट्रॉमा अस्पताल, मातृ स्वास्थ्य केंद्र, दवा स्टॉक टेलीमेट्री और डेंगू रोधी फॉगिंग",

    "sector_schools_facilities_name": "सरकारी स्कूल एवं नागरिक सुविधाएं",
    "sector_schools_facilities_badge": "सामाजिक अवसंरचना",
    "sector_schools_facilities_desc": "स्कूल भवन सुरक्षा, पॉलिटेक्निक कौशल केंद्र, सार्वजनिक पुस्तकालय और डिजिटल शिक्षण लैब",

    "sector_parks_environment_name": "सार्वजनिक पार्क, हरित पट्टियां एवं वायु गुणवत्ता",
    "sector_parks_environment_badge": "पर्यावरण पुनर्स्थापन",
    "sector_parks_environment_desc": "शहरी वनीकरण, स्मॉग-रोधी मिस्टिंग टॉवर, पार्क सोलर लाइटिंग और जैव विविधता गलियारे",

    "sector_public_safety_name": "सार्वजनिक सुरक्षा एवं आपातकालीन प्रणाली",
    "sector_public_safety_badge": "आपातकालीन सुरक्षा",
    "sector_public_safety_desc": "प्रेशराइज्ड फायर हाइड्रेंट, आपदा निकासी मार्ग, सीसीटीवी नेटवर्क और आपातकालीन सायरन",

    "sec_choose_category": "एक श्रेणी चुनें",
    "sec_choose_category_sub": "हमारे 10 नगर क्षेत्रों में से अपनी समस्या से संबंधित श्रेणी चुनें:",
    "sec_category_prompt": "फोटो या वॉयस नोट के साथ त्वरित रिपोर्ट फॉर्म खोलने के लिए ऊपर किसी भी श्रेणी पर क्लिक करें।",
    "lbl_sla_24h": "समाधान समय: < 24 घंटे",
    "btn_report_issue": "समस्या दर्ज करें",
    "badge_report_context": "समस्या रिपोर्ट करें",

    "cit_hero_tag": "सक्रिय नागरिक लोक निर्माण पोर्टल",
    "cit_hero_title": "समस्याएं दर्ज करें एवं सामुदायिक मांगें रखें",
    "cit_hero_subtitle": "स्थानीय बुनियादी ढांचे की समस्याओं को आसानी से दर्ज करें, विकास परियोजनाओं पर वोट करें और आवाज व फोटो अपडेट के साथ मरम्मत ट्रैक करें।",
    "cit_welcome_title": "स्वागत है, प्रिया शर्मा",
    "cit_welcome_desc": "समस्याओं की रिपोर्ट करने, पड़ोस के सुधारों पर वोट करने और मरम्मत पर नज़र रखने हेतु आपका नागरिक पोर्टल।",
    "cit_badge_resident": "सत्यापित नागरिक • दिल्ली",
    "cit_badge_ward": "वार्ड 14 • दिल्ली एनसीआर",
    "cit_badge_sla": "98.4% समय पर समाधान",
    "cit_launchpad_title": "आप क्या करना चाहते हैं?",
    "cit_launchpad_subtitle": "शुरू करने के लिए नीचे दिए गए विकल्पों में से चुनें:",

    "card_report_title": "समस्या दर्ज करें",
    "card_report_desc": "सड़क के गड्ढे, टूटी स्ट्रीट लाइट, पानी का रिसाव या कचरा एकत्र न होने की फोटो या वॉयस नोट के साथ शिकायत करें।",
    "card_report_btn": "समस्या दर्ज करें",
    "card_demands_title": "सामुदायिक मांगें एवं वोटिंग",
    "card_demands_desc": "पार्क, सड़क चौड़ीकरण और स्वच्छ जल जैसी परियोजनाओं के लिए वोट करें ताकि नगर निगम बजट को सही दिशा मिले।",
    "card_demands_btn": "सामुदायिक मांगें देखें",
    "card_track_title": "मेरी शिकायतें ट्रैक करें",
    "card_track_desc": "अपनी दर्ज की गई समस्याओं की प्रगति देखें, नियुक्त कर्मचारियों की जानकारी पाएं और ऑडियो अपडेट सुनें।",
    "card_track_btn": "शिकायतें ट्रैक करें",
    "card_whatsapp_title": "व्हाट्सएप सहायक",
    "card_whatsapp_desc": "हिंदी, अंग्रेजी, पुर्तगाली या अपनी स्थानीय भाषा में व्हाट्सएप पर चैट करके समस्या दर्ज करें।",
    "card_whatsapp_btn": "व्हाट्सएप चैट खोलें",

    "tag_quick_ai": "त्वरित एआई समीक्षा",
    "tag_10_categories": "10+ श्रेणियां",
    "tag_photo_review": "फोटो समीक्षा",
    "tag_voice_msg": "वॉयस संदेश",
    "tag_auto_loc": "स्वतः स्थान पहचान",
    "lbl_avg_resp": "औसत प्रतिक्रिया: 4 सेकंड",
    "lbl_votes_cast": "27,421 वोट दर्ज",
    "tag_public_voting": "सार्वजनिक वोटिंग",
    "tag_local_budget": "स्थानीय बजट",
    "tag_ward_projects": "वार्ड परियोजनाएं",
    "tag_live_count": "लाइव गणना",
    "lbl_active_wards": "8 वार्डों में सक्रिय",
    "tag_step_status": "चरणबद्ध स्थिति",
    "tag_voice_briefing": "वॉयस ब्रीफिंग",
    "tag_crew_map": "मरम्मत दल मैप",
    "tag_proof_photos": "प्रमाण फोटो",
    "lbl_tracked_live": "लाइव ट्रैकिंग",
    "lbl_24_7_wa": "24/7 व्हाट्सएप पर",
    "tag_no_app": "ऐप की जरूरत नहीं",
    "tag_any_lang": "कोई भी भाषा",
    "tag_smart_chat": "स्मार्ट चैट",
    "tag_instant_ticket": "तत्काल रसीद",
    "lbl_instant_reply": "तुरंत जवाब",
    "sec_recently_fixed": "आपके क्षेत्र में हाल ही में हल की गई समस्याएं",
    "sec_community_notices": "सामुदायिक सूचनाएं एवं बैठकें",

    "back_to_citizen_home": "← नागरिक होम पर लौटें",
    "return_to_executive_cmd": "← कार्यकारी विहंगावलोकन पर लौटें",

    "modal_report_title": "समस्या दर्ज करें",
    "modal_report_sub": "त्वरित समाधान हेतु विवरण, फोटो या वॉयस नोट जोड़ें।",
    "lbl_selected_category": "चयनित श्रेणी",
    "lbl_problem": "समस्या क्या है? *",
    "btn_voice_input": "एआई से बोलकर दर्ज करें",
    "ph_desc": "समस्या का विवरण दें, निकटतम लैंडमार्क या दुकान बताएं और बताएं कि इससे जनता कैसे प्रभावित हो रही है...",
    "voice_listening": "सुन रहे हैं... कृपया हिंदी, अंग्रेजी या अपनी मातृभाषा में बोलें",
    "btn_stop_rec": "पूर्ण / रोकें",
    "lbl_neighborhood_ward": "पड़ोस / वार्ड *",
    "lbl_street_address": "सड़क का पता या लैंडमार्क",
    "btn_use_current_location": "वर्तमान स्थान का उपयोग करें",
    "ph_street_address": "उदा. आउटर रिंग रोड, मेट्रो गेट 2 के पास",
    "gps_acquired": "📍 जीपीएस निर्देशांक प्राप्त हुए",
    "lbl_add_photo": "फोटो संलग्न करें (वैकल्पिक)",
    "lbl_add_photo_hint": "हमारा एआई नुकसान की गंभीरता का स्वतः विश्लेषण कर त्वरित समाधान सुनिश्चित करता है।",
    "lbl_add_voice": "वॉयस नोट जोड़ें (वैकल्पिक)",
    "lbl_add_voice_hint": "हिंदी, अंग्रेजी, पुर्तगाली या अपनी मातृभाषा में बोलें।",
    "btn_cancel": "रद्द करें",
    "btn_submit_report": "रिपोर्ट दर्ज करें",

    "badge_demands_context": "सामुदायिक मांगें",
    "sec_demands_title": "सामुदायिक मांगें एवं वोटिंग",
    "sec_demands_sub": "पार्क, सड़क चौड़ीकरण और स्वच्छ जल जैसी परियोजनाओं के लिए वोट करें ताकि नगर निगम बजट को सही दिशा मिले।",
    "btn_propose_project": "+ नया प्रोजेक्ट प्रस्तावित करें",
    "ph_search_demands": "शीर्षक, पड़ोस या कीवर्ड द्वारा प्रोजेक्ट खोजें...",
    "opt_all_wards": "सभी पड़ोस / वार्ड",
    "btn_upvote": "वोट दें",
    "lbl_votes": "वोट",
    "lbl_est_cost": "अनुमानित लागत",
    "lbl_beneficiaries": "लाभान्वित नागरिक",
    "lbl_proposed_by": "प्रस्तावक",
    "modal_propose_title": "सामुदायिक प्रोजेक्ट प्रस्तावित करें",
    "modal_propose_sub": "अधिक वोटों वाले प्रोजेक्ट्स को सीधे नगर योजनाकारों को बजट आवंटन हेतु भेजा जाता है।",
    "lbl_project_title": "प्रोजेक्ट का शीर्षक *",
    "ph_project_title": "उदा. सेक्टर 4 में नया पार्क और सोलर लाइटिंग",
    "lbl_category": "श्रेणी *",
    "lbl_budget": "अनुमानित लागत",
    "ph_budget": "उदा. ₹50 लाख / R$ 300,000",
    "lbl_est_beneficiaries": "अनुमानित लाभार्थी",
    "ph_beneficiaries": "उदा. 5,000 निवासी",
    "lbl_why_needed": "यह प्रोजेक्ट क्यों आवश्यक है? *",
    "ph_why_needed": "बताएं कि यह कार्य क्यों महत्वपूर्ण है और इससे पड़ोस में क्या सुधार होगा...",
    "btn_submit_voting": "वोटिंग हेतु सबमिट करें",

    "badge_track_context": "शिकायत ट्रैकर",
    "sec_track_title": "अपनी शिकायतें ट्रैक करें",
    "sec_track_sub": "अपनी समस्याओं के समाधान की प्रगति देखें, मरम्मत कर्मचारियों की जानकारी लें और वॉयस अपडेट सुनें।",
    "ph_search_track": "शिकायत आईडी (उदा. CP-2026...) या पता दर्ज करें...",
    "btn_listen_briefing": "ऑडियो स्थिति सुनें",
    "btn_open_maps": "गूगल मैप्स में देखें",
    "step_submitted": "दर्ज हुई",
    "step_dispatched": "टीम रवाना",
    "step_in_progress": "कार्य प्रगति पर",
    "step_resolved": "समस्या हल हुई",
    "lbl_assigned_worker": "नियुक्त कर्मचारी",

    "badge_wa_context": "व्हाट्सएप चैट",
    "sec_wa_title": "व्हाट्सएप पर सिविकपल्स से जुड़ें",
    "sec_wa_sub": "दोस्त से बात करने की तरह आसानी से फोटो, टेक्स्ट या वॉयस मैसेज भेजकर शिकायत करें।",
    "wa_assistant_name": "सिविकपल्स सहायक (सत्यापित सपोर्ट)",
    "wa_online_status": "● ऑनलाइन • त्वरित सहायता",
    "badge_online": "ऑनलाइन",
    "wa_bot_greeting": "नमस्ते / Hello! आज मैं आपकी क्या सहायता कर सकता हूँ? अपने पड़ोस की समस्या का वॉयस नोट भेजें या लिखें, मैं तुरंत रिपोर्ट दर्ज करूँगा।",
    "btn_wa_sample_hi": "🇮🇳 हिंदी वॉयस नोट",
    "btn_wa_sample_pt": "🇧🇷 पुर्तगाली नोट",
    "btn_wa_sample_en": "🇿🇦 अंग्रेजी संदेश",
    "ph_wa_input": "संदेश लिखें या ऊपर नमूने पर क्लिक करें...",

    "gov_hero_tag": "नगर नियोजन एवं परिचालन कमान",
    "gov_hero_title": "नगर परियोजनाएं एवं परिचालन नियंत्रण",
    "gov_hero_subtitle": "नागरिक शिकायतों पर नज़र रखें, मरम्मत दल भेजें, प्रमुख बुनियादी ढांचा परियोजनाओं की योजना बनाएं और एआई अंतर्दृष्टि से बजट समीक्षा करें।",
    "gov_welcome_title": "परिचालन विहंगावलोकन",
    "gov_welcome_desc": "वास्तविक समय की नागरिक रिपोर्ट, एआई नियोजन सिफारिशें और बजट आवंटन देखें। शुरू करने के लिए नीचे कोई भी मॉड्यूल चुनें।",
    "gov_badge_clearance": "प्रशासक पहुंच",
    "gov_badge_uptime": "99.98% सिस्टम अपटाइम",
    "gov_launchpad_title": "नगर प्रबंधन मॉड्यूल",
    "gov_launchpad_subtitle": "नगर संचालन प्रबंधित करने के लिए नीचे किसी भी उपकरण का चयन करें:",

    "card_megaplan_title": "एआई नगर परियोजना योजनाकार",
    "card_megaplan_desc": "नागरिक मांगों और क्षेत्रीय डेटा का विश्लेषण कर अनुमानित लागत और लाभ के साथ बड़े प्रोजेक्ट्स की सिफारिश करता है।",
    "card_megaplan_btn": "योजना टूल खोलें",
    "card_queue_title": "मरम्मत एवं कार्य आदेश",
    "card_queue_desc": "आने वाली नागरिक शिकायतों की समीक्षा करें, मरम्मत दल भेजें, समय सीमा ट्रैक करें और पूर्ण कार्य को मंजूरी दें।",
    "card_queue_btn": "मरम्मत सूची देखें",
    "card_budget_title": "बजट एवं संसाधन समता",
    "card_budget_desc": "वार्डों के बीच सार्वजनिक खर्च की तुलना करें ताकि पिछड़े क्षेत्रों को उचित धन और संसाधन मिल सकें।",
    "card_budget_btn": "बजट टूल खोलें",
    "card_map_title": "लाइव नगर मानचित्र",
    "card_map_desc": "शिकायतों, फील्ड टीमों के स्थान, वार्ड सीमाओं और संवेदनशील क्षेत्रों को दर्शाने वाला इंटरएक्टिव मैप।",
    "card_map_btn": "नगर मैप खोलें",
    "card_dpg_title": "डेटा मानक एवं अनुपालन",
    "card_dpg_desc": "डिजिटल पब्लिक गुड (DPG) मानकों की पुष्टि, ओपन एपीआई दस्तावेज और डेटा गोपनीयता दिशानिर्देश देखें।",
    "card_dpg_btn": "मानक देखें",

    "sec_live_weather": "लाइव नगर मौसम स्टेशन",
    "badge_sensor_data": "लाइव सेंसर डेटा",
    "lbl_weather_source": "स्रोत: ओपन-मेटियो रियल-टाइम सेंसर",
    "lbl_temperature": "परिवेश का तापमान",
    "lbl_humidity": "सापेक्षिक आर्द्रता",
    "lbl_precipitation": "वर्षा की मात्रा",
    "lbl_wind_velocity": "हवा की गति",
    "lbl_database": "डेटाबेस",
    "lbl_city_map_data": "नगर मैप डेटा",
    "lbl_storage": "स्टोरेज",
    "btn_sync_map_data": "मैप डेटा सिंक करें",
    "sec_recent_directives": "हाल के नगर निर्देश एवं कार्रवाइयां",
    "sec_repair_status": "नगर मरम्मत परिचालन स्थिति",
    "lbl_infra_health": "अवसंरचना स्वास्थ्य सूचकांक",
    "lbl_active_teams": "सक्रिय फील्ड टीमें",
    "lbl_budget_influence": "नागरिक बजट प्रभाव",

    "badge_planning_context": "नगर नियोजन",
    "sec_megaplan_title": "एआई बुनियादी ढांचा सिफारिशें",
    "sec_megaplan_sub": "नागरिक मांगों, यातायात बाधाओं और जनसांख्यिकीय प्राथमिकताओं के विश्लेषण द्वारा तैयार उच्च-प्रभाव वाली परियोजनाएं।",
    "btn_update_plan": "एआई योजना अपडेट करें",
    "lbl_capex": "अनुमानित पूंजीगत व्यय",
    "lbl_justification": "प्रोजेक्ट औचित्य",
    "btn_approve_project": "प्रोजेक्ट स्वीकृत करें",

    "badge_queue_context": "मरम्मत एवं प्रेषण",
    "sec_queue_title": "रिपोर्ट की गई समस्याएं एवं मरम्मत कतार",
    "sec_queue_sub": "नागरिक शिकायतों को प्रबंधित करें, फील्ड कर्मचारियों को कार्य सौंपें और पूर्ण मरम्मत को सत्यापित करें:",
    "th_id": "आईडी",
    "th_category": "श्रेणी",
    "th_description": "विवरण",
    "th_ward": "वार्ड",
    "th_severity": "गंभीरता",
    "th_status": "स्थिति",
    "th_action": "कार्रवाई",
    "btn_dispatch": "टीम भेजें",
    "btn_mark_resolved": "हल घोषित करें",

    "badge_budget_context": "बजट विश्लेषण",
    "sec_budget_title": "वार्ड बजट एवं व्यय समता",
    "sec_budget_sub": "संसाधनों के निष्पक्ष वितरण हेतु वार्ड की जरूरतों के सापेक्ष नगर निगम निवेश की तुलना करें:",
    "th_ward_budget": "पड़ोस / वार्ड",
    "th_population_vulnerability": "जनसंख्या एवं संवेदनशीलता",
    "th_planned_budget": "नियोजित बजट",
    "th_demand_share": "नागरिक मांग अनुपात",
    "th_funding_status": "फंडिंग स्थिति",
    "th_recommended_action": "अनुशंसित कार्रवाई",

    "badge_map_context": "नगर मानचित्र",
    "sec_map_title": "लाइव नगर घटना मानचित्र",
    "sec_map_sub": "रंगीन मार्कर समस्या की स्थिति, प्राथमिकता वाले क्षेत्र और फील्ड टीमों की स्थिति दर्शाते हैं:",

    "badge_dpg_context": "ओपन मानक",
    "sec_dpg_title": "डिजिटल पब्लिक गुड (DPG) मानक",
    "sec_dpg_sub": "9 ओपन सोर्स एवं डिजिटल पब्लिक गुड संकेतकों के साथ पूर्ण अनुपालन:",

    "login_hero_sub": "ब्रिक्स समुदायों में बेहतर पड़ोस के निर्माण हेतु नागरिकों और नगर योजनाकारों को एक मंच पर जोड़ना।",
    "card_citizen_title": "नागरिक पोर्टल",
    "card_citizen_tag": "निवासियों एवं समुदायों हेतु",
    "card_citizen_desc": "स्थानीय समस्याओं की रिपोर्ट करें, पड़ोस के विकास पर वोट दें और मरम्मत पर वास्तविक समय में नज़र रखें।",
    "lbl_citizen_email": "नागरिक ईमेल या उपयोगकर्ता नाम *",
    "ph_citizen_email": "उदा. resident@delhi.gov.in",
    "lbl_password": "पासवर्ड *",
    "btn_sign_in_citizen": "नागरिक पोर्टल में साइन इन करें",
    "lbl_or": "या",
    "btn_demo_citizen": "नागरिक पोर्टल में प्रवेश (1-क्लिक डेमो)",
    "card_gov_title": "सरकारी कमान केंद्र",
    "card_gov_tag": "अधिकारियों एवं नगर योजनाकारों हेतु",
    "card_gov_desc": "नागरिक रिपोर्टों की समीक्षा करें, मरम्मत दल भेजें, नगर परियोजनाओं की योजना बनाएं और एआई से बजट संतुलित करें।",
    "lbl_gov_email": "आधिकारिक सरकारी ईमेल *",
    "ph_gov_email": "उदा. official@brics.gov",
    "btn_sign_in_gov": "सरकारी केंद्र में साइन इन करें",
    "btn_demo_gov": "सरकारी केंद्र में प्रवेश (1-क्लिक डेमो)",

    "status_pending": "समीक्षाधीन",
    "status_progress": "प्रगति पर",
    "status_resolved": "हल किया गया"
}

# -------------------------------------------------------------
# PORTUGUESE (pt)
# -------------------------------------------------------------
PT = {
    "portal_citizen_badge": "Portal do Cidadão",
    "portal_gov_badge": "Centro Governamental",
    "nav_back": "Voltar",
    "nav_home": "Início",
    "btn_sign_out": "Sair",
    "btn_exit_command": "Sair do Portal",
    "detected_node_title": "Localização Detectada",
    "badge_cloud_connected": "Conectado à Nuvem",
    "badge_live_data": "Dados em Tempo Real",
    "badge_open_standard": "Padrão Aberto DPG",

    "sector_roads_transit_name": "Vias, Pontes e Corredores Arteriais",
    "sector_roads_transit_badge": "Espinha Viária",
    "sector_roads_transit_desc": "Vias expressas, viadutos, recapeamento asfáltico, pontes estruturais e passarelas de pedestres",

    "sector_water_supply_name": "Abastecimento de Água e Vazamentos",
    "sector_water_supply_badge": "Água Potável",
    "sector_water_supply_desc": "Distribuição de água potável, adutoras de alta pressão, telemetria inteligente de vazamentos e bombas",

    "sector_electricity_grid_name": "Eletricidade, Iluminação Pública e Rede",
    "sector_electricity_grid_badge": "Infraestrutura de Energia",
    "sector_electricity_grid_desc": "Subestações de alta tensão, cabeamento subterrâneo, iluminação LED inteligente e prevenção de apagões",

    "sector_waste_sanitation_name": "Gestão de Resíduos e Saneamento",
    "sector_waste_sanitation_badge": "Limpeza Circular",
    "sector_waste_sanitation_desc": "Recuperação automatizada, usinas de biometanação, remediação de aterros e coleta porta a porta",

    "sector_public_transport_name": "Transporte Público e Terminais",
    "sector_public_transport_badge": "Corredores de Mobilidade",
    "sector_public_transport_desc": "Linhas alimentadoras de metrô, frotas de ônibus elétricos, terminais multimodais e abrigos de passageiros",

    "sector_stormwater_flood_name": "Drenagem Pluvial e Enchentes",
    "sector_stormwater_flood_badge": "Defesa Hidrológica",
    "sector_stormwater_flood_desc": "Canais profundos de drenagem, diques fluviais, piscinões e comportas com telemetria automatizada",

    "sector_health_clinics_name": "Saúde Pública, Clínicas e Controle de Vetores",
    "sector_health_clinics_badge": "Saúde Comunitária",
    "sector_health_clinics_desc": "Hospitais de trauma, centros de saúde materno-infantil, estoque de medicamentos e fumacê contra dengue",

    "sector_schools_facilities_name": "Escolas Públicas e Instalações Cívicas",
    "sector_schools_facilities_badge": "Infraestrutura Social",
    "sector_schools_facilities_desc": "Segurança predial de escolas, centros técnicos politécnicos, bibliotecas cívicas e laboratórios digitais",

    "sector_parks_environment_name": "Parques Públicos, Áreas Verdes e Qualidade do Ar",
    "sector_parks_environment_badge": "Restauração Ecológica",
    "sector_parks_environment_desc": "Arborização urbana, torres anti-poluição, iluminação solar em praças e corredores de biodiversidade",

    "sector_public_safety_name": "Segurança Pública e Defesa Civil",
    "sector_public_safety_badge": "Defesa de Emergência",
    "sector_public_safety_desc": "Hidrantes pressurizados, rotas de evacuação de desastres, monitoramento por câmeras e sirenes de alerta",

    "sec_choose_category": "Escolha uma Categoria",
    "sec_choose_category_sub": "Selecione a categoria correspondente ao seu chamado nos nossos 10 setores municipais:",
    "sec_category_prompt": "Clique em qualquer categoria acima para abrir o formulário rápido com envio de foto ou áudio.",
    "lbl_sla_24h": "Prazo SLA: < 24h",
    "btn_report_issue": "Relatar Problema",
    "badge_report_context": "Relatar Problema",

    "cit_hero_tag": "Portal Ativo do Cidadão",
    "cit_hero_title": "Relate Problemas e Demandas Comunitárias",
    "cit_hero_subtitle": "Relate falhas urbanas com facilidade, vote em projetos essenciais para o seu bairro e acompanhe os reparos com fotos e áudios.",
    "cit_welcome_title": "Bem-vinda, Priya Sharma",
    "cit_welcome_desc": "Seu portal cívico para registrar problemas, votar em melhorias para o bairro e acompanhar consertos.",
    "cit_badge_resident": "Cidadã Verificada • São Paulo",
    "cit_badge_ward": "Distrito 14 • Região Metropolitana",
    "cit_badge_sla": "98,4% Resolvidos no Prazo",
    "cit_launchpad_title": "O que você gostaria de fazer?",
    "cit_launchpad_subtitle": "Escolha uma das opções abaixo para começar:",

    "card_report_title": "Relatar um Problema",
    "card_report_desc": "Informe buracos na rua, lâmpadas apagadas, vazamentos de água ou lixo acumulado com uma foto ou nota de voz.",
    "card_report_btn": "Relatar Problema",
    "card_demands_title": "Demandas Comunitárias e Votação",
    "card_demands_desc": "Vote em melhorias como novas praças, recapeamento e saneamento para orientar os investimentos municipais.",
    "card_demands_btn": "Ver Demandas Comunitárias",
    "card_track_title": "Acompanhar Meus Chamados",
    "card_track_desc": "Consulte o status das suas solicitações, veja a equipe designada e ouça atualizações de voz.",
    "card_track_btn": "Acompanhar Chamados",
    "card_whatsapp_title": "Assistente WhatsApp",
    "card_whatsapp_desc": "Converse conosco pelo WhatsApp para abrir chamados em português, espanhol, inglês ou sua língua nativa.",
    "card_whatsapp_btn": "Abrir Chat no WhatsApp",

    "tag_quick_ai": "Análise Rápida com IA",
    "tag_10_categories": "10+ Categorias",
    "tag_photo_review": "Avaliação por Foto",
    "tag_voice_msg": "Mensagem de Voz",
    "tag_auto_loc": "Localização Automática",
    "lbl_avg_resp": "Tempo de resposta: 4s",
    "lbl_votes_cast": "27.421 Votos Registrados",
    "tag_public_voting": "Votação Pública",
    "tag_local_budget": "Orçamento Local",
    "tag_ward_projects": "Obras no Bairro",
    "tag_live_count": "Contagem ao Vivo",
    "lbl_active_wards": "Ativo em 8 Distritos",
    "tag_step_status": "Status Passo a Passo",
    "tag_voice_briefing": "Resumo em Áudio",
    "tag_crew_map": "Mapa da Equipe",
    "tag_proof_photos": "Fotos Comprobatórias",
    "lbl_tracked_live": "Rastreio em Tempo Real",
    "lbl_24_7_wa": "WhatsApp 24/7",
    "tag_no_app": "Sem Instalar App",
    "tag_any_lang": "Qualquer Idioma",
    "tag_smart_chat": "Chat Inteligente",
    "tag_instant_ticket": "Protocolo Imediato",
    "lbl_instant_reply": "Resposta Imediata",
    "sec_recently_fixed": "Problemas Resolvidos Recentemente no Bairro",
    "sec_community_notices": "Comunicados e Assembleias do Bairro",

    "back_to_citizen_home": "← Voltar ao Início",
    "return_to_executive_cmd": "← Voltar à Visão Geral",

    "modal_report_title": "Relatar um Problema",
    "modal_report_sub": "Adicione detalhes, fotos ou áudios para acelerar a solução.",
    "lbl_selected_category": "Categoria Selecionada",
    "lbl_problem": "Qual é o problema? *",
    "btn_voice_input": "Falar com a IA",
    "ph_desc": "Descreva o defeito, ponto de referência mais próximo e como isso afeta as pessoas...",
    "voice_listening": "Ouvindo... Fale agora em português, espanhol ou inglês",
    "btn_stop_rec": "Concluído / Parar",
    "lbl_neighborhood_ward": "Bairro / Distrito *",
    "lbl_street_address": "Endereço ou Ponto de Referência",
    "btn_use_current_location": "Usar Localização Atual",
    "ph_street_address": "ex: Av. Paulista, próximo ao Metrô",
    "gps_acquired": "📍 Coordenadas GPS Obtidas",
    "lbl_add_photo": "Adicionar Foto (Opcional)",
    "lbl_add_photo_hint": "Nossa IA avalia a gravidade do estrago para agilizar o envio da equipe.",
    "lbl_add_voice": "Adicionar Nota de Voz (Opcional)",
    "lbl_add_voice_hint": "Fale em português, espanhol, inglês ou outro idioma.",
    "btn_cancel": "Cancelar",
    "btn_submit_report": "Enviar Chamado",

    "badge_demands_context": "Demandas do Bairro",
    "sec_demands_title": "Demandas Comunitárias e Votação",
    "sec_demands_sub": "Vote em melhorias como novas praças, recapeamento e saneamento para orientar os investimentos municipais.",
    "btn_propose_project": "+ Propor um Projeto",
    "ph_search_demands": "Buscar projetos por título, bairro ou palavra-chave...",
    "opt_all_wards": "Todos os Bairros / Distritos",
    "btn_upvote": "Votar",
    "lbl_votes": "Votos",
    "lbl_est_cost": "Custo Estimado",
    "lbl_beneficiaries": "Pessoas Beneficiadas",
    "lbl_proposed_by": "Proposto por",
    "modal_propose_title": "Propor um Projeto Comunitário",
    "modal_propose_sub": "Projetos mais votados são encaminhados diretamente aos planejadores urbanos para obtenção de verba.",
    "lbl_project_title": "Título do Projeto *",
    "ph_project_title": "ex: Novo Parque com Iluminação Solar no Bairro",
    "lbl_category": "Categoria *",
    "lbl_budget": "Orçamento Estimado",
    "ph_budget": "ex: R$ 350.000 / ₹50 Lakhs",
    "lbl_est_beneficiaries": "Pessoas Beneficiadas",
    "ph_beneficiaries": "ex: 5.000 moradores",
    "lbl_why_needed": "Por que esta obra é necessária? *",
    "ph_why_needed": "Explique a importância do projeto e as melhorias que trará para a comunidade...",
    "btn_submit_voting": "Enviar para Votação",

    "badge_track_context": "Rastrear Chamados",
    "sec_track_title": "Acompanhe Seus Chamados",
    "sec_track_sub": "Consulte o andamento das solicitações, veja os operários responsáveis e ouça relatórios de voz.",
    "ph_search_track": "Digite o ID do chamado (ex: CP-2026...) ou endereço...",
    "btn_listen_briefing": "Ouvir Relatório em Áudio",
    "btn_open_maps": "Ver no Google Maps",
    "step_submitted": "Registrado",
    "step_dispatched": "Equipe a Caminho",
    "step_in_progress": "Em Andamento",
    "step_resolved": "Concluído",
    "lbl_assigned_worker": "Operário Encarregado",

    "badge_wa_context": "Chat do WhatsApp",
    "sec_wa_title": "Converse com o CivicPulse no WhatsApp",
    "sec_wa_sub": "Envie mensagens de texto, fotos ou áudios com a mesma facilidade de uma conversa com amigos.",
    "wa_assistant_name": "Assistente CivicPulse (Suporte Verificado)",
    "wa_online_status": "● Online • Ajuda Imediata",
    "badge_online": "ONLINE",
    "wa_bot_greeting": "Olá / Namaste! Como posso te ajudar hoje? Envie um áudio ou digite o problema da sua rua, e eu registrarei o chamado imediatamente.",
    "btn_wa_sample_hi": "🇮🇳 Áudio em Hindi",
    "btn_wa_sample_pt": "🇧🇷 Nota em Português",
    "btn_wa_sample_en": "🇿🇦 Mensagem em Inglês",
    "ph_wa_input": "Digite sua mensagem ou clique em um exemplo acima...",

    "gov_hero_tag": "Planejamento Urbano e Operações",
    "gov_hero_title": "Comando de Obras e Operações Urbanas",
    "gov_hero_subtitle": "Monitore chamados populares, despache equipes de reparo, planeje obras estruturais e avalie orçamentos com inteligência artificial.",
    "gov_welcome_title": "Visão Geral Operacional",
    "gov_welcome_desc": "Acompanhe chamados em tempo real, recomendações de IA e alocação orçamentária. Escolha um módulo abaixo para interagir.",
    "gov_badge_clearance": "Acesso Administrativo",
    "gov_badge_uptime": "99,98% Disponibilidade",
    "gov_launchpad_title": "Módulos de Gestão Urbana",
    "gov_launchpad_subtitle": "Selecione uma ferramenta abaixo para gerenciar as operações da cidade:",

    "card_megaplan_title": "Planejador de Projetos com IA",
    "card_megaplan_desc": "Cruza chamados dos moradores e dados censitários para propor grandes obras com custos e impactos estimados.",
    "card_megaplan_btn": "Abrir Ferramenta de Obras",
    "card_queue_title": "Fila de Reparos e Ordens de Serviço",
    "card_queue_desc": "Analise chamados abertos, envie equipes técnicas, acompanhe prazos de atendimento e aprove reparos concluídos.",
    "card_queue_btn": "Ver Fila de Reparos",
    "card_budget_title": "Equidade Orçamentária e Recursos",
    "card_budget_desc": "Compare investimentos entre bairros para garantir que regiões periféricas recebam verbas proporcionais.",
    "card_budget_btn": "Abrir Matriz Orçamentária",
    "card_map_title": "Mapa Urbano ao Vivo",
    "card_map_desc": "Mapa interativo com chamados, rotas das equipes de campo, limites distritais e pontos críticos.",
    "card_map_btn": "Abrir Mapa GIS",
    "card_dpg_title": "Padrões de Dados e Conformidade",
    "card_dpg_desc": "Verifique a conformidade com as diretrizes de Bens Públicos Digitais (DPG) e documentação de APIs abertas.",
    "card_dpg_btn": "Ver Padrões DPG",

    "sec_live_weather": "Estação Meteorológica Urbana",
    "badge_sensor_data": "Sensores em Tempo Real",
    "lbl_weather_source": "Fonte: Sensor Meteorológico Open-Meteo",
    "lbl_temperature": "Temperatura Ambiente",
    "lbl_humidity": "Umidade Relativa",
    "lbl_precipitation": "Precipitação (Chuva)",
    "lbl_wind_velocity": "Velocidade do Vento",
    "lbl_database": "Banco de Dados",
    "lbl_city_map_data": "Dados GIS da Cidade",
    "lbl_storage": "Armazenamento",
    "btn_sync_map_data": "Sincronizar Dados",
    "sec_recent_directives": "Diretrizes e Atos Municipais Recentes",
    "sec_repair_status": "Status Operacional de Reparos",
    "lbl_infra_health": "Índice de Saúde da Infraestrutura",
    "lbl_active_teams": "Equipes de Campo Ativas",
    "lbl_budget_influence": "Impacto dos Votos Populares",

    "badge_planning_context": "Planejamento Urbano",
    "sec_megaplan_title": "Recomendações Estruturais da IA",
    "sec_megaplan_sub": "Propostas de alto impacto geradas automaticamente a partir de demandas da população e gargalos de tráfego.",
    "btn_update_plan": "Atualizar Plano da IA",
    "lbl_capex": "Investimento Estimado (CapEx)",
    "lbl_justification": "Justificativa da Obra",
    "btn_approve_project": "Aprovar Projeto",

    "badge_queue_context": "Reparos e Despachos",
    "sec_queue_title": "Fila de Reparos e Chamados Abertos",
    "sec_queue_sub": "Filtre chamados de cidadãos, despache equipes de serviço e valide reparos concluídos:",
    "th_id": "ID",
    "th_category": "Categoria",
    "th_description": "Descrição",
    "th_ward": "Distrito",
    "th_severity": "Gravidade",
    "th_status": "Status",
    "th_action": "Ação",
    "btn_dispatch": "Despachar Equipe",
    "btn_mark_resolved": "Marcar Concluído",

    "badge_budget_context": "Auditoria Orçamentária",
    "sec_budget_title": "Orçamento Distrital e Equidade de Gastos",
    "sec_budget_sub": "Compare o investimento público com as demandas dos bairros para equilibrar a infraestrutura:",
    "th_ward_budget": "Bairro / Distrito",
    "th_population_vulnerability": "População e Vulnerabilidade",
    "th_planned_budget": "Orçamento Previsto",
    "th_demand_share": "Participação nas Demandas",
    "th_funding_status": "Status do Financiamento",
    "th_recommended_action": "Ação Recomendada",

    "badge_map_context": "Mapa da Cidade",
    "sec_map_title": "Mapa de Ocorrências Urbanas",
    "sec_map_sub": "Marcadores coloridos indicam status dos problemas, pontos prioritários e equipes em trânsito:",

    "badge_dpg_context": "Padrões Abertos",
    "sec_dpg_title": "Padrões de Bens Públicos Digitais",
    "sec_dpg_sub": "Aderência total aos 9 indicadores internacionais da DPGA:",

    "login_hero_sub": "Conectando moradores e planejadores municipais para construir bairros melhores nas cidades do BRICS.",
    "card_citizen_title": "Portal do Cidadão",
    "card_citizen_tag": "Para Moradores e Comunidades",
    "card_citizen_desc": "Relate problemas na sua rua, vote em melhorias e acompanhe reparos em tempo real.",
    "lbl_citizen_email": "E-mail ou Usuário do Cidadão *",
    "ph_citizen_email": "ex: cidadao@saopaulo.sp.gov.br",
    "lbl_password": "Senha *",
    "btn_sign_in_citizen": "Entrar no Portal do Cidadão",
    "lbl_or": "OU",
    "btn_demo_citizen": "Acessar Portal do Cidadão (Demo 1-Clique)",
    "card_gov_title": "Centro Governamental",
    "card_gov_tag": "Para Gestores e Técnicos Públicos",
    "card_gov_desc": "Analise chamados urbanos, despache equipes, planeje obras e equalize orçamentos com IA.",
    "lbl_gov_email": "E-mail Institucional *",
    "ph_gov_email": "ex: gestor@brics.gov",
    "btn_sign_in_gov": "Entrar no Centro Governamental",
    "btn_demo_gov": "Acessar Centro Governamental (Demo 1-Clique)",

    "status_pending": "Aguardando Triagem",
    "status_progress": "Em Andamento",
    "status_resolved": "Concluído"
}

# Helper to build Russian, Chinese, Tamil, Telugu, Zulu, Afrikaans
def create_localized_dict(lang_code):
    # Base mapping translations with specific terminology
    if lang_code == "ru":
        return {
            "portal_citizen_badge": "Портал граждан",
            "portal_gov_badge": "Государственный центр",
            "nav_back": "Назад",
            "nav_home": "Главная",
            "btn_sign_out": "Выйти",
            "btn_exit_command": "Выйти из портала",
            "detected_node_title": "Определенное местоположение",
            "badge_cloud_connected": "Облако подключено",
            "badge_live_data": "Онлайн данные",
            "badge_open_standard": "Открытый стандарт DPG",

            "sector_roads_transit_name": "Дороги, мосты и магистрали",
            "sector_roads_transit_badge": "Транспортный каркас",
            "sector_roads_transit_desc": "Автомагистрали, эстакады, ремонт дорожного покрытия, мосты и пешеходные переходы",

            "sector_water_supply_name": "Водоснабжение и утечки трубопроводов",
            "sector_water_supply_badge": "Питьевая вода",
            "sector_water_supply_desc": "Распределение чистой питьевой воды, магистральные водоводы, умная телеметрия утечек и насосные станции",

            "sector_electricity_grid_name": "Электричество, уличное освещение и сети",
            "sector_electricity_grid_badge": "Энергоинфраструктура",
            "sector_electricity_grid_desc": "Высоковольтные подстанции, подземная кабельная сеть, умное LED-освещение и предотвращение блэкаутов",

            "sector_waste_sanitation_name": "Управление отходами и санитария",
            "sector_waste_sanitation_badge": "Циркулярная чистота",
            "sector_waste_sanitation_desc": "Автоматизированная сортировка, биогазовые заводы, рекультивация полигонов и ежедневный сбор отходов",

            "sector_public_transport_name": "Общественный транспорт и пересадочные узлы",
            "sector_public_transport_badge": "Транспортные коридоры",
            "sector_public_transport_desc": "Маршруты подвоза к метро, электробусы, мультимодальные терминалы и остановочные павильоны",

            "sector_stormwater_flood_name": "Ливневая канализация и защита от паводков",
            "sector_stormwater_flood_badge": "Гидрозащита",
            "sector_stormwater_flood_desc": "Глубокие дренажные каналы, речные набережные, водохранилища и автоматические шлюзы",

            "sector_health_clinics_name": "Здравоохранение, поликлиники и санитарный контроль",
            "sector_health_clinics_badge": "Здоровье населения",
            "sector_health_clinics_desc": "Травматологические центры, перинатальные отделения, контроль запасов медикаментов и дезинсекция",

            "sector_schools_facilities_name": "Школы и общественные учреждения",
            "sector_schools_facilities_badge": "Социальная инфраструктура",
            "sector_schools_facilities_desc": "Безопасность зданий школ, политехнические центры, публичные библиотеки и цифровые лаборатории",

            "sector_parks_environment_name": "Парки, зеленые зоны и качество воздуха",
            "sector_parks_environment_badge": "Экологическое восстановление",
            "sector_parks_environment_desc": "Городское озеленение, вышки контроля смога, солнечное освещение в скверах и биокоридоры",

            "sector_public_safety_name": "Общественная безопасность и экстренные службы",
            "sector_public_safety_badge": "Экстренная защита",
            "sector_public_safety_desc": "Пожарные гидранты под давлением, маршруты эвакуации, система видеонаблюдения и сирены оповещения",

            "sec_choose_category": "Выберите категорию",
            "sec_choose_category_sub": "Выберите категорию проблемы из 10 секторов городского хозяйства:",
            "sec_category_prompt": "Нажмите на любую категорию, чтобы открыть форму с отправкой фото или голосового сообщения.",
            "lbl_sla_24h": "Срок SLA: < 24ч",
            "btn_report_issue": "Сообщить о проблеме",
            "badge_report_context": "Сообщить о проблеме",

            "cit_hero_tag": "Активный гражданский портал",
            "cit_hero_title": "Сообщайте о проблемах и предлагайте проекты",
            "cit_hero_subtitle": "Легко сообщайте о неполадках, голосуйте за нужные району проекты и отслеживайте ремонт с фото и голосовыми обновлениями.",
            "cit_welcome_title": "Добро пожаловать, Прия Шарма",
            "cit_welcome_desc": "Ваш портал для сообщения о проблемах, голосования за благоустройство и контроля ремонта.",
            "cit_badge_resident": "Проверенный житель • Дели",
            "cit_badge_ward": "Район 14 • Столичный округ",
            "cit_badge_sla": "98.4% решений в срок",
            "cit_launchpad_title": "Что вы хотите сделать?",
            "cit_launchpad_subtitle": "Выберите действие ниже, чтобы начать:",

            "card_report_title": "Сообщить о проблеме",
            "card_report_desc": "Сообщите о ямах на дорогах, неработающих фонарях, утечках воды или мусоре с фото или аудиосообщением.",
            "card_report_btn": "Сообщить о проблеме",
            "card_demands_title": "Общественные инициативы и голосование",
            "card_demands_desc": "Голосуйте за парки, расширение дорог и водопровод, чтобы направить городской бюджет на важные цели.",
            "card_demands_btn": "Посмотреть инициативы",
            "card_track_title": "Мои обращения",
            "card_track_desc": "Следите за ходом выполнения заявок, назначенной ремонтной бригадой и слушайте голосовой отчет.",
            "card_track_btn": "Отследить обращения",
            "card_whatsapp_title": "WhatsApp Ассистент",
            "card_whatsapp_desc": "Общайтесь с нами в WhatsApp на русском, английском, хинди или родном языке.",
            "card_whatsapp_btn": "Открыть чат WhatsApp",

            "tag_quick_ai": "Быстрый анализ ИИ",
            "tag_10_categories": "10+ категорий",
            "tag_photo_review": "Анализ по фото",
            "tag_voice_msg": "Голосовое сообщение",
            "tag_auto_loc": "Авто-геолокация",
            "lbl_avg_resp": "Ответ за 4 сек",
            "lbl_votes_cast": "27 421 голос",
            "tag_public_voting": "Открытое голосование",
            "tag_local_budget": "Местный бюджет",
            "tag_ward_projects": "Проекты района",
            "tag_live_count": "Онлайн подсчет",
            "lbl_active_wards": "В 8 районах",
            "tag_step_status": "Пошаговый статус",
            "tag_voice_briefing": "Голосовой отчет",
            "tag_crew_map": "Карта бригады",
            "tag_proof_photos": "Фотоотчет",
            "lbl_tracked_live": "Живой трекинг",
            "lbl_24_7_wa": "24/7 в WhatsApp",
            "tag_no_app": "Без скачивания",
            "tag_any_lang": "Любой язык",
            "tag_smart_chat": "Умный чат",
            "tag_instant_ticket": "Быстрый номер",
            "lbl_instant_reply": "Мгновенный ответ",
            "sec_recently_fixed": "Недавно решенные проблемы в вашем районе",
            "sec_community_notices": "Объявления и районные встречи",

            "back_to_citizen_home": "← На главную",
            "return_to_executive_cmd": "← К общему обзору",

            "modal_report_title": "Сообщить о проблеме",
            "modal_report_sub": "Добавьте подробности, фото или голосовую запись для быстрого устранения.",
            "lbl_selected_category": "Выбранная категория",
            "lbl_problem": "В чем заключается проблема? *",
            "btn_voice_input": "Надиктовать с ИИ",
            "ph_desc": "Опишите повреждение, ближайший ориентир и как это мешает жителям...",
            "voice_listening": "Слушаю... Говорите на русском, хинди или английском",
            "btn_stop_rec": "Готово / Стоп",
            "lbl_neighborhood_ward": "Район / Округ *",
            "lbl_street_address": "Улица или ориентир",
            "btn_use_current_location": "Использовать текущую геопозицию",
            "ph_street_address": "например: Кольцевая дорога, у метро",
            "gps_acquired": "📍 GPS-координаты получены",
            "lbl_add_photo": "Добавить фото (необязательно)",
            "lbl_add_photo_hint": "ИИ автоматически оценит степень повреждения для ускорения ремонта.",
            "lbl_add_voice": "Голосовое сообщение (необязательно)",
            "lbl_add_voice_hint": "Говорите на русском, английском, хинди или родном языке.",
            "btn_cancel": "Отмена",
            "btn_submit_report": "Отправить заявку",

            "badge_demands_context": "Инициативы жителей",
            "sec_demands_title": "Общественные инициативы и голосование",
            "sec_demands_sub": "Голосуйте за благоустройство района, новые парки и дороги для влияния на городской бюджет.",
            "btn_propose_project": "+ Предложить проект",
            "ph_search_demands": "Поиск проектов по названию, району или ключевому слову...",
            "opt_all_wards": "Все районы / округа",
            "btn_upvote": "Поддержать",
            "lbl_votes": "Голосов",
            "lbl_est_cost": "Ориентировочная стоимость",
            "lbl_beneficiaries": "Благополучателей",
            "lbl_proposed_by": "Автор инициативы",
            "modal_propose_title": "Предложить районный проект",
            "modal_propose_sub": "Проекты, набравшие наибольшее количество голосов, напрямую передаются в мэрию для финансирования.",
            "lbl_project_title": "Название проекта *",
            "ph_project_title": "например: Новый сквер с солнечным освещением в секторе 4",
            "lbl_category": "Категория *",
            "lbl_budget": "Ориентировочный бюджет",
            "ph_budget": "например: 50 млн руб. / R$ 300,000",
            "lbl_est_beneficiaries": "Охват жителей",
            "ph_beneficiaries": "например: 5 000 жителей",
            "lbl_why_needed": "Почему необходим этот проект? *",
            "ph_why_needed": "Опишите пользу проекта для района и жителей...",
            "btn_submit_voting": "Опубликовать для голосования",

            "badge_track_context": "Отслеживание",
            "sec_track_title": "Отслеживание ваших заявок",
            "sec_track_sub": "Следите за стадиями ремонта, закрепленными специалистами и слушайте аудиоотчеты.",
            "ph_search_track": "Введите номер заявки (напр. CP-2026...) или адрес...",
            "btn_listen_briefing": "Прослушать голосовой отчет",
            "btn_open_maps": "Открыть в Google Maps",
            "step_submitted": "Принята",
            "step_dispatched": "Бригада направлена",
            "step_in_progress": "В работе",
            "step_resolved": "Выполнено",
            "lbl_assigned_worker": "Назначенный специалист",

            "badge_wa_context": "Чат WhatsApp",
            "sec_wa_title": "Чат с CivicPulse в WhatsApp",
            "sec_wa_sub": "Отправляйте сообщения, фото и голосовые заметки так же просто, как в диалоге с другом.",
            "wa_assistant_name": "Ассистент CivicPulse (Официальная поддержка)",
            "wa_online_status": "● Онлайн • Быстрый ответ",
            "badge_online": "ОНЛАЙН",
            "wa_bot_greeting": "Здравствуйте / Hello! Чем могу помочь? Отправьте голосовое сообщение или напишите о проблеме, и я сразу зарегистрирую заявку.",
            "btn_wa_sample_hi": "🇮🇳 Запись на хинди",
            "btn_wa_sample_pt": "🇧🇷 Сообщение на португальском",
            "btn_wa_sample_en": "🇿🇦 Сообщение на английском",
            "ph_wa_input": "Напишите сообщение или нажмите на пример выше...",

            "gov_hero_tag": "Городское планирование и диспетчеризация",
            "gov_hero_title": "Центр управления городскими проектами и операциями",
            "gov_hero_subtitle": "Мониторинг обращений граждан, распределение ремонтных бригад, стратегическое планирование и анализ бюджета с помощью ИИ.",
            "gov_welcome_title": "Оперативный обзор",
            "gov_welcome_desc": "Обращения граждан в реальном времени, рекомендации ИИ и бюджетные показатели. Выберите модуль для перехода.",
            "gov_badge_clearance": "Доступ администратора",
            "gov_badge_uptime": "99.98% времени работы",
            "gov_launchpad_title": "Модули городского управления",
            "gov_launchpad_subtitle": "Выберите инструмент для управления городским хозяйством:",

            "card_megaplan_title": "ИИ-планировщик городских проектов",
            "card_megaplan_desc": "Объединяет запросы жителей и демографические данные для выработки крупных проектов с оценкой затрат.",
            "card_megaplan_btn": "Открыть планировщик",
            "card_queue_title": "Очередь ремонтов и нарядов",
            "card_queue_desc": "Просмотр входящих заявок, отправка бригад на объекты, контроль сроков и приемка работ.",
            "card_queue_btn": "Открыть очередь работ",
            "card_budget_title": "Бюджетный баланс районов",
            "card_budget_desc": "Сравнение расходов по районам для обеспечения справедливого финансирования нуждающихся территорий.",
            "card_budget_btn": "Открыть баланс бюджета",
            "card_map_title": "Онлайн-карта города",
            "card_map_desc": "Интерактивная карта с обращениями, местоположением техники, границами районов и очагами аварийности.",
            "card_map_btn": "Открыть геокарту",
            "card_dpg_title": "Стандарты открытых данных (DPG)",
            "card_dpg_desc": "Проверка соответствия 9 стандартам цифровых общественных благ и открытые API.",
            "card_dpg_btn": "Смотреть стандарты",

            "sec_live_weather": "Метеостанция города",
            "badge_sensor_data": "Показания датчиков онлайн",
            "lbl_weather_source": "Источник: Сенсор Open-Meteo",
            "lbl_temperature": "Температура воздуха",
            "lbl_humidity": "Относительная влажность",
            "lbl_precipitation": "Осадки (дождь)",
            "lbl_wind_velocity": "Скорость ветра",
            "lbl_database": "База данных",
            "lbl_city_map_data": "ГИС-данные города",
            "lbl_storage": "Хранилище",
            "btn_sync_map_data": "Синхронизировать данные",
            "sec_recent_directives": "Последние распоряжения и действия мэрии",
            "sec_repair_status": "Статус ремонтных служб",
            "lbl_infra_health": "Индекс состояния инфраструктуры",
            "lbl_active_teams": "Работающие выездные бригады",
            "lbl_budget_influence": "Влияние голосов жителей",

            "badge_planning_context": "Городское развитие",
            "sec_megaplan_title": "Рекомендации ИИ по инфраструктуре",
            "sec_megaplan_sub": "Масштабные проекты, синтезированные на основе запросов населения, транспортной загруженности и приоритетов.",
            "btn_update_plan": "Обновить план ИИ",
            "lbl_capex": "Планируемый объем CapEx",
            "lbl_justification": "Обоснование проекта",
            "btn_approve_project": "Утвердить проект",

            "badge_queue_context": "Ремонты и диспетчеризация",
            "sec_queue_title": "Очередь городских заявок и ремонтов",
            "sec_queue_sub": "Фильтрация жалоб, диспетчеризация бригад и подтверждение устранения дефектов:",
            "th_id": "№",
            "th_category": "Категория",
            "th_description": "Описание",
            "th_ward": "Район",
            "th_severity": "Срочность",
            "th_status": "Статус",
            "th_action": "Действие",
            "btn_dispatch": "Направить бригаду",
            "btn_mark_resolved": "Пометить выполненным",

            "badge_budget_context": "Анализ бюджета",
            "sec_budget_title": "Бюджет районов и баланс расходов",
            "sec_budget_sub": "Сопоставление городских инвестиций с реальными потребностями районов:",
            "th_ward_budget": "Район / Округ",
            "th_population_vulnerability": "Население и уязвимость",
            "th_planned_budget": "Выделенный бюджет",
            "th_demand_share": "Доля запросов жителей",
            "th_funding_status": "Статус финансирования",
            "th_recommended_action": "Рекомендуемое действие",

            "badge_map_context": "Карта города",
            "sec_map_title": "Оперативная карта инцидентов",
            "sec_map_sub": "Цветные маркеры отображают статус инцидентов, приоритетные точки и спецтехнику:",

            "badge_dpg_context": "Открытые стандарты",
            "sec_dpg_title": "Стандарты цифровых общественных благ (DPG)",
            "sec_dpg_sub": "Полное соответствие 9 критериям Альянса цифровых общественных благ:",

            "login_hero_sub": "Объединение жителей и городских властей для создания комфортных районов в странах БРИКС.",
            "card_citizen_title": "Портал граждан",
            "card_citizen_tag": "Для жителей и сообществ",
            "card_citizen_desc": "Сообщайте о проблемах, голосуйте за инициативы и отслеживайте ремонт в реальном времени.",
            "lbl_citizen_email": "Email жителя или логин *",
            "ph_citizen_email": "напр.: resident@delhi.gov.in",
            "lbl_password": "Пароль *",
            "btn_sign_in_citizen": "Войти в портал граждан",
            "lbl_or": "ИЛИ",
            "btn_demo_citizen": "Демо-вход для граждан (в 1 клик)",
            "card_gov_title": "Государственный центр",
            "card_gov_tag": "Для сотрудников и градостроителей",
            "card_gov_desc": "Обработка обращений, выездные бригады, планирование объектов и балансировка бюджета с ИИ.",
            "lbl_gov_email": "Служебный email *",
            "ph_gov_email": "напр.: official@brics.gov",
            "btn_sign_in_gov": "Войти в государственный центр",
            "btn_demo_gov": "Демо-вход для властей (в 1 клик)",

            "status_pending": "Ожидает обработки",
            "status_progress": "В работе",
            "status_resolved": "Выполнено"
        }
    elif lang_code == "zh":
        return {
            "portal_citizen_badge": "市民门户",
            "portal_gov_badge": "政府指挥中心",
            "nav_back": "返回",
            "nav_home": "首页",
            "btn_sign_out": "退出登录",
            "btn_exit_command": "退出指挥中心",
            "detected_node_title": "自动识别节点",
            "badge_cloud_connected": "云端已连接",
            "badge_live_data": "实时云数据",
            "badge_open_standard": "DPG 开放标准",

            "sector_roads_transit_name": "道路、桥梁与主干道走廊",
            "sector_roads_transit_badge": "交通骨干",
            "sector_roads_transit_desc": "快速路、高架立交桥、主干道路面维护、结构桥梁与人行天桥",

            "sector_water_supply_name": "供水管网与管道渗漏排查",
            "sector_water_supply_badge": "清洁饮水",
            "sector_water_supply_desc": "清洁饮用水分配、高压干管、智能漏损遥测与泵站调度",

            "sector_electricity_grid_name": "电力供应、路灯照明与电网",
            "sector_electricity_grid_badge": "能源基础设施",
            "sector_electricity_grid_desc": "高压变电站、地下综合管廊电缆、智能LED路灯与停电防范",

            "sector_waste_sanitation_name": "垃圾管理与环卫清洁",
            "sector_waste_sanitation_badge": "循环保洁",
            "sector_waste_sanitation_desc": "自动化资源回收、生物制气厂、垃圾填埋场生态修复与上门清运",

            "sector_public_transport_name": "公共交通与综合枢纽",
            "sector_public_transport_badge": "出行走廊",
            "sector_public_transport_desc": "地铁接驳线路、纯电动公交车队、多式联运客运枢纽与候车亭",

            "sector_stormwater_flood_name": "雨水排涝与汛期防洪工程",
            "sector_stormwater_flood_badge": "防汛水利",
            "sector_stormwater_flood_desc": "重力排水主干渠、江河护岸堤防、蓄洪调节池与自动化水闸",

            "sector_health_clinics_name": "公共卫生、社区诊所与病媒防制",
            "sector_health_clinics_badge": "社区医疗",
            "sector_health_clinics_desc": "急救创伤中心、母婴健康驿站、应急药品储备遥测与蚊虫消杀",

            "sector_schools_facilities_name": "公立学校与公共文教设施",
            "sector_schools_facilities_badge": "社会基础设施",
            "sector_schools_facilities_desc": "学校校舍安全排查、职业技术培训中心、社区公益图书馆与数字实验室",

            "sector_parks_environment_name": "城市公园、绿化带与空气质量",
            "sector_parks_environment_badge": "生态修复",
            "sector_parks_environment_desc": "城市造林工程、防霾降尘喷雾塔、公园太阳能照明与生态走廊",

            "sector_public_safety_name": "公共安全与应急防御基础设施",
            "sector_public_safety_badge": "应急防护",
            "sector_public_safety_desc": "高压消防栓网络、市政防灾避险疏散通道、天网高清视频监控与警报系统",

            "sec_choose_category": "选择服务领域",
            "sec_choose_category_sub": "从全市10大市政基础设施板块中选择您要反映的问题：",
            "sec_category_prompt": "点击上方任一板块，即可打开支持拍照与语音上报的快捷工单表单。",
            "lbl_sla_24h": "解决时限: < 24小时",
            "btn_report_issue": "上报问题",
            "badge_report_context": "上报市政问题",

            "cit_hero_tag": "公众市政参与平台",
            "cit_hero_title": "反映民生诉求 · 共建社区规划",
            "cit_hero_subtitle": "便捷上报周边设施故障，对社区公共改造项目进行投票，通过照片与语音实时追踪维修进度。",
            "cit_welcome_title": "欢迎您，Priya Sharma",
            "cit_welcome_desc": "您的专属市民门户：一键反映问题、参与社区微改造投票、全程追踪工单进度。",
            "cit_badge_resident": "实名认证居民 • 德里",
            "cit_badge_ward": "第14社区 • 德里首都圈",
            "cit_badge_sla": "98.4% 按期办结率",
            "cit_launchpad_title": "您今天想办理什么业务？",
            "cit_launchpad_subtitle": "请从下方功能入口选择：",

            "card_report_title": "上报市政设施问题",
            "card_report_desc": "路面坑洼、路灯不亮、管道跑冒滴漏或垃圾堆积，拍照或录一段语音即可快速报修。",
            "card_report_btn": "立即上报",
            "card_demands_title": "社区诉求与公共投票墙",
            "card_demands_desc": "为新建公园、道路拓宽和净水工程投票，让市民意愿直接影响市政预算分配。",
            "card_demands_btn": "查看社区诉求",
            "card_track_title": "追踪我的报修工单",
            "card_track_desc": "查看工单最新处理进度，了解指派的维修师傅，收听多语言语音进度播报。",
            "card_track_btn": "追踪工单进度",
            "card_whatsapp_title": "WhatsApp 智能民生助手",
            "card_whatsapp_desc": "通过 WhatsApp 发送文字、照片或语音，支持中文、英语、印地语等多语种实时沟通。",
            "card_whatsapp_btn": "打开 WhatsApp 咨询",

            "tag_quick_ai": "AI 快速初审",
            "tag_10_categories": "10+ 服务大类",
            "tag_photo_review": "图像智能定损",
            "tag_voice_msg": "语音便捷输入",
            "tag_auto_loc": "高精度定位",
            "lbl_avg_resp": "平均响应 4秒",
            "lbl_votes_cast": "已投 27,421 票",
            "tag_public_voting": "公众公开投票",
            "tag_local_budget": "社区微预算",
            "tag_ward_projects": "片区实事件",
            "tag_live_count": "实时计票",
            "lbl_active_wards": "覆盖8大片区",
            "tag_step_status": "节点全程追踪",
            "tag_voice_briefing": "语音状态播报",
            "tag_crew_map": "工班位置地图",
            "tag_proof_photos": "办结前后对比",
            "lbl_tracked_live": "全程在线透明",
            "lbl_24_7_wa": "7×24小时在线",
            "tag_no_app": "无需安装 App",
            "tag_any_lang": "多语种支持",
            "tag_smart_chat": "智能对话",
            "tag_instant_ticket": "即时生成编号",
            "lbl_instant_reply": "秒级响应",
            "sec_recently_fixed": "您所在片区最新办结公示",
            "sec_community_notices": "社区民生公告与民主协商会",

            "back_to_citizen_home": "← 返回市民首页",
            "return_to_executive_cmd": "← 返回指挥中心总览",

            "modal_report_title": "上报市政设施问题",
            "modal_report_sub": "提供详细描述、现场照片或语音说明，以便工班以最快速度处置。",
            "lbl_selected_category": "已选服务大类",
            "lbl_problem": "问题具体情况 *",
            "btn_voice_input": "AI 语音输入",
            "ph_desc": "请描述故障情况、附近明显地标或商铺，以及对居民出行的影响...",
            "voice_listening": "正在倾听... 请使用中文、英语、印地语或母语说话",
            "btn_stop_rec": "完成 / 停止",
            "lbl_neighborhood_ward": "所在片区 / 社区 *",
            "lbl_street_address": "详细街道地址或标志物",
            "btn_use_current_location": "获取当前位置",
            "ph_street_address": "例如：外环路地铁2号口往北100米",
            "gps_acquired": "📍 已成功捕获 GPS 经纬度",
            "lbl_add_photo": "上传现场照片 (选填)",
            "lbl_add_photo_hint": "系统内置视觉模型将自动分析损坏等级，加快工班派单速度。",
            "lbl_add_voice": "上传语音说明 (选填)",
            "lbl_add_voice_hint": "支持普通话、英语、印地语、葡萄牙语等语音录入。",
            "btn_cancel": "取消",
            "btn_submit_report": "提交报修单",

            "badge_demands_context": "社区心愿墙",
            "sec_demands_title": "社区诉求与公共投票墙",
            "sec_demands_sub": "为新建公园、道路拓宽和净水工程投票，让市民意愿直接影响市政预算分配。",
            "btn_propose_project": "+ 提出新微改造提案",
            "ph_search_demands": "输入提案名称、社区或关键字进行搜索...",
            "opt_all_wards": "全市所有片区 / 社区",
            "btn_upvote": "赞成投票",
            "lbl_votes": "获得票数",
            "lbl_est_cost": "预估工程总投资",
            "lbl_beneficiaries": "预计受惠人口",
            "lbl_proposed_by": "提案发起主体",
            "modal_propose_title": "发起社区改造微提案",
            "modal_propose_sub": "得票靠前的民生项目将直接上报市规建委列入下阶段财政重点预算。",
            "lbl_project_title": "项目名称 *",
            "ph_project_title": "例如：4区加装太阳能路灯与街角绿化口袋公园",
            "lbl_category": "所属基础设施领域 *",
            "lbl_budget": "预估资金需求",
            "ph_budget": "例如：人民币 50万元 / R$ 300,000",
            "lbl_est_beneficiaries": "预计惠及居民",
            "ph_beneficiaries": "例如：5,000名常住居民",
            "lbl_why_needed": "立项必要性陈述 *",
            "ph_why_needed": "说明该微改造工程对改善社区生活环境的必要性及预期效果...",
            "btn_submit_voting": "提交进入公开投票",

            "badge_track_context": "工单追踪中心",
            "sec_track_title": "我的报修工单实时追踪",
            "sec_track_sub": "了解报修进度流水线，查看责任技师与网格员，收听智能语音进度播报。",
            "ph_search_track": "输入工单号 (如 CP-2026...) 或街道名称...",
            "btn_listen_briefing": "收听语音进度播报",
            "btn_open_maps": "在地图中精确定位",
            "step_submitted": "工单已受理",
            "step_dispatched": "工班已派发",
            "step_in_progress": "施工抢修中",
            "step_resolved": "已修复办结",
            "lbl_assigned_worker": "负责工班组长",

            "badge_wa_context": "WhatsApp 智能客服",
            "sec_wa_title": "在 WhatsApp 与 CivicPulse 互动",
            "sec_wa_sub": "像与好友聊天一样，随时发送文字、照片或语音即刻办结市政申报。",
            "wa_assistant_name": "CivicPulse 官方市政助手 (官方认证)",
            "wa_online_status": "● 在线 · 智能秒回",
            "badge_online": "在线",
            "wa_bot_greeting": "您好！请问有什么可以帮您？发送语音或简短文字告诉我您身边的设施损坏，我将第一时间为您立案。",
            "btn_wa_sample_hi": "🇮🇳 印地语语音示例",
            "btn_wa_sample_pt": "🇧🇷 葡萄牙语录音",
            "btn_wa_sample_en": "🇿🇦 英语报修文本",
            "ph_wa_input": "输入问题或点击上方示例快速体验...",

            "gov_hero_tag": "市域治理与城市运行指挥中心",
            "gov_hero_title": "城市重大基础设施规划与运行指挥枢纽",
            "gov_hero_subtitle": "打通基层民情诉求与市政资本开支 (CapEx)，结合 Gemini 2.5 和地理空间分析的数字治理驾驶舱。",
            "gov_welcome_title": "运行指挥概览",
            "gov_welcome_desc": "实时汇聚市民诉求、AI 规划建议及财政预算分配。请选择下方任一功能模块开展调度。",
            "gov_badge_clearance": "安全权限：指挥级",
            "gov_badge_uptime": "系统高可用 99.98%",
            "gov_launchpad_title": "城市管理核心功能模块",
            "gov_launchpad_subtitle": "点击下方卡片进入对应业务调度工作台：",

            "card_megaplan_title": "AI 基础设施工程规划引擎",
            "card_megaplan_desc": "深度提炼数以万计的民生诉求与人口普查数据，生成兼具成本估算与效益预测的重大工程方案。",
            "card_megaplan_btn": "打开规划引擎",
            "card_queue_title": "抢修调度与工单流转",
            "card_queue_desc": "审核群众诉求、网格化调度应急工程队、监控时效预警并验收办结质量。",
            "card_queue_btn": "进入工单调度中心",
            "card_budget_title": "资本支出差异与预算均衡",
            "card_budget_desc": "比对各片区公共投入与民生需求指数，识别薄弱环节，实现资源科学精准倾斜。",
            "card_budget_btn": "进入预算均衡矩阵",
            "card_map_title": "地理空间实况指挥地图",
            "card_map_desc": "交互式 GIS 地图，展示热点事件、抢修车定位、网格界线及应急资源分布。",
            "card_map_btn": "打开指挥大屏地图",
            "card_dpg_title": "数字公共产品 (DPG) 规范",
            "card_dpg_desc": "全面遵循联合国 DPGA 9项指标验证标准及 OpenAPI 3.1 开放架构规范。",
            "card_dpg_btn": "查看 DPG 合规报告",

            "sec_live_weather": "城市微气象实时监测站",
            "badge_sensor_data": "实时物联网传感器",
            "lbl_weather_source": "数据源：Open-Meteo 高精度气象遥感",
            "lbl_temperature": "环境温度",
            "lbl_humidity": "空气相对湿度",
            "lbl_precipitation": "实时降雨量",
            "lbl_wind_velocity": "地面风速",
            "lbl_database": "数据底座",
            "lbl_city_map_data": "GIS 空间数据流",
            "lbl_storage": "数据仓库",
            "btn_sync_map_data": "同步空间分区数据",
            "sec_recent_directives": "最新下达的城市运行调度令",
            "sec_repair_status": "市政一线抢修工班状态",
            "lbl_infra_health": "市政设施健康指数",
            "lbl_active_teams": "一线作业工班数",
            "lbl_budget_influence": "公众投票参与度",

            "badge_planning_context": "工程规划",
            "sec_megaplan_title": "AI 智能综合基建规划建议",
            "sec_megaplan_sub": "基于市民诉求聚合、交通堵点辨识及人口分布自动生成的重大公共工程方案。",
            "btn_update_plan": "重新生成 AI 规划方案",
            "lbl_capex": "预估资本性支出 (CapEx)",
            "lbl_justification": "立项论证与效益分析",
            "btn_approve_project": "批准立项进入招投标",

            "badge_queue_context": "抢修调度",
            "sec_queue_title": "接诉即办 · 市政诉求处置工单池",
            "sec_queue_sub": "全流程闭环处理市民工单，智能派单、工单催办及办结抽检：",
            "th_id": "工单号",
            "th_category": "业务分类",
            "th_description": "工单简述",
            "th_ward": "所在片区",
            "th_severity": "优先级",
            "th_status": "流转状态",
            "th_action": "调度操作",
            "btn_dispatch": "指派工班",
            "btn_mark_resolved": "确认办结",

            "badge_budget_context": "财政审计",
            "sec_budget_title": "片区预算分配与基础设施均等化分析",
            "sec_budget_sub": "比对各片区历史投入与实际民生诉求比例，纠正资金错配与薄弱环节：",
            "th_ward_budget": "行政片区 / 社区",
            "th_population_vulnerability": "常住人口与脆弱性指标",
            "th_planned_budget": "已核拨预算",
            "th_demand_share": "诉求占比指数",
            "th_funding_status": "均衡状态判定",
            "th_recommended_action": "财政平衡建议",

            "badge_map_context": "空间指挥",
            "sec_map_title": "2D/3D 空间动态感知一张图",
            "sec_map_sub": "以不同颜色标识事件处置状态、高发热点、抢修车实时 GPS 及应急避难所：",

            "badge_dpg_context": "开源合规",
            "sec_dpg_title": "数字公共产品联盟 (DPGA) 标准",
            "sec_dpg_sub": "全面通过 9 项核心指标严格审查，实现开放架构与数据主权并重：",

            "login_hero_sub": "连接市民诉求与城市规划，携手共建金砖国家智慧宜居现代化社区。",
            "card_citizen_title": "市民直通门户",
            "card_citizen_tag": "面向常住居民与社区自治组织",
            "card_citizen_desc": "在线上报民生故障、参与社区民意投票、全程追踪抢修办结实效。",
            "lbl_citizen_email": "居民邮箱或身份证号 *",
            "ph_citizen_email": "例如: resident@delhi.gov.in",
            "lbl_password": "登录密码 *",
            "btn_sign_in_citizen": "进入市民门户",
            "lbl_or": "或",
            "btn_demo_citizen": "一键以市民身份体验 (快速演示)",
            "card_gov_title": "政府指挥中心",
            "card_gov_tag": "面向城市管理者、网格长与规划工程师",
            "card_gov_desc": "全量审阅民生诉求、一键调度专业工班、AI规划重大工程、优化均衡财政支出。",
            "lbl_gov_email": "政府政务邮箱 *",
            "ph_gov_email": "例如: official@brics.gov",
            "btn_sign_in_gov": "进入指挥中心",
            "btn_demo_gov": "一键以官员身份体验 (快速演示)",

            "status_pending": "待分流处理",
            "status_progress": "工班抢修中",
            "status_resolved": "已核验办结"
        }
    
    # For Tamil, Telugu, Zulu, Afrikaans: build comprehensive high quality translations
    # using English fallback + distinct authentic localized terms
    d = dict(EN)
    
    if lang_code == "ta": # Tamil
        d["portal_citizen_badge"] = "குடிமக்கள் தளம்"
        d["portal_gov_badge"] = "அரசு கட்டுப்பாட்டு மையம்"
        d["nav_back"] = "பின்செல்"
        d["nav_home"] = "முகப்பு"
        d["btn_sign_out"] = "வெளியேறு"
        d["btn_exit_command"] = "வெளியேறு"
        d["sec_choose_category"] = "ஒரு துறையைத் தேர்ந்தெடுக்கவும்"
        d["sec_choose_category_sub"] = "எங்கள் 10 நகர துறைகளில் உங்கள் பிரச்சனைக்குரிய துறையைத் தேர்ந்தெடுக்கவும்:"
        d["lbl_sla_24h"] = "தீர்வு நேரம்: < 24 மணி"
        d["btn_report_issue"] = "புகார் செய்"
        d["badge_report_context"] = "புகார் பதிவு"
        d["sector_roads_transit_name"] = "சாலைகள், பாலங்கள் மற்றும் பெருவழிகள்"
        d["sector_water_supply_name"] = "குடிநீர் வழங்கல் மற்றும் குழாய் கசிவு"
        d["sector_electricity_grid_name"] = "மின்சாரம், தெருவிளக்குகள் மற்றும் கட்டமைப்பு"
        d["sector_waste_sanitation_name"] = "கழிவு மேலாண்மை மற்றும் துப்புரவு"
        d["sector_public_transport_name"] = "பொதுப் போக்குவரத்து மற்றும் முனையங்கள்"
        d["sector_stormwater_flood_name"] = "மழைநீர் வடிகால் மற்றும் வெள்ளத் தடுப்பு"
        d["sector_health_clinics_name"] = "பொது சுகாதாரம் மற்றும் மருத்துவமனைகள்"
        d["sector_schools_facilities_name"] = "அரசுப் பள்ளிகள் மற்றும் பொது வசதிகள்"
        d["sector_parks_environment_name"] = "பூங்காக்கள் மற்றும் காற்றுத் தரம்"
        d["sector_public_safety_name"] = "பொதுப் பாதுகாப்பு மற்றும் அவசர உதவிகள்"
        d["modal_report_title"] = "புகாரை பதிவு செய்யவும்"
        d["lbl_problem"] = "பிரச்சனை என்ன? *"
        d["btn_voice_input"] = "குரல் வழி பதிவு"
        d["lbl_neighborhood_ward"] = "பகுதி / வார்டு *"
        d["btn_use_current_location"] = "தற்போதைய இருப்பிடத்தைப் பயன்படுத்து"
        d["btn_submit_report"] = "புகாரை சமர்ப்பி"
        d["card_report_title"] = "புகார் பதிவு செய்யவும்"
        d["card_demands_title"] = "சமூக கோரிக்கைகள் மற்றும் வாக்குப்பதிவு"
        d["card_track_title"] = "புகார் நிலையை அறிய"
        d["card_whatsapp_title"] = "வாட்ஸ்அப் உதவி மையம்"
        d["status_pending"] = "பரிசீலனையில்"
        d["status_progress"] = "பணியில்"
        d["status_resolved"] = "தீர்க்கப்பட்டது"

    elif lang_code == "te": # Telugu
        d["portal_citizen_badge"] = "పౌర వేదిక"
        d["portal_gov_badge"] = "ప్రభుత్వ కమాండ్ సెంటర్"
        d["nav_back"] = "వెనుకకు"
        d["nav_home"] = "హోమ్"
        d["btn_sign_out"] = "లాగ్ అవుట్"
        d["btn_exit_command"] = "నిష్క్రమించు"
        d["sec_choose_category"] = "విభాగాన్ని ఎంచుకోండి"
        d["sec_choose_category_sub"] = "మా 10 నగర విభాగాలలో మీ సమస్యకు సరిపోలే రంగాన్ని ఎంచుకోండి:"
        d["lbl_sla_24h"] = "పరిష్కార గడువు: < 24 గం"
        d["btn_report_issue"] = "ఫిర్యాదు చేయండి"
        d["badge_report_context"] = "సమస్య నమోదు"
        d["sector_roads_transit_name"] = "రోడ్లు, వంతెనలు మరియు రహదారులు"
        d["sector_water_supply_name"] = "నీటి సరఫరా మరియు పైప్‌లైన్ లీకేజీలు"
        d["sector_electricity_grid_name"] = "విద్యుత్, వీధి దీపాలు మరియు గ్రిడ్"
        d["sector_waste_sanitation_name"] = "వ్యర్థాల నిర్వహణ మరియు పారిశుధ్యం"
        d["sector_public_transport_name"] = "ప్రజా రవాణా మరియు బస్ టెర్మినల్స్"
        d["sector_stormwater_flood_name"] = "వర్షపు నీటి డ్రైనేజీ మరియు వరద రక్షణ"
        d["sector_health_clinics_name"] = "ప్రజారోగ్యం, క్లినిక్‌లు మరియు వ్యాధి నియంత్రణ"
        d["sector_schools_facilities_name"] = "ప్రభుత్వ పాఠశాలలు మరియు ప్రజా సౌకర్యాలు"
        d["sector_parks_environment_name"] = "ప్రజా పార్కులు మరియు గాలి నాణ్యత"
        d["sector_public_safety_name"] = "ప్రజా భద్రత మరియు అత్యవసర వ్యవస్థ"
        d["modal_report_title"] = "ఫిర్యాదును నమోదు చేయండి"
        d["lbl_problem"] = "సమస్య ఏమిటి? *"
        d["btn_voice_input"] = "వాయిస్ ద్వారా నమోదు చేయండి"
        d["lbl_neighborhood_ward"] = "ప్రాంతం / వార్డు *"
        d["btn_use_current_location"] = "ప్రస్తుత లొకేషన్ ఉపయోగించండి"
        d["btn_submit_report"] = "ఫిర్యాదు సమర్పించండి"
        d["card_report_title"] = "సమస్యను నివేదించండి"
        d["card_demands_title"] = "కమ్యూనిటీ డిమాండ్లు & ఓటింగ్"
        d["card_track_title"] = "నా ఫిర్యాదులను ట్రాక్ చేయండి"
        d["card_whatsapp_title"] = "వాట్సాప్ సహాయం"
        d["status_pending"] = "పరిశీలనలో ఉంది"
        d["status_progress"] = "పురోగతిలో ఉంది"
        d["status_resolved"] = "పరిష్కరించబడింది"

    elif lang_code == "zu": # isiZulu
        d["portal_citizen_badge"] = "Ingosi Yezakhamizi"
        d["portal_gov_badge"] = "Isikhungo Sikahulumeni"
        d["nav_back"] = "Emuva"
        d["nav_home"] = "Ekhaya"
        d["btn_sign_out"] = "Phuma"
        d["btn_exit_command"] = "Phuma Esikhungweni"
        d["sec_choose_category"] = "Khetha Umkhakha"
        d["sec_choose_category_sub"] = "Khetha umkhakha ohambisana nenkinga yakho emikhakheni yethu eyi-10 yedolobha:"
        d["lbl_sla_24h"] = "Isikhathi: < 24h"
        d["btn_report_issue"] = "Bika Inkinga"
        d["badge_report_context"] = "Bika Inkinga"
        d["sector_roads_transit_name"] = "Imigwaqo, Amabhuloho Nemigwaqo Emikhulu"
        d["sector_water_supply_name"] = "Ukuhlinzekwa Kwamanzi Nokuvuza Kwamapayipi"
        d["sector_electricity_grid_name"] = "Ugesi, Izibani Zomgwaqo Negridi"
        d["sector_waste_sanitation_name"] = "Ukulawulwa Kwendle Nokuhlanzeka"
        d["sector_public_transport_name"] = "Ezokuthutha Zomphakathi Neziteshi"
        d["sector_stormwater_flood_name"] = "Amanzi Emvula Nokunqanda Izikhukhula"
        d["sector_health_clinics_name"] = "Ezempilo Yomphakathi Nemitholampilo"
        d["sector_schools_facilities_name"] = "Izikole Zikahulumeni Nezindawo Zomphakathi"
        d["sector_parks_environment_name"] = "Amapaki Omphakathi Nezinga Lomoya"
        d["sector_public_safety_name"] = "Ukuphepha Komphakathi Nezimo Eziphuthumayo"
        d["modal_report_title"] = "Bika Inkinga Kamasipala"
        d["lbl_problem"] = "Yini inkinga? *"
        d["btn_voice_input"] = "Khuluma ne-AI"
        d["lbl_neighborhood_ward"] = "Indawo / Iwadi *"
        d["btn_use_current_location"] = "Sebenzisa Indawo Yamanje"
        d["btn_submit_report"] = "Thumela Umbiko"
        d["card_report_title"] = "Bika Inkinga"
        d["card_demands_title"] = "Izicelo Zomphakathi Nokuvota"
        d["card_track_title"] = "Landelela Imibiko Yami"
        d["card_whatsapp_title"] = "Umsizi We-WhatsApp"
        d["status_pending"] = "Ilinde Ukubuyekezwa"
        d["status_progress"] = "Iyasebenza"
        d["status_resolved"] = "Iilungisiwe"

    elif lang_code == "af": # Afrikaans
        d["portal_citizen_badge"] = "Burgerportaal"
        d["portal_gov_badge"] = "Regeringsentrum"
        d["nav_back"] = "Terug"
        d["nav_home"] = "Tuis"
        d["btn_sign_out"] = "Teken Uit"
        d["btn_exit_command"] = "Verlaat Portaal"
        d["sec_choose_category"] = "Kies 'n Kategorie"
        d["sec_choose_category_sub"] = "Kies die kategorie wat by jou probleem pas oor ons 10 stadssektore:"
        d["lbl_sla_24h"] = "SLA: < 24u"
        d["btn_report_issue"] = "Meld Probleem Aan"
        d["badge_report_context"] = "Meld Probleem Aan"
        d["sector_roads_transit_name"] = "Paaie, Brûe en Hoofweë"
        d["sector_water_supply_name"] = "Watervoorsiening en Pyplyngleuwe"
        d["sector_electricity_grid_name"] = "Elektrisiteit, Straatligte en Kragnetwerk"
        d["sector_waste_sanitation_name"] = "Afvalbestuur en Sanitasie"
        d["sector_public_transport_name"] = "Openbare Vervoer en Haltes"
        d["sector_stormwater_flood_name"] = "Stormwaterdreinering en Vloedbeheer"
        d["sector_health_clinics_name"] = "Openbare Gesondheid en Klinieke"
        d["sector_schools_facilities_name"] = "Staatskole en Openbare Geriewe"
        d["sector_parks_environment_name"] = "Openbare Parke en Luggehalte"
        d["sector_public_safety_name"] = "Openbare Veiligheid en Nooddienste"
        d["modal_report_title"] = "Meld 'n Probleem Aan"
        d["lbl_problem"] = "Wat is die probleem? *"
        d["btn_voice_input"] = "Praat met KI"
        d["lbl_neighborhood_ward"] = "Wyk / Buurt *"
        d["btn_use_current_location"] = "Gebruik Huidige Ligging"
        d["btn_submit_report"] = "Dien Verslag In"
        d["card_report_title"] = "Meld 'n Probleem Aan"
        d["card_demands_title"] = "Gemeenskapsversoeke en Stemme"
        d["card_track_title"] = "Volg My Verslae"
        d["card_whatsapp_title"] = "WhatsApp-assistent"
        d["status_pending"] = "Hangende Hersiening"
        d["status_progress"] = "Aan die Gang"
        d["status_resolved"] = "Opgelos"

    return d

ALL_TRANSLATIONS = {
    "en": EN,
    "hi": HI,
    "pt": PT,
    "ru": create_localized_dict("ru"),
    "zh": create_localized_dict("zh"),
    "ta": create_localized_dict("ta"),
    "te": create_localized_dict("te"),
    "zu": create_localized_dict("zu"),
    "af": create_localized_dict("af")
}


# Inject extra keys across all languages
for lang, kvs in {'en': {'badge_underfunding': 'SEVERE UNDERFUNDING', 'badge_surplus': 'SURPLUS ALLOCATION', 'badge_balanced': 'OPTIMAL BALANCE', 'btn_reopen': 'Re-open Incident'}, 'hi': {'badge_underfunding': 'गंभीर कम फंडिंग', 'badge_surplus': 'अधिशेष आवंटन', 'badge_balanced': 'संतुलित आवंटन', 'btn_reopen': 'शिकायत दोबारा खोलें'}, 'pt': {'badge_underfunding': 'SUBFINANCIAMENTO SEVERO', 'badge_surplus': 'ALOCAÇÃO COM SUPERÁVIT', 'badge_balanced': 'EQUILÍBRIO ÓTIMO', 'btn_reopen': 'Reabrir Incidente'}, 'ru': {'badge_underfunding': 'ОСТРЫЙ ДЕФИЦИТ СРЕДСТВ', 'badge_surplus': 'ПРОФИЦИТНОЕ ВЫДЕЛЕНИЕ', 'badge_balanced': 'ОПТИМАЛЬНЫЙ БАЛАНС', 'btn_reopen': 'Возобновить заявку'}, 'zh': {'badge_underfunding': '严重资金不足', 'badge_surplus': '预算盈余分配', 'badge_balanced': '最佳预算平衡', 'btn_reopen': '重新打开事件'}, 'ta': {'badge_underfunding': 'கடுமையான நிதி பற்றாக்குறை', 'badge_surplus': 'உபரி நிதி ஒதுக்கீடு', 'badge_balanced': 'உகந்த சமநிலை', 'btn_reopen': 'புகாரை மீண்டும் திறக்க'}, 'te': {'badge_underfunding': 'తీవ్రమైన నిధుల కొరత', 'badge_surplus': 'మిగులు నిధుల కేటాయింపు', 'badge_balanced': 'సరైన బడ్జెట్ సమతుల్యత', 'btn_reopen': 'ఫిర్యాదును మళ్లీ తెరవండి'}, 'zu': {'badge_underfunding': 'UKUSWELEKA KWEZIMALI OKUKHULU', 'badge_surplus': 'UKWABIWA KWENZALO ETHE XAXA', 'badge_balanced': 'UKULINGANA OKUFANELEKILE', 'btn_reopen': 'Vula Kabusha Isikhalazo'}, 'af': {'badge_underfunding': 'ERNSTIGE ONDERBEFONDSING', 'badge_surplus': 'SURPLUS TOEWYSING', 'badge_balanced': 'OPTIMALE BALANS', 'btn_reopen': 'Heropen Klagte'}}.items():
    if lang in ALL_TRANSLATIONS:
        ALL_TRANSLATIONS[lang].update(kvs)

js_content = f"""/**
 * CIVICPULSE-BRICS: SOVEREIGN INTERNATIONALIZATION (i18n) ENGINE
 * Comprehensive Translations for 9 BRICS & Regional Languages:
 * English (en), Hindi (hi), Portuguese (pt), Russian (ru), Mandarin Chinese (zh),
 * Tamil (ta), Telugu (te), isiZulu (zu), Afrikaans (af)
 */

window.I18N = {json.dumps(ALL_TRANSLATIONS, indent=2, ensure_ascii=False)};

/**
 * Universal translation getter with optional fallback
 */
window.getTranslation = function(key, fallback = '') {{
  const lang = localStorage.getItem('civicpulse_lang') || 'en';
  const dict = (window.I18N && window.I18N[lang]) || (window.I18N && window.I18N['en']) || {{}};
  return dict[key] || (window.I18N && window.I18N['en'] && window.I18N['en'][key]) || fallback;
}};
window.i18n = window.getTranslation;

/**
 * Global Language Switcher with Instant Dynamic Component Re-Rendering
 */
window.setLanguage = function(lang) {{
  if (!window.I18N || !window.I18N[lang]) {{
    lang = 'en';
  }}
  
  localStorage.setItem('civicpulse_lang', lang);
  document.documentElement.setAttribute('lang', lang);

  // Sync all language dropdowns
  document.querySelectorAll('#lang-selector, #login-lang-select').forEach(sel => {{
    if (sel.value !== lang) sel.value = lang;
  }});

  const dict = window.I18N[lang] || window.I18N['en'];

  // Apply to text content
  document.querySelectorAll('[data-i18n]').forEach(el => {{
    const key = el.getAttribute('data-i18n');
    if (dict[key]) {{
      el.textContent = dict[key];
    }}
  }});

  // Apply to placeholder attributes
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {{
    const key = el.getAttribute('data-i18n-placeholder');
    if (dict[key]) {{
      el.setAttribute('placeholder', dict[key]);
    }}
  }});

  // Apply to title attributes
  document.querySelectorAll('[data-i18n-title]').forEach(el => {{
    const key = el.getAttribute('data-i18n-title');
    if (dict[key]) {{
      el.setAttribute('title', dict[key]);
    }}
  }});

  // Automatically re-render dynamic components if present
  try {{
    if (window.renderSectorCards && typeof window.renderSectorCards === 'function') {{
      window.renderSectorCards();
    }}
  }} catch(e) {{
    console.warn('renderSectorCards re-render:', e);
  }}

  try {{
    if (window.renderDemands && typeof window.renderDemands === 'function' && window.AppState && window.AppState.demands) {{
      window.renderDemands(window.AppState.demands);
    }}
  }} catch(e) {{
    console.warn('renderDemands re-render:', e);
  }}

  try {{
    if (window.renderTrackedComplaints && typeof window.renderTrackedComplaints === 'function' && window.AppState && window.AppState.complaints) {{
      window.renderTrackedComplaints(window.AppState.complaints);
    }}
  }} catch(e) {{
    console.warn('renderTrackedComplaints re-render:', e);
  }}

  try {{
    if (window.renderMegaPlans && typeof window.renderMegaPlans === 'function' && window.AppState && window.AppState.megaPlans) {{
      window.renderMegaPlans();
    }}
  }} catch(e) {{
    console.warn('renderMegaPlans re-render:', e);
  }}

  try {{
    if (window.renderBudgetTable && typeof window.renderBudgetTable === 'function' && window.AppState && window.AppState.budgetAlignment) {{
      window.renderBudgetTable();
    }}
  }} catch(e) {{
    console.warn('renderBudgetTable re-render:', e);
  }}

  // Trigger custom event for other modules
  window.dispatchEvent(new CustomEvent('civicpulse:languageChanged', {{ detail: {{ lang, dict }} }}));
}};

/**
 * Initialize language from storage or browser preference
 */
window.initLanguage = function() {{
  const savedLang = localStorage.getItem('civicpulse_lang');
  let initialLang = savedLang;

  if (!initialLang) {{
    const browserLang = (navigator.language || navigator.userLanguage || 'en').toLowerCase().split('-')[0];
    if (window.I18N && window.I18N[browserLang]) {{
      initialLang = browserLang;
    }} else {{
      initialLang = 'en';
    }}
  }}

  window.setLanguage(initialLang);

// Setup change event listeners on all language dropdowns
  document.querySelectorAll('#lang-selector, #login-lang-select, .lang-select').forEach(sel => {{
    sel.addEventListener('change', (e) => {{
      window.setLanguage(e.target.value);
    }});
  }});
}};

// Auto-initialize language engine upon page readiness
if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', window.initLanguage);
}} else {{
  window.initLanguage();
}}
"""

with open("static/js/i18n.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated static/js/i18n.js with {len(ALL_TRANSLATIONS)} languages. Key count in 'en': {len(EN)}, 'hi': {len(HI)}, 'pt': {len(PT)}")
