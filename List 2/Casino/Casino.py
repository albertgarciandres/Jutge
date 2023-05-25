def buy_tokens(n):
	'''
	>>> buy_tokens(20)
	(0, 5)
	>>> buy_tokens(50)
	(6, 2)
	>>> buy_tokens(39)
	(5, 1)
	'''
	seven = n // 7
	rest = n % 7 
	
	while rest % 4 != 0:
		seven = seven - 1
		rest = rest + 7
		
	return(seven, rest//4)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
