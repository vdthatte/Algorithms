

def multiply(x,y):
	if y==0:
		return 0
	z = multiply(x,y/2)
	if (y%2 == 0):
		return (2*x)
	else:
		return (x+(2*z))


print multiply(5, 5)