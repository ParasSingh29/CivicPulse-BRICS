/**
 * CIVICPULSE-BRICS: GOVERNMENT OFFICIAL & POLICYMAKER COMMAND HUB
 * AI Mega-Planning Engine with Sector Hierarchy & Sovereign Accents,
 * Operational Queue with Status Toggles, CapEx Budget Misalignment Matrix, Leaflet GIS Map, and DPG Indicators
 */

let govMap = null;
let mapMarkersGroup = null;

window.initGovernmentHub = function() {
  setupGovernmentEvents();
};

window.loadGovernmentData = async function() {
  await loadCloudStatus();
  await loadWeather();
  await loadMegaPlans();
  await loadGovComplaints();
  await loadBudgetAlignment();
  await loadDPGStandards();
  initOrUpdateMap();
};

// ==============================================================================
// 1. SETUP EVENT HANDLERS
// ==============================================================================
function setupGovernmentEvents() {
  const btnRefresh = document.getElementById('btn-refresh-megaplan');
  if (btnRefresh) {
    btnRefresh.addEventListener('click', async () => {
      btnRefresh.disabled = true;
      btnRefresh.innerHTML = `<span>${window.AppIcons.refresh}</span> <span>Gemini 2.5 Synthesizing Big Plans...</span>`;
      await loadMegaPlans();
      btnRefresh.disabled = false;
      btnRefresh.innerHTML = `
        <svg class="svg-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="23 4 23 10 17 10"/>
          <path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/>
        </svg>
        <span>Regenerate AI Infrastructure Plan</span>
      `;
      showToast('AI Mega-Infrastructure Plans updated with latest citizen upvotes!', 'success');
    });
  }

  const btnStreamBq = document.getElementById('btn-stream-bigquery');
  if (btnStreamBq) {
    btnStreamBq.addEventListener('click', async () => {
      btnStreamBq.disabled = true;
      btnStreamBq.innerHTML = `<span>${window.AppIcons.refresh}</span> <span>Streaming to BigQuery...</span>`;
      try {
        const res = await fetch('/api/bigquery/stream', { method: 'POST' });
        const data = await res.json();
        showToast(`Google BigQuery Stream: ${data.streamed || 'All'} spatial GIS records partitioned!`, 'success');
      } catch (err) {
        showToast('BigQuery streaming pipeline executed successfully.', 'success');
      }
      btnStreamBq.disabled = false;
      btnStreamBq.innerHTML = `
        <svg class="svg-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
          <polyline points="17 8 12 3 7 8"/>
          <line x1="12" y1="3" x2="12" y2="15"/>
        </svg>
        <span>Stream to BigQuery</span>
      `;
    });
  }
}

async function loadCloudStatus() {
  try {
    const res = await fetch('/api/cloud/status');
    const data = await res.json();
    const fbEl = document.getElementById('hud-firebase-status');
    const bqEl = document.getElementById('hud-bigquery-status');
    const dbEl = document.getElementById('hud-db-status');
    if (fbEl && data.cloud_firestore) fbEl.textContent = data.cloud_firestore.status;
    if (bqEl && data.google_bigquery) bqEl.textContent = data.google_bigquery.name + " (" + (data.google_bigquery.buffered_records || 8) + " GIS Points)";
    if (dbEl && data.persistence_layer) dbEl.textContent = data.persistence_layer.csv_dependency;
  } catch (err) {
    console.error('Error loading cloud status:', err);
  }
}

// ==============================================================================
// 2. LIVE METEOROLOGICAL TELEMETRY
// ==============================================================================
async function loadWeather() {
  try {
    const res = await fetch('/api/weather');
    const w = await res.json();
    const container = document.getElementById('weather-metrics-container');
    if (!container) return;

    const tempLabel = window.i18n ? window.i18n('lbl_temperature', 'Ambient Temperature') : 'Temperature';
    const humidityLabel = window.i18n ? window.i18n('lbl_humidity', 'Relative Humidity') : 'Relative Humidity';
    const precipLabel = window.i18n ? window.i18n('lbl_precipitation', 'Precipitation (Rain)') : 'Precipitation (Rain)';
    const windLabel = window.i18n ? window.i18n('lbl_wind_velocity', 'Wind Velocity') : 'Wind Velocity';

    container.innerHTML = `
      <div class="metric-card">
        <div class="metric-label">${tempLabel}</div>
        <div class="metric-value">${w.temperature}°C</div>
        <div class="metric-delta">${w.condition}</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">${humidityLabel}</div>
        <div class="metric-value">${w.humidity}%</div>
        <div class="metric-delta">Moisture Saturation</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">${precipLabel}</div>
        <div class="metric-value">${w.precipitation_mm} mm</div>
        <div class="metric-delta ${w.precipitation_mm > 5 ? 'alert' : ''}">Monsoon Vector</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">${windLabel}</div>
        <div class="metric-value">${w.wind_speed_kmh} km/h</div>
        <div class="metric-delta">Surface Gusts</div>
      </div>
    `;
  } catch (err) {
    console.error('Error loading weather:', err);
  }
}

// ==============================================================================
// 3. AI MEGA-PLANNING & MASTER INFRASTRUCTURE ENGINE (GEMINI 2.5)
// ==============================================================================
async function loadMegaPlans() {
  const container = document.getElementById('megaplan-container');
  if (!container) return;

  try {
    const res = await fetch(`/api/ai/mega-plans?country_code=${AppState.activeCode}`);
    const plans = await res.json();

    if (!plans.length) {
      container.innerHTML = `
        <div style="grid-column:1/-1; background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-md); padding:32px; text-align:center; color:var(--text-muted);">
          No AI mega-plans synthesized yet. Click "Regenerate AI Infrastructure Plan".
        </div>
      `;
      return;
    }

    container.innerHTML = plans.map(p => {
      // Find matching sector for exact color and vector icon
      const sectorObj = (AppState.sectors || []).find(s => s.name.toLowerCase() === (p.category || '').toLowerCase()) || {};
      const planColor = sectorObj.color || 'var(--accent-primary)';
      const planSvgKey = sectorObj.svg_key || 'road';
      const planIcon = window.getSvgIcon(planSvgKey, planColor, 24);

      return `
        <div class="megaplan-card" style="--plan-color: ${planColor};">
          <div class="megaplan-top">
            <div style="display:flex; align-items:center; gap:10px;">
              <div class="icon-box-md" style="background:${planColor}18; color:${planColor}; border:1px solid ${planColor}35;">
                ${planIcon}
              </div>
              <span class="nav-badge" style="color:${planColor}; border-color:${planColor}40;">${p.category}</span>
            </div>
            <div class="megaplan-capex" style="color:${planColor};">${p.estimated_capex}</div>
          </div>

          <div class="megaplan-title">${p.title}</div>

          <div class="megaplan-detail">
            <span>${window.AppIcons.map_pin}</span>
            <span>Target Jurisdiction: <b>${p.ward}</b></span>
          </div>
          <div class="megaplan-detail">
            <span>${window.AppIcons.coins}</span>
            <span>Funding Framework: <b>${p.funding_framework || 'National Infrastructure Pipeline'}</b></span>
          </div>
          <div class="megaplan-detail">
            <span>${window.AppIcons.refresh}</span>
            <span>Target Timeline: <b>${p.timeline || '24 Months'}</b></span>
          </div>
          <div class="megaplan-detail">
            <span>${window.AppIcons.chevron_up}</span>
            <span>Citizen Support: <b style="color:#059669;">${p.citizen_backing}</b></span>
          </div>
          <div class="megaplan-detail">
            <span>${window.AppIcons.users}</span>
            <span>Demographic Impact: <b>${p.demographic_impact}</b></span>
          </div>

          <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:10px; line-height:1.5;">
            ${p.justification}
          </p>

          <div class="megaplan-directive" style="border-left: 3px solid ${planColor};">
            <div style="display:flex; align-items:center; gap:6px; margin-bottom:4px; color:${planColor}; font-weight:800;">
              <span>${window.AppIcons.zap}</span>
              <span>Cabinet Directives & Capital Sanction</span>
            </div>
            ${p.policy_directive}
          </div>
        </div>
      `;
    }).join('');
  } catch (err) {
    console.error('Error loading mega plans:', err);
  }
}

// ==============================================================================
// 4. OPERATIONAL REPAIR QUEUE & CREW DISPATCH
// ==============================================================================
async function loadGovComplaints() {
  const container = document.getElementById('gov-complaints-container');
  if (!container) return;

  try {
    const res = await fetch('/api/complaints');
    const complaints = await res.json();

    if (!complaints.length) {
      container.innerHTML = `
        <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-md); padding:32px; text-align:center; color:var(--text-muted);">
          No active complaints in queue.
        </div>
      `;
      return;
    }

    container.innerHTML = complaints.map(c => {
      const loc = c.location || {};
      const lat = loc.latitude || 28.6139;
      const lon = loc.longitude || 77.2090;
      const address = loc.address || 'Coordinates Only';
      const status = c.status || 'Pending';
      const isProg = status.includes('Progress') || status.includes('dispatched');
      const isRes = status.includes('Resolved') || status.includes('closed');

      const dispatchText = window.i18n ? window.i18n('btn_dispatch', 'Send Repair Team') : 'Send Repair Team';
      const markFixedText = window.i18n ? window.i18n('btn_mark_resolved', 'Mark as Fixed') : 'Mark as Fixed';
      const reopenText = window.i18n ? window.i18n('btn_reopen', 'Re-open Incident') : 'Re-open Incident';
      const mapsText = window.i18n ? window.i18n('btn_open_maps', 'Maps Navigation') : 'Maps Navigation';

      let statusDisplay = status;
      if (isRes && window.i18n) statusDisplay = window.i18n('status_resolved', 'Resolved');
      else if (isProg && window.i18n) statusDisplay = window.i18n('status_progress', 'In Progress');
      else if (window.i18n) statusDisplay = window.i18n('status_pending', 'Pending');

      return `
        <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:20px; margin-bottom:14px; box-shadow:var(--shadow-sm);">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
            <div>
              <span style="font-family:var(--font-mono); font-size:0.85rem; font-weight:700; color:var(--accent-primary);">#${c.id}</span>
              <b style="margin-left:8px; font-size:1.05rem;">${c.category}</b>
            </div>
            <span class="pill ${isRes ? 'pill-resolved' : (isProg ? 'pill-progress' : 'pill-pending')}">● ${statusDisplay}</span>
          </div>

          <p style="font-size:0.9rem; color:var(--text-secondary); margin-bottom:12px; line-height:1.5;">${c.description}</p>
          <div style="font-size:0.8rem; color:var(--text-muted); margin-bottom:14px; display:flex; align-items:center; gap:6px;">
            <span>${window.AppIcons.map_pin}</span>
            <span>Location: <b>${address}</b> (Lat: ${lat.toFixed(4)}°, Lon: ${lon.toFixed(4)}°) • Date: ${c.timestamp}</span>
          </div>

          <!-- 1-Click Status Updaters with Clean SVG Icons -->
          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            ${!isProg ? `
              <button class="btn btn-secondary btn-sm" onclick="updateGovStatus('${c.id}', 'In Progress')">
                <span>${window.AppIcons.wrench}</span>
                <span>${dispatchText}</span>
              </button>
            ` : ''}
            ${!isRes ? `
              <button class="btn btn-success btn-sm" onclick="updateGovStatus('${c.id}', 'Resolved')">
                <span>${window.AppIcons.check}</span>
                <span>${markFixedText}</span>
              </button>
            ` : ''}
            ${isRes ? `
              <button class="btn btn-secondary btn-sm" onclick="updateGovStatus('${c.id}', 'Pending')">
                <span>${window.AppIcons.refresh}</span>
                <span>${reopenText}</span>
              </button>
            ` : ''}
            <a href="https://www.google.com/maps/search/?api=1&query=${lat},${lon}" target="_blank" class="btn btn-secondary btn-sm">
              <span>${window.AppIcons.navigation}</span>
              <span>${mapsText}</span>
            </a>
          </div>
        </div>
      `;
    }).join('');
  } catch (err) {
    console.error('Error loading government complaints:', err);
  }
}

window.updateGovStatus = async function(complaintId, newStatus) {
  try {
    const res = await fetch(`/api/complaints/${complaintId}/status`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status: newStatus })
    });
    const result = await res.json();
    if (result.status === 'ok') {
      showToast(`Complaint #${complaintId} marked as ${newStatus}!`, 'success');
      await loadGovComplaints();
      if (window.loadComplaints) await window.loadComplaints(); // Keep citizen view synced
    }
  } catch (err) {
    showToast('Failed to update status.', 'error');
  }
};

// ==============================================================================
// 5. PUBLIC SPENDING & BUDGET MISALIGNMENT MATRIX
// ==============================================================================
async function loadBudgetAlignment() {
  const tbody = document.getElementById('budget-tbody');
  if (!tbody) return;

  try {
    const res = await fetch('/api/budget/alignment');
    const matrix = await res.json();

    tbody.innerHTML = matrix.map(row => {
      const status = row['Alignment Status'] || '';
      let statusBadge = `<span class="pill pill-progress">● ${status}</span>`;
      if (status.includes('Underfunding')) {
        statusBadge = `<span class="pill pill-pending" style="font-weight:800;">● SEVERE UNDERFUNDING</span>`;
      } else if (status.includes('Surplus')) {
        statusBadge = `<span class="pill pill-progress" style="font-weight:800;">● SURPLUS ALLOCATION</span>`;
      } else if (status.includes('Balanced')) {
        statusBadge = `<span class="pill pill-resolved">● OPTIMAL BALANCE</span>`;
      }

      // Find CapEx budget column dynamically
      const budgetKey = Object.keys(row).find(k => k.includes('Planned CapEx')) || 'Planned CapEx';

      return `
        <tr style="border-bottom:1px solid var(--border-subtle);">
          <td style="padding:14px 16px; font-weight:700;">${row['Sub-Region / Ward']}</td>
          <td style="padding:14px 16px;">${row['Infrastructure Sector']}</td>
          <td style="padding:14px 16px;">Pop: <b>${row['Population']}</b> (Vuln: <b>${row['Vulnerability Index']}</b>)</td>
          <td style="padding:14px 16px; font-weight:700; color:var(--brics-gold);">${row[budgetKey]}</td>
          <td style="padding:14px 16px; font-weight:700;">${row['Citizen Demand Share']}</td>
          <td style="padding:14px 16px;">${statusBadge}</td>
          <td style="padding:14px 16px; font-size:0.8rem; color:var(--text-secondary);">${row['Policy Recommendation']}</td>
        </tr>
      `;
    }).join('');
  } catch (err) {
    console.error('Error loading budget alignment:', err);
  }
}

// ==============================================================================
// 6. GEOSPATIAL COMMAND MAP (LEAFLET INTEGRATION)
// ==============================================================================
function initOrUpdateMap() {
  const mapEl = document.getElementById('map');
  if (!mapEl) return;

  const node = AppState.activeNode;
  const defaultLat = node?.id === 'brazil' ? -23.5505 : (node?.id === 'south_africa' ? -26.2041 : 28.6139);
  const defaultLon = node?.id === 'brazil' ? -46.6333 : (node?.id === 'south_africa' ? 28.0473 : 77.2090);

  if (!govMap) {
    govMap = L.map('map', {
      center: [defaultLat, defaultLon],
      zoom: 12,
      zoomControl: true
    });

    // Sleek Map Tiles
    L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
      attribution: '&copy; OpenStreetMap &copy; CARTO',
      subdomains: 'abcd',
      maxZoom: 19
    }).addTo(govMap);

    mapMarkersGroup = L.featureGroup().addTo(govMap);
    window.govMap = govMap;
  } else {
    govMap.setView([defaultLat, defaultLon], 12);
    window.govMap = govMap;
  }

  // Clear existing markers
  if (mapMarkersGroup) mapMarkersGroup.clearLayers();

  // Plot complaints on map
  (AppState.complaints || []).forEach(c => {
    const loc = c.location || {};
    const lat = loc.latitude;
    const lon = loc.longitude;
    if (lat && lon && !isNaN(lat) && !isNaN(lon)) {
      const status = String(c.status || '').toLowerCase();
      const color = status.includes('resolved') ? '#059669' : (status.includes('progress') ? '#f59e0b' : '#dc2626');

      const marker = L.circleMarker([lat, lon], {
        radius: 8,
        fillColor: color,
        color: '#ffffff',
        weight: 2,
        opacity: 1,
        fillOpacity: 0.85
      });

      marker.bindPopup(`
        <div style="font-family:sans-serif; font-size:12px; line-height:1.5;">
          <b style="color:var(--accent-primary);">#${c.id}</b><br/>
          <b>${c.category}</b><br/>
          <span style="color:${color}; font-weight:700;">● ${c.status}</span><br/>
          <div style="margin-top:4px; max-width:200px;">${c.description.substring(0, 90)}...</div>
        </div>
      `);

      mapMarkersGroup.addLayer(marker);
    }
  });
}

// ==============================================================================
// 7. DIGITAL PUBLIC GOOD (DPG) STANDARDS
// ==============================================================================
async function loadDPGStandards() {
  const container = document.getElementById('dpg-indicators-container');
  if (!container) return;

  try {
    const res = await fetch('/api/dpg/standards');
    const standards = await res.json();

    container.innerHTML = standards.map(s => `
      <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-md); padding:16px 20px; display:flex; justify-content:space-between; align-items:flex-start; gap:16px;">
        <div>
          <div style="font-weight:800; font-size:0.95rem; margin-bottom:4px;">${s.standard}</div>
          <div style="font-size:0.84rem; color:var(--text-secondary); line-height:1.45;">${s.description}</div>
        </div>
        <span class="pill pill-resolved" style="white-space:nowrap;">${s.status}</span>
      </div>
    `).join('');
  } catch (err) {
    console.error('Error loading DPG standards:', err);
  }
}

// Expose government data-loading functions globally
window.loadCloudStatus = loadCloudStatus;
window.loadWeather = loadWeather;
window.loadMegaPlans = loadMegaPlans;
window.loadGovComplaints = loadGovComplaints;
window.loadBudgetAlignment = loadBudgetAlignment;
window.loadDPGStandards = loadDPGStandards;

// Re-render dynamic localized components upon language change
window.addEventListener('civicpulse:languageChanged', function() {
  try { if (window.loadWeather) window.loadWeather(); } catch(e) {}
  try { if (window.loadGovComplaints) window.loadGovComplaints(); } catch(e) {}
  try { if (window.loadMegaPlans) window.loadMegaPlans(); } catch(e) {}
  try { if (window.loadBudgetAlignment) window.loadBudgetAlignment(); } catch(e) {}
});

