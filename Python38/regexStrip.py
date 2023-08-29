#!python3
#regexStrip.py - Regex Version of strip()

import re

def regexStrip(s, chars = None):
    if chars == None:
        stripLeft = re.compile(r'^\s*')
        stripRight = re.compile(r'\s*$')

        s = re.sub(stripLeft,'',s)
        s = re.sub(stripRight,'',s)

    else:
        stripLeft = re.compile(r'^[' + re.escape(chars) + r']*')
        stripRight = re.compile(r'[' + re.escape(chars) + r']*$')
        s = re.sub(stripLeft,'',s)
        s = re.sub(stripRight,'',s)
    return s
# In output first give your s a string value, then print the function.
    
    
