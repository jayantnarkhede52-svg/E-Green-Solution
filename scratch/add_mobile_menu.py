import os

area_pages = [
    "solar-panel-pune.html", "solar-panel-chakan.html", "solar-panel-lonavala.html",
    "solar-panel-pimpri-chinchwad.html", "solar-panel-baner-bavdhan.html",
    "solar-panel-kiwale.html", "solar-panel-bhosari-pcmc.html", "solar-subsidy.html"
]

hamburger_and_mobile = """            <!-- Hamburger Menu for Mobile -->
            <div class="hamburger" id="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
            <!-- Mobile Menu -->
            <div class="mobile-menu" id="mobile-menu">
                <ul class="mobile-nav-links">
                    <li><a href="/">Home</a></li>
                    <li><a href="/solar-guide">Solar 101</a></li>
                    <li><a href="/services">Services</a></li>
                    <li><a href="/projects">Projects</a></li>
                    <li><a href="/calculator">Calculator</a></li>
                    <li><a href="/solar-subsidy">Subsidy</a></li>
                    <li><a href="/areas">Areas</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact" class="btn-contact-mobile">Contact Us</a></li>
                </ul>
            </div>"""

for filename in area_pages:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="hamburger"' in content:
        print(f"Skipping {filename}, already has hamburger.")
        continue

    # Insert after </ul> inside the nav-container
    content = content.replace('</ul>', '</ul>' + hamburger_and_mobile)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Added mobile menu to {filename}")
