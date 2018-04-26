class Node:
	def __init__(self,dataval):
		self.dataval=dataval
		self.nextval=None

class SLinkedList:
	def __init__(self):
		self.headval=None

	def listPrint(self):
		printval=self.headval
		while printval is not None:
			print(printval.dataval)
			printval=printval.nextval
	def insertAtBeginning(self,NewVal):
		NewNode=Node(NewVal)
		NewNode.nextval=self.headval
		self.headval=NewNode
listO=SLinkedList()
listO.headval=Node('Lun')
e2=Node('Mar')
e3=Node('Mie')

listO.headval.nextval=e2
e2.nextval=e3

listO.insertAtBeginning('Dom')
listO.listPrint()
		
