from easyinput import read
n, k = read(int, int)
number = read(int)
dict = {}
found = False

while number is not None and not found:
    if number % n == 0:
        if number in dict:
            dict[number] += 1
        else:
            dict[number] = 1
        if dict[number] >= k:
            print(number)
            found = True
    number = read(int)
