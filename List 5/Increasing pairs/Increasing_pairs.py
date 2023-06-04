from jutge import read

nseqs = read(int)

for i in range(nseqs) :
	num = read(int)
	count = 0
	while num != 0 :
		ant = num
		num = read(int)
		if (ant < num) :
			count += 1
	print(count)
