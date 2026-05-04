// ── MOBILE MENU TOGGLE (standalone, no dependencies) ──
if (!window.__menuInitialized) {
window.__menuInitialized = true;
document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobile-menu');

    if (hamburger && mobileMenu) {
        // Move menu to body root to avoid nav stacking context issues
        document.body.appendChild(mobileMenu);

        // Create close button inside menu
        const closeBtn = document.createElement('button');
        closeBtn.innerHTML = '&times;';
        closeBtn.className = 'mobile-menu-close';
        closeBtn.setAttribute('aria-label', 'Close Menu');
        closeBtn.style.cssText = 'position:absolute;top:24px;right:24px;background:none;border:none;font-size:36px;color:#333;cursor:pointer;z-index:10003;padding:8px;line-height:1;';
        mobileMenu.appendChild(closeBtn);

        function closeMenu() {
            hamburger.classList.remove('active');
            mobileMenu.classList.remove('active');
            document.body.style.overflow = '';
        }

        function openMenu() {
            hamburger.classList.add('active');
            mobileMenu.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        hamburger.addEventListener('click', (e) => {
            e.stopPropagation();
            if (mobileMenu.classList.contains('active')) {
                closeMenu();
            } else {
                openMenu();
            }
        });

        // Close button
        closeBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            closeMenu();
        });

        // Close menu when a link is clicked
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', closeMenu);
        });

        // Close on resize to desktop
        window.addEventListener('resize', () => {
            if (window.innerWidth > 768) closeMenu();
        });

    }
});
} // end guard

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', () => {
    
    // --- CALCULATOR LOGIC (Moved to top for reliability) ---
    const monthlyBillInput = document.getElementById('monthlyBill');
    const monthlyBillRange = document.getElementById('monthlyBillRange');
    const unitRateInput = document.getElementById('unitRate');
    const btnShowResults = document.getElementById('btn-show-results');
    const btnBackToInput = document.getElementById('btn-back-to-input');
    const step1 = document.getElementById('calc-step-1');
    const step2 = document.getElementById('calc-step-2');
    const dot1 = document.getElementById('step1-dot');
    const dot2 = document.getElementById('step2-dot');

    if (monthlyBillInput && monthlyBillRange && unitRateInput && btnShowResults) {
        const resSystemSize = document.getElementById('resSystemSize');
        const resSpace = document.getElementById('resSpace');
        const resMonthlySavings = document.getElementById('resMonthlySavings');
        const resSystemCost = document.getElementById('resSystemCost');
        const resNetCost = document.getElementById('resNetCost');
        const summaryBill = document.getElementById('summary-bill');

        function calculateSolar() {
            let bill = parseFloat(monthlyBillInput.value) || 0;
            let rate = parseFloat(unitRateInput.value) || 10;
            let dailyUnitsRequired = bill / (rate * 30);
            let capacityKw = dailyUnitsRequired / 4; 

            const priceMap = [
                { kw: 3, price: 195000 }, { kw: 5, price: 275000 },
                { kw: 6, price: 325000 }, { kw: 7, price: 350000 },
                { kw: 8, price: 375000 }, { kw: 10, price: 425000 }
            ];

            if (capacityKw < 3) capacityKw = 3;
            let systemCost = 0;
            if (capacityKw <= 3) { systemCost = 195000; capacityKw = 3; }
            else if (capacityKw >= 10) { systemCost = 425000 + (Math.round(capacityKw) - 10) * 37500; capacityKw = Math.round(capacityKw); }
            else {
                for (let i = 0; i < priceMap.length - 1; i++) {
                    if (capacityKw >= priceMap[i].kw && capacityKw <= priceMap[i+1].kw) {
                        let ratio = (capacityKw - priceMap[i].kw) / (priceMap[i+1].kw - priceMap[i].kw);
                        systemCost = priceMap[i].price + ratio * (priceMap[i+1].price - priceMap[i].price);
                        break;
                    }
                }
            }
            
            let monthlySavings = Math.round(bill * 0.9);
            let subsidy = 78000;
            let netInvestment = systemCost - subsidy;
            let spaceRequired = Math.round(capacityKw * 100); // 100 sqft per kW is standard

            if (resSystemSize) resSystemSize.innerText = capacityKw.toFixed(1);
            if (resSpace) resSpace.innerText = spaceRequired;
            if (resMonthlySavings) resMonthlySavings.innerText = monthlySavings.toLocaleString('en-IN');
            if (resSystemCost) resSystemCost.innerText = Math.round(systemCost).toLocaleString('en-IN');
            if (resNetCost) resNetCost.innerText = Math.round(netInvestment).toLocaleString('en-IN');
            if (summaryBill) summaryBill.innerText = bill.toLocaleString('en-IN');
        }

        btnShowResults.addEventListener('click', (e) => {
            e.preventDefault();
            calculateSolar();
            if (step1 && step2) {
                step1.classList.remove('active');
                step2.classList.add('active');
                if (dot1 && dot2) { dot1.classList.remove('active'); dot2.classList.add('active'); }
                window.scrollTo({ top: document.getElementById('calculator-section').offsetTop - 100, behavior: 'smooth' });
            }
        });

        if (btnBackToInput) {
            btnBackToInput.addEventListener('click', () => {
                step2.classList.remove('active');
                step1.classList.add('active');
                if (dot2 && dot1) { dot2.classList.remove('active'); dot1.classList.add('active'); }
            });
        }

        monthlyBillRange.addEventListener('input', (e) => {
            monthlyBillInput.value = e.target.value;
            calculateSolar(); // Optional: Live calculation
        });
        monthlyBillInput.addEventListener('input', (e) => {
            monthlyBillRange.value = e.target.value;
            calculateSolar(); // Optional: Live calculation
        });
        unitRateInput.addEventListener('input', calculateSolar);

        calculateSolar();
    }

    // Initialize GSAP
    if (typeof gsap !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);
    }

    // Check if user prefers reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Hero Animations - MOTION DISABLED AS REQUESTED
    /* 
    const tl = gsap.timeline({ defaults: { ease: "power3.out" } });
    if (!prefersReducedMotion) {
        tl.from(".hero-tagline", { opacity: 0, y: 30, duration: 1, delay: 0.5 })
          .from(".hero-container h1", { opacity: 0, y: 30, duration: 1 }, "-=0.7")
          .from(".hero-btns", { opacity: 0, y: 30, duration: 1 }, "-=0.7")
          .to(".stats-bar", { opacity: 1, y: 0, duration: 1 }, "-=0.5")
          .from(".stat-item", { 
              opacity: 0, 
              y: 20, 
              stagger: 0.2, 
              duration: 0.8 
          }, "-=0.5");
    }
    */
    // Ensure stats bar is visible since timeline is disabled
    if (document.querySelector(".stats-bar")) {
        gsap.set(".stats-bar", { opacity: 1, y: 0 });
    }

    // Number Counter Animation
    const stats = document.querySelectorAll('.stat-number');
    stats.forEach(stat => {
        const target = parseInt(stat.getAttribute('data-target'));
        const originalText = stat.innerText;
        let suffix = "";
        
        // Extract suffix more reliably
        if (originalText.includes('MW+')) suffix = 'MW+';
        else if (originalText.includes('+')) suffix = '+';
        else if (originalText.includes('k')) suffix = 'k';
        
        const countObj = { val: 0 };
        
        gsap.to(countObj, {
            val: target,
            duration: 4,
            ease: "power2.out",
            scrollTrigger: {
                trigger: stat,
                start: "top 95%",
                toggleActions: "play none none none"
            },
            onUpdate: () => {
                if (suffix === 'k') {
                    stat.innerText = Math.ceil(countObj.val / 1000) + 'k';
                } else {
                    stat.innerText = Math.ceil(countObj.val) + suffix;
                }
            }
        });
    });

    // Mouse Parallax Effect - DISABLED AS REQUESTED
    /*
    const isMobile = window.innerWidth <= 768;
    const heroCard = document.querySelector('.hero-content-wrapper');
    if (heroCard && !isMobile) {
        let ticking = false;
        document.addEventListener('mousemove', (e) => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    const xAxis = (window.innerWidth / 2 - e.pageX) / 45;
                    const yAxis = (window.innerHeight / 2 - e.pageY) / 45;
                    heroCard.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
                    ticking = false;
                });
                ticking = true;
            }
        });
        // ... rest of parallax listeners
    }
    */

    // Sticky Navbar - Throttled
    const navbar = document.getElementById('navbar');
    let lastScrollY = window.scrollY;
    let scrollTicking = false;

    window.addEventListener('scroll', () => {
        if (!scrollTicking) {
            window.requestAnimationFrame(() => {
                if (window.scrollY > 50) {
                    navbar.classList.add('scrolled');
                } else {
                    navbar.classList.remove('scrolled');
                }
                scrollTicking = false;
            });
            scrollTicking = true;
        }
    });




    // Smooth Scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            if (this.getAttribute('href').length > 1) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Staggered Grid Reveals (GSAP ScrollTrigger)
    const grids = document.querySelectorAll('.services-grid, .project-grid, .why-us-grid');
    grids.forEach(grid => {
        if (!prefersReducedMotion && grid.children.length > 0) {
            gsap.fromTo(grid.children, 
                { y: 50, opacity: 0 },
                {
                    scrollTrigger: {
                        trigger: grid,
                        start: "top 85%",
                        toggleActions: "play none none none"
                    },
                    y: 0,
                    opacity: 1,
                    duration: 0.8,
                    stagger: 0.15,
                    ease: "power2.out",
                    clearProps: "all"
                }
            );
        }
    });

    // General Section Reveals
    const revealElements = document.querySelectorAll('.section-header, .about-section, .service-row');
    revealElements.forEach(el => {
        if (!prefersReducedMotion) {
            gsap.fromTo(el, 
                { y: 40, opacity: 0 },
                {
                    scrollTrigger: {
                        trigger: el,
                        start: "top 85%",
                        toggleActions: "play none none none"
                    },
                    y: 0,
                    opacity: 1,
                    duration: 1,
                    ease: "power2.out",
                    clearProps: "all"
                }
            );
        }
    });

    // FAQ Accordion Functionality
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(button => {
        button.addEventListener('click', () => {
            const faqItem = button.parentElement;
            const faqAnswer = faqItem.querySelector('.faq-answer');
            const icon = button.querySelector('i');
            const isOpen = faqAnswer.style.display === 'block';

            // Close all other items
            document.querySelectorAll('.faq-item').forEach(item => {
                const answer = item.querySelector('.faq-answer');
                const btn = item.querySelector('.faq-question');
                const icn = btn.querySelector('i');
                if (answer !== faqAnswer) {
                    answer.style.display = 'none';
                    answer.style.maxHeight = '0';
                    btn.style.background = 'white';
                    icn.style.transform = 'rotate(0deg)';
                }
            });

            // Toggle current item
            if (isOpen) {
                faqAnswer.style.display = 'none';
                faqAnswer.style.maxHeight = '0';
                button.style.background = 'white';
                icon.style.transform = 'rotate(0deg)';
            } else {
                faqAnswer.style.display = 'block';
                // Use a slight timeout to ensure display: block is processed before reading scrollHeight
                // to minimize layout thrashing if possible, or just accept the single read.
                const height = faqAnswer.scrollHeight;
                faqAnswer.style.maxHeight = height + 'px';
                button.style.background = 'rgba(46, 125, 50, 0.08)';
                icon.style.transform = 'rotate(180deg)';
            }
        });
    });

    // Why Choose Us hover effect (Desktop Only)
    if (!isMobile) {
        document.querySelectorAll('.why-card').forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-10px)';
                this.style.boxShadow = '0 15px 40px rgba(46, 125, 50, 0.15)';
            });
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
                this.style.boxShadow = '0 8px 25px rgba(0,0,0,0.08)';
            });
        });
    }


    // --- FIX FOR LAZY LOADED IMAGES SHIFTING LAYOUT ---
    // Ensure GSAP ScrollTrigger recalculates trigger positions after images load
    window.addEventListener('load', () => {
        ScrollTrigger.refresh();
    });

    const lazyImages = document.querySelectorAll('img[loading="lazy"]');
    lazyImages.forEach(img => {
        if (img.complete) {
            ScrollTrigger.refresh();
        } else {
            img.addEventListener('load', () => {
                ScrollTrigger.refresh();
            });
        }
    });
    
    // Email Obfuscation Helper
    const emailPlaceholders = document.querySelectorAll('.email-obfuscated');
    emailPlaceholders.forEach(placeholder => {
        const user = 'egreensolution1';
        const domain = 'gmail.com';
        const email = user + '@' + domain;
        
        if (placeholder.tagName === 'A') {
            placeholder.href = 'mailto:' + email;
            if (placeholder.innerText.trim() === '') {
                placeholder.innerText = email;
            }
        } else {
            placeholder.innerText = email;
        }
    });

    // --- PREMIUM SOLAR HERO LOGIC (SolarX) ---
    const initSolarXHero = () => {
        const svg = document.querySelector('.panel-svg');
        if (!svg) return;
        const ns = 'http://www.w3.org/2000/svg';

        const cols = 6, rows = 10;
        const padX = 16, padY = 14;
        const gapX = 4, gapY = 4;
        const totalW = 380 - padX * 2;
        const totalH = 420 - padY * 2;
        const cellW = (totalW - gapX * (cols - 1)) / cols;
        const cellH = (totalH - gapY * (rows - 1)) / rows;

        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                const x = padX + c * (cellW + gapX);
                const y = padY + r * (cellH + gapY);

                // Cell body
                const cell = document.createElementNS(ns, 'rect');
                cell.setAttribute('x', x);
                cell.setAttribute('y', y);
                cell.setAttribute('width', cellW);
                cell.setAttribute('height', cellH);
                cell.setAttribute('rx', '1.5');
                cell.setAttribute('fill', 'url(#cellGrad)');
                svg.appendChild(cell);

                // Iridescent sheen overlay per cell
                const sheen = document.createElementNS(ns, 'rect');
                sheen.setAttribute('x', x);
                sheen.setAttribute('y', y);
                sheen.setAttribute('width', cellW);
                sheen.setAttribute('height', cellH);
                sheen.setAttribute('rx', '1.5');
                sheen.setAttribute('fill', 'url(#sheenGrad)');
                sheen.setAttribute('opacity', (0.3 + Math.random() * 0.25).toFixed(2));
                svg.appendChild(sheen);

                // Horizontal bus bars (2 per cell)
                for (let b = 1; b <= 2; b++) {
                    const bar = document.createElementNS(ns, 'rect');
                    const by = y + (cellH / 3) * b;
                    bar.setAttribute('x', x + 2);
                    bar.setAttribute('y', by - 0.5);
                    bar.setAttribute('width', cellW - 4);
                    bar.setAttribute('height', '1');
                    bar.setAttribute('fill', 'url(#busGrad)');
                    bar.setAttribute('opacity', '0.7');
                    svg.appendChild(bar);
                }

                // Vertical finger lines (5 per cell)
                for (let f = 1; f <= 5; f++) {
                    const line = document.createElementNS(ns, 'rect');
                    const fx = x + (cellW / 6) * f;
                    line.setAttribute('x', fx - 0.3);
                    line.setAttribute('y', y + 2);
                    line.setAttribute('width', '0.6');
                    line.setAttribute('height', cellH - 4);
                    line.setAttribute('fill', 'url(#busGrad)');
                    line.setAttribute('opacity', '0.35');
                    svg.appendChild(line);
                }
            }
        }

        // Vertical main bus bars between columns
        for (let c = 0; c <= cols; c++) {
            const bx = padX + c * (cellW + gapX) - (c > 0 && c < cols ? gapX / 2 : 0);
            if (c === 0 || c === cols) continue;
            const vbar = document.createElementNS(ns, 'rect');
            vbar.setAttribute('x', bx - 1);
            vbar.setAttribute('y', padY);
            vbar.setAttribute('width', '2');
            vbar.setAttribute('height', totalH);
            vbar.setAttribute('fill', 'url(#busGrad)');
            vbar.setAttribute('opacity', '0.5');
            svg.appendChild(vbar);
        }

        /* ── Mouse-tracking 3D tilt ── */
        const card = document.getElementById('panelCard');
        const stage = document.getElementById('stage');
        const specular = document.getElementById('specular');
        const shadow = document.getElementById('panelShadow');

        let currentX = 0, currentY = 0;
        let targetX = 0, targetY = 0;

        const MAX_TILT = 22; // degrees
        function lerp(a, b, t) { return a + (b - a) * t; }

        stage.addEventListener('mousemove', (e) => {
            const rect = stage.getBoundingClientRect();
            const cx = rect.left + rect.width / 2;
            const cy = rect.top + rect.height / 2;
            const mx = e.clientX - cx;
            const my = e.clientY - cy;

            // Normalize −1..1
            const nx = mx / (rect.width / 2);
            const ny = my / (rect.height / 2);

            targetX = -ny * MAX_TILT;   // rotateX (tilt up/down)
            targetY = nx * MAX_TILT;   // rotateY (tilt left/right)

            // Move specular opposite to tilt direction
            if (specular) {
                const sx = 50 - nx * 30;
                const sy = 50 - ny * 30;
                specular.style.background = `radial-gradient(ellipse 55% 50% at ${sx}% ${sy}%, rgba(255,255,255,0.22) 0%, transparent 65%)`;
            }
        });

        stage.addEventListener('mouseleave', () => {
            targetX = 0;
            targetY = 0;
            if (specular) {
                specular.style.background = 'radial-gradient(ellipse 55% 50% at 30% 30%, rgba(255,255,255,0.12) 0%, transparent 65%)';
            }
        });

        function animate() {
            currentX = lerp(currentX, targetX, 0.1);
            currentY = lerp(currentY, targetY, 0.1);

            if (card) {
                card.style.transform = `perspective(1200px) rotateX(${currentX}deg) rotateY(${currentY}deg) scale3d(1.02,1.02,1.02)`;
            }

            // Shadow moves opposite
            if (shadow) {
                const shadowX = currentY * 1.5;
                shadow.style.transform = `translateX(calc(-50% + ${shadowX}px)) scaleX(${1 - Math.abs(currentY) / 80})`;
            }

            requestAnimationFrame(animate);
        }
        animate();

        /* ── Live watt counter animation ── */
        const wattEl = document.getElementById('wattCounter');
        let base = 4280;
        function tickWatt() {
            const delta = (Math.random() - 0.48) * 12;
            base = Math.max(4100, Math.min(4450, base + delta));
            if (wattEl) wattEl.textContent = Math.round(base).toLocaleString();
            setTimeout(tickWatt, 600 + Math.random() * 600);
        }
        setTimeout(tickWatt, 2000);
    };

    initSolarXHero();

    // Handle Area Form Submission (Global)
    const areaForm = document.getElementById('area-form');
    if (areaForm) {
        areaForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = areaForm.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.innerText;
            
            submitBtn.disabled = true;
            submitBtn.innerText = 'Sending...';
            
            const formData = new FormData(areaForm);
            const leadData = {
                full_name: formData.get('fullName') || formData.get('companyName'),
                phone: formData.get('phone'),
                city: formData.get('location') || 'Area Page',
                message: `Lead from area page: ${window.location.pathname}`,
                status: 'New'
            };

            try {
                // Sync to Supabase
                if (typeof _supabase !== 'undefined') {
                    await _supabase.from('leads').insert([leadData]);
                }
                // Submit to FormSubmit
                areaForm.submit();
            } catch (err) {
                console.error('Area form sync error:', err);
                areaForm.submit();
            }
        });
    }

});

