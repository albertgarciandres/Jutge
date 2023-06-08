from jutge import read, read_line

alphabet = 'abcdefghijklmnopqrstuvwxyz'

code = read(str)

while code != None:
	nl = read(int)

	for i in range(0, nl):
		line = read_line()
		decoded = ''
	
		for x in line:
			if x == '_':
				decoded += ' '
			else:
				pos = code.index(x)
				decoded += alphabet[pos]
		
		print(decoded)

	print()
	
	code = read(str)
