from Node import Node
import csv
root = Node(value="rrrbggg",cost=0,level=0)

tree = {}

levelValues = {}

levelCount = {0:1}
needToAdd = []
seen = []


def createTree(node):
		tree[node] = node.getChildren()
		count=0
		for node in tree[node]:
			count+=1
			print(str(node.level)+" "+node.value)
			needToAdd.append(node)
		if(node.level in levelCount):
			levelCount[node.level] += count
		else:
			levelCount[node.level] =count

createTree(root)

while (len(needToAdd)>0):
	createTree(needToAdd.pop(0))



for x in tree:
	if ((x.level in levelValues)):
		levelValues[x.level].append(x.value)
	else:
		levelValues[x.level] = [x.value]

# open the file in the write mode
#f = open('test.csv', 'w')
# create the csv writer
#writer = csv.writer(f)

# close the file



print(levelCount)
for x in levelValues:
	print(str(len(levelValues[x]))+" "+str(levelValues[x]))
	# write a row to the csv file
	#writer.writerow(levelValues[x])

#f.close()