from TreeNode import Node



node = Node(value="rrrbggg")
node.evaluateChildren()
"""for n1 in node.children:

	if (not n1.isGoal()):
		n1.evaluateChildren()
	else:
		print("Goal Found!!" + n1.value)

	for n2 in n1.children:

		if (not n2.isGoal()):
			n2.evaluateChildren()
		else:
			print("Goal Found!!" + n2.value)

		for n3 in n2.children:
			if (not n3.isGoal()):
				n3.evaluateChildren()
			else:
				print("Goal Found!!" + n3.value)

			for n4 in n3.children:

				if (not n4.isGoal()):
					n4.evaluateChildren()
				else:
					print("Goal Found!!" + n4.value)

				for n5 in n4.children:

					if (not n5.isGoal()):
						n5.evaluateChildren()
					else:
						print("Goal Found!!" + n5.value)
						"""

def createLevels(node):
	while (not Node.isGoalFound()):
		node.evaluateChildren()
		for child in node.children:
			createLevels(child)



createLevels(node)
node.printHistory(0)
node.printHistory(1)
print(Node.isGoalFound())
















