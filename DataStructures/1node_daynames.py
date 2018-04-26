class daynames:
	def __init__(self,data=None):
		self.data=data
		self.nextval=None
e1=daynames('Jun')
e2=daynames('Mar')
e3=daynames('Mie')
e4=daynames('Jue')

e1.nextval=e2
e2.nextval=e3
e3.nextval=e4
thisval=e1
while thisval:
	print(thisval.data)
	thisval=thisval.nextval

	
