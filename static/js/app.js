/**
 * CIVICPULSE-BRICS: CORE APPLICATION CONTROLLER
 * State Management, BRICS Sovereign Dynamic Theming, SVG Icon System & Role Switcher
 */

// ==============================================================================
// 1. ENTERPRISE SVG VECTOR REGISTRY
// ==============================================================================
window.AppIcons = {
  // Sovereign BRICS Flags (Pure Vector SVGs)
  flag_in: `<svg class="flag-svg" viewBox="0 0 24 16" width="22" height="15"><rect width="24" height="5.33" fill="#ff9933"/><rect y="5.33" width="24" height="5.33" fill="#ffffff"/><rect y="10.66" width="24" height="5.33" fill="#138808"/><circle cx="12" cy="8" r="2.1" fill="none" stroke="#000080" stroke-width="0.7"/><circle cx="12" cy="8" r="0.5" fill="#000080"/></svg>`,
  flag_br: `<svg class="flag-svg" viewBox="0 0 24 16" width="22" height="15"><rect width="24" height="16" fill="#009c3b"/><polygon points="12,2.2 21.8,8 12,13.8 2.2,8" fill="#ffdf00"/><circle cx="12" cy="8" r="3.2" fill="#002776"/><path d="M9.2,7.4 Q12,6.5 14.8,8.2" stroke="#ffffff" stroke-width="0.5" fill="none"/></svg>`,
  flag_za: `<svg class="flag-svg" viewBox="0 0 24 16" width="22" height="15"><rect width="24" height="8" fill="#e03c31"/><rect y="8" width="24" height="8" fill="#001489"/><polygon points="0,0 8.5,8 0,16" fill="#000000"/><polygon points="0,1.2 7.2,8 0,14.8" fill="#000000"/><path d="M0,0 L9,8 L24,8 L24,5 L11.5,5 L6,0 Z" fill="#ffffff" opacity="0.95"/><path d="M0,16 L9,8 L24,8 L24,11 L11.5,11 L6,16 Z" fill="#ffffff" opacity="0.95"/><path d="M0,0 L8,8 L24,8 L24,6 L10.5,6 L4,0 Z" fill="#007749"/><path d="M0,16 L8,8 L24,8 L24,10 L10.5,10 L4,16 Z" fill="#007749"/><polyline points="0,1 7,8 0,15" stroke="#ffb612" stroke-width="1.3" fill="none"/></svg>`,

  // UI Symbols
  sun: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>`,
  moon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>`,
  zap: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>`,
  chevron_up: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>`,
  map_pin: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>`,
  tag: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>`,
  coins: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="8" r="6"/><path d="M18.09 10.37A6 6 0 1 1 10.34 18"/><path d="M7 6h1v4"/><path d="M16.7 13.7h.6v2.6"/></svg>`,
  users: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>`,
  volume: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>`,
  check: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>`,
  wrench: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>`,
  refresh: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg>`,
  navigation: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 11 22 2 13 21 11 13 3 11"/></svg>`,

  // Infrastructure Sectors (Crisp Vectors)
  road: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="12" y1="4" x2="12" y2="8"/><line x1="12" y1="12" x2="12" y2="16"/><line x1="12" y1="20" x2="12" y2="22"/></svg>`,
  droplet: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>`,
  trash: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><line x1="10" y1="11" x2="10" y2="17"/><line x1="14" y1="11" x2="14" y2="17"/></svg>`,
  bus: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="14" rx="2"/><path d="M3 10h18"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/><line x1="3" y1="17" x2="5" y2="17"/><line x1="19" y1="17" x2="21" y2="17"/></svg>`,
  cloud_rain: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="16" y1="13" x2="16" y2="21"/><line x1="8" y1="13" x2="8" y2="21"/><line x1="12" y1="15" x2="12" y2="23"/><path d="M20 16.58A5 5 0 0 0 18 7h-1.26A8 8 0 1 0 4 15.25"/></svg>`,
  health: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>`,
  school: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>`,
  trees: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 19 14 5 14 12 2"/><rect x="10" y="14" width="4" height="8"/></svg>`,
  shield: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>`,
  brain: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>`
};

// Aliases for brics_context.py keys
window.AppIcons.roads = window.AppIcons.road;
window.AppIcons.water = window.AppIcons.droplet;
window.AppIcons.electricity = window.AppIcons.zap;
window.AppIcons.waste = window.AppIcons.trash;
window.AppIcons.transit = window.AppIcons.bus;
window.AppIcons.drainage = window.AppIcons.cloud_rain;
window.AppIcons.schools = window.AppIcons.school;
window.AppIcons.parks = window.AppIcons.trees;
window.AppIcons.safety = window.AppIcons.shield;

window.getSvgIcon = function(key, color, size = 18) {
  let iconHtml = window.AppIcons[key] || window.AppIcons['zap'];
  if (color) {
    iconHtml = iconHtml.replace('stroke="currentColor"', `stroke="${color}"`);
  }
  if (size) {
    iconHtml = iconHtml.replace('width="20"', `width="${size}"`).replace('height="20"', `height="${size}"`);
  }
  return iconHtml;
};

// ==============================================================================
// 2. GLOBAL APPLICATION STATE
// ==============================================================================
const AppState = {
  activeNode: null,
  activeCode: 'IN',
  currentRole: 'citizen', // 'citizen' or 'gov'
  theme: localStorage.getItem('civicpulse_theme') || 'dark',
  sectors: [],
  complaints: [],
  demands: []
};

// ==============================================================================
// 3. INITIALIZATION
// ==============================================================================
// 3. INITIALIZATION
// ==============================================================================
document.addEventListener('DOMContentLoaded', async () => {
  initTheme();
  loadUserProfile();
  if (window.initLanguage) window.initLanguage();
  setupEventListeners();
  await loadBRICSContext();
  await loadSectors();
  
  // Initialize subsystems
  if (window.initCitizenPortal) window.initCitizenPortal();
  if (window.initGovernmentHub) {
    window.initGovernmentHub();
    // Auto-load government data on dedicated government hub or if gov elements are present
    if (document.getElementById('gov-tab-megaplan')) {
      if (window.loadGovernmentData) window.loadGovernmentData();
    }
  }
});

// ==============================================================================
// 4. USER PROFILE & THEME ENGINE
// ==============================================================================
function loadUserProfile() {
  try {
    const userJson = localStorage.getItem('civicpulse_user');
    if (userJson) {
      const user = JSON.parse(userJson);
      const nameEl = document.getElementById('user-display-name');
      const roleEl = document.getElementById('user-display-role');
      const avatarEl = document.querySelector('.user-profile-avatar');
      
      if (nameEl && user.name) nameEl.textContent = user.name;
      const welcomeNameEl = document.getElementById('home-welcome-name');
      if (welcomeNameEl && user.name) welcomeNameEl.textContent = `Welcome, ${user.name}`;
      if (roleEl) {
        roleEl.textContent = user.role === 'government' 
          ? 'Policy Directorate • Level-4' 
          : `Verified Citizen • ${AppState.activeCode || 'DL'}-8842`;
      }
      if (avatarEl && user.name) {
        const initials = user.name.split(' ').map(w => w[0]).filter(Boolean).slice(0, 2).join('').toUpperCase();
        avatarEl.textContent = initials || (user.role === 'government' ? 'DG' : 'P');
      }
    }
  } catch (err) {
    console.warn('Could not load user profile from session:', err);
  }
}

function initTheme() {
  document.documentElement.setAttribute('data-theme', AppState.theme);
  updateThemeIcon();
}

function toggleTheme() {
  AppState.theme = AppState.theme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', AppState.theme);
  localStorage.setItem('civicpulse_theme', AppState.theme);
  updateThemeIcon();
}

function updateThemeIcon() {
  const icon = document.getElementById('theme-icon');
  if (icon) {
    icon.innerHTML = AppState.theme === 'dark' ? window.AppIcons.sun : window.AppIcons.moon;
  }
}

// ==============================================================================
// 5. EVENT LISTENERS SETUP
// ==============================================================================
function setupEventListeners() {
  // Theme Toggle
  const themeBtn = document.getElementById('theme-toggle');
  if (themeBtn) themeBtn.addEventListener('click', toggleTheme);

  // Logout / Sign Out Button
  const logoutBtn = document.getElementById('btn-logout');
  if (logoutBtn) {
    logoutBtn.addEventListener('click', () => {
      localStorage.removeItem('civicpulse_user');
      localStorage.removeItem('civicpulse_token');
      window.location.href = '/login';
    });
  }

  // Role Switcher Buttons (for index.html fallback)
  const btnCit = document.getElementById('btn-role-citizen');
  const btnGov = document.getElementById('btn-role-gov');

  if (btnCit && btnGov) {
    btnCit.addEventListener('click', () => switchRole('citizen'));
    btnGov.addEventListener('click', () => switchRole('gov'));
  }

  // BRICS Node Selector
  const nodeSelector = document.getElementById('node-selector');
  if (nodeSelector) {
    nodeSelector.addEventListener('change', async (e) => {
      await switchBRICSNode(e.target.value);
    });
  }

  // Global Navigation History & State
  window.navHistory = window.navHistory || [];
  window.currentTabId = window.currentTabId || (document.getElementById('gov-tab-home') ? 'gov-tab-home' : 'cit-tab-home');

  // Global Tab Switcher Function with History Tracking
  window.switchTab = function(targetId, isBack = false) {
    if (!targetId) return;
    const activeTab = document.getElementById(targetId);
    if (!activeTab) return;

    // Track navigation history if moving to a new tab forward
    if (!isBack && window.currentTabId && window.currentTabId !== targetId) {
      window.navHistory.push(window.currentTabId);
    }
    window.currentTabId = targetId;

    // Find associated tab navigation link if present
    const targetLink = document.querySelector(`.tab-link[data-target="${targetId}"]`);
    if (targetLink) {
      const parentNav = targetLink.closest('.tab-nav');
      if (parentNav) {
        parentNav.querySelectorAll('.tab-link').forEach(l => l.classList.remove('active'));
        targetLink.classList.add('active');
      }
    }

    // Hide all tab contents in the active container
    const container = activeTab.closest('#citizen-viewport, #government-viewport') || activeTab.parentElement || document;
    container.querySelectorAll('.tab-content').forEach(tc => tc.style.display = 'none');
    
    // Show active tab
    activeTab.style.display = 'block';

    // Trigger map resize if GIS map tab is activated
    if (targetId === 'gov-tab-map' && window.govMap) {
      setTimeout(() => window.govMap.invalidateSize(), 250);
    }

    // Smooth scroll to top of page / view
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Global Navbar "Home" Action
  window.navGoHome = function() {
    // 1. Close any open dialogs/modals
    const incidentModal = document.getElementById('incident-modal');
    if (incidentModal) incidentModal.classList.remove('active');
    const demandModal = document.getElementById('demand-modal');
    if (demandModal) demandModal.classList.remove('active');

    // 2. Identify the home tab for the current portal
    let homeTabId = 'cit-tab-home';
    if (document.getElementById('city-tab-home')) {
      homeTabId = 'city-tab-home';
    } else if (document.getElementById('central-tab-home')) {
      homeTabId = 'central-tab-home';
    } else if (document.getElementById('gov-tab-home') && !document.getElementById('cit-tab-home')) {
      homeTabId = 'gov-tab-home';
    } else if (window.AppState && window.AppState.currentRole === 'government') {
      homeTabId = 'gov-tab-home';
    }

    // 3. Switch to Home or scroll to top if already there
    if (window.currentTabId !== homeTabId && document.getElementById(homeTabId)) {
      window.switchTab(homeTabId);
    } else {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  // Global Navbar "Back" Action
  window.navGoBack = function() {
    // 1. If incident modal is open, closing it is the natural back step
    const incidentModal = document.getElementById('incident-modal');
    if (incidentModal && incidentModal.classList.contains('active')) {
      incidentModal.classList.remove('active');
      return;
    }

    // 2. If demand proposal modal is open, close it
    const demandModal = document.getElementById('demand-modal');
    if (demandModal && demandModal.classList.contains('active')) {
      demandModal.classList.remove('active');
      return;
    }

    // 3. Check internal navigation history stack
    if (window.navHistory && window.navHistory.length > 0) {
      const prevTabId = window.navHistory.pop();
      if (prevTabId && document.getElementById(prevTabId)) {
        window.switchTab(prevTabId, true);
        return;
      }
    }

    // 4. If on a sub-service tab without history, return to portal Home
    let homeTabId = 'cit-tab-home';
    if (document.getElementById('city-tab-home')) {
      homeTabId = 'city-tab-home';
    } else if (document.getElementById('central-tab-home')) {
      homeTabId = 'central-tab-home';
    } else if (document.getElementById('gov-tab-home') && !document.getElementById('cit-tab-home')) {
      homeTabId = 'gov-tab-home';
    } else if (window.AppState && window.AppState.currentRole === 'government') {
      homeTabId = 'gov-tab-home';
    }

    if (window.currentTabId && window.currentTabId !== homeTabId && document.getElementById(homeTabId)) {

      window.switchTab(homeTabId, true);
      return;
    }

    // 5. If already on Home, navigate browser back
    if (window.history && window.history.length > 1) {
      window.history.back();
    } else {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  // Keyboard shortcut listener: Alt+Left for Back, Alt+Home for Home
  window.addEventListener('keydown', (e) => {
    if (e.altKey && e.key === 'ArrowLeft') {
      e.preventDefault();
      window.navGoBack();
    } else if (e.altKey && e.key === 'Home') {
      e.preventDefault();
      window.navGoHome();
    }
  });

  // Generic Tab Navigation button click
  document.querySelectorAll('.tab-link').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const targetId = e.currentTarget.getAttribute('data-target');
      window.switchTab(targetId);
    });
  });

  // Global handler for Home Page Launchpad cards & buttons (data-open-tab)
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-open-tab]');
    if (trigger) {
      e.preventDefault();
      const targetId = trigger.getAttribute('data-open-tab');
      window.switchTab(targetId);
    }
  });
}

// ==============================================================================
// 6. ROLE SWITCHING (CITIZEN VS GOVERNMENT)
// ==============================================================================
function switchRole(role) {
  AppState.currentRole = role;
  const citViewport = document.getElementById('citizen-viewport');
  const govViewport = document.getElementById('government-viewport');
  const btnCit = document.getElementById('btn-role-citizen');
  const btnGov = document.getElementById('btn-role-gov');

  if (role === 'citizen') {
    btnCit.classList.add('active');
    btnGov.classList.remove('active');
    citViewport.style.display = 'block';
    govViewport.style.display = 'none';
  } else {
    btnGov.classList.add('active');
    btnCit.classList.remove('active');
    govViewport.style.display = 'block';
    citViewport.style.display = 'none';
    if (window.loadGovernmentData) window.loadGovernmentData();
  }
}

// ==============================================================================
// 7. BRICS NODE AUTO-DETECTION & DYNAMIC SOVEREIGN THEMING
// ==============================================================================
function autoDetectNode(defaultCode = 'IN') {
  try {
    // 1. Check authenticated user profile in localStorage
    const userJson = localStorage.getItem('civicpulse_user');
    if (userJson) {
      const user = JSON.parse(userJson);
      if (user.node && ['IN', 'BR', 'ZA'].includes(user.node.toUpperCase())) {
        return user.node.toUpperCase();
      }
      if (user.country) {
        const c = user.country.toLowerCase();
        if (c.includes('brazil') || c.includes('brasil')) return 'BR';
        if (c.includes('south africa') || c.includes('afrika')) return 'ZA';
        if (c.includes('india') || c.includes('bharat')) return 'IN';
      }
      if (user.email) {
        const em = user.email.toLowerCase();
        if (em.includes('.br') || em.includes('sp.') || em.includes('brazil')) return 'BR';
        if (em.includes('.za') || em.includes('joburg') || em.includes('sa.')) return 'ZA';
        if (em.includes('.in') || em.includes('delhi') || em.includes('nic.in') || em.includes('gov.in')) return 'IN';
      }
    }

    // 2. Check explicitly stored session preference
    const savedNode = localStorage.getItem('civicpulse_active_node');
    if (savedNode && ['IN', 'BR', 'ZA'].includes(savedNode.toUpperCase())) {
      return savedNode.toUpperCase();
    }

    // 3. Fallback to browser timezone / locale
    const tz = (Intl && Intl.DateTimeFormat) ? Intl.DateTimeFormat().resolvedOptions().timeZone : '';
    if (tz) {
      const tzl = tz.toLowerCase();
      if (tzl.includes('sao_paulo') || tzl.includes('brazil') || tzl.includes('fortaleza') || tzl.includes('belem')) return 'BR';
      if (tzl.includes('johannesburg') || tzl.includes('pretoria') || tzl.includes('africa')) return 'ZA';
      if (tzl.includes('calcutta') || tzl.includes('kolkata') || tzl.includes('delhi') || tzl.includes('india')) return 'IN';
    }
  } catch (e) {
    console.warn('Auto-detect node resolution notice:', e);
  }
  return defaultCode;
}

async function loadBRICSContext() {
  try {
    const res = await fetch('/api/brics/nodes');
    const data = await res.json();
    AppState.activeNode = data.active_node;
    AppState.activeCode = data.active_code || 'IN';

    // Auto-detect jurisdiction node without requiring manual user switching
    const detectedCode = autoDetectNode(AppState.activeCode);
    if (detectedCode && detectedCode !== AppState.activeCode) {
      await switchBRICSNode(detectedCode, true); // silent auto-align
      return;
    }

    updateHeaderBanner();
    populateWardSelectors();
  } catch (err) {
    console.error('Error loading BRICS nodes:', err);
  }
}

async function switchBRICSNode(code, silent = false) {
  try {
    const res = await fetch('/api/brics/switch', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code })
    });
    const data = await res.json();
    AppState.activeNode = data.active_node;
    AppState.activeCode = data.code;
    localStorage.setItem('civicpulse_active_node', data.code);
    updateHeaderBanner();
    populateWardSelectors();

    // Refresh citizen and government views for the new nation
    if (window.renderSectorCards) window.renderSectorCards();
    if (window.loadCitizenDemands) window.loadCitizenDemands();
    if (window.loadComplaints) window.loadComplaints();
    if (window.loadGovernmentData) window.loadGovernmentData();

    if (!silent) {
      showToast(`Switched to ${AppState.activeNode.country} DPI Sovereign Node`, 'info');
    }
  } catch (err) {
    console.error('Error switching BRICS node:', err);
  }
}

function updateHeaderBanner() {
  const node = AppState.activeNode;
  if (!node) return;

  // DYNAMICALLY APPLY SOVEREIGN NATION COLOR PALETTE TO DOM (RULE 04)
  document.documentElement.setAttribute('data-node', AppState.activeCode);

  // SVG Flag Vector rendering
  const flagContainer = document.getElementById('active-flag-container');
  const flagKey = `flag_${AppState.activeCode.toLowerCase()}`;
  if (flagContainer) {
    flagContainer.innerHTML = window.AppIcons[flagKey] || '';
  }

  const labelEl = document.getElementById('active-node-text');
  if (labelEl) {
    labelEl.textContent = `${node.country.toUpperCase()} DPI NODE`;
  }

  // Update Auto-Detected Jurisdiction Badge
  const nodeFlagEl = document.getElementById('node-detected-flag');
  const nodeLabelEl = document.getElementById('node-detected-label');
  if (nodeFlagEl) {
    const flagEmojis = { IN: '🇮🇳', BR: '🇧🇷', ZA: '🇿🇦' };
    nodeFlagEl.textContent = flagEmojis[AppState.activeCode] || '🌐';
  }
  if (nodeLabelEl) {
    const cityLabels = {
      IN: 'India (Delhi NCR)',
      BR: 'Brazil (São Paulo)',
      ZA: 'South Africa (Johannesburg)'
    };
    nodeLabelEl.textContent = cityLabels[AppState.activeCode] || `${node.country} Node`;
  }

  const tag = document.getElementById('hero-jurisdiction-tag');
  if (tag) tag.textContent = `${node.framework.toUpperCase()}`;

  const kpiBudget = document.getElementById('kpi-budget');
  if (kpiBudget) kpiBudget.textContent = `${node.currency_symbol} ${node.total_capex_budget.toLocaleString()} ${node.unit}`;

  const selector = document.getElementById('node-selector');
  if (selector && selector.value !== AppState.activeCode) {
    selector.value = AppState.activeCode;
  }
}

function populateWardSelectors() {
  const wards = AppState.activeNode?.wards || [];
  const complaintWardSelect = document.getElementById('complaint-ward-select');
  const modalDemandWard = document.getElementById('modal-demand-ward');
  const demandFilterWard = document.getElementById('demand-filter-ward');

  const optionsHtml = wards.map(w => `<option value="${w.name}">${w.name}</option>`).join('');

  if (complaintWardSelect) complaintWardSelect.innerHTML = optionsHtml;
  if (modalDemandWard) modalDemandWard.innerHTML = optionsHtml;
  if (demandFilterWard) {
    demandFilterWard.innerHTML = '<option value="All Wards">All Sub-Districts / Wards</option>' + optionsHtml;
  }
}

async function loadSectors() {
  try {
    const res = await fetch('/api/sectors');
    AppState.sectors = await res.json();
    if (window.renderSectorCards) window.renderSectorCards();
  } catch (err) {
    console.error('Error loading sectors:', err);
  }
}

// Toast notification helper
function showToast(message, type = 'info') {
  const toast = document.createElement('div');
  toast.style.position = 'fixed';
  toast.style.bottom = '24px';
  toast.style.right = '24px';
  toast.style.background = type === 'success' ? '#059669' : (type === 'error' ? '#dc2626' : 'var(--accent-primary)');
  toast.style.color = '#ffffff';
  toast.style.padding = '12px 20px';
  toast.style.borderRadius = '10px';
  toast.style.boxShadow = '0 10px 30px rgba(0,0,0,0.5)';
  toast.style.fontSize = '0.9rem';
  toast.style.fontWeight = '700';
  toast.style.zIndex = '9999';
  toast.style.transition = 'all 0.3s ease';
  toast.style.display = 'flex';
  toast.style.alignItems = 'center';
  toast.style.gap = '8px';
  toast.innerHTML = `<span>${type === 'success' ? window.AppIcons.check : window.AppIcons.zap}</span><span>${message}</span>`;
  document.body.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}
