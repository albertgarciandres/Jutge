def slow_pi_approx(n):
	'''
	>>> slow_pi_approx(10)
	3.2323
	>>> slow_pi_approx(100)
	3.1515
	>>> slow_pi_approx(1000)
	3.1426
	'''

	total = 0
	
	for k in range(0,n+1):
		total += ((-1)**k) / (2 * k + 1)
		
		pi = total * 4
	
	return round(pi,4)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
