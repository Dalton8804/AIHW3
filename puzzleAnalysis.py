from TreeNode import Node



root = Node(value="rrrbggg")

#initializes levels array with level 1 - the root node
levels = [set({root.value})]
print(root.value,end='\n\n')


root.evaluateChildren()
#adds the second level, children of the root node
level2List=set()
level3List=set()
level4List=set()
level5List=set()
for node in root.children:
	node.evaluateChildren()
	level2List.add(node.value)
	for n3 in node.children:
		n3.evaluateChildren()
		level3List.add(n3.value)
		for n4 in n3.children:
			n4.evaluateChildren()
			level4List.add(n4.value)
			for n5 in n4.children:
				n5.evaluateChildren()
				level5List.add(n5.value)

print(levels)
print(level2List)
print(level3List)
print(level4List)
print(level5List)
print(len(level5List))

#adds the third level, grandchildren of the root node
"""tempList=[]
for node in root.children:
	node.evaluateChildren()
	for child in node.children:
		tempList.add(child.value)
levels.add(tempList)"""

