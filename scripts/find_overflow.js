const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:5000/areas', { waitUntil: 'domcontentloaded' });
  
  const docScrollWidth = await page.evaluate(() => document.documentElement.scrollWidth);
  const bodyScrollWidth = await page.evaluate(() => document.body.scrollWidth);
  console.log(`Viewport: 390. docScrollWidth: ${docScrollWidth}, bodyScrollWidth: ${bodyScrollWidth}`);
  
  const overflowing = await page.evaluate(() => {
    const elms = Array.from(document.querySelectorAll('*'));
    return elms
      .filter(el => {
        const rect = el.getBoundingClientRect();
        return rect.right > 390 + 2; // tolerance
      })
      .map(el => ({
        tag: el.tagName,
        id: el.id,
        className: (el.className && typeof el.className === 'string') ? el.className.trim() : '',
        right: Math.round(el.getBoundingClientRect().right),
        width: Math.round(el.getBoundingClientRect().width),
        html: el.outerHTML.substring(0, 100)
      }))
      .slice(0, 20);
  });
  
  console.log('Overflowing elements count:', overflowing.length);
  console.log(JSON.stringify(overflowing, null, 2));
  
  await browser.close();
})();
