class Stack:
	def __init__(self):
		self.stack=[]
	def add(self,dataval):
		if dataval not in self.stack:
			self.stack.append(dataval)
			return True
		else:
			return False
	def remove(self):
		if len(self.stack) <=0:
			print("There are no elements in the stack to remove")
		else:
			return self.stack.pop()

AStack=Stack()
AStack.add('Dom')
AStack.add('Lun')
print(AStack.remove())
AStack.add('Mar')
print(AStack.remove())
print(AStack.remove())
