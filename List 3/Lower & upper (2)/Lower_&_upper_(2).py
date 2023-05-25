def lowupp(info):
	'''
	>>> lowupp('_Hi There!')
	'hi there!'
	>>> lowupp('^Hi There!')
	'HI THERE!'
	>>> lowupp('Hi There!')
	'Hi There!'
	>>> lowupp('')
	''
	'''
	
	
	
	if info == '':
		return ''
	else:
		if info[0] == '_':
			low = info[1:].lower()
			return low
	
		elif info[0] == '^':
			up = info[1:].upper()
			return up
		else:
			return info

	
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
