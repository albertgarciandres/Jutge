def sum_divisors(n):
	'''
	>>> sum_divisors(1)
	0
	>>> sum_divisors(2)
	1
	>>> sum_divisors(6)
	6
	>>> sum_divisors(15)
	9
	>>> sum_divisors(24)
	36
	>>> sum_divisors(28)
	28
	>>> sum_divisors(47)
	1
	'''
	
	counter = 1
	total = 0
	
	while n > counter:
		if n % counter == 0:
			total += counter
			counter += 1
		else:
			counter += 1
	return total




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
