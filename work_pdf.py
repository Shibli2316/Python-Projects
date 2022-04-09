import PyPDF2


new_pdf = open('intro.pdf', 'rb')
reading_pdf = PyPDF2.PdfFileReader(new_pdf)
print(reading_pdf.numPages)
pdf_page= reading_pdf.getPage(0)
print(pdf_page.extractText())
new_pdf.close()