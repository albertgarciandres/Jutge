from easyinput import *

word = None
counter = 0

for line in read_many_lines():
    if word is None:
        word = line
        continue

    if word in line:
        counter += 1

print(counter)
