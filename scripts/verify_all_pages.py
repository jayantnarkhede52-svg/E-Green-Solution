import urllib.request
import re
import sys

routes_to_test = [
    # Homepage
    '/',
    
    # Category 1: Services (13 pages)
    '/services',
    '/residential-solar',
    '/commercial-solar-pune',
    '/industrial-solar',
    '/solar-water-heater-pune',
    '/solar-panel-cleaning-pune',
    '/solar-amc-pune',
    '/solar-inverter-repair-pune',
    '/solar-net-meter-msedcl-pune',
    '/solar-plant-revamping-repowering',
    '/solar-repair-maintenance-pune',
    '/solar-subsidy',
    '/solar-guide',

    # Category 2: Projects Showcase (3 pages)
    '/projects',
    '/projects/eagle-burgmann-200kw-solar-pune',
    '/projects/konark-a-plus-100kw-housing-society-solar-pune',

    # Category 3: Service Areas (8 pages)
    '/areas',
    '/solar-panel-pune',
    '/solar-panel-pimpri-chinchwad',
    '/solar-panel-baner-bavdhan',
    '/solar-panel-chakan',
    '/solar-panel-bhosari-pcmc',
    '/solar-panel-kiwale',
    '/solar-panel-lonavala',

    # Category 4: Blog Hub & Articles (10 pages)
    '/blog',
    '/blog/3kw-vs-5kw-solar-price-pune-subsidy',
    '/blog/bifacial-solar-panels-pune',
    '/blog/dcr-solar-panels-pune',
    '/blog/elevated-rooftop-solar-structure-pune',
    '/blog/enphase-microinverter-installers-pune',
    '/blog/housing-society-solar-pune-rules-subsidy',
    '/blog/hybrid-solar-system-lithium-battery-pune',
    '/blog/mono-perc-vs-topcon-solar-pune',
    '/blog/on-grid-solar-inverter-dealers-pune',

    # Category 5: Core & Utilities (5 pages)
    '/calculator',
    '/about',
    '/contact',
    '/privacy-policy',
    '/admin/login.html'
]

print(f"==================================================")
print(f"VERIFYING ENTIRE WEBSITE: {len(routes_to_test)} ROUTES")
print(f"==================================================")

passed = 0
failed = 0

for route in routes_to_test:
    url = f"http://localhost:3002{route}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 AuditBot/2.0'})
        res = urllib.request.urlopen(req, timeout=10)
        body = res.read().decode('utf-8', errors='ignore')
        
        # Quality assertions
        status_ok = (res.status == 200)
        has_title = bool(re.search(r'<title>(.*?)</title>', body, re.IGNORECASE))
        has_nav = ('id="dt-navbar"' in body) or ('admin' in route)
        has_footer = ('id="dt-footer"' in body) or ('admin' in route)
        has_dark_tokens = ('var(--bg-primary)' in body) or ('--bg-primary' in body) or ('dark-technical' in body) or ('#0B0D12' in body) or ('admin' in route)
        length_ok = (len(body) > 10000)

        if status_ok and has_title and has_nav and has_footer and length_ok:
            passed += 1
            print(f"[PASS] {route:<50} (Status: 200, Len: {len(body):>6} bytes)")
        else:
            failed += 1
            print(f"[FAIL] {route:<50} (status: {res.status}, nav: {has_nav}, footer: {has_footer}, len: {len(body)})")
    except Exception as e:
        failed += 1
        print(f"[ERROR] {route:<50} Exception: {e}")

print(f"==================================================")
print(f"AUDIT SUMMARY: {passed} PASSED / {failed} FAILED (TOTAL {len(routes_to_test)})")
print(f"==================================================")

if failed > 0:
    sys.exit(1)
