const { execSync } = require('child_process');
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const pages = [
  { url: 'http://localhost:5000/journey', name: 'journey_check_top', size: '1440,900' },
  { url: 'http://localhost:5000/journey?p=0.4', name: 'journey_check_p40', size: '1440,900' },
  { url: 'http://localhost:5000/journey', name: 'journey_check_mobile', size: '390,844' },
  { url: 'http://localhost:5000/areas', name: 'areas_check_pc', size: '1440,900' },
  { url: 'http://localhost:5000/areas', name: 'areas_check_mobile', size: '390,844' },
  { url: 'http://localhost:5000/gallery', name: 'gallery_check_pc', size: '1440,900' },
  { url: 'http://localhost:5000/about', name: 'about_check_pc', size: '1440,900' }
];

for (const p of pages) {
  try {
    const outPath = `C:\\Users\\KIIT0001\\.gemini\\antigravity\\brain\\74d70c66-0eaf-40bc-9050-334d323e8cdd\\${p.name}.png`;
    const cmd = `"${chromePath}" --headless --disable-gpu --window-size=${p.size} --screenshot="${outPath}" "${p.url}"`;
    execSync(cmd, { stdio: 'pipe', timeout: 15000 });
    console.log('Captured ' + p.name);
  } catch (e) {
    console.error('Error capturing ' + p.name, e.message);
  }
}
