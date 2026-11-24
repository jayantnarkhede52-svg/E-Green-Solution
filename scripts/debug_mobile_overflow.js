// Check if any package like puppeteer exists or we can use Chrome DevTools Protocol directly over WebSocket or inspect CSS!
const fs = require('fs');
console.log('Checking package.json...');
if (fs.existsSync('package.json')) {
  console.log(fs.readFileSync('package.json', 'utf8'));
}
