def kth_word(s,k):
	'''
	>>> kth_word('Alea iacta est', 3)
	'est'
	>>> kth_word('Alea iacta est', 1)
	'Alea'
	>>> kth_word('KingKong', 2)
	''
	'''
	space = " "
	found_space = False
	counter = 1
	result = ""

	if  s[0] == space :
		counter = 0

	for i in s :
		if i == space and not found_space :
			found_space = True
			counter += 1
		elif i == space and found_space :
			continue
		else :
			found_space = False
		if counter == k and not found_space :
			result += i
		if counter > k :
			break
	return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
