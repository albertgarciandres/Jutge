from jutge import read

h = read(int)
m = read(int)
s = read(int)

def add1sec(h,m,s):
	H = h
	M = m
	S = s+1
	
	if S == 60:
		M = m + 1
		S = 0
	
	if M == 60:
		H = h +1
		M = 0
	
	if H == 24:
		H = 0
	
	return(H, M, S)


H, M, S = add1sec(h,m,s)

if H <= 9:
	zh = '0'
else:
	zh = ''

if M <= 9:
	zm = '0'
else:
	zm = ''

if S <= 9:
	zs = '0'
else:
	zs = ''
	

print (zh+str(H)+':'+zm+str(M)+':'+zs+str(S))
