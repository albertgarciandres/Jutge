def group_words_by_suffix(words):
    word_groups = {}
    suffixes = set()

    # Split the sequence into words
    word_list = words.split()

    # Iterate over each word
    for word in word_list:
        # Ignore words with less than 3 letters
        if len(word) >= 3:
            # Extract the 3-letter suffix
            suffix = word[-3:]

            # Add the word to the corresponding group
            if suffix not in word_groups:
                word_groups[suffix] = []
            word_groups[suffix].append(word)

            # Add the suffix to the set of suffixes
            suffixes.add(suffix)

    # Sort the suffixes alphabetically
    sorted_suffixes = sorted(suffixes)

    # Generate the output
    output = []
    for suffix in sorted_suffixes:
        words_with_suffix = word_groups[suffix]
        unique_words = sorted(set(words_with_suffix))
        num_words = len(unique_words)
        output.append(f"{num_words} {' '.join(unique_words)}")

    return output


# Read the input sequence of words
input_sequence = input()

# Group the words by suffix and get the output
output = group_words_by_suffix(input_sequence)

# Print the output
for line in output:
    print(line)
