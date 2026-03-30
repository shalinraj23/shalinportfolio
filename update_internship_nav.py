import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace navigation text
    if '>Internship</a>' in content:
        content = content.replace('>Internship</a>', '>Virtual Internship</a>')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Navbar updated in all HTML files.")
