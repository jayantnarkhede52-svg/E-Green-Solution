(function () {
  function setupMobileNavigation() {
    const drawer = document.getElementById('dt-mobile-drawer');
    const trigger = document.getElementById('dt-hamburger');
    const closeButton = document.getElementById('dt-drawer-close');
    const backdrop = document.getElementById('dt-backdrop');

    if (!drawer || !trigger || drawer.dataset.accessibilityReady === 'true') return;
    drawer.dataset.accessibilityReady = 'true';
    drawer.inert = true;
    drawer.setAttribute('aria-hidden', 'true');
    drawer.removeAttribute('aria-modal');
    if (backdrop) backdrop.setAttribute('aria-hidden', 'true');

    const background = Array.from(document.body.children).filter((element) =>
      element !== drawer && element !== backdrop && !['SCRIPT', 'STYLE', 'LINK'].includes(element.tagName)
    );
    const originalBackgroundState = new Map(background.map((element) => [element, {
      inert: element.inert,
      ariaHidden: element.getAttribute('aria-hidden')
    }]));
    let wasOpen = drawer.classList.contains('active');

    function syncDrawerState() {
      const isOpen = drawer.classList.contains('active');
      if (isOpen === wasOpen) return;
      wasOpen = isOpen;

      drawer.inert = !isOpen;
      drawer.setAttribute('aria-hidden', String(!isOpen));
      if (isOpen) {
        drawer.setAttribute('aria-modal', 'true');
        background.forEach((element) => {
          element.inert = true;
          element.setAttribute('aria-hidden', 'true');
        });
        requestAnimationFrame(() => {
          const first = drawer.querySelector('button:not([disabled]), a[href], input:not([disabled]), select:not([disabled])');
          (first || drawer).focus();
        });
      } else {
        drawer.removeAttribute('aria-modal');
        originalBackgroundState.forEach((state, element) => {
          element.inert = state.inert;
          if (state.ariaHidden === null) element.removeAttribute('aria-hidden');
          else element.setAttribute('aria-hidden', state.ariaHidden);
        });
        trigger.focus();
      }
    }

    const observer = new MutationObserver(syncDrawerState);
    observer.observe(drawer, { attributes: true, attributeFilter: ['class'] });

    document.addEventListener('keydown', (event) => {
      if (!drawer.classList.contains('active')) return;

      if (event.key === 'Escape') {
        event.preventDefault();
        if (closeButton) closeButton.click();
        else trigger.click();
        return;
      }

      if (event.key !== 'Tab') return;
      const focusable = Array.from(drawer.querySelectorAll(
        'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
      )).filter((element) => element.getClientRects().length && getComputedStyle(element).visibility !== 'hidden');
      if (!focusable.length) {
        event.preventDefault();
        drawer.focus();
        return;
      }

      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (event.shiftKey && (document.activeElement === first || !drawer.contains(document.activeElement))) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && (document.activeElement === last || !drawer.contains(document.activeElement))) {
        event.preventDefault();
        first.focus();
      }
    });

    syncDrawerState();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupMobileNavigation, { once: true });
  } else {
    setupMobileNavigation();
  }
})();
