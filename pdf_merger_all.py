import PyPDF2
import sys
import os
#merging of pdf files
def merge(argv):
# this list is for storing the pdf files
  pdfs=[]
#this line takes input for-- we have to merge pdfs of "current dir" or "given path dir"
  if sys.argv[1]=="3" :
#this line changes the directory to the given dir
     os.chdir(sys.argv[2])
#this basically loops over all the files in the directory
  for name in os.listdir('.'):
# this line filter only pdf file
    if name.endswith('.pdf'):
#this line add pdf file in the list
	pdfs.append(name)
# sorting the PDF files in ascnding order
  pdfs.sort(key=str.lower)
#this is writer object for final pdf file(merge of all pdf files)
  w1=PyPDF2.PdfFileWriter()
#we are looping over all the pdf files stored in the list
  for i in xrange(len(pdfs)):
#you can print all the pdf files whom merge pdf you are creating or simply comment this line
	  print pdfs[i]
#open the pdf file
          f1=open(pdfs[i], 'rb')
# read the pdf file
	  r1=PyPDF2.PdfFileReader(f1)
#loop over all the pages in the pdf file
	  for j in range(r1.numPages):
		 page=r1.getPage(j)
		 w1.addPage(page)
#create final pdf file 
  final=open(sys.argv[3], 'wb')
#write to final pdf file
  w1.write(final)
#close the final pdf file
  final.close()
#execution starts from here
if sys.argv[1]=="1" :
    merging_of_pdfs(sys.argv)
elif sys.argv[1]=="2" :
    merge(sys.argv)
else :
    merge(sys.argv)
