def calculate(a,b,oper):

	def add(a,b):
		return a + b
	def sub(a,b):
		return a - b
	def mul(a,b):
		return a*b
	def div(a,b):
		return a/b
print("enter two numbers")
a = int(input())
b = int(input())
print("enter which operation")
oper = int(input())

if oper == 1:
	print(f'{a} + f'{b} , add(a,b))
if oper == 2:
	print(f'{a} + f'{b} , sub(a,b))
if oper == 3:
	print(f'{a} + f'{b} , mul(a,b))
if oper == 4:
	print(f'{a} + f'{b} , div(a,b))
d = calculate(a,b,oper)
print(d)

# def calc(a,b,c):
# 	if c == 1:
# 		d = a + b
# 		return d
# 	elif c == 2:
# 		return a - b
# 	elif c == 3:
# 		return a * b
# 	elif c == 4:
# 		return a / b
# 	else:
# 		print("nothing")
