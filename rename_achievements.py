import os
import glob

# Rename file if it exists
if os.path.exists('achievements.html'):
    os.rename('achievements.html', 'extracurricular.html')

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update links
    content = content.replace('href="achievements.html"', 'href="extracurricular.html"')
    
    # Update link text in nav
    content = content.replace('>Achievements<', '>Extra Curricular Activities<')

    # Update title and header specifically for the new extracurricular page
    if file == 'extracurricular.html':
        content = content.replace('<title>Achievements | Shalin Raj</title>', '<title>Extra Curricular Activities | Shalin Raj</title>')
        content = content.replace('<h2 class="section-title">Milestones & Achievements</h2>', '<h2 class="section-title">Extra Curricular Activities</h2>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Renamed Achievements to Extra Curricular Activities")
