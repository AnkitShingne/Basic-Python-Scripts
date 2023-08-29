while True :
    print ('Who are you')
    name = input()
    if name != 'Ankit' :
        continue
    while True :
        print('Hello Ankit. What is your password?')
        password = input()
        if password == 'fis':
            break
    break
print('Access granted')
