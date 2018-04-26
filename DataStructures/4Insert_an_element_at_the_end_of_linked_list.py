class Node(object):
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
	def insertAtBeginning(self,newdata):
		NewNode=Node(newdata)
		NewNode.nextval=self.headval
		self.headval=NewNode
	def insertAtEnd(self,newdata):
		NewNode=Node(newdata)
		if self.headval is None:
			self.headval=NewNode
			return
		laste=self.headval
		while laste.nextval is not None:
			laste=laste.nextval
		laste.nextval=NewNode
listO=SLinkedList()
listO.headval=Node('Lun')
e2=Node('Mar')
e3=Node('Mie')

listO.headval.nextval=e2
e2.nextval=e3

listO.insertAtBeginning('Dom')
listO.insertAtEnd('Jue')
listO.listPrint()
			
