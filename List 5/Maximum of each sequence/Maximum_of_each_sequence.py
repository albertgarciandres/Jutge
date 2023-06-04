from jutge import read

n = read(int)

while n is not None:
	mx = read(int)
	for i in range(0,n-1):
		k = read(int)
		if k > mx:
			mx = k
	print(mx)
	
	n = read(int)
