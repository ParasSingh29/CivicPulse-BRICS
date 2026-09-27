/**
 * CIVICPULSE-BRICS: CENTRAL OFFICIAL COMMAND CONTROLLER
 * Oversees All Assigned City Officers, Red/Yellow/Green Problem Health Meters,
 * Municipal Proposals Sanctioning, Gemini AI BRICS Joint Ventures, and Inbound Partner Requests
 */

window.initCentralOfficialPortal = async function() {
  setupCentralEvents();
  await refreshCentralDashboard();
};

if (document.readyState === 'interactive' || document.readyState === 'complete') {
  window.initCentralOfficialPortal();
} else {
  document.addEventListener('DOMContentLoaded', window.initCentralOfficialPortal);
}


function setupCentralEvents() {
  // Proposals filter
  const propFilter = document.getElementById('central-proposals-filter');
  if (propFilter) {
    propFilter.addEventListener('change', loadCentralProposals);
  }

  // Modal close handlers
  const btnCloseJv = document.getElementById('btn-close-jv-modal');
  const btnCancelJv = document.getElementById('btn-cancel-jv');
  const modalJv = document.getElementById('draft-jv-modal');

  const closeJvModal = () => { if (modalJv) modalJv.style.display = 'none'; };
  if (btnCloseJv) btnCloseJv.addEventListener('click', closeJvModal);
  if (btnCancelJv) btnCancelJv.addEventListener('click', closeJvModal);

  // Close modal on Escape key press
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeJvModal();
  });

  // Form draft JV submission
  const formDraftJv = document.getElementById('form-draft-jv');
  if (formDraftJv) {
    formDraftJv.addEventListener('submit', async (e) => {
      e.preventDefault();
      await handleTransmitBilateralJv();
    });
  }
}

async function refreshCentralDashboard() {
  await Promise.all([
    loadCityOfficersOverview(),
    loadCentralProposals(),
    loadCentralBricsJVs(),
    loadInboundPartnerRequests()
  ]);
}

// ==============================================================================
// 1. PANEL 1: ASSIGNED CITY OFFICERS & RED / YELLOW / GREEN STATUS METERS
// ==============================================================================
window.loadCityOfficersOverview = async function loadCityOfficersOverview() {
  const grid = document.getElementById('central-officers-grid');
  if (!grid) return;

  try {
    // Determine the active BRICS node (country) for this portal session.
    // We read from the stored session or fall back to /api/brics/nodes.
    let countryCode = window._centralPortalCountryCode;
    if (!countryCode) {
      try {
        const nodeRes = await fetch('/api/brics/nodes');
        const nodeData = await nodeRes.json();
        countryCode = nodeData.active_code || 'IN';
        window._centralPortalCountryCode = countryCode; // cache for this session
      } catch (_) {
        countryCode = 'IN'; // safe default
      }
    }

    // Fetch officers filtered to this country only
    const res = await fetch(`/api/city-officers?country_code=${encodeURIComponent(countryCode)}`);
    const officers = await res.json();

    // Calculate aggregated nationwide totals
    let natTotal = 0, natRed = 0, natYellow = 0, natGreen = 0;
    officers.forEach(o => {
      natTotal += o.total_problems || 0;
      natRed += o.red_problems || 0;
      natYellow += o.yellow_problems || 0;
      natGreen += o.green_problems || 0;
    });

    const kpiTotal = document.getElementById('central-kpi-total-nat');
    const kpiRed = document.getElementById('central-kpi-red');
    const kpiYellow = document.getElementById('central-kpi-yellow');
    const kpiGreen = document.getElementById('central-kpi-green');

    if (kpiTotal) kpiTotal.textContent = natTotal;
    if (kpiRed) kpiRed.textContent = natRed;
    if (kpiYellow) kpiYellow.textContent = natYellow;
    if (kpiGreen) kpiGreen.textContent = natGreen;

    if (!officers.length) {
      grid.innerHTML = `
        <div style="grid-column:1/-1; background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:40px; text-align:center; color:var(--text-muted);">
          <div style="font-size:2rem; margin-bottom:12px;">🏛️</div>
          <div style="font-size:1.05rem; font-weight:700; margin-bottom:6px;">No City Officers Assigned</div>
          <div style="font-size:0.85rem;">No municipal officers are registered for your country node (${countryCode}).</div>
        </div>
      `;
      return;
    }

    grid.innerHTML = officers.map(o => {
      const initials = o.name.split(' ').map(w => w[0]).filter(Boolean).slice(-2).join('');
      const total = o.total_problems || 0;
      const red = o.red_problems || 0;
      const yellow = o.yellow_problems || 0;
      const green = o.green_problems || 0;
      const health = o.health_index || 95;

      const pctRed = total > 0 ? (red / total) * 100 : 0;
      const pctYellow = total > 0 ? (yellow / total) * 100 : 0;
      const pctGreen = total > 0 ? (green / total) * 100 : 100;

      let healthColor = '#10b981';
      if (health < 40) healthColor = '#ef4444';
      else if (health < 70) healthColor = '#f59e0b';

      return `
        <div class="officer-card">
          <div>
            <div class="officer-header">
              <div style="display:flex; align-items:center; gap:12px;">
                <div class="officer-avatar-box">${initials}</div>
                <div>
                  <div style="display:flex; align-items:center; gap:6px;">
                    <b style="font-size:1.05rem; color:var(--text-primary);">${o.name}</b>
                    <span>${o.flag}</span>
                  </div>
                  <div style="font-size:0.78rem; color:var(--text-muted);">${o.designation}</div>
                  <div style="font-size:0.75rem; color:var(--accent-primary); font-weight:700;">📍 ${o.jurisdiction}</div>
                </div>
              </div>
              <span class="nav-badge" style="background:${healthColor}15; color:${healthColor}; border:1px solid ${healthColor}35;">
                ${window.getTranslation('label_health', 'Health')}: ${health}%
              </span>
            </div>

            <div style="font-size:0.8rem; color:var(--text-secondary); margin-bottom:12px;">
              <b>${window.getTranslation('label_department', 'Department')}:</b> ${o.department} • <b>${window.getTranslation('label_contact', 'Contact')}:</b> ${o.phone}
            </div>

            <!-- Problem Statistics Breakdown -->
            <div style="background:rgba(255,255,255,0.02); border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:12px; margin-bottom:8px;">
              <div style="display:flex; justify-content:space-between; font-size:0.82rem; margin-bottom:6px;">
                <span style="font-weight:700;">${window.getTranslation('label_total_city_problems', 'Total City Problems')}:</span>
                <b style="color:var(--text-primary);">${total}</b>
              </div>

              <!-- Multi-Segment RYG Meter -->
              <div class="ryg-bar-wrap" style="height:8px; margin:6px 0;">
                <div class="ryg-seg-red" style="width:${pctRed}%;"></div>
                <div class="ryg-seg-yellow" style="width:${pctYellow}%;"></div>
                <div class="ryg-seg-green" style="width:${pctGreen}%;"></div>
              </div>

              <div class="ryg-legend" style="justify-content:space-between; margin-top:6px;">
                <span class="ryg-legend-item"><span class="ryg-dot ryg-dot-red"></span> ${window.getTranslation('legend_red_critical', 'Red: Critical')}: <b>${red}</b></span>
                <span class="ryg-legend-item"><span class="ryg-dot ryg-dot-yellow"></span> ${window.getTranslation('legend_yellow_in_progress', 'Yellow: In Progress')}: <b>${yellow}</b></span>
                <span class="ryg-legend-item"><span class="ryg-dot ryg-dot-green"></span> ${window.getTranslation('legend_green_resolved', 'Green: Resolved')}: <b>${green}</b></span>
              </div>
            </div>
          </div>

          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:10px; padding-top:10px; border-top:1px solid var(--border-subtle);">
            <span style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">${o.id}</span>
            <span class="badge" style="font-size:0.75rem; padding:4px 8px; background:rgba(37,99,235,0.12); color:#60a5fa; border:1px solid rgba(37,99,235,0.3); border-radius:4px;">
              <span>${o.city} Municipal Operations</span>
            </span>
          </div>
        </div>
      `;
    }).join('');
  } catch (err) {
    console.error('Error loading city officers overview:', err);
  }
}

// ==============================================================================
// 2. PANEL 2: STRATEGIC PROPOSALS SUBMITTED BY CITY OFFICERS
// ==============================================================================
window.loadCentralProposals = async function loadCentralProposals() {
  const feed = document.getElementById('central-proposals-feed');
  if (!feed) return;

  try {
    const filter = document.getElementById('central-proposals-filter')?.value || 'All';
    const query = filter !== 'All' ? `?city=${encodeURIComponent(filter)}` : '';
    const res = await fetch(`/api/city-proposals${query}`);
    const proposals = await res.json();

    if (!proposals.length) {
      feed.innerHTML = `
        <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:32px; text-align:center; color:var(--text-muted);">
          No municipal proposals submitted yet for this filter.
        </div>
      `;
      return;
    }

    feed.innerHTML = proposals.map(p => {
      const translatedStatus = window.getTranslation(p.status) || p.status || 'Submitted to Centre';
      let statusPill = `<span class="status-badge-review">● ${translatedStatus}</span>`;
      if ((p.status || '').includes('Approved') || (p.status || '').includes('Sanctioned')) {
        statusPill = `<span class="status-badge-sanctioned">● ${translatedStatus}</span>`;
      } else if ((p.status || '').includes('BRICS')) {
        statusPill = `<span class="status-badge-escalated">● ${translatedStatus}</span>`;
      }

      return `
        <div class="proposal-card">
          <div class="proposal-top">
            <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
              <span class="nav-badge" style="background:rgba(245,158,11,0.12); color:#fbbf24; border:1px solid rgba(245,158,11,0.3);">
                📍 ${(window.getTranslation && window.getTranslation('label_city')) || 'City'}: ${p.city}
              </span>
              <span class="nav-badge">${p.category}</span>
              <span class="nav-badge" style="background:rgba(16,185,129,0.12); color:#10b981;">
                ▲ ${p.upvotes || 0} ${window.getTranslation('label_peer_upvotes', 'Peer Upvotes')}
              </span>
            </div>
            ${statusPill}
          </div>

          <h3 class="proposal-title">${p.title}</h3>
          <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.55; margin-bottom:12px;">${p.justification}</p>

          <div class="proposal-meta-grid">
            <div>👤 <b>${window.getTranslation('label_submitting_officer', 'Submitting Officer')}:</b> ${p.officer_name} (${p.city})</div>
            <div>💰 <b>${window.getTranslation('label_requested_capex', 'Requested CapEx')}:</b> <b style="color:var(--brics-gold);">${p.estimated_capex}</b></div>
            <div>⏱️ <b>${window.getTranslation('label_target_timeline', 'Target Timeline')}:</b> ${p.timeline || '24 Months'}</div>
            <div>👥 <b>${window.getTranslation('label_demographic_impact', 'Demographic Impact')}:</b> ${p.demographic_impact}</div>
          </div>

          ${p.central_notes ? `
            <div style="background:rgba(37,99,235,0.08); border-left:3px solid #2563eb; padding:8px 12px; border-radius:0 6px 6px 0; font-size:0.82rem; color:var(--text-primary); margin-bottom:12px;">
              <b style="color:#60a5fa;">${window.getTranslation('label_current_directive', 'Current Planning Directive:')}</b> ${p.central_notes}
            </div>
          ` : ''}

          <!-- Central Executive Action Buttons -->
          <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:10px;">
            <button class="btn btn-success btn-sm" onclick="handleUpdateProposalStatus('${p.id}', 'Approved for National Budget', 'Sanctioned under National Infrastructure Pipeline.')">
              <span>${window.AppIcons.check}</span>
              <span>${window.getTranslation('btn_sanction_approve_budget', 'Sanction / Approve Budget')}</span>
            </button>
            <button class="btn btn-primary btn-sm" onclick="handleUpdateProposalStatus('${p.id}', 'Escalated to BRICS JV', 'Referred to BRICS Bilateral Joint Venture Committee.')">
              <span>${window.AppIcons.zap}</span>
              <span>${window.getTranslation('btn_escalate_brics_jv', 'Escalate to BRICS Joint Venture')}</span>
            </button>
            <button class="btn btn-secondary btn-sm" onclick="handleUpdateProposalStatus('${p.id}', 'Under Technical Revision', 'Clarifications requested from municipal engineering team.')">
              <span>${window.AppIcons.refresh}</span>
              <span>${window.getTranslation('btn_request_revision', 'Request Revision')}</span>
            </button>
          </div>
        </div>
      `;
    }).join('');
  } catch (err) {
    console.error('Error loading central proposals:', err);
  }
}

window.handleUpdateProposalStatus = async function(id, newStatus, notes) {
  try {
    const res = await fetch(`/api/city-proposals/${id}/status`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status: newStatus, central_notes: notes })
    });
    const data = await res.json();
    if (data.status === 'ok') {
      showToast(`Proposal #${id} updated: ${newStatus}!`, 'success');
      await loadCentralProposals();
    }
  } catch (err) {
    showToast('Failed to update proposal status', 'error');
  }
};

// ==============================================================================
// 3. PANEL 3: NATIONAL INTEREST AI BRICS JOINT VENTURES
// ==============================================================================
window.loadCentralBricsJVs = async function loadCentralBricsJVs() {
  const container = document.getElementById('central-brics-jv-container');
  if (!container) return;

  try {
    container.innerHTML = `
      <div style="text-align:center; padding:30px; color:var(--text-muted);">
        Evaluating national problem patterns & synthesizing BRICS Joint Ventures...
      </div>
    `;

    const res = await fetch('/api/central/ai/brics-plans');
    const plans = await res.json();

    if (!plans.length) {
      container.innerHTML = `<div style="text-align:center; color:var(--text-muted);">No BRICS joint ventures synthesized.</div>`;
      return;
    }

    container.innerHTML = plans.map((jv, idx) => {
      return `
        <div class="brics-jv-card">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:8px;">
            <div class="brics-flag-pair">
              <span>🇮🇳</span>
              <span>🤝</span>
              <span>${jv.partner_flag || '🇨🇳'}</span>
              <span style="font-size:0.9rem; font-weight:800; margin-left:4px;">India — ${jv.partner_country}</span>
            </div>
            <span class="nav-badge" style="background:rgba(245,158,11,0.15); color:var(--brics-gold); border:1px solid rgba(245,158,11,0.35);">
              CapEx: ${jv.estimated_capex}
            </span>
          </div>

          <h3 class="jv-title">${jv.title}</h3>

          <div style="font-size:0.84rem; color:var(--text-muted); margin-bottom:10px;">
            <b>${window.getTranslation('label_sector', 'Sector')}:</b> ${jv.sector} • <b>${window.getTranslation('label_domestic_body', 'Domestic Body')}:</b> ${jv.domestic_counterpart} • <b>${window.getTranslation('label_foreign_entity', 'Foreign Entity')}:</b> ${jv.partner_entity}
          </div>

          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.55; margin-bottom:12px;">
            ${jv.national_interest_analysis}
          </p>

          <div style="background:rgba(255,255,255,0.02); border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:12px; margin-bottom:16px;">
            <div style="font-size:0.8rem; font-weight:700; color:#60a5fa; margin-bottom:6px;">🚀 ${window.getTranslation('label_tech_transfer_synergy', 'Technology Transfer & National Synergy:')}</div>
            <ul style="padding-left:18px; font-size:0.8rem; color:var(--text-secondary); line-height:1.5;">
              ${(jv.synergy_benefits || []).map(s => `<li>${s}</li>`).join('')}
            </ul>
          </div>

          <button class="btn btn-primary" style="width:100%; background:#2563eb; border-color:#2563eb;" onclick="openDraftJvModal(${idx})">
            <span>${window.getTranslation('btn_draft_propose_jv', 'Draft & Propose Joint Venture')} (${jv.partner_country})</span>
            <svg class="svg-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
          </button>
        </div>
      `;
    }).join('');

    window.currentBricsJvs = plans;
  } catch (err) {
    console.error('Error loading BRICS JVs:', err);
  }
}

window.openDraftJvModal = function(idx) {
  const jv = (window.currentBricsJvs || [])[idx];
  if (!jv) return;

  const titleEl = document.getElementById('modal-jv-title');
  const partnerInput = document.getElementById('jv-input-partner');
  const entityInput = document.getElementById('jv-input-entity');
  const titleInput = document.getElementById('jv-input-title');
  const domesticInput = document.getElementById('jv-input-domestic');
  const capexInput = document.getElementById('jv-input-capex');
  const financingInput = document.getElementById('jv-input-financing');
  const notesInput = document.getElementById('jv-input-notes');

  if (titleEl) titleEl.textContent = `Propose Bilateral JV to ${jv.partner_country}`;
  if (partnerInput) partnerInput.value = `${jv.partner_flag} ${jv.partner_country}`;
  if (entityInput) entityInput.value = jv.partner_entity || '';
  if (titleInput) titleInput.value = jv.title || '';
  if (domesticInput) domesticInput.value = jv.domestic_counterpart || '';
  if (capexInput) capexInput.value = jv.estimated_capex || '';
  if (financingInput) financingInput.value = jv.financing_structure || '50% Sovereign Equity + NDB Guarantee';
  if (notesInput) notesInput.value = `National CapEx Planning Commission approves formal diplomatic submission to the ${jv.partner_country} Ministry of Transport and Trade.`;

  window.activeDraftingJv = jv;
  const modalEl = document.getElementById('draft-jv-modal');
  if (modalEl) modalEl.style.display = 'flex';
};

async function handleTransmitBilateralJv() {
  const btn = document.getElementById('btn-transmit-jv');
  if (btn) btn.disabled = true;

  const jv = window.activeDraftingJv || {};
  const payload = {
    partner_country: jv.partner_country || 'China',
    project_title: jv.title,
    capex: jv.estimated_capex,
    notes: document.getElementById('jv-input-notes')?.value || ''
  };

  try {
    const res = await fetch('/api/central/brics-proposals', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    showToast(data.message || 'Bilateral proposal transmitted!', 'success');
    const modalEl = document.getElementById('draft-jv-modal');
    if (modalEl) modalEl.style.display = 'none';
  } catch (err) {
    showToast('Failed to transmit bilateral proposal', 'error');
  } finally {
    if (btn) btn.disabled = false;
  }
}

// ==============================================================================
// 4. PANEL 4: INBOUND REQUESTS FROM OTHER BRICS COUNTRIES
// ==============================================================================
window.loadInboundPartnerRequests = async function loadInboundPartnerRequests() {
  const container = document.getElementById('central-inbound-requests-container');
  if (!container) return;

  try {
    const res = await fetch('/api/central/brics-incoming-requests');
    const requests = await res.json();

    if (!requests.length) {
      container.innerHTML = `<div style="text-align:center; color:var(--text-muted); padding:20px;">No incoming requests.</div>`;
      return;
    }

    container.innerHTML = requests.map(req => {
      let badgeColor = '#f59e0b';
      if ((req.status || '').includes('Sanctioned') || (req.status || '').includes('Accepted')) badgeColor = '#10b981';
      else if ((req.status || '').includes('Bilateral')) badgeColor = '#60a5fa';

      return `
        <div class="inbound-req-card">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px; flex-wrap:wrap; gap:6px;">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:1.25rem;">${req.origin_flag}</span>
              <b>From: ${req.origin_country}</b>
            </div>
            <span class="nav-badge" style="background:${badgeColor}15; color:${badgeColor}; border:1px solid ${badgeColor}35; font-size:0.72rem;">
              ${req.status}
            </span>
          </div>

          <h4 style="font-size:0.95rem; font-weight:800; color:var(--text-primary); margin-bottom:6px; line-height:1.35;">${req.project_title}</h4>
          <p style="font-size:0.83rem; color:var(--text-secondary); line-height:1.45; margin-bottom:10px;">${req.summary}</p>

          <div style="font-size:0.78rem; color:var(--text-muted); margin-bottom:10px; line-height:1.4;">
            <div>🏢 <b>${window.getTranslation('label_origin', 'Origin')}:</b> ${req.origin_ministry}</div>
            <div>💰 <b>${window.getTranslation('label_proposed_budget', 'Proposed Budget')}:</b> <b style="color:var(--brics-gold);">${req.proposed_capex}</b></div>
            <div>📍 <b>${window.getTranslation('label_target_location', 'Target Location')}:</b> ${req.target_location}</div>
          </div>

          <!-- Quick Action Buttons -->
          <div style="display:flex; gap:8px; flex-wrap:wrap;">
            <button class="btn btn-success btn-sm" style="font-size:0.76rem; padding:4px 10px;" onclick="handleRespondToInbound('${req.id}', 'accept')">
              <span>${window.getTranslation('btn_accept_sanction', 'Accept & Sanction')}</span>
            </button>
            <button class="btn btn-secondary btn-sm" style="font-size:0.76rem; padding:4px 10px;" onclick="handleRespondToInbound('${req.id}', 'negotiate')">
              <span>${window.getTranslation('btn_bilateral_dialogue', 'Bilateral Dialogue')}</span>
            </button>
          </div>
        </div>
      `;
    }).join('');
  } catch (err) {
    console.error('Error loading inbound requests:', err);
  }
}

window.handleRespondToInbound = async function(id, action) {
  try {
    const res = await fetch(`/api/central/brics-incoming-requests/${id}/respond`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ action: action })
    });
    const data = await res.json();
    if (data.status === 'ok') {
      showToast(`Request #${id} marked as ${data.request?.status}!`, 'success');
      await loadInboundPartnerRequests();
    }
  } catch (err) {
    showToast('Failed to respond to request', 'error');
  }
};

// Re-render when language changes
window.addEventListener('civicpulse:languageChanged', () => {
  if (typeof loadCityOfficersOverview === 'function') loadCityOfficersOverview();
  if (typeof loadCentralProposalsFeed === 'function') loadCentralProposalsFeed();
  if (typeof loadCentralMegaPlans === 'function') loadCentralMegaPlans();
  if (typeof loadInboundPartnerRequests === 'function') loadInboundPartnerRequests();
});

