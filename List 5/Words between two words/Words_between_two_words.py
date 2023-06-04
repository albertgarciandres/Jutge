from jutge import read

trobat = False
acabat = False
word = read(str)
counter = 0

while word is not None:
	if word == "beginning":
		trobat = True
	elif word == "end":
		acabat = True
		break
	elif trobat:
		counter += 1
	word = read(str)

if trobat and acabat:
	print(counter)
else:
	print("wrong sequence")
