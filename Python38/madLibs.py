import re
madLibs = open('MADLIBS.txt')
fis = madLibs.read()
madLibs.close()

check = re.compile(r'ADJECTIVE|VERB|ADVERB|NOUN')
while True:
    result = check.search(fis)
    if result == None:
        break
    if result.group() == 'ADJECTIVE' or result.group() == 'ADVERB':
        print('Enter an %s'%(result.group().lower()))
    if result.group() == 'NOUN' or result.group() == 'VERB':
        print('Enter a %s'%(result.group().lower()))
    i = input()
    fis = check.sub(i, fis, 1)
print(fis)
output = open('OUTPUT.txt','w')
output.write(fis)
output.close()
