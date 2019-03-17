from Person import Person
class Employee(Person):
	def __init__(self,age,name,tricks,language,company):
		Person.__init__(self, company)
		self.company = company
		