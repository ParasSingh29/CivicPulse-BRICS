/**
 * CIVICPULSE-BRICS: SOVEREIGN LOGIN & AUTHENTICATION CONTROLLER
 * Handles Role Selection, 1-Click Quick Demo Access, Sovereign BRICS Nodes, and Dedicated Portal Routing
 */

document.addEventListener('DOMContentLoaded', async () => {
  initLoginTheme();
  await loadLoginBRICSContext();
  setupLoginEvents();
  initRoleSelectionFromURL();
});

// ==============================================================================
// 0. ROLE SELECTION & DESIGNATED PORTAL CONTROLLER
// ==============================================================================
window.selectLoginRole = function(role) {
  let normalizedRole = role || 'citizen';
  if (normalizedRole.includes('city')) normalizedRole = 'city';
  else if (normalizedRole.includes('gov') || normalizedRole.includes('central')) normalizedRole = 'gov';

  const roleStep = document.getElementById('role-selection-step');
  const designatedStep = document.getElementById('designated-login-step');

  if (roleStep && designatedStep) {
    roleStep.style.display = 'none';
    designatedStep.style.display = 'block';

    // Hide all portal cards
    const citCard = document.getElementById('citizen-login-card');
    const cityCard = document.getElementById('city-login-card');
    const govCard = document.getElementById('gov-login-card');

    if (citCard) citCard.style.display = 'none';
    if (cityCard) cityCard.style.display = 'none';
    if (govCard) govCard.style.display = 'none';

    // Show target card
    if (normalizedRole === 'citizen' && citCard) citCard.style.display = 'block';
    else if (normalizedRole === 'city' && cityCard) cityCard.style.display = 'block';
    else if (normalizedRole === 'gov' && govCard) govCard.style.display = 'block';

    // Update active tab buttons
    ['citizen', 'city', 'gov'].forEach(r => {
      const btn = document.getElementById(`tab-role-${r}`);
      if (btn) {
        if (r === normalizedRole) btn.classList.add('active');
        else btn.classList.remove('active');
      }
    });

    // Update URL query parameter
    try {
      const url = new URL(window.location);
      url.searchParams.set('role', normalizedRole);
      window.history.replaceState({}, '', url);
    } catch (e) {}
  }
};

window.showRoleSelectionScreen = function() {
  const roleStep = document.getElementById('role-selection-step');
  const designatedStep = document.getElementById('designated-login-step');

  if (roleStep && designatedStep) {
    designatedStep.style.display = 'none';
    roleStep.style.display = 'block';

    try {
      const url = new URL(window.location);
      url.searchParams.delete('role');
      window.history.replaceState({}, '', url);
    } catch (e) {}
  }
};

function initRoleSelectionFromURL() {
  const params = new URLSearchParams(window.location.search);
  const roleParam = params.get('role');
  if (roleParam) {
    window.selectLoginRole(roleParam);
  } else {
    window.showRoleSelectionScreen();
  }
}


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

window.switchAuthMode = function(role, mode) {
  const loginView = document.getElementById(`${role}-login-view`);
  const regView = document.getElementById(`${role}-register-view`);
  const loginBtn = document.getElementById(`btn-mode-login-${role}`);
  const regBtn = document.getElementById(`btn-mode-reg-${role}`);

  if (loginView && regView) {
    if (mode === 'register') {
      loginView.style.display = 'none';
      regView.style.display = 'block';
      if (loginBtn) loginBtn.classList.remove('active');
      if (regBtn) regBtn.classList.add('active');
    } else {
      regView.style.display = 'none';
      loginView.style.display = 'block';
      if (regBtn) regBtn.classList.remove('active');
      if (loginBtn) loginBtn.classList.add('active');
    }
  }
};

function showAuthError(message) {
  let errBox = document.getElementById('auth-error-banner');
  if (!errBox) {
    errBox = document.createElement('div');
    errBox.id = 'auth-error-banner';
    errBox.style.cssText = 'position:fixed; top:80px; left:50%; transform:translateX(-50%); z-index:99999; background:rgba(225,29,72,0.95); color:#ffffff; padding:12px 24px; border-radius:12px; font-weight:600; font-size:0.92rem; box-shadow:0 8px 32px rgba(225,29,72,0.5); border:1px solid rgba(255,255,255,0.25); text-align:center; max-width:90%; transition:all 0.3s ease;';
    document.body.appendChild(errBox);
  }
  errBox.innerHTML = `<span>⚠️ ${message}</span>`;
  errBox.style.display = 'block';
  setTimeout(() => {
    if (errBox) errBox.style.display = 'none';
  }, 5000);
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

  // --- 1. CITIZEN LOGIN & REGISTER ---
  const citForm = document.getElementById('citizen-login-form');
  if (citForm) {
    citForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('citizen-email').value.trim();
      const password = document.getElementById('citizen-password').value;
      if (!email || !password) {
        showAuthError('Please fill in both email and password.');
        return;
      }
      performLogin({
        role: 'citizen',
        email: email,
        password: password,
        is_demo: false,
        node: currentLoginNodeCode
      });
    });
  }

  const citRegForm = document.getElementById('citizen-register-form');
  if (citRegForm) {
    citRegForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('reg-citizen-name').value.trim();
      const email = document.getElementById('reg-citizen-email').value.trim();
      const phone = document.getElementById('reg-citizen-phone')?.value.trim() || '';
      const city = document.getElementById('reg-citizen-city')?.value.trim() || 'Delhi';
      const password = document.getElementById('reg-citizen-password').value;
      const confirmPass = document.getElementById('reg-citizen-confirm').value;

      if (password !== confirmPass) {
        showAuthError('Passwords do not match. Please re-enter.');
        return;
      }

      performRegister({
        role: 'citizen',
        name: name,
        email: email,
        phone: phone,
        city: city,
        password: password,
        node: currentLoginNodeCode
      });
    });
  }

  // Citizen 1-Click Fast Demo
  ['btn-demo-citizen', 'btn-demo-citizen-reg'].forEach(btnId => {
    const btn = document.getElementById(btnId);
    if (btn) {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        performLogin({
          role: 'citizen',
          name: 'Priya Sharma (Verified Resident)',
          email: 'priya.sharma@delhi.gov.in',
          is_demo: true,
          node: currentLoginNodeCode
        });
      });
    }
  });

  // --- 2. CITY OFFICIAL LOGIN & REGISTER ---
  const cityForm = document.getElementById('city-login-form');
  if (cityForm) {
    cityForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('city-email').value.trim();
      const password = document.getElementById('city-password').value;
      if (!email || !password) {
        showAuthError('Please fill in both email and password.');
        return;
      }
      performLogin({
        role: 'city_official',
        email: email,
        password: password,
        is_demo: false,
        node: currentLoginNodeCode
      });
    });
  }

  const cityRegForm = document.getElementById('city-register-form');
  if (cityRegForm) {
    cityRegForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('reg-city-name').value.trim();
      const email = document.getElementById('reg-city-email').value.trim();
      const dept = document.getElementById('reg-city-dept')?.value.trim() || 'Public Works Dept';
      const city = document.getElementById('reg-city-jurisdiction')?.value.trim() || 'Delhi';
      const password = document.getElementById('reg-city-password').value;
      const confirmPass = document.getElementById('reg-city-confirm').value;

      if (password !== confirmPass) {
        showAuthError('Passwords do not match. Please re-enter.');
        return;
      }

      performRegister({
        role: 'city_official',
        name: name,
        email: email,
        city: city,
        department: dept,
        password: password,
        node: currentLoginNodeCode
      });
    });
  }

  // City Official 1-Click Fast Demo
  ['btn-demo-city', 'btn-demo-city-reg'].forEach(btnId => {
    const btn = document.getElementById(btnId);
    if (btn) {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        performLogin({
          role: 'city_official',
          name: 'Er. Vikram Sharma (Chief Municipal Engineer)',
          email: 'vikram.sharma@delhi.gov.in',
          is_demo: true,
          node: currentLoginNodeCode
        });
      });
    }
  });

  // --- 3. CENTRAL OFFICIAL GOVERNMENT HUB LOGIN & REGISTER ---
  const govForm = document.getElementById('gov-login-form');
  if (govForm) {
    govForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('gov-email').value.trim();
      const password = document.getElementById('gov-password').value;
      if (!email || !password) {
        showAuthError('Please fill in both email and password.');
        return;
      }
      performLogin({
        role: 'central_official',
        email: email,
        password: password,
        is_demo: false,
        node: currentLoginNodeCode
      });
    });
  }

  const govRegForm = document.getElementById('gov-register-form');
  if (govRegForm) {
    govRegForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('reg-gov-name').value.trim();
      const email = document.getElementById('reg-gov-email').value.trim();
      const ministry = document.getElementById('reg-gov-ministry')?.value.trim() || 'Ministry of Urban Infrastructure';
      const password = document.getElementById('reg-gov-password').value;
      const confirmPass = document.getElementById('reg-gov-confirm').value;

      if (password !== confirmPass) {
        showAuthError('Passwords do not match. Please re-enter.');
        return;
      }

      performRegister({
        role: 'central_official',
        name: name,
        email: email,
        ministry: ministry,
        password: password,
        node: currentLoginNodeCode
      });
    });
  }

  // Central Official 1-Click Fast Demo
  ['btn-demo-gov', 'btn-demo-gov-reg'].forEach(btnId => {
    const btn = document.getElementById(btnId);
    if (btn) {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        performLogin({
          role: 'central_official',
          name: 'Dr. Rajesh Verma (Director General, Infrastructure & CapEx)',
          email: 'director.general@brics.gov',
          is_demo: true,
          node: currentLoginNodeCode
        });
      });
    }
  });
}

// ==============================================================================
// 4. PERFORM LOGIN & REGISTER ROUTING
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
    if (res.ok && data.status === 'ok') {
      // Save session info
      localStorage.setItem('civicpulse_user', JSON.stringify(data.user));
      localStorage.setItem('civicpulse_token', data.token);
      localStorage.setItem('civicpulse_active_node', data.user?.node || currentLoginNodeCode);

      const isGitHubPages = window.location.hostname.includes('github.io');
      let target = isGitHubPages ? 'static/pages/citizen.html' : '/citizen';

      if (data.redirect_url) {
        if (isGitHubPages) {
          if (data.redirect_url.includes('city')) target = 'static/pages/city_official.html';
          else if (data.redirect_url.includes('central')) target = 'static/pages/central_official.html';
          else if (data.redirect_url.includes('gov')) target = 'static/pages/government.html';
          else target = 'static/pages/citizen.html';
        } else {
          target = data.redirect_url;
        }
      }

      document.body.style.opacity = '0.85';
      window.location.href = target;
    } else {
      showAuthError(data.message || 'Invalid login credentials. Please check your email and password, or click Register Account.');
      submitBtns.forEach(b => {
        b.disabled = false;
        if (b.dataset.origHtml) b.innerHTML = b.dataset.origHtml;
      });
    }
  } catch (err) {
    console.error('Login error:', err);
    showAuthError('Connection error. Please try again.');
    submitBtns.forEach(b => {
      b.disabled = false;
      if (b.dataset.origHtml) b.innerHTML = b.dataset.origHtml;
    });
  }
}

async function performRegister(credentials) {
  const submitBtns = document.querySelectorAll('.btn-portal-action, .btn-demo-quick');
  submitBtns.forEach(b => {
    b.disabled = true;
    b.dataset.origHtml = b.innerHTML;
    b.innerHTML = `<span>Creating Account...</span>`;
  });

  try {
    const res = await fetch('/api/auth/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(credentials)
    });

    const data = await res.json();
    if (res.ok && data.status === 'ok') {
      localStorage.setItem('civicpulse_user', JSON.stringify(data.user));
      localStorage.setItem('civicpulse_token', data.token);
      localStorage.setItem('civicpulse_active_node', data.user?.node || currentLoginNodeCode);

      const isGitHubPages = window.location.hostname.includes('github.io');
      let target = isGitHubPages ? 'static/pages/citizen.html' : '/citizen';

      if (data.redirect_url) {
        if (isGitHubPages) {
          if (data.redirect_url.includes('city')) target = 'static/pages/city_official.html';
          else if (data.redirect_url.includes('central')) target = 'static/pages/central_official.html';
          else if (data.redirect_url.includes('gov')) target = 'static/pages/government.html';
          else target = 'static/pages/citizen.html';
        } else {
          target = data.redirect_url;
        }
      }

      document.body.style.opacity = '0.85';
      window.location.href = target;
    } else {
      showAuthError(data.message || 'Registration failed. Please try again.');
      submitBtns.forEach(b => {
        b.disabled = false;
        if (b.dataset.origHtml) b.innerHTML = b.dataset.origHtml;
      });
    }
  } catch (err) {
    console.error('Registration error:', err);
    showAuthError('Connection error during registration. Please try again.');
    submitBtns.forEach(b => {
      b.disabled = false;
      if (b.dataset.origHtml) b.innerHTML = b.dataset.origHtml;
    });
  }
}

