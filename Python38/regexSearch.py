import re, os
files = os.listdir('C:\\python\\python38\\Test')
text = []
for i in range(0,len(files)):
    if '.txt' in files[i]:
        text.append(files[i])
readRegex = re.compile(r'Alaska')
display = []
for i in range(0,len(text)):
    numberi = open(text[i])
    numbi = numberi.read()
    display.append(readRegex.findall(numbi))
    numberi.close()
print(display)
    

        
