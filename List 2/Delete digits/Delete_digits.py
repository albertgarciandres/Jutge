def delete_digits(s):
	'''
	>>> delete_digits('#Pelham 1-2-3#')
	'#Pelham --#'
	>>> delete_digits('7 up')
	' up'
	>>> delete_digits('92920')
	''
	'''
	
	r = ''
	
	for n in s:
		
		if n not in '1234567890':
			r = r+n
	return r


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
