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

  // Scroll to Chapter 4 (~85%)
  await page.evaluate(() => {
    window.scrollTo(0, 2800);
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'C:\\Users\\KIIT0001\\.gemini\\antigravity\\brain\\74d70c66-0eaf-40bc-9050-334d323e8cdd\\journey_chapter4.png' });
  console.log('Saved journey_chapter4.png');

  // Scroll to Calculator & Lead form (~100%)
  await page.evaluate(() => {
    const el = document.getElementById('journeySavingsSection');
    if (el) el.scrollIntoView({ block: 'start' });
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'C:\\Users\\KIIT0001\\.gemini\\antigravity\\brain\\74d70c66-0eaf-40bc-9050-334d323e8cdd\\journey_calculator.png' });
  console.log('Saved journey_calculator.png');

  await browser.close();
})();
