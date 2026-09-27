import sys

with open('static/js/citizen.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hardcoded IDs in applyCoordinates
new_content = content.replace("getElementById('complaint-address-input')", "getElementById('complaint-address-input') || document.getElementById('modal-demand-address')")
new_content = new_content.replace("getElementById('complaint-ward-select')", "getElementById('complaint-ward-select') || document.getElementById('modal-demand-ward')")
new_content = new_content.replace("getElementById('location-detected-chip')", "getElementById('location-detected-chip') || document.getElementById('demand-location-detected-chip')")
new_content = new_content.replace("getElementById('location-chip-text')", "getElementById('location-chip-text') || document.getElementById('demand-location-chip-text')")
new_content = new_content.replace("getElementById('loc-btn-label')", "getElementById('loc-btn-label') || document.getElementById('demand-loc-btn-label')")
new_content = new_content.replace("getElementById('complaint-form')", "getElementById('complaint-form') || document.getElementById('propose-demand-form')")
new_content = new_content.replace("getElementById('btn-use-current-location')", "getElementById('btn-use-current-location') || document.getElementById('btn-demand-use-current-location')")
new_content = new_content.replace("getElementById('complaint-gps-address')", "getElementById('complaint-gps-address') || document.getElementById('modal-demand-gps-address')")

# toggleModalPinMap
new_content = new_content.replace("getElementById('modal-location-map-wrap')", "querySelector('.modal-box:not([style*=\"display: none\"]) #modal-location-map-wrap') || document.querySelector('.modal-box:not([style*=\"display: none\"]) #demand-modal-location-map-wrap') || document.getElementById('modal-location-map-wrap')")
new_content = new_content.replace("getElementById('btn-toggle-pin-map')", "querySelector('.modal-box:not([style*=\"display: none\"]) #btn-toggle-pin-map') || document.querySelector('.modal-box:not([style*=\"display: none\"]) #btn-demand-toggle-pin-map') || document.getElementById('btn-toggle-pin-map')")
new_content = new_content.replace("getElementById('pin-map-btn-label')", "querySelector('.modal-box:not([style*=\"display: none\"]) #pin-map-btn-label') || document.querySelector('.modal-box:not([style*=\"display: none\"]) #demand-pin-map-btn-label') || document.getElementById('pin-map-btn-label')")

# initModalPinMap
new_content = new_content.replace("getElementById('modal-pin-map')", "querySelector('.modal-box:not([style*=\"display: none\"]) #modal-pin-map') || document.querySelector('.modal-box:not([style*=\"display: none\"]) #demand-modal-pin-map') || document.getElementById('modal-pin-map')")

with open('static/js/citizen.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Updated citizen.js IDs')
