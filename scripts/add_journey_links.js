const fs = require('fs');
const path = require('path');

const rootFiles = fs.readdirSync('.').filter(f => f.endsWith('.html'));
let navCount = 0;
let mobileCount = 0;
let footerCount = 0;

rootFiles.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let changed = false;

  // 1. Desktop Nav
  if (content.includes('class="dt-nav-links"') || content.includes("class='dt-nav-links'")) {
    const navMatch = content.match(/<nav[^>]*class=["'][^"']*dt-nav-links[^"']*["'][^>]*>([\s\S]*?)<\/nav>/);
    if (navMatch && !navMatch[1].includes('href="/journey"') && !navMatch[1].includes("href='/journey'")) {
      const isJourney = (f === 'journey.html');
      const journeyLink = isJourney ? '<a href="/journey" class="active">Journey</a>' : '<a href="/journey">Journey</a>';
      if (content.includes('<a href="/gallery">Gallery</a>')) {
        content = content.replace(
          '<a href="/gallery">Gallery</a>',
          `<a href="/gallery">Gallery</a>\n                ${journeyLink}`
        );
        navCount++;
        changed = true;
      }
    }
  }

  // 2. Mobile Nav
  if (content.includes('class="dt-mobile-links"') || content.includes("class='dt-mobile-links'")) {
    const mobileMatch = content.match(/<ul[^>]*class=["'][^"']*dt-mobile-links[^"']*["'][^>]*>([\s\S]*?)<\/ul>/);
    if (mobileMatch && !mobileMatch[1].includes('href="/journey"') && !mobileMatch[1].includes("href='/journey'")) {
      if (content.includes('<li><a href="/gallery">Gallery</a></li>')) {
        content = content.replace(
          '<li><a href="/gallery">Gallery</a></li>',
          '<li><a href="/gallery">Gallery</a></li>\n                <li><a href="/journey">The Solar Journey (3D)</a></li>'
        );
        mobileCount++;
        changed = true;
      }
    }
  }

  // 3. Footer Links
  if (content.includes('class="dt-footer-links"') && !content.includes('href="/journey"')) {
    if (content.includes('<li><a href="/gallery"')) {
      content = content.replace(
        /<li><a href="\/gallery"[^>]*>[\s\S]*?<\/a><\/li>/,
        match => `${match}\n                        <li><a href="/journey"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Interactive 3D Journey</a></li>`
      );
      footerCount++;
      changed = true;
    } else if (content.includes('<li><a href="/projects"')) {
      content = content.replace(
        /<li><a href="\/projects"[^>]*>[\s\S]*?<\/a><\/li>/,
        match => `${match}\n                        <li><a href="/journey"><i class="fas fa-chevron-right" style="font-size: 10px; color: var(--gold-accent);"></i> Interactive 3D Journey</a></li>`
      );
      footerCount++;
      changed = true;
    }
  }

  if (changed) {
    fs.writeFileSync(f, content, 'utf8');
    console.log(`Updated journey links in ${f}`);
  }
});

console.log(`Done: Nav in ${navCount} files, Mobile in ${mobileCount} files, Footer in ${footerCount} files.`);
