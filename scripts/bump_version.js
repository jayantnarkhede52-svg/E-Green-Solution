const fs = require('fs');
const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

let count = 0;
for (const file of files) {
  let content = fs.readFileSync(file, 'utf8');
  if (content.includes('layout-polish.css?v=2.5')) {
    content = content.replaceAll('layout-polish.css?v=2.5', 'layout-polish.css?v=2.6');
    fs.writeFileSync(file, content, 'utf8');
    count++;
  }
}
console.log(`Updated cache buster to v=2.6 across ${count} HTML files.`);
