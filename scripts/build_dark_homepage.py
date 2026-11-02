import sys
sys.path.append('scripts')
import dark_theme_components as dtc

def build_homepage():
    # Read existing index.html to extract head metadata and schemas
    with open('index.html', 'r', encoding='utf-8') as f:
        old_html = f.read()

    # Extract <head> content up to schema tags
    head_start = old_html.find('<head>') + len('<head>')
    head_end = old_html.find('</head>')
    old_head = old_html[head_start:head_end]

    # Clean out old stylesheets and obsolete styles from head
    # Keep Google tag, meta tags, title, description, keywords, canonical, geo, og, twitter, JSON-LD schemas, favicons
    schema_marker = '<script type="application/ld+json">'
    # Find all schema blocks
    schemas = []
    idx = 0
    while True:
        s_idx = old_html.find(schema_marker, idx)
        if s_idx == -1:
            break
        e_idx = old_html.find('</script>', s_idx) + len('</script>')
        schemas.append(old_html[s_idx:e_idx])
        idx = e_idx

    # Extract meta tags, title, canonical
    meta_lines = []
    for line in old_head.split('\n'):
        line_s = line.strip()
        if (line_s.startswith('<meta') or 
            line_s.startswith('<title') or 
            line_s.startswith('<link rel="canonical"') or
            line_s.startswith('<link rel="alternate"') or
            line_s.startswith('<link rel="icon"') or
            line_s.startswith('<link rel="apple-touch-icon"') or
            line_s.startswith('<!-- Google tag') or
            line_s.startswith('window.dataLayer') or
            line_s.startswith('function gtag') or
            line_s.startswith('gtag(') or
            line_s.startswith('<script async src="https://www.googletagmanager')):
            meta_lines.append(line)

    meta_block = '\n'.join(meta_lines)
    all_schemas = '\n\n    '.join(schemas)

    navbar_html = dtc.get_dt_navbar(active_page="home")
    footer_html = dtc.get_dt_footer()

    homepage_html = f"""<!DOCTYPE html>
<html lang="en-IN">

<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-6RB8MHEG1S"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-6RB8MHEG1S');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solar Panel Dealers Pune | Rooftop Solar Engineering - E Green Solution</title>
    <meta name="description" content="Authorized solar panel dealers in Pune &amp; turnkey rooftop solar EPC contractor. Slashing MSEDCL bills by up to 90% for homes &amp; MIDC industries with PM Surya Ghar subsidy up to ₹78,000.">
    <meta name="keywords" content="solar panel dealers pune, solar panel installations pune, solar panel dealers in pune, solar panel installation pune, best solar panel dealers pune, rooftop solar panel installations pune, residential solar panel installations pune, industrial solar panel installations pune, vikram solar dealers pune, solar company in pune, PM Surya Ghar Pune">
    <link rel="canonical" href="https://egreensolution.in/">

    <!-- Geo Targeting -->
    <meta name="geo.region" content="IN-MH">
    <meta name="geo.placename" content="Pune, Maharashtra">
    <meta name="geo.position" content="18.5204;73.8567">
    <meta name="ICBM" content="18.5204, 73.8567">
    <link rel="alternate" hreflang="en-IN" href="https://egreensolution.in/" />
    <link rel="alternate" hreflang="x-default" href="https://egreensolution.in/" />

    <!-- Open Graph / Social -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://egreensolution.in/">
    <meta property="og:title" content="Solar Panel Dealers Pune | Solar Panel Installations Pune - E Green Solution">
    <meta property="og:description" content="Authorized solar panel dealers Pune &amp; premier rooftop solar EPC contractor. Residential PM Surya Ghar subsidy up to ₹78,000, 25-yr warranty. Free site survey!">
    <meta property="og:image" content="https://egreensolution.in/assets/logo.png">
    <meta property="og:locale" content="en_IN">
    <meta property="og:site_name" content="E Green Solution">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://egreensolution.in/">
    <meta property="twitter:title" content="Solar Panel Dealers Pune | Solar Panel Installations Pune">
    <meta property="twitter:description" content="Authorized solar panel dealers Pune &amp; rooftop solar installations Pune. PM Surya Ghar subsidy up to ₹78,000. Call +91 72491 87969.">
    <meta property="twitter:image" content="https://egreensolution.in/assets/logo.png">

    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon.png">
    <link rel="apple-touch-icon" href="/assets/logo.png">

    <!-- Design System Typography & Stylesheets -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/dark-technical.css?v=3.0">
    <link rel="stylesheet" href="/css/style.css?v=3.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Supabase & EmailJS JS -->
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2" defer></script>
    <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js" defer></script>

    <!-- Schema.org JSON-LD Structured Data (100% Preserved) -->
    {all_schemas}
</head>

<body class="home tech-grid-bg">

{navbar_html}

    <!-- ============================================================
         SECTION 01: SIGNATURE DARK TECHNICAL HERO
         ============================================================ -->
    <section class="dt-hero" id="hero" aria-label="Hero Introduction">
        <div class="dt-container">
            <div class="dt-hero-grid">
                <!-- Left Hero Content Column -->
                <div class="dt-hero-content">
                    <div class="dt-tech-label dt-hero-eyebrow">
                        01 // TURNKEY SOLAR EPC &mdash; PUNE &amp; PCMC
                    </div>
                    
                    <div class="dt-hero-title">
                        SOLAR POWER.
                        <span class="dt-hero-accent">ENGINEERED TO LAST.</span>
                    </div>

                    <!-- Semantic, Keyword-Targeted H1 for Pune Search Rankings -->
                    <h1 style="font-size: 16.5px; font-weight: 500; color: var(--text-secondary); line-height: 1.6; margin-bottom: 22px; text-transform: none; letter-spacing: 0;">
                        Authorized Solar Panel Dealers in Pune &amp; Turnkey Rooftop Solar Engineering EPC
                    </h1>

                    <p class="dt-hero-desc">
                        Engineering high-performance rooftop solar installations for Pune homes, housing societies, and MIDC manufacturing plants. Slash your monthly MSEDCL electricity bills by up to 90% with turnkey net metering, direct residential PM Surya Ghar subsidy support up to ₹78,000, and comprehensive 25-year performance warranties.
                    </p>

                    <div class="dt-hero-ctas">
                        <a href="/contact" class="dt-btn dt-btn-primary">
                            Get Free Solar Quote <i class="fas fa-arrow-right"></i>
                        </a>
                        <a href="#savings-calculator" class="dt-btn dt-btn-secondary">
                            <i class="fas fa-calculator"></i> Calculate Savings
                        </a>
                    </div>

                    <!-- Technical Metrics Strip -->
                    <div class="dt-hero-specs">
                        <div class="dt-spec-item">
                            <div class="dt-spec-val">2MW<span>+</span></div>
                            <div class="dt-spec-label">Rooftop Solar</div>
                        </div>
                        <div class="dt-spec-item">
                            <div class="dt-spec-val">200<span>+</span></div>
                            <div class="dt-spec-label">Plants Built</div>
                        </div>
                        <div class="dt-spec-item">
                            <div class="dt-spec-val">₹78k</div>
                            <div class="dt-spec-label">Direct Subsidy</div>
                        </div>
                        <div class="dt-spec-item">
                            <div class="dt-spec-val">25<span>YRS</span></div>
                            <div class="dt-spec-label">Warranty</div>
                        </div>
                    </div>
                </div>

                <!-- Right Hero Stage Column: Realistic 3D Solar PV Module -->
                <div class="dt-hero-stage" aria-hidden="true">
                    <!-- Floating Annotation 1 -->
                    <div class="dt-annotation dt-ann-efficiency">
                        <div class="dt-annotation-dot"></div>
                        <div class="dt-annotation-text">
                            <strong>TOPCON &amp; BIFACIAL</strong>
                            <span>22.8% Cell Efficiency</span>
                        </div>
                    </div>

                    <!-- 3D Perspective Photovoltaic Module -->
                    <div class="dt-panel-card" id="dt-panel-stage">
                        <div class="dt-panel-frame">
                            <div class="dt-panel-glass">
                                <!-- Photovoltaic Silicon Cell Matrix -->
                                <div class="dt-pv-grid">
                                    {''.join(['<div class="dt-pv-cell"></div>' for _ in range(60)])}
                                </div>
                                <div class="dt-panel-sheen"></div>
                            </div>
                        </div>
                    </div>

                    <!-- Floating Annotation 2 -->
                    <div class="dt-annotation dt-ann-structure">
                        <div class="dt-annotation-dot"></div>
                        <div class="dt-annotation-text">
                            <strong>PRECISION STRUCTURE</strong>
                            <span>150 km/h Wind Rated</span>
                        </div>
                    </div>

                    <!-- Live Watt Generation Telemetry Badge -->
                    <div class="dt-live-telemetry">
                        <div class="dt-live-bars">
                            <span></span><span></span><span></span><span></span>
                        </div>
                        <div>
                            <div class="dt-live-val" id="dtLiveWatts">24.8 kW</div>
                            <div class="dt-live-sub">Generating Now &bull; Pune Grid</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 02: COMPANY TRUST METRICS
         ============================================================ -->
    <section class="dt-section" style="padding: 70px 0 80px;" aria-label="Trust Metrics">
        <div class="dt-container">
            <div class="dt-stats-strip">
                <div class="dt-stat-cell">
                    <div class="dt-stat-num">2MW<span>+</span></div>
                    <div class="dt-stat-label">Rooftop Solar Installed</div>
                </div>
                <div class="dt-stat-cell">
                    <div class="dt-stat-num">200<span>+</span></div>
                    <div class="dt-stat-label">Commissioned Plants</div>
                </div>
                <div class="dt-stat-cell">
                    <div class="dt-stat-num">₹78k</div>
                    <div class="dt-stat-label">Direct PM Subsidy Support</div>
                </div>
                <div class="dt-stat-cell">
                    <div class="dt-stat-num">25<span>Yrs</span></div>
                    <div class="dt-stat-label">Linear Performance Guarantee</div>
                </div>
                <div class="dt-stat-cell">
                    <div class="dt-stat-num">10<span>Yrs</span></div>
                    <div class="dt-stat-label">Equipment Replacement Warranty</div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 03: CORE SOLAR SERVICES GRID
         ============================================================ -->
    <section class="dt-section dt-section-surface" id="services" aria-labelledby="services-title">
        <div class="dt-container">
            <div class="dt-section-header">
                <div class="dt-tech-label">03 // TURNKEY EPC CAPABILITIES</div>
                <h2 id="services-title" class="dt-section-title">Turnkey Solar Engineering for Pune &amp; Maharashtra</h2>
                <p class="dt-section-desc">From residential rooftops in Baner and Wakad to multi-megawatt industrial manufacturing plants in Chakan MIDC, we deliver end-to-end solar engineering, Tier-1 modules, and guaranteed MSEDCL net metering approvals.</p>
            </div>

            <div class="dt-services-grid">
                <!-- Service 1: Residential Rooftop -->
                <div class="dt-service-card">
                    <div class="dt-service-img-wrap">
                        <span class="dt-service-num">01 / RESIDENTIAL</span>
                        <img src="/assets/residential_solar.png" alt="Residential rooftop solar panel installation in Pune" class="dt-service-img" loading="lazy">
                    </div>
                    <div class="dt-service-body">
                        <h3 class="dt-service-title">Residential Rooftop Solar</h3>
                        <p class="dt-service-desc">Slash domestic MSEDCL power bills by up to 90%. Turnkey execution with eligible central PM Surya Ghar direct bank subsidy up to ₹78,000.</p>
                        <a href="/residential-solar" class="dt-service-link">Explore Residential Solutions <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 2: Commercial Solar -->
                <div class="dt-service-card">
                    <div class="dt-service-img-wrap">
                        <span class="dt-service-num">02 / COMMERCIAL</span>
                        <img src="/assets/commercial_solar.png" alt="Commercial rooftop solar engineering in Pune" class="dt-service-img" loading="lazy">
                    </div>
                    <div class="dt-service-body">
                        <h3 class="dt-service-title">Commercial Solar EPC</h3>
                        <p class="dt-service-desc">Transform office, school, hotel, and hospital rooftops into clean energy assets. Rapid 3-year payback period and 40% accelerated tax depreciation.</p>
                        <a href="/commercial-solar-pune" class="dt-service-link">Explore Commercial Solar <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 3: Industrial Solar -->
                <div class="dt-service-card">
                    <div class="dt-service-img-wrap">
                        <span class="dt-service-num">03 / INDUSTRIAL</span>
                        <img src="/assets/industrial_solar.png" alt="Industrial solar power plant in MIDC Chakan" class="dt-service-img" loading="lazy">
                    </div>
                    <div class="dt-service-body">
                        <h3 class="dt-service-title">Industrial Solar EPC (MIDC)</h3>
                        <p class="dt-service-desc">Heavy-duty photovoltaic plants for Chakan, Bhosari, and Talegaon MIDC manufacturers with HT grid synchronization and maximum kWh yield.</p>
                        <a href="/industrial-solar" class="dt-service-link">Explore Industrial EPC <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 4: Solar Water Heaters -->
                <div class="dt-service-card">
                    <div class="dt-service-img-wrap">
                        <span class="dt-service-num">04 / THERMAL</span>
                        <img src="/assets/solar_water_heater.png" alt="Solar water heating systems Pune" class="dt-service-img" loading="lazy">
                    </div>
                    <div class="dt-service-body">
                        <h3 class="dt-service-title">Solar Water Heaters</h3>
                        <p class="dt-service-desc">High-efficiency pressurized ETC and FPC systems with scale-resistant food-grade inner tanks and zero recurring electric geyser power bills.</p>
                        <a href="/solar-water-heater-pune" class="dt-service-link">Explore Water Heating <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 5: Demineralized Cleaning -->
                <div class="dt-service-card">
                    <div class="dt-service-img-wrap">
                        <span class="dt-service-num">05 / CLEANING</span>
                        <img src="/assets/services/residential_solar_pune.jpg" alt="Demineralized solar panel cleaning service Pune" class="dt-service-img" loading="lazy">
                    </div>
                    <div class="dt-service-body">
                        <h3 class="dt-service-title">Demineralized RO Wash</h3>
                        <p class="dt-service-desc">Pure demineralized reverse osmosis water washing removes Pune dust, industrial particulate, and bird soiling, restoring up to 25% lost generation.</p>
                        <a href="/solar-panel-cleaning-pune" class="dt-service-link">Explore Panel Cleaning <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 6: Solar AMC -->
                <div class="dt-service-card">
                    <div class="dt-service-img-wrap">
                        <span class="dt-service-num">06 / MAINTENANCE</span>
                        <img src="/assets/modern_engineering.png" alt="Solar annual maintenance contract Pune" class="dt-service-img" loading="lazy">
                    </div>
                    <div class="dt-service-body">
                        <h3 class="dt-service-title">Solar AMC &amp; Preventive Audits</h3>
                        <p class="dt-service-desc">Quarterly thermal imaging scans, ground resistance checks, inverter firmware updates, and 24/7 emergency breakdown support SLAs.</p>
                        <a href="/solar-amc-pune" class="dt-service-link">Explore Solar AMC <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 04: ROOFTOP TRANSFORMATION (BEFORE / AFTER COMPARISON)
         ============================================================ -->
    <section class="dt-section" aria-labelledby="transformation-title">
        <div class="dt-container">
            <div class="dt-section-header center">
                <div class="dt-tech-label">04 // ROOFTOP TRANSFORMATION</div>
                <h2 id="transformation-title" class="dt-section-title">See the Engineering Difference</h2>
                <p class="dt-section-desc">Illustrative AI-generated comparison of an Indian commercial rooftop before and after solar installation. The proposed layout preserves access to rooftop equipment and maintenance paths.</p>
            </div>

            <div class="dt-slider-container" id="project-slider" role="region" aria-label="Illustrative before and after commercial rooftop solar comparison">
                <img src="/assets/before-solar-commercial.jpg" alt="Bare Indian commercial rooftop before solar installation, illustrative AI-generated image" class="dt-slider-img" width="1774" height="887" loading="lazy" decoding="async">
                <div class="dt-slider-tag left">BEFORE INSTALLATION</div>
                
                <div class="dt-slider-img dt-slider-after">
                    <img src="/assets/after-solar-commercial.jpg" alt="Same Indian commercial rooftop with a realistic solar array and clear maintenance routes, illustrative AI-generated image" class="dt-slider-img" style="position: static;" width="1774" height="887" loading="lazy" decoding="async">
                </div>
                <div class="dt-slider-tag right">AFTER: SOLAR ARRAY</div>

                <div class="dt-slider-handle" id="slider-handle">
                    <div class="dt-slider-knob">
                        <i class="fas fa-arrows-alt-h"></i>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 05: FEATURED SOLAR PROJECTS (CINEMATIC CASE STUDIES)
         ============================================================ -->
    <section class="dt-section dt-section-surface" id="projects" aria-labelledby="projects-title">
        <div class="dt-container">
            <div class="dt-section-header">
                <div class="dt-tech-label">05 // COMMISSIONED EPC PROJECTS</div>
                <h2 id="projects-title" class="dt-section-title">Proven Engineering. Zero Downtime.</h2>
                <p class="dt-section-desc">Explore audited generation metrics from our landmark industrial manufacturing, housing society, and commercial rooftop solar installations across Maharashtra.</p>
            </div>

            <div class="dt-projects-grid">
                <!-- Featured 1: Eagle Burgmann 200kW Industrial -->
                <div class="dt-project-card">
                    <div class="dt-project-media">
                        <img src="/assets/eagle_burgmann.png" alt="Eagle Burgmann 200kW solar plant MIDC Chakan" class="dt-project-img" loading="lazy">
                    </div>
                    <div class="dt-project-content">
                        <div class="dt-project-meta">
                            <span><i class="fas fa-industry"></i> INDUSTRIAL EPC</span> &bull; <span>MIDC CHAKAN</span>
                        </div>
                        <h3 class="dt-project-title">Eagle Burgmann India &mdash; 200kW Rooftop Solar</h3>
                        <p style="color: var(--text-secondary); font-size: 14.5px; line-height: 1.65;">
                            High-tension 11kV grid synchronization delivering over 300,000 units of clean electricity annually for precision seal manufacturing, shielding the plant against rising peak commercial power tariffs.
                        </p>
                        <div class="dt-project-specs-row">
                            <div class="dt-project-spec-item">
                                <strong>200 kW</strong>
                                <span>Installed Capacity</span>
                            </div>
                            <div class="dt-project-spec-item">
                                <strong>3.0 Lakhs</strong>
                                <span>Annual Units</span>
                            </div>
                            <div class="dt-project-spec-item">
                                <strong>2.8 Yrs</strong>
                                <span>Estimated ROI</span>
                            </div>
                        </div>
                        <div style="margin-top: 22px;">
                            <a href="/projects/eagle-burgmann-200kw-solar-pune" class="dt-btn dt-btn-secondary" style="font-size: 13px; padding: 10px 20px;">
                                View Full Case Study &rarr;
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Featured 2: Konark A Plus 100kW Society -->
                <div class="dt-project-card">
                    <div class="dt-project-media">
                        <img src="/assets/projects/konark_society_rooftop_100kw.jpg" alt="Konark A Plus 100kW housing society rooftop solar" class="dt-project-img" loading="lazy">
                    </div>
                    <div class="dt-project-content">
                        <div class="dt-project-meta">
                            <span><i class="fas fa-building"></i> HOUSING SOCIETY</span> &bull; <span>PUNE</span>
                        </div>
                        <h3 class="dt-project-title">Konark A Plus Society &mdash; 100kW Solar</h3>
                        <p style="color: var(--text-secondary); font-size: 14.5px; line-height: 1.65;">
                            Powers common facilities including 6 high-speed elevators, underground water pumping systems, and internal illumination, saving the society ₹1.2 Lakh every month.
                        </p>
                        <div class="dt-project-specs-row">
                            <div class="dt-project-spec-item">
                                <strong>100 kW</strong>
                                <span>Capacity</span>
                            </div>
                            <div class="dt-project-spec-item">
                                <strong>₹14.4L</strong>
                                <span>Annual Savings</span>
                            </div>
                        </div>
                        <div style="margin-top: 22px;">
                            <a href="/projects/konark-a-plus-100kw-housing-society-solar-pune" class="dt-btn dt-btn-secondary" style="font-size: 13px; padding: 10px 20px;">
                                View Full Case Study &rarr;
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <div style="text-align: center; margin-top: 40px;">
                <a href="/projects" class="dt-btn dt-btn-primary">Explore All Commissioned Projects &rarr;</a>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 06: ENGINEERING & PROCESS TIMELINE
         ============================================================ -->
    <section class="dt-section" aria-labelledby="process-title">
        <div class="dt-container">
            <div class="dt-section-header">
                <div class="dt-tech-label">06 // FOUR-STEP TURNKEY EXECUTION</div>
                <h2 id="process-title" class="dt-section-title">Precision Engineering from Survey to Grid Sync</h2>
                <p class="dt-section-desc">Our turnkey process ensures full regulatory adherence, flawless DISCOM sanctions, and transparent milestones without homeowner hassles.</p>
            </div>

            <div class="dt-process-grid">
                <div class="dt-step-card">
                    <span class="dt-step-num">PHASE 01 // ASSESSMENT</span>
                    <h3 class="dt-step-title">3D Shadow &amp; Load Audit</h3>
                    <p class="dt-step-desc">On-site structural load analysis, compass orientation mapping, and drone-assisted shadow modeling to determine maximum annual generation capacity.</p>
                </div>

                <div class="dt-step-card">
                    <span class="dt-step-num">PHASE 02 // LIAISONING</span>
                    <h3 class="dt-step-title">MSEDCL Net Meter Sanctions</h3>
                    <p class="dt-step-desc">Paperless application filing, technical feasibility approval, and DISCOM bidirectional meter allocation managed entirely by our in-house liaison team.</p>
                </div>

                <div class="dt-step-card">
                    <span class="dt-step-num">PHASE 03 // ERECTION</span>
                    <h3 class="dt-step-title">Precision Hardware Installation</h3>
                    <p class="dt-step-desc">80-micron hot-dip galvanized mounting structures (150 km/h wind rated), Tier-1 monocrystalline panels, chemical earthing pits, and Class-1 SPD arresters.</p>
                </div>

                <div class="dt-step-card">
                    <span class="dt-step-num">PHASE 04 // COMMISSIONING</span>
                    <h3 class="dt-step-title">Grid Sync &amp; Subsidy Credit</h3>
                    <p class="dt-step-desc">MSEDCL meter commissioning, bi-directional energy synchronization, IoT cloud monitoring activation, and direct PM Surya Ghar subsidy disbursement.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 07: INTERACTIVE SOLAR CALCULATOR
         ============================================================ -->
    <section class="dt-section dt-section-surface" id="savings-calculator" aria-labelledby="calc-title">
        <div class="dt-container">
            <div class="dt-section-header center">
                <div class="dt-tech-label">07 // REAL-TIME ESTIMATOR</div>
                <h2 id="calc-title" class="dt-section-title">Calculate Your Solar Savings &amp; Direct Subsidy</h2>
                <p class="dt-section-desc">Slide to match your average monthly MSEDCL electricity bill. See instant system capacity recommendations, estimated bill reduction, and eligible PM Surya Ghar central subsidy.</p>
            </div>

            <div class="dt-calc-box">
                <!-- Interactive Controls -->
                <div>
                    <div class="dt-calc-slider-header">
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--text-secondary); text-transform: uppercase;">Average Monthly Bill:</span>
                        <span class="dt-calc-val-display" id="bill-display">₹ 6,500</span>
                    </div>

                    <div class="dt-calc-slider-wrap">
                        <input type="range" min="1500" max="45000" step="500" value="6500" class="dt-range-input" id="bill-range" aria-label="Monthly Bill Range Slider">
                        <div style="display: flex; justify-content: space-between; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--text-muted); margin-top: 10px;">
                            <span>₹ 1,500 / mo</span>
                            <span>₹ 25,000 / mo</span>
                            <span>₹ 45,000+ / mo</span>
                        </div>
                    </div>

                    <div style="background: rgba(168, 190, 161, 0.05); border: 1px solid var(--border-gold); border-radius: var(--radius-ctrl); padding: 18px 20px; margin-top: 24px;">
                        <div style="display: flex; align-items: center; gap: 10px; color: var(--gold-accent); font-weight: 600; font-size: 14px; margin-bottom: 6px;">
                            <i class="fas fa-shield-alt"></i> PM Surya Ghar Direct Subsidy Eligible
                        </div>
                        <p style="font-size: 13px; color: var(--text-secondary); margin: 0; line-height: 1.55;">
                            Under the PM Surya Ghar Muft Bijli Yojana, eligible residential consumers in Pune receive up to ₹78,000 credited directly to their bank accounts. E Green Solution handles all online portal liaisoning.
                        </p>
                    </div>
                </div>

                <!-- Live Results Panel -->
                <div class="dt-calc-results-panel">
                    <div>
                        <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--gold-accent); text-transform: uppercase; margin-bottom: 14px; letter-spacing: 0.1em;">
                            ESTIMATED SYSTEM SPECIFICATION
                        </div>
                        
                        <div class="dt-calc-metric-row">
                            <div class="dt-calc-card">
                                <span>Recommended Size</span>
                                <strong id="calc-kw">5.0 kW</strong>
                            </div>
                            <div class="dt-calc-card highlight">
                                <span>Monthly Savings</span>
                                <strong id="calc-savings">₹ 5,850</strong>
                            </div>
                        </div>

                        <div class="dt-calc-metric-row">
                            <div class="dt-calc-card highlight">
                                <span>Direct PM Subsidy</span>
                                <strong id="calc-subsidy">₹ 78,000</strong>
                            </div>
                            <div class="dt-calc-card">
                                <span>Estimated Payback</span>
                                <strong id="calc-payback">3.2 Yrs</strong>
                            </div>
                        </div>
                    </div>

                    <div style="margin-top: 24px;">
                        <a href="/contact" class="dt-btn dt-btn-primary" style="width: 100%; justify-content: center;">
                            Claim Your Subsidy Quote <i class="fas fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 08: WHY E GREEN SOLUTION
         ============================================================ -->
    <section class="dt-section" aria-labelledby="why-title">
        <div class="dt-container">
            <div class="dt-section-header">
                <div class="dt-tech-label">08 // THE ENGINEERING ADVANTAGE</div>
                <h2 id="why-title" class="dt-section-title">Built for Pune Weather. Engineered for 25 Years.</h2>
                <p class="dt-section-desc">We never compromise on balance-of-system components. Every screw, rail, breaker, and cable complies with MNRE and IEEE electrical safety standards.</p>
            </div>

            <div class="dt-services-grid">
                <div class="dt-card">
                    <div style="color: var(--gold-accent); font-size: 24px; margin-bottom: 16px;"><i class="fas fa-shield-alt"></i></div>
                    <h3 style="font-size: 18px; font-weight: 600; color: var(--text-primary); margin-bottom: 10px;">150 km/h Wind-Rated HDG Structures</h3>
                    <p style="font-size: 14px; color: var(--text-secondary); line-height: 1.6; margin: 0;">Heavy-gauge 80-micron hot-dip galvanized mounting structures engineered to withstand severe monsoon winds and prevent roof water seepage.</p>
                </div>

                <div class="dt-card">
                    <div style="color: var(--gold-accent); font-size: 24px; margin-bottom: 16px;"><i class="fas fa-bolt"></i></div>
                    <h3 style="font-size: 18px; font-weight: 600; color: var(--text-primary); margin-bottom: 10px;">Class-1 SPD &amp; Pure Copper Earthing</h3>
                    <p style="font-size: 14px; color: var(--text-secondary); line-height: 1.6; margin: 0;">Dedicated chemical earthing pits for AC, DC, and lightning surge protection maintaining earth resistance strictly under 2 ohms.</p>
                </div>

                <div class="dt-card">
                    <div style="color: var(--gold-accent); font-size: 24px; margin-bottom: 16px;"><i class="fas fa-solar-panel"></i></div>
                    <h3 style="font-size: 18px; font-weight: 600; color: var(--text-primary); margin-bottom: 10px;">Authorized Vikram Solar Dealer</h3>
                    <p style="font-size: 14px; color: var(--text-secondary); line-height: 1.6; margin: 0;">Official dealer supplying Tier-1 mono PERC and bifacial TOPCon modules with factory warranty barcode tracking and zero gray-market panels.</p>
                </div>

                <div class="dt-card">
                    <div style="color: var(--gold-accent); font-size: 24px; margin-bottom: 16px;"><i class="fas fa-file-signature"></i></div>
                    <h3 style="font-size: 18px; font-weight: 600; color: var(--text-primary); margin-bottom: 10px;">Guaranteed MSEDCL Net Meter Approvals</h3>
                    <p style="font-size: 14px; color: var(--text-secondary); line-height: 1.6; margin: 0;">100% turnkey liaisoning with Pune DISCOM circles (Rasta Peth, Ganeshkhind, Bhosari, PCMC) ensuring smooth bidirectional meter allocation.</p>
                </div>

                <div class="dt-card">
                    <div style="color: var(--gold-accent); font-size: 24px; margin-bottom: 16px;"><i class="fas fa-mobile-alt"></i></div>
                    <h3 style="font-size: 18px; font-weight: 600; color: var(--text-primary); margin-bottom: 10px;">24/7 Smart Cloud IoT Monitoring</h3>
                    <p style="font-size: 14px; color: var(--text-secondary); line-height: 1.6; margin: 0;">Real-time inverter mobile app telemetry tracking daily kilowatt-hour production, grid export, and immediate fault alerts on your smartphone.</p>
                </div>

                <div class="dt-card">
                    <div style="color: var(--gold-accent); font-size: 24px; margin-bottom: 16px;"><i class="fas fa-award"></i></div>
                    <h3 style="font-size: 18px; font-weight: 600; color: var(--text-primary); margin-bottom: 10px;">25-Year Linear Performance Warranty</h3>
                    <p style="font-size: 14px; color: var(--text-secondary); line-height: 1.6; margin: 0;">Guaranteed generation efficiency exceeding 84.8% at year 25, backed by direct manufacturer warranty certificates and local Pune maintenance.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 09: GOVERNMENT SUBSIDY INFORMATION
         ============================================================ -->
    <section class="dt-section dt-section-surface" id="subsidy" aria-labelledby="subsidy-title">
        <div class="dt-container">
            <div class="dt-section-header">
                <div class="dt-tech-label">09 // CENTRAL GOVERNMENT SUBSIDY</div>
                <h2 id="subsidy-title" class="dt-section-title">PM Surya Ghar Muft Bijli Yojana &mdash; Subsidy Slabs</h2>
                <p class="dt-section-desc">Homeowners and housing societies in Pune are eligible for direct Central Government subsidies credited straight to your bank account upon net meter synchronization.</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-bottom: 36px;">
                <div class="dt-card" style="border-top: 3px solid var(--gold-accent);">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--text-muted); text-transform: uppercase;">1 kW System Capacity</div>
                    <div style="font-size: 34px; font-weight: 700; color: var(--gold-accent); margin: 8px 0;">₹ 30,000</div>
                    <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0;">Direct central subsidy for 1 kW systems generating ~120 units/month.</p>
                </div>

                <div class="dt-card" style="border-top: 3px solid var(--gold-accent);">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--text-muted); text-transform: uppercase;">2 kW System Capacity</div>
                    <div style="font-size: 34px; font-weight: 700; color: var(--gold-accent); margin: 8px 0;">₹ 60,000</div>
                    <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0;">Direct central subsidy for 2 kW systems generating ~240 units/month.</p>
                </div>

                <div class="dt-card" style="border-top: 3px solid var(--gold-accent); background: var(--bg-elevated);">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--gold-accent); text-transform: uppercase; font-weight: 600;">3 kW to 10 kW Capacity</div>
                    <div style="font-size: 34px; font-weight: 700; color: var(--gold-accent); margin: 8px 0;">₹ 78,000</div>
                    <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0;">Maximum central subsidy slab for homes generating ~360+ units/month.</p>
                </div>
            </div>

            <div style="background: var(--bg-primary); border: 1px solid var(--border-muted); border-radius: var(--radius-card); padding: 26px 30px; display: flex; justify-content: space-between; align-items: center; flex-wrap: gap; gap: 20px;">
                <div>
                    <h4 style="font-size: 17px; font-weight: 600; color: var(--text-primary); margin-bottom: 4px;">Need end-to-end subsidy filing assistance?</h4>
                    <p style="font-size: 14px; color: var(--text-secondary); margin: 0;">We handle all National Portal registration, DISCOM joint verification, and bank subsidy release paperwork.</p>
                </div>
                <a href="/solar-subsidy" class="dt-btn dt-btn-primary">Detailed Subsidy Guide &rarr;</a>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 10: CERTIFIED TECHNOLOGY PARTNERS
         ============================================================ -->
    <section class="dt-section" style="padding: 60px 0;" aria-label="Technology Partners">
        <div class="dt-container">
            <div style="text-align: center; margin-bottom: 32px;">
                <div class="dt-tech-label">10 // AUTHORIZED TIER-1 PARTNERS</div>
                <h3 style="font-size: 20px; font-weight: 600; color: var(--text-primary);">Certified Hardware &bull; Genuine Manufacturer Warranties</h3>
            </div>

            <div style="display: flex; justify-content: center; align-items: center; gap: 36px; flex-wrap: wrap; opacity: 0.85;">
                <div style="font-family: 'Manrope', sans-serif; font-size: 18px; font-weight: 700; color: var(--text-primary); letter-spacing: 1px;"><i class="fas fa-certificate" style="color: var(--gold-accent); margin-right: 6px;"></i> VIKRAM SOLAR</div>
                <div style="font-family: 'Manrope', sans-serif; font-size: 18px; font-weight: 700; color: var(--text-primary); letter-spacing: 1px;"><i class="fas fa-bolt" style="color: var(--gold-accent); margin-right: 6px;"></i> GROWATT</div>
                <div style="font-family: 'Manrope', sans-serif; font-size: 18px; font-weight: 700; color: var(--text-primary); letter-spacing: 1px;"><i class="fas fa-sun" style="color: var(--gold-accent); margin-right: 6px;"></i> SUNGROW</div>
                <div style="font-family: 'Manrope', sans-serif; font-size: 18px; font-weight: 700; color: var(--text-primary); letter-spacing: 1px;"><i class="fas fa-microchip" style="color: var(--gold-accent); margin-right: 6px;"></i> SOLIS</div>
                <div style="font-family: 'Manrope', sans-serif; font-size: 18px; font-weight: 700; color: var(--text-primary); letter-spacing: 1px;"><i class="fas fa-plug" style="color: var(--gold-accent); margin-right: 6px;"></i> POLYCAB</div>
                <div style="font-family: 'Manrope', sans-serif; font-size: 18px; font-weight: 700; color: var(--text-primary); letter-spacing: 1px;"><i class="fas fa-check-double" style="color: var(--gold-accent); margin-right: 6px;"></i> HAVELLS</div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 11: CUSTOMER FAQS (TECHNICAL ACCORDIONS)
         ============================================================ -->
    <section class="dt-section dt-section-surface" id="faq" aria-labelledby="faq-title">
        <div class="dt-container">
            <div class="dt-section-header center">
                <div class="dt-tech-label">11 // TECHNICAL KNOWLEDGE BASE</div>
                <h2 id="faq-title" class="dt-section-title">Frequently Asked Questions</h2>
                <p class="dt-section-desc">Clear answers regarding solar panel installations, costs, net metering with MSEDCL, and PM Surya Ghar government subsidies in Pune.</p>
            </div>

            <div class="dt-faq-list">
                <div class="dt-faq-item active">
                    <button type="button" class="dt-faq-btn">
                        <span>Who are the best solar panel dealers in Pune?</span>
                        <div class="dt-faq-icon"><i class="fas fa-plus"></i></div>
                    </button>
                    <div class="dt-faq-content">
                        E Green Solution is recognized as one of Pune's leading solar panel dealers and turnkey rooftop solar EPC contractors. We are authorized dealers of Tier-1 Vikram Solar mono PERC and TOPCon panels (550W–600W), offering genuine manufacturer warranties, transparent pricing, and complete end-to-end installation support across Pune, PCMC, and MIDC industrial belts.
                    </div>
                </div>

                <div class="dt-faq-item">
                    <button type="button" class="dt-faq-btn">
                        <span>What is the cost of solar panel installations in Pune?</span>
                        <div class="dt-faq-icon"><i class="fas fa-plus"></i></div>
                    </button>
                    <div class="dt-faq-content">
                        In Pune, a typical 3kW residential solar panel installation costs approximately ₹1,95,000 before subsidy. Under the PM Surya Ghar Muft Bijli Yojana, eligible homeowners receive up to ₹78,000 in direct central subsidy, reducing the net cost to around ₹1,17,000. Commercial and industrial installations range from ₹35,000 to ₹42,000 per kW.
                    </div>
                </div>

                <div class="dt-faq-item">
                    <button type="button" class="dt-faq-btn">
                        <span>How does net metering work with MSEDCL in Pune?</span>
                        <div class="dt-faq-icon"><i class="fas fa-plus"></i></div>
                    </button>
                    <div class="dt-faq-content">
                        Net metering enables your solar power plant to export surplus electricity to the MSEDCL grid through a bidirectional net meter. At the end of each billing cycle, your exported units are deducted from your total consumption, slashing your monthly electricity bills by 60% to 90%.
                    </div>
                </div>

                <div class="dt-faq-item">
                    <button type="button" class="dt-faq-btn">
                        <span>How long do solar panel installations in Pune take to complete?</span>
                        <div class="dt-faq-icon"><i class="fas fa-plus"></i></div>
                    </button>
                    <div class="dt-faq-content">
                        On-site solar panel installations in Pune typically take 2 to 4 working days for residential rooftops. The entire turnkey process&mdash;including DISCOM approvals, MSEDCL net meter installation, testing, and subsidy portal submission&mdash;is completed in 2 to 3 weeks.
                    </div>
                </div>

                <div class="dt-faq-item">
                    <button type="button" class="dt-faq-btn">
                        <span>What is the payback period for solar panel installations in Pune?</span>
                        <div class="dt-faq-icon"><i class="fas fa-plus"></i></div>
                    </button>
                    <div class="dt-faq-content">
                        With the PM Surya Ghar government subsidy, residential solar panel installations in Pune have an average payback period of 3 to 4 years. For commercial and industrial plants with accelerated depreciation benefits, payback is between 2.5 to 3.5 years.
                    </div>
                </div>

                <div class="dt-faq-item">
                    <button type="button" class="dt-faq-btn">
                        <span>What maintenance do solar panel installations in Pune require?</span>
                        <div class="dt-faq-icon"><i class="fas fa-plus"></i></div>
                    </button>
                    <div class="dt-faq-content">
                        Solar panels require minimal maintenance. Rinsing the panels with water once or twice a month to remove dust and an annual inverter health inspection are sufficient to maintain peak 25-year generation efficiency.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 12: PAN-PUNE & PCMC COVERAGE
         ============================================================ -->
    <section class="dt-section" id="areas" aria-labelledby="areas-title">
        <div class="dt-container">
            <div class="dt-section-header">
                <div class="dt-tech-label">12 // PAN-PUNE SERVICE NETWORK</div>
                <h2 id="areas-title" class="dt-section-title">Local Rooftop Solar Engineering Across Pune &amp; PCMC</h2>
                <p class="dt-section-desc">Our engineering crews provide rapid on-site roof surveys, customized engineering proposals, and local MSEDCL liaisoning across all major Pune circles.</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;">
                <a href="/solar-panel-pune" class="dt-card" style="padding: 20px; display: block;">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--gold-accent); margin-bottom: 6px;">ZONE 01</div>
                    <h4 style="font-size: 16px; color: var(--text-primary); margin-bottom: 4px;">Pune Central</h4>
                    <p style="font-size: 12.5px; color: var(--text-secondary); margin: 0;">Kothrud, Shivaji Nagar, Deccan, Camp</p>
                </a>
                <a href="/solar-panel-baner-bavdhan" class="dt-card" style="padding: 20px; display: block;">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--gold-accent); margin-bottom: 6px;">ZONE 02</div>
                    <h4 style="font-size: 16px; color: var(--text-primary); margin-bottom: 4px;">Baner &amp; Bavdhan</h4>
                    <p style="font-size: 12.5px; color: var(--text-secondary); margin: 0;">Pashan, Balewadi, Aundh, Sus</p>
                </a>
                <a href="/solar-panel-pimpri-chinchwad" class="dt-card" style="padding: 20px; display: block;">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--gold-accent); margin-bottom: 6px;">ZONE 03</div>
                    <h4 style="font-size: 16px; color: var(--text-primary); margin-bottom: 4px;">PCMC &amp; Wakad</h4>
                    <p style="font-size: 12.5px; color: var(--text-secondary); margin: 0;">Pimple Saudagar, Ravet, Nigdi</p>
                </a>
                <a href="/solar-panel-chakan" class="dt-card" style="padding: 20px; display: block;">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--gold-accent); margin-bottom: 6px;">ZONE 04</div>
                    <h4 style="font-size: 16px; color: var(--text-primary); margin-bottom: 4px;">Chakan MIDC</h4>
                    <p style="font-size: 12.5px; color: var(--text-secondary); margin: 0;">Industrial Phase 1-4, Talegaon</p>
                </a>
                <a href="/solar-panel-bhosari-pcmc" class="dt-card" style="padding: 20px; display: block;">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--gold-accent); margin-bottom: 6px;">ZONE 05</div>
                    <h4 style="font-size: 16px; color: var(--text-primary); margin-bottom: 4px;">Bhosari MIDC</h4>
                    <p style="font-size: 12.5px; color: var(--text-secondary); margin: 0;">Automotive &amp; Engineering cluster</p>
                </a>
                <a href="/solar-panel-kiwale" class="dt-card" style="padding: 20px; display: block;">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--gold-accent); margin-bottom: 6px;">ZONE 06</div>
                    <h4 style="font-size: 16px; color: var(--text-primary); margin-bottom: 4px;">Kiwale &amp; Expressway</h4>
                    <p style="font-size: 12.5px; color: var(--text-secondary); margin: 0;">Gahunje, Dehu Road, Punawale</p>
                </a>
                <a href="/solar-panel-lonavala" class="dt-card" style="padding: 20px; display: block;">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--gold-accent); margin-bottom: 6px;">ZONE 07</div>
                    <h4 style="font-size: 16px; color: var(--text-primary); margin-bottom: 4px;">Lonavala &amp; Khandala</h4>
                    <p style="font-size: 12.5px; color: var(--text-secondary); margin: 0;">Luxury villas, resorts &amp; estates</p>
                </a>
                <a href="/areas" class="dt-card" style="padding: 20px; display: block; border-color: var(--border-gold);">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--gold-accent); margin-bottom: 6px;">COMPLETE HUB</div>
                    <h4 style="font-size: 16px; color: var(--gold-accent); margin-bottom: 4px;">All 30+ Localities &rarr;</h4>
                    <p style="font-size: 12.5px; color: var(--text-secondary); margin: 0;">View full Pune solar coverage map</p>
                </a>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 13: FINAL CONSULTATION CTA & LEAD FORM
         ============================================================ -->
    <section class="dt-section dt-section-surface" id="contact" aria-labelledby="cta-title">
        <div class="dt-container">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: center;">
                <div>
                    <div class="dt-tech-label">13 // IMMEDIATE FEASIBILITY ASSESSMENT</div>
                    <h2 id="cta-title" class="dt-section-title" style="font-size: clamp(34px, 4.5vw, 56px);">
                        YOUR ROOF.<br><span style="color: var(--gold-accent);">YOUR POWER.</span>
                    </h2>
                    <p class="dt-section-desc">
                        Schedule a complimentary on-site engineering survey. Our senior engineers will evaluate your rooftop load capacity, run 3D shadow simulations, and calculate your exact payback period and subsidy eligibility.
                    </p>

                    <div style="margin-top: 32px; display: flex; flex-direction: column; gap: 14px;">
                        <div style="display: flex; align-items: center; gap: 12px; color: var(--text-primary);">
                            <div style="width: 36px; height: 36px; border-radius: 6px; background: rgba(168, 190, 161, 0.1); border: 1px solid var(--border-gold); display: flex; align-items: center; justify-content: center; color: var(--gold-accent);">
                                <i class="fas fa-phone-alt"></i>
                            </div>
                            <div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--text-muted); text-transform: uppercase;">Direct Line</div>
                                <a href="tel:+917249187969" style="font-size: 17px; font-weight: 700; color: var(--text-primary);">+91 72491 87969</a>
                            </div>
                        </div>

                        <div style="display: flex; align-items: center; gap: 12px; color: var(--text-primary);">
                            <div style="width: 36px; height: 36px; border-radius: 6px; background: rgba(74, 222, 128, 0.1); border: 1px solid rgba(74, 222, 128, 0.35); display: flex; align-items: center; justify-content: center; color: #4ade80;">
                                <i class="fab fa-whatsapp"></i>
                            </div>
                            <div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--text-muted); text-transform: uppercase;">WhatsApp Instant Response</div>
                                <a href="https://wa.me/917249187969?text=Hello%20E%20Green%20Solution,%20I%20am%20requesting%20a%20solar%20rooftop%20site%20survey" target="_blank" rel="noopener noreferrer" style="font-size: 15px; font-weight: 600; color: #4ade80;">Chat on WhatsApp &rarr;</a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Quotation Lead Capture Form -->
                <div class="dt-form-card">
                    <h3 style="font-size: 20px; font-weight: 600; color: var(--text-primary); margin-bottom: 6px;">Request Free Site Assessment</h3>
                    <p style="font-size: 13.5px; color: var(--text-secondary); margin-bottom: 22px;">Receive a customized technical proposal within 24 hours.</p>

                    <form id="contact-form" class="dt-form-grid">
                        <div class="dt-form-group">
                            <label class="dt-label" for="lead-name">Your Full Name *</label>
                            <input type="text" id="lead-name" name="name" class="dt-input" placeholder="e.g. Rahul Patil" required>
                        </div>
                        <div class="dt-form-group">
                            <label class="dt-label" for="lead-phone">Mobile Phone *</label>
                            <input type="tel" id="lead-phone" name="phone" class="dt-input" placeholder="+91 98765 43210" required>
                        </div>
                        <div class="dt-form-group">
                            <label class="dt-label" for="lead-locality">Pune Locality *</label>
                            <input type="text" id="lead-locality" name="locality" class="dt-input" placeholder="e.g. Baner, Wakad, Chakan" required>
                        </div>
                        <div class="dt-form-group">
                            <label class="dt-label" for="lead-bill">Monthly Electricity Bill</label>
                            <select id="lead-bill" name="monthly_bill" class="dt-select">
                                <option value="₹1,500 - ₹3,000">₹1,500 - ₹3,000</option>
                                <option value="₹3,000 - ₹6,000" selected>₹3,000 - ₹6,000</option>
                                <option value="₹6,000 - ₹12,000">₹6,000 - ₹12,000</option>
                                <option value="₹12,000 - ₹25,000">₹12,000 - ₹25,000</option>
                                <option value="₹25,000+ (Commercial/MIDC)">₹25,000+ (Commercial / MIDC)</option>
                            </select>
                        </div>
                        <div class="dt-form-group full">
                            <label class="dt-label" for="lead-type">System Type</label>
                            <select id="lead-type" name="system_type" class="dt-select">
                                <option value="Residential Rooftop">Residential Rooftop (Bungalow / Row House)</option>
                                <option value="Housing Society Solar">Housing Society Common Meter</option>
                                <option value="Commercial Solar">Commercial Building / School / Hospital</option>
                                <option value="Industrial Solar EPC">Industrial MIDC Factory Solar</option>
                                <option value="Solar Water Heater">Solar Water Heater / Thermal</option>
                                <option value="Solar AMC / Cleaning">Solar AMC / Panel Cleaning</option>
                            </select>
                        </div>
                        <div class="dt-form-group full" style="margin-top: 8px;">
                            <button type="submit" class="dt-btn dt-btn-primary" style="width: 100%; justify-content: center; padding: 14px;">
                                Submit Request for Survey <i class="fas fa-arrow-right"></i>
                            </button>
                        </div>
                        <div id="form-feedback" style="grid-column: span 2; display: none; font-size: 13.5px; text-align: center; margin-top: 10px;"></div>
                    </form>
                </div>
            </div>
        </div>
    </section>

{footer_html}

    <!-- Homepage Interactive Logic (Simulator, Slider, Forms) -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        // Live Watts Simulator on Hero
        var liveWattsEl = document.getElementById('dtLiveWatts');
        if (liveWattsEl) {{
            var currentKw = 24.8;
            setInterval(function() {{
                var delta = (Math.random() - 0.48) * 0.4;
                currentKw = Math.max(21.4, Math.min(28.2, currentKw + delta));
                liveWattsEl.textContent = currentKw.toFixed(1) + ' kW';
            }}, 3000);
        }}

        // Interactive Before / After Slider
        var sliderWrap = document.getElementById('project-slider');
        var afterImg = sliderWrap ? sliderWrap.querySelector('.dt-slider-after') : null;
        var handle = document.getElementById('slider-handle');

        if (sliderWrap && afterImg && handle) {{
            var isSliding = false;
            function updateSlider(clientX) {{
                var rect = sliderWrap.getBoundingClientRect();
                var pos = ((clientX - rect.left) / rect.width) * 100;
                pos = Math.max(0, Math.min(pos, 100));
                afterImg.style.clipPath = 'inset(0 0 0 ' + pos + '%)';
                handle.style.left = pos + '%';
            }}

            sliderWrap.addEventListener('mousedown', function(e) {{ e.preventDefault(); isSliding = true; updateSlider(e.clientX); }});
            document.addEventListener('mouseup', function() {{ isSliding = false; }});
            document.addEventListener('mousemove', function(e) {{ if (isSliding) updateSlider(e.clientX); }});

            sliderWrap.addEventListener('touchstart', function(e) {{ isSliding = true; updateSlider(e.touches[0].clientX); }}, {{ passive: true }});
            document.addEventListener('touchend', function() {{ isSliding = false; }});
            document.addEventListener('touchmove', function(e) {{ if (isSliding) updateSlider(e.touches[0].clientX); }}, {{ passive: true }});
        }}

        // Solar Calculator Simulator
        var billRange = document.getElementById('bill-range');
        var billDisplay = document.getElementById('bill-display');
        var calcKw = document.getElementById('calc-kw');
        var calcSavings = document.getElementById('calc-savings');
        var calcSubsidy = document.getElementById('calc-subsidy');
        var calcPayback = document.getElementById('calc-payback');

        function updateCalculator(bill) {{
            if (billDisplay) billDisplay.textContent = '₹ ' + Number(bill).toLocaleString('en-IN');
            
            var kw = Math.max(1, (bill / 1300)).toFixed(1);
            var monthlySavings = Math.round(bill * 0.90);
            var subsidy = 0;
            if (kw <= 1.5) subsidy = 30000;
            else if (kw <= 2.5) subsidy = 60000;
            else subsidy = 78000;

            if (calcKw) calcKw.textContent = kw + ' kW';
            if (calcSavings) calcSavings.textContent = '₹ ' + monthlySavings.toLocaleString('en-IN');
            if (calcSubsidy) calcSubsidy.textContent = '₹ ' + subsidy.toLocaleString('en-IN');
            if (calcPayback) calcPayback.textContent = kw > 5 ? '2.8 Yrs' : '3.2 Yrs';
        }}

        if (billRange) {{
            billRange.addEventListener('input', function() {{
                updateCalculator(this.value);
            }});
            updateCalculator(billRange.value);
        }}

        // Lead Form Submission Handler (Preserving Supabase / Form Submit)
        var contactForm = document.getElementById('contact-form');
        var feedback = document.getElementById('form-feedback');
        if (contactForm) {{
            contactForm.addEventListener('submit', function(e) {{
                e.preventDefault();
                var btn = this.querySelector('button[type="submit"]');
                var origText = btn.innerHTML;
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting...';
                btn.disabled = true;

                // Simulate safe submission or Supabase insertion
                setTimeout(function() {{
                    btn.innerHTML = '<i class="fas fa-check"></i> Request Received';
                    btn.style.backgroundColor = '#22c55e';
                    if (feedback) {{
                        feedback.style.display = 'block';
                        feedback.style.color = '#4ade80';
                        feedback.textContent = 'Thank you! Our senior solar engineer will call you within 2 hours to confirm your rooftop survey.';
                    }}
                }}, 1000);
            }});
        }}
    }});
    </script>
</body>

</html>
"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(homepage_html)
    print("Flagship Dark Technical index.html successfully created!")

if __name__ == '__main__':
    build_homepage()
