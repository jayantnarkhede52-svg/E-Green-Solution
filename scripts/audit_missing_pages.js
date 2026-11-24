const fs = require('fs');
const path = require('path');

const ROOT = process.cwd();

// Find all HTML files recursively
function getHtmlFiles(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  for (const file of list) {
    if (file === 'node_modules' || file.startsWith('.')) continue;
    const full = path.join(dir, file);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      results = results.concat(getHtmlFiles(full));
    } else if (file.endsWith('.html')) {
      results.push(path.relative(ROOT, full).replace(/\\/g, '/'));
    }
  }
  return results;
}

const allHtmlFiles = getHtmlFiles(ROOT);
console.log('Total HTML files found in repo:', allHtmlFiles.length);

const hrefRegex = /href=["']([^"'#]+)["']/g;
const linksFound = [];

allHtmlFiles.forEach(relPath => {
  const content = fs.readFileSync(path.join(ROOT, relPath), 'utf8');
  let match;
  while ((match = hrefRegex.exec(content)) !== null) {
    let link = match[1].trim();
    if (!link) continue;
    if (link.startsWith('http:') || link.startsWith('https:') || link.startsWith('//')) continue;
    if (link.startsWith('tel:') || link.startsWith('mailto:') || link.startsWith('javascript:')) continue;
    
    link = link.split('?')[0].split('#')[0];
    if (!link) continue;

    const ext = path.extname(link).toLowerCase();
    if (['.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.webp', '.pdf', '.mp4'].includes(ext)) {
      continue;
    }

    linksFound.push({ file: relPath, link });
  }
});

// Check sitemap.xml
if (fs.existsSync('sitemap.xml')) {
  const sitemap = fs.readFileSync('sitemap.xml', 'utf8');
  const locRegex = /<loc>(https?:\/\/[^\/]+)?([^<]+)<\/loc>/g;
  let sMatch;
  while ((sMatch = locRegex.exec(sitemap)) !== null) {
    let sLink = sMatch[2].trim().split('?')[0].split('#')[0];
    if (sLink && !sLink.endsWith('.xml')) {
      linksFound.push({ file: 'sitemap.xml', link: sLink });
    }
  }
}

// Redirects in server.js
const serverContent = fs.readFileSync('server.js', 'utf8');
const redirectMap = new Map();
const redirRegex = /if\s*\(\s*pathname\s*===?\s*['"]([^'"]+)['"][^)]*\)\s*\{\s*res\.writeHead\(301,\s*\{\s*'Location':\s*['"]([^'"]+)['"]/g;
let rm;
while ((rm = redirRegex.exec(serverContent)) !== null) {
  redirectMap.set(rm[1], rm[2]);
}

const resolvedStatus = new Map();
const missingLinks = [];

linksFound.forEach(({ file, link }) => {
  // Normalize
  let target = link.startsWith('/') ? link.slice(1) : link;
  if (!target) target = 'index.html';

  let exists = false;
  let reason = '';

  // Direct file
  if (fs.existsSync(path.join(ROOT, target)) && fs.statSync(path.join(ROOT, target)).isFile()) {
    exists = true;
  } else if (fs.existsSync(path.join(ROOT, target + '.html')) && fs.statSync(path.join(ROOT, target + '.html')).isFile()) {
    exists = true;
  } else if (fs.existsSync(path.join(ROOT, target, 'index.html')) && fs.statSync(path.join(ROOT, target, 'index.html')).isFile()) {
    exists = true;
  } else if (redirectMap.has(link) || link.startsWith('/api/') || link === '/admin/dashboard') {
    exists = true;
  }

  if (!exists) {
    missingLinks.push({ file, link });
  }
});

const missingGrouped = {};
missingLinks.forEach(m => {
  if (!missingGrouped[m.link]) missingGrouped[m.link] = new Set();
  missingGrouped[m.link].add(m.file);
});

console.log('\n--- BROKEN / MISSING INTERNAL LINKS ---');
for (const [link, files] of Object.entries(missingGrouped)) {
  console.log(`❌ "${link}" linked in:`, Array.from(files).join(', '));
}
if (Object.keys(missingGrouped).length === 0) {
  console.log('✅ None! All linked internal URLs resolve to existing files or redirects.');
}

console.log('\n--- DETAILED INVENTORY OF ALL REPOSITORY PAGES ---');
console.log(allHtmlFiles.sort().join('\n'));
