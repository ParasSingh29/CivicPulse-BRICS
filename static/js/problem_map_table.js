/**
 * CivicPulse-BRICS: Global Problems Command Map, Country Telemetry Table & Filter Controller
 */

window.GlobalProblemMapSystem = {
  instances: {},
  complaintsData: [],
  countryStats: [],

  // Initialize or reload problem map & table for a given page section
  async init(config) {
    const {
      mapId,
      tableBodyId,
      countrySelectId,
      citySelectId,
      statusSelectId,
      searchInputId,
      counterBadgeId,
      countryTableBodyId
    } = config;

    // Load data if not already fetched
    if (!this.complaintsData.length) {
      await this.fetchComplaints();
    }

    // Populate country/city dropdowns
    this.populateFilterDropdowns(countrySelectId, citySelectId);

    // Render Country Table if requested
    if (countryTableBodyId) {
      await this.renderCountryTable(countryTableBodyId, countrySelectId);
    }

    // Render Map & Problems Table
    const mapEl = document.getElementById(mapId);
    if (!mapEl) return;

    // Destroy existing Leaflet map instance if re-initializing
    if (this.instances[mapId]) {
      try { this.instances[mapId].map.remove(); } catch(e) {}
      delete this.instances[mapId];
    }

    // Default center (New Delhi / BRICS overview)
    const map = L.map(mapId, {
      zoomControl: true,
      scrollWheelZoom: false
    }).setView([20.0, 45.0], 3);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; OpenStreetMap & CivicPulse-BRICS'
    }).addTo(map);

    const markersGroup = L.layerGroup().addTo(map);

    const instance = {
      map,
      markersGroup,
      markersMap: {},
      config
    };
    this.instances[mapId] = instance;

    // Setup event listeners for filters
    const updateHandler = () => {
      this.filterAndRender(mapId);
    };

    const countrySelect = document.getElementById(countrySelectId);
    const citySelect = document.getElementById(citySelectId);
    const statusSelect = document.getElementById(statusSelectId);
    const searchInput = document.getElementById(searchInputId);

    if (countrySelect) countrySelect.addEventListener('change', updateHandler);
    if (citySelect) citySelect.addEventListener('change', updateHandler);
    if (statusSelect) statusSelect.addEventListener('change', updateHandler);
    if (searchInput) searchInput.addEventListener('input', updateHandler);

    // Initial render
    this.filterAndRender(mapId);
  },

  async fetchComplaints() {
    try {
      const res = await fetch('/api/complaints');
      const data = await res.json();
      this.complaintsData = data.map(c => {
        const loc = c.location || {};
        const lat = parseFloat(loc.latitude || loc.lat || 28.6139);
        const lon = parseFloat(loc.longitude || loc.lon || 77.2090);
        const city = loc.city || this.detectCity(loc.address || c.description);
        const country = loc.country || this.detectCountry(city);
        const flag = loc.flag || this.getCountryFlag(country);
        return {
          ...c,
          lat,
          lon,
          city,
          country,
          flag,
          address: loc.address || c.description
        };
      });
    } catch(e) {
      console.error('Error fetching complaints:', e);
      this.complaintsData = [];
    }
  },

  detectCity(str) {
    if (!str) return 'Delhi';
    const s = str.toLowerCase();
    if (s.includes('são paulo') || s.includes('sao paulo') || s.includes('brazil')) return 'São Paulo';
    if (s.includes('moscow') || s.includes('russia')) return 'Moscow';
    if (s.includes('shanghai') || s.includes('china')) return 'Shanghai';
    if (s.includes('johannesburg') || s.includes('joburg') || s.includes('south africa')) return 'Johannesburg';
    if (s.includes('cairo') || s.includes('egypt')) return 'Cairo';
    if (s.includes('jakarta') || s.includes('indonesia')) return 'Jakarta';
    if (s.includes('dubai') || s.includes('uae')) return 'Dubai';
    if (s.includes('riyadh') || s.includes('saudi')) return 'Riyadh';
    if (s.includes('addis') || s.includes('ethiopia')) return 'Addis Ababa';
    if (s.includes('tehran') || s.includes('iran')) return 'Tehran';
    if (s.includes('mumbai')) return 'Mumbai';
    if (s.includes('bengaluru') || s.includes('bangalore')) return 'Bengaluru';
    return 'Delhi';
  },

  detectCountry(city) {
    const map = {
      'Delhi': 'India', 'Mumbai': 'India', 'Bengaluru': 'India',
      'São Paulo': 'Brazil', 'Moscow': 'Russia', 'Shanghai': 'China',
      'Johannesburg': 'South Africa', 'Cairo': 'Egypt', 'Jakarta': 'Indonesia',
      'Dubai': 'UAE', 'Riyadh': 'Saudi Arabia', 'Addis Ababa': 'Ethiopia', 'Tehran': 'Iran'
    };
    return map[city] || 'India';
  },

  getCountryFlag(country) {
    const flags = {
      'India': '🇮🇳', 'Brazil': '🇧🇷', 'Russia': '🇷🇺', 'China': '🇨🇳',
      'South Africa': '🇿🇦', 'Egypt': '🇪🇬', 'Indonesia': '🇮🇩', 'UAE': '🇦🇪',
      'Saudi Arabia': '🇸🇦', 'Ethiopia': '🇪🇹', 'Iran': '🇮🇷'
    };
    return flags[country] || '🌐';
  },

  populateFilterDropdowns(countrySelectId, citySelectId) {
    const countrySel = document.getElementById(countrySelectId);
    const citySel = document.getElementById(citySelectId);

    const countries = Array.from(new Set(this.complaintsData.map(c => c.country))).filter(Boolean).sort();
    const cities = Array.from(new Set(this.complaintsData.map(c => c.city))).filter(Boolean).sort();

    if (countrySel && countrySel.options.length <= 1) {
      countries.forEach(c => {
        const flag = this.getCountryFlag(c);
        const opt = document.createElement('option');
        opt.value = c;
        opt.textContent = `${flag} ${c}`;
        countrySel.appendChild(opt);
      });
    }

    if (citySel && citySel.options.length <= 1) {
      cities.forEach(c => {
        const opt = document.createElement('option');
        opt.value = c;
        opt.textContent = c;
        citySel.appendChild(opt);
      });
    }
  },

  filterAndRender(mapId) {
    const instance = this.instances[mapId];
    if (!instance) return;

    const { config, map, markersGroup } = instance;
    const countryVal = document.getElementById(config.countrySelectId)?.value || 'All';
    const cityVal = document.getElementById(config.citySelectId)?.value || 'All';
    const statusVal = document.getElementById(config.statusSelectId)?.value || 'All';
    const searchVal = (document.getElementById(config.searchInputId)?.value || '').toLowerCase().trim();

    const filtered = this.complaintsData.filter(c => {
      if (countryVal !== 'All' && c.country !== countryVal) return false;
      if (cityVal !== 'All' && c.city !== cityVal) return false;
      if (statusVal !== 'All') {
        const st = c.status.toLowerCase();
        if (statusVal === 'pending' && (!st.includes('pending') && !st.includes('critical') && st.includes('resolved'))) return false;
        if (statusVal === 'in_progress' && !st.includes('progress') && !st.includes('dispatch')) return false;
        if (statusVal === 'resolved' && !st.includes('resolved') && !st.includes('closed') && !st.includes('fixed')) return false;
      }
      if (searchVal) {
        const text = `${c.id} ${c.title || ''} ${c.category || ''} ${c.description || ''} ${c.address || ''} ${c.city} ${c.country}`.toLowerCase();
        if (!text.includes(searchVal)) return false;
      }
      return true;
    });

    // Update Counter Badge
    const counterBadge = document.getElementById(config.counterBadgeId);
    if (counterBadge) {
      const showTxt = window.getTranslation ? window.getTranslation('showing', 'Showing') : 'Showing';
      const ofTxt = window.getTranslation ? window.getTranslation('of', 'of') : 'of';
      const probTxt = window.getTranslation ? window.getTranslation('problems', 'Problems') : 'Problems';
      counterBadge.textContent = `${showTxt} ${filtered.length} ${ofTxt} ${this.complaintsData.length} ${probTxt}`;
    }

    // Clear map markers
    markersGroup.clearLayers();
    instance.markersMap = {};

    const bounds = [];

    filtered.forEach(c => {
      let markerColor = '#ef4444'; // Pending Red
      const st = c.status.toLowerCase();
      if (st.includes('progress') || st.includes('dispatch')) markerColor = '#f59e0b';
      else if (st.includes('resolved') || st.includes('closed') || st.includes('fixed')) markerColor = '#10b981';

      const customIcon = L.divIcon({
        className: 'custom-map-pin',
        html: `<div style="background-color:${markerColor}; width:14px; height:14px; border-radius:50%; border:2px solid #fff; box-shadow:0 0 8px ${markerColor};"></div>`,
        iconSize: [14, 14],
        iconAnchor: [7, 7]
      });

      const marker = L.marker([c.lat, c.lon], { icon: customIcon }).addTo(markersGroup);
      
      const popupHtml = `
        <div style="font-family:var(--font-sans); min-width:200px; color:#0f172a;">
          <div style="font-weight:700; font-size:0.9rem; margin-bottom:4px; color:#1e293b;">${c.flag} ${c.category || 'Infrastructure Report'}</div>
          <div style="font-size:0.8rem; color:#475569; margin-bottom:6px;">📍 ${c.city}, ${c.country}</div>
          <div style="font-size:0.8rem; color:#334155; margin-bottom:8px;">${c.description ? c.description.substring(0, 90) + '...' : ''}</div>
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:0.72rem; padding:2px 8px; border-radius:12px; font-weight:700; color:#fff; background:${markerColor};">
              ${c.status}
            </span>
            <span style="font-size:0.72rem; color:#64748b; font-family:var(--font-mono);">${c.id}</span>
          </div>
        </div>
      `;
      marker.bindPopup(popupHtml);
      instance.markersMap[c.id] = marker;
      bounds.push([c.lat, c.lon]);
    });

    if (bounds.length > 0 && map) {
      map.fitBounds(bounds, { padding: [30, 30], maxZoom: 13 });
    }

    // Render Data Table
    this.renderTable(config.tableBodyId, filtered, mapId);
  },

  renderTable(tableBodyId, list, mapId) {
    const tbody = document.getElementById(tableBodyId);
    if (!tbody) return;

    if (!list.length) {
      tbody.innerHTML = `
        <tr>
          <td colspan="5" style="text-align:center; padding:30px; color:var(--text-muted);">
            <div>🔍 No complaints found matching selected filters.</div>
          </td>
        </tr>
      `;
      return;
    }

    tbody.innerHTML = list.map(c => {
      let badgeStyle = 'background:rgba(239,68,68,0.12); color:#f87171; border:1px solid rgba(239,68,68,0.3);';
      const st = c.status.toLowerCase();
      if (st.includes('progress') || st.includes('dispatch')) {
        badgeStyle = 'background:rgba(245,158,11,0.12); color:#fbbf24; border:1px solid rgba(245,158,11,0.3);';
      } else if (st.includes('resolved') || st.includes('closed') || st.includes('fixed')) {
        badgeStyle = 'background:rgba(16,185,129,0.12); color:#34d399; border:1px solid rgba(16,185,129,0.3);';
      }

      return `
        <tr class="problem-row" style="cursor:pointer; border-bottom:1px solid var(--border-subtle); transition:background 0.2s;" onclick="GlobalProblemMapSystem.focusMap('${mapId}', '${c.id}', ${c.lat}, ${c.lon})">
          <td style="padding:10px 12px; font-size:0.8rem; font-family:var(--font-mono); color:var(--accent-primary);">
            ${c.flag} ${c.id.substring(0, 14)}
          </td>
          <td style="padding:10px 12px; font-size:0.82rem; font-weight:600; color:var(--text-primary);">
            <div>${c.city}</div>
            <div style="font-size:0.72rem; color:var(--text-muted); font-weight:400;">${c.country}</div>
          </td>
          <td style="padding:10px 12px; font-size:0.82rem; color:var(--text-secondary);">
            <div style="font-weight:600; color:var(--text-primary); margin-bottom:2px;">${c.category || 'General Report'}</div>
            <div style="font-size:0.75rem; color:var(--text-muted); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:220px;">
              ${c.description || c.address || ''}
            </div>
          </td>
          <td style="padding:10px 12px;">
            <span class="nav-badge" style="${badgeStyle} font-size:0.72rem; padding:3px 8px;">
              ${c.status}
            </span>
          </td>
          <td style="padding:10px 12px; text-align:right;">
            <button class="btn btn-sm btn-secondary" style="padding:3px 8px; font-size:0.72rem;" onclick="event.stopPropagation(); GlobalProblemMapSystem.focusMap('${mapId}', '${c.id}', ${c.lat}, ${c.lon})">
              🎯 Focus
            </button>
          </td>
        </tr>
      `;
    }).join('');
  },

  focusMap(mapId, complaintId, lat, lon) {
    const instance = this.instances[mapId];
    if (!instance) return;
    const { map, markersMap } = instance;
    if (map) {
      map.setView([lat, lon], 14, { animate: true });
      const marker = markersMap[complaintId];
      if (marker) {
        marker.openPopup();
      }
    }
  },

  async renderCountryTable(tableBodyId, countrySelectIdToSync) {
    const tbody = document.getElementById(tableBodyId);
    if (!tbody) return;

    try {
      const res = await fetch('/api/city-officers?country_code=ALL');
      const officers = await res.json();
      
      this.countryStats = officers;

      if (!officers.length) {
        tbody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:20px; color:var(--text-muted);">No country telemetry available.</td></tr>`;
        return;
      }

      tbody.innerHTML = officers.map(o => {
        let healthColor = '#10b981';
        if (o.health_index < 40) healthColor = '#ef4444';
        else if (o.health_index < 70) healthColor = '#f59e0b';

        return `
          <tr style="border-bottom:1px solid var(--border-subtle);">
            <td style="padding:12px; font-weight:700; color:var(--text-primary); font-size:0.9rem;">
              <span style="font-size:1.2rem; margin-right:6px;">${o.flag}</span> ${o.country}
            </td>
            <td style="padding:12px; font-size:0.85rem; color:var(--text-secondary);">
              📍 ${o.city}
            </td>
            <td style="padding:12px; font-weight:700; font-size:0.9rem; color:var(--text-primary); text-align:center;">
              ${o.total_problems}
            </td>
            <td style="padding:12px; font-weight:700; color:#ef4444; text-align:center;">
              ${o.red_problems}
            </td>
            <td style="padding:12px; font-weight:700; color:#f59e0b; text-align:center;">
              ${o.yellow_problems}
            </td>
            <td style="padding:12px; font-weight:700; color:#10b981; text-align:center;">
              ${o.green_problems}
            </td>
            <td style="padding:12px; text-align:center;">
              <span class="nav-badge" style="background:${healthColor}15; color:${healthColor}; border:1px solid ${healthColor}35; font-weight:700; font-size:0.8rem; padding:4px 10px;">
                ${o.health_index}%
              </span>
            </td>
            <td style="padding:12px; text-align:right;">
              <button class="btn btn-sm btn-outline" style="padding:4px 10px; font-size:0.75rem;" onclick="GlobalProblemMapSystem.filterByCountry('${countrySelectIdToSync}', '${o.country}')">
                🔍 Filter Map
              </button>
            </td>
          </tr>
        `;
      }).join('');
    } catch(e) {
      console.error('Error rendering country table:', e);
    }
  },

  filterByCountry(countrySelectId, countryName) {
    const sel = document.getElementById(countrySelectId);
    if (sel) {
      sel.value = countryName;
      sel.dispatchEvent(new Event('change'));
      // Scroll to map section smoothly
      const mapSection = sel.closest('section') || document.querySelector('.problem-map-table-section');
      if (mapSection) {
        mapSection.scrollIntoView({ behavior: 'smooth' });
      }
    }
  }
};
