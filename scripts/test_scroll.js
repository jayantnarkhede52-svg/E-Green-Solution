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

  // Wait 1 second
  await new Promise(r => setTimeout(r, 1500));

  const state = await page.evaluate(() => {
    const c = document.getElementById('journeyCanvas');
    return {
      canvasW: c ? c.width : null,
      canvasH: c ? c.height : null,
      scrollTrackHeight: document.getElementById('journeyScrollTrack').offsetHeight,
      scrollY: window.scrollY,
      framesLoaded: typeof loaded !== 'undefined' ? loaded : null,
      totalFrames: typeof totalFrames !== 'undefined' ? totalFrames : null,
      isUsingVideoFrames: typeof isUsingVideoFrames !== 'undefined' ? isUsingVideoFrames : null
    };
  });
  console.log('State:', state);

  // Now simulate user scrolling smoothly down!
  await page.evaluate(() => {
    window.scrollTo(0, 1500);
  });
  await new Promise(r => setTimeout(r, 800));

  await page.screenshot({ path: 'C:\\Users\\KIIT0001\\.gemini\\antigravity\\brain\\74d70c66-0eaf-40bc-9050-334d323e8cdd\\journey_scrolled_test.png' });
  console.log('Saved journey_scrolled_test.png');

  await browser.close();
})();
