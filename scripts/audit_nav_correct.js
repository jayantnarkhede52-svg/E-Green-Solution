const fs = require('fs');
const glob = fs.readdirSync('.').filter(f => f.endsWith('.html'));

console.log(`Checking ${glob.length} root HTML files for nav links...`);

const missingDesktopJourney = [];
const missingDesktopBlog = [];
const missingMobileJourney = [];
const missingMobileBlog = [];

for (const file of glob) {
  const content = fs.readFileSync(file, 'utf8');
  
  // Desktop Nav: <nav class="dt-nav-links" ... </nav>
  const desktopNavMatch = content.match(/<nav class="dt-nav-links"[\s\S]*?<\/nav>/);
  if (desktopNavMatch) {
    const navText = desktopNavMatch[0];
    if (!navText.includes('href="/journey"')) {
      missingDesktopJourney.push(file);
    }
    if (!navText.includes('href="/blog"')) {
      missingDesktopBlog.push(file);
    }
  }
  
  // Mobile Drawer: id="dt-mobile-drawer" or class="dt-mobile-menu"
  const mobileDrawerMatch = content.match(/id="dt-mobile-drawer"[\s\S]*?<\/div>\s*<\/div>/);
  if (mobileDrawerMatch) {
    const mText = mobileDrawerMatch[0];
    if (!mText.includes('href="/journey"')) {
      missingMobileJourney.push(file);
    }
    if (!mText.includes('href="/blog"')) {
      missingMobileBlog.push(file);
    }
  }
}

console.log('Missing /journey in Desktop Nav:', missingDesktopJourney);
console.log('Missing /blog in Desktop Nav:', missingDesktopBlog);
console.log('Missing /journey in Mobile Drawer:', missingMobileJourney);
console.log('Missing /blog in Mobile Drawer:', missingMobileBlog);
