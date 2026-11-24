// Navigation controls for pages that do not have an inline drawer controller.
document.addEventListener('DOMContentLoaded', function () {
  const trigger = document.getElementById('dt-hamburger');
  const drawer = document.getElementById('dt-mobile-drawer');
  const backdrop = document.getElementById('dt-backdrop');
  const close = document.getElementById('dt-drawer-close');
  if (!trigger || !drawer || !backdrop) return;

  function setOpen(open) {
    drawer.classList.toggle('active', open);
    backdrop.classList.toggle('active', open);
    trigger.classList.toggle('active', open);
    trigger.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
  }

  trigger.addEventListener('click', () => setOpen(!drawer.classList.contains('active')));
  if (close) close.addEventListener('click', () => setOpen(false));
  backdrop.addEventListener('click', () => setOpen(false));
});
