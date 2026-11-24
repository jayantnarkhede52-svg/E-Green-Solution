const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:5000/journey', { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1000));

  await page.evaluate(() => {
    window.scrollTo(0, 1000);
  });
  await new Promise(r => setTimeout(r, 500));

  const debug = await page.evaluate(() => {
    const track = document.getElementById('journeyScrollTrack');
    const vp = document.getElementById('journeyStickyViewport');
    const canvas = document.getElementById('journeyCanvas');
    return {
      windowScrollY: window.scrollY,
      trackRect: track ? track.getBoundingClientRect() : null,
      vpRect: vp ? vp.getBoundingClientRect() : null,
      canvasRect: canvas ? canvas.getBoundingClientRect() : null,
      vpComputedStyle: vp ? {
        position: window.getComputedStyle(vp).position,
        top: window.getComputedStyle(vp).top,
        transform: window.getComputedStyle(vp).transform,
        display: window.getComputedStyle(vp).display,
        visibility: window.getComputedStyle(vp).visibility
      } : null,
      canvasComputedStyle: canvas ? {
        width: canvas.width,
        height: canvas.height,
        display: window.getComputedStyle(canvas).display
      } : null
    };
  });
  console.log('DEBUG:', JSON.stringify(debug, null, 2));
  await browser.close();
})();
