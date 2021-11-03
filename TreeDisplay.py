from Node import Node

root = Node(value="rrrbggg", cost=0, level=0)

tree = {}  # for node traversal
levelValues = {}  # for tree display purposes, needed values so legible to human readers
levelCount = {0: 1}  # holds the number of nodes at each level
needToAdd = []  # used as queue to determine next node to evaluate


def createTree(node):
    if not (node in tree):
        tree[node] = node.getChildren()
    count = 0
    for node in tree[node]:
        count += 1
        # print(str(node.level)+" "+node.value)
        needToAdd.append(node)
    if node.level in levelCount:
        levelCount[node.level] += count
    else:
        levelCount[node.level] = count


needToAdd.append(root)

while len(needToAdd) > 0:
    createTree(needToAdd.pop(0))

for x in tree:
    if x.level in levelValues:
        levelValues[x.level].append(x.value)
    else:
        levelValues[x.level] = [x.value]

# open the file in the write mode
# f = open('test.csv', 'w')
# create the csv writer
# writer = csv.writer(f)

# close the file


print(levelCount)
i = 0
for x in levelValues:
    print("Level " + str(i) + ": " + str(levelValues[x]))
    i += 1
# write a row to the csv file
# writer.writerow(levelValues[x])

# f.close()
