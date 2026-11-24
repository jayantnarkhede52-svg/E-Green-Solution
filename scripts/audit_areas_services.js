const fs = require('fs');

const areasHtml = fs.readFileSync('areas.html', 'utf8');
const cardBlocks = areasHtml.split('<div class="area-card"');
cardBlocks.shift(); // remove header

console.log('=== AREA CARDS AUDIT IN AREAS.HTML ===');
cardBlocks.forEach((b, i) => {
  const title = (b.match(/<h3>([^<]+)<\/h3>/) || [])[1] || 'Unknown';
  const href = (b.match(/href="([^"#]+)"/) || [])[1] || 'No Link';
  const exists = href.startsWith('http') || fs.existsSync(href.replace(/^\//, '') + '.html') || fs.existsSync(href.replace(/^\//, ''));
  console.log(`${i+1}. ${title} -> ${href} [${exists ? 'EXISTS' : 'MISSING'}]`);
});

// Check services dropdown in index.html
const indexHtml = fs.readFileSync('index.html', 'utf8');
const servicesMatches = indexHtml.match(/<a href="([^"#]+)" class="dt-drop-item"/g) || [];
console.log('\n=== SERVICES DROPDOWN AUDIT ===');
servicesMatches.forEach((s, i) => {
  const href = (s.match(/href="([^"#]+)"/) || [])[1];
  const exists = fs.existsSync(href.replace(/^\//, '') + '.html');
  console.log(`${i+1}. ${href} [${exists ? 'EXISTS' : 'MISSING'}]`);
});

// Check all links in dt-footer
const footerLinks = indexHtml.match(/<ul class="dt-footer-links">[\s\S]*?<\/ul>/g) || [];
console.log('\n=== FOOTER LINKS AUDIT ===');
footerLinks.forEach(fl => {
  const matches = fl.match(/href="([^"#]+)"/g) || [];
  matches.forEach(m => {
    const href = (m.match(/href="([^"#]+)"/) || [])[1];
    const exists = fs.existsSync(href.replace(/^\//, '') + '.html') || fs.existsSync(href.replace(/^\//, ''));
    console.log(`- ${href} [${exists ? 'EXISTS' : 'MISSING'}]`);
  });
});
