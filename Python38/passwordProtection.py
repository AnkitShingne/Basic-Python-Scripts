import re
def strongPassword():
  
    lengthRegex = re.compile(r'[a-zA-Z0-9]{8,}')
    leng = lengthRegex.search(password)
    if leng == None:
        return('Your password is too short.')
    uppercaseRegex = re.compile(r'[A-Z]+')
    upp = uppercaseRegex.search(password)
    if upp == None:
        return('Please enter an uppercase character.')
    lowercaseRegex = re.compile(r'[a-z]+')
    low = lowercaseRegex.search(password)
    if low == None:
        return('Please enter a lowercase character.')
    digitRegex = re.compile(r'\d+')
    dig = digitRegex.search(password)
    if dig == None:
        return('Please enter a digit.')
    return('You have a strong password.')
r = ''
while 'You have a strong password.' != r:
    print('Enter your password.') 
    password = input()
    r = strongPassword()
    print(r)

