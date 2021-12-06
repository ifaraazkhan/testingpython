from weasyprint import HTML, CSS
css = CSS(string='''
    @page {size: A4; margin: 1cm;} 
    th, td {border: 1px solid black;}
    ''')
HTML('test.html').write_pdf('weasyprint_pdf_report.pdf', stylesheets=[css])
