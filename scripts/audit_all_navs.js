const fs = require('fs');
const glob = fs.readdirSync('.').filter(f => f.endsWith('.html'));

console.log(`Checking ${glob.length} root HTML files for nav links...`);

const missingJourney = [];
const missingBlog = [];
const missingJourneyMobile = [];
const missingBlogMobile = [];

for (const file of glob) {
  const content = fs.readFileSync(file, 'utf8');
  
  // Check desktop nav
  const desktopNavMatch = content.match(/<nav class="dt-nav-links"[\s\S]*?<\/nav>/);
  if (desktopNavMatch) {
    const navText = desktopNavMatch[0];
    if (!navText.includes('href="/journey"')) {
      missingJourney.push(file);
    }
    if (!navText.includes('href="/blog"')) {
      missingBlog.push(file);
    }
  }
  
  // Check mobile links
  const mobileNavMatch = content.match(/<ul class="dt-mobile-links"[\s\S]*?<\/ul>/);
  if (mobileNavMatch) {
    const mText = mobileNavMatch[0];
    if (!mText.includes('href="/journey"')) {
      missingJourneyMobile.push(file);
    }
    if (!mText.includes('href="/blog"')) {
      missingBlogMobile.push(file);
    }
  }
}

console.log('Missing /journey in Desktop Nav:', missingJourney);
console.log('Missing /blog in Desktop Nav:', missingBlog);
console.log('Missing /journey in Mobile Drawer:', missingJourneyMobile);
console.log('Missing /blog in Mobile Drawer:', missingBlogMobile);
