import os
import sys
import re

sys.path.append(os.path.abspath('scripts'))
from dark_theme_components import get_dt_head_tags, get_dt_navbar, get_dt_footer
from convert_services_group import clean_html_content

area_files = [
    ('areas.html', 'PAN-PUNE SERVICE NETWORK', 'Solar Installation Service Areas in Pune & PCMC'),
    ('solar-panel-pune.html', 'PUNE CITY ZONE', 'Rooftop Solar Panel Installation in Pune City'),
    ('solar-panel-pimpri-chinchwad.html', 'PCMC INDUSTRIAL & URBAN', 'Best Solar Company in Pimpri Chinchwad (PCMC)'),
    ('solar-panel-baner-bavdhan.html', 'WEST PUNE RESIDENTIAL', 'Rooftop Solar Panel Installation in Baner & Bavdhan'),
    ('solar-panel-chakan.html', 'CHAKAN MIDC AUTOMOTIVE', 'Industrial Solar Panel Installation in Chakan MIDC'),
    ('solar-panel-bhosari-pcmc.html', 'BHOSARI MIDC MANUFACTURING', 'Industrial Solar Panel Installation in Bhosari MIDC'),
    ('solar-panel-kiwale.html', 'KIWALE & RAVET EXPRESSWAY', 'Rooftop Solar Panel Installation in Kiwale & Ravet'),
    ('solar-panel-lonavala.html', 'LONAVALA & KHANDALA HILLS', 'Solar Panel Installation in Lonavala & Khandala'),
]

def convert_area_page(filename, label_code, fallback_h1):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Title, Meta description, Keywords, Canonical, Schemas
    title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    title = title_m.group(0) if title_m else f'<title>{fallback_h1} - E Green Solution</title>'

    desc_m = re.search(r'<meta name="description" content="([^"]*)">', content)
    desc = desc_m.group(0) if desc_m else ''

    kw_m = re.search(r'<meta name="keywords" content="([^"]*)">', content)
    kw = kw_m.group(0) if kw_m else ''

    canon_m = re.search(r'<link rel="canonical" href="([^"]*)">', content)
    canonical = canon_m.group(0) if canon_m else f'<link rel="canonical" href="https://egreensolution.in/{filename[:-5]}">'

    schemas = re.findall(r'<script type="application/ld\+json">.*?</script>', content, re.DOTALL)
    schemas_str = '\n    '.join(schemas)

    gtag = '''    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-6RB8MHEG1S"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-6RB8MHEG1S');
    </script>'''

    # Extract H1 and Desc
    h1_m = re.search(r'<h1 class="hero-split-title">(.*?)</h1>', content, re.DOTALL)
    if not h1_m:
        h1_m = re.search(r'<h1.*?>(.*?)</h1>', content, re.DOTALL)
    raw_h1 = h1_m.group(1).strip() if h1_m else fallback_h1
    clean_h1 = re.sub(r'<.*?>', '', raw_h1).strip()

    desc_hero_m = re.search(r'<p class="hero-split-desc">(.*?)</p>', content, re.DOTALL)
    raw_desc = desc_hero_m.group(1).strip() if desc_hero_m else f"Turnkey rooftop and industrial solar installations across {clean_h1}."
    clean_desc = re.sub(r'<span class="highlight-mark">(.*?)</span>', r'\1', raw_desc)
    clean_desc = re.sub(r'<span class="accent-underline">(.*?)</span>', r'\1', clean_desc)

    chips = re.findall(r'<div class="hero-feature-chip">.*?<span>(.*?)</span>.*?</div>', content, re.DOTALL)
    chips_html = ''
    for chip in chips[:4]:
        chips_html += f'<span class="dt-pill"><i class="fas fa-check" style="color: var(--gold-accent);"></i> {chip.strip()}</span>\n                        '

    # Extract Form
    form_card_m = re.search(r'<div class="hero-form-card">(.*?)</div>\s*</div>\s*</div>\s*</header>', content, re.DOTALL)
    if form_card_m:
        raw_form = form_card_m.group(1)
        cleaned_form = clean_html_content(raw_form)
    else:
        cleaned_form = f'''<span class="dt-tech-label" style="margin-bottom: 12px;">LOCAL SURVEY</span>
        <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 6px;">Check Area Feasibility</h3>
        <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 18px;">Get local MSEDCL circle sanction support and accurate pricing.</p>
        <form action="https://formspree.io/f/xbjnqkyw" method="POST" style="display: flex; flex-direction: column; gap: 12px;">
            <input type="hidden" name="_subject" value="{clean_h1} - Area Inquiry">
            <input type="hidden" name="_page" value="{filename[:-5]}">
            <input type="text" name="name" required placeholder="Full Name" class="dt-input">
            <input type="tel" name="phone" required placeholder="Mobile Number" class="dt-input">
            <input type="text" name="location" value="{clean_h1}" class="dt-input">
            <button type="submit" class="dt-btn dt-btn-primary" style="width: 100%;">Check Feasibility &rarr;</button>
        </form>'''

    # Extract middle body between </header> and <footer
    header_end = content.find('</header>')
    if header_end != -1:
        middle = content[header_end + 9:]
    else:
        sec_start = content.find('<section')
        middle = content[sec_start:] if sec_start != -1 else ''
    
    footer_start = middle.find('<footer')
    if footer_start != -1:
        middle = middle[:footer_start]
    
    cleaned_middle = clean_html_content(middle)

    breadcrumbs = f'''<div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <a href="/areas">Service Areas</a>
                <span class="sep">/</span>
                <span class="current">{clean_h1}</span>
            </div>''' if filename != 'areas.html' else f'''<div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <span class="current">Service Areas Hub</span>
            </div>'''

    page_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{gtag}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {title}
    {desc}
    {kw}
    {canonical}

    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon.png">
    <link rel="apple-touch-icon" href="/assets/logo.png">

    <!-- Schema.org Data -->
    {schemas_str}

{get_dt_head_tags()}
</head>
<body class="tech-grid-bg">
{get_dt_navbar('areas')}

    <!-- ============================================================
         SUBPAGE HERO (Dark Technical Editorial)
         ============================================================ -->
    <section class="dt-subpage-hero">
        <div class="dt-container">
            {breadcrumbs}

            <div class="dt-subpage-grid">
                <div>
                    <div class="dt-tech-label">{label_code}</div>
                    <h1 class="dt-hero-title" style="font-size: clamp(34px, 4.2vw, 52px); margin-bottom: 20px;">
                        {clean_h1}
                    </h1>
                    <p class="dt-section-desc" style="margin-bottom: 28px;">
                        {clean_desc}
                    </p>

                    <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px;">
                        {chips_html}
                    </div>

                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; background: var(--bg-surface); border: 1px solid var(--border-muted); border-radius: var(--radius-card); padding: 18px;">
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--gold-accent); display: block;">100%</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">MSEDCL Network</span>
                        </div>
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--text-primary); display: block;">24 Hr</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Site Inspection</span>
                        </div>
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--gold-accent); display: block;">₹78,000</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Direct Subsidy</span>
                        </div>
                    </div>
                </div>

                <div>
                    <div class="dt-form-card">
                        {cleaned_form}
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Content Sections -->
    <div class="dt-page-content">
        {cleaned_middle}
    </div>

    <!-- Global Area CTA -->
    <section class="dt-section" style="background: var(--bg-primary); border-top: 1px solid var(--border-muted);">
        <div class="dt-container" style="text-align: center;">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-container); padding: 50px; max-width: 860px; margin: 0 auto;">
                <div class="dt-tech-label" style="margin: 0 auto 16px;">LOCAL ENGINEERING SUPPORT</div>
                <h2 style="font-size: clamp(28px, 3.4vw, 40px); color: var(--text-primary); margin-bottom: 14px;">Schedule an On-Site Survey in Your Area</h2>
                <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 28px;">
                    Our localized Pune engineering team handles roof load auditing, shadow profiling, and direct MSEDCL subdivision paperwork.
                </p>
                <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
                    <a href="/contact" class="dt-btn dt-btn-primary">Book Free Site Survey &rarr;</a>
                    <a href="tel:+917249187969" class="dt-btn dt-btn-secondary"><i class="fas fa-phone-alt"></i> +91 72491 87969</a>
                </div>
            </div>
        </div>
    </section>

{get_dt_footer()}
</body>
</html>'''

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page_html)
    print(f'Converted {filename} successfully!')

if __name__ == '__main__':
    for fn, lcode, fh1 in area_files:
        convert_area_page(fn, lcode, fh1)
