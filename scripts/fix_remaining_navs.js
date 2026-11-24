const fs = require('fs');

// 1. Fix gallery.html desktop nav
let galleryHtml = fs.readFileSync('gallery.html', 'utf8');
if (!galleryHtml.includes('<a href="/journey">Journey</a>')) {
  galleryHtml = galleryHtml.replace(
    '<a href="/gallery" class="active">Gallery</a>',
    '<a href="/gallery" class="active">Gallery</a>\n                <a href="/journey">Journey</a>'
  );
  fs.writeFileSync('gallery.html', galleryHtml, 'utf8');
  console.log('Fixed gallery.html desktop nav');
}

// 2. Fix areas.html
let areasHtml = fs.readFileSync('areas.html', 'utf8');
if (!areasHtml.includes('<a href="/blog">Blog</a>')) {
  areasHtml = areasHtml.replace(
    '<a href="/areas" class="active">Areas</a>',
    '<a href="/areas" class="active">Areas</a>\n                <a href="/blog">Blog</a>'
  );
}
// Also fix mobile drawer li in areas.html
areasHtml = areasHtml.replace(
  '<li><a href="/areas">Areas</a>\n                <a href="/blog">Blog</a></li>',
  '<li><a href="/areas">Areas</a></li>\n                <li><a href="/blog">Blog</a></li>'
);
fs.writeFileSync('areas.html', areasHtml, 'utf8');
console.log('Fixed areas.html');

// 3. Fix the regional pages missing /blog in desktop nav
const regionalFiles = [
  'solar-panel-baner-bavdhan.html',
  'solar-panel-bhosari-pcmc.html',
  'solar-panel-chakan.html',
  'solar-panel-kiwale.html',
  'solar-panel-lonavala.html',
  'solar-panel-pimpri-chinchwad.html',
  'solar-panel-pune.html'
];

for (const file of regionalFiles) {
  let content = fs.readFileSync(file, 'utf8');
  // Check if nav has /blog
  const navMatch = content.match(/<nav class="dt-nav-links"[\s\S]*?<\/nav>/);
  if (navMatch && !navMatch[0].includes('href="/blog"')) {
    // Replace <a href="/about">About</a> in the nav with <a href="/blog">Blog</a>\n                <a href="/about">About</a>
    const updatedNav = navMatch[0].replace(
      '<a href="/about">About</a>',
      '<a href="/blog">Blog</a>\n                <a href="/about">About</a>'
    );
    content = content.replace(navMatch[0], updatedNav);
    fs.writeFileSync(file, content, 'utf8');
    console.log(`Fixed desktop nav in ${file}`);
  }
}
