def calc(a,b,c):
	if c == 1:
		d = a + b
		return d
	elif c == 2:
		return a - b
	elif c == 3:
		return a * b
	elif c == 4:
		return a / b
	else:
		print("nothing")
print("enter two numbers")
a = int(input())
b = int(input())
print("enter 1:add, 2:sub, 3:multiplication, 4:division")
c = int(input())
d = calc(a, b,c)
print(d)
