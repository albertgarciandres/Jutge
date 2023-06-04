from jutge import read

n = read(str)

while n:
    c = 0
    for i in n:
        c += int(i)
   
    print('The sum of the digits of '+ n +' is ' + str(c)+'.')
    n = read(str)
