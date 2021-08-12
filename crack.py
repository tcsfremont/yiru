from sys import argv as arguements
from analyze import analyze

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if len(arguements) != 3:

    print("2 arguents required!") 
    exit()

from_filename = arguements[1]
to_filename = arguements [2]

print("input: " + from_filename)
print("output: " + to_filename)

from_file = open(from_filename, 'r', encoding='utf8')
to_file = open(to_filename, 'w', encoding='utf8')

contents = from_file.read()

to_file.write(contents)

from_file.close()
to_file.close()
