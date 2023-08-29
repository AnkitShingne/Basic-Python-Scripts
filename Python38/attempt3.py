import re
def Fis(inp, cut):
    charRegex = re.compile(r'as+(\w)sa+')
    charRegex.sub(r'\1',inp)

cut = 'as' or 'sa'
inp = 'asdjjssassa'
print(Fis(inp, cut))
