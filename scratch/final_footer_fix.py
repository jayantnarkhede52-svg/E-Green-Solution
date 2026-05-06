import os

def final_footer_fix(directory):
    privacy_link_quick = '    <li><a href="/privacy-policy.html">Privacy Policy</a></li>'
    privacy_link_bottom = '&nbsp; | &nbsp; <a href="/privacy-policy.html" style="color: inherit; text-decoration: none; opacity: 0.8;">Privacy Policy</a>'
    
    for filename in os.listdir(directory):
        if filename.endswith(".html") and filename != "privacy-policy.html":
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 1. Add to Quick Links if not already there in THAT section
            header_pos = content.find('<h3>Quick Links</h3>')
            if header_pos != -1:
                ul_end_pos = content.find('</ul>', header_pos)
                section_content = content[header_pos:ul_end_pos]
                if 'privacy-policy.html' not in section_content:
                    print(f"Adding to Quick Links in {filename}")
                    content = content[:ul_end_pos] + privacy_link_quick + "\n                " + content[ul_end_pos:]
            
            # 2. Add to Bottom Footer if not already there in THAT section
            footer_bottom_pos = content.find('class="container footer-bottom"')
            if footer_bottom_pos != -1:
                footer_end_pos = content.find('</div>', footer_bottom_pos)
                footer_section = content[footer_bottom_pos:footer_end_pos]
                if 'privacy-policy.html' not in footer_section:
                    print(f"Adding to Bottom Footer in {filename}")
                    content = content.replace('All Rights Reserved.', f'All Rights Reserved. {privacy_link_bottom}')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == "__main__":
    target_dir = r"c:\work\E GREEN WEBSITE"
    final_footer_fix(target_dir)
