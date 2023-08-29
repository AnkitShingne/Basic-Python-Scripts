#! python3
# seatingCards.py - Creates images for invitation cards to be distributed out to the guests.

from PIL import Image
guests = open('guests.txt')
which = guests.read()
for name in which:
	