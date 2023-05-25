def intersection(a,b,c,d):
	'''
	>>> intersection(1, 5, 3, 7)
	(3, 5)
	>>> intersection(10, 16, 12, 15)
	(12, 15)
	>>> intersection(3, 5, 2, 11)
	(3, 5)
	>>> intersection(1, 4, 4, 6)
	(4, 4)
	'''
	
	p = max (a, c)
	
	q = min (b, d)
	
	return (p, q)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
