random = [1,4,6,6,8,3,1]
# def removeDuplicate(kuchtoh):
# 	new = []
# 	for i in kuchtoh:
# 		if i not in new:
# 			new.append(i)
# 	return new

# print(removeDuplicate(random))

dicto = {}
for i in random:
	if i in dicto:
		dicto[i] += 1
	else:
		dicto[i] = 1
print(dicto)