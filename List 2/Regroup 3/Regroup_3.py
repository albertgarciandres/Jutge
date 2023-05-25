def regroup(s):
	'''
	>>> regroup('r2b2')
	'rb22'
	>>> regroup('a45tr09pw')
	'atrpw4509'
	>>> regroup('nonumbers')
	'nonumbers'
	>>> regroup('543210')
	'543210'
	'''
	
	let = ''
	num = ''
	
	for n in s:
		
		if n not in ('1234567890'):
			let = let + n
		
		if n in ('1234567890'):
			num = num + n
	
	
	return let + num  


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
