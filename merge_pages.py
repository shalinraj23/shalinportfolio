import os
import re

ordered_pages = ['skills.html', 'projects.html', 'internship.html', 'certifications.html', 'extracurricular.html', 'workshop.html', 'resume.html', 'contact.html']

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

if 'id="skills"' in index_content:
    print("Already merged.")
else:
    nav_replacements = {
        'href="index.html"': 'href="#home"',
        'href="skills.html"': 'href="#skills"',
        'href="projects.html"': 'href="#projects"',
        'href="internship.html"': 'href="#internship"',
        'href="certifications.html"': 'href="#certifications"',
        'href="extracurricular.html"': 'href="#extracurricular"',
        'href="workshop.html"': 'href="#workshop"',
        'href="resume.html"': 'href="#resume"',
        'href="contact.html"': 'href="#contact"'
    }
    
    index_content = index_content.replace('<section class="landing-section">', '<section id="home" class="landing-section">')
    
    for old, new in nav_replacements.items():
        index_content = index_content.replace(old, new)

    sections_html = ""
    for page in ordered_pages:
        if not os.path.exists(page):
            continue
        with open(page, 'r', encoding='utf-8') as pf:
            p_content = pf.read()
        
        match = re.search(r'<main[^>]*>(.*?)</main>', p_content, re.DOTALL)
        if match:
            inner_html = match.group(1)
            section_id = page.replace('.html', '')
            sections_html += f'\n    <!-- {section_id.upper()} SECTION -->\n'
            sections_html += f'    <section id="{section_id}" class="container section-enter">\n'
            sections_html += inner_html
            sections_html += f'    </section>\n'

    index_content = index_content.replace('</main>', f'</main>\n{sections_html}')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if 'scroll-behavior: smooth' not in css:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write("\nhtml {\n    scroll-behavior: smooth;\n}\n")

print("Merge complete.")
