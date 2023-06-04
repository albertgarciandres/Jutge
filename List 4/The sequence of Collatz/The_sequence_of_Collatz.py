import sys

line = sys.stdin.readline()

while line != '':
# extract ifo from the line
    n = int(line)
# process info appropiately
    c = 0
    while n > 1 :
        if n % 2 == 0 :
            n = n // 2
        else :
            n = (n * 3) + 1
        c = c + 1
    print (c)
# get next line (if any)
    line = sys.stdin.readline()
