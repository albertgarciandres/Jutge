from easyinput import read
n = read(int)
word = read(str)
dict = {}
found = False

while word is not None and not found:
    if word.islower():
        if word in dict:
            dict[word] += 1
        elif word not in dict:
            dict[word] = 1
        if dict[word] > n:
            print(f'The first word to reach above frequency {n} is "{word}".')
            found = True
    word = read(str)

if not found:
    print(f"No words reach above frequency {n}.")
