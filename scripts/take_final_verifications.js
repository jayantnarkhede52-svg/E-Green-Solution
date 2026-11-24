const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  // 1. Areas PC scrolled to cards
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 900 });
    await page.goto('http://localhost:5000/areas', { waitUntil: 'domcontentloaded' });
    await page.evaluate(() => {
      const el = document.getElementById('areasGrid');
      if (el) el.scrollIntoView({ block: 'start' });
    });
    await new Promise(r => setTimeout(r, 600));
    await page.screenshot({ path: 'C:\\Users\\KIIT0001\\.gemini\\antigravity\\brain\\74d70c66-0eaf-40bc-9050-334d323e8cdd\\final_areas_pc.png' });
    await page.close();
    console.log('Captured final_areas_pc.png');
  }

  // 2. Areas Mobile
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 390, height: 844 });
    await page.goto('http://localhost:5000/areas', { waitUntil: 'domcontentloaded' });
    await page.evaluate(() => {
      const el = document.getElementById('areasGrid');
      if (el) el.scrollIntoView({ block: 'start' });
    });
    await new Promise(r => setTimeout(r, 600));
    await page.screenshot({ path: 'C:\\Users\\KIIT0001\\.gemini\\antigravity\\brain\\74d70c66-0eaf-40bc-9050-334d323e8cdd\\final_areas_mobile.png' });
    await page.close();
    console.log('Captured final_areas_mobile.png');
  }

  // 3. About Page Values & Why Choose Us
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 900 });
    await page.goto('http://localhost:5000/about', { waitUntil: 'domcontentloaded' });
    await page.evaluate(() => {
      const el = document.querySelector('.why-us-grid');
      if (el) el.scrollIntoView({ block: 'center' });
    });
    await new Promise(r => setTimeout(r, 600));
    await page.screenshot({ path: 'C:\\Users\\KIIT0001\\.gemini\\antigravity\\brain\\74d70c66-0eaf-40bc-9050-334d323e8cdd\\final_about_values.png' });

    // Scroll to Why Choose Us / Standard
    await page.evaluate(() => {
      const el = document.querySelector('.dt-why-us-grid');
      if (el) el.scrollIntoView({ block: 'center' });
    });
    await new Promise(r => setTimeout(r, 600));
    await page.screenshot({ path: 'C:\\Users\\KIIT0001\\.gemini\\antigravity\\brain\\74d70c66-0eaf-40bc-9050-334d323e8cdd\\final_about_whyus.png' });
    await page.close();
    console.log('Captured final_about_values.png and final_about_whyus.png');
  }

  // 4. Gallery PC
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 900 });
    await page.goto('http://localhost:5000/gallery', { waitUntil: 'domcontentloaded' });
    await page.evaluate(() => {
      const el = document.getElementById('videoGrid');
      if (el) el.scrollIntoView({ block: 'center' });
    });
    await new Promise(r => setTimeout(r, 600));
    await page.screenshot({ path: 'C:\\Users\\KIIT0001\\.gemini\\antigravity\\brain\\74d70c66-0eaf-40bc-9050-334d323e8cdd\\final_gallery_pc.png' });
    await page.close();
    console.log('Captured final_gallery_pc.png');
  }

  // 5. Journey PC scrubber
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 900 });
    await page.goto('http://localhost:5000/journey?p=0.45', { waitUntil: 'domcontentloaded' });
    await new Promise(r => setTimeout(r, 1200));
    await page.screenshot({ path: 'C:\\Users\\KIIT0001\\.gemini\\antigravity\\brain\\74d70c66-0eaf-40bc-9050-334d323e8cdd\\final_journey_p45.png' });
    await page.close();
    console.log('Captured final_journey_p45.png');
  }

  await browser.close();
  console.log('All final verification screenshots successfully taken!');
})();
