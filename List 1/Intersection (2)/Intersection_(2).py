def intersection2(a,b,c,d):
	'''
	>>> intersection2(1, 5, 6, 7)
	(False, 1, 0)
	>>> intersection2(10, 16, 12, 15)
	(True, 12, 15)
	>>> intersection2(3, 5, 2, 11)
	(True, 3, 5)
	>>> intersection2(1, 4, 4, 6)
	(True, 4, 4)
	'''
	
	p = max (a,c)
	
	q = min (b,d)
	
	if b < c:
		return (False, 1, 0)
	elif a > d:
		return (False, 1, 0)
	
	else:
		return (True, p, q)




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
