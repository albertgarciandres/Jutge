def grade(s):
	'''
	>>> grade(4.99)
	'suspens'
	>>> grade(8)
	'notable'
	>>> grade(6.99)
	'aprovat'
	>>> grade(9.5)
	'excel.lent'
	>>> grade(10)
	'MH'
	'''
	
	if s <= 4.99:
		return('suspens')
	elif s <= 6.99:
		return('aprovat')
	elif s <= 8.99:
		return('notable')
	elif s <= 9.99:
		return('excel.lent')
	else:
		return('MH')
	

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
