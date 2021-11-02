historyStates = set()
goalFound = False

class Node():
	global historyStates
	# This initialization would have flaws if used by other people
	# 	since me and my partner are the only ones using this it is safe to assume
	# 	all inputs will be accurate and there will be no variation that would cause problems

	# 	A fix for this would be to simply provide errors and catches for the mismatching errors
	def __init__(self,parent=None, value=None, children=None, goalState = None, cost=None):
		if goalState != None and (goalState is True or goalState is False):
			self.goalState = goalState
		else:
			self.goalState = None
		# initialize parent variable for each node
		if parent != None:
			self.parent = parent
			historyStates.add(parent.value)
		else:
			self.parent = None
		# initialize value variable for each node
		if value != None:
			self.value = value
		else:
			self.value = None
		# initialize children variable for each node
		if children != None:
			self.children = children
		else:
			self.children = []
		if cost != None:
			self.cost = cost #CHANGE THIS TO CALCULATE COST AT INTILIZATION TIME (COST = DIFFERENCE IN POSITION OF B, IF 0 THEN 1)
		else: 
			self.cost = None
	def printHistory(self,n):
		if n==0:
			print(historyStates)
		else:
			print(len(historyStates))


	def evaluateChildren(self):
		indxOfB = self.value.index('b')
		if indxOfB==0:
			tmpstr = self.value
			for i in range(1,4):
				tmpstr = list(self.value)
				tmpstr[i],tmpstr[0] = tmpstr[0],tmpstr[i]
				self.children.append(Node(parent=self,value=("".join(tmpstr))))

		if indxOfB==6:
			tmpstr = self.value
			for i in range(5,2,-1):
				tmpstr = list(self.value)
				tmpstr[i],tmpstr[6] = tmpstr[6],tmpstr[i]
				self.children.append(Node(parent=self,value=("".join(tmpstr))))


		if indxOfB==1:
			tmpstr = list(self.value)
			tmpstr[0],tmpstr[1] = tmpstr[1],tmpstr[0]
			self.children.append(Node(parent=self,value=("".join(tmpstr))))
			for i in range(4,1,-1):
				tmpstr = list(self.value)
				tmpstr[i],tmpstr[1] = tmpstr[1],tmpstr[i]
				self.children.append(Node(parent=self,value=("".join(tmpstr))))

		if indxOfB==5:
			tmpstr = list(self.value)
			tmpstr[6],tmpstr[5] = tmpstr[5],tmpstr[6]
			self.children.append(Node(parent=self,value=("".join(tmpstr))))
			for i in range(2,5):
				tmpstr = list(self.value)
				tmpstr[i],tmpstr[5] = tmpstr[5],tmpstr[i]
				self.children.append(Node(parent=self,value=("".join(tmpstr))))


		if indxOfB==2:
			tmpstr = list(self.value)
			for i in range(0,6):
				if i!=2:
					tmpstr = list(self.value)
					tmpstr[i],tmpstr[2] = tmpstr[2],tmpstr[i]
					self.children.append(Node(parent=self,value=("".join(tmpstr))))

		if indxOfB==4:
			tmpstr = list(self.value)
			for i in range(1,7):
				if i!=4:
					tmpstr = list(self.value)
					tmpstr[i],tmpstr[4] = tmpstr[4],tmpstr[i]
					self.children.append(Node(parent=self,value=("".join(tmpstr))))


		if indxOfB==3:
			tmpstr = self.value
			for i in range(0,7):
				if i!=3:
					tmpstr = list(self.value)
					tmpstr[i],tmpstr[3] = tmpstr[3],tmpstr[i]
					self.children.append(Node(parent=self,value=("".join(tmpstr))))
				

	# checkState will check the value of the node given and determine whether that node is a goal state or not
	def checkState(self):
		gCount = 0
		for i in self.value:
			if gCount >= 3:
				self.goalState = True
				goalFound = True
				return True
			if gCount < 3 and i=='g':
				gCount+=1
			elif gCount < 3 and i=='r':
				self.goalState = False
				return False

	# this function will serve to determine if the current node has any children nodes that are goal states
	def checkChildrenNodes(self):
		goalCount=0
		for node in self.children:
			if node.checkState(): 
				goalCount+=1
		return goalCount
