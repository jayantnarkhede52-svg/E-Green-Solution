const fs = require('fs');
const html = fs.readFileSync('areas.html', 'utf8');
const cardRegex = /<div class="area-card"[\s\S]*?<\/div>\s*<\/div>/g;
let match;
let i = 0;
while ((match = cardRegex.exec(html)) !== null) {
  i++;
  const title = match[0].match(/<h3>(.*?)<\/h3>/);
  const meta = [...match[0].matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m => m[1].replace(/<[^>]+>/g, '').trim());
  const btn = match[0].match(/class="area-link"[^>]*>([\s\S]*?)<\/a>/);
  console.log(`Card ${i}: ${title ? title[1] : 'Unknown'}`);
  console.log(`  Meta items: ${meta.length}`);
  meta.forEach(m => console.log(`    - ${m}`));
  console.log(`  Button: ${btn ? btn[1].replace(/<[^>]+>/g, '').trim() : 'None'}`);
}
