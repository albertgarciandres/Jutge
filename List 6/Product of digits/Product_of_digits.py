from easyinput import read

n = read(int)
c = 1

while n != None:
	a = str(n)
	if len(a) == 1:
		print('The product of the digits of ' + a + ' is ' + a + '.')
	while len(a) > 1:
		c = 1
		for i in a:
			b = int(i)
			c *= b
			d = str(c)
		print('The product of the digits of ' + a + ' is ' + d + '.')
		a = d
	if len(a) == 1:
		print('----------')
		
	c = 1
	n = read(int)
