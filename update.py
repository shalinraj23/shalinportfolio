import os
import glob

html_files = glob.glob('*.html')

for file in html_files:
    if file == 'training.html':
        with open(file, 'r', encoding='utf-8') as f:
            intern_content = f.read()

        intern_content = intern_content.replace('<li><a href="training.html">Training</a></li>', '<li><a href="internship.html">Internship</a></li>')
        intern_content = intern_content.replace('<li><a href="training.html" class="active">Training</a></li>', '<li><a href="internship.html" class="active">Internship</a></li>')
        intern_content = intern_content.replace('<title>Training | Shalin Raj</title>', '<title>Internship | Shalin Raj</title>')
        intern_content = intern_content.replace('<h2 class="section-title">Professional Training</h2>', '<h2 class="section-title">Internship Experience</h2>')

        start_idx = intern_content.find('<!-- Training Item 2 -->')
        end_idx = intern_content.find('</div>', start_idx)
        if start_idx != -1 and end_idx != -1:
            intern_content = intern_content[:start_idx] + intern_content[end_idx:]

        with open('internship.html', 'w', encoding='utf-8') as f:
            f.write(intern_content)

    else:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace('<li><a href="training.html">Training</a></li>', '<li><a href="internship.html">Internship</a></li>')
        content = content.replace('<li><a href="training.html" class="active">Training</a></li>', '<li><a href="internship.html" class="active">Internship</a></li>')
        
        if file == 'certifications.html':
            cert_old = """<h3>Google Networking Course</h3>
                <div class="cert-image">
                    <i class="fas fa-certificate"></i>
                </div>
                <a href="#" class="btn btn-secondary btn-sm"><i class="fas fa-external-link-alt"></i> View Certificate</a>"""
            
            cert_new = """<h3>The Bits and Bytes of Computer Networking</h3>
                <div class="cert-image">
                    <i class="fas fa-certificate"></i>
                </div>
                <a href="https://drive.google.com/drive/folders/1mTgeukI4zDH7bwADhkywAtOCjigVVdi6" target="_blank" class="btn btn-secondary btn-sm"><i class="fas fa-external-link-alt"></i> View Certificate</a>"""
            content = content.replace(cert_old, cert_new)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

if os.path.exists('training.html'):
    os.remove('training.html')
print("Update complete")
