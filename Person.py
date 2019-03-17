#------------inheritance---------------------------------
# from Animal import Animal

# class Person(Animal):

# 	def __init__(self,name, age, height,weight,color,job,school,university):
# 		Animal.__init__(self,name,age,height,weight,color) #used to exclude initialization of name,age,height,weight,color again in this program since these are already initialized in animal class
# 		self.job = job
# 		self.school = school
# 		self.university = university
# 		self.friends = []

# 	def get_friends(self):
# 		return self.friends
	
# 	def add_friend(self, fname):
# 		if fname not in self.friends:
# 			self.friends.append(fname)
# 	def age_diff(self, other):
# 		diff = self.age - other.age
# 		print(abs(diff),"year difference")


# mohan = Person('mohan', 24,6,80,'brown','engineer','mss','vtu')
# raghu = Person('raghu', 28,6,80,'brown','engineer','mss','vtu')
# rohan = Person('rohan',32,5,85,'black','doctor','aps','tvu')

# print(mohan.get_friends())
# mohan.add_friend(raghu.name)
# print(mohan.get_friends())
# mohan.add_friend(rohan.name)
# print(mohan.get_friends()[0])
# print(mohan.get_friends()[0][0])

# print(mohan.name)
# print(mohan.speak())
# print(Person.age_diff(mohan,raghu))
#--------------------------------------------------------------------------inheriting from example

from Monkey import Monkey

class Person(Monkey):

	def __init__(self,age,name,tricks,language):
		Monkey.__init__(self,age,name,tricks)
		self.language = language






