def sum_interval(a,b):
	'''
	>>> sum_interval(5,10)
	45
	>>> sum_interval(1,100)
	5050
	>>> sum_interval(10,20)
	165
	>>> sum_interval(10, 10)
	10
	'''
	total = 0
	
	while a != b:
		total += a
		a = a + 1
		
	return total + b

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
