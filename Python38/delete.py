import os
for foldername, subfolders, filenames in os.walk('C:\\New folder (2)'):
    for filename in filenames:
        size = os.path.getsize(foldername + '\\' + filename)
        if size > 100000000:
            print(os.path.abspath(foldername + '\\' + filename))
