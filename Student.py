from Person import Person

class Student(Person):
	def __init__(self,age,name,tricks,language, subject):
		Person.__init__(self, subject)
		self.subject = subject

