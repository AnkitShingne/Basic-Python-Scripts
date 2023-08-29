import os, shutil, re
path = 'C:\\python\\python38'
os.chdir(path)
filenameRegex = re.compile(r'''
^(.*?)
(\d{2})
(.*?)$
''', re.VERBOSE)

for files in os.listdir(path):
    mo = filenameRegex.search(files)
    beforePart = mo.group(1)
    middlePart = mo.group(2)
    afterPart = mo.group(3)
    print(f'File found in {path} is {files}')
    print('Need to rename: ' + middlePart + '\n')

newDigitPart = 1
for files in os.listdir(path):
    newFileName = beforePart + str(newDigitPart).zfill(3) + afterPart
    newDigitPart += 1
    source = os.path.join(path, files)
    destination = os.path.join(path, newFileName)
    if newFileName in os.listdir(path):
        print(f'{newFileName}already exists! Skipping...')
        continue
else:
    print(f'Renaming {files} to {newFileName}')
    shutil.move(source, destination)

print('\nRenaming Process Done!')
