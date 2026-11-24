const fs = require('fs');
const path = require('path');

const blogDir = path.join(__dirname, '..', 'blog');
if (fs.existsSync(blogDir)) {
  const blogFiles = fs.readdirSync(blogDir).filter(f => f.endsWith('.html'));
  blogFiles.forEach(f => {
    const full = path.join(blogDir, f);
    let content = fs.readFileSync(full, 'utf8');
    let changed = false;

    if (content.includes('class="dt-nav-links"') || content.includes("class='dt-nav-links'")) {
      const isIndex = (f === 'index.html');
      const blogLink = isIndex ? '<a href="/blog" class="active">Blog</a>' : '<a href="/blog">Blog</a>';
      const navMatch = content.match(/<nav[^>]*class=["'][^"']*dt-nav-links[^"']*["'][^>]*>([\s\S]*?)<\/nav>/);
      if (navMatch && !navMatch[1].includes('/blog')) {
        if (content.includes('<a href="/areas">Areas</a>')) {
          content = content.replace(
            '<a href="/areas">Areas</a>',
            `<a href="/areas">Areas</a>\n                ${blogLink}`
          );
          changed = true;
        }
      }
    }

    if (content.includes('class="dt-mobile-links"') || content.includes("class='dt-mobile-links'")) {
      const mobileMatch = content.match(/<ul[^>]*class=["'][^"']*dt-mobile-links[^"']*["'][^>]*>([\s\S]*?)<\/ul>/);
      if (mobileMatch && !mobileMatch[1].includes('/blog')) {
        if (content.includes('<li><a href="/areas">Areas</a></li>')) {
          content = content.replace(
            '<li><a href="/areas">Areas</a></li>',
            '<li><a href="/areas">Areas</a></li>\n                <li><a href="/blog">Blog</a></li>'
          );
          changed = true;
        }
      }
    }

    // Also update layout-polish.css cache bust if present
    if (content.includes('layout-polish.css')) {
      content = content.replace(/layout-polish\.css(\?v=[\d\.]+)?/g, 'layout-polish.css?v=2.5');
      changed = true;
    }

    if (changed) {
      fs.writeFileSync(full, content, 'utf8');
      console.log(`Updated blog nav in blog/${f}`);
    }
  });
}
