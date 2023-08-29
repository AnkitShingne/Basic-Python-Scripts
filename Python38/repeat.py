#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
os.makedirs('knewLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png' or '.PNG') or filename.endswith('.jpg' or '.JPG') or filename.endswith('.gif' or '.GIF') or filename.endswith('.bmp' or '.BMP')) \
       or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself
    im = Image.open(filename)
    width, height = im.size
    #print(width, height)
    if width > 2*SQUARE_FIT_SIZE and height > 2*SQUARE_FIT_SIZE:
        print(filename)
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        #print('Resizing %s...' % (filename))
        im = im.resize((width, height))
    #print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im.save(os.path.join('knewLogo', filename))
