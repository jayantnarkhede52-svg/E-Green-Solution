with open('admin/login.html', 'r', encoding='utf-8') as f:
    t = f.read()

t = t.replace('--primary: #2e7d32;', '--primary: #49B99E;')
t = t.replace('--secondary: #fbc02d;', '--secondary: #49B99E;')
t = t.replace('--dark: #121212;', '--dark: #0B0D12;')
t = t.replace('--surface: #1e1e1e;', '--surface: #171B23;')
t = t.replace("font-family: 'Outfit', sans-serif;", "font-family: 'Manrope', 'Inter', sans-serif;")
t = t.replace('rgba(251, 192, 45, 0.4)', 'rgba(73, 185, 158, 0.4)')

with open('admin/login.html', 'w', encoding='utf-8') as f:
    f.write(t)
print('Updated admin/login.html to dark technical tokens!')
