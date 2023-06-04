from jutge import read

n = read(int)

while n is not None:
	
	for i in range(n):
		
		if n <= 9:
			print(str(n)*n)
		
	n = read(int)
	if n is not None:
		print()
