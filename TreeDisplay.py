from Node import Node

root = Node(value="rrrbggg",cost=0,level=0)

tree = {}
valueTree = {}

levelCount = {0:1}
needToAdd = []

def createTree(node):
	tree[node] = node.getChildren()
	count=0
	for node in tree[node]:
		count+=1
		needToAdd.append(node)
	if(node.level in levelCount):
		levelCount[node.level] += count
	else:
		levelCount[node.level] =count

createTree(root)

while (len(needToAdd)>0):
	createTree(needToAdd.pop(0))


def pathToGoal(node,arr):
	
	if(node.parent!=None):
		arr = pathToGoal(node.parent,arr)
	arr += " -> "+node.value
	return arr

# Start BFS
visited = []
queue = []

def bfs(visited, tree, node):
	visited.append(node)
	queue.append(node)

	while(queue):
		curr = queue.pop(0)
		if (curr.isGoal()):
			print("\nLevel Found: "+str(curr.level)+" Total Cost: "+str(curr.totalCost)+" State: "+curr.value)
			print("Path from root: "+ str(pathToGoal(curr,"")),end="\n\n")
		for neighbor in tree[curr]:
			if (neighbor not in visited):
				visited.append(neighbor)
				queue.append(neighbor)

bfs(visited, tree, root)
