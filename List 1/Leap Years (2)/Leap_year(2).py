def leapyear(y):
	'''
	>>> leapyear(1999)
	False
	>>> leapyear(1968)
	True
	>>> leapyear(2000)
	True
	>>> leapyear(1800)
	False
	'''
	if (y%100) != 0:
		if (y%4) == 0:
			return (True)
		else:
			return (False)
	else:
		if ((y/100)%4) == 0:
			return (True)
		else:
			return (False) 

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
