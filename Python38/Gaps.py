import  re, shutil, os
fis = []
path = 'C:\\python\\python38\\Test'
os.chdir(path)
for folder, subfolders, filenames in os.walk('C:\\python\\python38\\Test'):
    for filename in filenames:
        if filename.startswith('capitals'):
            
            fis.append(filename)
fis.sort()
print(fis)

filenameRegex = re.compile(r'''
^(capitalsquiz)
(\d*)
(.*)$
''', re.VERBOSE)

for files in fis:
    mo = filenameRegex.search(files)
    beforePart = mo.group(1)
    middlePart = mo.group(2)
    afterPart = mo.group(3)
    print(f'File found in {path} is {files}')
    print('Need to rename: ' +  middlePart +  '\n')

newDigitPart = 16
for files in os.listdir(path):
    newFileName = beforePart + str(newDigitPart).zfill(2) + afterPart
    newDigitPart += 1
    source = os.path.join(path, files)
    destination = os.path.join(path, newFileName)
    if newFileName in os.listdir(path):
        print(f'{newFileName} already exists! Skipping...')
        continue
    else:
        print(f'Renaming {files} to {newFileName}')
        shutil.move(source, destination)

print('\nRenaming Process Done!')


