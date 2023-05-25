def sum_interval(a,b,n):
	'''
	>>> sum_interval(5,10,8)
	8
	>>> sum_interval(5,10,3)
	0
	>>> sum_interval(1,100,6)
	510
	>>> sum_interval(10,20,0)
	30
	'''
	total = 0
	while a <= b:
		if str(n) in str(a)[-1]:
			total += a
			a += 1
		else:
			a += 1
			
	return total

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
