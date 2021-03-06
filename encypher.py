from sys import argv as arguements

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 'EOVRTYUQHPASXFNWDKZLJCIBGM'

if len(arguements) != 3:

    print("3 arguents required!") 
    exit()

from_filename = arguements[1]
to_filename = arguements [2]

print("input: " + from_filename)
print("output: " + to_filename)

from_file = open(from_filename, 'r', encoding='utf8')
to_file = open(to_filename, 'w', encoding='utf8')

contents = list(from_file.read())

for index in range(len(contents)):

    letter = contents[index]
    order = ord(letter) - ord('A')

    if order < 0 or order >= len(KEY):

        continue

    cipher_letter = KEY[order]
    contents[index] = cipher_letter

to_file.write(''.join(contents))

from_file.close()
to_file.close()
