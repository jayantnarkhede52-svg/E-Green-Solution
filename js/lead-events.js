// Record contact actions without sending form values or personal details.
(function () {
    document.addEventListener('click', function (event) {
        var link = event.target.closest('a[href]');
        if (!link || typeof window.gtag !== 'function') return;

        var href = link.getAttribute('href') || '';
        if (/^tel:/i.test(href)) {
            window.gtag('event', 'contact_phone_click');
        } else if (/^https?:\/\/(?:www\.)?(?:wa\.me|api\.whatsapp\.com)\//i.test(href)) {
            window.gtag('event', 'contact_whatsapp_click');
        }
    });
}());
