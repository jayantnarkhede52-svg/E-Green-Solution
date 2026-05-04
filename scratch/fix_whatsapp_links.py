import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace wa.me links that don't have target="_blank"
    # This regex looks for <a> tags with wa.me and adds target and rel if missing
    def replacer(match):
        tag = match.group(0)
        if 'target="_blank"' in tag:
            return tag
        # Insert target="_blank" and rel before the closing >
        return tag.replace('>', ' target="_blank" rel="noopener noreferrer">')

    # Match <a> tags containing wa.me
    new_content = re.sub(r'<a[^>]*href="https://wa\.me/[^"]*"[^>]*>', replacer, content)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated WhatsApp links in {filename}")
