from TreeNode import Node


node = Node(value="rrrbggg")
node.evaluateChildren()
for n1 in node.children:
	n1.evaluateChildren()
	for n2 in n1.children:
		n2.evaluateChildren()
		for n3 in n2.children:
			n3.evaluateChildren()
			for n4 in n3.children:
				n4.evaluateChildren()
				for n5 in n4.children:
					n5.evaluateChildren()
node.printHistory(1)