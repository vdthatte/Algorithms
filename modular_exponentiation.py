

def modexp(x,y,N):

	if y==0 :
		return 1

	z = modexp(x, y/2, N)
