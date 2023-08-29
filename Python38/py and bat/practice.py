stuff = {'rope': 1,'torch': 6,'gold coin': 42, 'dagger': 1,'arrow': 12}
def displayInventory(things):
    for k, v in things.items():
        print(str(v) + ' ' + k)

    a = 0
    for v in things.values():
        a = a + v
    print('Total number of items:' + ' ' + str(a))
print('Inventory:')
displayInventory(stuff)


    
        
    
