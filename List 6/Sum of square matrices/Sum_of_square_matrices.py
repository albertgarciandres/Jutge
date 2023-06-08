def sum(a, b) :

	'''
	given two square matrices, returns the sum of them
	'''

	c = []
	n = len(a)

	for i in range(n) :
		row = []
		for j in range(n) :
			row.append(a[i][j] + b[i][j])
		c.append(row)

	return c
