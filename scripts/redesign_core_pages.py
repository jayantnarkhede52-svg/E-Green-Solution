import os
import sys
import re

sys.path.append(os.path.abspath('scripts'))
from dark_theme_components import get_dt_head_tags, get_dt_navbar, get_dt_footer
from convert_services_group import clean_html_content

def convert_about_page():
    with open('about.html', 'r', encoding='utf-8') as f:
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
    title = title_m.group(0) if title_m else '<title>About E Green Solution | Solar EPC Contractor Pune</title>'

    desc_m = re.search(r'<meta name="description" content="([^"]*)">', content)
    desc = desc_m.group(0) if desc_m else ''

    canon_m = re.search(r'<link rel="canonical" href="([^"]*)">', content)
    canonical = canon_m.group(0) if canon_m else '<link rel="canonical" href="https://egreensolution.in/about">'

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
    <meta name="keywords" content="about e green solution, solar company pune, solar engineers pune, rooftop solar company, solar EPC maharashtra">
    {canonical}

    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon.png">
    <link rel="apple-touch-icon" href="/assets/logo.png">

    <!-- Schema.org Data -->
    {schemas_str}

{get_dt_head_tags()}
</head>
<body class="tech-grid-bg">
{get_dt_navbar('about')}

    <!-- ============================================================
         SUBPAGE HERO (Dark Technical Editorial)
         ============================================================ -->
    <section class="dt-subpage-hero">
        <div class="dt-container">
            <div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <span class="current">About Us</span>
            </div>

            <div style="max-width: 900px;">
                <div class="dt-tech-label">ABOUT E GREEN SOLUTION // 10+ YEARS</div>
                <h1 class="dt-hero-title" style="font-size: clamp(34px, 4.4vw, 54px); margin-bottom: 20px;">
                    Leading Rooftop Solar Engineering Experts in Pune
                </h1>
                <p class="dt-section-desc" style="font-size: 18px; line-height: 1.8; margin-bottom: 30px;">
                    Over a decade of dedicated photovoltaic engineering excellence. Delivering precision turnkey residential, commercial, and industrial installations backed by certified Tier-1 equipment, direct MSEDCL net metering sanctions, and 25-year performance warranties.
                </p>

                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; background: var(--bg-surface); border: 1px solid var(--border-muted); border-radius: var(--radius-card); padding: 20px;">
                    <div>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 700; color: var(--gold-accent); display: block;">10+ Yrs</span>
                        <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Engineering</span>
                    </div>
                    <div>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 700; color: var(--text-primary); display: block;">200+</span>
                        <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Plants Built</span>
                    </div>
                    <div>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 700; color: var(--gold-accent); display: block;">2.0+ MW</span>
                        <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Installed</span>
                    </div>
                    <div>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 700; color: var(--text-primary); display: block;">ISO 9001</span>
                        <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Certified</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Content Sections -->
    <div class="dt-page-content">
        {cleaned_middle}
    </div>

    <!-- Global CTA -->
    <section class="dt-section" style="background: var(--bg-primary); border-top: 1px solid var(--border-muted);">
        <div class="dt-container" style="text-align: center;">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-container); padding: 50px; max-width: 860px; margin: 0 auto;">
                <div class="dt-tech-label" style="margin: 0 auto 16px;">PARTNER WITH CERTIFIED LEADERS</div>
                <h2 style="font-size: clamp(28px, 3.4vw, 40px); color: var(--text-primary); margin-bottom: 14px;">Ready to Engineer Your Clean Energy Future?</h2>
                <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 28px;">
                    Meet our engineering team for an on-site technical inspection, shadow analysis, and custom quotation.
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

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    print('Converted about.html successfully!')

def convert_calculator_page():
    with open('calculator.html', 'r', encoding='utf-8') as f:
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
    title = title_m.group(0) if title_m else '<title>Solar Calculator Pune | Savings, ROI & System Sizing</title>'

    desc_m = re.search(r'<meta name="description" content="([^"]*)">', content)
    desc = desc_m.group(0) if desc_m else ''

    canon_m = re.search(r'<link rel="canonical" href="([^"]*)">', content)
    canonical = canon_m.group(0) if canon_m else '<link rel="canonical" href="https://egreensolution.in/calculator">'

    page_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{gtag}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {title}
    {desc}
    <meta name="keywords" content="solar panel price in pune, solar savings calculator pune, solar roi calculator india, electricity savings estimator, rooftop solar sizing">
    {canonical}

    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon.png">
    <link rel="apple-touch-icon" href="/assets/logo.png">

    <!-- Schema.org Data -->
    {schemas_str}

{get_dt_head_tags()}
</head>
<body class="tech-grid-bg">
{get_dt_navbar('calculator')}

    <!-- ============================================================
         SUBPAGE HERO (Dark Technical Editorial)
         ============================================================ -->
    <section class="dt-subpage-hero">
        <div class="dt-container">
            <div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <span class="current">Solar Calculator</span>
            </div>

            <div style="max-width: 860px;">
                <div class="dt-tech-label">SAVINGS &amp; ROI SIMULATOR</div>
                <h1 class="dt-hero-title" style="font-size: clamp(34px, 4.4vw, 54px); margin-bottom: 20px;">
                    Solar Savings &amp; ROI Calculator
                </h1>
                <p class="dt-section-desc" style="font-size: 18px; line-height: 1.8; margin-bottom: 24px;">
                    Calculate your required kilowatt capacity, monthly MSEDCL bill reductions, government PM Surya Ghar subsidy entitlement, and exact capital payback in seconds.
                </p>

                <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                    <span class="dt-pill"><i class="fas fa-check" style="color: var(--gold-accent);"></i> Calibrated for Maharashtra Tariffs</span>
                    <span class="dt-pill"><i class="fas fa-check" style="color: var(--gold-accent);"></i> Includes ₹78,000 Subsidy Math</span>
                    <span class="dt-pill"><i class="fas fa-check" style="color: var(--gold-accent);"></i> Tier-1 Vikram Solar Sizing</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Interactive Wizard Calculator Section -->
    <section class="dt-section">
        <div class="dt-container">
            <div style="max-width: 960px; margin: 0 auto; background: var(--bg-surface); border: 1px solid var(--border-emp); border-radius: var(--radius-container); padding: 48px; box-shadow: var(--shadow-elevated);">
                
                <!-- Step 1: Input -->
                <div id="calc-step-1">
                    <div style="margin-bottom: 32px;">
                        <span class="dt-tech-label">STEP 01 // MONTHLY USAGE INPUT</span>
                        <h2 style="font-size: 26px; color: var(--text-primary); margin: 10px 0 6px;">Enter Your Current Electricity Consumption</h2>
                        <p style="color: var(--text-secondary); font-size: 15px;">Adjust the slider or enter your monthly MSEDCL power bill.</p>
                    </div>

                    <div style="margin-bottom: 36px;">
                        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 14px;">
                            <label style="font-family: 'JetBrains Mono', monospace; font-size: 13px; text-transform: uppercase; color: var(--text-secondary);">Average Monthly Bill (₹)</label>
                            <div style="display: flex; align-items: center; gap: 6px; background: var(--bg-input); border: 1px solid var(--border-gold); padding: 6px 14px; border-radius: var(--radius-ctrl);">
                                <span style="color: var(--gold-accent); font-weight: 700;">₹</span>
                                <input type="number" id="monthlyBill" value="5000" min="1000" max="100000" style="background: transparent; border: none; color: var(--text-primary); font-family: 'Manrope', sans-serif; font-size: 20px; font-weight: 700; width: 100px; outline: none;">
                            </div>
                        </div>

                        <input type="range" id="monthlyBillRange" min="1000" max="50000" step="500" value="5000" class="dt-range-input">
                    </div>

                    <div style="margin-bottom: 36px; background: var(--bg-elevated); border: 1px solid var(--border-muted); border-radius: var(--radius-card); padding: 22px;">
                        <label for="unitRate" style="font-family: 'JetBrains Mono', monospace; font-size: 12px; text-transform: uppercase; color: var(--text-secondary); display: block; margin-bottom: 8px;">
                            <i class="fas fa-bolt" style="color: var(--gold-accent);"></i> MSEDCL Electricity Rate (₹ / unit)
                        </label>
                        <p style="font-size: 12.5px; color: var(--text-muted); margin-bottom: 12px;">Maharashtra Residential Slabs: ₹9 – ₹14/unit (avg ₹10/unit)</p>
                        <div style="display: inline-flex; align-items: center; gap: 6px; background: var(--bg-input); border: 1px solid var(--border-muted); padding: 8px 16px; border-radius: var(--radius-ctrl);">
                            <span style="color: var(--text-muted);">₹</span>
                            <input type="number" id="unitRate" value="10" min="5" max="25" step="0.5" style="background: transparent; border: none; color: var(--text-primary); font-family: 'Manrope', sans-serif; font-size: 16px; font-weight: 600; width: 80px; outline: none;">
                        </div>
                    </div>

                    <button type="button" class="dt-btn dt-btn-primary" id="btn-show-results" style="width: 100%; padding: 16px; font-size: 15px;">
                        Calculate Solar Savings &rarr;
                    </button>
                </div>

                <!-- Step 2: Results -->
                <div id="calc-step-2" style="display: none;">
                    <div style="margin-bottom: 30px;">
                        <span class="dt-tech-label">STEP 02 // ESTIMATED SOLAR POTENTIAL</span>
                        <h2 style="font-size: 26px; color: var(--text-primary); margin: 10px 0 6px;">Your Projected Savings &amp; Capacity</h2>
                        <p style="color: var(--text-secondary); font-size: 14.5px;">Modeled for a monthly bill of ₹<span id="summary-bill" style="color: var(--gold-accent); font-weight: 700;">5000</span>.</p>
                    </div>

                    <!-- Highlight Box -->
                    <div style="background: linear-gradient(135deg, rgba(23, 27, 35, 0.95), rgba(39, 45, 55, 0.95)); border: 1px solid var(--border-gold); border-radius: var(--radius-card); padding: 28px; margin-bottom: 28px; text-align: center;">
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 12px; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.1em;">Estimated Monthly Bill Savings</span>
                        <div style="font-family: 'Manrope', sans-serif; font-size: clamp(38px, 5vw, 54px); font-weight: 800; color: var(--gold-accent); margin: 6px 0;">
                            ₹ <span id="resMonthlySavings">4,500</span>
                        </div>
                        <span style="font-size: 13px; color: #4ade80;"><i class="fas fa-check-circle"></i> Slashes approximately 90% of your ongoing electricity bill</span>
                    </div>

                    <!-- Stats Grid -->
                    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-bottom: 32px;">
                        <div style="background: var(--bg-elevated); border: 1px solid var(--border-muted); border-radius: var(--radius-ctrl); padding: 20px;">
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; text-transform: uppercase; color: var(--text-muted);">Required System Capacity</span>
                            <div style="font-size: 24px; font-weight: 700; color: var(--text-primary); margin-top: 6px;"><span id="resSystemSize">4.2</span> kW</div>
                        </div>

                        <div style="background: var(--bg-elevated); border: 1px solid var(--border-muted); border-radius: var(--radius-ctrl); padding: 20px;">
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; text-transform: uppercase; color: var(--text-muted);">Shadow-Free Roof Area</span>
                            <div style="font-size: 24px; font-weight: 700; color: var(--text-primary); margin-top: 6px;"><span id="resSpace">417</span> sq.ft.</div>
                        </div>

                        <div style="background: var(--bg-elevated); border: 1px solid var(--border-muted); border-radius: var(--radius-ctrl); padding: 20px;">
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; text-transform: uppercase; color: var(--text-muted);">Gross Turnkey Cost</span>
                            <div style="font-size: 24px; font-weight: 700; color: var(--text-primary); margin-top: 6px;">₹ <span id="resSystemCost">2,29,167</span></div>
                            <span style="font-size: 11px; color: var(--text-muted);">*Before central subsidy</span>
                        </div>

                        <div style="background: var(--bg-elevated); border: 1px solid var(--border-gold); border-radius: var(--radius-ctrl); padding: 20px;">
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; text-transform: uppercase; color: var(--gold-accent);">Net Investment After Subsidy</span>
                            <div style="font-size: 24px; font-weight: 700; color: var(--gold-accent); margin-top: 6px;">₹ <span id="resNetCost">1,51,167</span></div>
                            <span style="font-size: 11px; color: #4ade80;">*Includes ₹78,000 PM Surya Ghar Subsidy</span>
                        </div>
                    </div>

                    <div style="display: flex; gap: 14px; flex-wrap: wrap;">
                        <button type="button" class="dt-btn dt-btn-secondary" id="btn-back-to-input">
                            <i class="fas fa-arrow-left"></i> Edit Bill Inputs
                        </button>
                        <a href="/contact" class="dt-btn dt-btn-primary" style="flex: 1; justify-content: center;">
                            Book Free Site Survey &amp; Verify Proposal &rarr;
                        </a>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Educational Content Section -->
    <section class="dt-section dt-section-surface">
        <div class="dt-container">
            <div class="dt-section-header center">
                <div class="dt-tech-label">FINANCIAL METRICS</div>
                <h2 class="dt-section-title">Understanding Your Solar ROI in Pune</h2>
                <p class="dt-section-desc" style="margin: 0 auto;">
                    Investing in a rooftop solar plant is one of the highest-yielding, risk-free investments available in Maharashtra.
                </p>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-coins"></i></div>
                    <h3 class="dt-card-title">Factors Affecting Solar Pricing in Pune</h3>
                    <p class="dt-card-desc">Turnkey project cost depends on module technology (Mono PERC vs N-Type TOPCon bifacial), structure elevation (flush mount vs raised pergola), and inverter phase configuration. Our estimates use authentic Tier-1 equipment with 25-year performance warranties.</p>
                </div>

                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-piggy-bank"></i></div>
                    <h3 class="dt-card-title">Maximize Savings with PM Surya Ghar</h3>
                    <p class="dt-card-desc">By leveraging the central ₹78,000 DBT subsidy, your effective capital recovery drops to just 2.8 to 3.2 years. For the remaining 22+ years of the system's operational life, all power generated is 100% free of utility charges.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Global CTA -->
    <section class="dt-section" style="background: var(--bg-primary); border-top: 1px solid var(--border-muted);">
        <div class="dt-container" style="text-align: center;">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-container); padding: 50px; max-width: 860px; margin: 0 auto;">
                <div class="dt-tech-label" style="margin: 0 auto 16px;">VERIFY YOUR ROOF POTENTIAL</div>
                <h2 style="font-size: clamp(28px, 3.4vw, 40px); color: var(--text-primary); margin-bottom: 14px;">Want an Exact On-Site Energy Audit?</h2>
                <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 28px;">
                    Our engineers will inspect your terrace in Pune, conduct drone shadow analysis, and deliver a guaranteed output proposal.
                </p>
                <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
                    <a href="/contact" class="dt-btn dt-btn-primary">Book Free Site Survey &rarr;</a>
                    <a href="tel:+917249187969" class="dt-btn dt-btn-secondary"><i class="fas fa-phone-alt"></i> +91 72491 87969</a>
                </div>
            </div>
        </div>
    </section>

{get_dt_footer()}
    <script src="/js/main.js" defer></script>
</body>
</html>'''

    with open('calculator.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    print('Converted calculator.html successfully!')

def convert_contact_page():
    with open('contact.html', 'r', encoding='utf-8') as f:
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
    title = title_m.group(0) if title_m else '<title>Contact E Green Solution | Solar Company Pune & Free Site Survey</title>'

    desc_m = re.search(r'<meta name="description" content="([^"]*)">', content)
    desc = desc_m.group(0) if desc_m else ''

    canon_m = re.search(r'<link rel="canonical" href="([^"]*)">', content)
    canonical = canon_m.group(0) if canon_m else '<link rel="canonical" href="https://egreensolution.in/contact">'

    page_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{gtag}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {title}
    <meta name="geo.region" content="IN-MH">
    <meta name="geo.placename" content="Pune, Maharashtra, India">
    <meta name="geo.position" content="18.5204;73.8567">
    <meta name="ICBM" content="18.5204, 73.8567">
    {desc}
    <meta name="keywords" content="rooftop solar installation in pune, solar panel pune, request solar site survey, solar panel quotes Pune, contact solar installer Mumbai, solar expert consultation">
    {canonical}

    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon.png">
    <link rel="apple-touch-icon" href="/assets/logo.png">

    <!-- Schema.org Data -->
    {schemas_str}

{get_dt_head_tags()}
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
</head>
<body class="tech-grid-bg">
{get_dt_navbar('contact')}

    <!-- ============================================================
         SUBPAGE HERO (Dark Technical Editorial)
         ============================================================ -->
    <section class="dt-subpage-hero">
        <div class="dt-container">
            <div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <span class="current">Contact Us</span>
            </div>

            <div style="max-width: 860px;">
                <div class="dt-tech-label">OFFICIAL PUNE HEADQUARTERS</div>
                <h1 class="dt-hero-title" style="font-size: clamp(34px, 4.4vw, 54px); margin-bottom: 20px;">
                    Contact E Green Solution &amp; Request Free Site Survey
                </h1>
                <p class="dt-section-desc" style="font-size: 18px; line-height: 1.8; margin-bottom: 28px;">
                    Schedule a comprehensive on-site shadow analysis and engineering feasibility survey across Pune, PCMC, Chakan MIDC, or Mumbai. Fast response from certified rooftop solar engineers.
                </p>

                <div style="display: flex; gap: 12px; flex-wrap: wrap;">
                    <span class="dt-pill"><i class="fas fa-check" style="color: var(--gold-accent);"></i> 100% Free Site Inspection</span>
                    <span class="dt-pill"><i class="fas fa-check" style="color: var(--gold-accent);"></i> 3D Shadow Simulation</span>
                    <span class="dt-pill"><i class="fas fa-check" style="color: var(--gold-accent);"></i> Turnkey Cost &amp; Payback Proposal</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Contact Grid -->
    <section class="dt-section">
        <div class="dt-container">
            <div style="display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 50px; align-items: flex-start;">
                
                <!-- Left: High Converting Lead Form -->
                <div>
                    <div class="dt-form-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                            <span class="dt-tech-label" style="margin: 0;">DIRECT INQUIRY FORM</span>
                            <span style="font-size: 11px; color: #4ade80;"><i class="fas fa-circle" style="font-size: 8px;"></i> 15-Min Response</span>
                        </div>
                        <h2 style="font-size: 24px; color: var(--text-primary); margin-bottom: 8px;">Book Your Free Site Inspection</h2>
                        <p style="font-size: 14px; color: var(--text-secondary); margin-bottom: 24px;">Fill out the details below. Our technical team will reach out directly to schedule a site audit.</p>

                        <form id="solar-form" action="https://formspree.io/f/xbjnqkyw" method="POST" style="display: flex; flex-direction: column; gap: 16px;">
                            <input type="hidden" name="_subject" value="New Contact Form Submission - E Green Solution">
                            <input type="hidden" name="_page" value="contact">

                            <div class="dt-form-group">
                                <label class="dt-label">Full Name *</label>
                                <input type="text" name="fullName" required placeholder="e.g. Ramesh Kulkarni" class="dt-input">
                            </div>

                            <div class="dt-form-group">
                                <label class="dt-label">Mobile / WhatsApp Number *</label>
                                <input type="tel" name="phone" required placeholder="10-digit mobile number" class="dt-input">
                            </div>

                            <div class="dt-form-group">
                                <label class="dt-label">City / Area in Pune *</label>
                                <input type="text" name="city" required placeholder="e.g. Baner, Chakan, PCMC, Kothrud" class="dt-input">
                            </div>

                            <div class="dt-form-group">
                                <label class="dt-label">Project Details / Message</label>
                                <textarea name="message" rows="3" placeholder="Tell us about your property type (bungalow, society, factory) or monthly power bill..." class="dt-textarea"></textarea>
                            </div>

                            <button type="submit" class="dt-btn dt-btn-primary submit-btn" style="width: 100%; padding: 15px; font-size: 15px;">
                                Schedule Free Site Survey &rarr;
                            </button>
                            <span style="font-size: 11.5px; color: var(--text-muted); text-align: center; display: block;">
                                <i class="fas fa-lock" style="color: var(--gold-accent);"></i> Zero spam • Direct engineer consultation • No sales pressure
                            </span>
                        </form>
                    </div>
                </div>

                <!-- Right: Official Contact Details & Map -->
                <div>
                    <div style="background: var(--bg-surface); border: 1px solid var(--border-muted); border-radius: var(--radius-container); padding: 36px; margin-bottom: 28px;">
                        <span class="dt-tech-label">OFFICE INFORMATION</span>
                        <h3 style="font-size: 20px; color: var(--text-primary); margin: 10px 0 20px;">E Green Solution Pune HQ</h3>

                        <div class="dt-footer-contact-item" style="margin-bottom: 20px;">
                            <i class="fas fa-map-marker-alt" style="font-size: 18px; color: var(--gold-accent); margin-top: 3px;"></i>
                            <div>
                                <strong style="color: var(--text-primary); display: block; font-size: 14.5px;">Registered Office Address:</strong>
                                <span style="font-size: 14px; color: var(--text-secondary); line-height: 1.6; display: block; margin-top: 4px;">
                                    Plot No 12, Ground floor, Hira Banglow, Vidyadeep Society, Gulabnagar, Dhankawadi, Pune, Maharashtra 411043
                                </span>
                            </div>
                        </div>

                        <div class="dt-footer-contact-item" style="margin-bottom: 20px;">
                            <i class="fas fa-phone-alt" style="font-size: 16px; color: var(--gold-accent); margin-top: 3px;"></i>
                            <div>
                                <strong style="color: var(--text-primary); display: block; font-size: 14.5px;">Phone / Technical Helpline:</strong>
                                <a href="tel:+917249187969" style="font-size: 15px; color: var(--gold-accent); font-weight: 700; margin-top: 4px; display: inline-block;">
                                    +91 72491 87969
                                </a>
                            </div>
                        </div>

                        <div class="dt-footer-contact-item" style="margin-bottom: 20px;">
                            <i class="fab fa-whatsapp" style="font-size: 18px; color: #4ade80; margin-top: 3px;"></i>
                            <div>
                                <strong style="color: var(--text-primary); display: block; font-size: 14.5px;">Instant WhatsApp Consultation:</strong>
                                <a href="https://wa.me/917249187969?text=Hello%20E%20Green%20Solution,%20I%20would%20like%20to%20request%20a%20solar%20site%20survey" target="_blank" rel="noopener noreferrer" style="font-size: 14.5px; color: #4ade80; font-weight: 600; margin-top: 4px; display: inline-block;">
                                    Chat with an Engineer &rarr;
                                </a>
                            </div>
                        </div>

                        <div class="dt-footer-contact-item" style="margin-bottom: 20px;">
                            <i class="fas fa-envelope" style="font-size: 16px; color: var(--gold-accent); margin-top: 3px;"></i>
                            <div>
                                <strong style="color: var(--text-primary); display: block; font-size: 14.5px;">Official Email:</strong>
                                <a href="mailto:egreensolution1@gmail.com" style="font-size: 14px; color: var(--text-secondary); margin-top: 4px; display: inline-block;">
                                    egreensolution1@gmail.com
                                </a>
                            </div>
                        </div>

                        <div class="dt-footer-contact-item">
                            <i class="fas fa-clock" style="font-size: 16px; color: var(--gold-accent); margin-top: 3px;"></i>
                            <div>
                                <strong style="color: var(--text-primary); display: block; font-size: 14.5px;">Working Hours:</strong>
                                <span style="font-size: 14px; color: var(--text-secondary); display: block; margin-top: 4px;">
                                    Mon – Sat: 09:00 AM – 07:00 PM
                                </span>
                            </div>
                        </div>
                    </div>

                    <!-- Google Map Embed -->
                    <div style="border-radius: var(--radius-card); overflow: hidden; border: 1px solid var(--border-emp); height: 260px;">
                        <iframe 
                            src="https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3784.453303102434!2d73.85078810000001!3d18.465131799999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMTjCsDI3JzU0LjUiTiA3M8KwNTEnMTIuMSJF!5e0!3m2!1sen!2sin!4v1714981358054!5m2!1sen!2sin" 
                            width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="E Green Solution Pune Location">
                        </iframe>
                    </div>
                </div>

            </div>
        </div>
    </section>

{get_dt_footer()}
    <script src="/js/supabase-config.js" defer></script>
    <script src="/js/main.js" defer></script>
    <script>
    document.addEventListener('DOMContentLoaded', () => {{
        const emailReady = typeof emailjs !== 'undefined' && typeof EMAILJS_PUBLIC_KEY !== 'undefined';
        if (emailReady) emailjs.init(EMAILJS_PUBLIC_KEY);
        const form = document.getElementById('solar-form');
        if (form) {{
            form.addEventListener('submit', async (e) => {{
                e.preventDefault();
                const submitBtn = form.querySelector('.submit-btn');
                const originalBtnText = submitBtn.innerText;
                
                submitBtn.disabled = true;
                submitBtn.innerText = 'Sending...';
                
                const formData = new FormData(form);
                const leadData = {{
                    full_name: formData.get('fullName'),
                    phone: formData.get('phone'),
                    city: formData.get('city'),
                    message: formData.get('message'),
                    status: 'New'
                }};

                try {{
                    if (typeof _supabase !== 'undefined') {{
                        await _supabase.from('leads').insert([leadData]);
                        console.log('Lead synced to Admin Panel');
                    }}
                    form.submit(); 
                }} catch (err) {{
                    console.error('Submission sync error:', err);
                    form.submit();
                }} finally {{
                    submitBtn.disabled = false;
                    submitBtn.innerText = originalBtnText;
                }}
            }});
        }}
    }});
    </script>
</body>
</html>'''

    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    print('Converted contact.html successfully!')

def convert_privacy_page():
    with open('privacy-policy.html', 'r', encoding='utf-8') as f:
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

    middle = content[content.find('<main'):content.find('</main>') + 7] if '<main' in content else ''
    if not middle:
        sec_start = content.find('<section')
        sec_end = content.find('<footer')
        middle = content[sec_start:sec_end] if sec_start != -1 and sec_end != -1 else ''
    
    cleaned_middle = clean_html_content(middle)

    page_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{gtag}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy | E Green Solution Pune</title>
    <meta name="description" content="Privacy Policy of E Green Solution. Learn how we handle your contact information, site data, and lead privacy in compliance with Indian IT regulations.">
    <link rel="canonical" href="https://egreensolution.in/privacy-policy">

    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon.png">
    <link rel="apple-touch-icon" href="/assets/logo.png">

    <!-- Schema.org Data -->
    {schemas_str}

{get_dt_head_tags()}
</head>
<body class="tech-grid-bg">
{get_dt_navbar('')}

    <section class="dt-subpage-hero">
        <div class="dt-container">
            <div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <span class="current">Privacy Policy</span>
            </div>

            <div style="max-width: 860px;">
                <div class="dt-tech-label">LEGAL INFORMATION</div>
                <h1 class="dt-hero-title" style="font-size: clamp(34px, 4.4vw, 52px); margin-bottom: 20px;">
                    Privacy Policy &amp; Data Security
                </h1>
                <p class="dt-section-desc" style="font-size: 17px; line-height: 1.8;">
                    Last updated: October 2026. This policy describes how E Green Solution collects, uses, and safeguards information obtained through egreensolution.in.
                </p>
            </div>
        </div>
    </section>

    <div class="dt-container dt-prose" style="max-width: 900px; padding: 70px 28px;">
        {cleaned_middle}
    </div>

{get_dt_footer()}
</body>
</html>'''

    with open('privacy-policy.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    print('Converted privacy-policy.html successfully!')

if __name__ == '__main__':
    convert_about_page()
    convert_calculator_page()
    convert_contact_page()
    convert_privacy_page()
