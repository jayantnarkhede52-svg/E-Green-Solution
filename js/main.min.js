// Wait for DOM to load
document.addEventListener('DOMContentLoaded', () => {
    
    // Initialize GSAP
    gsap.registerPlugin(ScrollTrigger);

    // Check if user prefers reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Hero Animations
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

    // Mouse Parallax Effect for Hero (Desktop Only) - Throttled for performance
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

        document.addEventListener('mouseleave', () => {
            heroCard.style.transform = `rotateY(0deg) rotateX(0deg)`;
            heroCard.style.transition = 'all 0.5s ease';
        });

        document.addEventListener('mouseenter', () => {
             heroCard.style.transition = 'none';
        });
    }

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

    // Hamburger Menu Toggle
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (hamburger && mobileMenu) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            mobileMenu.classList.toggle('active');
            document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
        });

        // Close mobile menu when a link is clicked
        const mobileLinks = mobileMenu.querySelectorAll('a');
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                mobileMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });

        // Close mobile menu on window resize
        window.addEventListener('resize', () => {
            if (window.innerWidth > 768) {
                hamburger.classList.remove('active');
                mobileMenu.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }

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
            gsap.from(grid.children, {
                scrollTrigger: {
                    trigger: grid,
                    start: "top 85%",
                    toggleActions: "play none none none"
                },
                y: 50,
                opacity: 0,
                duration: 0.8,
                stagger: 0.15,
                ease: "power2.out"
            });
        }
    });

    // General Section Reveals
    const revealElements = document.querySelectorAll('.section-header, .about-section, .service-row');
    revealElements.forEach(el => {
        if (!prefersReducedMotion) {
            gsap.from(el, {
                scrollTrigger: {
                    trigger: el,
                    start: "top 85%",
                    toggleActions: "play none none none"
                },
                y: 40,
                opacity: 0,
                duration: 1,
                ease: "power2.out"
            });
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

    // Calculator & Wizard Logic
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
        const summaryBill = document.getElementById('summary-bill');

        function calculateSolar() {
            let bill = parseFloat(monthlyBillInput.value) || 0;
            let rate = parseFloat(unitRateInput.value) || 10;
            
            // Formula for Capacity (for technical transparency, though savings is fixed at 90%)
            let dailyUnitsRequired = bill / (rate * 30);
            let capacityKw = dailyUnitsRequired / 4; 
            if(capacityKw < 1 && bill > 0) capacityKw = 1;
            
            // Logic update: Savings are exactly 90% of the bill as requested
            let monthlySavings = Math.round(bill * 0.9);
            
            let systemSize = capacityKw.toFixed(1);
            let spaceRequired = Math.round(capacityKw * 100); 
            let cost = Math.round(capacityKw * 52000); // Updated to ₹52,000/kW as requested

            // Update UI
            resSystemSize.innerText = systemSize;
            resSpace.innerText = spaceRequired;
            resMonthlySavings.innerText = monthlySavings.toLocaleString('en-IN');
            resSystemCost.innerText = cost.toLocaleString('en-IN');
            summaryBill.innerText = bill.toLocaleString('en-IN');
        }

        // Navigation logic
        btnShowResults.addEventListener('click', () => {
            calculateSolar();
            step1.classList.remove('active');
            step2.classList.add('active');
            dot1.classList.remove('active');
            dot2.classList.add('active');
            window.scrollTo({ top: document.getElementById('calculator-section').offsetTop - 100, behavior: 'smooth' });
        });

        btnBackToInput.addEventListener('click', () => {
            step2.classList.remove('active');
            step1.classList.add('active');
            dot2.classList.remove('active');
            dot1.classList.add('active');
        });

        // Sync inputs
        monthlyBillRange.addEventListener('input', (e) => {
            monthlyBillInput.value = e.target.value;
        });
        monthlyBillInput.addEventListener('input', (e) => {
            monthlyBillRange.value = e.target.value;
        });

        // Initial check
        calculateSolar();
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

});
