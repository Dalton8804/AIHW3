from Node import Node

root = Node(value="rrrbggg", cost=0, level=0)

tree = {}  # for node traversal
levelValues = {}  # for tree display purposes, needed values so legible to human readers
levelCount = {0: 1}  # holds the number of nodes at each level
needToAdd = []  # used as queue to determine next node to evaluate


def createLevel(node):
    if not (node in tree):
        tree[node] = node.getChildren()
    count = 0
    for node in tree[node]:
        count += 1
        needToAdd.append(node)
    if node.level in levelCount:
        levelCount[node.level] += count
    else:
        levelCount[node.level] = count


needToAdd.append(root)

while len(needToAdd) > 0:
    createLevel(needToAdd.pop(0))

for x in tree:
    if x.level in levelValues:
        levelValues[x.level].append(x.value)
    else:
        levelValues[x.level] = [x.value]


print(levelCount)
i = 0
for x in levelValues:
    print("Level " + str(i) + ": " + str(levelValues[x]))
    i += 1

for x in tree:
	tmparr= []
	for y in tree[x]:
		tmparr.append(y.value)
	if (len(tmparr) > 0):
		print("Parent at Level "+str(x.level)+" : "+x.value)
		print("Children: "+str(tmparr))


