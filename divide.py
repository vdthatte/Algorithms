
def divide(x,y):
	"""

Using Recursion

	"""

	# Base Case
	if x==0:
		return (0,0)

	# Recursion
	(q,r) = divide((x/2),y)
	
	q = (2*q)
	r = (2*r)
	
	# if x is odd add one to the remainder
	if ((x%2) == 1):
		r = r + 1
	
	# if remainder is greater than y, add one to the quotient and subtract y from remainder
	if (r >= y):
		r = r - y 
		q = q + 1 

	return (q,r)

print divide(8,3)