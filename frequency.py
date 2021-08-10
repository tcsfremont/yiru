import sys

text = ' '.join(sys.argv[1:])
frequencies = {}

for letter in text:

    if letter not in frequencies: 

        frequencies[letter] = 1

    else:

        frequencies[letter] += 1

print(frequencies)
