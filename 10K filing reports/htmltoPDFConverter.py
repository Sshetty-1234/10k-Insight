import os
import pdfkit

# Directory containing HTML files
'''
for APPL files: 10K filing reports/APPL
for DELL files: 10K filing reports/DELL

'''
html_dir = 'APPL'

# Output directory for PDF files
pdf_dir = 'APPL_PDF'

if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)


html_files = [f for f in os.listdir(html_dir) if f.endswith('.html')]


for html_file in html_files:
    input_path = os.path.join(html_dir, html_file)
    output_file = os.path.splitext(html_file)[0] + '.pdf'
    output_path = os.path.join(pdf_dir, output_file)
    
 
    pdfkit.from_file(input_path, output_path)
    
    print(f'Converted {html_file} to {output_file}')
