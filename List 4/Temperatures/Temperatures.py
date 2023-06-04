from jutge import read

t = read(int)

if t > 30 and t <= 99:
	print("it's hot")
elif t >= 100:
	print("it's hot\nwater would boil")
elif t < 10 and t >= 1:
	print("it's cold")
elif t >= 10 and t <= 30:
	print("it's ok")
elif t <= 0:
	print ("it's cold\nwater would freeze") 
