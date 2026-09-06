/**
 * CIVICPULSE-BRICS: SOVEREIGN LOGIN & AUTHENTICATION CONTROLLER
 * Handles Role Selection, 1-Click Quick Demo Access, Sovereign BRICS Nodes, and Dedicated Portal Routing
 */

document.addEventListener('DOMContentLoaded', async () => {
  initLoginTheme();
  await loadLoginBRICSContext();
  setupLoginEvents();
});

// ==============================================================================
// 1. THEME ENGINE FOR LOGIN
// ==============================================================================
function initLoginTheme() {
  const savedTheme = localStorage.getItem('civicpulse_theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateLoginThemeIcon(savedTheme);

  const themeBtn = document.getElementById('login-theme-toggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'dark';
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('civicpulse_theme', next);
      updateLoginThemeIcon(next);
    });
  }
}

function updateLoginThemeIcon(theme) {
  const icon = document.getElementById('login-theme-icon');
  if (icon) {
    icon.innerHTML = theme === 'dark' 
      ? `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>`
      : `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>`;
  }
}

// ==============================================================================
// 2. BRICS NODE INITIALIZATION & SWITCHING
// ==============================================================================
let currentLoginNodeCode = 'IN';

async function loadLoginBRICSContext() {
  try {
    const res = await fetch('/api/brics/nodes');
    const data = await res.json();
    currentLoginNodeCode = data.active_code || 'IN';
    updateLoginNodeUI(currentLoginNodeCode);
  } catch (err) {
    console.error('Error loading BRICS nodes on login:', err);
  }
}

function updateLoginNodeUI(code) {
  document.documentElement.setAttribute('data-node', code);
  
  const selector = document.getElementById('login-node-select');
  if (selector && selector.value !== code) {
    selector.value = code;
  }

  // Update Flag
  const flagContainer = document.getElementById('login-flag-container');
  if (flagContainer && window.AppIcons) {
    const flagKey = `flag_${code.toLowerCase()}`;
    flagContainer.innerHTML = window.AppIcons[flagKey] || '';
  }
}

async function switchLoginNode(code) {
  try {
    const res = await fetch('/api/brics/switch', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code })
    });
    const data = await res.json();
    currentLoginNodeCode = data.code;
    updateLoginNodeUI(data.code);
  } catch (err) {
    console.error('Error switching node on login:', err);
  }
}

// ==============================================================================
// 3. EVENT HANDLERS & AUTH FLOW
// ==============================================================================
function setupLoginEvents() {
  // Node selector change
  const selector = document.getElementById('login-node-select');
  if (selector) {
    selector.addEventListener('change', (e) => {
      switchLoginNode(e.target.value);
    });
  }

  // 1. Citizen Login Form Submit
  const citForm = document.getElementById('citizen-login-form');
  if (citForm) {
    citForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('citizen-email').value.trim();
      const password = document.getElementById('citizen-password').value;
      performLogin({
        role: 'citizen',
        email: email,
        password: password,
        name: 'Priya Sharma (Verified Resident)',
        node: currentLoginNodeCode
      });
    });
  }

  // Citizen 1-Click Fast Demo
  const btnDemoCitizen = document.getElementById('btn-demo-citizen');
  if (btnDemoCitizen) {
    btnDemoCitizen.addEventListener('click', () => {
      performLogin({
        role: 'citizen',
        name: 'Priya Sharma (Verified Resident)',
        email: 'priya.sharma@delhi.gov.in',
        node: currentLoginNodeCode
      });
    });
  }

  // 2. City Official Login Form Submit
  const cityForm = document.getElementById('city-login-form');
  if (cityForm) {
    cityForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('city-email').value.trim();
      const password = document.getElementById('city-password').value;
      performLogin({
        role: 'city_official',
        email: email,
        password: password,
        name: 'Er. Vikram Sharma (Chief Municipal Engineer)',
        node: currentLoginNodeCode
      });
    });
  }

  // City Official 1-Click Fast Demo
  const btnDemoCity = document.getElementById('btn-demo-city');
  if (btnDemoCity) {
    btnDemoCity.addEventListener('click', () => {
      performLogin({
        role: 'city_official',
        name: 'Er. Vikram Sharma (Chief Municipal Engineer)',
        email: 'vikram.sharma@delhi.gov.in',
        node: currentLoginNodeCode
      });
    });
  }

  // 3. Central Official Government Hub Login Form Submit
  const govForm = document.getElementById('gov-login-form');
  if (govForm) {
    govForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('gov-email').value.trim();
      const password = document.getElementById('gov-password').value;
      performLogin({
        role: 'central_official',
        email: email,
        password: password,
        name: 'Dr. Rajesh Verma (Director General, Infrastructure & CapEx)',
        node: currentLoginNodeCode
      });
    });
  }

  // Central Official 1-Click Fast Demo
  const btnDemoGov = document.getElementById('btn-demo-gov');
  if (btnDemoGov) {
    btnDemoGov.addEventListener('click', () => {
      performLogin({
        role: 'central_official',
        name: 'Dr. Rajesh Verma (Director General, Infrastructure & CapEx)',
        email: 'director.general@capex.brics.gov',
        node: currentLoginNodeCode
      });
    });
  }
}

// ==============================================================================
// 4. PERFORM LOGIN & ROUTING
// ==============================================================================
async function performLogin(credentials) {
  const submitBtns = document.querySelectorAll('.btn-portal-action, .btn-demo-quick');
  submitBtns.forEach(b => {
    b.disabled = true;
    b.dataset.origHtml = b.innerHTML;
    b.innerHTML = `<span>Authenticating...</span>`;
  });

  try {
    const res = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(credentials)
    });

    const data = await res.json();
    if (data.status === 'ok') {
      // Save session info
      localStorage.setItem('civicpulse_user', JSON.stringify(data.user));
      localStorage.setItem('civicpulse_token', data.token);
      localStorage.setItem('civicpulse_active_node', data.user?.node || currentLoginNodeCode);

      // Show brief feedback and redirect
      document.body.style.opacity = '0.85';
      window.location.href = data.redirect_url;
    } else {
      alert('Authentication failed. Please check your credentials.');
      submitBtns.forEach(b => {
        b.disabled = false;
        if (b.dataset.origHtml) b.innerHTML = b.dataset.origHtml;
      });
    }
  } catch (err) {
    console.error('Login error:', err);
    // Fallback direct redirection
    let target = '/citizen';
    if (credentials.role && credentials.role.includes('city')) target = '/city-official';
    else if (credentials.role && credentials.role.includes('central')) target = '/central-official';
    else if (credentials.role && credentials.role.includes('gov')) target = '/government';

    localStorage.setItem('civicpulse_user', JSON.stringify({
      name: credentials.name || (credentials.role.includes('city') ? 'Chief Municipal Engineer' : (credentials.role.includes('gov') || credentials.role.includes('central') ? 'Director General' : 'Citizen Member')),
      role: credentials.role,
      node: currentLoginNodeCode
    }));
    window.location.href = target;
  }
}
