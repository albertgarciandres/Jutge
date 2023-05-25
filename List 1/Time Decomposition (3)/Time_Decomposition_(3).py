def decompose (n):
	
	'''
	>>> decompose(147)
	(0, 2, 27)
	>>> decompose(3661)
	(1, 1, 1)
	>>> decompose(76234)
	(21, 10, 34)
	'''
	
	s = n % 60
	m = n // 60 % 60
	h = n // 60 // 60
	
	return (h, m, s)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
