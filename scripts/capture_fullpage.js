const { execSync } = require('child_process');
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

const tasks = [
  { url: 'http://localhost:5000/areas', name: 'areas_full_pc', size: '1440,3200' },
  { url: 'http://localhost:5000/areas', name: 'areas_full_mobile', size: '390,3200' },
  { url: 'http://localhost:5000/gallery', name: 'gallery_full_pc', size: '1440,3200' },
  { url: 'http://localhost:5000/journey?p=0.5', name: 'journey_mid_pc', size: '1440,900' },
  { url: 'http://localhost:5000/journey?p=0.85', name: 'journey_end_pc', size: '1440,900' }
];

for (const t of tasks) {
  try {
    const outPath = `C:\\Users\\KIIT0001\\.gemini\\antigravity\\brain\\74d70c66-0eaf-40bc-9050-334d323e8cdd\\${t.name}.png`;
    const cmd = `"${chromePath}" --headless=new --disable-gpu --window-size=${t.size} --screenshot="${outPath}" "${t.url}"`;
    execSync(cmd, { stdio: 'pipe', timeout: 15000 });
    console.log('Done ' + t.name);
  } catch (e) {
    console.error('Error on ' + t.name, e.message);
  }
}
