from Person import Person
from Machine import Machine

class Robot(Person,Machine):
	def __init__(self,age,name,tricks,language,material):
		Person.__init__(self,age,name,tricks,language)
		Machine.__init__(self,material)

avenger = Robot(23,"avenger","turn","English","Iron")
print(avenger.run())