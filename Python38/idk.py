tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(givenList):
	colWidth = [8, 5, 5]
	#for i in range(3):
	#	for j in givenList[i]:
	#		print(j.rjust(8))
	for i in range(len(givenList[0])):
		print()
		for j in range(len(givenList)):
			print(givenList[j][i].rjust(max(colWidth)), end = '')

printTable(tableData)