import sys

x = float(sys.stdin.readline())
coefficients = sys.stdin.readline().split()

n = 0
result = 0
for c in coefficients:
	c = float(c)
	result += c*(x**n) 
	n += 1

print(format(result, '.4f'))
