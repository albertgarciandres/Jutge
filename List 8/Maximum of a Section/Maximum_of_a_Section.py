def find_maximum_value(a, b, sequence):
    # Find the first occurrence of a
    try:
        start_index = sequence.index(a) + 1
    except ValueError:
        print("nonexistent section")
        return

    # Find the first occurrence of b after the first occurrence of a
    try:
        end_index = sequence.index(b, start_index)
    except ValueError:
        print("nonexistent section")
        return

    # Check if there are any numbers between a and b
    if start_index >= end_index:
        print("empty section")
        return

    # Find the maximum value in the section
    maximum_value = max(sequence[start_index:end_index])
    print("maximum is:", maximum_value)


# Read input values
a, b = map(int, input().split())
sequence = list(map(int, input().split()))

# Call the function to find the maximum value in the section
find_maximum_value(a, b, sequence)
