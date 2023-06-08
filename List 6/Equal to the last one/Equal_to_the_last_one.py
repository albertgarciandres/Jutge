import sys

dummy = sys.stdin.readline()

line = sys.stdin.readline().strip()
line = line.split()

counter = -1

for i in line:
	if i == line[-1]:
		counter += 1
print(counter)
