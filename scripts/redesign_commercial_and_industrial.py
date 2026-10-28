import os
import sys
import re

sys.path.append(os.path.abspath('scripts'))
from dark_theme_components import get_dt_head_tags, get_dt_navbar, get_dt_footer

def convert_commercial_solar():
    with open('commercial-solar-pune.html', 'r', encoding='utf-8') as f:
        orig = f.read()

    # Extract schema scripts
    schemas = re.findall(r'<script type="application/ld\+json">.*?</script>', orig, re.DOTALL)
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
    <title>Commercial Solar Installation Pune | Offices, Hospitals & Malls</title>
    <meta name="description" content="Turnkey commercial rooftop solar EPC for corporate offices, hospitals, IT parks, colleges, and malls across Pune. Save up to 80% with under 3.2-year payback and 40% depreciation.">
    <meta name="keywords" content="commercial solar installation pune, commercial rooftop solar pune, solar for offices pune, solar for hospitals pune, commercial solar panel price pune, solar depreciation benefits india">
    <link rel="canonical" href="https://egreensolution.in/commercial-solar-pune">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://egreensolution.in/commercial-solar-pune">
    <meta property="og:title" content="Commercial Solar EPC &amp; Installation in Pune | E Green Solution">
    <meta property="og:description" content="Turnkey rooftop solar EPC for offices, hospitals, IT parks, and malls in Pune. 40% Section 32 depreciation and under 3.2-year payback.">
    <meta property="og:image" content="https://egreensolution.in/assets/services/commercial_solar_pune.jpg">

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
                <span class="current">Commercial Solar</span>
            </div>

            <div class="dt-subpage-grid">
                <div>
                    <div class="dt-tech-label">03 // COMMERCIAL &amp; INSTITUTIONAL EPC</div>
                    <h1 class="dt-hero-title" style="font-size: clamp(34px, 4.2vw, 52px); margin-bottom: 20px;">
                        Commercial Solar Installation in Pune
                    </h1>
                    <p class="dt-section-desc" style="margin-bottom: 28px;">
                        Displace expensive commercial tariffs (₹11–₹14+/kWh) with zero-cost daytime solar power. Benefit from 40% Section 32 accelerated depreciation tax offsets and under 3.2-year capital payback for corporate offices, hospitals, colleges, and commercial complexes.
                    </p>

                    <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px;">
                        <span class="dt-pill"><i class="fas fa-chart-line" style="color: var(--gold-accent);"></i> 2.8 – 3.2 Yrs Capital Payback</span>
                        <span class="dt-pill"><i class="fas fa-file-invoice-dollar" style="color: var(--gold-accent);"></i> 40% Section 32 Depreciation</span>
                        <span class="dt-pill"><i class="fas fa-bolt" style="color: var(--gold-accent);"></i> MSEDCL HT/LT Net Metering</span>
                        <span class="dt-pill"><i class="fas fa-shield-alt" style="color: var(--gold-accent);"></i> 25-Year Linear Warranty</span>
                    </div>

                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; background: var(--bg-surface); border: 1px solid var(--border-muted); border-radius: var(--radius-card); padding: 18px;">
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--gold-accent); display: block;">65–80%</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Daytime Reduction</span>
                        </div>
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--text-primary); display: block;">&lt; ₹2.50</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">LCOE Per Unit</span>
                        </div>
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--gold-accent); display: block;">15kW–1MW</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">System Sizes</span>
                        </div>
                    </div>
                </div>

                <div>
                    <div class="dt-form-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                            <span class="dt-tech-label" style="margin: 0;">COMMERCIAL AUDIT</span>
                            <span style="font-size: 11px; color: #4ade80;"><i class="fas fa-circle" style="font-size: 8px;"></i> Engineer Response</span>
                        </div>
                        <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 6px;">Request Commercial Feasibility</h3>
                        <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px;">Get a detailed commercial ROI, tariff displacement, and structural proposal.</p>

                        <form action="https://formspree.io/f/xbjnqkyw" method="POST" style="display: flex; flex-direction: column; gap: 14px;">
                            <input type="hidden" name="_subject" value="Commercial Solar Feasibility Request - Pune">
                            <input type="hidden" name="_page" value="commercial-solar-pune">

                            <div class="dt-form-group">
                                <label class="dt-label">Company / Entity Name *</label>
                                <input type="text" name="company_name" required placeholder="e.g. Phoenix IT Park / Ruby Clinic" class="dt-input">
                            </div>

                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                                <div class="dt-form-group">
                                    <label class="dt-label">Contact Person *</label>
                                    <input type="text" name="name" required placeholder="e.g. Rahul Patil" class="dt-input">
                                </div>
                                <div class="dt-form-group">
                                    <label class="dt-label">Mobile / Phone *</label>
                                    <input type="tel" name="phone" required placeholder="e.g. 98765 43210" class="dt-input">
                                </div>
                            </div>

                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                                <div class="dt-form-group">
                                    <label class="dt-label">Sector</label>
                                    <select name="sector" class="dt-select">
                                        <option value="Corporate Office / IT Park">Corporate Office / IT Park</option>
                                        <option value="Hospital / Healthcare">Hospital / Healthcare</option>
                                        <option value="Hotel / Resort / Banquet">Hotel / Resort / Banquet</option>
                                        <option value="School / College / Institute">School / College / Institute</option>
                                        <option value="Mall / Commercial Complex">Mall / Commercial Complex</option>
                                        <option value="Housing Society Common">Housing Society Common</option>
                                    </select>
                                </div>
                                <div class="dt-form-group">
                                    <label class="dt-label">Monthly Power Bill</label>
                                    <select name="monthly_bill" class="dt-select">
                                        <option value="₹50k - ₹1.5L">₹50,000 – ₹1.5 Lakhs</option>
                                        <option value="₹1.5L - ₹3.0L">₹1.5 – ₹3.0 Lakhs</option>
                                        <option value="₹3.0L - ₹10L+">₹3.0 – ₹10 Lakhs+</option>
                                    </select>
                                </div>
                            </div>

                            <button type="submit" class="dt-btn dt-btn-primary" style="width: 100%; margin-top: 6px;">
                                Get Commercial Proposal &rarr;
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Commercial Solar Essential -->
    <section class="dt-section">
        <div class="dt-container">
            <div class="dt-section-header center">
                <div class="dt-tech-label">ECONOMIC CATALYST</div>
                <h2 class="dt-section-title">Why Rooftop Solar is Essential for Pune Businesses</h2>
                <p class="dt-section-desc" style="margin: 0 auto;">
                    Under MSEDCL commercial tariffs (LT-II and HT Commercial), enterprises pay ₹11 to ₹14+ per kWh. Because air conditioning, lighting, servers, and elevators run during daylight hours, solar directly offsets top-tier utility tariffs, creating unprecedented returns.
                </p>
            </div>

            <!-- 4 Metric Cards -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px;">
                <div class="dt-card" style="text-align: center;">
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 36px; font-weight: 700; color: var(--gold-accent); display: block; margin-bottom: 8px;">65% – 80%</span>
                    <strong style="color: var(--text-primary); font-size: 15px; display: block; margin-bottom: 6px;">Daytime Bill Displacement</strong>
                    <p style="font-size: 13px; color: var(--text-secondary); margin: 0;">Direct reduction of daytime peak units from Day 1 of commissioning.</p>
                </div>
                <div class="dt-card" style="text-align: center;">
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 36px; font-weight: 700; color: var(--text-primary); display: block; margin-bottom: 8px;">2.8 – 3.2 Yrs</span>
                    <strong style="color: var(--text-primary); font-size: 15px; display: block; margin-bottom: 6px;">Typical Capital Payback</strong>
                    <p style="font-size: 13px; color: var(--text-secondary); margin: 0;">Full capital recovery, followed by 20+ years of essentially free power.</p>
                </div>
                <div class="dt-card" style="text-align: center;">
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 36px; font-weight: 700; color: var(--gold-accent); display: block; margin-bottom: 8px;">40%</span>
                    <strong style="color: var(--text-primary); font-size: 15px; display: block; margin-bottom: 6px;">Section 32 Tax Write-off</strong>
                    <p style="font-size: 13px; color: var(--text-secondary); margin: 0;">Accelerated tax depreciation benefit under Section 32 in the first year.</p>
                </div>
                <div class="dt-card" style="text-align: center;">
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 36px; font-weight: 700; color: var(--text-primary); display: block; margin-bottom: 8px;">25 Years</span>
                    <strong style="color: var(--text-primary); font-size: 15px; display: block; margin-bottom: 6px;">Performance Warranty</strong>
                    <p style="font-size: 13px; color: var(--text-secondary); margin: 0;">Linear power generation backed by tier-1 global PV manufacturers.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Commercial Sectors Grid -->
    <section class="dt-section dt-section-surface">
        <div class="dt-container">
            <div class="dt-section-header center">
                <div class="dt-tech-label">SPECIALIZED SECTORS</div>
                <h2 class="dt-section-title">Commercial Facilities We Power in Pune &amp; PCMC</h2>
                <p class="dt-section-desc" style="margin: 0 auto;">
                    Customized mounting structures, DG-PV synchronization, and smart sub-metering tailored for each commercial category.
                </p>
            </div>

            <div class="dt-services-grid">
                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-laptop-code"></i></div>
                    <h3 class="dt-card-title">Corporate Offices &amp; Tech Parks</h3>
                    <p class="dt-card-desc">Designed for Hinjewadi, Kharadi, and Baner IT offices. Elevated pergolas preserve 100% of terrace recreational space while powering HVAC and server racks.</p>
                </div>
                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-hospital"></i></div>
                    <h3 class="dt-card-title">Hospitals &amp; Healthcare Centers</h3>
                    <p class="dt-card-desc">Continuous clean power with DG-PV synchronizer integration. Slashes operational cost per patient bed while ensuring zero interruption to critical care.</p>
                </div>
                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-hotel"></i></div>
                    <h3 class="dt-card-title">Hotels, Resorts &amp; Banquets</h3>
                    <p class="dt-card-desc">Powers central chillers, banquet hall ACs, and kitchen pumps. Solar carports double as executive covered parking with EV charging integration.</p>
                </div>
                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-graduation-cap"></i></div>
                    <h3 class="dt-card-title">Schools, Colleges &amp; Campuses</h3>
                    <p class="dt-card-desc">Banks weekend and summer vacation surplus power directly into MSEDCL's grid via net metering. Enhances green campus accreditation (NAAC).</p>
                </div>
                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-cart-shopping"></i></div>
                    <h3 class="dt-card-title">Retail Malls &amp; Showrooms</h3>
                    <p class="dt-card-desc">Significantly reduces Common Area Maintenance (CAM) electricity expenses for high-volume escalators, lighting, and AHUs.</p>
                </div>
                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-users-between-lines"></i></div>
                    <h3 class="dt-card-title">Society Common Meter Solar</h3>
                    <p class="dt-card-desc">Powers common elevators, water pumps, and clubhouse amenities. Qualifies for PM Surya Ghar Group Housing Society subsidies up to ₹18,000/kW.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Commercial Sizing Table -->
    <section class="dt-section">
        <div class="dt-container">
            <div class="dt-section-header center">
                <div class="dt-tech-label">FINANCIAL SIZING MATRIX</div>
                <h2 class="dt-section-title">Commercial Solar Sizing, Generation &amp; Savings</h2>
                <p class="dt-section-desc" style="margin: 0 auto;">
                    Modeled on Pune's average annual irradiance (5.2–5.4 kWh/m²/day) and MSEDCL commercial tariffs (avg. ₹12.50/unit).
                </p>
            </div>

            <div class="dt-table-wrap">
                <table class="dt-table">
                    <thead>
                        <tr>
                            <th>Capacity</th>
                            <th>Daily Generation</th>
                            <th>Monthly Power Units</th>
                            <th>Est. Monthly Savings</th>
                            <th>Est. Annual Savings</th>
                            <th>Roof Area</th>
                            <th>Estimated Payback</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="highlight">15 kWp</td>
                            <td>60 – 65 Units</td>
                            <td>~1,800 Units</td>
                            <td class="highlight">₹22,500 – ₹25,000</td>
                            <td>₹2.70 – ₹3.00 Lakhs</td>
                            <td>1,200 sq.ft.</td>
                            <td>3.2 Years</td>
                        </tr>
                        <tr>
                            <td class="highlight">25 kWp</td>
                            <td>100 – 110 Units</td>
                            <td>~3,100 Units</td>
                            <td class="highlight">₹38,000 – ₹42,000</td>
                            <td>₹4.50 – ₹5.00 Lakhs</td>
                            <td>2,000 sq.ft.</td>
                            <td>3.1 Years</td>
                        </tr>
                        <tr>
                            <td class="highlight">50 kWp</td>
                            <td>200 – 220 Units</td>
                            <td>~6,200 Units</td>
                            <td class="highlight">₹77,000 – ₹85,000</td>
                            <td>₹9.20 – ₹10.2 Lakhs</td>
                            <td>4,000 sq.ft.</td>
                            <td>3.0 Years</td>
                        </tr>
                        <tr>
                            <td class="highlight">100 kWp</td>
                            <td>400 – 440 Units</td>
                            <td>~12,500 Units</td>
                            <td class="highlight">₹1,55,000 – ₹1,70,000</td>
                            <td>₹18.5 – ₹20.5 Lakhs</td>
                            <td>8,000 sq.ft.</td>
                            <td>2.9 Years</td>
                        </tr>
                        <tr>
                            <td class="highlight">250 kWp+</td>
                            <td>1,000 – 1,100 Units</td>
                            <td>~31,000 Units</td>
                            <td class="highlight">₹3,85,000 – ₹4,20,000</td>
                            <td>₹46.0 – ₹50.0 Lakhs</td>
                            <td>20,000 sq.ft.</td>
                            <td>2.8 Years</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- Commercial FAQs -->
    <section class="dt-section dt-section-surface">
        <div class="dt-container">
            <div class="dt-section-header center">
                <div class="dt-tech-label">COMMERCIAL FAQ</div>
                <h2 class="dt-section-title">Commercial Solar Questions Answered</h2>
            </div>

            <div class="dt-faq-list">
                <div class="dt-faq-item active">
                    <button type="button" class="dt-faq-btn">
                        <span>How does commercial solar help Pune businesses reduce operating expenses?</span>
                        <div class="dt-faq-icon"><i class="fas fa-plus"></i></div>
                    </button>
                    <div class="dt-faq-content">
                        Commercial power tariffs in Pune under MSEDCL (LT-II and HT Commercial) range between ₹11 to ₹14+ per kWh. Commercial facilities run air conditioning, lighting, servers, and elevators during daytime hours (9 AM to 6 PM), which coincides exactly with peak solar irradiance. Solar power displaces expensive grid electricity unit-for-unit, typically yielding a 2.8 to 3.2 year capital payback.
                    </div>
                </div>

                <div class="dt-faq-item">
                    <button type="button" class="dt-faq-btn">
                        <span>Can corporate entities claim 40% accelerated depreciation in India?</span>
                        <div class="dt-faq-icon"><i class="fas fa-plus"></i></div>
                    </button>
                    <div class="dt-faq-content">
                        Yes. Under Section 32 of the Income Tax Act, eligible commercial enterprises and companies investing in rooftop solar power generation systems can claim 40% accelerated depreciation in the first year of commissioning, significantly reducing corporate income tax liability.
                    </div>
                </div>

                <div class="dt-faq-item">
                    <button type="button" class="dt-faq-btn">
                        <span>Can solar panels be installed on elevated structures without compromising terrace usage?</span>
                        <div class="dt-faq-icon"><i class="fas fa-plus"></i></div>
                    </button>
                    <div class="dt-faq-content">
                        Yes. We engineer elevated superstructures (8–10 ft clearance) on RCC roofs that preserve 100% of usable terrace space for cafeteria seating or recreational zones. We also design solar carports over commercial parking areas, providing vehicle shade while generating clean power.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Global CTA -->
    <section class="dt-section">
        <div class="dt-container" style="text-align: center;">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-container); padding: 50px; max-width: 860px; margin: 0 auto;">
                <div class="dt-tech-label" style="margin: 0 auto 16px;">ZERO OBLIGATION COMMERCIAL FEASIBILITY</div>
                <h2 style="font-size: clamp(28px, 3.4vw, 40px); color: var(--text-primary); margin-bottom: 14px;">Power Your Business with Solar Energy</h2>
                <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 28px;">
                    Our senior solar engineers will inspect your facility, evaluate your load curves, and provide a comprehensive financial proposal within 48 hours.
                </p>
                <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
                    <a href="/contact" class="dt-btn dt-btn-primary">Book Commercial Survey &rarr;</a>
                    <a href="tel:+917249187969" class="dt-btn dt-btn-secondary"><i class="fas fa-phone-alt"></i> +91 72491 87969</a>
                </div>
            </div>
        </div>
    </section>

{get_dt_footer()}
</body>
</html>'''

    with open('commercial-solar-pune.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Converted commercial-solar-pune.html successfully!')

def convert_industrial_solar():
    with open('industrial-solar.html', 'r', encoding='utf-8') as f:
        orig = f.read()

    schemas = re.findall(r'<script type="application/ld\+json">.*?</script>', orig, re.DOTALL)
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
    <title>Industrial Solar EPC Pune | Factory Rooftop Solar Solutions</title>
    <meta name="description" content="Industrial solar EPC solutions for factories and manufacturing plants in Pune, Chakan, Bhosari, and Talegaon MIDC. Turnkey design, CEIG approval, and net metering.">
    <meta name="keywords" content="industrial solar installation pune, factory rooftop solar, industrial solar epc pune, solar for manufacturing plant, chakan midc solar, bhosari midc solar, industrial solar price pune">
    <link rel="canonical" href="https://egreensolution.in/industrial-solar">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://egreensolution.in/industrial-solar">
    <meta property="og:title" content="Industrial Solar EPC Pune | Turnkey Factory Solar Solutions">
    <meta property="og:description" content="Turnkey industrial rooftop solar installations for manufacturing units across Chakan, Bhosari, and Talegaon MIDC. CEIG clearance and guaranteed ROI.">
    <meta property="og:image" content="https://egreensolution.in/assets/projects/eagle_burgmann.png">

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
                <span class="current">Industrial Solar</span>
            </div>

            <div class="dt-subpage-grid">
                <div>
                    <div class="dt-tech-label">04 // HEAVY MANUFACTURING &amp; MIDC EPC</div>
                    <h1 class="dt-hero-title" style="font-size: clamp(34px, 4.2vw, 52px); margin-bottom: 20px;">
                        Industrial Solar EPC in Pune &amp; MIDC
                    </h1>
                    <p class="dt-section-desc" style="margin-bottom: 28px;">
                        Engineered for heavy power consumers across Chakan MIDC, Bhosari, Talegaon, and Ranjangaon industrial hubs. Turnkey 100 kW to 5 MW industrial rooftop solar power plants featuring non-penetrating sheet clamps, CEIG clearances, harmonic filtration, and 25-year performance guarantees.
                    </p>

                    <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px;">
                        <span class="dt-pill"><i class="fas fa-industry" style="color: var(--gold-accent);"></i> MIDC Chakan, Bhosari &amp; Talegaon</span>
                        <span class="dt-pill"><i class="fas fa-stamp" style="color: var(--gold-accent);"></i> Guaranteed CEIG Approvals</span>
                        <span class="dt-pill"><i class="fas fa-shield-alt" style="color: var(--gold-accent);"></i> Non-Penetrative Clamping</span>
                        <span class="dt-pill"><i class="fas fa-bolt" style="color: var(--gold-accent);"></i> HT Net Metering Synchronization</span>
                    </div>

                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; background: var(--bg-surface); border: 1px solid var(--border-muted); border-radius: var(--radius-card); padding: 18px;">
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--gold-accent); display: block;">100kW–5MW</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">EPC Sizing</span>
                        </div>
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--text-primary); display: block;">2.5 – 3 Yrs</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Capital Payback</span>
                        </div>
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700; color: var(--gold-accent); display: block;">100%</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">CEIG Clearance</span>
                        </div>
                    </div>
                </div>

                <div>
                    <div class="dt-form-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                            <span class="dt-tech-label" style="margin: 0;">MIDC INDUSTRIAL EPC</span>
                            <span style="font-size: 11px; color: #4ade80;"><i class="fas fa-circle" style="font-size: 8px;"></i> Plant Survey</span>
                        </div>
                        <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 6px;">Request Industrial Plant Audit</h3>
                        <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px;">Direct engineering consultation for manufacturing plants and factory sheds.</p>

                        <form action="https://formspree.io/f/xbjnqkyw" method="POST" style="display: flex; flex-direction: column; gap: 14px;">
                            <input type="hidden" name="_subject" value="Industrial Solar EPC Audit Request - Pune">
                            <input type="hidden" name="_page" value="industrial-solar">

                            <div class="dt-form-group">
                                <label class="dt-label">Factory / Company Name *</label>
                                <input type="text" name="company_name" required placeholder="e.g. Precision Forge Pvt Ltd" class="dt-input">
                            </div>

                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                                <div class="dt-form-group">
                                    <label class="dt-label">Contact Person *</label>
                                    <input type="text" name="name" required placeholder="e.g. Sanjay Kadam" class="dt-input">
                                </div>
                                <div class="dt-form-group">
                                    <label class="dt-label">Phone *</label>
                                    <input type="tel" name="phone" required placeholder="e.g. 98765 43210" class="dt-input">
                                </div>
                            </div>

                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                                <div class="dt-form-group">
                                    <label class="dt-label">MIDC Zone</label>
                                    <select name="midc_zone" class="dt-select">
                                        <option value="Chakan MIDC Phase 1/2/3/4">Chakan MIDC</option>
                                        <option value="Bhosari / Pimpri MIDC">Bhosari / PCMC</option>
                                        <option value="Talegaon MIDC">Talegaon MIDC</option>
                                        <option value="Ranjangaon MIDC">Ranjangaon MIDC</option>
                                        <option value="Other Maharashtra MIDC">Other MIDC</option>
                                    </select>
                                </div>
                                <div class="dt-form-group">
                                    <label class="dt-label">Estimated Shed Area</label>
                                    <select name="shed_area" class="dt-select">
                                        <option value="10,000 - 25,000 sq ft">10,000 – 25,000 sq.ft.</option>
                                        <option value="25,000 - 50,000 sq ft">25,000 – 50,000 sq.ft.</option>
                                        <option value="50,000+ sq ft (Mega Plant)">50,000+ sq.ft. (1MW+)</option>
                                    </select>
                                </div>
                            </div>

                            <button type="submit" class="dt-btn dt-btn-primary" style="width: 100%; margin-top: 6px;">
                                Request Industrial Proposal &rarr;
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Industrial Framework Sections -->
    <section class="dt-section">
        <div class="dt-container">
            <div class="dt-section-header center">
                <div class="dt-tech-label">INDUSTRIAL ENGINEERING STANDARDS</div>
                <h2 class="dt-section-title">Scalable Solar EPC for Manufacturing Plants</h2>
                <p class="dt-section-desc" style="margin: 0 auto;">
                    We design and construct high-voltage rooftop plants that harmonize with heavy inductive loads, variable frequency drives, and overhead crane vibrations.
                </p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;">
                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-hammer"></i></div>
                    <h3 class="dt-card-title">Zero Roof Penetration</h3>
                    <p class="dt-card-desc">Specialized aluminum standing seam and trapezoidal sheet clamps preserving shed waterproofing warranties and eliminating rust.</p>
                </div>
                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-stamp"></i></div>
                    <h3 class="dt-card-title">CEIG Electrical Clearances</h3>
                    <p class="dt-card-desc">Complete end-to-end statutory documentation, safety drawing approval, and physical site inspection clearance from the Chief Electrical Inspector.</p>
                </div>
                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-wave-square"></i></div>
                    <h3 class="dt-card-title">Harmonic &amp; Power Factor Sync</h3>
                    <p class="dt-card-desc">Advanced filtering inverters and APFC panel coordination preventing grid penalty charges and reactive power imbalances.</p>
                </div>
                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-shield-virus"></i></div>
                    <h3 class="dt-card-title">ESE Lightning Protection</h3>
                    <p class="dt-card-desc">Early Streamer Emission lightning arrestors providing 100m+ radius umbrella protection over your factory roofs and electrical assets.</p>
                </div>
                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-walkie-talkie"></i></div>
                    <h3 class="dt-card-title">Safe Walkway &amp; Lifelines</h3>
                    <p class="dt-card-desc">FRP anti-skid roof walkways and continuous stainless-steel safety lifelines for seamless, OSHA-compliant O&amp;M cleaning access.</p>
                </div>
                <div class="dt-card">
                    <div class="dt-card-icon"><i class="fas fa-server"></i></div>
                    <h3 class="dt-card-title">Cloud SCADA Monitoring</h3>
                    <p class="dt-card-desc">Centralized industrial SCADA telemetry displaying string currents, irradiation sensor data, and transformer temperature in real-time.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Featured Industrial Project: Eagle Burgmann -->
    <section class="dt-section dt-section-surface">
        <div class="dt-container">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-container); padding: 44px; display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 40px; align-items: center;">
                <div>
                    <span class="dt-tech-label"><i class="fas fa-industry"></i> FLAGSHIP INDUSTRIAL CASE STUDY</span>
                    <h3 style="font-size: clamp(26px, 3vw, 36px); color: var(--text-primary); margin: 12px 0 16px;">Eagle Burgmann India — 200kW Industrial Rooftop</h3>
                    <p style="font-size: 15px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 20px;">
                        Engineered and commissioned across the precision manufacturing facilities of Eagle Burgmann India Pvt. Ltd. Generating over 2,90,000 kWh annually with high-voltage net metering, custom trapezoidal non-penetrating clamping, and zero factory downtime during installation.
                    </p>
                    <div style="display: flex; gap: 16px; margin-bottom: 24px;">
                        <div style="background: var(--bg-elevated); padding: 12px 18px; border-radius: var(--radius-ctrl); border: 1px solid var(--border-muted);">
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 700; color: var(--gold-accent); display: block;">200 kWp</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Installed Capacity</span>
                        </div>
                        <div style="background: var(--bg-elevated); padding: 12px 18px; border-radius: var(--radius-ctrl); border: 1px solid var(--border-muted);">
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 700; color: #4ade80; display: block;">~2.9 Lakh</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Annual Units</span>
                        </div>
                        <div style="background: var(--bg-elevated); padding: 12px 18px; border-radius: var(--radius-ctrl); border: 1px solid var(--border-muted);">
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 700; color: var(--text-primary); display: block;">&lt; 3.0 Yrs</span>
                            <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Full Payback</span>
                        </div>
                    </div>
                    <a href="/projects/eagle-burgmann-200kw-solar-pune" class="dt-btn dt-btn-primary">
                        Read Full 200kW Industrial Case Study &rarr;
                    </a>
                </div>
                <div style="border-radius: var(--radius-card); overflow: hidden; border: 1px solid var(--border-emp); height: 340px;">
                    <img src="/assets/projects/eagle_burgmann.png" alt="Industrial Solar EPC Plant Chakan MIDC Pune - Eagle Burgmann 200kW Project" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
            </div>
        </div>
    </section>

    <!-- Global CTA -->
    <section class="dt-section">
        <div class="dt-container" style="text-align: center;">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-container); padding: 50px; max-width: 860px; margin: 0 auto;">
                <div class="dt-tech-label" style="margin: 0 auto 16px;">MIDC SITE FEASIBILITY INSPECTION</div>
                <h2 style="font-size: clamp(28px, 3.4vw, 40px); color: var(--text-primary); margin-bottom: 14px;">Cut Factory Operating Costs with Industrial Solar</h2>
                <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 28px;">
                    Our industrial EPC team conducts drone shed profiling, transformer capacity evaluation, and custom SLD engineering across all Maharashtra MIDC zones.
                </p>
                <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
                    <a href="/contact" class="dt-btn dt-btn-primary">Book Factory Site Inspection &rarr;</a>
                    <a href="tel:+917249187969" class="dt-btn dt-btn-secondary"><i class="fas fa-phone-alt"></i> +91 72491 87969</a>
                </div>
            </div>
        </div>
    </section>

{get_dt_footer()}
</body>
</html>'''

    with open('industrial-solar.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Converted industrial-solar.html successfully!')

if __name__ == '__main__':
    convert_commercial_solar()
    convert_industrial_solar()
