from sys import argv as arguements

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if len(arguements) != 2:

    print("1 arguement required!") 
    exit()

from_filename = arguements[1]
#to_filename = arguements [2]

print("input: " + from_filename)
#print("output: " + to_filename)

from_file = open(from_filename, 'r', encoding='utf8')
#to_file = open(to_filename, 'w', encoding='utf8')

contents = from_file.read()

def analyze(contents):

    length = float(len(contents))

    frequencies = {}

    for letter in ALPHABET:

        frequencies[letter] = 0.0

    for letter in contents:

        frequencies[letter] += 1.0

    ratios = {}

    for letter in ALPHABET: 

        ratios[letter] = frequencies[letter] / length

    return ratios

ratios = analyze(contents)

for letter in ALPHABET:

    print(letter, end=' ')
    print(ratios[letter])

#to_file.write(contents)

from_file.close()
#to_file.close()
