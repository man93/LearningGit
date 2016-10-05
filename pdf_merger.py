import PyPDF2
import sys
#this function merge two pdf files given in the command line
f1=open(sys.argv[1], 'rb')
f2=open(sys.argv[2], 'rb')
r1=PyPDF2.PdfFileReader(f1)
r2=PyPDF2.PdfFileReader(f2)
w1=PyPDF2.PdfFileWriter()
for i in range(r1.numPages):
	pages=r1.getPage(i)
	w1.addPage(pages)
for j in range(r2.numPages):
	pages=r2.getPage(j)
	w1.addPage(pages)
final=open(sys.argv[3], 'wb')
w1.write(final)
final.close()

