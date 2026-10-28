import os
import sys
import re

sys.path.append(os.path.abspath('scripts'))
from dark_theme_components import get_dt_head_tags, get_dt_navbar, get_dt_footer

def extract_head_essentials(html_content, default_title, default_canonical):
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.DOTALL)
    title = title_match.group(0) if title_match else f'<title>{default_title}</title>'
    
    desc_match = re.search(r'<meta name="description" content="([^"]*)">', html_content)
    desc = desc_match.group(0) if desc_match else ''
    
    keywords_match = re.search(r'<meta name="keywords" content="([^"]*)">', html_content)
    keywords = keywords_match.group(0) if keywords_match else ''
    
    canonical_match = re.search(r'<link rel="canonical" href="([^"]*)">', html_content)
    canonical = canonical_match.group(0) if canonical_match else f'<link rel="canonical" href="{default_canonical}">'
    
    schemas = re.findall(r'<script type="application/ld\+json">.*?</script>', html_content, re.DOTALL)
    schemas_str = '\n    '.join(schemas)

    gtag = '''    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-6RB8MHEG1S"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-6RB8MHEG1S');
    </script>'''

    head = f'''<!DOCTYPE html>
<html lang="en">
<head>
{gtag}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {title}
    {desc}
    {keywords}
    {canonical}

    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon.png">
    <link rel="apple-touch-icon" href="/assets/logo.png">

    <!-- Schema.org Data -->
    {schemas_str}

{get_dt_head_tags()}
</head>'''
    return head

# ==============================================================================
# 1. RESIDENTIAL SOLAR
# ==============================================================================
def convert_residential_solar():
    with open('residential-solar.html', 'r', encoding='utf-8') as f:
        orig = f.read()
    
    head = extract_head_essentials(orig, "Solar Panels for Home Pune | Residential Rooftop Solar", "https://egreensolution.in/residential-solar")
    
    body = f'''{head}
<body class="tech-grid-bg">
{get_dt_navbar('services')}

    <section class="dt-subpage-hero">
        <div class="dt-container">
            <div class="dt-breadcrumbs">
                <a href="/">Home</a>
                <span class="sep">/</span>
                <a href="/services">Services</a>
                <span class="sep">/</span>
                <span class="current">Residential Solar</span>
            </div>

            <div class="dt-subpage-grid">
                <div>
                    <div class="dt-tech-label">02 // RESIDENTIAL ROOFTOP PHOTOVOLTAICS</div>
                    <h1 class="dt-hero-title" style="font-size: clamp(34px, 4.2vw, 52px); margin-bottom: 20px;">
                        Solar Panels for Home in Pune
                    </h1>
                    <p class="dt-section-desc" style="margin-bottom: 28px;">
                        Slash monthly electricity bills by up to 90%. Receive direct bank transfer subsidy up to ₹78,000 under the PM Surya Ghar Muft Bijli Yojana with seamless MSEDCL net metering and 25-year performance warranties.
                    </p>

                    <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px;">
                        <span class="dt-pill"><i class="fas fa-file-invoice-dollar" style="color: var(--gold-accent);"></i> Up to ₹78,000 Direct Subsidy</span>
                        <span class="dt-pill"><i class="fas fa-shield-alt" style="color: var(--gold-accent);"></i> 25-Year Linear Warranty</span>
                        <span class="dt-pill"><i class="fas fa-bolt" style="color: var(--gold-accent);"></i> Vikram Solar 550W+ Modules</span>
                        <span class="dt-pill"><i class="fas fa-chart-line" style="color: var(--gold-accent);"></i> ~3.2 Year Payback Period</span>
                    </div>

                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; background: var(--bg-surface); border: 1px solid var(--border-muted); border-radius: var(--radius-card); padding: 18px;">
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--gold-accent); display: block;">₹78k</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Max Subsidy</span>
                        </div>
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--text-primary); display: block;">90%</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Bill Reduction</span>
                        </div>
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--gold-accent); display: block;">3-5 Days</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Installation</span>
                        </div>
                    </div>
                </div>

                <div>
                    <div class="dt-form-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                            <span class="dt-tech-label" style="margin: 0;">PM SURYA GHAR</span>
                            <span style="font-size: 11px; color: #4ade80;"><i class="fas fa-circle" style="font-size: 8px;"></i> Fast Approval</span>
                        </div>
                        <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 6px;">Claim Home Solar Subsidy</h3>
                        <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px;">Get exact sizing, subsidy calculation, and quote for your home.</p>

                        <form action="https://formspree.io/f/xbjnqkyw" method="POST" style="display: flex; flex-direction: column; gap: 14px;">
                            <input type="hidden" name="_subject" value="Residential Solar Inquiry - Pune">
                            <input type="hidden" name="_page" value="residential-solar">

                            <div class="dt-form-group">
                                <label class="dt-label">Full Name *</label>
                                <input type="text" name="name" required placeholder="e.g. Anand Deshmukh" class="dt-input">
                            </div>

                            <div class="dt-form-group">
                                <label class="dt-label">Mobile / WhatsApp Number *</label>
                                <input type="tel" name="phone" required placeholder="e.g. 98765 43210" class="dt-input">
                            </div>

                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                                <div class="dt-form-group">
                                    <label class="dt-label">Location in Pune</label>
                                    <input type="text" name="location" placeholder="e.g. Baner, Wakad" class="dt-input">
                                </div>
                                <div class="dt-form-group">
                                    <label class="dt-label">System Size</label>
                                    <select name="requirement" class="dt-select">
                                        <option value="3 kW (Best for 2-3 BHK)">3 kW (2-3 BHK)</option>
                                        <option value="5 kW (Bungalow / 4 BHK)">5 kW (Bungalow)</option>
                                        <option value="10 kW+ (Large Villa / Society)">10 kW+ (Villa/Society)</option>
                                    </select>
                                </div>
                            </div>

                            <button type="submit" class="dt-btn dt-btn-primary" style="width: 100%; margin-top: 6px;">
                                Calculate Subsidy &amp; Quote <i class="fas fa-arrow-right"></i>
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Solar for Home -->
    <section class="dt-section">
        <div class="dt-container">
            <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 50px; align-items: center;">
                <div>
                    <div class="dt-tech-label">ECONOMIC INDEPENDENCE</div>
                    <h2 class="dt-section-title">Lock in Zero-Cost Power for 25 Years</h2>
                    <p class="dt-section-desc">
                        In Pune, MSEDCL residential electricity slab rates reach over ₹14 per unit. A customized rooftop solar power plant eliminates 80% to 90% of your ongoing power expenses while shielding your family against rising utility tariffs.
                    </p>
                    <ul class="dt-feature-list">
                        <li><i class="fas fa-check-circle"></i> <strong>Vikram Solar TOPCon Modules:</strong> Advanced bifacial cells absorbing reflected sunlight from white terrace tiles for 10-15% extra yield.</li>
                        <li><i class="fas fa-check-circle"></i> <strong>Smart On-Grid Inverter:</strong> High-frequency dual-MPPT inverters with WiFi telemetry and smartphone yield monitoring.</li>
                        <li><i class="fas fa-check-circle"></i> <strong>Elevated Structure Options:</strong> Raised GI structures allowing full usable terrace area for walking or leisure beneath panels.</li>
                        <li><i class="fas fa-check-circle"></i> <strong>100% Paperwork Handling:</strong> We manage DISCOM sanctions, net meter testing, and national portal subsidy documentation end-to-end.</li>
                    </ul>
                </div>
                <div style="border-radius: var(--radius-container); overflow: hidden; border: 1px solid var(--border-emp); height: 380px;">
                    <img src="/assets/services/residential_solar_pune.jpg" alt="Residential Solar Rooftop Pune" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
            </div>
        </div>
    </section>

    <!-- Technical Specification Table for Residential Systems -->
    <section class="dt-section dt-section-surface">
        <div class="dt-container">
            <div class="dt-section-header center">
                <div class="dt-tech-label">SYSTEM COMPARISON SPECIFICATIONS</div>
                <h2 class="dt-section-title">Residential System Capacities &amp; Subsidies</h2>
                <p class="dt-section-desc" style="margin: 0 auto;">
                    Standard configurations engineered for typical Pune homes under the PM Surya Ghar scheme.
                </p>
            </div>

            <div class="dt-table-wrap">
                <table class="dt-table">
                    <thead>
                        <tr>
                            <th>System Capacity</th>
                            <th>Recommended Property</th>
                            <th>Monthly Generation</th>
                            <th>PM Surya Ghar Subsidy</th>
                            <th>Roof Area Needed</th>
                            <th>Typical ROI</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="highlight">3 kW System</td>
                            <td>2–3 BHK Flat / Row House</td>
                            <td>360 – 420 Units</td>
                            <td class="highlight">₹78,000</td>
                            <td>~300 sq.ft.</td>
                            <td>3.2 Years</td>
                        </tr>
                        <tr>
                            <td class="highlight">5 kW System</td>
                            <td>3–4 BHK Bungalow / Duplex</td>
                            <td>600 – 700 Units</td>
                            <td class="highlight">₹78,000</td>
                            <td>~500 sq.ft.</td>
                            <td>3.4 Years</td>
                        </tr>
                        <tr>
                            <td class="highlight">10 kW System</td>
                            <td>Large Villa / Housing Society Common</td>
                            <td>1,200 – 1,400 Units</td>
                            <td class="highlight">₹78,000 + GHS</td>
                            <td>~1,000 sq.ft.</td>
                            <td>3.0 Years</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- Featured Housing Society Case Study -->
    <section class="dt-section">
        <div class="dt-container">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-container); padding: 44px; display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 40px; align-items: center;">
                <div>
                    <span class="dt-tech-label"><i class="fas fa-building"></i> FEATURED HOUSING SOCIETY SPOTLIGHT</span>
                    <h3 style="font-size: clamp(24px, 2.8vw, 34px); color: var(--text-primary); margin: 12px 0 16px;">Konark A Plus Society — 100kW Commissioned Rooftop</h3>
                    <p style="font-size: 15px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 20px;">
                        See how a premier housing society in Sopan Baug, Pune slashed their monthly MSEDCL power bill from ₹3.2+ Lakhs down to ~₹32,000 for common elevators, water pumps, and lighting with ₹18 Lakhs central subsidy support.
                    </p>
                    <div style="display: flex; gap: 16px; margin-bottom: 24px;">
                        <div style="background: var(--bg-elevated); padding: 12px 18px; border-radius: var(--radius-ctrl); border: 1px solid var(--border-muted);">
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 700; color: #4ade80; display: block;">90%</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Bill Reduction</span>
                        </div>
                        <div style="background: var(--bg-elevated); padding: 12px 18px; border-radius: var(--radius-ctrl); border: 1px solid var(--border-muted);">
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 700; color: var(--gold-accent); display: block;">₹18 Lakhs</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Central Subsidy</span>
                        </div>
                        <div style="background: var(--bg-elevated); padding: 12px 18px; border-radius: var(--radius-ctrl); border: 1px solid var(--border-muted);">
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 700; color: var(--text-primary); display: block;">&lt; 3 Years</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Full Payback</span>
                        </div>
                    </div>
                    <a href="/projects/konark-a-plus-100kw-housing-society-solar-pune" class="dt-btn dt-btn-primary">
                        Read Full 100kW Case Study &rarr;
                    </a>
                </div>
                <div style="border-radius: var(--radius-card); overflow: hidden; border: 1px solid var(--border-emp); height: 320px;">
                    <img src="/assets/projects/konark_society_rooftop_100kw.jpg" alt="100kW Rooftop Solar Konark A Plus Housing Society Pune" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
            </div>
        </div>
    </section>

    <!-- Residential FAQ -->
    <section class="dt-section dt-section-surface">
        <div class="dt-container">
            <div class="dt-section-header center">
                <div class="dt-tech-label">RESIDENTIAL FAQ</div>
                <h2 class="dt-section-title">Homeowner Questions Answered</h2>
            </div>

            <div class="dt-faq-list">
                <div class="dt-faq-item active">
                    <button type="button" class="dt-faq-btn">
                        <span>How much does a 3 kW solar system cost for a home in Pune after subsidy?</span>
                        <div class="dt-faq-icon"><i class="fas fa-plus"></i></div>
                    </button>
                    <div class="dt-faq-content">
                        A premium 3 kW turnkey rooftop solar system with Vikram Solar TOPCon modules and an on-grid smart inverter costs approximately ₹1,90,000 to ₹2,15,000 before subsidy. With the ₹78,000 direct PM Surya Ghar subsidy deposited into your account, your net investment is only around ₹1,15,000 to ₹1,35,000, recovering your entire capital within ~3.2 years.
                    </div>
                </div>

                <div class="dt-faq-item">
                    <button type="button" class="dt-faq-btn">
                        <span>How does net metering work with MSEDCL in Maharashtra?</span>
                        <div class="dt-faq-icon"><i class="fas fa-plus"></i></div>
                    </button>
                    <div class="dt-faq-content">
                        MSEDCL replaces your regular meter with a bidirectional net meter. During the day, power produced by your solar panels runs your home loads first; excess units are automatically pushed into the MSEDCL grid. At night, you draw power from the grid. In your bill, exported units are subtracted from imported units, dropping your bill to zero or the minimum fixed meter charge.
                    </div>
                </div>

                <div class="dt-faq-item">
                    <button type="button" class="dt-faq-btn">
                        <span>Can solar panels be installed on elevated structures without blocking terrace use?</span>
                        <div class="dt-faq-icon"><i class="fas fa-plus"></i></div>
                    </button>
                    <div class="dt-faq-content">
                        Yes! E Green Solution specializes in elevated rooftop solar structures (raised 8 to 10 feet above terrace level). This protects the entire usable terrace area for walking, rooftop gardens, or family gatherings while providing solar power and naturally insulating the floor below against summer heat.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Global CTA -->
    <section class="dt-section">
        <div class="dt-container" style="text-align: center;">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-container); padding: 50px; max-width: 860px; margin: 0 auto;">
                <div class="dt-tech-label" style="margin: 0 auto 16px;">ZERO OBLIGATION CONSULTATION</div>
                <h2 style="font-size: clamp(28px, 3.4vw, 40px); color: var(--text-primary); margin-bottom: 14px;">Switch Your Home to Solar Energy Today</h2>
                <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 28px;">
                    Our certified solar engineers will inspect your terrace, conduct 3D shadow analysis, and calculate your exact savings and subsidy entitlement.
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

    with open('residential-solar.html', 'w', encoding='utf-8') as f:
        f.write(body)
    print('Converted residential-solar.html successfully!')

if __name__ == '__main__':
    convert_residential_solar()
