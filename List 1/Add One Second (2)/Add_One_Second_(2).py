def add1sec(h,m,s):
	'''
	>>> add1sec(0, 1, 2)
	(0, 1, 3)
	>>> add1sec(3, 5, 9)
	(3, 5, 10)
	>>> add1sec(19, 45, 59)
	(19, 46, 0)
	>>> add1sec(12, 59, 59)
	(13, 0, 0)
	'''
	
	if h == 23 and m == 59 and s == 59:
		return (h-23, m-59, s-59)
		
	s = s+1
	if s == 60:
		s = 0
		m = m+1
		if m == 60:
			h = h+1
			m = 0
			return (h,m,s)
		return (h,m,s)
	else:
		return (h,m,s)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
