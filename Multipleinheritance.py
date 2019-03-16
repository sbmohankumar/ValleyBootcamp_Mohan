#-----Animal.py--------
class Animal:
	def __init__(self, age):
		self.age = age
#-----Monkey.py---------
from Animal import Animal
class Monkey(Animal):

	def __init__(self,age,name,tricks):
		Animal.__init__(self,age)
		self.name = name
		self.tricks = tricks
	def run(self):
		return 'I can run'
#--------dog.py-----------
from Animal import Animal

class dog(Animal):
	def __init__(self,age,name,play):
		Animal.__init__(self,age)
		self.name = name
		self.play = play
#----------Person.py----------
from Monkey import Monkey

class Person(Monkey):

	def __init__(self,age,name,tricks,language):
		Monkey.__init__(self,age,name,tricks)
		self.language = language
#------Student.py------------
from Person import Person

class Student(Person):
	def __init__(self,age,name,tricks,language, subject):
		Person.__init__(self, subject)
		self.subject = subject
#-----------Employee.py-----------------
from Person import Person
class Employee(Person):
	def __init__(self,age,name,tricks,language,company):
		Person.__init__(self, company)
		self.company = company
		
#---------Machine.py-----------------------
class Machine:
	def __init__(self,material):
		self.material = material
#--------Robot.py----------------------------
from Person import Person
from Machine import Machine

class Robot(Person,Machine):
	def __init__(self,age,name,tricks,language,material):
		Person.__init__(self,age,name,tricks,language)
		Machine.__init__(self,material)

avenger = Robot(23,"avenger","turn","English","Iron")
print(avenger.run())

#------------OUTPUT----------------------
#Run robot.py we will get
I CAN RUN
