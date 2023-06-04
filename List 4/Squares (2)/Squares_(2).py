import sys

line = sys.stdin.readline()

while line != '':
	n = int(line)
	r = 0
	for x in range(0,n):
		t = ''
		for i in range(0,n):
			t = t + str(r)
			r = r + 1
			
			if r > 9:
				r = 0
		print(t)	
	
	
	line = sys.stdin.readline()
	if line != '':
		print()
