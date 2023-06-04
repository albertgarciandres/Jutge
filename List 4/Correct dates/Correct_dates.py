from easyinput import read

d = read(int)

while d is not None:

	m = read(int)
	y = read(int)
	
	
	m1 = [1, 3, 5, 7, 8, 10, 12]
	m2 = [2]
	m3 = [4, 6, 9, 11]


	if (d > 31) or (d < 1) or (m > 12) or (m < 1) or (y < 1800) or (y > 9999):
		x = "Incorrect Date"
	elif m in m1 :
		x = "Correct Date"
	elif m in m3 :
		if d < 31 :
			x = "Correct Date"
		else :
			x = "Incorrect Date"
	else :
		if (( y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)) and (d <= 29) :
			x = "Correct Date"
		elif d <= 28 :
			x = "Correct Date"
		else :
			x = "Incorrect Date"

	print(x)

	d = read(int)
	
