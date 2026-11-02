# Python script generating standard Dark Technical Navbar, Footer, and Meta Tags

def get_dt_head_tags():
    return """    <!-- Google Fonts: Manrope, Inter, JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/dark-technical.css?v=3.0">
    <link rel="stylesheet" href="/css/style.css?v=3.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">"""

def get_dt_navbar(active_page=""):
    def is_act(page):
        return ' class="active"' if active_page == page else ''

    return f"""    <!-- ============================================================
         GLOBAL DARK TECHNICAL NAVIGATION (#0B0D12 / Solar Sage #A8BEA1)
         ============================================================ -->
    <header id="dt-navbar" role="banner">
        <div class="dt-nav-container">
            <a href="/" class="dt-brand" aria-label="E Green Solution Home">
                <div class="dt-logo-wrap">
                    <img src="/assets/logo.png" alt="E Green Solution - Solar Panel Dealers Pune" class="dt-logo" width="150" height="34" loading="eager">
                </div>
                <span class="dt-brand-title">E GREEN <span>SOLUTION</span></span>
            </a>

            <!-- Desktop Navigation Links -->
            <nav class="dt-nav-links" aria-label="Main Navigation">
                <a href="/"{is_act('home')}>Home</a>
                
                <div class="dt-has-dropdown">
                    <a href="/services" class="dt-dropdown-trigger{is_act('services')}" aria-haspopup="true" aria-expanded="false">
                        Services <i class="fas fa-chevron-down"></i>
                    </a>
                    <div class="dt-dropdown-menu" role="menu">
                        <div class="dt-dropdown-header">
                            <span class="dt-dropdown-eyebrow">ENGINEERING SOLUTIONS</span>
                            <a href="/services" class="dt-dropdown-viewall">All 10 Services &rarr;</a>
                        </div>
                        <div class="dt-dropdown-grid">
                            <a href="/residential-solar" class="dt-drop-item" role="menuitem">
                                <div class="dt-drop-icon"><i class="fas fa-home"></i></div>
                                <div class="dt-drop-info">
                                    <strong>Residential Rooftop</strong>
                                    <span>PM Surya Ghar subsidy up to ₹78k</span>
                                </div>
                            </a>
                            <a href="/commercial-solar-pune" class="dt-drop-item" role="menuitem">
                                <div class="dt-drop-icon"><i class="fas fa-building"></i></div>
                                <div class="dt-drop-info">
                                    <strong>Commercial Solar</strong>
                                    <span>Offices, schools, malls, hospitals</span>
                                </div>
                            </a>
                            <a href="/industrial-solar" class="dt-drop-item" role="menuitem">
                                <div class="dt-drop-icon"><i class="fas fa-industry"></i></div>
                                <div class="dt-drop-info">
                                    <strong>Industrial Solar EPC</strong>
                                    <span>MIDC Chakan, Bhosari, Talegaon</span>
                                </div>
                            </a>
                            <a href="/solar-water-heater-pune" class="dt-drop-item" role="menuitem">
                                <div class="dt-drop-icon"><i class="fas fa-water"></i></div>
                                <div class="dt-drop-info">
                                    <strong>Solar Water Heaters</strong>
                                    <span>Pressurized ETC &amp; FPC systems</span>
                                </div>
                            </a>
                            <a href="/solar-panel-cleaning-pune" class="dt-drop-item" role="menuitem">
                                <div class="dt-drop-icon"><i class="fas fa-broom"></i></div>
                                <div class="dt-drop-info">
                                    <strong>Demineralized RO Wash</strong>
                                    <span>Restore up to 25% lost generation</span>
                                </div>
                            </a>
                            <a href="/solar-amc-pune" class="dt-drop-item" role="menuitem">
                                <div class="dt-drop-icon"><i class="fas fa-file-contract"></i></div>
                                <div class="dt-drop-info">
                                    <strong>Solar AMC Contracts</strong>
                                    <span>Preventive checkups &amp; uptime SLAs</span>
                                </div>
                            </a>
                            <a href="/solar-inverter-repair-pune" class="dt-drop-item" role="menuitem">
                                <div class="dt-drop-icon"><i class="fas fa-bolt"></i></div>
                                <div class="dt-drop-info">
                                    <strong>Inverter Service &amp; Repair</strong>
                                    <span>Growatt, Sungrow, Solis, Polycab</span>
                                </div>
                            </a>
                            <a href="/solar-net-meter-msedcl-pune" class="dt-drop-item" role="menuitem">
                                <div class="dt-drop-icon"><i class="fas fa-tachometer-alt"></i></div>
                                <div class="dt-drop-info">
                                    <strong>MSEDCL Net Metering</strong>
                                    <span>Liaisoning, bi-directional sync</span>
                                </div>
                            </a>
                            <a href="/solar-plant-revamping-repowering" class="dt-drop-item" role="menuitem">
                                <div class="dt-drop-icon"><i class="fas fa-sync-alt"></i></div>
                                <div class="dt-drop-info">
                                    <strong>Plant Revamping</strong>
                                    <span>Repower older plants to TOPCon</span>
                                </div>
                            </a>
                            <a href="/solar-repair-maintenance-pune" class="dt-drop-item" role="menuitem">
                                <div class="dt-drop-icon"><i class="fas fa-wrench"></i></div>
                                <div class="dt-drop-info">
                                    <strong>Plant Repair &amp; Emergency</strong>
                                    <span>On-site breakdown troubleshooting</span>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>

                <a href="/projects"{is_act('projects')}>Projects</a>
                <a href="/solar-subsidy"{is_act('subsidy')}>Subsidy</a>
                <a href="/solar-guide"{is_act('guide')}>Solar 101</a>
                <a href="/calculator"{is_act('calculator')}>Calculator</a>
                <a href="/areas"{is_act('areas')}>Areas</a>
                <a href="/about"{is_act('about')}>About</a>
                <a href="/contact"{is_act('contact')}>Contact</a>
            </nav>

            <!-- Actions: Direct Call & Gold Quote CTA -->
            <div class="dt-nav-actions">
                <a href="tel:+917249187969" class="dt-phone-link" aria-label="Call E Green Solution">
                    <i class="fas fa-phone-alt"></i> <span>+91 72491 87969</span>
                </a>
                <a href="/contact" class="dt-btn dt-btn-primary" style="padding: 8px 18px; font-size: 13px;">
                    Get Free Quote <i class="fas fa-arrow-right" style="font-size: 11px;"></i>
                </a>

                <!-- Mobile Hamburger Toggle -->
                <button type="button" class="dt-hamburger" id="dt-hamburger" aria-label="Toggle Navigation Menu" aria-expanded="false">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </header>

    <!-- Mobile Navigation Drawer -->
    <div class="dt-mobile-backdrop" id="dt-backdrop"></div>
    <div class="dt-mobile-menu" id="dt-mobile-drawer" role="dialog" aria-modal="true" aria-label="Mobile Navigation Drawer">
        <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; padding-bottom: 14px; border-bottom: 1px solid var(--border-muted);">
                <span class="dt-brand-title">E GREEN <span>SOLUTION</span></span>
                <button type="button" id="dt-drawer-close" aria-label="Close Navigation" style="background: transparent; border: none; color: var(--text-primary); font-size: 20px; cursor: pointer;">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            
            <ul class="dt-mobile-links">
                <li><a href="/">Home <i class="fas fa-chevron-right" style="font-size: 11px; color: var(--gold-accent);"></i></a></li>
                <li><a href="/services">All Services <i class="fas fa-chevron-right" style="font-size: 11px; color: var(--gold-accent);"></i></a></li>
                <li><a href="/residential-solar">&mdash; Residential Rooftop Solar</a></li>
                <li><a href="/commercial-solar-pune">&mdash; Commercial Solar EPC</a></li>
                <li><a href="/industrial-solar">&mdash; Industrial Solar (MIDC)</a></li>
                <li><a href="/solar-subsidy">&mdash; PM Surya Ghar Subsidy Guide</a></li>
                <li><a href="/solar-water-heater-pune">&mdash; Solar Water Heaters</a></li>
                <li><a href="/solar-panel-cleaning-pune">&mdash; Demineralized Cleaning</a></li>
                <li><a href="/solar-amc-pune">&mdash; Solar AMC Contracts</a></li>
                <li><a href="/projects">Case Studies &amp; Projects <i class="fas fa-chevron-right" style="font-size: 11px; color: var(--gold-accent);"></i></a></li>
                <li><a href="/calculator">Solar Savings Calculator <i class="fas fa-chevron-right" style="font-size: 11px; color: var(--gold-accent);"></i></a></li>
                <li><a href="/solar-guide">Solar 101 Knowledge Guide <i class="fas fa-chevron-right" style="font-size: 11px; color: var(--gold-accent);"></i></a></li>
                <li><a href="/areas">Pune Service Locations <i class="fas fa-chevron-right" style="font-size: 11px; color: var(--gold-accent);"></i></a></li>
                <li><a href="/about">About Engineering Team <i class="fas fa-chevron-right" style="font-size: 11px; color: var(--gold-accent);"></i></a></li>
                <li><a href="/contact">Contact &amp; Site Survey <i class="fas fa-chevron-right" style="font-size: 11px; color: var(--gold-accent);"></i></a></li>
            </ul>
        </div>

        <div class="dt-mobile-footer">
            <a href="/contact" class="dt-btn dt-btn-primary" style="width: 100%; text-align: center;">Get Free Solar Quote &rarr;</a>
            <div style="display: flex; gap: 10px; margin-top: 8px;">
                <a href="tel:+917249187969" class="dt-btn dt-btn-secondary" style="flex: 1; padding: 10px; font-size: 12px; justify-content: center;"><i class="fas fa-phone-alt"></i> Call</a>
                <a href="https://wa.me/917249187969?text=Hello%20E%20Green%20Solution,%20I%20am%20interested%20in%20a%20solar%20quote" target="_blank" rel="noopener noreferrer" class="dt-btn dt-btn-secondary" style="flex: 1; padding: 10px; font-size: 12px; justify-content: center; color: #4ade80 !important;"><i class="fab fa-whatsapp"></i> WhatsApp</a>
            </div>
        </div>
    </div>"""

def get_dt_footer():
    return """    <!-- ============================================================
         GLOBAL DARK TECHNICAL FOOTER (#07080B / Solar Sage #A8BEA1)
         ============================================================ -->
    <footer id="dt-footer" role="contentinfo">
        <div class="dt-container">
            <div class="dt-footer-grid">
                <!-- Column 1: Brand & Authority Summary -->
                <div class="dt-footer-col">
                    <a href="/" class="dt-brand" style="margin-bottom: 18px; display: inline-flex;" aria-label="E Green Solution Home">
                        <img src="/assets/logo.png" alt="E Green Solution" class="dt-logo" width="140" height="32" loading="lazy">
                        <span class="dt-brand-title">E GREEN <span>SOLUTION</span></span>
                    </a>
                    <p style="font-size: 13.5px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 20px;">
                        Pune's premier rooftop solar engineering contractor and authorized solar equipment dealer. Delivering precision turnkey photovoltaic installations for homeowners, housing societies, and MIDC manufacturing plants with guaranteed MSEDCL net metering approvals, direct PM Surya Ghar subsidy support, and 25-year linear performance warranties.
                    </p>
                    <div style="display: flex; gap: 12px;">
                        <span class="dt-tech-label" style="font-size: 9.5px; padding: 3px 8px; margin: 0;"><i class="fas fa-shield-alt"></i> MNRE &amp; IEEE COMPLIANT</span>
                        <span class="dt-tech-label" style="font-size: 9.5px; padding: 3px 8px; margin: 0;"><i class="fas fa-certificate"></i> TIER-1 MODULES</span>
                    </div>
                </div>

                <!-- Column 2: Turnkey Solar Installations -->
                <div class="dt-footer-col">
                    <h4>Solar Engineering</h4>
                    <ul class="dt-footer-links">
                        <li><a href="/residential-solar"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Residential Rooftop Solar</a></li>
                        <li><a href="/commercial-solar-pune"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Commercial Solar EPC</a></li>
                        <li><a href="/industrial-solar"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Industrial Solar (MIDC)</a></li>
                        <li><a href="/solar-subsidy"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> PM Surya Ghar Subsidy Guide</a></li>
                        <li><a href="/solar-guide"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Solar 101 Knowledge Guide</a></li>
                        <li><a href="/calculator"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Solar Savings Calculator</a></li>
                        <li><a href="/projects"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Commissioned Case Studies</a></li>
                    </ul>
                </div>

                <!-- Column 3: Operation, Maintenance & AMC -->
                <div class="dt-footer-col">
                    <h4>Maintenance &amp; Service</h4>
                    <ul class="dt-footer-links">
                        <li><a href="/solar-amc-pune"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Solar AMC Contracts</a></li>
                        <li><a href="/solar-panel-cleaning-pune"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Demineralized RO Wash</a></li>
                        <li><a href="/solar-inverter-repair-pune"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Inverter Repair &amp; Service</a></li>
                        <li><a href="/solar-net-meter-msedcl-pune"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> MSEDCL Net Meter Testing</a></li>
                        <li><a href="/solar-plant-revamping-repowering"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Plant Revamping &amp; Repower</a></li>
                        <li><a href="/solar-water-heater-pune"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Solar Water Heating Systems</a></li>
                        <li><a href="/areas"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Pan-Pune Service Areas</a></li>
                    </ul>
                </div>

                <!-- Column 4: Official Office & Immediate Contact -->
                <div class="dt-footer-col">
                    <h4>Pune Headquarters</h4>
                    <div class="dt-footer-contact-item">
                        <i class="fas fa-map-marker-alt"></i>
                        <span>Plot No 12, Ground floor, Hira Banglow, Vidyadeep Society, Gulabnagar, Dhankawadi, Pune, Maharashtra 411043</span>
                    </div>
                    <div class="dt-footer-contact-item">
                        <i class="fas fa-phone-alt"></i>
                        <span><a href="tel:+917249187969" style="color: var(--text-primary); font-weight: 600;">+91 72491 87969</a></span>
                    </div>
                    <div class="dt-footer-contact-item">
                        <i class="fas fa-envelope"></i>
                        <span><a href="mailto:egreensolution1@gmail.com">egreensolution1@gmail.com</a></span>
                    </div>
                    <div class="dt-footer-contact-item">
                        <i class="fab fa-whatsapp" style="color: #4ade80;"></i>
                        <span><a href="https://wa.me/917249187969?text=Hello%20E%20Green%20Solution,%20I%20would%20like%20to%20request%20a%20solar%20consultation" target="_blank" rel="noopener noreferrer">Instant WhatsApp Consultation</a></span>
                    </div>
                    <div class="dt-footer-contact-item">
                        <i class="fas fa-clock"></i>
                        <span>Mon – Sat: 09:00 AM – 07:00 PM</span>
                    </div>
                </div>
            </div>

            <!-- Bottom Legal & Internal Network -->
            <div class="dt-footer-bottom">
                <div>
                    &copy; 2026 E Green Solution. All Rights Reserved. Turnkey Rooftop Solar Engineering &amp; Authorized Dealers Pune.
                </div>
                <div class="dt-legal-links">
                    <a href="/privacy-policy">Privacy Policy</a>
                    <a href="/sitemap.xml">XML Sitemap</a>
                    <a href="/areas">Service Hub</a>
                    <a href="/blog">Solar Articles</a>
                    <a href="/contact">Free Site Survey</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Global Dark Technical Scripts (Drawer Toggle, FAQ Accordion, Telemetry) -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        // Mobile Drawer Toggle
        var hamburger = document.getElementById('dt-hamburger');
        var drawer = document.getElementById('dt-mobile-drawer');
        var backdrop = document.getElementById('dt-backdrop');
        var closeBtn = document.getElementById('dt-drawer-close');

        function toggleDrawer(open) {
            if (!drawer || !backdrop || !hamburger) return;
            if (open) {
                drawer.classList.add('active');
                backdrop.classList.add('active');
                hamburger.classList.add('active');
                hamburger.setAttribute('aria-expanded', 'true');
                document.body.style.overflow = 'hidden';
            } else {
                drawer.classList.remove('active');
                backdrop.classList.remove('active');
                hamburger.classList.remove('active');
                hamburger.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            }
        }

        if (hamburger) hamburger.addEventListener('click', function() { toggleDrawer(!drawer.classList.contains('active')); });
        if (closeBtn) closeBtn.addEventListener('click', function() { toggleDrawer(false); });
        if (backdrop) backdrop.addEventListener('click', function() { toggleDrawer(false); });

        // Sticky Navbar shadow
        var navbar = document.getElementById('dt-navbar');
        window.addEventListener('scroll', function() {
            if (navbar) {
                if (window.scrollY > 20) {
                    navbar.style.borderBottomColor = 'rgba(168, 190, 161, 0.25)';
                    navbar.style.boxShadow = '0 10px 30px rgba(0,0,0,0.7)';
                } else {
                    navbar.style.borderBottomColor = 'rgba(241, 243, 245, 0.12)';
                    navbar.style.boxShadow = 'none';
                }
            }
        }, { passive: true });

        // Global FAQ Accordion Toggle
        document.querySelectorAll('.dt-faq-btn').forEach(function(btn) {
            btn.addEventListener('click', function() {
                var item = this.closest('.dt-faq-item');
                var isActive = item.classList.contains('active');
                var parent = item.closest('.dt-faq-list');
                if (parent) {
                    parent.querySelectorAll('.dt-faq-item').forEach(function(i) { i.classList.remove('active'); });
                }
                if (!isActive) {
                    item.classList.add('active');
                }
            });
        });
    });
    </script>"""
