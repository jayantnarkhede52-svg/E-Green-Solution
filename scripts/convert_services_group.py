import os
import sys
import re

sys.path.append(os.path.abspath('scripts'))
from dark_theme_components import get_dt_head_tags, get_dt_navbar, get_dt_footer

def clean_html_content(raw_html):
    # Remove highlight marks & underlines
    cleaned = re.sub(r'<span class="highlight-mark">(.*?)</span>', r'\1', raw_html)
    cleaned = re.sub(r'<span class="accent-underline">(.*?)</span>', r'\1', cleaned)
    
    # Replace container
    cleaned = re.sub(r'\bcontainer\b', 'dt-container', cleaned)
    
    # Replace content section backgrounds
    cleaned = re.sub(r'style="[^"]*background:\s*(?:#f8fafc|#f1f5f9|#fff|#ffffff|white|#f4f8f4|#f8f9fa|#f9f9f9|#eef5ee|#fdfdfd|#f4f4f4)[^"]*"',
                     'class="dt-section" style="background-color: var(--bg-surface); border-bottom: 1px solid var(--border-muted);"', cleaned)
    
    # Replace inner cards with white or light background
    cleaned = re.sub(r'background:\s*(?:#fff|#ffffff|white|#f8fafc|#f1f5f9|#f9f9f9|#f4f8f4);?',
                     'background: var(--bg-surface); border: 1px solid var(--border-muted);', cleaned)
    
    # Replace text colors
    cleaned = re.sub(r'color:\s*(?:#0f172a|#1e293b|#1a1a1a|#334155);?', 'color: var(--text-primary);', cleaned)
    cleaned = re.sub(r'color:\s*(?:#475569|#64748b|#555|#666|#777|#555555|#666666);?', 'color: var(--text-secondary);', cleaned)
    cleaned = re.sub(r'color:\s*(?:var\(--primary\)|#2e7d32|#1b5e20);?', 'color: var(--gold-accent);', cleaned)
    
    # Replace border colors
    cleaned = re.sub(r'border:\s*1px solid\s*(?:#e2e8f0|#cbd5e1|#eee|#e0e0e0|#e8e8e8);?', 'border: 1px solid var(--border-muted);', cleaned)
    cleaned = re.sub(r'border-top:\s*4px solid[^;"]*;?', 'border-top: 3px solid var(--gold-accent);', cleaned)
    
    # Replace button styling
    cleaned = re.sub(r'class="btn-primary[^"]*"', 'class="dt-btn dt-btn-primary"', cleaned)
    cleaned = re.sub(r'class="btn-secondary[^"]*"', 'class="dt-btn dt-btn-secondary"', cleaned)
    
    # Replace inputs and forms
    cleaned = re.sub(r'<input ([^>]*)style="[^"]*"', r'<input \1class="dt-input"', cleaned)
    cleaned = re.sub(r'<select ([^>]*)style="[^"]*"', r'<select \1class="dt-select"', cleaned)
    cleaned = re.sub(r'<textarea ([^>]*)style="[^"]*"', r'<textarea \1class="dt-textarea"', cleaned)
    cleaned = re.sub(r'class="form-group-compact"', 'class="dt-form-group"', cleaned)
    cleaned = re.sub(r'class="form-row-2col"', 'style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;"', cleaned)
    cleaned = re.sub(r'class="btn-hero-form"', 'class="dt-btn dt-btn-primary" style="width: 100%; margin-top: 8px;"', cleaned)
    cleaned = re.sub(r'class="hero-form-card"', 'class="dt-form-card"', cleaned)
    
    # Table enhancements
    cleaned = re.sub(r'class="[^"]*table[^"]*"', 'class="dt-table"', cleaned)
    cleaned = re.sub(r'<table\b', '<table class="dt-table"', cleaned)
    # Avoid duplicate class="dt-table"
    cleaned = cleaned.replace('class="dt-table" class="dt-table"', 'class="dt-table"')
    cleaned = re.sub(r'<div class="[^"]*table-container[^"]*">', '<div class="dt-table-wrap">', cleaned)
    
    # FAQ accordion elements
    cleaned = re.sub(r'class="faq-item"', 'class="dt-faq-item active" style="margin-bottom: 14px; background: var(--bg-surface); border: 1px solid var(--border-muted); border-radius: var(--radius-card); padding: 22px;"', cleaned)
    
    return cleaned

def convert_service_file(filename, page_code, label_code):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Title, Meta description, Keywords, Canonical, Schemas
    title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    title = title_m.group(0) if title_m else f'<title>Solar Services in Pune - E Green Solution</title>'

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

    # Extract Hero parts
    h1_m = re.search(r'<h1 class="hero-split-title">(.*?)</h1>', content, re.DOTALL)
    if not h1_m:
        h1_m = re.search(r'<h1.*?>(.*?)</h1>', content, re.DOTALL)
    raw_h1 = h1_m.group(1).strip() if h1_m else "Solar Engineering Solutions in Pune"
    clean_h1 = re.sub(r'<.*?>', '', raw_h1).strip()

    desc_hero_m = re.search(r'<p class="hero-split-desc">(.*?)</p>', content, re.DOTALL)
    raw_desc = desc_hero_m.group(1).strip() if desc_hero_m else "Turnkey rooftop solar installations and lifecycle operations in Pune."
    clean_desc = re.sub(r'<span class="highlight-mark">(.*?)</span>', r'\1', raw_desc)
    clean_desc = re.sub(r'<span class="accent-underline">(.*?)</span>', r'\1', clean_desc)

    chips = re.findall(r'<div class="hero-feature-chip">.*?<span>(.*?)</span>.*?</div>', content, re.DOTALL)
    chips_html = ''
    for chip in chips[:4]:
        chips_html += f'<span class="dt-pill"><i class="fas fa-check" style="color: var(--gold-accent);"></i> {chip.strip()}</span>\n                        '

    # Extract the hero form
    form_card_m = re.search(r'<div class="hero-form-card">(.*?)</div>\s*</div>\s*</div>\s*</header>', content, re.DOTALL)
    if form_card_m:
        raw_form = form_card_m.group(1)
        cleaned_form = clean_html_content(raw_form)
    else:
        # Generic form fallback
        cleaned_form = f'''<span class="dt-tech-label" style="margin-bottom: 12px;">FAST CALLBACK</span>
        <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 6px;">Request Immediate Quote</h3>
        <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 18px;">Certified engineer callback within 15 minutes.</p>
        <form action="https://formspree.io/f/xbjnqkyw" method="POST" style="display: flex; flex-direction: column; gap: 12px;">
            <input type="hidden" name="_subject" value="{clean_h1} - Inquiry">
            <input type="hidden" name="_page" value="{filename[:-5]}">
            <input type="text" name="name" required placeholder="Full Name" class="dt-input">
            <input type="tel" name="phone" required placeholder="Mobile Number" class="dt-input">
            <input type="text" name="location" placeholder="Location in Pune" class="dt-input">
            <button type="submit" class="dt-btn dt-btn-primary" style="width: 100%;">Get Free Quote &rarr;</button>
        </form>'''

    # Extract middle body content between </header> and <footer
    header_end = content.find('</header>')
    if header_end != -1:
        middle = content[header_end + 9:]
    else:
        # Search for first section
        sec_start = content.find('<section')
        middle = content[sec_start:] if sec_start != -1 else ''

    footer_start = middle.find('<footer')
    if footer_start != -1:
        middle = middle[:footer_start]

    cleaned_middle = clean_html_content(middle)

    # Build Dark Technical Page
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

    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon.png">
    <link rel="apple-touch-icon" href="/assets/logo.png">

    <!-- Schema.org Data -->
    {schemas_str}

{get_dt_head_tags()}
</head>
<body class="tech-grid-bg">
{get_dt_navbar('services')}

    <!-- ============================================================
         SUBPAGE HERO (Dark Technical Editorial)
         ============================================================ -->
    <section class="dt-subpage-hero">
        <div class="dt-container">
            <div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <a href="/services">Services</a>
                <span class="sep">/</span>
                <span class="current">{clean_h1}</span>
            </div>

            <div class="dt-subpage-grid">
                <div>
                    <div class="dt-tech-label">{label_code} // SOLAR ENGINEERING</div>
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
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--gold-accent); display: block;">200+</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Completed Sites</span>
                        </div>
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--text-primary); display: block;">4.9 / 5</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Client Rating</span>
                        </div>
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--gold-accent); display: block;">100%</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">MSEDCL Verified</span>
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

    <!-- Global Consultation CTA -->
    <section class="dt-section" style="background: var(--bg-primary); border-top: 1px solid var(--border-muted);">
        <div class="dt-container" style="text-align: center;">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-container); padding: 50px; max-width: 860px; margin: 0 auto;">
                <div class="dt-tech-label" style="margin: 0 auto 16px;">DIRECT TECHNICAL SUPPORT</div>
                <h2 style="font-size: clamp(28px, 3.4vw, 40px); color: var(--text-primary); margin-bottom: 14px;">Speak Directly with a Pune Solar Engineer</h2>
                <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 28px;">
                    Have questions about sizing, technical compatibility, MSEDCL approvals, or warranty support? Contact our engineering team for immediate assistance.
                </p>
                <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
                    <a href="/contact" class="dt-btn dt-btn-primary">Book Technical Inspection &rarr;</a>
                    <a href="tel:+917249187969" class="dt-btn dt-btn-secondary"><i class="fas fa-phone-alt"></i> +91 72491 87969</a>
                    <a href="https://wa.me/917249187969?text=Hello%20E%20Green%20Solution,%20I%20have%20an%20inquiry%20regarding%20{clean_h1}" target="_blank" rel="noopener noreferrer" class="dt-btn dt-btn-secondary" style="color: #4ade80 !important;"><i class="fab fa-whatsapp"></i> WhatsApp Us</a>
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

services_to_convert = [
    ('solar-water-heater-pune.html', 'services', '05'),
    ('solar-panel-cleaning-pune.html', 'services', '06'),
    ('solar-amc-pune.html', 'services', '07'),
    ('solar-inverter-repair-pune.html', 'services', '08'),
    ('solar-net-meter-msedcl-pune.html', 'services', '09'),
    ('solar-plant-revamping-repowering.html', 'services', '10'),
    ('solar-repair-maintenance-pune.html', 'services', '11'),
]

if __name__ == '__main__':
    for fn, pcode, lcode in services_to_convert:
        convert_service_file(fn, pcode, lcode)
