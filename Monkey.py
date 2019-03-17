from Animal import Animal
class Monkey(Animal):

	def __init__(self,age,name,tricks):
		Animal.__init__(self,age)
		self.name = name
		self.tricks = tricks
	def run(self):
		return 'I can run'
