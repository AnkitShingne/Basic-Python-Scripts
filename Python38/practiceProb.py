tableData = [['apples','oranges','cherries','bananas'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]
def printTable():
    colWidth = [0]*len(tableData)
    
    for i in range(0,len(tableData)):
        maxim = 0
        for j in range(0,len(tableData[i])):
            colWidth[i] = len(tableData[i][j])
            if colWidth[i] > maxim:
                maxim = colWidth[i]
            colWidth[i] = maxim
    
    for i in range(0, len(tableData[1])):
        for j in range(0,len(tableData)):
            print(tableData[j][i].rjust(colWidth[j])+" ",end='')
        print()   
printTable()
        
        
            
