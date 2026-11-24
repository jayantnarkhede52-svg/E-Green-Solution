const fs = require('fs');
const html = fs.readFileSync('areas.html', 'utf8');

const regex = /<h3>(.*?)<\/h3>[\s\S]*?<ul class="area-meta-list">([\s\S]*?)<\/ul>/g;
let m;
while ((m = regex.exec(html)) !== null) {
  console.log('--- ' + m[1] + ' ---');
  const items = [...m[2].matchAll(/<li>([\s\S]*?)<\/li>/g)].map(x => x[1].replace(/<[^>]+>/g, '').trim());
  items.forEach(it => console.log('  * ' + it));
}
