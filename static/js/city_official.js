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

document.addEventListener('DOMContentLoaded', async () => {
  // Check stored city preference
  const savedCity = localStorage.getItem('civicpulse_city') || 'Delhi';
  setCity(savedCity);

  setupCityOfficialEvents();
  await refreshCityOfficialDashboard();
});

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
  // City Selector Change
  const citySelector = document.getElementById('city-selector');
  if (citySelector) {
    citySelector.addEventListener('change', async (e) => {
      setCity(e.target.value);
      await refreshCityOfficialDashboard();
      showToast(`Switched to ${e.target.value} Municipal Command Console`, 'info');
    });
  }

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
  const btnCloseModal = document.getElementById('btn-close-proposal-modal');
  const btnCancelModal = document.getElementById('btn-cancel-proposal');
  const modalEl = document.getElementById('file-proposal-modal');

  const openModal = () => { if (modalEl) modalEl.style.display = 'flex'; };
  const closeModal = () => { if (modalEl) modalEl.style.display = 'none'; };

  if (btnOpenModal) btnOpenModal.addEventListener('click', openModal);
  if (btnTriggerModal) btnTriggerModal.addEventListener('click', openModal);
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
}

// ==============================================================================
// 2. CITY COMPLAINTS & REPAIR OPERATIONS (SCOPED STRICTLY TO CITY)
// ==============================================================================
async function loadCityComplaints() {
  const container = document.getElementById('city-complaints-container');
  if (!container) return;

  try {
    const res = await fetch(`/api/complaints?city=${encodeURIComponent(activeCity)}`);
    const allCityComplaints = await res.json();

    // Update KPIs and RYG Multi-Segment Bar
    updateMunicipalHealthHUD(allCityComplaints);

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

    container.innerHTML = filtered.map(c => {
      const loc = c.location || {};
      const lat = loc.latitude || 28.6139;
      const lon = loc.longitude || 77.2090;
      const address = loc.address || `${activeCity} Municipality Area`;
      const status = c.status || 'Pending';

      const isProg = status.includes('Progress') || status.includes('dispatched');
      const isRes = status.includes('Resolved') || status.includes('closed');

      let statusBadge = `<span class="pill pill-pending">● Red: Pending Action</span>`;
      if (isRes) statusBadge = `<span class="pill pill-resolved">● Green: Resolved</span>`;
      else if (isProg) statusBadge = `<span class="pill pill-progress">● Yellow: Crew Dispatched</span>`;

      return `
        <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:20px; margin-bottom:14px; box-shadow:var(--shadow-sm);">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
            <div>
              <span style="font-family:var(--font-mono); font-size:0.85rem; font-weight:700; color:var(--accent-primary);">#${c.id}</span>
              <b style="margin-left:8px; font-size:1.05rem;">${c.category}</b>
            </div>
            ${statusBadge}
          </div>

          <p style="font-size:0.92rem; color:var(--text-secondary); margin-bottom:12px; line-height:1.5;">${c.description}</p>

          <div style="font-size:0.8rem; color:var(--text-muted); margin-bottom:14px; display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
            <span>${window.AppIcons.map_pin}</span>
            <span>Location: <b>${address}</b> • Date: ${c.timestamp}</span>
          </div>

          <!-- 1-Click Status Toggles -->
          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            ${!isProg ? `
              <button class="btn btn-secondary btn-sm" onclick="changeCityComplaintStatus('${c.id}', 'In Progress')">
                <span>${window.AppIcons.wrench}</span>
                <span>Send Repair Team</span>
              </button>
            ` : ''}
            ${!isRes ? `
              <button class="btn btn-success btn-sm" onclick="changeCityComplaintStatus('${c.id}', 'Resolved')">
                <span>${window.AppIcons.check}</span>
                <span>Mark as Fixed</span>
              </button>
            ` : ''}
            ${isRes ? `
              <button class="btn btn-secondary btn-sm" onclick="changeCityComplaintStatus('${c.id}', 'Pending')">
                <span>${window.AppIcons.refresh}</span>
                <span>Re-open Incident</span>
              </button>
            ` : ''}
            <a href="https://www.google.com/maps/search/?api=1&query=${lat},${lon}" target="_blank" class="btn btn-secondary btn-sm">
              <span>${window.AppIcons.navigation}</span>
              <span>Open Maps</span>
            </a>
          </div>
        </div>
      `;
    }).join('');
  } catch (err) {
    console.error('Error loading city complaints:', err);
  }
}

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

window.changeCityComplaintStatus = async function(id, newStatus) {
  try {
    const res = await fetch(`/api/complaints/${id}/status`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status: newStatus })
    });
    const data = await res.json();
    if (data.status === 'ok') {
      showToast(`Problem #${id} marked as ${newStatus}!`, 'success');
      await loadCityComplaints();
    }
  } catch (err) {
    showToast('Failed to update status', 'error');
  }
};

// ==============================================================================
// 3. LOCAL AREA AI STRATEGIC SUGGESTIONS (GEMINI 2.5)
// ==============================================================================
async function loadCityAiSuggestions() {
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
              <div>⏱️ <b>Timeline:</b> ${p.timeline || '24 Months'}</div>
              <div>👥 <b>Impact:</b> ${p.demographic_impact}</div>
              <div style="margin-top:6px; color:#60a5fa;">💡 <b>AI Directive:</b> ${p.policy_recommendation || 'Escalate to Central Command.'}</div>
            </div>
          </div>

          <button class="btn btn-primary" style="background:#059669; border-color:#059669; width:100%;" onclick="prefillAndOpenProposalModal(${idx})">
            <span>File This Proposal to Centre</span>
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
async function loadCityProposalsFeed() {
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
              ${isMine ? `<span class="nav-badge" style="background:rgba(16,185,129,0.15); color:#10b981;">Your City's Proposal</span>` : ''}
            </div>
            <div style="display:flex; align-items:center; gap:10px;">
              ${statusPill}
              <button class="btn-upvote ${hasUpvoted ? 'upvoted' : ''}" onclick="upvoteProposal('${p.id}')" title="Upvote peer city proposal">
                <span>▲</span>
                <span id="upvote-count-${p.id}">${p.upvotes || 0}</span>
                <span style="font-size:0.75rem;">Upvotes</span>
              </button>
            </div>
          </div>

          <h3 class="proposal-title">${p.title}</h3>
          <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.55; margin-bottom:12px;">${p.justification}</p>

          <div class="proposal-meta-grid">
            <div>👤 <b>Submitted by:</b> ${p.officer_name} (${p.city})</div>
            <div>💰 <b>Estimated CapEx:</b> <b style="color:var(--brics-gold);">${p.estimated_capex}</b></div>
            <div>⏱️ <b>Timeline:</b> ${p.timeline || '24 Months'}</div>
            <div>👥 <b>Beneficiaries:</b> ${p.demographic_impact || 'Regional population'}</div>
          </div>

          ${p.central_notes ? `
            <div style="background:rgba(37,99,235,0.08); border-left:3px solid #2563eb; padding:10px 14px; border-radius:0 8px 8px 0; font-size:0.84rem; color:var(--text-primary); margin-top:10px;">
              <b style="color:#60a5fa;">Central Planning Commission Note:</b> ${p.central_notes}
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
