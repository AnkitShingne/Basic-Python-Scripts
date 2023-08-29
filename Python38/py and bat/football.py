goals = {'Messi': 19,'Ronaldo': 20,'Hazard': 17}
strikers = ['Suarez','Lewandowski','Neymar','Neymar','Ronaldo','Messi']
def football(players, added):

    myDict = dict()
    for i in set(added):
        myDict[i] = added.count(i) 
    
    #print(myDict)
    for j in myDict:
        if j in players:
            players[j]  = players[j] + myDict[j]
        else:
            players[j] = myDict[j]
    
    for k, v in players.items():
        print(str(v) + ' ' + k)
    
    
    a = 0
    for v in players.values():
        a = a + v
    print('Total number of goals:' + ' ' + str(a))
print('Statistics:')
football(goals, strikers )
