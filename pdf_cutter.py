import PyPDF2
import sys
list=[]
for i in range(3,len(sys.argv)):
    list.append(int(sys.argv[i]))
list.sort(key=int)
#print list
#print len(list)
f1=open(sys.argv[1], 'rb')
r1=PyPDF2.PdfFileReader(f1)
w1=PyPDF2.PdfFileWriter()
j=0
for i in range(r1.numPages):
    #print i
    if i==list[j]:
	if j+1<len(list):
           j=j+1
	continue
    else:
	pages=r1.getPage(i)
	w1.addPage(pages)
final=open(sys.argv[2], 'wb')
w1.write(final)
final.close()

