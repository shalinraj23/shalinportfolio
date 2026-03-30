import os
import glob

# 1. Create workshop.html based on certifications.html
with open('certifications.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Modify title and headers
content = content.replace('<title>Certifications | Shalin Raj</title>', '<title>Workshops | Shalin Raj</title>')
content = content.replace('<h2 class="section-title">Certifications</h2>', '<h2 class="section-title">Workshops</h2>')

# Modify nav
content = content.replace('<li><a href="certifications.html" class="active">Certifications</a></li>', '<li><a href="certifications.html">Certifications</a></li>')
content = content.replace('<li><a href="achievements.html">Achievements</a></li>', '<li><a href="achievements.html">Achievements</a></li>\n            <li><a href="workshop.html" class="active">Workshops</a></li>')

# We need to replace cert-grid with workshop item
workshop_html = '''<div class="achievement-highlight" style="text-align: center;">
            <h3><i class="fas fa-award" style="color:#fbbf24; margin-right: 15px;"></i> IIT Bombay Workshop Certificate</h3>
            <p style="color: var(--text-muted); font-size: 1.1rem; max-width: 600px; margin: 0 auto 1.5rem;">
                Successfully completed the intensive workshop at IIT Bombay, demonstrating advanced problem-solving capabilities and analytical thinking in a highly competitive environment.
            </p>
            <a href="#" class="btn btn-primary"><i class="fas fa-medal"></i> View Details</a>
        </div>'''

start_grid = content.find('<div class="cert-grid">')
end_grid = content.find('</main>')
if start_grid != -1 and end_grid != -1:
    content = content[:start_grid] + workshop_html + '\n    ' + content[end_grid:]

with open('workshop.html', 'w', encoding='utf-8') as f:
    f.write(content)


# 2. Update all OTHER html files to include workshop in nav
html_files = glob.glob('*.html')
for file in html_files:
    if file == 'workshop.html':
        continue
    with open(file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    target = '<li><a href="achievements.html">Achievements</a></li>'
    if target in html_content:
        html_content = html_content.replace(target, target + '\n            <li><a href="workshop.html">Workshops</a></li>')
    else:
        target_active = '<li><a href="achievements.html" class="active">Achievements</a></li>'
        if target_active in html_content:
            html_content = html_content.replace(target_active, target_active + '\n            <li><a href="workshop.html">Workshops</a></li>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html_content)

# 3. Modify achievements.html to remove the workshop section
try:
    with open('achievements.html', 'r', encoding='utf-8') as f:
        ach_content = f.read()

    start_highlight = ach_content.find('<!-- Premium Highlight -->')
    end_highlight = ach_content.find('<div class="achievement-list">')
    if start_highlight != -1 and end_highlight != -1:
        ach_content = ach_content[:start_highlight] + ach_content[end_highlight:]

    with open('achievements.html', 'w', encoding='utf-8') as f:
        f.write(ach_content)
except FileNotFoundError:
    print("achievements.html not found, skipping.")

print("Workshop section added successfully.")
