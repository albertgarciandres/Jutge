def correct_date(d,m,y):
	'''
	>>> correct_date(30, 11, 1971)
	True
	>>> correct_date(6, 4, 1971)
	True
	>>> correct_date(4, 8, 2001)
	True
	>>> correct_date(29, 2, 2001)
	False
	>>> correct_date(32, 11, 2005)
	False
	>>> correct_date(30, 11, 2004)
	True
	>>> correct_date(-20, 15, 2000)
	False
	'''
	
	return (m>0 and d>0) and (((m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d <= 31) \
	or ((m == 4 or m == 6 or m == 9 or m == 11) and d <= 30)\
	or ((m == 2 and d <= 28) or ((y % 100 != 0 and y % 4 == 0) or (y / 100 % 4 == 0) and (m == 2 and d <= 29 ))))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
