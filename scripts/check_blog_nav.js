const fs = require('fs');
const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));
const hasBlogInNav = [];
files.forEach(f => {
  const content = fs.readFileSync(f, 'utf8');
  if (content.includes('dt-nav-links') && content.includes('<a href="/blog"')) {
    hasBlogInNav.push(f);
  }
});
console.log('Files with /blog in nav:', hasBlogInNav.length, hasBlogInNav);
