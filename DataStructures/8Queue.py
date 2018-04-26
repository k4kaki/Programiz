class Queue:
	def __init__(self):
		self.queue=list()
	def addToQueue(self,dataval):
		if dataval not in self.queue:
			self.queue.insert(0,dataval)
			return True
		return False
	
	def removeFromQueue(self):
		if len(self.queue) > 0:
			return self.queue.pop()
		return("No elements left to to POP")
TheQueue=Queue()
TheQueue.addToQueue('Lun')
TheQueue.addToQueue('Mar')
TheQueue.addToQueue('Mie')
print(TheQueue.removeFromQueue())
print(TheQueue.removeFromQueue())
print(TheQueue.removeFromQueue())
print(TheQueue.removeFromQueue())
print(TheQueue.removeFromQueue())
