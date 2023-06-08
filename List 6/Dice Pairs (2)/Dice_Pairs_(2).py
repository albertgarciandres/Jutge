from jutge import read

n = read(int)


while n is not None:
	counter = [0,0,0,0,0,0,0,0,0,0,0,0,0]
	while n != 0:
		counter[n] += 1
		n = read(int)

	for i in range(2,13):
		if counter[i] != 0:
			print(i, ': ', counter[i], sep='')
	print('-----')	
	n = read(int)
