/**
 * CIVICPULSE-BRICS: SOVEREIGN INTERNATIONALIZATION (i18n) ENGINE
 * Comprehensive Multi-Engine Translations for All 23 BRICS & Indian Sovereign Languages:
 * English (en), Hindi (hi), Portuguese (pt), Russian (ru), Mandarin (zh),
 * Tamil (ta), Telugu (te), isiZulu (zu), Afrikaans (af),
 * Arabic (ar), Indonesian (id), Persian (fa), Amharic (am), isiXhosa (xh),
 * Bengali (bn), Marathi (mr), Gujarati (gu), Kannada (kn),
 * Malayalam (ml), Punjabi (pa), Odia (or), Assamese (as), Urdu (ur).
 */

window.I18N = {};

/**
 * Universal translation getter with multi-level fallback
 */
window.getTranslation = function(keyOrText, fallback) {
  if (!keyOrText) return fallback || '';
  const lang = localStorage.getItem('civicpulse_lang') || 'en';
  const dict = (window.I18N && window.I18N[lang]) || (window.I18N && window.I18N['en']) || {};
  const phraseDict = (window.I18N_PHRASES && window.I18N_PHRASES[lang]) || {};
  const enDict = (window.I18N && window.I18N['en']) || {};
  const enPhraseDict = (window.I18N_PHRASES && window.I18N_PHRASES['en']) || {};

  // 1. Check exact key in dictionary
  if (dict[keyOrText] !== undefined) return dict[keyOrText];

  // 2. Check exact text in phrase map
  const clean = String(keyOrText).trim();
  if (phraseDict[clean] !== undefined) return phraseDict[clean];

  // 3. Fallback to EN key
  if (enDict[keyOrText] !== undefined) return enDict[keyOrText];

  // 4. Fallback to EN phrase map
  if (enPhraseDict[clean] !== undefined) return enPhraseDict[clean];

  return fallback !== undefined ? fallback : keyOrText;
};
window.i18n = window.getTranslation;
window.t = window.getTranslation;

/**
 * Clean punctuation helpers
 */
function cleanPunctuation(str) {
  if (!str) return '';
  return str.replace(/^[•\s\.,:%/+\-→←●|()#*⚡🇮🇳🏛️📍📱🔄▼▲]+/, '')
            .replace(/[•\s\.,:%/+\-→←●|()#*▼▲]+$/, '')
            .trim();
}

/**
 * Deep recursive DOM text translator with TreeWalker architecture
 */
window.translateDOM = function(root) {
  const lang = localStorage.getItem('civicpulse_lang') || 'en';
  const dict = (window.I18N && window.I18N[lang]) || (window.I18N && window.I18N['en']) || {};
  const phraseDict = (window.I18N_PHRASES && window.I18N_PHRASES[lang]) || {};
  const fallbackDict = (window.I18N && window.I18N['en']) || {};

  const target = root || document.body;
  if (!target) return;

  // 1. Elements with data-i18n
  target.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    const val = dict[key] || fallbackDict[key] || phraseDict[key];
    if (val !== undefined && val !== null) {
      el.textContent = val;
    }
  });

  // 2. Elements with data-i18n-placeholder
  target.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    const val = dict[key] || fallbackDict[key] || phraseDict[key];
    if (val !== undefined && val !== null) {
      el.setAttribute('placeholder', val);
    }
  });

  // 3. Elements with data-i18n-title
  target.querySelectorAll('[data-i18n-title]').forEach(el => {
    const key = el.getAttribute('data-i18n-title');
    const val = dict[key] || fallbackDict[key] || phraseDict[key];
    if (val !== undefined && val !== null) {
      el.setAttribute('title', val);
    }
  });

  // 4. TreeWalker over ALL text nodes for mixed-content & dynamic HTML
  const walker = document.createTreeWalker(
    target,
    NodeFilter.SHOW_TEXT,
    {
      acceptNode: function(node) {
        if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        const parent = node.parentElement;
        if (!parent) return NodeFilter.FILTER_REJECT;
        const tag = parent.tagName.toLowerCase();
        if (['script', 'style', 'select', 'option', 'textarea', 'code', 'pre'].includes(tag)) {
          return NodeFilter.FILTER_REJECT;
        }
        if (parent.closest('select') || parent.classList.contains('lang-select')) {
          return NodeFilter.FILTER_REJECT;
        }
        // If parent has data-i18n and NO child elements, data-i18n already handled it
        if (parent.hasAttribute('data-i18n') && parent.children.length === 0) {
          return NodeFilter.FILTER_REJECT;
        }
        return NodeFilter.FILTER_ACCEPT;
      }
    }
  );

  const textNodes = [];
  while (walker.nextNode()) {
    textNodes.push(walker.currentNode);
  }

  textNodes.forEach(node => {
    // Save original English string on first encounter
    if (!node.__civic_orig) {
      node.__civic_orig = node.nodeValue;
    }

    const origVal = node.__civic_orig;
    const trimmedOrig = origVal.trim();
    if (!trimmedOrig) return;

    // If English, smoothly restore original
    if (lang === 'en') {
      if (node.nodeValue !== origVal) {
        node.nodeValue = origVal;
      }
      return;
    }

    // Check exact match
    if (phraseDict[trimmedOrig]) {
      const match = phraseDict[trimmedOrig];
      node.nodeValue = origVal.replace(trimmedOrig, match);
      return;
    }

    // Check clean stripped match
    const cleanOrig = cleanPunctuation(trimmedOrig);
    if (cleanOrig && phraseDict[cleanOrig]) {
      const cleanMatch = phraseDict[cleanOrig];
      node.nodeValue = origVal.replace(cleanOrig, cleanMatch);
    }
  });
};

/**
 * GOOGLE TRANSLATE ENGINE SEAMLESS INTEGRATION (GNMT)
 */
const GOOGLE_LANG_MAP = {
  'en': 'en',
  'hi': 'hi',
  'pt': 'pt',
  'ru': 'ru',
  'zh': 'zh-CN',
  'ar': 'ar',
  'id': 'id',
  'fa': 'fa',
  'am': 'am',
  'xh': 'xh',
  'zu': 'zu',
  'af': 'af',
  'ta': 'ta',
  'te': 'te',
  'kn': 'kn',
  'ml': 'ml',
  'bn': 'bn',
  'mr': 'mr',
  'gu': 'gu',
  'pa': 'pa',
  'or': 'or',
  'as': 'as',
  'ur': 'ur'
};

window.googleTranslateElementInit = function() {
  try {
    if (window.google && window.google.translate) {
      new window.google.translate.TranslateElement({
        pageLanguage: 'en',
        includedLanguages: Object.values(GOOGLE_LANG_MAP).join(','),
        layout: window.google.translate.TranslateElement.InlineLayout.SIMPLE,
        autoDisplay: false
      }, 'google_translate_element');

      setTimeout(() => {
        const savedLang = localStorage.getItem('civicpulse_lang') || 'en';
        if (savedLang && savedLang !== 'en') {
          window.triggerGoogleTranslate(savedLang);
        }
      }, 300);
    }
  } catch (err) {
    console.warn('Google Translate initialization notice:', err);
  }
};

function ensureGoogleTranslateElements() {
  if (!document.getElementById('google_translate_element')) {
    const el = document.createElement('div');
    el.id = 'google_translate_element';
    el.style.display = 'none';
    document.body.appendChild(el);
  }
  if (!document.getElementById('google-translate-script')) {
    const s = document.createElement('script');
    s.id = 'google-translate-script';
    s.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
    s.async = true;
    document.head.appendChild(s);
  }
}

window.triggerGoogleTranslate = function(lang) {
  const gLang = GOOGLE_LANG_MAP[lang] || lang;
  const host = window.location.hostname;
  
  if (gLang === 'en') {
    document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
    document.cookie = `googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=${host};`;
    document.cookie = `googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=.${host};`;
    document.cookie = 'googtrans=/en/en; path=/;';
    const combo = document.querySelector('.goog-te-combo');
    if (combo) {
      combo.value = 'en';
      combo.dispatchEvent(new Event('change'));
    }
  } else {
    document.cookie = `googtrans=/en/${gLang}; path=/;`;
    document.cookie = `googtrans=/en/${gLang}; path=/; domain=${host};`;
    document.cookie = `googtrans=/en/${gLang}; path=/; domain=.${host};`;

    const combo = document.querySelector('.goog-te-combo');
    if (combo) {
      combo.value = gLang;
      combo.dispatchEvent(new Event('change'));
    } else {
      let attempts = 0;
      const poll = setInterval(() => {
        attempts++;
        const c = document.querySelector('.goog-te-combo');
        if (c) {
          clearInterval(poll);
          c.value = gLang;
          c.dispatchEvent(new Event('change'));
        } else if (attempts > 30) {
          clearInterval(poll);
        }
      }, 100);
    }
  }
};

/**
 * Global Language Switcher with Dual-Engine (Synchronous DOM + Google GNMT Engine)
 */
window.setLanguage = function(lang) {
  const previousLang = localStorage.getItem('civicpulse_lang') || 'en';
  if (!lang) lang = 'en';

  localStorage.setItem('civicpulse_lang', lang);
  document.documentElement.setAttribute('lang', lang);

  // Set RTL for Arabic, Persian, and Urdu
  if (lang === 'ar' || lang === 'fa' || lang === 'ur') {
    document.documentElement.setAttribute('dir', 'rtl');
  } else {
    document.documentElement.setAttribute('dir', 'ltr');
  }

  // Sync all language dropdowns
  document.querySelectorAll('#lang-selector, #login-lang-select, .lang-select').forEach(sel => {
    if (sel && sel.value !== lang) sel.value = lang;
  });

  // If reverting from non-English back to English:
  if (lang === 'en' && previousLang !== 'en') {
    window.triggerGoogleTranslate('en');
    setTimeout(() => {
      window.location.reload();
    }, 100);
    return;
  }

  // 1. Instant local synchronous pass
  if (typeof window.translateDOM === 'function') {
    window.translateDOM(document.body);
  }

  // 2. Trigger Google Translate engine for 100% full-page deep coverage!
  window.triggerGoogleTranslate(lang);

  // 3. Re-render Dynamic Components across all portals
  try { if (window.renderSectorCards && typeof window.renderSectorCards === 'function') window.renderSectorCards(); } catch(e) {}
  try { if (window.renderDemands && typeof window.renderDemands === 'function' && window.AppState && window.AppState.demands) window.renderDemands(window.AppState.demands); } catch(e) {}
  try { if (window.renderTrackedComplaints && typeof window.renderTrackedComplaints === 'function' && window.AppState && window.AppState.complaints) window.renderTrackedComplaints(window.AppState.complaints); } catch(e) {}
  try { if (window.refreshCityOfficialDashboard && typeof window.refreshCityOfficialDashboard === 'function') window.refreshCityOfficialDashboard(); } catch(e) {}
  try { if (window.loadCityComplaints && typeof window.loadCityComplaints === 'function') window.loadCityComplaints(); } catch(e) {}
  try { if (window.loadPeerProposals && typeof window.loadPeerProposals === 'function') window.loadPeerProposals(); } catch(e) {}
  try { if (window.refreshCentralDashboard && typeof window.refreshCentralDashboard === 'function') window.refreshCentralDashboard(); } catch(e) {}
  try { if (window.loadCentralOfficersOverview && typeof window.loadCentralOfficersOverview === 'function') window.loadCentralOfficersOverview(); } catch(e) {}
  try { if (window.loadCentralProposals && typeof window.loadCentralProposals === 'function') window.loadCentralProposals(); } catch(e) {}
  try { if (window.loadCentralMegaPlans && typeof window.loadCentralMegaPlans === 'function') window.loadCentralMegaPlans(); } catch(e) {}
  try { if (window.loadBricsIncomingRequests && typeof window.loadBricsIncomingRequests === 'function') window.loadBricsIncomingRequests(); } catch(e) {}
  try { if (window.renderMegaPlans && typeof window.renderMegaPlans === 'function' && window.AppState && window.AppState.megaPlans) window.renderMegaPlans(); } catch(e) {}
  try { if (window.renderBudgetTable && typeof window.renderBudgetTable === 'function' && window.AppState && window.AppState.budgetAlignment) window.renderBudgetTable(); } catch(e) {}

  // Trigger custom event for other modules
  window.dispatchEvent(new CustomEvent('civicpulse:languageChanged', { detail: { lang } }));
};

/**
 * Initialize language from storage or browser preference
 */
window.initLanguage = function() {
  ensureGoogleTranslateElements();
  const savedLang = localStorage.getItem('civicpulse_lang');
  let initialLang = savedLang;

  if (!initialLang) {
    const browserLang = (navigator.language || navigator.userLanguage || 'en').toLowerCase().split('-')[0];
    if (GOOGLE_LANG_MAP[browserLang]) {
      initialLang = browserLang;
    } else {
      initialLang = 'en';
    }
  }

  window.setLanguage(initialLang);

  // Setup change event listeners on all language dropdowns
  document.querySelectorAll('#lang-selector, #login-lang-select, .lang-select').forEach(sel => {
    if (sel) {
      sel.addEventListener('change', (e) => {
        window.setLanguage(e.target.value);
      });
    }
  });

  // Install dynamic DOM mutation observer to translate newly injected content
  try {
    let mutationTimer = null;
    const observer = new MutationObserver((mutations) => {
      const currentLang = localStorage.getItem('civicpulse_lang') || 'en';
      if (currentLang === 'en') return;
      clearTimeout(mutationTimer);
      mutationTimer = setTimeout(() => {
        if (typeof window.translateDOM === 'function') {
          window.translateDOM(document.body);
        }
      }, 60);
    });
    observer.observe(document.body, { childList: true, subtree: true });
  } catch(e) {}
};

// Auto-initialize language engine upon page readiness
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', window.initLanguage);
} else {
  window.initLanguage();
}
