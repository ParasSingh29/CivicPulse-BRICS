/**
 * CIVICPULSE-BRICS: CITY OFFICIAL COMMAND PORTAL CONTROLLER
 * Manages City-Scoped Complaints, Local Area AI Synthesis,
 * Proposal Escalation to Centre, and Inter-City Peer Upvoting
 */

let activeCity = 'Delhi';
let cityOfficerInfo = {
  id: 'OFF-DEL-01',
  name: 'Er. Vikram Sharma',
  role: 'Chief Executive Engineer • Delhi PWD',
  city: 'Delhi',
  country_code: 'IN',
  flag: '🇮🇳'
};

const CITY_OFFICER_MAP = {
  'Delhi': { id: 'OFF-DEL-01', name: 'Er. Vikram Sharma', role: 'Chief Executive Engineer • Delhi PWD', flag: '🇮🇳', node: 'IN' },
  'Mumbai': { id: 'OFF-MUM-02', name: 'Er. Rajesh Kulkarni', role: 'Superintending Transit Engineer • Mumbai MMRDA', flag: '🇮🇳', node: 'IN' },
  'Bengaluru': { id: 'OFF-BLR-03', name: 'Dr. Sunita Rao', role: 'Executive Director • Greater Bengaluru BBMP', flag: '🇮🇳', node: 'IN' },
  'São Paulo': { id: 'OFF-SP-04', name: 'Eng. Carlos Mendes', role: 'Diretor Geral de Obras • SP RMSP', flag: '🇧🇷', node: 'BR' },
  'Johannesburg': { id: 'OFF-JHB-05', name: 'Dir. Sipho Nkosi', role: 'Executive Infrastructure Director • JRA & City Power', flag: '🇿🇦', node: 'ZA' }
};

window.initCityOfficialPortal = async function() {
  const savedCity = localStorage.getItem('civicpulse_city') || 'Delhi';
  setCity(savedCity);

  setupCityOfficialEvents();
  await refreshCityOfficialDashboard();
};

if (document.readyState === 'interactive' || document.readyState === 'complete') {
  window.initCityOfficialPortal();
} else {
  document.addEventListener('DOMContentLoaded', window.initCityOfficialPortal);
}


function setCity(city) {
  activeCity = city;
  localStorage.setItem('civicpulse_city', city);
  const officer = CITY_OFFICER_MAP[city] || CITY_OFFICER_MAP['Delhi'];
  cityOfficerInfo = { ...officer, city: city };

  // Update DOM City Indicators
  const citySelector = document.getElementById('city-selector');
  if (citySelector && citySelector.value !== city) citySelector.value = city;

  const flagContainer = document.getElementById('active-flag-container');
  if (flagContainer) flagContainer.textContent = officer.flag;

  const navTitle = document.getElementById('city-nav-title');
  if (navTitle) navTitle.textContent = `${city} Municipal Command`;

  const heroCityName = document.getElementById('hero-city-name');
  if (heroCityName) heroCityName.textContent = city;

  const complaintsLabel = document.getElementById('complaints-city-label');
  if (complaintsLabel) complaintsLabel.textContent = city;

  const rygCityName = document.getElementById('ryg-city-name');
  if (rygCityName) rygCityName.textContent = city;

  document.querySelectorAll('.current-city-text').forEach(el => el.textContent = city);

  // Update Officer UI
  const officerNameEl = document.getElementById('officer-display-name');
  if (officerNameEl) officerNameEl.textContent = officer.name;

  const officerRoleEl = document.getElementById('officer-display-role');
  if (officerRoleEl) officerRoleEl.textContent = officer.role;

  const avatarBox = document.querySelector('.user-profile-avatar');
  if (avatarBox) {
    const initials = officer.name.split(' ').map(w => w[0]).filter(Boolean).slice(-2).join('');
    avatarBox.textContent = initials;
  }

  // Update Proposal Modal Inputs
  const modalCityInput = document.getElementById('prop-input-city');
  if (modalCityInput) modalCityInput.value = city;

  const modalOfficerInput = document.getElementById('prop-input-officer');
  if (modalOfficerInput) modalOfficerInput.value = officer.name;

  // Set country theme attribute
  document.documentElement.setAttribute('data-node', officer.node || 'IN');
}

// ==============================================================================
// 1. EVENT LISTENERS
// ==============================================================================
function setupCityOfficialEvents() {
  // City is fixed to the officer's assigned jurisdiction — no switcher event needed.

  // Sector and Status filters for complaints
  const sectorFilter = document.getElementById('complaints-sector-filter');
  const statusFilter = document.getElementById('complaints-status-filter');
  if (sectorFilter) sectorFilter.addEventListener('change', loadCityComplaints);
  if (statusFilter) statusFilter.addEventListener('change', loadCityComplaints);

  // Proposals City Filter
  const propCityFilter = document.getElementById('proposals-city-filter');
  if (propCityFilter) propCityFilter.addEventListener('change', loadCityProposalsFeed);

  // Refresh City AI suggestions
  const btnRefreshAi = document.getElementById('btn-refresh-city-ai');
  if (btnRefreshAi) {
    btnRefreshAi.addEventListener('click', async () => {
      btnRefreshAi.disabled = true;
      btnRefreshAi.innerHTML = `<span>Synthesizing ${activeCity} Infrastructure...</span>`;
      await loadCityAiSuggestions();
      btnRefreshAi.disabled = false;
      btnRefreshAi.innerHTML = `
        <svg class="svg-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg>
        <span>Regenerate AI Analysis</span>
      `;
      showToast(`AI Area Recommendations refreshed for ${activeCity}!`, 'success');
    });
  }

  // Modal Open / Close
  const btnOpenModal = document.getElementById('btn-open-file-proposal-modal');
  const btnTriggerModal = document.getElementById('btn-trigger-file-proposal');
  const btnTriggerHome = document.getElementById('btn-trigger-file-proposal-home');
  const btnCloseModal = document.getElementById('btn-close-proposal-modal');
  const btnCancelModal = document.getElementById('btn-cancel-proposal');
  const modalEl = document.getElementById('file-proposal-modal');

  const openModal = () => { if (modalEl) modalEl.style.display = 'flex'; };
  const closeModal = () => { if (modalEl) modalEl.style.display = 'none'; };

  if (btnOpenModal) btnOpenModal.addEventListener('click', openModal);
  if (btnTriggerModal) btnTriggerModal.addEventListener('click', openModal);
  if (btnTriggerHome) btnTriggerHome.addEventListener('click', openModal);
  if (btnCloseModal) btnCloseModal.addEventListener('click', closeModal);
  if (btnCancelModal) btnCancelModal.addEventListener('click', closeModal);

  // Close modal on Escape key press
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
  });

  // Proposal Form Submission
  const formProposal = document.getElementById('form-file-proposal');
  if (formProposal) {
    formProposal.addEventListener('submit', async (e) => {
      e.preventDefault();
      await handleProposalSubmit();
    });
  }
}

async function refreshCityOfficialDashboard() {
  await Promise.all([
    loadCityComplaints(),
    loadCityAiSuggestions(),
    loadCityProposalsFeed()
  ]);

  if (window.GlobalProblemMapSystem) {
    window.GlobalProblemMapSystem.init({
      mapId: 'city-geospatial-map',
      tableBodyId: 'city-map-table-body',
      countrySelectId: 'city-map-country-filter',
      citySelectId: 'city-map-city-filter',
      statusSelectId: 'city-map-status-filter',
      searchInputId: 'city-map-search-input',
      mapModeSelectId: 'city-map-mode-select',
      counterBadgeId: 'city-map-counter-badge',
      countryTableBodyId: 'city-country-telemetry-body'
    });
  }
}

function getCleanCityDescription(desc) {
  if (!desc) return '';
  let cleaned = String(desc);
  cleaned = cleaned.replace(/\[Priority\]:\s*[^.\n\r]+(\([^\)]*\))?/gi, '');
  cleaned = cleaned.replace(/Priority:\s*(High|Medium|Low|Critical|Urgent)/gi, '');
  cleaned = cleaned.replace(/\[Location\]:\s*[^.\n\r]+/gi, '');
  cleaned = cleaned.replace(/near Ward \d+ - [^,.]+(,\s*[^,.]+)?\.?/gi, '');
  cleaned = cleaned.replace(/Testing E2E reporting for sector \[[^\]]+\]:\s*/gi, '');
  cleaned = cleaned.replace(/for sector \[[^\]]+\]:\s*/gi, '');
  cleaned = cleaned.replace(/\[Status\]:\s*[^.\n\r]+/gi, '');
  cleaned = cleaned.split('\n').map(l => l.trim()).filter(Boolean).join('\n\n');
  return cleaned || desc;
}

// ==============================================================================
// 2. CITY COMPLAINTS & REPAIR OPERATIONS (SCOPED STRICTLY TO CITY)
// ==============================================================================
window.loadCityComplaints = async function loadCityComplaints() {
  const container = document.getElementById('city-complaints-container');
  if (!container) return;

  try {
    const res = await fetch(`/api/complaints?city=${encodeURIComponent(activeCity)}`);
    if (!res.ok) {
      throw new Error(`HTTP ${res.status} ${res.statusText}`);
    }
    const allCityComplaints = await res.json();
    window.cachedCityComplaints = allCityComplaints;

    // Update KPIs and RYG Multi-Segment Bar
    try { updateMunicipalHealthHUD(allCityComplaints); } catch(e) { console.warn('HUD error:', e); }

    // Apply Client Filter
    const sectorFilter = document.getElementById('complaints-sector-filter')?.value || 'All Sectors';
    const statusFilter = document.getElementById('complaints-status-filter')?.value || 'All';

    let filtered = allCityComplaints;
    if (sectorFilter !== 'All Sectors') {
      filtered = filtered.filter(c => c.category === sectorFilter);
    }
    if (statusFilter !== 'All') {
      filtered = filtered.filter(c => {
        const s = (c.status || '').toLowerCase();
        if (statusFilter === 'Pending') return !s.includes('progress') && !s.includes('resolved') && !s.includes('closed');
        if (statusFilter === 'In Progress') return s.includes('progress') || s.includes('dispatch');
        if (statusFilter === 'Resolved') return s.includes('resolved') || s.includes('closed');
        return true;
      });
    }

    if (!filtered.length) {
      container.innerHTML = `
        <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:32px; text-align:center; color:var(--text-muted);">
          No complaints matching the selected filters for ${activeCity}.
        </div>
      `;
      return;
    }

    const mapPinIcon = (window.AppIcons && window.AppIcons.map_pin) || '📍';
    const wrenchIcon = (window.AppIcons && window.AppIcons.wrench) || '🔧';
    const checkIcon = (window.AppIcons && window.AppIcons.check) || '✓';
    const refreshIcon = (window.AppIcons && window.AppIcons.refresh) || '🔄';
    const navIcon = (window.AppIcons && window.AppIcons.navigation) || '🗺️';

    container.innerHTML = filtered.map(c => {
      const loc = c.location || {};
      const lat = loc.latitude || 28.6139;
      const lon = loc.longitude || 77.2090;
      const address = loc.address || `${activeCity} Municipality Area`;
      const status = c.status || 'Pending';

      const isProg = status.includes('Progress') || status.includes('dispatched');
      const isRes = status.includes('Resolved') || status.includes('closed');

      let statusBadge = `<span class="pill pill-pending">${window.getTranslation('status_red_pending_action', '● Red: Pending Action')}</span>`;
      if (isRes) statusBadge = `<span class="pill pill-resolved">${window.getTranslation('status_green_resolved', '● Green: Resolved')}</span>`;
      else if (isProg) statusBadge = `<span class="pill pill-progress">${window.getTranslation('status_yellow_crew_dispatched', '● Yellow: Crew Dispatched')}</span>`;

      const prioMatch = (c.description || '').match(/\[Priority\]:\s*([^.\n\r]+)/i);
      let prioVal = prioMatch ? prioMatch[1].trim().split('-')[0].trim() : 'Medium';
      if (!prioVal) prioVal = 'Medium';
      let prioColor = '#f59e0b';
      let prioBg = 'rgba(245,158,11,0.14)';
      let prioBorder = 'rgba(245,158,11,0.35)';
      if (/high|critical|urgent/i.test(prioVal) || /critical/i.test(c.description)) {
        prioColor = '#ef4444'; prioBg = 'rgba(239,68,68,0.14)'; prioBorder = 'rgba(239,68,68,0.35)';
        if (!prioMatch) prioVal = 'High';
      } else if (/low/i.test(prioVal)) {
        prioColor = '#10b981'; prioBg = 'rgba(16,185,129,0.14)'; prioBorder = 'rgba(16,185,129,0.35)';
      }

      const descFn = (typeof formatDescriptionHTML === 'function') ? formatDescriptionHTML : (window.formatDescriptionHTML || (d => d));
      const descHTML = descFn(c.description);

      return `
        <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:16px 20px; margin-bottom:12px; box-shadow:var(--shadow-sm);">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:10px; padding-bottom:10px; border-bottom:1px solid rgba(255,255,255,0.06);">
            <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
              <span style="font-family:var(--font-mono); font-size:0.85rem; font-weight:700; color:var(--accent-primary); background:rgba(245,158,11,0.1); padding:3px 8px; border-radius:4px; border:1px solid rgba(245,158,11,0.25);">#${c.id}</span>
              <b style="font-size:1.05rem; color:var(--text-primary);">${c.category}</b>
            </div>
            <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
              ${statusBadge}
              <span class="pill" style="color:${prioColor}; background:${prioBg}; border:1px solid ${prioBorder}; font-weight:600;">⚡ ${window.getTranslation('label_priority', 'Priority')}: ${(window.getTranslation('prio_' + (prioVal || 'medium').toLowerCase())) || (window.getTranslation(prioVal)) || prioVal}</span>
            </div>
          </div>

          <div style="font-size:0.82rem; color:var(--text-muted); margin-bottom:12px; display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
            <span>${mapPinIcon}</span>
            <span>${window.getTranslation('label_location', 'Location')}: <b>${address}</b> • ${window.getTranslation('lbl_date', 'Date')}: ${c.timestamp}</span>
            <span style="background:rgba(59,130,246,0.12); color:#60a5fa; border:1px solid rgba(59,130,246,0.3); padding:2px 8px; border-radius:12px; font-weight:600; margin-left:4px;">👤 ${window.getTranslation('lbl_reported_by', 'Reported by')}: ${c.reported_by || c.user_id || 'Citizen'}</span>
          </div>

          ${(c.photo_url || c.resolution_photo) ? `
            <div style="display:flex; gap:12px; margin-bottom:12px; flex-wrap:wrap; align-items:center;">
              ${c.photo_url ? `
                <div style="position:relative; width:130px; height:85px; border-radius:8px; overflow:hidden; border:1px solid var(--border-color); background:rgba(0,0,0,0.3); cursor:pointer;" onclick="openImageLightbox('${c.photo_url}', 'Reported Issue (#${c.id})')">
                  <img src="${c.photo_url}" alt="Reported Problem" style="width:100%; height:100%; object-fit:cover;">
                  <span style="position:absolute; bottom:0; left:0; right:0; background:rgba(0,0,0,0.7); font-size:0.65rem; color:#fff; text-align:center; padding:2px;">📸 Issue Photo</span>
                </div>
              ` : ''}
              ${c.resolution_photo ? `
                <div style="position:relative; width:130px; height:85px; border-radius:8px; overflow:hidden; border:1px solid #10b981; background:rgba(0,0,0,0.3); cursor:pointer;" onclick="openImageLightbox('${c.resolution_photo}', 'Completed Work Proof (#${c.id})')">
                  <img src="${c.resolution_photo}" alt="Completed Work Proof" style="width:100%; height:100%; object-fit:cover;">
                  <span style="position:absolute; bottom:0; left:0; right:0; background:rgba(16,185,129,0.9); font-size:0.65rem; color:#fff; text-align:center; padding:2px; font-weight:700;">✅ Fixed Work Proof</span>
                </div>
              ` : ''}
            </div>
          ` : ''}

          <!-- 1-Click Status Toggles -->
          <div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center;">
            <button id="btn-city-desc-${c.id}" class="btn btn-secondary btn-sm" onclick="toggleReportDescription('city-desc-${c.id}')" style="background:rgba(255,255,255,0.06); border:1px solid var(--border-color); font-weight:600;">
              <span>📄 ${window.getTranslation('btn_read_description', 'Read Description')}</span>
              <span style="margin-left:4px; font-size:0.75rem;">▼</span>
            </button>
            ${!isProg ? `
              <button class="btn btn-secondary btn-sm" onclick="changeCityComplaintStatus('${c.id}', 'In Progress')">
                <span>${wrenchIcon}</span>
                <span>${window.getTranslation('btn_send_repair_team', 'Send Repair Team')}</span>
              </button>
            ` : ''}
            ${!isRes ? `
              <button class="btn btn-success btn-sm" onclick="openMarkFixedModal('${c.id}')" style="background:#059669; border-color:#059669;">
                <span>${checkIcon}</span>
                <span>${window.getTranslation('btn_mark_fixed', 'Mark as Fixed')}</span>
              </button>
            ` : ''}
            ${isRes ? `
              <button class="btn btn-secondary btn-sm" onclick="changeCityComplaintStatus('${c.id}', 'Pending')">
                <span>${refreshIcon}</span>
                <span>${window.getTranslation('btn_reopen_incident', 'Re-open Incident')}</span>
              </button>
            ` : ''}
            <a href="https://www.google.com/maps/search/?api=1&query=${lat},${lon}" target="_blank" class="btn btn-secondary btn-sm">
              <span>${navIcon}</span>
              <span>${window.getTranslation('btn_open_maps', 'Open Maps')}</span>
            </a>
          </div>

          <div id="city-desc-${c.id}" style="display:none; margin-top:12px; padding:14px 16px; background:rgba(0,0,0,0.25); border-radius:8px; border:1px solid rgba(255,255,255,0.08); font-size:0.9rem; color:var(--text-secondary); line-height:1.55;">
            ${descHTML}
          </div>
        </div>
      `;
    }).join('');
  } catch (err) {
    console.error('Error loading city complaints:', err);
    if (container) {
      container.innerHTML = `
        <div style="background:rgba(239,68,68,0.1); border:1px solid rgba(239,68,68,0.3); border-radius:var(--radius-lg); padding:24px; text-align:center; color:#ef4444;">
          <div style="font-weight:700; margin-bottom:8px;">⚠️ Error loading city complaints</div>
          <div style="font-size:0.85rem; color:var(--text-muted); margin-bottom:12px;">${err.message || String(err)}</div>
          <button class="btn btn-secondary btn-sm" onclick="window.loadCityComplaints && window.loadCityComplaints()">🔄 Retry Loading</button>
        </div>
      `;
    }
  }
};


function updateMunicipalHealthHUD(complaints) {
  let red = 0, yellow = 0, green = 0;
  complaints.forEach(c => {
    const s = (c.status || '').toLowerCase();
    if (s.includes('resolved') || s.includes('closed') || s.includes('fixed')) green++;
    else if (s.includes('progress') || s.includes('dispatch')) yellow++;
    else red++;
  });

  const total = complaints.length;
  const health = total > 0 ? Math.round(((green * 1.0) + (yellow * 0.5)) / total * 100) : 95;

  const kpiTotal = document.getElementById('kpi-total-problems');
  const kpiRed = document.getElementById('kpi-red-problems');
  const kpiYellow = document.getElementById('kpi-yellow-problems');
  const kpiGreen = document.getElementById('kpi-green-problems');
  const kpiScope = document.getElementById('kpi-city-scope');

  if (kpiTotal) kpiTotal.textContent = total;
  if (kpiRed) kpiRed.textContent = red;
  if (kpiYellow) kpiYellow.textContent = yellow;
  if (kpiGreen) kpiGreen.textContent = green;
  if (kpiScope) kpiScope.textContent = `Scoped strictly to ${activeCity}`;

  // Multi-Segment Bar
  const barRed = document.getElementById('ryg-bar-red');
  const barYellow = document.getElementById('ryg-bar-yellow');
  const barGreen = document.getElementById('ryg-bar-green');
  const badgeRed = document.getElementById('count-red-badge');
  const badgeYellow = document.getElementById('count-yellow-badge');
  const badgeGreen = document.getElementById('count-green-badge');
  const badgeHealth = document.getElementById('health-index-badge');

  if (badgeRed) badgeRed.textContent = red;
  if (badgeYellow) badgeYellow.textContent = yellow;
  if (badgeGreen) badgeGreen.textContent = green;
  if (badgeHealth) badgeHealth.textContent = `Health Index: ${health}%`;

  if (total > 0) {
    if (barRed) barRed.style.width = `${(red / total) * 100}%`;
    if (barYellow) barYellow.style.width = `${(yellow / total) * 100}%`;
    if (barGreen) barGreen.style.width = `${(green / total) * 100}%`;
  } else {
    if (barRed) barRed.style.width = '0%';
    if (barYellow) barYellow.style.width = '0%';
    if (barGreen) barGreen.style.width = '100%';
  }
}

window.openMarkFixedModal = function(id) {
  const modal = document.getElementById('modal-mark-fixed');
  if (!modal) return;

  const complaint = (window.cachedCityComplaints || []).find(c => String(c.id) === String(id));
  document.getElementById('fixed-complaint-id').value = id;

  const infoEl = document.getElementById('modal-fixed-complaint-info');
  if (infoEl) {
    const loc = complaint?.location || {};
    const addr = loc.address || loc.city || 'Municipal Sector';
    infoEl.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <span style="font-family:var(--font-mono); font-weight:700; color:var(--accent-primary);">#${id}</span>
        <span class="badge" style="background:rgba(245,158,11,0.15); color:#f59e0b; padding:2px 8px; border-radius:4px; font-weight:600;">${complaint?.category || 'General Municipal'}</span>
      </div>
      <div style="color:var(--text-muted); font-size:0.8rem; margin-top:4px;">
        📍 Location: <b>${addr}</b>
      </div>
    `;
  }

  // Reset form inputs & preview
  const fileInput = document.getElementById('fixed-photo-input');
  if (fileInput) fileInput.value = '';
  const previewWrap = document.getElementById('fixed-photo-preview-wrap');
  if (previewWrap) previewWrap.style.display = 'none';
  const promptWrap = document.getElementById('fixed-photo-prompt');
  if (promptWrap) promptWrap.style.display = 'block';
  const errorEl = document.getElementById('fixed-photo-error');
  if (errorEl) errorEl.style.display = 'none';
  const notesEl = document.getElementById('fixed-notes');
  if (notesEl) notesEl.value = '';

  modal.style.display = 'flex';
};

window.closeMarkFixedModal = function() {
  const modal = document.getElementById('modal-mark-fixed');
  if (modal) modal.style.display = 'none';
};

window.previewFixedPhoto = function(e) {
  const file = e.target.files && e.target.files[0];
  if (!file) return;

  const errorEl = document.getElementById('fixed-photo-error');
  if (errorEl) errorEl.style.display = 'none';

  const reader = new FileReader();
  reader.onload = function(evt) {
    const previewImg = document.getElementById('fixed-photo-preview');
    const previewWrap = document.getElementById('fixed-photo-preview-wrap');
    const promptWrap = document.getElementById('fixed-photo-prompt');
    if (previewImg) previewImg.src = evt.target.result;
    if (previewWrap) previewWrap.style.display = 'block';
    if (promptWrap) promptWrap.style.display = 'none';
  };
  reader.readAsDataURL(file);
};

window.handleFixedSubmit = async function(e) {
  e.preventDefault();
  const id = document.getElementById('fixed-complaint-id').value;
  const fileInput = document.getElementById('fixed-photo-input');
  const file = fileInput && fileInput.files && fileInput.files[0];
  const notes = (document.getElementById('fixed-notes')?.value || '').trim();

  if (!file) {
    const errorEl = document.getElementById('fixed-photo-error');
    if (errorEl) errorEl.style.display = 'block';
    showToast('A photo of completed work is strictly required!', 'error');
    return;
  }

  const btnSubmit = document.getElementById('btn-confirm-fixed');
  if (btnSubmit) {
    btnSubmit.disabled = true;
    btnSubmit.innerHTML = `<span>⏳ Uploading Proof...</span>`;
  }

  try {
    const dept = cityOfficerInfo ? cityOfficerInfo.role : 'Municipal Public Works Dept';
    const eng = cityOfficerInfo ? cityOfficerInfo.name : 'Er. Vikram Sharma';

    const formData = new FormData();
    formData.append('status', 'Resolved');
    formData.append('department', dept);
    formData.append('engineer', eng);
    formData.append('resolution_notes', notes);
    formData.append('resolution_photo', file);

    const res = await fetch(`/api/complaints/${id}/status`, {
      method: 'POST',
      body: formData
    });
    const data = await res.json();
    if (data.status === 'ok') {
      showToast(`Problem #${id} marked as Fixed with verified photo proof! 📱 Citizen SMS dispatched.`, 'success');
      closeMarkFixedModal();
      await loadCityComplaints();
    } else {
      showToast('Error updating status: ' + (data.error || 'Server error'), 'error');
    }
  } catch (err) {
    console.error('Error submitting fixed proof:', err);
    showToast('Failed to upload proof: ' + err.message, 'error');
  } finally {
    if (btnSubmit) {
      btnSubmit.disabled = false;
      btnSubmit.innerHTML = `<span>✓ Mark as Fixed with Proof</span>`;
    }
  }
};

window.openImageLightbox = function(src, title = 'Photo Evidence') {
  const modal = document.getElementById('image-lightbox-modal');
  const img = document.getElementById('lightbox-image');
  const titleEl = document.getElementById('lightbox-title');
  if (!modal || !img) return;

  img.src = src;
  if (titleEl) titleEl.textContent = title;
  modal.style.display = 'flex';
};

window.closeImageLightbox = function() {
  const modal = document.getElementById('image-lightbox-modal');
  if (modal) modal.style.display = 'none';
};

window.changeCityComplaintStatus = async function(id, newStatus) {
  if (newStatus === 'Resolved') {
    openMarkFixedModal(id);
    return;
  }
  try {
    const dept = cityOfficerInfo ? cityOfficerInfo.role : 'Municipal Public Works Dept';
    const eng = cityOfficerInfo ? cityOfficerInfo.name : 'Er. Vikram Sharma';
    const res = await fetch(`/api/complaints/${id}/status`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status: newStatus, department: dept, engineer: eng })
    });
    const data = await res.json();
    if (data.status === 'ok') {
      const milestoneLabel = newStatus.includes('Resolved') ? 'SOLVED' : (newStatus.includes('Progress') ? 'TEAM ASSIGNED' : 'REGISTERED');
      showToast(`Problem #${id} marked as ${newStatus}! 📱 Citizen SMS Alert (${milestoneLabel}) Dispatched.`, 'success');
      await loadCityComplaints();
    }
  } catch (err) {
    showToast('Failed to update status', 'error');
  }
};

// ==============================================================================
// 3. LOCAL AREA AI STRATEGIC SUGGESTIONS (GEMINI 2.5)
// ==============================================================================
window.loadCityAiSuggestions = async function loadCityAiSuggestions() {
  const grid = document.getElementById('city-ai-suggestions-grid');
  if (!grid) return;

  try {
    grid.innerHTML = `
      <div style="grid-column:1/-1; text-align:center; padding:30px; color:var(--text-muted);">
        Analyzing ${activeCity} complaint patterns with Gemini AI...
      </div>
    `;

    const res = await fetch(`/api/ai/city-plan?city=${encodeURIComponent(activeCity)}`);
    const plans = await res.json();

    if (!plans.length) {
      grid.innerHTML = `<div style="grid-column:1/-1; text-align:center; color:var(--text-muted);">No AI proposals generated yet.</div>`;
      return;
    }

    grid.innerHTML = plans.map((p, idx) => {
      const isTraffic = (p.category || '').toLowerCase().includes('road') || (p.category || '').toLowerCase().includes('transport');
      const tagBg = isTraffic ? 'rgba(245,158,11,0.15)' : 'rgba(59,130,246,0.15)';
      const tagColor = isTraffic ? '#f59e0b' : '#60a5fa';

      return `
        <div style="background:var(--bg-card); border:1px solid rgba(59,130,246,0.3); border-radius:var(--radius-lg); padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:var(--shadow-sm);">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
              <span class="nav-badge" style="background:${tagBg}; color:${tagColor}; border:1px solid ${tagColor}40;">${p.category}</span>
              <span style="font-weight:800; color:var(--brics-gold); font-size:1.05rem;">${p.estimated_capex}</span>
            </div>

            <h3 style="font-size:1.15rem; font-weight:800; margin-bottom:10px; color:var(--text-primary); line-height:1.35;">${p.title}</h3>

            <p style="font-size:0.86rem; color:var(--text-secondary); line-height:1.55; margin-bottom:14px;">
              ${p.justification}
            </p>

            <div style="background:rgba(255,255,255,0.03); border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:12px; margin-bottom:16px; font-size:0.8rem; line-height:1.5;">
              <div>⏱️ <b>${window.getTranslation('label_timeline', 'Timeline')}:</b> ${p.timeline || '24 Months'}</div>
              <div>👥 <b>${window.getTranslation('label_impact', 'Impact')}:</b> ${p.demographic_impact}</div>
              <div style="margin-top:6px; color:#60a5fa;">💡 <b>${window.getTranslation('label_ai_directive', 'AI Directive')}:</b> ${p.policy_recommendation || 'Escalate to Central Command.'}</div>
            </div>
          </div>

          <button class="btn btn-primary" style="background:#059669; border-color:#059669; width:100%;" onclick="prefillAndOpenProposalModal(${idx})">
            <span>${window.getTranslation('btn_file_this_proposal', 'File This Proposal to Centre')}</span>
            <svg class="svg-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
          </button>
        </div>
      `;
    }).join('');

    // Store plans in window for pre-filling modal
    window.currentCityAiPlans = plans;
  } catch (err) {
    console.error('Error loading AI city plans:', err);
  }
}

window.prefillAndOpenProposalModal = function(idx) {
  const p = (window.currentCityAiPlans || [])[idx];
  if (!p) return;

  const titleInput = document.getElementById('prop-input-title');
  const catInput = document.getElementById('prop-input-category');
  const capexInput = document.getElementById('prop-input-capex');
  const timelineInput = document.getElementById('prop-input-timeline');
  const impactInput = document.getElementById('prop-input-impact');
  const justInput = document.getElementById('prop-input-justification');

  if (titleInput) titleInput.value = p.title || '';
  if (catInput) catInput.value = p.category || 'Roads, Bridges & Arterial Corridors';
  if (capexInput) capexInput.value = p.estimated_capex || '';
  if (timelineInput) timelineInput.value = p.timeline || '24 Months';
  if (impactInput) impactInput.value = p.demographic_impact || '';
  if (justInput) justInput.value = p.justification || '';

  const modalEl = document.getElementById('file-proposal-modal');
  if (modalEl) modalEl.style.display = 'flex';
};

// ==============================================================================
// 4. INTER-CITY PROPOSALS & PEER UPVOTING REGISTRY
// ==============================================================================
window.loadCityProposalsFeed = async function loadCityProposalsFeed() {
  const feed = document.getElementById('city-proposals-feed');
  if (!feed) return;

  try {
    const filterCity = document.getElementById('proposals-city-filter')?.value || 'All Cities';
    const query = filterCity !== 'All Cities' ? `?city=${encodeURIComponent(filterCity)}` : '';
    const res = await fetch(`/api/city-proposals${query}`);
    const proposals = await res.json();

    if (!proposals.length) {
      feed.innerHTML = `
        <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:32px; text-align:center; color:var(--text-muted);">
          No proposals submitted yet. Click "File New Proposal to Centre" to start!
        </div>
      `;
      return;
    }

    feed.innerHTML = proposals.map(p => {
      const isMine = p.city.toLowerCase() === activeCity.toLowerCase();
      const hasUpvoted = (p.upvoted_by || []).includes(cityOfficerInfo.id);

      let statusPill = `<span class="status-badge-review">● ${p.status || 'Submitted to Centre'}</span>`;
      if ((p.status || '').includes('Approved') || (p.status || '').includes('Sanctioned')) {
        statusPill = `<span class="status-badge-sanctioned">● ${p.status}</span>`;
      } else if ((p.status || '').includes('BRICS')) {
        statusPill = `<span class="status-badge-escalated">● ${p.status}</span>`;
      }

      return `
        <div class="proposal-card">
          <div class="proposal-top">
            <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
              <span class="nav-badge" style="background:rgba(245,158,11,0.12); color:#fbbf24; border:1px solid rgba(245,158,11,0.3);">
                📍 ${p.city}
              </span>
              <span class="nav-badge">${p.category}</span>
              ${isMine ? `<span class="nav-badge" style="background:rgba(16,185,129,0.15); color:#10b981;">${window.getTranslation('badge_your_city_proposal', "Your City's Proposal")}</span>` : ''}
            </div>
            <div style="display:flex; align-items:center; gap:10px;">
              ${statusPill}
              <button class="btn-upvote ${hasUpvoted ? 'upvoted' : ''}" onclick="upvoteProposal('${p.id}')" title="Upvote peer city proposal">
                <span>▲</span>
                <span id="upvote-count-${p.id}">${p.upvotes || 0}</span>
                <span style="font-size:0.75rem;">${window.getTranslation('label_upvotes', 'Upvotes')}</span>
              </button>
            </div>
          </div>

          <h3 class="proposal-title">${p.title}</h3>
          <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.55; margin-bottom:12px;">${p.justification}</p>

          <div class="proposal-meta-grid">
            <div>👤 <b>${window.getTranslation('label_submitted_by', 'Submitted by')}:</b> ${p.officer_name} (${p.city})</div>
            <div>💰 <b>${window.getTranslation('label_estimated_capex', 'Estimated CapEx')}:</b> <b style="color:var(--brics-gold);">${p.estimated_capex}</b></div>
            <div>⏱️ <b>${window.getTranslation('label_timeline', 'Timeline')}:</b> ${p.timeline || '24 Months'}</div>
            <div>👥 <b>${window.getTranslation('label_beneficiaries', 'Beneficiaries')}:</b> ${p.demographic_impact || 'Regional population'}</div>
          </div>

          ${p.central_notes ? `
            <div style="background:rgba(37,99,235,0.08); border-left:3px solid #2563eb; padding:10px 14px; border-radius:0 8px 8px 0; font-size:0.84rem; color:var(--text-primary); margin-top:10px;">
              <b style="color:#60a5fa;">${window.getTranslation('label_central_commission_note', 'Central Planning Commission Note:')}</b> ${p.central_notes}
            </div>
          ` : ''}
        </div>
      `;
    }).join('');
  } catch (err) {
    console.error('Error loading proposals feed:', err);
  }
}

window.upvoteProposal = async function(id) {
  try {
    const res = await fetch(`/api/city-proposals/${id}/upvote`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ voter_id: cityOfficerInfo.id })
    });
    const data = await res.json();
    if (data.status === 'ok') {
      showToast('Upvote recorded! Regional consensus score increased.', 'success');
      const el = document.getElementById(`upvote-count-${id}`);
      if (el) el.textContent = data.upvotes;
      await loadCityProposalsFeed();
    } else {
      showToast(data.message || 'Already upvoted', 'info');
    }
  } catch (err) {
    showToast('Failed to upvote', 'error');
  }
};

async function handleProposalSubmit() {
  const btn = document.getElementById('btn-submit-proposal');
  if (btn) btn.disabled = true;

  const payload = {
    city: activeCity,
    officer_name: document.getElementById('prop-input-officer')?.value || cityOfficerInfo.name,
    officer_id: cityOfficerInfo.id,
    department: cityOfficerInfo.role,
    title: document.getElementById('prop-input-title')?.value,
    category: document.getElementById('prop-input-category')?.value,
    estimated_capex: document.getElementById('prop-input-capex')?.value,
    timeline: document.getElementById('prop-input-timeline')?.value,
    demographic_impact: document.getElementById('prop-input-impact')?.value,
    justification: document.getElementById('prop-input-justification')?.value,
    ai_generated: false
  };

  try {
    const res = await fetch('/api/city-proposals', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    if (data.status === 'created') {
      showToast('Proposal transmitted to Central Command successfully!', 'success');
      const modalEl = document.getElementById('file-proposal-modal');
      if (modalEl) modalEl.style.display = 'none';
      document.getElementById('form-file-proposal')?.reset();
      setCity(activeCity); // reset modal city input
      await loadCityProposalsFeed();
    }
  } catch (err) {
    showToast('Failed to transmit proposal', 'error');
  } finally {
    if (btn) btn.disabled = false;
  }
}

// Re-render when language changes
window.addEventListener('civicpulse:languageChanged', () => {
  if (typeof loadCityComplaints === 'function') loadCityComplaints();
  if (typeof loadCityAiPlans === 'function') loadCityAiPlans();
  if (typeof loadCityProposalsFeed === 'function') loadCityProposalsFeed();
});

