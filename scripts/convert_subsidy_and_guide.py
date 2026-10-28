import os
import sys
import re

sys.path.append(os.path.abspath('scripts'))
from dark_theme_components import get_dt_head_tags, get_dt_navbar, get_dt_footer
from convert_services_group import clean_html_content

def convert_solar_subsidy():
    with open('solar-subsidy.html', 'r', encoding='utf-8') as f:
        content = f.read()

    title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    title = title_m.group(0) if title_m else '<title>Solar Subsidy Pune | PM Surya Ghar Muft Bijli Yojana</title>'

    desc_m = re.search(r'<meta name="description" content="([^"]*)">', content)
    desc = desc_m.group(0) if desc_m else ''

    kw_m = re.search(r'<meta name="keywords" content="([^"]*)">', content)
    kw = kw_m.group(0) if kw_m else ''

    canon_m = re.search(r'<link rel="canonical" href="([^"]*)">', content)
    canonical = canon_m.group(0) if canon_m else '<link rel="canonical" href="https://egreensolution.in/solar-subsidy">'

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

    # Middle content
    header_end = content.find('</header>')
    middle = content[header_end + 9:] if header_end != -1 else ''
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
{get_dt_navbar('subsidy')}

    <!-- ============================================================
         SUBPAGE HERO (Dark Technical Editorial)
         ============================================================ -->
    <section class="dt-subpage-hero">
        <div class="dt-container">
            <div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <span class="current">Solar Subsidy</span>
            </div>

            <div class="dt-subpage-grid">
                <div>
                    <div class="dt-tech-label">CENTRAL GOVERNMENT INCENTIVE</div>
                    <h1 class="dt-hero-title" style="font-size: clamp(34px, 4.2vw, 52px); margin-bottom: 20px;">
                        PM Surya Ghar Solar Subsidy in Pune
                    </h1>
                    <p class="dt-section-desc" style="margin-bottom: 28px;">
                        Under the PM Surya Ghar: Muft Bijli Yojana, eligible individual homeowners in Maharashtra receive direct central bank transfer subsidies up to ₹78,000, while Housing Societies (GHS/RWA) receive ₹18,000 per kW up to 500 kW. E Green Solution handles the entire National Portal workflow on your behalf.
                    </p>

                    <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px;">
                        <span class="dt-pill"><i class="fas fa-file-invoice-dollar" style="color: var(--gold-accent);"></i> ₹30,000 for 1 kW</span>
                        <span class="dt-pill"><i class="fas fa-file-invoice-dollar" style="color: var(--gold-accent);"></i> ₹60,000 for 2 kW</span>
                        <span class="dt-pill"><i class="fas fa-file-invoice-dollar" style="color: var(--gold-accent);"></i> ₹78,000 for 3 kW+</span>
                        <span class="dt-pill"><i class="fas fa-building" style="color: var(--gold-accent);"></i> ₹18,000/kW for Societies</span>
                    </div>

                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; background: var(--bg-surface); border: 1px solid var(--border-muted); border-radius: var(--radius-card); padding: 18px;">
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--gold-accent); display: block;">₹78,000</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Max Home Subsidy</span>
                        </div>
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--text-primary); display: block;">30 Days</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Direct DBT Credit</span>
                        </div>
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--gold-accent); display: block;">100%</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Portal Assistance</span>
                        </div>
                    </div>
                </div>

                <div>
                    <div class="dt-form-card">
                        <span class="dt-tech-label" style="margin-bottom: 12px;">CHECK SUBSIDY ELIGIBILITY</span>
                        <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 6px;">Claim Your PM Surya Ghar Subsidy</h3>
                        <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px;">We check your MSEDCL consumer number, roof viability, and file your national subsidy portal application.</p>

                        <form action="https://formspree.io/f/xbjnqkyw" method="POST" style="display: flex; flex-direction: column; gap: 14px;">
                            <input type="hidden" name="_subject" value="PM Surya Ghar Subsidy Application - Pune">
                            <input type="hidden" name="_page" value="solar-subsidy">

                            <div class="dt-form-group">
                                <label class="dt-label">Full Name *</label>
                                <input type="text" name="name" required placeholder="Full Name as per Electricity Bill" class="dt-input">
                            </div>

                            <div class="dt-form-group">
                                <label class="dt-label">Mobile Number (Aadhaar linked) *</label>
                                <input type="tel" name="phone" required placeholder="10-digit Mobile Number" class="dt-input">
                            </div>

                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                                <div class="dt-form-group">
                                    <label class="dt-label">Pune Location</label>
                                    <input type="text" name="location" placeholder="e.g. Baner, Wakad" class="dt-input">
                                </div>
                                <div class="dt-form-group">
                                    <label class="dt-label">Property Type</label>
                                    <select name="property_type" class="dt-select">
                                        <option value="Independent Bungalow / Row House">Individual Bungalow</option>
                                        <option value="Apartment / Top Floor Flat">Apartment Flat</option>
                                        <option value="Housing Society (RWA / Common Meter)">Housing Society RWA</option>
                                    </select>
                                </div>
                            </div>

                            <button type="submit" class="dt-btn dt-btn-primary" style="width: 100%; margin-top: 6px;">
                                Check My Subsidy &rarr;
                            </button>
                        </form>
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
                <div class="dt-tech-label" style="margin: 0 auto 16px;">END-TO-END PORTAL SUBMISSION</div>
                <h2 style="font-size: clamp(28px, 3.4vw, 40px); color: var(--text-primary); margin-bottom: 14px;">Let Us Handle Your Subsidy Paperwork</h2>
                <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 28px;">
                    From Aadhaar OTP authentication to net meter testing report upload and final DBT bank disbursement, our compliance team ensures you get 100% of your entitled subsidy.
                </p>
                <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
                    <a href="/contact" class="dt-btn dt-btn-primary">Apply for PM Surya Ghar &rarr;</a>
                    <a href="tel:+917249187969" class="dt-btn dt-btn-secondary"><i class="fas fa-phone-alt"></i> +91 72491 87969</a>
                </div>
            </div>
        </div>
    </section>

{get_dt_footer()}
</body>
</html>'''

    with open('solar-subsidy.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    print('Converted solar-subsidy.html successfully!')

def convert_solar_guide():
    with open('solar-guide.html', 'r', encoding='utf-8') as f:
        content = f.read()

    title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    title = title_m.group(0) if title_m else '<title>Solar 101 Knowledge Guide | E Green Solution Pune</title>'

    desc_m = re.search(r'<meta name="description" content="([^"]*)">', content)
    desc = desc_m.group(0) if desc_m else ''

    kw_m = re.search(r'<meta name="keywords" content="([^"]*)">', content)
    kw = kw_m.group(0) if kw_m else ''

    canon_m = re.search(r'<link rel="canonical" href="([^"]*)">', content)
    canonical = canon_m.group(0) if canon_m else '<link rel="canonical" href="https://egreensolution.in/solar-guide">'

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

    # Middle content
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
{get_dt_navbar('guide')}

    <!-- ============================================================
         SUBPAGE HERO (Dark Technical Editorial)
         ============================================================ -->
    <section class="dt-subpage-hero">
        <div class="dt-container">
            <div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <span class="current">Solar 101 Knowledge Guide</span>
            </div>

            <div style="max-width: 860px;">
                <div class="dt-tech-label">SOLAR 101 // ENGINEERING KNOWLEDGE BASE</div>
                <h1 class="dt-hero-title" style="font-size: clamp(34px, 4.4vw, 54px); margin-bottom: 20px;">
                    Everything You Need to Know About Solar Energy
                </h1>
                <p class="dt-section-desc" style="font-size: 18px; line-height: 1.8; margin-bottom: 30px;">
                    The complete, no-jargon technical guide for homeowners, housing societies, and business owners in Pune. Understand how photovoltaic cells generate power, how MSEDCL bi-directional net metering works, equipment warranties, and real-world capital payback.
                </p>

                <div style="display: flex; flex-wrap: wrap; gap: 12px;">
                    <a href="#basics" class="dt-btn dt-btn-secondary"><i class="fas fa-solar-panel"></i> How Solar Works</a>
                    <a href="#costs" class="dt-btn dt-btn-secondary"><i class="fas fa-calculator"></i> Costs &amp; Subsidies</a>
                    <a href="#roi" class="dt-btn dt-btn-secondary"><i class="fas fa-chart-line"></i> Payback Period</a>
                    <a href="/calculator" class="dt-btn dt-btn-primary">Try Savings Calculator &rarr;</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Content Sections wrapped in dt-prose -->
    <div class="dt-container dt-prose" style="padding: 70px 28px;">
        {cleaned_middle}
    </div>

    <!-- Global CTA -->
    <section class="dt-section" style="background: var(--bg-surface); border-top: 1px solid var(--border-muted);">
        <div class="dt-container" style="text-align: center;">
            <div style="max-width: 800px; margin: 0 auto;">
                <div class="dt-tech-label" style="margin: 0 auto 16px;">BEGIN YOUR SOLAR JOURNEY</div>
                <h2 style="font-size: clamp(28px, 3.4vw, 40px); color: var(--text-primary); margin-bottom: 14px;">Ready to Stop Paying Electricity Bills?</h2>
                <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 28px;">
                    Join over 200 satisfied property owners across Pune and Maharashtra who trust E Green Solution for turnkey engineering.
                </p>
                <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
                    <a href="/contact" class="dt-btn dt-btn-primary">Book Free Site Survey &rarr;</a>
                    <a href="/calculator" class="dt-btn dt-btn-secondary"><i class="fas fa-calculator"></i> Calculate Savings</a>
                </div>
            </div>
        </div>
    </section>

{get_dt_footer()}
</body>
</html>'''

    with open('solar-guide.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    print('Converted solar-guide.html successfully!')

if __name__ == '__main__':
    convert_solar_subsidy()
    convert_solar_guide()
