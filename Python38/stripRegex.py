import re
def Fis(axe):
    if fax != '':
        charRegex = re.compile(r'(fax)?*(\w+)(fax)?*')
        return(charRegex.sub(r'\2',axe))
    else:
        blankRegex = re.compile(r'\'\s*(\w+)\s*\'')
        return(blankRegex.sub(r'\1',axe))
    
axe = input()
print(Fis(axe))
