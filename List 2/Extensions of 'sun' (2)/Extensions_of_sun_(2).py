def is_sun_extension(s):
	'''
	>>> is_sun_extension('sun')
	True
	>>> is_sun_extension('assumption')
	True
	>>> is_sun_extension('assume')
	False
	>>> is_sun_extension('russian')
	False
	>>> is_sun_extension('scouting')
	True
	>>> is_sun_extension('innocuous')
	False
	'''
	
	look = 's'
	
	for n in s:
		
		if n == look:
			
				if look == 's':
					look = 'u'
				elif look == 'u':
					look = 'n'
				elif look == 'n':
					return True
	
	return False



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
