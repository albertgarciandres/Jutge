def vowel_consonant_count(s):
	
	'''
	>>> vowel_consonant_count('SpartacUs')
	(3, 6)
	>>> vowel_consonant_count('KingKong')
	(2, 6)
	'''
	
		
	Vcount = 0
	Ccount = 0
	
	for n in s:
		
		if n in ("AEIOUaeiou"):
			Vcount = Vcount + 1
		else:
			Ccount = Ccount + 1
	
	return (Vcount, Ccount)
	

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
