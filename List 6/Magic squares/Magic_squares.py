from jutge import read

n = read(int)
while n!= None:

	a = []
	d = {}
	for i in range(0, n):
		row = []
		for j in range(0, n):
			x = read(int)
			row.append(x)
			
			if x in d:
				d[x] += 1
			else:
				d[x] = 1
				
		a.append(row)
	
	ok = True
	
	# check all numbers are there just once
	for x in d:
		if x < 1 or x > n*n or d[x] != 1:
			ok = False
			
	# sum first row
	total = 0
	for j in range(0, n):
		total += a[0][j]
	
	# check rows
	for i in range(0, n):
		s = 0
		for j in range(0, n):
			s += a[i][j]
		
		if s != total:
			ok = False

	# check columns
	for j in range(0, n):
		s = 0
		for i in range(0, n):
			s += a[i][j]
		
		if s != total:
			ok = False

	# check main diagonal
	s = 0
	for i in range(0, n):
		s += a[i][i]

	if s != total:
		ok = False

	# check reverse diagonal
	s = 0
	for i in range(0, n):
		s += a[i][n-1-i]

	if s != total:
		ok = False


	if ok:
		print('yes')
	else:
		print('no')
	
	n = read(int)
