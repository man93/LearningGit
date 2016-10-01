import PyPDF2
pdffile1=open('mozilla.pdf', 'rb')
pdffile2=open('Manjul_Amazon.pdf', 'rb')
pdfreader1=PyPDF2.PdfFileReader(pdffile1)
pdfreader2=PyPDF2.PdfFileReader(pdffile2)
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
pdffile1.close()
pdffile2.close()
