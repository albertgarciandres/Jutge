def count_a(s, stop):
	
	'''
	>>> count_a('naturally', 'u')
	1
	>>> count_a('russian', 't')
	-1
	>>> count_a('adaptation', 'a')
	0
	>>> count_a('adaptation', 'n')
	3
	'''
	
	count = 0
	
	for x in s:
		
		if x == stop:
			return count
		
		elif 'a' == x:
			count = count + 1
			
		
			
	
	return -1
	

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
