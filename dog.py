from Animal import Animal

class dog(Animal):
	def __init__(self,age,name,play):
		Animal.__init__(self,age)
		self.name = name
		self.play = play
