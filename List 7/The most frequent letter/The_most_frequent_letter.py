from jutge import read

word = read(str)
d = dict()

while word is not None:
	for x in word:
		if x in d and x.islower():
			d[x] += 1
		if x not in d and x.islower():
			d[x] = 1
	word = read(str)

found = False

for i in sorted(d):
	if d[i] == max(d.values()) and not found:
		print(str(i) +' ' + str(max(d.values())))
		found = True
