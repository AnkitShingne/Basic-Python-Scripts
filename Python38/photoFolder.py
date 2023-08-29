#! python3
# photoFolder.py - Finds photo folders

from PIL import Image
import os

for foldername, subfolders, filenames in os.walk('C:\\'):
	numPhotoFiles = 0
	numNonPhotoFiles = 0
	for filename in filenames:
		if (('.png' not in filename) or ('.jpg' not in filename)) :
			numNonPhotoFiles += 1
			continue
		img = Image.open(filename)
		width, height = img.size
		if width > 500 and height > 500:
			numPhotoFiles += 1
		else:
			numNonPhotoFiles += 1
	if numPhotoFiles > numNonPhotoFiles:
		print(os.path.join('C:\\' + foldername))
	else:
		print('No photo folder found.')