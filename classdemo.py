class Bottle:
	quantity = 100
	shape = 'cylindrical'

	def __init__(self, color, quality, sipper):
		self.color = color
		self.quality = quality
		self.sipper = sipper

	def fill_water(self):
		print('Water for', self.color, 'is changed')

	def change_color(self, new_color):
		print("old color is", self.color)
		self.color = new_color
		print("The color has been changed to ", self.color)

bottle1 = Bottle(color = 'red', quality = 'high', sipper = "True")
bottle2 = Bottle(color = 'blue', quality = 'medium', sipper = "False")

print(bottle1.fill_water)

# print(bottle1.quantity)