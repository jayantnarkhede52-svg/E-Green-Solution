const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:5000/solar-guide', { waitUntil: 'domcontentloaded' });
  await page.screenshot({
    path: 'C:\\Users\\KIIT0001\\.gemini\\antigravity\\brain\\74d70c66-0eaf-40bc-9050-334d323e8cdd\\solar_guide_check.png',
    fullPage: false
  });
  console.log('Saved solar_guide_check.png');
  await browser.close();
})();
