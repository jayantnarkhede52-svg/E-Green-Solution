import os

def update_footer(directory):
    privacy_link_quick = '    <li><a href="/privacy-policy.html">Privacy Policy</a></li>'
    privacy_link_bottom = '&nbsp; | &nbsp; <a href="/privacy-policy.html" style="color: inherit; text-decoration: none; opacity: 0.8;">Privacy Policy</a>'
    
    for filename in os.listdir(directory):
        if filename.endswith(".html") and filename != "privacy-policy.html":
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Target Quick Links section specifically
            if '<h3>Quick Links</h3>' in content and 'privacy-policy.html' not in content:
                print(f"Updating Quick Links in {filename}")
                # Find the first </ul> AFTER <h3>Quick Links</h3>
                header_pos = content.find('<h3>Quick Links</h3>')
                ul_end_pos = content.find('</ul>', header_pos)
                if ul_end_pos != -1:
                    content = content[:ul_end_pos] + privacy_link_quick + "\n                " + content[ul_end_pos:]
            
            # Target Footer Bottom
            if 'All Rights Reserved.' in content and 'privacy-policy.html' not in content:
                print(f"Updating Footer Bottom in {filename}")
                content = content.replace('All Rights Reserved.', f'All Rights Reserved. {privacy_link_bottom}')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == "__main__":
    target_dir = r"c:\work\E GREEN WEBSITE"
    update_footer(target_dir)
