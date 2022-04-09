import PyPDF2

# This will only work if you have the file in the directory if not use the write method
new_pdf = open('intro.pdf', 'rb')
reading_pdf = PyPDF2.PdfFileReader(new_pdf)
print(reading_pdf.numPages)
pdf_page= reading_pdf.getPage(0)
print(pdf_page.extractText())
new_pdf.close()
