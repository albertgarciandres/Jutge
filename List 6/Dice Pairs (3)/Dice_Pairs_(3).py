from collections import defaultdict

def count_numbers():
    first_input = True

    while True:
        numbers = input().split()

        if not numbers:
            break

        counter = defaultdict(int)

        for num in numbers:
            counter[num] += 1

        if not first_input:
            print('-----')
        else:
            first_input = False

        sorted_counts = sorted(counter.items(), key=lambda x: int(x[0]))

        for num, count in sorted_counts:
            print(f"{num}: {count}")

count_numbers()
