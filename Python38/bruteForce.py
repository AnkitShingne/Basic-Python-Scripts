#! python3
# bruteForce.py - Finds password using all words from a text file.

import PyPDF2
alpha = []
dic = open('dictionary.txt')
text = dic.readlines()
for i in range(0,len(text)):
	add = text[i].lower()
	alpha.append(add)
pdf = open('watermark_encrypted.pdf','rb')
PdfReader = PyPDF2.PdfFileReader(pdf)
for word in alpha:
	pas = PdfReader.decrypt(word)
	if pas == 0:
		continue
	if pas == 1:
		print(word)
		fis = word
		break
print(f'{fis} is your password.')
		

