from jutge import read

n = read(int)

s = n % 60

m = n // 60 % 60

h = n // 60 // 60

print(h, m, s)
