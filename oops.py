#-----------------Pen example-------------------------------------------------------
# class pen:
# 	length = 20
	
# 	def __init__(self,color, height, diameter):
# 		self.color = color
# 		self.height = height
# 		self.diameter = diameter
	
# 	def write(self):
# 		return "hello world!"
	
# 	def change_filler_color(self,color):
# 		self.color = color


# reynolds = pen('red', 16, 4)
# FC = pen('blue',15,3)
# #print(reynolds.color)
# reynolds.change_filler_color('black')

# print(reynolds.color)
# print(reynolds.height)
# print(reynolds.diameter)
# print(FC.color)
# print(FC.height)
# print(FC.diameter)
# print(self.length)
# print(reynolds.write())
#----------------distance between two points--------------------------------------------
# class Point:
# 	noattempts = 2
	
# 	def __init__(self,x,y):
# 		self.x = x
# 		self.y = y
# 	#Point.noattempts += 1

# 	def __add__(self,other):
# 		return Point(self.x + other.x, self.y + other.y)
	
# 	def __str__(self):
# 		return f'[{self.x},{self.y}]'
	
	# def distance(self,other):
	# 	xsq = (self.x - other.x)**2
	# 	ysq = (self.y - other.y)**2
	# 	return (xsq + ysq)**0.5

# print(Point.noattempts)

# a = Point(2,3)
# b = Point(3,4)
# c = a + b
# print(Point.__add__(a,b))
# print(Point.__str__(a))
#--------------square-------------------------------------------------------------------------------
# a = Point(1,2)
# b = Point(2,3)
# c = Point(3,4)
# d = Point(5,6)

# class square:
# 	def __init__(self,p1,p2,p3,p4):
# 		self.p1 = p1
# 		self.p2 = p2
# 		self.p3 = p3
# 		self.p4 = p4

# 	def area(self):
# 		side = self.p1.distance(self.p2)
# 		return side
# square1 = square(a,b,c,d)
# print(square1.area())
#--------------------OOPS concepts.py---------------------------------------------------------------
class Animal:

	def __init__(self,name, age, height, weight, color):
		self.age = age
		self.name = name
		self.height = height
		self.weight = weight
		self.color = color

	def __str__(self):
		return "animal:" + str(self.name) + ":" + str(self.age)

	def speak(self):
		return "Sounds"

		