import os
import sys
import re

sys.path.append(os.path.abspath('scripts'))
from dark_theme_components import get_dt_head_tags, get_dt_navbar, get_dt_footer
from convert_services_group import clean_html_content

def redesign_projects_index():
    with open('projects/index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Schemas
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

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{gtag}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solar Projects Pune | Rooftop &amp; Industrial Case Studies - E Green Solution</title>
    <meta name="description" content="Explore E Green Solution solar projects in Pune and Maharashtra, including residential, commercial and industrial rooftop installations and verified case studies.">
    <meta name="keywords" content="solar panel installations in pune, solar panel pune, solar installation images, solar projects in Pune, industrial solar case studies, solar rooftop success stories">
    <link rel="canonical" href="https://egreensolution.in/projects">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://egreensolution.in/projects">
    <meta property="og:title" content="Solar Case Studies &amp; Commissioned Projects | E Green Solution">
    <meta property="og:description" content="Explore our extensive portfolio of solar installations across Pune, PCMC, Chakan MIDC, and Maharashtra. Industrial, commercial, and residential expertise.">
    <meta property="og:image" content="https://egreensolution.in/assets/logo.png">

    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon.png">
    <link rel="apple-touch-icon" href="/assets/logo.png">

    <!-- Schema.org Data -->
    {schemas_str}

{get_dt_head_tags()}
</head>
<body class="tech-grid-bg">
{get_dt_navbar('projects')}

    <!-- ============================================================
         SUBPAGE HERO SECTION
         ============================================================ -->
    <section class="dt-subpage-hero">
        <div class="dt-container">
            <div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <span class="current">Commissioned Projects</span>
            </div>

            <div style="max-width: 900px;">
                <div class="dt-tech-label">PROVEN ENGINEERING TRACK RECORD</div>
                <h1 class="dt-hero-title" style="font-size: clamp(34px, 4.4vw, 54px); margin-bottom: 20px;">
                    Solar Projects &amp; Case Studies in Pune
                </h1>
                <p class="dt-section-desc" style="font-size: 18px; line-height: 1.8; margin-bottom: 30px;">
                    Real telemetry data and verified generation metrics from our residential, commercial, and industrial rooftop installations across Pune, Chakan MIDC, Bhosari, Talegaon, and Western Maharashtra.
                </p>

                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; background: var(--bg-surface); border: 1px solid var(--border-muted); border-radius: var(--radius-card); padding: 20px;">
                    <div>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 700; color: var(--gold-accent); display: block;">200+</span>
                        <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Plants Built</span>
                    </div>
                    <div>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 700; color: var(--text-primary); display: block;">2.0+ MW</span>
                        <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Capacity</span>
                    </div>
                    <div>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 700; color: var(--gold-accent); display: block;">90%</span>
                        <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Avg Bill Cut</span>
                    </div>
                    <div>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 700; color: var(--text-primary); display: block;">&lt; 3.2 Yrs</span>
                        <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Avg Payback</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         DRONE VIDEO DOCUMENTATION SECTION
         ============================================================ -->
    <section class="dt-section">
        <div class="dt-container">
            <div class="dt-section-header center">
                <div class="dt-tech-label">ON-SITE VIDEO DOCUMENTATION</div>
                <h2 class="dt-section-title">Walkthrough Our Commissioned Mega Plants</h2>
                <p class="dt-section-desc" style="margin: 0 auto;">
                    Drone video documentation showcasing our hot-dip galvanized mounting structures, Tier-1 Vikram Solar modules, and high-tension grid synchronization.
                </p>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 24px;">
                <div style="background: var(--bg-surface); border: 1px solid var(--border-emp); border-radius: var(--radius-card); overflow: hidden; box-shadow: var(--shadow-elevated);">
                    <video width="100%" height="auto" controls muted playsinline preload="metadata" poster="/assets/projects/eagle_burgmann.png" style="aspect-ratio: 16/9; object-fit: cover; display: block;" aria-label="Eagle Burgmann 200kW Industrial Solar Installation Video">
                        <source src="/assets/projects/video1.mp4" type="video/mp4">
                    </video>
                    <div style="padding: 18px 24px;">
                        <span class="dt-pill" style="margin-bottom: 8px;">200 kW Industrial EPC</span>
                        <h4 style="color: var(--text-primary); font-size: 17px; margin-bottom: 4px;">Eagle Burgmann India — Chakan MIDC</h4>
                        <p style="color: var(--text-secondary); font-size: 13.5px; margin: 0;">200kW industrial shed installation with non-penetrating clamps and 11kV HT net metering.</p>
                    </div>
                </div>

                <div style="background: var(--bg-surface); border: 1px solid var(--border-emp); border-radius: var(--radius-card); overflow: hidden; box-shadow: var(--shadow-elevated);">
                    <video width="100%" height="auto" controls muted playsinline preload="metadata" poster="/assets/Projects_egreen/IMG-20260331-WA0013.jpg" style="aspect-ratio: 16/9; object-fit: cover; display: block;" aria-label="Bhagawati Industries 140kW Solar Installation Video">
                        <source src="/assets/projects/video2.mp4" type="video/mp4">
                    </video>
                    <div style="padding: 18px 24px;">
                        <span class="dt-pill" style="margin-bottom: 8px;">140 kW Commercial EPC</span>
                        <h4 style="color: var(--text-primary); font-size: 17px; margin-bottom: 4px;">Bhagawati Industries — Pune</h4>
                        <p style="color: var(--text-secondary); font-size: 13.5px; margin: 0;">140kW high-capacity commercial rooftop slashing daytime utility bills by 72%.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         PORTFOLIO GRID OF COMMISSIONED PLANTS
         ============================================================ -->
    <section class="dt-section dt-section-surface">
        <div class="dt-container">
            <div class="dt-section-header center">
                <div class="dt-tech-label">COMMISSIONED PORTFOLIO</div>
                <h2 class="dt-section-title">Featured Rooftop Solar Installations</h2>
                <p class="dt-section-desc" style="margin: 0 auto;">
                    Select engineering projects demonstrating structural safety, high kilowatt output, and verified financial returns.
                </p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 28px;">
                <!-- Card 1: Konark A Plus Housing Society -->
                <div class="dt-project-card" style="border-color: var(--border-gold);">
                    <div class="dt-project-media">
                        <span class="dt-project-tag"><i class="fas fa-star" style="color: var(--gold-accent);"></i> FEATURED CASE STUDY</span>
                        <img src="/assets/projects/konark_society_rooftop_100kw.jpg" alt="Konark A Plus Housing Society - 100kW Solar Installation Pune" loading="lazy">
                    </div>
                    <div class="dt-project-body">
                        <div>
                            <span class="dt-tech-label" style="font-size: 9.5px; padding: 3px 8px; margin-bottom: 8px;">100 kW HOUSING SOCIETY</span>
                            <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 8px;">Konark A Plus Society, Sopan Baug</h3>
                            <p style="font-size: 14px; color: var(--text-secondary); line-height: 1.6;">
                                Slashed monthly common area power bill from ₹3.2+ Lakhs down to ~₹32,000 for lifts, pumps, and lighting with ₹18 Lakhs central subsidy.
                            </p>
                        </div>
                        <div class="dt-project-metrics">
                            <div>
                                <span class="dt-project-metric-val">90%</span>
                                <span class="dt-project-metric-lbl">Bill Cut</span>
                            </div>
                            <div>
                                <span class="dt-project-metric-val">₹18 Lakh</span>
                                <span class="dt-project-metric-lbl">Subsidy</span>
                            </div>
                            <div>
                                <span class="dt-project-metric-val">&lt; 3 Yrs</span>
                                <span class="dt-project-metric-lbl">Payback</span>
                            </div>
                        </div>
                        <a href="/projects/konark-a-plus-100kw-housing-society-solar-pune" class="dt-btn dt-btn-primary" style="width: 100%;">
                            Read 100kW Society Case Study &rarr;
                        </a>
                    </div>
                </div>

                <!-- Card 2: Eagle Burgmann India -->
                <div class="dt-project-card" style="border-color: var(--border-gold);">
                    <div class="dt-project-media">
                        <span class="dt-project-tag"><i class="fas fa-industry" style="color: var(--gold-accent);"></i> FLAGSHIP INDUSTRIAL</span>
                        <img src="/assets/projects/eagle_burgmann.png" alt="Eagle Burgmann India - 200KW Industrial Solar EPC Pune" loading="lazy">
                    </div>
                    <div class="dt-project-body">
                        <div>
                            <span class="dt-tech-label" style="font-size: 9.5px; padding: 3px 8px; margin-bottom: 8px;">200 kW INDUSTRIAL EPC</span>
                            <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 8px;">Eagle Burgmann India Pvt. Ltd.</h3>
                            <p style="font-size: 14px; color: var(--text-secondary); line-height: 1.6;">
                                High-tension 11kV substation grid synchronization across factory sheds in Chakan MIDC with zero roof penetration clamping.
                            </p>
                        </div>
                        <div class="dt-project-metrics">
                            <div>
                                <span class="dt-project-metric-val">2.9 Lakh</span>
                                <span class="dt-project-metric-lbl">Units/Yr</span>
                            </div>
                            <div>
                                <span class="dt-project-metric-val">40%</span>
                                <span class="dt-project-metric-lbl">Tax Depr.</span>
                            </div>
                            <div>
                                <span class="dt-project-metric-val">2.8 Yrs</span>
                                <span class="dt-project-metric-lbl">Payback</span>
                            </div>
                        </div>
                        <a href="/projects/eagle-burgmann-200kw-solar-pune" class="dt-btn dt-btn-primary" style="width: 100%;">
                            Read 200kW Industrial Case Study &rarr;
                        </a>
                    </div>
                </div>

                <!-- Card 3: Bhagawati Industries -->
                <div class="dt-project-card">
                    <div class="dt-project-media">
                        <span class="dt-project-tag">COMMERCIAL EPC</span>
                        <img src="/assets/Projects_egreen/IMG-20260331-WA0013.jpg" alt="Bhagawati Industries - 140KW Industrial Solar Installation Pune" loading="lazy">
                    </div>
                    <div class="dt-project-body">
                        <div>
                            <span class="dt-tech-label" style="font-size: 9.5px; padding: 3px 8px; margin-bottom: 8px;">140 kW COMMERCIAL</span>
                            <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 8px;">Bhagawati Industries</h3>
                            <p style="font-size: 14px; color: var(--text-secondary); line-height: 1.6;">
                                Multi-MPPT commercial plant generating ~18,500 units monthly with customized walkway access and lightning protection.
                            </p>
                        </div>
                        <div class="dt-project-metrics">
                            <div>
                                <span class="dt-project-metric-val">18.5k</span>
                                <span class="dt-project-metric-lbl">Units/Mo</span>
                            </div>
                            <div>
                                <span class="dt-project-metric-val">72%</span>
                                <span class="dt-project-metric-lbl">Bill Cut</span>
                            </div>
                            <div>
                                <span class="dt-project-metric-val">3.0 Yrs</span>
                                <span class="dt-project-metric-lbl">Payback</span>
                            </div>
                        </div>
                        <a href="/contact" class="dt-btn dt-btn-secondary" style="width: 100%;">
                            Inquire for Similar Capacity &rarr;
                        </a>
                    </div>
                </div>

                <!-- Card 4: Kotling Enterprises Bhosari MIDC -->
                <div class="dt-project-card">
                    <div class="dt-project-media">
                        <span class="dt-project-tag">BHOSARI MIDC</span>
                        <img src="/assets/Projects_egreen/IMG-20260331-WA0017.jpg" alt="Kotling Enterprises - 60KW Industrial Solar Bhosari MIDC" loading="lazy">
                    </div>
                    <div class="dt-project-body">
                        <div>
                            <span class="dt-tech-label" style="font-size: 9.5px; padding: 3px 8px; margin-bottom: 8px;">60 kW FACTORY EPC</span>
                            <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 8px;">Kotling Enterprises, Bhosari</h3>
                            <p style="font-size: 14px; color: var(--text-secondary); line-height: 1.6;">
                                Installed on industrial metal sheds using leak-proof standing-seam clamps with real-time IoT power factor telemetry.
                            </p>
                        </div>
                        <div class="dt-project-metrics">
                            <div>
                                <span class="dt-project-metric-val">60 kWp</span>
                                <span class="dt-project-metric-lbl">Capacity</span>
                            </div>
                            <div>
                                <span class="dt-project-metric-val">CEIG</span>
                                <span class="dt-project-metric-lbl">Approved</span>
                            </div>
                            <div>
                                <span class="dt-project-metric-val">3.1 Yrs</span>
                                <span class="dt-project-metric-lbl">Payback</span>
                            </div>
                        </div>
                        <a href="/contact" class="dt-btn dt-btn-secondary" style="width: 100%;">
                            Request Factory Survey &rarr;
                        </a>
                    </div>
                </div>

                <!-- Card 5: Divyaghar Commercial Site -->
                <div class="dt-project-card">
                    <div class="dt-project-media">
                        <span class="dt-project-tag">COASTAL COMMERCIAL</span>
                        <img src="/assets/Projects_egreen/IMG-20260331-WA0014.jpg" alt="Divyaghar Konkan Site - 35KW Commercial Solar" loading="lazy">
                    </div>
                    <div class="dt-project-body">
                        <div>
                            <span class="dt-tech-label" style="font-size: 9.5px; padding: 3px 8px; margin-bottom: 8px;">35 kW COMMERCIAL</span>
                            <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 8px;">Divyaghar Commercial Complex</h3>
                            <p style="font-size: 14px; color: var(--text-secondary); line-height: 1.6;">
                                Heavy-duty marine-grade anodized aluminum and HDG structure designed to withstand severe high-salinity coastal winds.
                            </p>
                        </div>
                        <div class="dt-project-metrics">
                            <div>
                                <span class="dt-project-metric-val">35 kWp</span>
                                <span class="dt-project-metric-lbl">Capacity</span>
                            </div>
                            <div>
                                <span class="dt-project-metric-val">Marine</span>
                                <span class="dt-project-metric-lbl">Grade</span>
                            </div>
                            <div>
                                <span class="dt-project-metric-val">150km/h</span>
                                <span class="dt-project-metric-lbl">Wind-Rated</span>
                            </div>
                        </div>
                        <a href="/contact" class="dt-btn dt-btn-secondary" style="width: 100%;">
                            Inquire for Similar Capacity &rarr;
                        </a>
                    </div>
                </div>

                <!-- Card 6: Wadgaon Budruk Society -->
                <div class="dt-project-card">
                    <div class="dt-project-media">
                        <span class="dt-project-tag">PUNE HOUSING SOCIETY</span>
                        <img src="/assets/Projects_egreen/IMG-20260331-WA0015.jpg" alt="Wadgaon Budruk Society - 35KW Residential Solar Pune" loading="lazy">
                    </div>
                    <div class="dt-project-body">
                        <div>
                            <span class="dt-tech-label" style="font-size: 9.5px; padding: 3px 8px; margin-bottom: 8px;">35 kW COMMON METER</span>
                            <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 8px;">Wadgaon Budruk Society, Pune</h3>
                            <p style="font-size: 14px; color: var(--text-secondary); line-height: 1.6;">
                                Completely powered 4 high-speed residential lifts and submersible water pumps, reducing maintenance costs to zero.
                            </p>
                        </div>
                        <div class="dt-project-metrics">
                            <div>
                                <span class="dt-project-metric-val">35 kWp</span>
                                <span class="dt-project-metric-lbl">Capacity</span>
                            </div>
                            <div>
                                <span class="dt-project-metric-val">Zero</span>
                                <span class="dt-project-metric-lbl">Lift Bill</span>
                            </div>
                            <div>
                                <span class="dt-project-metric-val">3.0 Yrs</span>
                                <span class="dt-project-metric-lbl">Payback</span>
                            </div>
                        </div>
                        <a href="/contact" class="dt-btn dt-btn-secondary" style="width: 100%;">
                            Request Society Proposal &rarr;
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Global CTA -->
    <section class="dt-section" style="background: var(--bg-primary); border-top: 1px solid var(--border-muted);">
        <div class="dt-container" style="text-align: center;">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-container); padding: 50px; max-width: 860px; margin: 0 auto;">
                <div class="dt-tech-label" style="margin: 0 auto 16px;">COMMISSION YOUR HIGH-YIELD PLANT</div>
                <h2 style="font-size: clamp(28px, 3.4vw, 40px); color: var(--text-primary); margin-bottom: 14px;">Want a High-Yield Solar System Like These?</h2>
                <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 28px;">
                    Get a certified on-site engineering audit, 3D shadow analysis, and turnkey proposal customized for your rooftop.
                </p>
                <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
                    <a href="/contact" class="dt-btn dt-btn-primary">Book Free Site Survey &rarr;</a>
                    <a href="tel:+917249187969" class="dt-btn dt-btn-secondary"><i class="fas fa-phone-alt"></i> Call +91 72491 87969</a>
                </div>
            </div>
        </div>
    </section>

{get_dt_footer()}
</body>
</html>'''

    with open('projects/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Converted projects/index.html successfully!')

def redesign_case_study(filename, active_id, title_text, label_code, h1_text):
    with open(filename, 'r', encoding='utf-8') as f:
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
    title = title_m.group(0) if title_m else f'<title>{title_text} - E Green Solution</title>'

    desc_m = re.search(r'<meta name="description" content="([^"]*)">', content)
    desc = desc_m.group(0) if desc_m else ''

    canon_m = re.search(r'<link rel="canonical" href="([^"]*)">', content)
    canonical = canon_m.group(0) if canon_m else f'<link rel="canonical" href="https://egreensolution.in/{filename[:-5]}">'

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

    page_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{gtag}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {title}
    {desc}
    {canonical}

    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon.png">
    <link rel="apple-touch-icon" href="/assets/logo.png">

    <!-- Schema.org Data -->
    {schemas_str}

{get_dt_head_tags()}
</head>
<body class="tech-grid-bg">
{get_dt_navbar('projects')}

    <!-- ============================================================
         SUBPAGE HERO (Dark Technical Editorial)
         ============================================================ -->
    <section class="dt-subpage-hero">
        <div class="dt-container">
            <div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <a href="/projects">Projects</a>
                <span class="sep">/</span>
                <span class="current">{h1_text}</span>
            </div>

            <div style="max-width: 900px;">
                <div class="dt-tech-label">{label_code} // DETAILED CASE STUDY</div>
                <h1 class="dt-hero-title" style="font-size: clamp(32px, 4.2vw, 50px); margin-bottom: 20px;">
                    {h1_text}
                </h1>
                <p class="dt-section-desc" style="font-size: 17px; line-height: 1.8; margin-bottom: 24px;">
                    In-depth engineering documentation, tariff analysis, structural layout, and generation telemetry audited by E Green Solution.
                </p>

                <div style="display: flex; gap: 12px; flex-wrap: wrap;">
                    <span class="dt-pill"><i class="fas fa-check-circle" style="color: var(--gold-accent);"></i> Verified Telemetry</span>
                    <span class="dt-pill"><i class="fas fa-bolt" style="color: var(--gold-accent);"></i> MSEDCL Approved</span>
                    <span class="dt-pill"><i class="fas fa-shield-alt" style="color: var(--gold-accent);"></i> 25-Year Linear Warranty</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Case Study In-Depth Body -->
    <div class="dt-page-content">
        {cleaned_middle}
    </div>

    <!-- Global CTA -->
    <section class="dt-section" style="background: var(--bg-primary); border-top: 1px solid var(--border-muted);">
        <div class="dt-container" style="text-align: center;">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-container); padding: 50px; max-width: 860px; margin: 0 auto;">
                <div class="dt-tech-label" style="margin: 0 auto 16px;">ENGINEER YOUR PLANT</div>
                <h2 style="font-size: clamp(28px, 3.4vw, 40px); color: var(--text-primary); margin-bottom: 14px;">Plan a Similar Rooftop Solar Plant</h2>
                <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 28px;">
                    Contact our senior project engineers for customized site feasibility, structural layout, and financial modeling.
                </p>
                <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
                    <a href="/contact" class="dt-btn dt-btn-primary">Request Site Survey &rarr;</a>
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
    redesign_projects_index()
    redesign_case_study(
        'projects/eagle-burgmann-200kw-solar-pune.html',
        'eagle-burgmann',
        '200kW Industrial Solar Eagle Burgmann Pune Case Study',
        'INDUSTRIAL EPC',
        '200kW Industrial Rooftop Solar Project — Eagle Burgmann India'
    )
    redesign_case_study(
        'projects/konark-a-plus-100kw-housing-society-solar-pune.html',
        'konark-a-plus',
        '100kW Housing Society Solar Konark A Plus Pune Case Study',
        'HOUSING SOCIETY EPC',
        '100kW Housing Society Rooftop Solar — Konark A Plus, Pune'
    )
