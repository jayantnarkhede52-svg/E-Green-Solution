import os

files_to_update = [
    "index.html", "about.html", "services.html", "projects.html", "calculator.html",
    "solar-subsidy.html", "areas.html", "contact.html", "industrial-solar.html",
    "residential-solar.html", "solar-panel-baner-bavdhan.html",
    "solar-panel-bhosari-pcmc.html", "solar-panel-chakan.html",
    "solar-panel-kiwale.html", "solar-panel-lonavala.html",
    "solar-panel-pimpri-chinchwad.html", "solar-panel-pune.html"
]

target = '<li><a href="/solar-guide">Solar 101</a></li>\n<li><a href="/solar-guide">Solar 101</a></li>'
replacement = '<li><a href="/solar-guide">Solar 101</a></li>'

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target in content:
        content = content.replace(target, replacement)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filename}")
