from jutge import read

n = read(int)

counter = [0,0,0,0,0,0,0,0,0,0,0,0,0]

while n is not None:
	counter[n] += 1
	n = read(int)

for i in range(2,13):
	if counter[i] != 0:
		print(i, ': ', counter[i], sep='')
