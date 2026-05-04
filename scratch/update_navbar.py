import os
import re

files_to_update = [
    "index.html", "about.html", "services.html", "projects.html", "calculator.html",
    "solar-subsidy.html", "areas.html", "contact.html", "industrial-solar.html",
    "residential-solar.html", "solar-panel-baner-bavdhan.html",
    "solar-panel-bhosari-pcmc.html", "solar-panel-chakan.html",
    "solar-panel-kiwale.html", "solar-panel-lonavala.html",
    "solar-panel-pimpri-chinchwad.html", "solar-panel-pune.html"
]

new_nav_item = '                <li><a href="/solar-guide">Solar 101</a></li>\n'
new_mobile_item = '                    <li><a href="/solar-guide">Solar 101</a></li>\n'

for filename in files_to_update:
    if not os.path.exists(filename):
        print(f"Skipping {filename}, not found.")
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already added
    if 'href="/solar-guide"' in content:
        print(f"Skipping {filename}, already has Solar 101.")
        continue

    # Update desktop nav
    # Find <li><a href="/">Home</a></li> and insert after
    content = re.sub(r'(<li><a href="/">Home</a></li>)', r'\1\n' + new_nav_item.strip(), content)
    
    # Update mobile nav
    content = re.sub(r'(<ul class="mobile-nav-links">\s*<li><a href="/">Home</a></li>)', r'\1\n' + new_mobile_item.strip(), content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")
