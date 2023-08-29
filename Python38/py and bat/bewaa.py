spam = ['apples','bananas','tofu','cats']
def fis(roo):
    l = roo[0]
    for i in spam[1:-1]:
        l = l +', ' + i
    return (l + " and " + roo[-1])
print(fis(spam))
    

