def is_univariate_word(s):
	'''
	>>> is_univariate_word('xxXxxxXX')
	True
	>>> is_univariate_word('xyyyyYYY')
	False
	>>> is_univariate_word('y')
	True
	>>> is_univariate_word('yyyyx')
	False
	'''
	
	s = s.lower()
	
	result = True
	
	for n in s:
		
		if n != s[0]:
			result = False
	
	return result
			

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
