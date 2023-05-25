def winner(p,q,r,s):
	'''
	>>> winner(1, 3, 5, 3)
	1
	>>> winner(2, 4, 4, 3)
	2
	>>> winner(1, 3, 2, 3)
	2
	>>> winner(2, 4, 3, 3)
	0
	>>> winner(4, 4, 5, 6)
	0
	'''
	
	P1 = p+q
	P2 = r+s
	
	if P1 > P2 and P1 <= 7:
		return 1
		
	if P1 < P2 and P1 <= 7 and P2 > 7:
		return 1 
	
	if P2 > P1 and P2 <= 7:
		return 2
		
	if P2 < P1 and P2 <= 7 and P1 > 7:
		return 2
	
	else: 
		return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
