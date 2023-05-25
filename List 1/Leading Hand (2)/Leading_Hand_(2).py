def leading_hand(h,m):
	'''
	>>> leading_hand(22, 51)
	'minute hand'
	>>> leading_hand(21, 45)
	'draw'
	>>> leading_hand(6, 28)
	'hour hand'
	>>> leading_hand(4, 20)
	'draw'
	'''
	if h >= 12:
		h = h - 12
	
	if h == 0 and m == 0:
		return ("draw")
	if h*5 == m: 
		return("draw")
	elif h*5 < m:
		return("minute hand")
	elif h*5 > m:
		return("hour hand")

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
