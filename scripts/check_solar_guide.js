const fs = require('fs');
const html = fs.readFileSync('solar-guide.html', 'utf8');

const regex = /class="([^"]*(?:step|num|badge|box|circle|count)[^"]*)"/gi;
let match;
const classes = new Set();
while ((match = regex.exec(html)) !== null) {
  classes.add(match[1]);
}
console.log('Classes found in solar-guide.html:');
console.log([...classes]);

// Also check lines containing 01, 02, 03 or 1, 2, 3
const lines = html.split('\n');
lines.forEach((l, i) => {
  if (l.includes('step') || l.includes('Step') || l.includes('01') || l.includes('02')) {
    if (l.length < 120) console.log(`${i+1}: ${l.trim()}`);
  }
});
