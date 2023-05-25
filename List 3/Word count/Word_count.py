def word_count(s):
	'''
	>>> word_count('Qui invenit amicum invenit thesaurum')
	5
	>>> word_count('alea iacta          est')
	3
	>>> word_count('KingKong')
	1
	'''
	
	found_space = False
	counter = 1

	for i in s :
		if i == " " and not found_space:
			found_space = True
			counter += 1
		elif i == " " and found_space:
			continue
		elif i != " ":
			found_space = False
	return counter


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
