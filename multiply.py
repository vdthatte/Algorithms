

def multiply(x,y):

	# Base Case
	if y==0:
		return 0

	# Recursion
	z = multiply(x,y/2)

	# If y is even, return two times y
	if (y%2 == 0):
		return (2*x)
	
	# If y is not even, return the following below
	else:
		return (x+(2*z))


print multiply(5, 5)