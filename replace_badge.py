import os
import glob

directory = r'c:\work\E GREEN WEBSITE'
old_badge = r"https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fegreensolution.in&count_bg=%232E7D32&title_bg=%231A1A1A&icon=&title=Total+Visits&edge_flat=false"
new_badge = r"https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fegreensolution.in&countColor=%232e7d32&bgColor=%231a1a1a&label=VISUAL+COUNT"
old_badge_esc = old_badge.replace('&', '&amp;')

# We also want to replace the standard hits URL that was inserted.
# Just to be safe, we'll replace the encoded ones too.
for filepath in glob.glob(os.path.join(directory, '*.html')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Also replace & encoded as &amp;
    content = content.replace(old_badge, new_badge)
    content = content.replace(old_badge_esc, new_badge)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")
