import os
import sys
import re
import glob

sys.path.append(os.path.abspath('scripts'))
from dark_theme_components import get_dt_head_tags, get_dt_navbar, get_dt_footer
from convert_services_group import clean_html_content

def redesign_blog_index():
    with open('blog/index.html', 'r', encoding='utf-8') as f:
        content = f.read()

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

    # Extract all blog cards from the original
    cards = re.findall(r'<article class="blog-card[^"]*">(.*?)</article>', content, re.DOTALL)
    if not cards:
        cards = re.findall(r'<div class="blog-card[^"]*">(.*?)</div>\s*</div>\s*</div>', content, re.DOTALL)

    # Let's define the 9 verified articles cleanly
    articles_data = [
        {
            'slug': '3kw-vs-5kw-solar-price-pune-subsidy',
            'tag': 'PRICING & SIZING',
            'title': '3kW vs 5kW Rooftop Solar Price in Pune: Cost, Subsidy & Payback Guide',
            'desc': 'Complete financial and technical breakdown comparing 3kW vs 5kW on-grid solar plants in Pune. Sizing math, PM Surya Ghar ₹78,000 subsidy eligibility, and MSEDCL domestic payback.',
            'img': '/assets/blog/3kw_vs_5kw_solar_pune.jpg',
            'read_time': '8 min read'
        },
        {
            'slug': 'bifacial-solar-panels-pune',
            'tag': 'TECHNOLOGY',
            'title': 'Bifacial Solar Panels in Pune: Boost Rooftop Generation by Up to 25%',
            'desc': 'How double-sided bifacial PV modules harvest reflected albedo light from white terrace tiles to deliver 15%–25% higher kilowatt-hour yield in Maharashtra sunshine.',
            'img': '/assets/blog/bifacial_solar_panels_pune.jpg',
            'read_time': '6 min read'
        },
        {
            'slug': 'dcr-solar-panels-pune',
            'tag': 'SUBSIDY RULES',
            'title': 'DCR Solar Panels in Pune: The Mandatory Subsidy Compliance Rule',
            'desc': 'Why Domestic Content Requirement (DCR) solar cells and modules are strictly mandatory to qualify for the central ₹78,000 PM Surya Ghar bank transfer subsidy.',
            'img': '/assets/blog/dcr_solar_panels_pune.jpg',
            'read_time': '7 min read'
        },
        {
            'slug': 'elevated-rooftop-solar-structure-pune',
            'tag': 'TERRACE DESIGN',
            'title': 'Elevated Rooftop Solar Structure Pune: Preserve 100% Usable Terrace Area',
            'desc': 'High-clearance solar pergolas and canopies raised 8 to 10 feet above flat RCC roofs. Enjoy rooftop gardens and recreational spaces while producing clean energy.',
            'img': '/assets/blog/elevated_solar_structure_pune.jpg',
            'read_time': '7 min read'
        },
        {
            'slug': 'enphase-microinverter-installers-pune',
            'tag': 'HARDWARE',
            'title': 'Enphase Microinverter Installers in Pune: Maximum Safety & Module-Level MPPT',
            'desc': 'Why premium homeowners and partial-shade roofs choose Enphase IQ8 microinverters with module-level monitoring, rapid shutdown, and 25-year warranty.',
            'img': '/assets/blog/enphase_microinverters_pune.jpg',
            'read_time': '6 min read'
        },
        {
            'slug': 'housing-society-solar-pune-rules-subsidy',
            'tag': 'SOCIETY HOUSING',
            'title': 'Housing Society Rooftop Solar in Pune: Bye-Laws, AGM Resolution & Subsidy Guide',
            'desc': 'Step-by-step roadmap for housing societies and RWAs in Pune. AGM quorum requirements, MSEDCL common meter net-metering, and ₹18,000/kW subsidy claims.',
            'img': '/assets/blog/housing_society_solar_pune.jpg',
            'read_time': '9 min read'
        },
        {
            'slug': 'hybrid-solar-system-lithium-battery-pune',
            'tag': 'BATTERY STORAGE',
            'title': 'Hybrid Solar System with Lithium Battery Pune: Zero Power Outages',
            'desc': 'Combine net metering savings with 24/7 backup power using lithium ferro phosphate (LFP) batteries and hybrid bidirectional smart inverters.',
            'img': '/assets/blog/hybrid_solar_battery_pune.jpg',
            'read_time': '7 min read'
        },
        {
            'slug': 'mono-perc-vs-topcon-solar-pune',
            'tag': 'PANEL COMPARISON',
            'title': 'Mono PERC vs. TOPCon Solar Panels in Pune: Which Delivers Higher Yield?',
            'desc': 'Technical benchmark comparing N-Type Tunnel Oxide Passivated Contact (TOPCon) vs P-Type Mono PERC modules across degradation, temperature coefficient, and price.',
            'img': '/assets/blog/topcon_vs_mono_perc_pune.jpg',
            'read_time': '8 min read'
        },
        {
            'slug': 'on-grid-solar-inverter-dealers-pune',
            'tag': 'INVERTER BRANDS',
            'title': 'On-Grid Solar Inverter Dealers in Pune: Growatt, Sungrow, Solis & Polycab',
            'desc': 'Authorized dealers and certified installation partners for leading string inverters in Pune. Inverter sizing, dual-MPPT efficiency, and warranty support.',
            'img': '/assets/blog/ongrid_solar_inverter_pune.jpg',
            'read_time': '7 min read'
        }
    ]

    cards_html = ''
    for a in articles_data:
        cards_html += f'''                <article class="dt-card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
                    <a href="/blog/{a['slug']}" style="position: relative; height: 210px; overflow: hidden; display: block;">
                        <img src="{a['img']}" alt="{a['title']}" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" loading="lazy">
                        <span class="dt-project-tag">{a['tag']}</span>
                    </a>
                    <div style="padding: 24px; flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; font-size: 11px; color: var(--text-muted); font-family: 'JetBrains Mono', monospace;">
                                <span><i class="fas fa-clock" style="color: var(--gold-accent);"></i> {a['read_time']}</span>
                                <span>OCT 2026</span>
                            </div>
                            <h3 style="font-size: 18px; line-height: 1.4; color: var(--text-primary); margin-bottom: 12px; font-weight: 700;">
                                <a href="/blog/{a['slug']}" style="color: inherit;">{a['title']}</a>
                            </h3>
                            <p style="font-size: 13.5px; color: var(--text-secondary); line-height: 1.6; margin-bottom: 20px;">
                                {a['desc']}
                            </p>
                        </div>
                        <a href="/blog/{a['slug']}" class="dt-btn-ghost">
                            Read Full Technical Article &rarr;
                        </a>
                    </div>
                </article>\n'''

    page_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{gtag}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solar Insights &amp; Technical Guides | E Green Solution Blog Pune</title>
    <meta name="description" content="Expert rooftop solar insights, technology comparisons, subsidy updates, and technical guides for homeowners and commercial businesses in Pune.">
    <meta name="keywords" content="solar blog pune, solar energy guides maharashtra, bifacial solar panels pune, topcon vs mono perc, dcr solar subsidy pune, hybrid solar battery pune, enphase microinverters pune">
    <link rel="canonical" href="https://egreensolution.in/blog">

    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon.png">
    <link rel="apple-touch-icon" href="/assets/logo.png">

    <!-- Schema.org Data -->
    {schemas_str}

{get_dt_head_tags()}
</head>
<body class="tech-grid-bg">
{get_dt_navbar('blog')}

    <!-- ============================================================
         SUBPAGE HERO (Dark Technical Editorial)
         ============================================================ -->
    <section class="dt-subpage-hero">
        <div class="dt-container">
            <div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <span class="current">Solar Insights Blog</span>
            </div>

            <div style="max-width: 880px;">
                <div class="dt-tech-label">ENGINEERING KNOWLEDGE HUB</div>
                <h1 class="dt-hero-title" style="font-size: clamp(34px, 4.4vw, 54px); margin-bottom: 20px;">
                    Solar Insights, Technical Guides &amp; Industry News
                </h1>
                <p class="dt-section-desc" style="font-size: 18px; line-height: 1.8; margin-bottom: 30px;">
                    Explore verified photovoltaic engineering analyses, equipment comparisons, PM Surya Ghar subsidy updates, and MSEDCL net metering regulatory guides written by certified solar professionals in Pune.
                </p>

                <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                    <span class="dt-pill"><i class="fas fa-check" style="color: var(--gold-accent);"></i> Technical Comparisons</span>
                    <span class="dt-pill"><i class="fas fa-check" style="color: var(--gold-accent);"></i> PM Surya Ghar Subsidy Math</span>
                    <span class="dt-pill"><i class="fas fa-check" style="color: var(--gold-accent);"></i> MSEDCL Net Metering Walkthroughs</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Articles Grid -->
    <section class="dt-section">
        <div class="dt-container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 30px;">
{cards_html}
            </div>
        </div>
    </section>

    <!-- Global CTA -->
    <section class="dt-section dt-section-surface">
        <div class="dt-container" style="text-align: center;">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-container); padding: 50px; max-width: 860px; margin: 0 auto;">
                <div class="dt-tech-label" style="margin: 0 auto 16px;">CUSTOM ENGINEERING ADVICE</div>
                <h2 style="font-size: clamp(28px, 3.4vw, 40px); color: var(--text-primary); margin-bottom: 14px;">Have Questions About Your Property's Solar Setup?</h2>
                <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 28px;">
                    Get direct answers from certified rooftop solar engineers in Pune. We deliver custom capacity sizing and shadow analysis.
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

    with open('blog/index.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    print('Converted blog/index.html successfully!')

def redesign_blog_article(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

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

    title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    title = title_m.group(0) if title_m else '<title>Solar Article - E Green Solution</title>'

    desc_m = re.search(r'<meta name="description" content="([^"]*)">', content)
    desc = desc_m.group(0) if desc_m else ''

    kw_m = re.search(r'<meta name="keywords" content="([^"]*)">', content)
    kw = kw_m.group(0) if kw_m else ''

    canon_m = re.search(r'<link rel="canonical" href="([^"]*)">', content)
    canonical = canon_m.group(0) if canon_m else f'<link rel="canonical" href="https://egreensolution.in/{filepath[:-5]}">'

    # Extract H1
    h1_m = re.search(r'<h1.*?>(.*?)</h1>', content, re.DOTALL)
    raw_h1 = h1_m.group(1).strip() if h1_m else "Solar Insights in Pune"
    clean_h1 = re.sub(r'<.*?>', '', raw_h1).strip()

    # Extract middle body between </header> and <footer
    header_end = content.find('</header>')
    if header_end != -1:
        middle = content[header_end + 9:]
    else:
        sec_start = content.find('<section')
        if sec_start == -1:
            sec_start = content.find('<article')
            if sec_start == -1:
                sec_start = content.find('<div class="blog-content"')
        middle = content[sec_start:] if sec_start != -1 else ''
    
    footer_start = middle.find('<footer')
    if footer_start != -1:
        middle = middle[:footer_start]

    cleaned_middle = clean_html_content(middle)

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
{get_dt_navbar('blog')}

    <!-- ============================================================
         SUBPAGE HERO (Dark Technical Editorial)
         ============================================================ -->
    <section class="dt-subpage-hero">
        <div class="dt-container">
            <div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <a href="/blog">Blog</a>
                <span class="sep">/</span>
                <span class="current">{clean_h1}</span>
            </div>

            <div style="max-width: 900px;">
                <div class="dt-tech-label">TECHNICAL ENGINEERING GUIDE</div>
                <h1 class="dt-hero-title" style="font-size: clamp(30px, 4vw, 48px); margin-bottom: 20px;">
                    {clean_h1}
                </h1>
                
                <div style="display: flex; gap: 14px; align-items: center; font-size: 12px; color: var(--text-muted); font-family: 'JetBrains Mono', monospace; flex-wrap: wrap;">
                    <span><i class="fas fa-user-shield" style="color: var(--gold-accent);"></i> E Green Engineering Team</span>
                    <span>•</span>
                    <span><i class="fas fa-calendar-alt"></i> October 2026</span>
                    <span>•</span>
                    <span><i class="fas fa-check-circle" style="color: #4ade80;"></i> Verified Technical Guide</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Article Content -->
    <article class="dt-container dt-prose" style="max-width: 920px; padding: 70px 28px;">
        {cleaned_middle}
    </article>

    <!-- Global CTA -->
    <section class="dt-section dt-section-surface" style="border-top: 1px solid var(--border-muted);">
        <div class="dt-container" style="text-align: center;">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-container); padding: 50px; max-width: 860px; margin: 0 auto;">
                <div class="dt-tech-label" style="margin: 0 auto 16px;">FREE SOLAR CONSULTATION</div>
                <h2 style="font-size: clamp(28px, 3.4vw, 40px); color: var(--text-primary); margin-bottom: 14px;">Ready to Engineer Your Rooftop Solar System?</h2>
                <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 28px;">
                    Our certified rooftop solar engineers will inspect your terrace, conduct 3D shadow analysis, and calculate your exact savings and subsidy entitlement.
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

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(page_html)
    print(f'Converted {filepath} successfully!')

if __name__ == '__main__':
    redesign_blog_index()
    for fp in glob.glob('blog/*.html'):
        if fp.replace('\\', '/') != 'blog/index.html':
            redesign_blog_article(fp)
