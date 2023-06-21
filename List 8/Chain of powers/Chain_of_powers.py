def is_power7(n):
    '''
    Requires a non negative integer n.
    Returns True when n is a power of 7
    Returns False when n is not a power of 7
    '''
    if n == 0:
        return False
    while n != 1:
        if n%7 != 0:
            return False
        n = n//7
    return True


   
def short_power7_chains(f, k):
	'''
	>>> short_power7_chains([1, 7, 49, 7*7*7, 2], 3)
	False
	>>> short_power7_chains([1, 7, 49, 7*7*7, 2], 4)
	True
	>>> short_power7_chains([1, 7, 14, 7*7*7, 21, 28], 2)
	True
	>>> short_power7_chains([14, 7], 1)
	True
	>>> short_power7_chains([], 1)
	True
	'''
	
	counter = 0
	posi= 0
    # where p stores the position of the number in the list 			
	for p, num in enumerate(f):
		power = is_power7(num)
		
		if power == True:
			counter = counter + 1
			if counter == 1:
				posi = p
				
		if power != True:
			if counter > k:
				return False
			else:
				counter = 0
				
	if counter > k:
		return False		
	else:
		return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
