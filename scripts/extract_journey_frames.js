/**
 * E Green Solution - Journey Video Frame Extractor
 * Converts AI-generated journey video into high-quality JPEG frames,
 * removes/masks the bottom-right Gemini watermark, and generates manifest.json
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const args = process.argv.slice(2);
const videoPath = args[0] ? path.resolve(args[0]) : path.resolve(__dirname, '../Building_web_project_from_scratch_0e5a59ea_1080p.mp4');
const targetFps = parseInt(args[1], 10) || 12; // 12 fps over 14.9s gives 179 frames (super smooth and fast loading)
const outputDir = path.resolve(__dirname, '../assets/journey-frames');

if (!fs.existsSync(videoPath)) {
    console.error(`❌ Video file not found: ${videoPath}`);
    process.exit(1);
}

if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

// Clean old frames
const oldFiles = fs.readdirSync(outputDir);
for (const file of oldFiles) {
    if (file.endsWith('.webp') || file.endsWith('.jpg') || file.endsWith('.png') || file === 'manifest.json') {
        try { fs.unlinkSync(path.join(outputDir, file)); } catch (e) {}
    }
}

console.log(`🎬 Processing Journey Video: ${videoPath}`);
console.log(`🎯 Target Framerate: ${targetFps} fps`);
console.log(`📁 Output Directory: ${outputDir}`);

try {
    // 1. FFmpeg command with watermark removal (delogo at x=1690, y=850, w=90, h=90)
    // Scale to crisp 1600x900 for ultra-fast canvas painting and network performance
    const filter = `fps=${targetFps},scale=1600:-2,delogo=x=1408:y=708:w=76:h=76:show=0`;
    const simpleFilter = `fps=${targetFps},scale=1600:-2`;

    console.log(`⚡ Extracting and optimizing high-definition frames...`);
    let cmd = `ffmpeg -y -i "${videoPath}" -vf "${filter}" -q:v 4 "${path.join(outputDir, 'frame_%04d.jpg')}"`;

    try {
        execSync(cmd, { stdio: 'inherit' });
    } catch (e) {
        console.warn(`⚠️ Delogo filter failed, falling back to simple extraction...`);
        cmd = `ffmpeg -y -i "${videoPath}" -vf "${simpleFilter}" -q:v 4 "${path.join(outputDir, 'frame_%04d.jpg')}"`;
        execSync(cmd, { stdio: 'inherit' });
    }

    // Count generated frames
    const frames = fs.readdirSync(outputDir).filter(f => f.startsWith('frame_') && f.endsWith('.jpg')).sort();
    console.log(`✅ Successfully generated ${frames.length} frames!`);

    // Write manifest
    const manifest = {
        totalFrames: frames.length,
        fps: targetFps,
        format: 'jpg',
        width: 1600,
        height: 900,
        framePattern: '/assets/journey-frames/frame_%04d.jpg',
        frames: frames.map(f => `/assets/journey-frames/${f}`),
        generatedAt: new Date().toISOString()
    };

    fs.writeFileSync(path.join(outputDir, 'manifest.json'), JSON.stringify(manifest, null, 2));
    console.log(`📄 Saved manifest.json (${manifest.totalFrames} frames ready for GSAP scroll scrubber)`);

} catch (err) {
    console.error(`❌ Frame extraction failed:`, err.message);
    process.exit(1);
}
