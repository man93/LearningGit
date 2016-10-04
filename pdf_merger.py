import PyPDF2
pdf1=open('mozilla.pdf', 'rb')
pdf2=open('Manjul_Amazon.pdf', 'rb')
pdfreader1=PyPDF2.PdfFileReader(pdf1)
pdfreader2=PyPDF2.PdfFileReader(pdf2)
pdfwriter=PyPDF2.PdfFileWriter()
for i in range(pdfreader1.numPages):
     page1=pdfreader1.getPage(i)
     pdfwriter.addPage(page1)
for j in range(pdfreader2.numPages):
    page2=pdfreader2.getPage(j)
    pdfwriter.addPage(page2)
pdfout=open('mergedpdf.pdf', 'wb')
pdfwriter.write(pdfout)
pdfout.close()
pdf1.close()
pdf2.close()
