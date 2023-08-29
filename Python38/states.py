import pyperclip, re
capitals = pyperclip.paste()
for word in capitals.split():
    print(word)
#CharRegex = re.compile(r'[A-Z][a-z]+{,15}')
#CharRegex.findall(capitals)
