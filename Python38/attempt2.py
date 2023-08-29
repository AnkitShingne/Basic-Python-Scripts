import re
def Fis(axe, a):
    blankRegex = re.compile(r'\'\s*|a*([A-Z]+)\s*|a*\'')
    return(blankRegex.sub(r'\1',axe))
a = 'abc'or'acb'or'bac'or'bca'or'cab'or'cba'
axe = input()
print(Fis(axe, a))
 
