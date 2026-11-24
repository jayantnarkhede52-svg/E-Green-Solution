const fs = require('fs');

const files = [
  'residential-solar.html',
  'commercial-solar-pune.html',
  'industrial-solar.html',
  'solar-water-heater-pune.html',
  'solar-panel-cleaning-pune.html',
  'solar-amc-pune.html',
  'solar-inverter-repair-pune.html',
  'solar-net-meter-msedcl-pune.html',
  'solar-plant-revamping-repowering.html',
  'solar-repair-maintenance-pune.html',
  'services.html'
];

files.forEach(f => {
  if (!fs.existsSync(f)) return;
  const content = fs.readFileSync(f, 'utf8');
  console.log('=== ' + f + ' ===');
  const h2Matches = [...content.matchAll(/<h2([^>]*)>([\s\S]*?)<\/h2>/g)];
  h2Matches.forEach((m, idx) => {
    const attrs = m[1];
    const text = m[2].replace(/<[^>]+>/g, '').trim().replace(/\s+/g, ' ');
    const pos = m.index;
    const before = content.slice(Math.max(0, pos - 150), pos);
    const hasCenter = before.includes('center') || before.includes('text-center');
    console.log(`  h2[${idx}] (parent center: ${hasCenter}): "${text}" | attrs: ${attrs.trim()}`);
  });
});
