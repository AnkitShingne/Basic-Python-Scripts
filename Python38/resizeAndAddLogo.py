#! python3
# resizeAndAddLogo.py - Resizes all imaages in current working directory to fit in a 300X300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image 

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size 

os.makedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
	if not (filename.endswith('.png') or filename.endswith('.jpg')) \
	 or filename == LOGO_FILENAME:
	 continue

	im = Image.open(filename)
	width, height = im.size 
	if 