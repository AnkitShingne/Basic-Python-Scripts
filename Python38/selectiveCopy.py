import shutil, os 
for foldername, subfolders, filenames in os.walk('E:\\Statistics-Books'):
    print('Copying from %s'%(foldername))
    for filename in filenames:
        if filename.endswith('.pdf'):
            print(filename)
            shutil.copy('E:\\Statistics-Books' +'\\'+ filename,'C:\\delicious')
            continue
        
        
