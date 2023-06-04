from jutge import read

num = read(int)


while num is not None :
	result = []
	for i in range(num) :
		n = read(str)
		result.append(n)

	result.reverse()
	result = " ".join(result)
	print(result)
	num = read(int)
