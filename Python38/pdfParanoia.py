#! python3
# pdfParanoia.py -  Encryptes and decryptes all the pdfs in a folder.

import PyPDF2, sys, os, re
pdfFiles = []
pdfWriter = PyPDF2.PdfFileWriter()
for folders,subfolders,filenames in os.walk('C:\\Python\\Python38'):
	for filename in filenames:
		if filename.endswith('.pdf'):
			pdfFiles.append(filename)
print(pdfFiles)
for file in pdfFiles:
    pdfFileObj = open(file,'rb')
    pdfReader = PyPDF2.PdfFileReader(file)
    for pageNum in range(1,pdfReader.numPages):
    	pageObj = pdfReader.getPage(pageNum)
    	pdfWriter.addPage(pageObj)

    regex = re.compile('.pdf')
    new = regex.sub('',file)
    pdfnew = open( new + '_encrypted.pdf','wb')
    pdfWriter.write(pdfnew)
    pdfWriter.encrypt(sys.argv[1])
    pdfnew.close()
    
    
    

			


			 
					
